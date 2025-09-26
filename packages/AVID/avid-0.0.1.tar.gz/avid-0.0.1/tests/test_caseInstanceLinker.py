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

import unittest

import avid.common.artefact as artefact
import avid.common.artefact.generator as artefactGenerator
from avid.linkers import CaseInstanceLinker


class TestCaseInstanceLinker(unittest.TestCase):
    def setUp(self):
        self.a1 = artefactGenerator.generateArtefactEntry(
            "Case1", None, 0, "Action1", "result", "dummy", None
        )
        self.a2 = artefactGenerator.generateArtefactEntry(
            "Case2", "a", 1, "Action2", "result", "dummy", None
        )
        self.a3 = artefactGenerator.generateArtefactEntry(
            "Case2", 4, 2, "Action2", "result", "dummy", None
        )
        self.a4 = artefactGenerator.generateArtefactEntry(
            "Case3", "a", 0, "Action2", "result", "dummy", None
        )
        self.a5 = artefactGenerator.generateArtefactEntry(
            "Case4", "1", 0, "Action3", "result", "dummy", None
        )
        self.a6 = artefactGenerator.generateArtefactEntry(
            "Case4", "noLink", 0, "Action3", "result", "dummy", None
        )

        self.secondary = [[self.a1], [self.a2], [self.a3], [self.a4], [self.a5]]
        self.primary = [[self.a1], [self.a2], [self.a3], [self.a6]]

    def test_CaseInstanceLinker_strict(self):
        linker = CaseInstanceLinker(True)
        selection = linker.getLinkedSelection(0, self.primary, self.secondary)
        self.assertEqual(len(selection), 1)
        self.assertEqual(len(selection[0]), 1)
        self.assertIn(self.a1, selection[0])

        linker = CaseInstanceLinker(True)
        selection = linker.getLinkedSelection(1, self.primary, self.secondary)
        self.assertEqual(len(selection), 2)
        self.assertEqual(len(selection[0]), 1)
        self.assertEqual(len(selection[1]), 1)
        self.assertIn(self.a2, selection[0])
        self.assertIn(self.a4, selection[1])

        linker = CaseInstanceLinker(True)
        selection = linker.getLinkedSelection(2, self.primary, self.secondary)
        self.assertEqual(len(selection), 1)
        self.assertEqual(len(selection[0]), 1)
        self.assertIn(self.a3, selection[0])

        linker = CaseInstanceLinker(True)
        selection = linker.getLinkedSelection(3, self.primary, self.secondary)
        self.assertEqual(len(selection), 0)

    def test_CaseInstanceLinker_not_strict(self):
        linker = CaseInstanceLinker()
        selection = linker.getLinkedSelection(0, self.primary, self.secondary)
        self.assertEqual(len(selection), 5)
        self.assertEqual(len(selection[0]), 1)
        self.assertEqual(len(selection[1]), 1)
        self.assertEqual(len(selection[2]), 1)
        self.assertEqual(len(selection[3]), 1)
        self.assertEqual(len(selection[4]), 1)
        self.assertIn(self.a1, selection[0])
        self.assertIn(self.a2, selection[1])
        self.assertIn(self.a3, selection[2])
        self.assertIn(self.a4, selection[3])
        self.assertIn(self.a5, selection[4])

        linker = CaseInstanceLinker()
        selection = linker.getLinkedSelection(1, self.primary, self.secondary)
        self.assertEqual(len(selection), 3)
        self.assertEqual(len(selection[0]), 1)
        self.assertEqual(len(selection[1]), 1)
        self.assertEqual(len(selection[2]), 1)
        self.assertIn(self.a1, selection[0])
        self.assertIn(self.a2, selection[1])
        self.assertIn(self.a4, selection[2])

        linker = CaseInstanceLinker()
        selection = linker.getLinkedSelection(2, self.primary, self.secondary)
        self.assertEqual(len(selection), 2)
        self.assertEqual(len(selection[0]), 1)
        self.assertEqual(len(selection[1]), 1)
        self.assertIn(self.a1, selection[0])
        self.assertIn(self.a3, selection[1])

        linker = CaseInstanceLinker()
        selection = linker.getLinkedSelection(3, self.primary, self.secondary)
        self.assertEqual(len(selection), 1)
        self.assertEqual(len(selection[0]), 1)
        self.assertIn(self.a1, selection[0])

    def test_CaseInstanceLinker_empty_secondary(self):
        linker = CaseInstanceLinker()
        selection = linker.getLinkedSelection(2, self.secondary, [])
        self.assertEqual(len(selection), 0)

        linker = CaseInstanceLinker(True)
        selection = linker.getLinkedSelection(2, self.secondary, [])
        self.assertEqual(len(selection), 0)


if __name__ == "__main__":
    unittest.main()
