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

import logging
import os
import re
import subprocess

import avid.common.artefact as artefactHelper
import avid.common.artefact.defaultProps as artefactProps
from avid.actions import BatchActionBase
from avid.actions.cliActionBase import CLIActionBase
from avid.actions.simpleScheduler import SimpleScheduler
from avid.common import AVIDUrlLocater, osChecker
from avid.linkers import CaseLinker, FractionLinker
from avid.selectors import TypeSelector

logger = logging.getLogger(__name__)


class CurveDescriptorMiniAppAction(CLIActionBase):
    """Class that wrapps the single action for the tool CurveDescriptorMiniApp."""

    def __init__(
        self,
        signal,
        mask=None,
        actionTag="CurveDescription",
        alwaysDo=False,
        session=None,
        additionalActionProps=None,
        actionConfig=None,
        propInheritanceDict=None,
    ):
        CLIActionBase.__init__(
            self,
            actionTag,
            alwaysDo,
            session,
            additionalActionProps,
            actionConfig=actionConfig,
            propInheritanceDict=propInheritanceDict,
        )

        self._addInputArtefacts(signal=signal, mask=mask)

        self._signal = signal
        self._mask = mask

        self._resultTemplate = self.generateArtefact(
            self._signal,
            userDefinedProps={
                artefactProps.TYPE: artefactProps.TYPE_VALUE_RESULT,
                artefactProps.FORMAT: artefactProps.FORMAT_VALUE_ITK,
            },
            url_user_defined_part=self.instanceName,
            url_extension="nrrd",
        )

        if self._cwd is None:
            self._cwd = os.path.dirname(
                AVIDUrlLocater.get_tool_executable_url(
                    self._session, "CurveDescriptorMiniApp", actionConfig
                )
            )

    def _generateName(self):
        name = "curveDesc_{}".format(artefactHelper.getArtefactShortName(self._signal))
        if self._mask is not None:
            name += "_ROI_{}".format(artefactHelper.getArtefactShortName(self._mask))

        return name

    def _indicateOutputs(self):
        resultsInfo = self._previewResult()

        self._resultArtefacts = dict()
        for info in resultsInfo:
            result = self.generateArtefact(
                self._signal,
                userDefinedProps={
                    artefactProps.TYPE: artefactProps.TYPE_VALUE_RESULT,
                    artefactProps.FORMAT: artefactProps.FORMAT_VALUE_ITK,
                    artefactProps.RESULT_SUB_TAG: info[1],
                },
            )
            result[artefactProps.URL] = info[2]
            self._resultArtefacts[info[1]] = result

        return list(self._resultArtefacts.values())

    def _generateCLIArguments(self):
        resultPath = artefactHelper.getArtefactProperty(
            self._resultTemplate, artefactProps.URL
        )
        signalPath = artefactHelper.getArtefactProperty(self._signal, artefactProps.URL)
        maskPath = artefactHelper.getArtefactProperty(self._mask, artefactProps.URL)

        execURL = AVIDUrlLocater.get_tool_executable_url(
            self._session, "CurveDescriptorMiniApp", self._actionConfig
        )

        result = list()
        result.append(execURL)
        result.append("-i")
        result.append("{}".format(signalPath))
        result.append("-o")
        result.append("{}".format(resultPath))

        if maskPath is not None:
            result.append("-m")
            result.append("{}".format(maskPath))

        return result

    def _previewResult(self):
        """Helper function that call the MiniApp in preview mode to depict the results. Returns a list of trippels (type, name, url)."""
        results = list()
        try:
            args = self._generateCLIArguments()
            args.append("--preview")
            output = subprocess.check_output(args, cwd=self._cwd)

            for line in output.splitlines():
                if line.startswith("Store result "):
                    regResults = re.findall("Store result (.*): (.*) -> (.*)", line)

                    try:
                        type = regResults[0][0]
                        name = regResults[0][1]
                        url = regResults[0][2]
                        results.append((type, name, url))
                    except:
                        raise RuntimeError(
                            "Failed to parse storage info line: {}".format(line)
                        )

        except subprocess.CalledProcessError as err:
            pass

        return results

    def _prepareCLIExecution(self):
        args = self._generateCLIArguments()
        # escape everything to be sure that no propblem in the batch file (reserved charactars) or with the pathes occure.
        # cannot be done in _generateCLIArguments because the direct call used by preview does not like the escapation.
        # should be handled soundly by reworking prepareCLIExecution not returning the content string, but all arguments
        # of the call. Then escaption etc can be handled in the base class.
        content = args[0] + ' "' + '" "'.join(args[1:]) + '"'
        resultPath = artefactHelper.getArtefactProperty(
            self._resultTemplate, artefactProps.URL
        )
        osChecker.checkAndCreateDir(os.path.split(resultPath)[0])

        return content


class CurveDescriptorMiniAppBatchAction(BatchActionBase):
    """Batch action for CurveDescriptorMiniApp."""

    def __init__(
        self,
        signalSelector,
        maskSelector=None,
        maskLinker=FractionLinker(),
        actionTag="CurveDescription",
        alwaysDo=False,
        session=None,
        additionalActionProps=None,
        scheduler=SimpleScheduler(),
        **singleActionParameters,
    ):
        BatchActionBase.__init__(
            self, actionTag, alwaysDo, scheduler, session, additionalActionProps
        )

        self._signals = signalSelector.getSelection(self._session.artefacts)

        self._masks = list()
        if maskSelector is not None:
            self._masks = maskSelector.getSelection(self._session.artefacts)

        self._maskLinker = maskLinker

        self._singleActionParameters = singleActionParameters

    def _generateActions(self):
        # filter only type result. Other artefact types are not interesting
        resultSelector = TypeSelector(artefactProps.TYPE_VALUE_RESULT)

        signals = self.ensureRelevantArtefacts(self._signals, resultSelector, "signals")
        masks = self.ensureRelevantArtefacts(self._masks, resultSelector, "masks")

        global logger

        actions = list()

        for pos, signal in enumerate(signals):
            linkedMasks = self._maskLinker.getLinkedSelection(pos, signals, masks)
            if len(linkedMasks) == 0:
                linkedMasks = [None]

            for lm in linkedMasks:
                action = CurveDescriptorMiniAppAction(
                    signal,
                    mask=lm,
                    actionTag=self._actionTag,
                    alwaysDo=self._alwaysDo,
                    session=self._session,
                    additionalActionProps=self._additionalActionProps,
                    **self._singleActionParameters,
                )
                actions.append(action)

        return actions
