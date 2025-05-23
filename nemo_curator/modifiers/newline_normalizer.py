# Copyright (c) 2025, NVIDIA CORPORATION.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import re

from nemo_curator.modifiers import DocumentModifier

THREE_OR_MORE_NEWLINES_REGEX = re.compile(r"(\n){3,}")
THREE_OR_MORE_WINDOWS_NEWLINES_REGEX = re.compile(r"(\r\n){3,}")


class NewlineNormalizer(DocumentModifier):
    """
    Replaces 3 or more consecutive newline characters with only 2 newline characters.
    """

    def __init__(self):
        super().__init__()

    def modify_document(self, text: str) -> str:
        text = THREE_OR_MORE_NEWLINES_REGEX.sub("\n\n", text)
        return THREE_OR_MORE_WINDOWS_NEWLINES_REGEX.sub("\r\n\r\n", text)
