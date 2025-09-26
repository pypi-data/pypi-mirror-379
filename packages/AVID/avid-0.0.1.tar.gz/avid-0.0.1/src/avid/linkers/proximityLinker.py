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

import avid.common.artefact as artefactHelper
import avid.common.artefact.defaultProps as artefactProps
from avid.linkers import LinkerBase

from .keyValueLinker import CaseLinker


class ProximityLinker(LinkerBase):
    """
    Links data by searching all link options fullfilling the following criteria:
    (1) same case
    (3) with the best proximity score.
    The proximity score is derived by comparing the value of the defined key by a provided
    proximity_delegate. A proximity score of 0 is a perfect match.
    Remark: The current simple implementation only checks the first artefact of a link option,
    even if a link option contains multiple artefacts (so no inner linkage is done).
    """

    def __init__(self, key, proximity_delegate, allow_only_full_linkage=True):
        """:param key Indicating the property of the artefact that will be used to measure the proximity.
        :param proximity_delegate Function that takes to property values and computes an proximity score. The proximity score
        should be a positive number. 0 indicates perfect match. Lower scores are better than higher ones.
        :param allow_only_full_linkage see documentation of InnerLinkerBase.
        """
        LinkerBase.__init__(self, allowOnlyFullLinkage=allow_only_full_linkage)
        self._proximity_delegate = proximity_delegate
        self._key = key
        self._caseLinker = CaseLinker(allowOnlyFullLinkage=allow_only_full_linkage)

    def _getLinkedSelection(self, primaryIndex, primarySelections, secondarySelections):
        """Filters the given secondary selections and returns the selections that have the best proximity
        score.
        In the current implementation it is simplfied by just checking the score of the first artefact of each
        selection."""

        primary_selection = primarySelections[primaryIndex]

        prefiltered_selection = self._caseLinker.getLinkedSelection(
            primaryIndex=primaryIndex,
            primarySelections=primarySelections,
            secondarySelections=secondarySelections,
        )
        result = list()

        try:
            primary_value = artefactHelper.getArtefactProperty(
                primary_selection[0], self._key
            )
            best_artefact = None
            best_proximity_score = float("inf")

            for selection in prefiltered_selection:
                try:
                    if selection[0] is None:
                        proximity_score = float("inf")
                    else:
                        proximity_score = float(
                            self._proximity_delegate(
                                primary_value,
                                artefactHelper.getArtefactProperty(
                                    selection[0], self._key
                                ),
                            )
                        )

                    if proximity_score <= best_proximity_score:
                        if proximity_score < best_proximity_score:
                            result.clear()
                            best_proximity_score = proximity_score
                        result.append(selection)
                except:
                    pass
        except:
            pass

        return result


class TimePointProximityLinker(ProximityLinker):
    """
    Links data on the basis of the artefactProps.TIMEPOINT entry.
    """

    def proximity_measure(val1, val2):
        return abs(float(val1) - float(val2))

    def __init__(self, allow_only_full_linkage=True):
        ProximityLinker.__init__(
            self,
            key=artefactProps.TIMEPOINT,
            proximity_delegate=TimePointProximityLinker.proximity_measure,
            allow_only_full_linkage=allow_only_full_linkage,
        )
