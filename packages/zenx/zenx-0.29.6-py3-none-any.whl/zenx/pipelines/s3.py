import os
from typing import Dict, List, Optional
from httpx import AsyncClient
from structlog import BoundLogger
import aiofiles

from zenx.utils import get_time, log_processing_time
from .base import Pipeline
from zenx.database import DBClient
from zenx.settings import Settings



class SynopticS3Pipeline(Pipeline):
    name = "synoptic_s3"
    required_settings = ["SYNOPTIC_S3_STREAM_ID", "SYNOPTIC_S3_API_KEY"]
    stream_id = "SYNOPTIC_S3_STREAM_ID"
    api_key = "SYNOPTIC_S3_API_KEY"
    

    def __init__(self, logger: BoundLogger, db: DBClient, settings: Settings) -> None:
        super().__init__(logger, db, settings)
        self._stream_id = getattr(settings, self.stream_id)
        self._api_key = getattr(settings, self.api_key)
        self._client = AsyncClient()
        self._cache = {} # mime_type: {"created_at": get_time(), "upload_url": upload_url}
        self._cache_ttl = 50 * 60 * 1000 # 50 minutes


    async def open(self) -> None:
        for setting in self.required_settings:
            if not getattr(self.settings, setting):
                raise ValueError(f"Missing required setting for pipeline '{self.name}': {setting}")
        self.logger.info("opened", pipeline=self.name)
        
    
    async def _fetch_presigned_media_url(self, mime_type: str) -> str:
        if mime_type in self._cache: 
            created_at = self._cache[mime_type]['created_at']
            # if cache record is less than 50 minutes, return the upload url
            if (get_time() - created_at) < self._cache_ttl: 
                return self._cache[mime_type]['upload_url']
        
        url = f"https://api.dev.synoptic.com/v1/streams/{self._stream_id}/post"
        headers={
            'x-api-key': self._api_key,
            'Accept': '*/*',
        }
        json_data = {
            'content': 'text',
            'uploadMedia': [
                {
                    'mimeType': mime_type,
                },
            ],
        }
        try:
            response = await self._client.post(
                url=url,
                headers=headers,
                json=json_data,
            )
            if response.status_code != 201:
                raise Exception(f"unexpected response: {response.status_code}")
        except Exception as e:
            self.logger.error("fetch_presigned_media_url", exception=str(e), mime_type=mime_type, pipeline=self.name)
        else:
            media_upload_urls = response.json()['mediaUploadURLs']
            if not media_upload_urls:
                self.logger.error("unsupported_mime_type", mime_type=mime_type, pipeline=self.name)
                return None
            upload_url = media_upload_urls[0]['url']
            self._cache[mime_type] = {"created_at": get_time(), "upload_url": upload_url}
            return upload_url

    
    @log_processing_time
    async def process_item(self, item: Dict, producer: str) -> Dict:
        presigned_url = await self._fetch_presigned_media_url(item['mime_type'])
        if not presigned_url:
            self.logger.error("no_presigned_url", item=item, pipeline=self.name)
            if item['fd'] != -1:
                os.close(item['fd'])
            return item
        
        payload = {"url": presigned_url, "headers": {"content-type": item['mime_type']}, "file_path": item['file_path']}
        await self.send(payload)
        if item['fd'] != -1:
            os.close(item['fd'])

        return item


    async def send(self, payload: Dict) -> None:
        url = payload['url']
        headers = payload['headers']
        file_path = payload['file_path']
        try:
            async with aiofiles.open(file_path, mode="rb") as f:
                response = await self._client.put(url, headers=headers, content=f)
                response.raise_for_status()
        except Exception as e:
            self.logger.error("processing", exception=str(e), url=url[:100], headers=headers, file_path=file_path, pipeline=self.name)

    
    async def close(self) -> None:
        if self._client:
            await self._client.aclose()
        self.logger.info("closed", pipeline=self.name)

