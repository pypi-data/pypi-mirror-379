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

from typing import Any


class ReportFile:
    name: str
    contents: Any

    def __init__(self, name: str, contents: Any, file_type: str = "json"):
        self.name = name
        self.contents = contents
        self.file_type = file_type

    def get_filename(self) -> str:
        return f"{self.name}.{self.file_type}"

    def get_contents(self) -> Any:
        return self.contents
