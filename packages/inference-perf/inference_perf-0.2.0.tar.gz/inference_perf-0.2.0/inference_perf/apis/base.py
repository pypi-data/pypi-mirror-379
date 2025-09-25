# Copyright 2025 The Kubernetes Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from abc import abstractmethod
from typing import Any, List, Optional
from aiohttp import ClientResponse
from pydantic import BaseModel
from inference_perf.utils.custom_tokenizer import CustomTokenizer
from inference_perf.config import APIConfig, APIType


class InferenceInfo(BaseModel):
    input_tokens: int = 0
    output_tokens: int = 0
    output_token_times: List[float] = []


class ErrorResponseInfo(BaseModel):
    error_type: str
    error_msg: str


class RequestLifecycleMetric(BaseModel):
    stage_id: Optional[int] = None
    scheduled_time: float
    start_time: float
    end_time: float
    request_data: str
    response_data: Optional[str] = None
    info: InferenceInfo
    error: Optional[ErrorResponseInfo]


class InferenceAPIData(BaseModel):
    @abstractmethod
    def get_api_type(self) -> APIType:
        raise NotImplementedError

    @abstractmethod
    def get_route(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def to_payload(self, model_name: str, max_tokens: int, ignore_eos: bool, streaming: bool) -> dict[str, Any]:
        raise NotImplementedError

    @abstractmethod
    async def process_response(self, response: ClientResponse, config: APIConfig, tokenizer: CustomTokenizer) -> InferenceInfo:
        raise NotImplementedError
