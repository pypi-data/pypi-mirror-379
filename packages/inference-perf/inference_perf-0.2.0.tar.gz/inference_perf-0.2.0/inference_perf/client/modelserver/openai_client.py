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
from inference_perf.client.requestdatacollector import RequestDataCollector
from inference_perf.config import APIConfig, APIType, CustomTokenizerConfig
from inference_perf.apis import InferenceAPIData, InferenceInfo, RequestLifecycleMetric, ErrorResponseInfo
from inference_perf.utils import CustomTokenizer
from .base import ModelServerClient, PrometheusMetricMetadata
from typing import List, Optional
import aiohttp
import json
import time
import logging
import requests

logger = logging.getLogger(__name__)


class openAIModelServerClient(ModelServerClient):
    def __init__(
        self,
        metrics_collector: RequestDataCollector,
        api_config: APIConfig,
        uri: str,
        model_name: Optional[str],
        tokenizer_config: Optional[CustomTokenizerConfig],
        max_tcp_connections: int,
        additional_filters: List[str],
        ignore_eos: bool = True,
        api_key: Optional[str] = None,
    ) -> None:
        super().__init__(api_config)
        self.uri = uri
        self.max_completion_tokens = 30  # default to use when not set at the request level
        self.ignore_eos = ignore_eos
        self.metrics_collector = metrics_collector
        self.max_tcp_connections = max_tcp_connections
        self.additional_filters = additional_filters
        self.api_key = api_key

        if model_name is None:
            supported_models = self.get_supported_models()
            if not supported_models:
                logger.error("No supported models found")
                raise Exception("openAI client init failed, no model_name could be found")
            self.model_name = supported_models[0].get("id")
            logger.info(f"Inferred model {self.model_name}")
            if len(supported_models) > 1:
                logger.warning(f"More than one supported model found {supported_models}, selecting {self.model_name}")
        else:
            self.model_name = model_name

        if tokenizer_config and not tokenizer_config.pretrained_model_name_or_path:
            tokenizer_config.pretrained_model_name_or_path = self.model_name
        elif not tokenizer_config:
            tokenizer_config = CustomTokenizerConfig(pretrained_model_name_or_path=self.model_name)
        self.tokenizer = CustomTokenizer(tokenizer_config)

    async def process_request(self, data: InferenceAPIData, stage_id: int, scheduled_time: float) -> None:
        payload = data.to_payload(
            model_name=self.model_name,
            max_tokens=self.max_completion_tokens,
            ignore_eos=self.ignore_eos,
            streaming=self.api_config.streaming,
        )
        headers = {"Content-Type": "application/json"}

        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"

        if self.api_config.headers:
            headers.update(self.api_config.headers)

        request_data = json.dumps(payload)

        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(limit=self.max_tcp_connections)) as session:
            start = time.perf_counter()
            try:
                async with session.post(self.uri + data.get_route(), headers=headers, data=request_data) as response:
                    response_info = await data.process_response(
                        response=response, config=self.api_config, tokenizer=self.tokenizer
                    )
                    response_content = await response.text()

                    end_time = time.perf_counter()
                    error = None
                    if response.status != 200:
                        error = ErrorResponseInfo(error_msg=response_content, error_type="Error response")

                    self.metrics_collector.record_metric(
                        RequestLifecycleMetric(
                            stage_id=stage_id,
                            request_data=request_data,
                            response_data=response_content,
                            info=response_info,
                            error=error,
                            start_time=start,
                            end_time=end_time,
                            scheduled_time=scheduled_time,
                        )
                    )
            except Exception as e:
                logger.error("error occured during request processing:", exc_info=True)
                self.metrics_collector.record_metric(
                    RequestLifecycleMetric(
                        stage_id=stage_id,
                        request_data=request_data,
                        response_data=response_content if "response_content" in locals() else "",
                        info=response_info if "response_info" in locals() else InferenceInfo(),
                        error=ErrorResponseInfo(
                            error_msg=str(e),
                            error_type=type(e).__name__,
                        ),
                        start_time=start,
                        end_time=time.perf_counter(),
                        scheduled_time=scheduled_time,
                    )
                )

    def get_supported_apis(self) -> List[APIType]:
        return []

    @abstractmethod
    def get_prometheus_metric_metadata(self) -> PrometheusMetricMetadata:
        raise NotImplementedError

    def get_supported_models(self) -> List[str]:
        try:
            response = requests.get(f"{self.uri}/v1/models")
            response.raise_for_status()
            data = response.json()
            if "data" in data and isinstance(data["data"], list):
                return data["data"]
            else:
                return []
        except Exception as e:
            logger.error(f"Got exception retrieving supported models {e}")
            return []
