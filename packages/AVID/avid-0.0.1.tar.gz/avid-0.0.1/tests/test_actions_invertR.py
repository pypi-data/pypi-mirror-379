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

# workaround a pyCharm bug
import os
import shutil
import unittest

import avid.common.workflow as workflow
from avid.actions.unrefactored.invertR import invertRBatchAction as invertR
from avid.common.AVIDUrlLocater import get_tool_executable_url
from avid.selectors.keyValueSelector import ActionTagSelector


@unittest.skipIf(
    get_tool_executable_url(None, "invertR") is None,
    "Tool invertR not installed on the system.",
)
class TestInvertR(unittest.TestCase):

    def setUp(self):
        self.testDataDir = os.path.join(
            os.path.split(__file__)[0], "data", "invertRTest"
        )
        self.testArtefactFile = os.path.join(
            os.path.split(__file__)[0], "data", "invertRTest", "testlist.avid"
        )
        self.sessionDir = os.path.join(
            os.path.split(__file__)[0], "temporary", "test_invertR"
        )
        self.session = workflow.initSession(
            os.path.join(self.sessionDir, "test.avid"),
            expandPaths=True,
            bootstrapArtefacts=self.testArtefactFile,
        )

    def tearDown(self):
        try:
            shutil.rmtree(self.sessionDir)
        except:
            pass

    def test_simple_inversion_action(self):
        action = invertR(ActionTagSelector("Registration"), actionTag="TestReg")
        action.do()

        self.assertEqual(action.isSuccess, True)

        action.do()
        self.assertEqual(action.isSkipped, True)

    def test_simple_inversion_action_always_do(self):
        action = invertR(
            ActionTagSelector("Registration"), actionTag="TestReg", alwaysDo=True
        )
        action.do()

        self.assertEqual(action.isSuccess, True)
        action.do()
        self.assertEqual(action.isSuccess, True)

    def test_inversion_with_template_image_action(self):
        action = invertR(
            ActionTagSelector("Registration"),
            templateSelector=ActionTagSelector("Target"),
            actionTag="TestReg",
        )
        action.do()
        self.assertEqual(action.isSuccess, True)


if __name__ == "__main__":
    unittest.main()
