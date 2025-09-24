# Copyright (C) 2025 Indoc Systems
#
# Contact Indoc Systems for any questions regarding the use of this source code.

from __future__ import annotations

import asyncio
import io
import os
from collections.abc import Mapping
from datetime import timedelta
from typing import Any
from urllib.parse import quote

import google.auth
from google.api_core.client_options import ClientOptions
from google.auth.credentials import AnonymousCredentials
from google.auth.transport.requests import AuthorizedSession
from google.cloud import storage
from google.oauth2.service_account import Credentials

from object_storage.providers.gcp.model import VersionNotFound


class GCSObjectClient:
    """
    Summary:
        Async Google Cloud Storage client using google-cloud-storage with asyncio.to_thread.
        Methods match your Azure client:
            - upload_object
            - is_file_exists
            - generate_resumable_session_uri
            - get_presigned_download_url
            - list_uploaded_chunks_with_sizes
            - download_object
            - copy_object
            - delete_object
            - restore_object
    """

    SCOPES = ['https://www.googleapis.com/auth/devstorage.read_write']

    def __init__(self, project_id: str, service_json: Mapping[str, Any] | None = None) -> None:
        self.project_id = project_id

        emulator_url = os.environ.get('GCS_EMULATOR_URL')
        if emulator_url:
            self._client = storage.Client(
                project=project_id,
                credentials=AnonymousCredentials(),
                client_options=ClientOptions(api_endpoint=emulator_url),
            )
        elif service_json:
            creds = Credentials.from_service_account_info(service_json, scopes=self.SCOPES)
            self._client = storage.Client(project=project_id, credentials=creds)

        # Fallback: use default creds
        else:
            creds, _ = google.auth.default(scopes=self.SCOPES)
            self._client = storage.Client(project=project_id, credentials=creds)

    def _get_bucket(self, bucket: str) -> storage.Bucket:
        return self._client.bucket(bucket)

    def _get_blob(self, bucket: str, object_name: str) -> storage.Blob:
        return self._get_bucket(bucket).blob(object_name)

    def _authed(self) -> AuthorizedSession:
        # authenticated session for direct HTTP calls
        return AuthorizedSession(self._client._credentials)

    def _part_object_name(self, final_key: str, upload_id: str, chunk_number: int) -> str:
        # Temporary object path for each chunk in google starts with 'multipart/'
        return f"multipart/{upload_id}/{final_key}/part-{chunk_number:06d}"

    # Object related methods

    async def is_file_exists(self, bucket: str, object_name: str) -> bool:
        """
        Summary:
            Check if an object exists in the specified bucket.
        Parameters:
            bucket (str): The name of the bucket.
            object_name (str): The name of the object to check.
        Returns:
            bool: True if the object exists, False otherwise.
        """

        def _exists() -> bool:
            return self._get_blob(bucket, object_name).exists()

        return await asyncio.to_thread(_exists)

    async def upload_object(
        self,
        bucket: str,
        object_name: str,
        data: bytes,
        content_type: str | None = None,
    ) -> int:
        """
        Summary:
            Single-shot upload of an object.
        Parameters:
            bucket (str): The name of the bucket to upload to.
            object_name (str): The name of the object to create.
            data (bytes): The data to upload.
            content_type (str | None): The content type of the object.
        Returns:
            int: The generation number of the uploaded object.
        """

        def _upload() -> int:
            blob = self._get_blob(bucket, object_name)
            blob.upload_from_string(
                data,
                content_type=content_type,
            )
            blob.reload()  # get generation
            return int(blob.generation)

        return await asyncio.to_thread(_upload)

    async def get_resumable_session_uri(
        self,
        bucket: str,
        final_key: str,
        total_size: int,
        current_crc32c: str,
        current_md5: str | None = None,  # if user wants MD5 validation
        *,
        content_type: str = 'application/octet-stream',
        prevent_overwrite: bool = True,
    ) -> str:
        """
        Summary:
            Generate a resumable upload session URI for uploading files.
        Parameters:
            bucket (str): The name of the bucket.
            final_key (str): The final object key.
            total_size (int): The total size of the object to be uploaded.
            current_crc32c (str): The CRC32C checksum of the current data.
            current_md5 (str | None): The MD5 checksum of the current data, if available.
            content_type (str): The content type of the object.
            prevent_overwrite (bool): If True, the upload will fail if the object already exists.
        Returns:
            str: The resumable upload session URI.
        """
        bucket_ref = self._get_bucket(bucket)
        blob = bucket_ref.blob(final_key)

        # Put checksums on the object resource (enforced at final commit)
        blob.crc32c = current_crc32c
        if current_md5:
            blob.md5_hash = current_md5

        # Preconditions: only create if object does not exist
        if_generation_match = 0 if prevent_overwrite else None

        # Create session URI
        session_uri = await asyncio.to_thread(
            blob.create_resumable_upload_session,
            content_type=content_type,
            size=total_size,
            if_generation_match=if_generation_match,
        )

        return session_uri

    async def get_presigned_download_url(
        self,
        bucket: str,
        object_name: str,
        expires: int = 15 * 60,
    ) -> dict[str, Any]:
        """
        Summary:
            Generate a presigned URL for downloading an object.
        Parameters:
            bucket (str): The name of the bucket.
            object_name (str): The name of the object to download.
            expires (int): Expiration time in seconds for the signed URL.
        Returns:
            dict: A dictionary containing the signed URL and required headers.
        """

        bucket_ref = self._get_bucket(bucket)
        blob = bucket_ref.blob(object_name)
        headers = {'x-goog-content-sha256': 'UNSIGNED-PAYLOAD'}
        url = await asyncio.to_thread(
            blob.generate_signed_url,
            version='v4',
            expiration=timedelta(seconds=expires),
            method='GET',
            headers=headers,
        )
        return {'url': url, 'method': 'GET', 'requiredHeaders': headers}

    async def list_uploaded_chunks_with_sizes(self, bucket: str, final_key: str, upload_id: str) -> dict[int, int]:
        """
        Summary:
            List previously uploaded chunks for a multipart upload session.
        Parameters:
            bucket (str): The name of the bucket.
            final_key (str): The final object key.
            upload_id (str): The upload session ID.
        Returns:
            dict[int, int]: A dictionary mapping chunk numbers to their sizes in bytes.
        """

        def _list() -> dict[int, int]:
            prefix = f"multipart/{upload_id}/{final_key}/"
            out: dict[int, int] = {}
            for b in self._client.list_blobs(bucket, prefix=prefix):
                leaf = b.name.rsplit('/', 1)[-1]  # e.g., part-000037
                if leaf.startswith('part-'):
                    num = int(leaf.split('-')[-1])
                    out[num] = int(b.size or 0)
            return out

        return await asyncio.to_thread(_list)

    async def download_object(
        self,
        bucket: str,
        object_name: str,
    ) -> bytes | None:
        """
        Summary:
            Download an object and return its bytes.
        Parameters:
            bucket (str): The name of the bucket containing the object.
            object_name (str): The name of the object to download.
        Returns:
            bytes | None: The content of the object as bytes, or None if the object does not exist.
        """

        def _download() -> bytes | None:
            blob = self._get_blob(bucket, object_name)
            buf = io.BytesIO()
            blob.download_to_file(buf)
            return buf.getvalue()

        return await asyncio.to_thread(_download)

    async def copy_object(
        self,
        src_bucket: str,
        src_object: str,
        dst_bucket: str,
        dst_object: str | None = None,
    ) -> tuple[str, str, int]:
        """
        Summary:
            Copy an object to another bucket.
        Parameters:
            src_bucket (str): The name of the source bucket.
            src_object (str): The name of the source object.
            dst_bucket (str): The name of the destination bucket.
            dst_object (str): The name of the destination object
        Returns:
            tuple: (destination bucket name, destination object name, new generation number)

        """

        def _copy() -> tuple[str, str, int]:
            dst_name = dst_object or src_object
            src_blob = self._get_blob(src_bucket, src_object)

            dst_bucket_obj = self._get_bucket(dst_bucket)
            new_blob = dst_bucket_obj.copy_blob(src_blob, dst_bucket_obj, dst_name)

            new_blob.reload()
            return dst_bucket, dst_name, int(new_blob.generation)

        return await asyncio.to_thread(_copy)

    async def delete_object(
        self,
        bucket: str,
        object_name: str,
    ) -> None:
        """
        Summary:
            Delete an object. This is a soft-delete if the bucket has versioning enabled.
        Parameters:
            bucket (str): The name of the bucket containing the object.
            object_name (str): The name of the object to delete.
        Returns:
            None
        """

        def _delete() -> None:
            blob = self._get_blob(bucket, object_name)
            try:
                blob.delete()
            except Exception:
                raise

        await asyncio.to_thread(_delete)

    async def restore_object(
        self,
        bucket: str,
        object_name: str,
    ) -> int:
        """
        Summary:
            Restore the latest soft-deleted version of an object. Bucket must have versioning enabled.
        Parameters:
            bucket (str): The name of the bucket containing the object.
            object_name (str): The name of the object to restore.
        Returns:
            int: The generation number of the restored object.
        """

        def _restore() -> int:
            bucket_ref = self._get_bucket(bucket)
            soft_delete_versions = list(self._client.list_blobs(bucket_ref, prefix=object_name, soft_deleted=True))
            if not soft_delete_versions:
                raise VersionNotFound(f"No soft-deleted versions found for {object_name!r}")
            soft_delete_versions.sort(key=lambda b: (getattr(b, 'soft_delete_time', None), b.generation), reverse=True)
            latest = soft_delete_versions[0]
            gen = int(latest.generation)

            # directly call the endpoint since there is not a library method for this
            authed = self._authed()
            url = (
                'https://storage.googleapis.com/storage/v1'
                f"/b/{bucket}/o/{quote(object_name, safe='')}/restore?generation={gen}"
            )
            resp = authed.post(url, headers={'Content-Type': 'application/json'})
            if resp.status_code >= 400:
                raise RuntimeError(f"Restore failed: {resp.status_code} {resp.text}")

            live_blobs = list(self._client.list_blobs(bucket, match_glob=object_name))
            live_blobs.sort(key=lambda b: (b.time_created, b.generation), reverse=True)
            return int(live_blobs[0].generation)

        return await asyncio.to_thread(_restore)
