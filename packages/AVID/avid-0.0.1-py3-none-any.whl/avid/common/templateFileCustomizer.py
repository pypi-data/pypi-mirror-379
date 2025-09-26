# SPDX-FileCopyrightText: 2024, German Cancer Research Center (DKFZ), Division of Medical Image Computing (MIC)
#
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# or find it in LICENSE.txt.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from builtins import str


def writeFileCustomized(templateFilename, targetFilename, replaceDict):
    inputFile = open(templateFilename, "r")
    content = inputFile.read()
    inputFile.close()

    for key, value in replaceDict.items():
        content = content.replace(key, str(value))

    outputFile = open(targetFilename, "w")
    outputFile.write(content)
    outputFile.close()
