"""Load flat indexes into elasticsearch."""


import csv
import json
import logging
import os
import pathlib
import sqlite3
import tempfile
import uuid
from datetime import datetime
from functools import lru_cache
from itertools import islice
from typing import Dict, Iterator, Any, Generator, List

import click
from dateutil.parser import parse
from gen3_tracker.meta.dataframer import LocalFHIRDatabase
import orjson
from opensearchpy import OpenSearch as Elasticsearch
from opensearchpy.exceptions import NotFoundError, OpenSearchException
from opensearchpy.helpers import bulk

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logging.getLogger('elasticsearch').setLevel(logging.WARNING)

DEFAULT_ELASTIC = "http://localhost:9200"

k8s_elastic = os.environ.get('GEN3_ELASTICSEARCH_MASTER_PORT', None)
if k8s_elastic:
    DEFAULT_ELASTIC = f"http://{k8s_elastic.replace('tcp://', '')}"

# TODO - fix me should be gen3.aced-idp.org but we need to coordinate with gitops.json
ES_INDEX_PREFIX = "calypr"


def read_ndjson(path: str) -> Iterator[Dict]:
    """Read ndjson file, load json line by line."""
    with open(path) as jsonfile:
        for l_ in jsonfile.readlines():
            yield json.loads(l_)


def is_integer_dtype(value: Any) -> bool:
    return isinstance(value, int) and value.bit_length() <= 32 and not isinstance(value, bool)

def is_long_dtype(value: Any) -> bool:
    return isinstance(value, int) and value.bit_length() > 32

def is_float_dtype(value: Any) -> bool:
    return isinstance(value, float)

def is_bool_dtype(value: Any) -> bool:
    return isinstance(value, bool)

def is_datetime64_any_dtype(value: Any) -> bool:
    try:
        if not isinstance(value, str):
            raise ValueError('Value is not a string')
        parse(value, ignoretz=True)
        return True
    except (ValueError, OverflowError):
        return False

def is_object_dtype(value: Any) -> bool:
    return isinstance(value, list) or isinstance(value, dict)

def infer_es_field(value: Any, existing_type: str | None = None) -> Dict[str, Any] | None:
    """Infer Elasticsearch field mapping from a value, following provided type rules."""
    if value is None:
        return None
    if is_long_dtype(value):
        return {"type": "long"}
    elif is_integer_dtype(value):
        # No way to know what will be an integer an what will be a
        # long in the future as more datasets are added to the dataframe so declare it a long
        return {"type": "long"}
    elif is_float_dtype(value):
        return {"type": "float"}
    elif is_bool_dtype(value):
        return {"type": "keyword"}
    elif is_datetime64_any_dtype(value):
        return {"type": "keyword"}  # Note: Original code uses keyword, not date
    elif is_object_dtype(value):
        return {"type": "keyword"}  # Lists and dicts mapped to keyword
    elif isinstance(value, str):
        return {"type": "keyword"}
    return None



def write_array_aliases(doc_type, alias, elastic=DEFAULT_ELASTIC, name_space=ES_INDEX_PREFIX):
    """Write the array aliases."""
    # EXPECTED_ALIASES = {
    #     ".kibana_1": {
    #         "aliases": {
    #             ".kibana": {}
    #         }
    #     },
    #     "etl-array-config_0": {
    #         "aliases": {
    #             "etl-array-config": {},
    #             "etl_array-config": {},
    #             "time_2022-08-25T01:44:47.115494": {}
    #         }
    #     },
    #     "etl_0": {
    #         "aliases": {
    #             "etl": {},
    #             "time_2022-08-25T01:44:47.115494": {}
    #         }
    #     },
    #     "file-array-config_0": {
    #         "aliases": {
    #             "file-array-config": {},
    #             "file_array-config": {},
    #             "time_2022-08-25T01:44:47.115494": {}
    #         }
    #     },
    #     "file_0": {
    #         "aliases": {
    #             "file": {},
    #             "time_2022-08-25T01:44:47.115494": {}
    #         }
    #     }
    # }
    return {
        "method": 'POST',
        "url": f'{elastic}/_aliases',
        "json": {
            "actions": [
                {"add": {"index": f"{name_space}_{doc_type}-array-config_0",
                         "alias": f"{name_space}_array-config"}},
                {"add": {"index": f"{name_space}_{doc_type}-array-config_0",
                         "alias": f"{alias}_array-config"}}
            ]}
    }


def write_array_config(doc_type, alias, field_array, elastic=DEFAULT_ELASTIC, name_space=ES_INDEX_PREFIX):
    """Write the array config."""
    return {
        "method": 'PUT',
        "url": f'/{name_space}_{doc_type}-array-config_0/_doc/{alias}',
        "json": {"timestamp": datetime.now().isoformat(), "array": field_array}
    }


def write_alias_config(doc_type, alias, elastic=DEFAULT_ELASTIC, name_space=ES_INDEX_PREFIX):
    """Write the alias config."""
    return {
        "method": 'POST',
        "url": f'{elastic}/_aliases',
        "json": {"actions": [{"add": {"index": f"{name_space}_{doc_type}_0", "alias": alias}}]}
    }


def write_bulk_http(elastic, index, limit, doc_type, generator) -> None:
    """Use efficient method to write to elastic, assumes a)generator is a list of dictionaries b) indices already exist. """
    counter = 0

    def _bulker(generator_, counter_=counter):
        idx_name = f"{index[len(ES_INDEX_PREFIX)+1:-1]}id"
        for dict_ in generator_:
            if limit and counter_ > limit:
                break  # for testing
            yield {
                '_index': index,
                '_op_type': 'index',
                '_source': dict_,
                # use the id from the FHIR object to upsert information
                '_id': dict_[idx_name]
            }
            counter_ += 1
            if counter_ % 10000 == 0:
                logger.info(f"{counter_} records written")
        logger.info(f"{counter_} records written")

    logger.info(f'Writing bulk to {index} limit {limit}.')
    _ = bulk(client=elastic,
             actions=(d for d in _bulker(generator)),
             request_timeout=120,
             max_retries=5)

    return


def processing_generator(base_doc_gen: Generator[Dict, None, None],
                        elastic: Elasticsearch,
                        es_index: str,
                        known_properties: Dict[str, Any],
                        field_array: set,
                        limit: int | None = None) -> Iterator[Dict]:
    """Process documents: update mapping and collect array fields."""
    counter = 0
    for doc in base_doc_gen:
        if limit and counter >= limit:
            break
        new_fields = {}
        for k, v in doc.items():
            if isinstance(v, list):
                field_array.add(k)
            if k not in known_properties:
                field_type = infer_es_field(v, known_properties.get(k, {}).get("type"))
                if field_type:
                    new_fields[k] = field_type
        if new_fields:
            update_body = {"properties": new_fields}
            try:
                elastic.indices.put_mapping(index=es_index, body=update_body)
                known_properties.update(new_fields)
                logger.info(f"Added new fields to {es_index}: {list(new_fields.keys())}")
            except OpenSearchException as e:
                logger.error(f"Failed to update mapping: {str(e)}")
                raise
        yield doc
        counter += 1


def resource_generator(project_id, generator) -> Iterator[Dict]:
    """Render guppy index for a FHIR resource entity."""
    program, project = project_id.split('-')
    for resource in generator:
        resource['project_id'] = project_id
        resource["auth_resource_path"] = f"/programs/{program}/projects/{project}"
        yield resource


@lru_cache(maxsize=1024 * 10)
def fetch_denormalized_patient(connection, patient_id):
    """Retrieve unique conditions and family history"""

    fh_condition = []
    fh_condition_coding = []
    condition = []
    condition_coding = []
    patient = None

    for row in connection.execute('select entity from patient where id = ? limit 1', (patient_id,)):
        patient = orjson.loads(row[0])
        break

    for row in connection.execute('select entity from family_history where patient_id = ? ', (patient_id,)):
        family_history = orjson.loads(row[0])
        for _ in family_history['condition']:
            if _ not in fh_condition:
                fh_condition.append(_)
        for _ in family_history['condition_coding']:
            if _ not in fh_condition_coding:
                fh_condition_coding.append(_)

    for row in connection.execute('select entity from condition where patient_id = ? ', (patient_id,)):
        condition_ = orjson.loads(row[0])
        if condition_['code'] not in condition:
            condition.append(condition_['code'])
            condition_coding.append(condition_['code_coding'])

    return {
        'patient': patient, 'condition': condition, 'condition_coding': condition_coding,
        'fh_condition': fh_condition, 'fh_condition_coding': fh_condition_coding
    }


def setup_aliases(alias, doc_type, elastic, field_array, index):
    """Create the alias to the data index"""
    if not elastic.indices.exists_alias(alias):
        logger.warning(f"Creating alias {alias}.")
        elastic.indices.put_alias(index, alias)
    else:
        logger.info(f"Alias {alias} already exists.")
    # create a configuration index that guppy will read that describes the array fields
    # TODO - find a doc or code reference in guppy that explains how this is used
    array_config_index = f'{ES_INDEX_PREFIX}_{doc_type}-array-config_0'
    try:
        mapping = {
            "mappings": {
                "properties": {
                    "timestamp": {"type": "date"},
                    "array": {"type": "keyword"},
                }
            }
        }
        if not elastic.indices.exists(index=array_config_index):
            logger.warning(f"Creating index {array_config_index}.")
            elastic.indices.create(index=array_config_index, body=mapping)

            elastic.indices.update_aliases(
                {"actions": [{"add": {"index": f"{ES_INDEX_PREFIX}_{doc_type}_0", "alias": alias}}]}
            )
            elastic.indices.update_aliases({
                "actions": [
                    {"add": {"index": f"{ES_INDEX_PREFIX}_{doc_type}-array-config_0",
                             "alias": f"{ES_INDEX_PREFIX}_array-config"}},
                    {"add": {"index": f"{ES_INDEX_PREFIX}_{doc_type}-array-config_0",
                             "alias": f"{doc_type}_array-config"}}
                ]}
            )
            logger.warning(f"Updated aliases {array_config_index}")
        else:
            logger.warning(f"{array_config_index} already exists.")
        elastic.index(index=array_config_index, id=alias,
                      body={"timestamp": datetime.now().isoformat(), "array": field_array},
                      refresh='wait_for')
        logger.warning(f"Populated {array_config_index} field_array {field_array}")

    except Exception as e:
        logger.warning(f"Could not create index. {array_config_index} {str(e)}")
        logger.warning("Continuing to load.")


@click.group('flat')
def cli():
    """Load flat indexes into elasticsearch."""
    pass


def write_flat_file(output_path, index, doc_type, limit, generator):
    """Write the flat model to a file."""
    counter_ = 0
    pathlib.Path(output_path).mkdir(parents=True, exist_ok=True)

    # The +1 and -1 indexing is for the '_' spacer chars
    idx_name = f"{index[len(ES_INDEX_PREFIX)+1:-1]}id"
    with open(f"{output_path}/{doc_type}.ndjson", "wb") as fp:
        for dict_ in generator:
            fp.write(
                orjson.dumps(
                    {
                        'id': dict_[idx_name],
                        'object': dict_,
                        'name': doc_type,
                        'relations': []
                    }
                )
            )
            fp.write(b'\n')

            counter_ += 1
            if counter_ % 10000 == 0:
                logger.info(f"{counter_} records written")
        logger.info(f"{counter_} records written")


@cli.command('denormalize-patient')
@click.option('--input_path', required=True,
              default=None,
              show_default=True,
              help='Path to flattened json'
              )
def _denormalize_patient(input_path):
    denormalize_patient(input_path)


def denormalize_patient(input_path):
    """Gather Patient, FamilyHistory, Condition into sqlite db."""

    path = pathlib.Path(input_path)

    def _load_vertex(file_name):
        """Get the object and patient id"""
        if not (path / file_name).is_file():
            return
        for _ in read_ndjson(path / file_name):
            patient_id = None
            if len(_['relations']) == 1 and _['relations'][0]['dst_name'] == 'Patient':
                patient_id = _['relations'][0]['dst_id']
            _ = _['object']
            _['id'] = _['id']
            if patient_id:
                _['patient_id'] = patient_id
            yield _

    connection = sqlite3.connect('denormalized_patient.sqlite')
    with connection:
        connection.execute('DROP table IF EXISTS patient')
        connection.execute('DROP table IF EXISTS family_history')
        connection.execute('DROP table IF EXISTS condition')
        connection.execute('CREATE TABLE if not exists patient (id PRIMARY KEY, entity Text)')
        connection.execute('CREATE TABLE if not exists family_history (id PRIMARY KEY, patient_id Text, entity Text)')
        connection.execute('CREATE TABLE if not exists condition (id PRIMARY KEY, patient_id Text, entity Text)')
    with connection:
        connection.executemany('insert into patient values (?, ?)',
                               [(entity['id'], orjson.dumps(entity).decode(),) for entity in
                                _load_vertex('Patient.ndjson')])
    with connection:
        connection.executemany('insert into family_history values (?, ?, ?)',
                               [(entity['id'], entity['patient_id'], orjson.dumps(entity).decode(),) for entity in
                                _load_vertex('FamilyMemberHistory.ndjson')])
    with connection:
        connection.executemany('insert into condition values (?, ?, ?)',
                               [(entity['id'], entity['patient_id'], orjson.dumps(entity).decode(),) for entity in
                                _load_vertex('Condition.ndjson')])
    with connection:
        connection.execute('CREATE INDEX if not exists condition_patient_id on condition(patient_id)')
        connection.execute('CREATE INDEX if not exists family_history_patient_id on condition(patient_id)')


def compare_mapping(existing_mapping: Dict[str, Any], new_mapping: Dict[str, Any]) -> Dict[str, Any]:
    """
    Compares an existing Elasticsearch index mapping with a new mapping create update for the index by adding missing fields.

    Args:
        existing_mapping (Dict[str, Any]): The existing mapping.
        new_mapping (Dict[str, Any]): The new mapping to compare against the existing mapping.

    Returns:
        None
    """

    new_properties = new_mapping['mappings']['properties']

    # Existing mapping could have been empty because no observations were provided on previous load, but not files.
    # In this case existing properties on file index wouldn't exist, resulting in a key error.
    if 'properties' in existing_mapping['mappings']:
        existing_properties = existing_mapping['mappings']['properties']
    else:
        existing_properties = {}

    # Find differences and update mapping
    updates = {}
    for field, field_type in new_properties.items():
        if field not in existing_properties:
            updates[field] = field_type

    return updates


def ndjson_file_generator(path):
    """Read ndjson file line by line."""
    with open(path) as f:
        for l_ in f.readlines():
            yield orjson.loads(l_)


@cli.command('load')
@click.option('--input_path', required=True,
              default='META/',
              show_default=True,
              help='Path to flattened json'
              )
@click.option('--project_id', required=True,
              default=None,
              show_default=True,
              help='program-project'
              )
@click.option('--data_type', required=True,
              default='observation',
              type=click.Choice(['observation', 'file'], case_sensitive=False),
              show_default=True,
              help='index to load[observation, file] '
              )
def _load_flat(input_path, project_id, data_type):
    import tempfile

    work_path = tempfile.TemporaryDirectory(delete=False).name
    assert pathlib.Path(work_path).exists(), f"Directory {work_path} does not exist."
    work_path = pathlib.Path(work_path)
    db_path = (work_path / "local_fhir.db")
    db_path.unlink(missing_ok=True)

    db = LocalFHIRDatabase(db_name=db_path)
    db.load_ndjson_from_dir(path=input_path)

    load_flat(project_id=project_id,
              generator=db.flattened_observations(),
              index=data_type,
              limit=None,
              elastic_url=DEFAULT_ELASTIC,
              output_path=None
              )


def load_flat(project_id: str, index: str, generator: Generator[dict, None, None], limit: int | None, elastic_url: str, output_path: str):
    """Loads flattened FHIR data into Elasticsearch database. Replaces tube-lite"""

    if limit:
        limit = int(limit)

    elastic = Elasticsearch([elastic_url], request_timeout=120, max_retries=5)
    assert elastic.ping(), f"Connection to {elastic_url} failed"
    index = index.lower()

    def load_index(elastic: Elasticsearch, output_path: str, es_index: str, alias: str, doc_type: str, limit: int | None):
        if not output_path:
            # Initialize dynamic templates as per original mapping function
            dynamic_templates = [
                {
                    "strings": {
                        "match_mapping_type": "string",
                        "mapping": {
                            "type": "keyword"
                        }
                    }
                }
            ]
            if elastic.indices.exists(index=es_index):
                logger.info(f"Index {es_index} exists.")
                full_mapping = elastic.indices.get_mapping(index=es_index)
                existing_properties = full_mapping[es_index]['mappings'].get('properties', {})
            else:
                logger.info(f"Index {es_index} does not exist.")
                elastic.indices.create(index=es_index, body={"mappings": {"dynamic_templates": dynamic_templates}})
                logger.info(f"Created {es_index}")
                existing_properties = {}

            known_properties = existing_properties.copy()
            field_array = set()

            base_loading_gen = resource_generator(project_id, generator)
            processed_gen = processing_generator(base_loading_gen, elastic, es_index, known_properties, field_array, limit)

            write_bulk_http(elastic=elastic, index=es_index, doc_type=doc_type, limit=limit,
                            generator=processed_gen)

            field_array = list(field_array)
            setup_aliases(alias, doc_type, elastic, field_array, es_index)

        else:
            # write file path
            loading_generator = resource_generator(project_id, generator)
            write_flat_file(output_path=output_path, index=es_index, doc_type=doc_type, limit=limit,
                            generator=loading_generator)

    load_index(elastic=elastic, output_path=output_path, es_index=f"{ES_INDEX_PREFIX}_{index}_0",
               alias=index, doc_type=index, limit=limit)

def chunk(arr_range, arr_size):
    """Iterate in chunks."""
    arr_range = iter(arr_range)
    return iter(lambda: tuple(islice(arr_range, arr_size)), ())


@cli.command('counts')
@click.option('--project_id', required=True,
              default=None,
              show_default=True,
              help='program-project'
              )
def _counts(project_id):
    counts(project_id)


def counts(project_id):
    """Count the number of patients, observations, and files."""
    elastic = Elasticsearch([DEFAULT_ELASTIC], request_timeout=120, max_retries=5)
    program, project = project_id.split('-')
    assert program, "program is required"
    assert project, "project is required"
    query = {
        "query": {
            "match": {
                "auth_resource_path": f"/programs/{program}/projects/{project}"
            }
        }
    }
    for index in ['observation', 'file']:
        # index = f"{ES_INDEX_PREFIX}_{index}_0"
        print(index, elastic.count(index=index, body=query)['count'])


@cli.command('rm')
@click.option('--project_id', required=True,
              default=None,
              show_default=True,
              help='program-project'
              )
@click.option('--index', required=True,
              default=None,
              show_default=True,
              help='one of observation, file'
              )
def _delete(project_id, index):
    delete(project_id, index)


def delete(project_id, index):
    """Delete items from elastic index for project_id."""
    elastic = Elasticsearch([DEFAULT_ELASTIC], request_timeout=120, max_retries=5)
    assert project_id, "project_id is required"
    program, project = project_id.split('-')
    assert program, "program is required"
    assert project, "project is required"
    assert index, "index is required"
    query = {
        "query": {
            "match": {
                "auth_resource_path": f"/programs/{program}/projects/{project}"
            }
        }
    }
    print("deleting, waiting up to 5 min. for response")
    try:
        print(index, elastic.delete_by_query(index=index, body=query, timeout=300))
    except NotFoundError:
        return


if __name__ == '__main__':
    cli()
