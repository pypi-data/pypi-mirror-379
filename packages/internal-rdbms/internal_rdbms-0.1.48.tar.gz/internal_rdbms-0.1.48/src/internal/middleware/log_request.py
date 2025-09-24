import logging
import time

from collections import defaultdict
from fastapi import FastAPI, Request
from starlette.middleware.base import BaseHTTPMiddleware
from ..const import CORRELATION_ID_HEADER_KEY_NAME


class LogRequestMiddleware(BaseHTTPMiddleware):
    def __init__(self, app: FastAPI, logger: logging.Logger):
        super().__init__(app)
        self.app = app
        self.logger = logger

    async def dispatch(self, request: Request, call_next):
        # 记录请求的URL和参数
        url = request.url.path
        method = request.method
        headers = request.headers
        request_id = headers.get(CORRELATION_ID_HEADER_KEY_NAME, "")
        content_type = headers.get('content-type', '') or headers.get('Content-Type', '')
        is_multipart = 'multipart' in content_type.lower()

        query_params = request.query_params
        temp = defaultdict(list)
        for key, value in query_params.multi_items():
            temp[key].append(value)
        # 如果只有一個值就轉成單一值
        params = {k: v[0] if len(v) == 1 else v for k, v in temp.items()}

        body = await request.body()
        if is_multipart:
            self.logger.info(f"[Request id: {request_id}] \nURL: {method} {url} \nParams: {params} \nBody: 因上傳檔案不顯示body \nHeaders: {headers} \nstart processing...")
        else:
            self.logger.info(f"[Request id: {request_id}] \nURL: {method} {url} \nParams: {params} \nBody: {body} \nHeaders: {headers} \nstart processing...")

        # 记录请求处理时间
        start_time = time.time()
        response = await call_next(request)
        process_time = time.time() - start_time

        if is_multipart:
            self.logger.info(f"[Request id: {request_id}] \nURL: {method} {url} \nParams: {params} \nBody: 因上傳檔案不顯示body \nCompleted in {process_time:.4f} seconds")
        else:
            self.logger.info(f"[Request id: {request_id}] \nURL: {method} {url} \nParams: {params} \nBody: {body} \nCompleted in {process_time:.4f} seconds")
        return response
