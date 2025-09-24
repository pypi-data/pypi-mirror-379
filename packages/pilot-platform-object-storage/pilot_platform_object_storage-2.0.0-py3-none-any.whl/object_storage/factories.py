# Copyright (C) 2023-2025 Indoc Systems
#
# Contact Indoc Systems for any questions regarding the use of this source code.


from typing import Any

from object_storage.clients import AzureBlobClient
from object_storage.clients import AzureContainerClient
from object_storage.managers import AzureBlobStorageManager
from object_storage.providers.enum import Provider
from object_storage.providers.gcp.bucket_client import GCSBucketClient
from object_storage.providers.gcp.object_client import GCSObjectClient


def get_file_client(provider: Provider | str, sas_url: str, **kwargs: dict[str, str]) -> AzureBlobClient | None:
    if provider == 'azure':
        return AzureBlobClient(blob_sas_url=sas_url)
    else:
        raise ValueError(f"Unknown provider: {provider}")


def get_gcs_object_client(project_id: str, service_json: dict[str, Any]) -> GCSObjectClient:
    """Returns an instance of an file client for GCS and sas url."""
    return GCSObjectClient(project_id=project_id, service_json=service_json)


def get_container_client(provider: Provider | str, sas_url: str, **kwargs: Any) -> AzureContainerClient | None:
    """Returns an instance of an container client for the given provider and sas url."""

    provider = Provider(provider)
    if provider == Provider.AZURE:
        if sas_url is None:
            raise ValueError('sas_url is mandatory to AzureContainerClient')
        return AzureContainerClient(container_sas_url=sas_url)
    return None


def get_gcs_container_client(project_id: str, service_json: dict[str, Any]) -> GCSBucketClient:
    """Returns an instance of an container client for GCS and sas url."""
    return GCSBucketClient(project_id=project_id, service_json=service_json)


def get_manager(provider: Provider | str, connection_string: str | None = None) -> AzureBlobStorageManager | None:
    """Returns an instance of an manager client for the given provider and connection string."""

    provider = Provider(provider)
    if provider == Provider.AZURE:
        if connection_string is None:
            raise ValueError('connection_string is mandatory to AzureBlobClient')
        client = AzureBlobStorageManager(connection_string=connection_string)
    return client


__all__ = [
    'get_file_client',
    'get_gcs_object_client',
    'get_container_client',
    'get_gcs_container_client',
    'get_manager',
]
