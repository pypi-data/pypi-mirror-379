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

import os
import shutil
import unittest

from avid.common.workflow import initSession
from avid.common.workflow.structure_definitions import (
    loadStructurDefinition_xml as load_xml,
)


class TestWorkflowHelper(unittest.TestCase):

    def setUp(self):
        self.sessionDir = os.path.join(
            os.path.split(__file__)[0], "temporary_test_workflow"
        )
        self.testDataDir = os.path.join(os.path.split(__file__)[0], "data")
        self.bootstrapFile = os.path.join(self.testDataDir, "testlist.avid")

    def tearDown(self):
        try:
            shutil.rmtree(self.sessionDir)
        except:
            pass

    def test_initSession(self):
        session = initSession(os.path.join(self.sessionDir, "test.avid"))
        session = initSession(
            os.path.join(self.sessionDir, "test_noLogging.avid"), initLogging=False
        )
        session = initSession(
            os.path.join(self.sessionDir, "test_bootstrap.avid"),
            expandPaths=True,
            bootstrapArtefacts=self.bootstrapFile,
        )


if __name__ == "__main__":
    unittest.main()
