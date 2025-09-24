# Pilot Platform Storage Manager

[![Run Tests](https://github.com/PilotDataPlatform/object-storage/actions/workflows/run-tests.yml/badge.svg?branch=develop)](https://github.com/PilotDataPlatform/object-storage/actions/workflows/run-tests.yml)
[![Python](https://img.shields.io/badge/python-3.9-brightgreen.svg)](https://www.python.org/)
[![PyPI](https://img.shields.io/pypi/v/pilot-platform-object-storage.svg)](https://pypi.org/project/pilot-platform-object-storage/)

Provides a simple and flexible Python library for efficient and reliable object storage solutions. Enables direct interaction with multiple object storage APIs, starting with Azure Blob API and with plans to add more in the future

## Getting Started

### Manager
```python
import asyncio
from object_storage.factories import get_manager

connection_string = 'DefaultEndpointsProtocol=https;AccountName=pilot;AccountKey=any;EndpointSuffix=core.windows.net'
azr_manager = get_manager('azure', connection_string)

account_sas = asyncio.run(azr_manager.get_container_sas('test'))
print(blob_sas)
> 'https://pilot.blob.core.windows.net/test/file.txt?sp=rw&st=2023-04-28T15:15:14Z&se=2023-04-28T23:15:14Z&spr=https&sv=2021-12-02&sr=b&sig=account_signature'


blob_sas = asyncio.run(azr_manager.get_blob_sas('test', 'small.txt'))

print(blob_sas)
> 'https://pilot.blob.core.windows.net/test/file.txt?sp=rw&st=2023-04-28T15:15:14Z&se=2023-04-28T23:15:14Z&spr=https&sv=2021-12-02&sr=b&sig=blob_signature'


blobs_list = asyncio.run(azr_manager.list_objects('test'))
print(blobs_list)
> [<class 'azure.storage.blob._models.BlobProperties'>, ...]


blobs_list = asyncio.run(azr_manager.create_container('test'))
```

### File Client
```python
import asyncio
from object_storage.factories import get_file_client

blob_sas_url = 'https://pilot.blob.core.windows.net/test/file.txt?sp=rw&st=2023-04-28T15:15:14Z&se=2023-04-28T23:15:14Z&spr=https&sv=2021-12-02&sr=b&sig=account_signature'
azr_file_client = get_file_client('azure', blob_sas_url)
asyncio.run(azr_file_client.upload_file('./small.txt'))
```

### Container Client
```python
import asyncio
from object_storage.factories import get_container_client

container_sas_url = 'https://pilot.blob.core.windows.net/test?sp=rw&st=2023-04-28T15:15:14Z&se=2023-04-28T23:15:14Z&spr=https&sv=2021-12-02&sr=b&sig=account_signature'
azr_container_client = get_container_client('azure', container_sas_url)
asyncio.run(azr_container_client.upload_file('small.txt', './small.txt'))

```

## Installation & Quick Start
The latest version of the object-storage package is available on [PyPi](https://pypi.org/project/pilot-platform-object-storage/) and can be installed into another service via Pip.

Pip install from PyPi:
```
pip install pilot-platform-object-storage
```

In `pyproject.toml`:
```
pilot-platform-object-storage = "^<VERSION>"
```

Pip install from a local `.whl` file:
```
pip install pilot_platform_object_storage-<VERSION>-py3-none-any.whl
```

## Documentation

API Reference and User Guide available at [pilotdataplatform.github.io/object-storage](https://pilotdataplatform.github.io/object-storage/)

## Contribution

You can contribute the project in following ways:

* Report a bug.
* Suggest a feature.
* Open a pull request for fixing issues or adding functionality. Please consider using [pre-commit](https://pre-commit.com) in this case.
* For general guidelines on how to contribute to the project, please take a look at the [contribution guide](CONTRIBUTING.md).
