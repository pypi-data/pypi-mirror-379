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
from builtins import object

import avid.common.artefact.defaultProps as artefactProps
import avid.common.workflow as workflow
from avid.linkers import CaseInstanceLinker, CaseLinker
from avid.selectors import TypeSelector
from avid.sorter import BaseSorter
from avid.splitter import SingleSplitter

logger = logging.getLogger(__name__)


class ActionBatchGenerator(object):
    """Class helps to generate concrete action instance for a given session and a given set of rules (for selecting, splitting, sorting and linking)."""

    PRIMARY_INPUT_KEY = "primaryInput"

    def __init__(
        self,
        primaryInputSelector,
        actionClass=None,
        actionCreationDelegate=None,
        primaryAlias=None,
        additionalInputSelectors=None,
        splitter=None,
        sorter=None,
        linker=None,
        dependentLinker=None,
        session=None,
        relevanceSelector=None,
        **actionParameters,
    ):
        """init the generator.
        @param actionClass: Class of the action that should be generated
        @param primaryInputSelector: Selector that indicates the primary input for the actions that should be generated
        :param actionCreationDelegate: Callable delegate that, if set, will be used to generate the action classes.
        Either actionClass or actionCreationDelegate have to be set; but only one of them. ActionBatchGenerator
        assumes that the delegate returns a list of generate action instances. The delegate will be called like the
        action class. A delegate can be used to manipulate the generation of the action instances after the whole
        splitting, sorting, selecting and linking is done.
        @param primaryAlias: Name of the primary input that should be used as argument key if passed to action.
        If not set PRIMARY_INPUT_KEY will be used.
        @param additionalInputSelectors: Dictionary containing additional input selectors for other inputs that should
        be passed to an action instance. Key is the name of an additional input an also the argument name used to pass
        the input to the action instance. The associated dict value must be a selector instance or None to indicate
        that this input will have no data but exists.
        @param splitter: Dictionary specifying a splitter that should be used for a specific input (primary or additional)
        If no splitter is defined explicitly for an input SingleSplitter() will be assumed. The key indicates the
        input that should be associated with the splitter. To associate primary input use PRIMARY_INPUT_KEY as key.The
        values of the dict are the splitter instances that should be used for the respective key.
        @param sorter: Dictionary specifying a sorter that should be used for a specific input (primary or additional)
        If no sorter is defined explicitly for an input BaseSorter() (so no sorting at all) will be assumed.
        The key indicates the input that should be associated with the sorter. To associate primary input use
        PRIMARY_INPUT_KEY as key. The values of the dict are the sorter instances that should be used for the
        respective key.
        @param linker: Dictionary specifying a linker that should be used for a specific additional input
        to link it with the primary input. Thus the master selection passed to the linker will always be provided by
        the primary input.
        If no linker is defined explicitly for an input CaseLinker() (so all inputs must have the same case) will be
        assumed. The key indicates the input that should be associated with the linker. The values of the dict are the
        linker instances that should be used for the respective key.
        @param dependentLinker: Allows to specify linkage for an additional input where the master selection must not
        be the primary input (in contrast to using the linker argument). Thus you can specifies that an additional
        input A is (also) linked to an additional input B. The method assumes the following structure of the variable.
        It is a dictionary. The dictionary key indicates the input that should be linked. So it can be any additional
        input. It must not be the primary input. The value associated with a dict key is an iterable (e.g. list) the
        first element is the name of the input that serves as primary selection for the linkage. It may be any additional input
        (except itself = key of the value) or the primary input. The second element is the linker instance that should
        be used. You may combine linker and dependentLinker specifications for any additional input.
        To associate primary input as master use PRIMARY_INPUT_KEY as value.
        @param relevanceSelector: Selector used to specify for all inputs of actions what is relevant. If not set
        it is assumed that only artefact of type TYPE_VALUE_RESULT are relevant.
        @param session: Session object of the workflow the action is working in
        """
        if session is None:
            # check if we have a current generated global session we can use
            if workflow.currentGeneratedSession is not None:
                self._session = workflow.currentGeneratedSession
            else:
                raise ValueError(
                    "Session passed to the action is invalid. Session is None."
                )
        else:
            self._session = session

        self._actionClass = actionClass
        self._actionCreationDelegate = actionCreationDelegate

        if (not self._actionClass is None) and (
            not self._actionCreationDelegate is None
        ):
            raise RuntimeError(
                "Cannot init ActionBatchGenerator. Both actionClass and actionCreationDelegate are defined."
            )

        if (self._actionClass is None) and (self._actionCreationDelegate is None):
            raise RuntimeError(
                "Cannot init ActionBatchGenerator. Neither actionClass nor actionCreationDelegate is defined."
            )

        self._singleActionParameters = actionParameters

        self._primaryInputSelector = primaryInputSelector

        self._primaryAlias = primaryAlias
        if self._primaryAlias is None:
            self._primaryAlias = self.PRIMARY_INPUT_KEY

        self._additionalInputSelectors = additionalInputSelectors
        if self._additionalInputSelectors is None:
            self._additionalInputSelectors = dict()

        if self.PRIMARY_INPUT_KEY in self._additionalInputSelectors:
            raise ValueError(
                'Additional input selectors passed to the action are invalid. It does contain key value "'
                + self.PRIMARY_INPUT_KEY
                + '" reserved for the primary input channel. Check passed additional input dictionary %s.'.format(
                    self._additionalInputSelectors
                )
            )

        self._splitter = dict()
        if splitter is not None:
            self._splitter = splitter.copy()
        for key in self._additionalInputSelectors:
            if not key in self._splitter:
                self._splitter[key] = SingleSplitter()
        if self._primaryAlias in self._splitter:
            self._splitter[self.PRIMARY_INPUT_KEY] = self._splitter[self._primaryAlias]
            self._splitter.pop(self._primaryAlias)
            logger.debug(
                "Splitter for primary alias detected. Corrected to default PRIMAR_INPUT_KEY."
            )
        if not self.PRIMARY_INPUT_KEY in self._splitter:
            self._splitter[self.PRIMARY_INPUT_KEY] = SingleSplitter()

        self._sorter = dict()
        if sorter is not None:
            self._sorter = sorter.copy()
        for key in self._additionalInputSelectors:
            if not key in self._sorter:
                self._sorter[key] = BaseSorter()
        if self._primaryAlias in self._sorter:
            self._sorter[self.PRIMARY_INPUT_KEY] = self._sorter[self._primaryAlias]
            self._sorter.pop(self._primaryAlias)
            logger.debug(
                "Sorter for primary alias detected. Corrected to default PRIMAR_INPUT_KEY."
            )
        if not self.PRIMARY_INPUT_KEY in self._sorter:
            self._sorter[self.PRIMARY_INPUT_KEY] = BaseSorter()

        self._linker = dict()
        if linker is not None:
            self._linker = linker.copy()
        if self.PRIMARY_INPUT_KEY in self._linker:
            raise ValueError(
                "Primary input can not have a linkage. Invalid linker setting. Check passed dictionary {}.".format(
                    self._dependentLinker
                )
            )

        for key in self._additionalInputSelectors:
            if not key in self._linker:
                self._linker[key] = CaseLinker() + CaseInstanceLinker()

        self._dependentLinker = dict()
        if dependentLinker is not None:
            self._dependentLinker = dependentLinker.copy()
        if self.PRIMARY_INPUT_KEY in self._dependentLinker:
            raise ValueError(
                "Primary input can not have a linkage. Invalid dependentLinker setting. Check passed dictionary {}.".format(
                    self._dependentLinker
                )
            )

        for key in self._dependentLinker:
            if self._dependentLinker[key][0] is key:
                raise ValueError(
                    "Recursive linkage dependency. Input indicates to depend on itself. Check passed dependentLinker dictionary {}.".format(
                        self._dependentLinker
                    )
                )

        self._relevanceSelector = relevanceSelector
        if self._relevanceSelector is None:
            self._relevanceSelector = TypeSelector(artefactProps.TYPE_VALUE_RESULT)

    def _ensureRelevantArtefacts(self, artefacts, infoTag="none"):
        """Helper function that filters the passed artefact list by the passed relevantSelector.
        Returns the list containing the relevant artefacts. If the valid list is empty
        it will be logged as. This function is for batch actions that want to ensure specific
        properties for there artefact before they are used in the batch processing (e.g. only
        artefacts of type "result" are allowed)."""

        result = self._relevanceSelector.getSelection(artefacts)

        if len(result) == 0:
            global logger
            logger.debug(
                "Input selection contains no valid artefacts. Info tag: %s", infoTag
            )

        return result

    def _prepareInputArtifacts(self, inputName):
        """Gets, for one input all artefact form the session, sorts and splits them."""
        artefacts = None

        selector = self._primaryInputSelector
        if not inputName == self.PRIMARY_INPUT_KEY:
            selector = self._additionalInputSelectors[inputName]

        if selector is not None:
            artefacts = selector.getSelection(self._session.artefacts)
            artefacts = self._ensureRelevantArtefacts(artefacts, inputName)

            splitter = self._splitter[inputName]
            splittedArtefacts = splitter.splitSelection(artefacts)

            sortedArtefacts = list()
            for split in splittedArtefacts:
                sortedArtefacts.append(self._sorter[inputName].sortSelection(split))

            artefacts = sortedArtefacts

        return artefacts

    def _generateDependencySequence(self):
        names = self._additionalInputSelectors.keys()
        # Get all inputs that do not depend on others and put it directly in the list
        result = [name for name in names if name not in self._dependentLinker]
        leftNames = list(self._dependentLinker.keys())

        while len(leftNames) > 0:
            masterName = None
            successfull = False
            for leftName in leftNames:
                masterName = self._dependentLinker[leftName][0]
                if masterName in result:
                    result.append(leftName)
                    leftNames.remove(leftName)
                    successfull = True
                    break
            if not successfull:
                raise RuntimeError(
                    "Error in dependent linker definition. Seems to be invald or containes cyclic dependencies. Left dependencies: {}".format(
                        leftNames
                    )
                )
        return result

    def generateActions(self):
        """Method that generates all actions based on the given state of the session and configuration of self.
        For the strategy how the actions are generated see the explination in the class documentation.
        """

        primaryInput = self._prepareInputArtifacts(inputName=self.PRIMARY_INPUT_KEY)

        additionalInputs = dict()
        for key in self._additionalInputSelectors:
            additionalInputs[key] = self._prepareInputArtifacts(inputName=key)

        actions = list()
        depSequence = self._generateDependencySequence()

        for pos, primarySplit in enumerate(primaryInput):
            linkedAdditionals = dict()
            for additionalKey in additionalInputs:
                secondSelections = additionalInputs[additionalKey]
                linkedAdditionals[additionalKey] = None
                if secondSelections is not None:
                    linkedAdditionals[additionalKey] = self._linker[
                        additionalKey
                    ].getLinkedSelection(pos, primaryInput, secondSelections)
            actions.extend(
                self._generateActions_recursive(
                    {self._primaryAlias: primarySplit.copy()},
                    None,
                    linkedAdditionals.copy(),
                    depSequence,
                )
            )

        return actions

    def _generateActions_recursive(
        self,
        relevantAdditionalInputs,
        relevantAdditionalInputPos,
        additionalInputs,
        leftInputNames,
    ):
        actions = list()
        if relevantAdditionalInputPos is None:
            relevantAdditionalInputPos = dict()

        if leftInputNames is None or len(leftInputNames) == 0:
            # check if all relevant inputs are valid
            # emptyInputs = '' # [inputName for inputName in relevantAdditionalInputs if relevantAdditionalInputs[inputName] is None]

            # if len(emptyInputs)>0:
            singleActionParameters = {
                **self._singleActionParameters,
                **relevantAdditionalInputs,
            }
            if self._actionClass is not None:
                action = self._actionClass(**singleActionParameters)
                actions.append(action)
            else:
                newActions = self._actionCreationDelegate(**singleActionParameters)
                actions.extend(newActions)
            # else:
            #    logger.debug('Action candidate was skipped because at least one of the additional inputs is undefined '
            #                 '(empty selection) and therefore no valid action instance can be generated. HINT: If you'
            #                 'want to allow combinations where "There is no valid artefact" (==[None] a as additional input is a '
            #                 'valid option, yempty ')
        else:
            currentName = leftInputNames[0]
            currentInputs = additionalInputs[currentName]

            newLeftNames = leftInputNames[1:]
            newRelInputs = relevantAdditionalInputs.copy()
            newRelPos = relevantAdditionalInputPos.copy()
            newAdditionalInputs = additionalInputs.copy()

            if currentName in self._dependentLinker:
                sourceName = self._dependentLinker[currentName][0]
                linker = self._dependentLinker[currentName][1]
                if additionalInputs[sourceName] is None:
                    currentInputs = None
                    logger.debug(
                        'Dependend linkage has set the selections for input "{}" to None. Reason: Primary dependent'
                        'selection "{}" is also None. Thus no valid linkage can be established as no primary'
                        "input artefacts are defined.".format(currentName, sourceName)
                    )
                elif relevantAdditionalInputPos[sourceName] is None:
                    raise RuntimeError(
                        'Cannot make dependend linkage for "{}". Inner state of the batch generator is invalid.'
                        'relevant dependent primary input "{}" is not processed yed, but should be.'
                        "Error in dependent linker definition. Seems to be invald or containes cyclic"
                        "dependencies.".format(currentName, sourceName)
                    )
                elif currentInputs is not None:
                    currentInputs = linker.getLinkedSelection(
                        relevantAdditionalInputPos[sourceName],
                        additionalInputs[sourceName],
                        currentInputs,
                    )

                newAdditionalInputs[currentName] = currentInputs

            if currentInputs is None:
                newRelPos[currentName] = None
                newRelInputs[currentName] = None
                actions.extend(
                    self._generateActions_recursive(
                        newRelInputs, newRelPos, newAdditionalInputs, newLeftNames
                    )
                )
            elif len(currentInputs) == 0:
                logger.debug(
                    "Action candidate was skipped because at least one of the additional inputs (input name:"
                    f' "{currentName}") is undefined (empty selection) and therefore no valid action instance can be'
                    " generated.\n"
                    'HINT: If you want to allow combinations where "There is no valid artefact" (==[None])'
                    " is a valid option, you have to configure the linker for the input accordingly to allow"
                    " also None as a valid linking option. For more details please see the linker"
                    " documentation."
                )
            else:
                for pos, aSplit in enumerate(currentInputs):
                    newRelPos[currentName] = pos
                    newRelInputs[currentName] = aSplit
                    actions.extend(
                        self._generateActions_recursive(
                            newRelInputs, newRelPos, newAdditionalInputs, newLeftNames
                        )
                    )

        return actions
