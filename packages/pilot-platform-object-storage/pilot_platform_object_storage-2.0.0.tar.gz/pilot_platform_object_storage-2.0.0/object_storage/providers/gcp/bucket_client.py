# Copyright (C) 2025 Indoc Systems
#
# Contact Indoc Systems for any questions regarding the use of this source code.

from __future__ import annotations

import asyncio
import os
from collections.abc import Iterable
from collections.abc import Mapping
from pathlib import Path
from typing import Any

import google.auth
from google.api_core.client_options import ClientOptions
from google.api_core.exceptions import Conflict
from google.api_core.exceptions import NotFound
from google.api_core.exceptions import PreconditionFailed
from google.auth.credentials import AnonymousCredentials
from google.cloud import storage
from google.oauth2.service_account import Credentials


class BucketNotFound(Exception):
    pass


class NotBucketEmpty(Exception):
    pass


class GCSBucketClient:
    """Async Google Cloud Storage client using ONLY Aiogoogle.

    Methods match your Azure client:
      - create_bucket
      - remove_bucket
      - upload_object (bytes)
      - is_bucket_exists
      - is_file_exists
    """

    service_json_path: Path
    SCOPES = ['https://www.googleapis.com/auth/devstorage.read_write']

    def __init__(
        self,
        project_id: str,
        service_json: Mapping[str, Any] | None = None,
    ) -> None:

        self.project_id = project_id

        emulator_url = os.environ.get('GCS_EMULATOR_URL')
        if emulator_url:
            # Use anonymous creds with the GCS emulator
            self._client = storage.Client(
                project=project_id,
                credentials=AnonymousCredentials(),
                client_options=ClientOptions(api_endpoint=emulator_url),
            )
        elif service_json:
            creds = Credentials.from_service_account_info(
                service_json,
                scopes=['https://www.googleapis.com/auth/devstorage.read_write'],
            )
            self._client = storage.Client(project=project_id, credentials=creds)
        else:
            # Fallback: use default creds
            creds, _ = google.auth.default(scopes=self.SCOPES)
            self._client = storage.Client(project=project_id, credentials=creds)

    # ---------------- Bucket ops ----------------

    async def create_bucket(self, bucket_name: str, location: str = 'US', storage_class: str = 'STANDARD') -> None:
        """
        Summary:
            Creates a new bucket in Google Cloud Storage.
        Parameters:
            bucket_name (str): The name of the bucket to create.
            location (Optional[str]): The location where the bucket will be created. Defaults to US.
            storage_class (Optional[str]): The storage class of the bucket. Defaults to STANDARD.
        Returns:
            dict: The response from the Google Cloud Storage API.
        """

        def _create() -> None:
            bucket = self._client.bucket(bucket_name)
            bucket.storage_class = storage_class
            self._client.create_bucket(bucket, location=location)

        await asyncio.to_thread(_create)

    async def delete_bucket(self, bucket_name: str, purge: bool = True) -> None:
        """
        Summary:
            Deletes a bucket in Google Cloud Storage.
        Parameters:
            bucket_name (str): The name of the bucket to delete.
            purge (bool): If True, deletes all objects in the bucket before deleting the bucket itself.
                Defaults to True. Because GCS does not allow deleting non-empty buckets.
        Raises:
            BucketNotFound: If the specified bucket does not exist.
        Returns:
            dict: A dictionary indicating the deletion status.
        """

        def _remove() -> None:
            try:
                bucket = self._client.bucket(bucket_name)
                if purge:
                    blobs = bucket.list_blobs()
                    for blob in blobs:
                        blob.delete()
                bucket.delete()
            except (Conflict, PreconditionFailed):
                raise NotBucketEmpty
            except NotFound:
                raise BucketNotFound

        await asyncio.to_thread(_remove)

    async def is_bucket_exists(self, bucket_name: str) -> bool:
        """
        Summary:
            Checks if a bucket exists in Google Cloud Storage.
        Parameters:
            bucket_name (str): The name of the bucket to check.
        Returns:
            bool: True if the bucket exists, False otherwise.
        """

        def _exists() -> bool:
            bucket = self._client.bucket(bucket_name)
            return bucket.exists(self._client)

        return await asyncio.to_thread(_exists)

    async def list_objects(
        self, bucket_name: str, prefix: str = '', delimiter: str | None = None, page_size: int | None = None
    ) -> list[str]:
        """
        Summary:
            Lists objects in a specified bucket with optional prefix and delimiter.
        Parameters:
            bucket_name (str): The name of the bucket to list objects from.
            prefix (Optional[str]): The prefix to filter objects. Defaults to an empty string.
            delimiter (Optional[str]): The delimiter to use for grouping objects. Defaults to None.
            page_size (Optional[int]): The maximum number of results to return per page. Defaults to None.
        Returns:
            list: A list of object names in the specified bucket.
        """

        def _list() -> list[str]:
            bucket = self._client.bucket(bucket_name)
            blobs_iter: Iterable[storage.Blob] = self._client.list_blobs(
                bucket,
                prefix=prefix or None,
                delimiter=delimiter,
                page_size=page_size,
            )
            return [blob.name for blob in blobs_iter]

        return await asyncio.to_thread(_list)
