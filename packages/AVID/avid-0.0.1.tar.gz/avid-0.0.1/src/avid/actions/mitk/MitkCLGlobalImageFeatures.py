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
from avid.actions.genericCLIAction import generate_cli_call
from avid.actions.simpleScheduler import SimpleScheduler
from avid.common import AVIDUrlLocater, osChecker
from avid.linkers import CaseLinker, FractionLinker
from avid.selectors import TypeSelector
from avid.splitter import BaseSplitter, KeyValueSplitter

logger = logging.getLogger(__name__)

FORMAT_VALUE_MITK_GIF_XML = "mitk_cl_gif_xml"


class MitkCLGlobalImageFeaturesAction(CLIActionBase):
    """Class that wraps the single action for the tool MITK CLGlobalImageFeatures."""

    def __init__(
        self,
        images,
        masks=None,
        cliArgs=None,
        legacyOutput=False,
        actionTag="MitkCLGlobalImageFeatures",
        alwaysDo=False,
        session=None,
        additionalActionProps=None,
        actionConfig=None,
        propInheritanceDict=None,
        cli_connector=None,
    ):
        CLIActionBase.__init__(
            self,
            actionTag,
            alwaysDo,
            session,
            additionalActionProps,
            actionConfig=actionConfig,
            propInheritanceDict=propInheritanceDict,
            cli_connector=cli_connector,
        )

        self._addInputArtefacts(images=images, masks=masks)

        self._legacyOutput = legacyOutput
        self._images = images
        self._masks = masks

        if not legacyOutput:
            self._images = self._ensureSingleArtefact(images, "images")
            self._masks = self._ensureSingleArtefact(masks, "masks")

        self._cliArgs = dict()
        if cliArgs is not None:
            illegalArgs = [
                "i",
                "image",
                "m",
                "mask",
                "morph-mask",
                "morph",
                "o",
                "output",
                "x",
                "xml-output",
            ]
            for arg in cliArgs:
                if arg not in illegalArgs:
                    self._cliArgs[arg] = cliArgs[arg]
                else:
                    logger.warning(
                        'Ignored illegal argument "{}". It will be set by action'.format(
                            arg
                        )
                    )

        if self._cwd is None:
            self._cwd = os.path.dirname(
                AVIDUrlLocater.get_tool_executable_url(
                    self._session, "MitkCLGlobalImageFeatures", actionConfig
                )
            )

    def _generateName(self):
        name = "gif"

        if not self._legacyOutput:
            name += "_{}_".format(artefactHelper.getArtefactShortName(self._images))
            if self._masks is not None:
                name += "_ROI_{}".format(
                    artefactHelper.getArtefactShortName(self._masks)
                )

        return name

    def _indicateOutputs(self):
        # Specify result artefact
        self._resultCSVArtefact = None
        self._resultXMLArtefact = None
        result = list()

        if self._legacyOutput:
            self._resultCSVArtefact = self.generateArtefact(
                self._images[0],
                userDefinedProps={
                    artefactProps.TYPE: artefactProps.TYPE_VALUE_RESULT,
                    artefactProps.FORMAT: artefactProps.FORMAT_VALUE_CSV,
                },
                url_user_defined_part=self.instanceName,
                url_extension="csv",
            )
            result = [self._resultCSVArtefact]

        else:
            self._resultCSVArtefact = self.generateArtefact(
                self._images,
                userDefinedProps={
                    artefactProps.TYPE: artefactProps.TYPE_VALUE_RESULT,
                    artefactProps.FORMAT: artefactProps.FORMAT_VALUE_CSV,
                },
                url_user_defined_part=self.instanceName,
                url_extension="csv",
            )
            self._resultXMLArtefact = self.generateArtefact(
                self._images,
                userDefinedProps={
                    artefactProps.TYPE: artefactProps.TYPE_VALUE_RESULT,
                    artefactProps.FORMAT: FORMAT_VALUE_MITK_GIF_XML,
                },
                url_user_defined_part=self.instanceName,
                url_extension="xml",
            )
            result = [self._resultCSVArtefact, self._resultXMLArtefact]

        return result

    def _getAllInputCombinations(self):
        """Helper that returns all combinations of masks and images that should be processed"""
        result = list()
        if self._legacyOutput:
            for image in self._images:
                for mask in self._masks:
                    result.append([image, mask])
        else:
            # if not in legacy mode the variables contain only one artefact and this should be used.
            result.append([self._images, self._masks])
        return result

    def _prepareCLIExecution(self):

        resultPath = artefactHelper.getArtefactProperty(
            self._resultCSVArtefact, artefactProps.URL
        )
        osChecker.checkAndCreateDir(os.path.split(resultPath)[0])

        content = ""

        try:
            execURL = self._cli_connector.get_executable_url(
                self._session, "MitkCLGlobalImageFeatures", self._actionConfig
            )
        except:
            logger.error("Error for getExecutable.")
            raise

        inputPairs = self._getAllInputCombinations()

        for inputPair in inputPairs:
            if not len(content) == 0:
                content += os.linesep

            artefactArgs = {
                "i": [inputPair[0]],
                "m": [inputPair[1]],
                "o": [self._resultCSVArtefact],
            }
            if not self._legacyOutput:
                artefactArgs["x"] = [self._resultXMLArtefact]

            content += generate_cli_call(
                exec_url=execURL,
                artefact_args=artefactArgs,
                additional_args=self._cliArgs,
                artefact_url_extraction_delegate=self._cli_connector.get_artefact_url_extraction_delegate(),
            )

        return content


class MitkCLGlobalImageFeaturesBatchAction(BatchActionBase):
    """Batch action for MITKCLGlobalImageFeatures to produce XML results."""

    def __init__(
        self,
        imageSelector,
        maskSelector,
        maskLinker=None,
        actionTag="MITKCLGlobalImageFeatures",
        session=None,
        additionalActionProps=None,
        scheduler=SimpleScheduler(),
        **singleActionParameters,
    ):

        if maskLinker is None:
            maskLinker = FractionLinker()

        additionalInputSelectors = {"masks": maskSelector}
        linker = {"masks": maskLinker}

        BatchActionBase.__init__(
            self,
            actionTag=actionTag,
            actionClass=MitkCLGlobalImageFeaturesAction,
            primaryInputSelector=imageSelector,
            primaryAlias="images",
            additionalInputSelectors=additionalInputSelectors,
            linker=linker,
            session=session,
            relevanceSelector=TypeSelector(artefactProps.TYPE_VALUE_RESULT),
            scheduler=scheduler,
            additionalActionProps=additionalActionProps,
            legacyOutput=False,
            **singleActionParameters,
        )


class MitkCLGlobalImageFeaturesLegacyCSVBatchAction(BatchActionBase):
    """Batch action for MITKCLGlobalImageFeatures that produces a condensed csv file.
    @param splitProperties You can define a list of split properties (list of property names)
    to separate images and masks into different actions. All artefacts of one action will be
    condensed into one csv."""

    def __init__(
        self,
        imageSelector,
        maskSelector,
        maskLinker=None,
        splitProperties=None,
        actionTag="MITKCLGlobalImageFeatures",
        session=None,
        additionalActionProps=None,
        scheduler=SimpleScheduler(),
        **singleActionParameters,
    ):
        if maskLinker is None:
            maskLinker = FractionLinker(allowOnlyFullLinkage=False)

        splitter = {
            BatchActionBase.PRIMARY_INPUT_KEY: BaseSplitter(),
            "masks": BaseSplitter(),
        }
        if splitProperties is not None:
            splitter = {
                BatchActionBase.PRIMARY_INPUT_KEY: KeyValueSplitter(*splitProperties),
                "masks": KeyValueSplitter(*splitProperties),
            }

        additionalInputSelectors = {"masks": maskSelector}
        linker = {"masks": maskLinker}

        BatchActionBase.__init__(
            self,
            actionTag=actionTag,
            actionClass=MitkCLGlobalImageFeaturesAction,
            primaryInputSelector=imageSelector,
            primaryAlias="images",
            additionalInputSelectors=additionalInputSelectors,
            linker=linker,
            splitter=splitter,
            session=session,
            relevanceSelector=TypeSelector(artefactProps.TYPE_VALUE_RESULT),
            scheduler=scheduler,
            additionalActionProps=additionalActionProps,
            legacyOutput=True,
            **singleActionParameters,
        )
