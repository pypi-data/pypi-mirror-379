#
# Copyright 2022 Benjamin Kiessling
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
# or implied. See the License for the specific language governing
# permissions and limitations under the License.
"""
kraken.ketos.repo
~~~~~~~~~~~~~~~~~

Command line driver for publishing models to the model repository.
"""
import re
import logging

import click

from pathlib import Path
from difflib import get_close_matches

from .util import message

logging.captureWarnings(True)
logger = logging.getLogger('kraken')


def _validate_script(script: str) -> str:
    from htrmopo.util import _iso15924
    if script not in _iso15924:
        return get_close_matches(script, _iso15924.keys())
    return script


def _validate_language(language: str) -> str:
    from htrmopo.util import _iso639_3
    if language not in _iso639_3:
        return get_close_matches(language, _iso639_3.keys())
    return language


def _validate_license(license: str) -> str:
    from htrmopo.util import _licenses
    if license not in _licenses:
        return get_close_matches(license, _licenses.keys())
    return license


def _get_field_list(name,
                    validation_fn=lambda x: x,
                    required: bool = False):
    values = []
    while True:
        value = click.prompt(name, default='')
        if value:
            if (cand := validation_fn(value)) == value:
                values.append(value)
            else:
                message(f'Not a valid {name} value. Did you mean {cand}?')
        else:
            if click.confirm(f'All `{name}` values added?'):
                if required and not values:
                    message(f'`{name}` is a required field.')
                    continue
                else:
                    break
            else:
                continue
    return values


@click.command('publish')
@click.pass_context
@click.option('-i', '--metadata', show_default=True,
              type=click.File(mode='r', lazy=True), help='Model card file for the model.')
@click.option('-a', '--access-token', prompt=True, help='Zenodo access token')
@click.option('-d', '--doi', help='DOI of an existing record to update')
@click.option('-p', '--private/--public', default=False, help='Disables Zenodo '
              'community inclusion request. Allows upload of models that will not show '
              'up on `kraken list` output')
@click.argument('model', nargs=1, type=click.Path(exists=False, readable=True, dir_okay=False))
def publish(ctx, metadata, access_token, doi, private, model):
    """
    Publishes a model on the zenodo model repository.
    """
    import json
    import yaml
    import tempfile

    from htrmopo import publish_model, update_model

    from kraken.lib.vgsl import TorchVGSLModel
    from kraken.lib.progress import KrakenDownloadProgressBar

    pub_fn = publish_model

    _yaml_delim = r'(?:---|\+\+\+)'
    _yaml = r'(.*?)'
    _content = r'\s*(.+)$'
    _re_pattern = r'^\s*' + _yaml_delim + _yaml + _yaml_delim + _content
    _yaml_regex = re.compile(_re_pattern, re.S | re.M)

    nn = TorchVGSLModel.load_model(model)

    frontmatter = {}
    # construct metadata if none is given
    if metadata:
        frontmatter, content = _yaml_regex.match(metadata.read()).groups()
        frontmatter = yaml.safe_load(frontmatter)
    else:
        frontmatter['summary'] = click.prompt('summary')
        content = click.edit('Write long form description (training data, transcription standards) of the model in markdown format here')

        creators = []
        message('To stop adding authors, leave the author name field empty.')
        while True:
            author = click.prompt('author name', default='')
            if author:
                creators.append({'name': author})
            else:
                if click.confirm('All authors added?'):
                    break
                else:
                    continue
            affiliation = click.prompt('affiliation', default='')
            orcid = click.prompt('orcid', default='')
            if affiliation is not None:
                creators[-1]['affiliation'] = affiliation
            if orcid is not None:
                creators[-1]['orcid'] = orcid
        if not creators:
            raise click.UsageError('The `authors` field is obligatory. Aborting')

        frontmatter['authors'] = creators
        while True:
            license = click.prompt('license')
            if (lic := _validate_license(license)) == license:
                frontmatter['license'] = license
                break
            else:
                message(f'Not a valid license identifier. Did you mean {lic}?')

        message('To stop adding values to the following fields, enter an empty field.')

        frontmatter['language'] = _get_field_list('language', _validate_language, required=True)
        frontmatter['script'] = _get_field_list('script', _validate_script, required=True)

        if len(tags := _get_field_list('tag')):
            frontmatter['tags'] = tags + ['kraken_pytorch']
        if len(datasets := _get_field_list('dataset URL')):
            frontmatter['datasets'] = datasets
        if len(base_model := _get_field_list('base model URL')):
            frontmatter['base_model'] = base_model

    software_hints = ['kind=vgsl']

    # take last metrics field, falling back to accuracy field in model metadata
    if nn.model_type == 'recognition':
        metrics = {}
        if len(nn.user_metadata.get('metrics', '')):
            if (val_accuracy := nn.user_metadata['metrics'][-1][1].get('val_accuracy', None)) is not None:
                metrics['cer'] = 100 - (val_accuracy * 100)
            if (val_word_accuracy := nn.user_metadata['metrics'][-1][1].get('val_word_accuracy', None)) is not None:
                metrics['wer'] = 100 - (val_word_accuracy * 100)
        elif (accuracy := nn.user_metadata.get('accuracy', None)) is not None:
            metrics['cer'] = 100 - accuracy
        frontmatter['metrics'] = metrics

        # some recognition-specific software hints and metrics
        software_hints.extend([f'seg_type={nn.seg_type}', f'one_channel_mode={nn.one_channel_mode}', f'legacy_polygons={nn.user_metadata["legacy_polygons"]}'])

    frontmatter['software_hints'] = software_hints

    frontmatter['software_name'] = 'kraken'
    frontmatter['model_type'] = [nn.model_type]

    # build temporary directory
    with tempfile.TemporaryDirectory() as tmpdir, KrakenDownloadProgressBar() as progress:
        upload_task = progress.add_task('Uploading', total=0, visible=True if not ctx.meta['verbose'] else False)

        model = Path(model).resolve()
        tmpdir = Path(tmpdir)
        (tmpdir / model.name).resolve().symlink_to(model)
        if nn.model_type == 'recognition':
            # v0 metadata only supports recognition models
            v0_metadata = {
                'summary': frontmatter['summary'],
                'description': content,
                'license': frontmatter['license'],
                'script': frontmatter['script'],
                'name': model.name,
                'graphemes': [char for char in ''.join(nn.codec.c2l.keys())]
            }
            if frontmatter['metrics']:
                v0_metadata['accuracy'] = 100 - metrics['cer']
            with open(tmpdir / 'metadata.json', 'w') as fo:
                json.dump(v0_metadata, fo)
        kwargs = {'model': tmpdir,
                  'model_card': f'---\n{yaml.dump(frontmatter)}---\n{content}',
                  'access_token': access_token,
                  'callback': lambda total, advance: progress.update(upload_task, total=total, advance=advance),
                  'private': private}
        if doi:
            pub_fn = update_model
            kwargs['model_id'] = doi
        oid = pub_fn(**kwargs)
    message(f'model PID: {oid}')
