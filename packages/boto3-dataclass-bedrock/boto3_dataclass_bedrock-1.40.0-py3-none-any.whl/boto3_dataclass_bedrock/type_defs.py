# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_bedrock import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AgreementAvailability:
    boto3_raw_data: "type_defs.AgreementAvailabilityTypeDef" = dataclasses.field()

    status = field("status")
    errorMessage = field("errorMessage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AgreementAvailabilityTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AgreementAvailabilityTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutomatedReasoningCheckRule:
    boto3_raw_data: "type_defs.AutomatedReasoningCheckRuleTypeDef" = dataclasses.field()

    id = field("id")
    policyVersionArn = field("policyVersionArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AutomatedReasoningCheckRuleTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutomatedReasoningCheckRuleTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutomatedReasoningCheckInputTextReference:
    boto3_raw_data: "type_defs.AutomatedReasoningCheckInputTextReferenceTypeDef" = (
        dataclasses.field()
    )

    text = field("text")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AutomatedReasoningCheckInputTextReferenceTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutomatedReasoningCheckInputTextReferenceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutomatedReasoningLogicStatement:
    boto3_raw_data: "type_defs.AutomatedReasoningLogicStatementTypeDef" = (
        dataclasses.field()
    )

    logic = field("logic")
    naturalLanguage = field("naturalLanguage")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AutomatedReasoningLogicStatementTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutomatedReasoningLogicStatementTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutomatedReasoningPolicyAddRuleAnnotation:
    boto3_raw_data: "type_defs.AutomatedReasoningPolicyAddRuleAnnotationTypeDef" = (
        dataclasses.field()
    )

    expression = field("expression")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AutomatedReasoningPolicyAddRuleAnnotationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutomatedReasoningPolicyAddRuleAnnotationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutomatedReasoningPolicyAddRuleFromNaturalLanguageAnnotation:
    boto3_raw_data: (
        "type_defs.AutomatedReasoningPolicyAddRuleFromNaturalLanguageAnnotationTypeDef"
    ) = dataclasses.field()

    naturalLanguage = field("naturalLanguage")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AutomatedReasoningPolicyAddRuleFromNaturalLanguageAnnotationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.AutomatedReasoningPolicyAddRuleFromNaturalLanguageAnnotationTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutomatedReasoningPolicyDefinitionRule:
    boto3_raw_data: "type_defs.AutomatedReasoningPolicyDefinitionRuleTypeDef" = (
        dataclasses.field()
    )

    id = field("id")
    expression = field("expression")
    alternateExpression = field("alternateExpression")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AutomatedReasoningPolicyDefinitionRuleTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutomatedReasoningPolicyDefinitionRuleTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutomatedReasoningPolicyDefinitionTypeValue:
    boto3_raw_data: "type_defs.AutomatedReasoningPolicyDefinitionTypeValueTypeDef" = (
        dataclasses.field()
    )

    value = field("value")
    description = field("description")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AutomatedReasoningPolicyDefinitionTypeValueTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutomatedReasoningPolicyDefinitionTypeValueTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutomatedReasoningPolicyAddTypeValue:
    boto3_raw_data: "type_defs.AutomatedReasoningPolicyAddTypeValueTypeDef" = (
        dataclasses.field()
    )

    value = field("value")
    description = field("description")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AutomatedReasoningPolicyAddTypeValueTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutomatedReasoningPolicyAddTypeValueTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutomatedReasoningPolicyAddVariableAnnotation:
    boto3_raw_data: "type_defs.AutomatedReasoningPolicyAddVariableAnnotationTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    type = field("type")
    description = field("description")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AutomatedReasoningPolicyAddVariableAnnotationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutomatedReasoningPolicyAddVariableAnnotationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutomatedReasoningPolicyDefinitionVariable:
    boto3_raw_data: "type_defs.AutomatedReasoningPolicyDefinitionVariableTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    type = field("type")
    description = field("description")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AutomatedReasoningPolicyDefinitionVariableTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutomatedReasoningPolicyDefinitionVariableTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutomatedReasoningPolicyDeleteRuleAnnotation:
    boto3_raw_data: "type_defs.AutomatedReasoningPolicyDeleteRuleAnnotationTypeDef" = (
        dataclasses.field()
    )

    ruleId = field("ruleId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AutomatedReasoningPolicyDeleteRuleAnnotationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutomatedReasoningPolicyDeleteRuleAnnotationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutomatedReasoningPolicyDeleteTypeAnnotation:
    boto3_raw_data: "type_defs.AutomatedReasoningPolicyDeleteTypeAnnotationTypeDef" = (
        dataclasses.field()
    )

    name = field("name")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AutomatedReasoningPolicyDeleteTypeAnnotationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutomatedReasoningPolicyDeleteTypeAnnotationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutomatedReasoningPolicyDeleteVariableAnnotation:
    boto3_raw_data: (
        "type_defs.AutomatedReasoningPolicyDeleteVariableAnnotationTypeDef"
    ) = dataclasses.field()

    name = field("name")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AutomatedReasoningPolicyDeleteVariableAnnotationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.AutomatedReasoningPolicyDeleteVariableAnnotationTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutomatedReasoningPolicyIngestContentAnnotation:
    boto3_raw_data: (
        "type_defs.AutomatedReasoningPolicyIngestContentAnnotationTypeDef"
    ) = dataclasses.field()

    content = field("content")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AutomatedReasoningPolicyIngestContentAnnotationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.AutomatedReasoningPolicyIngestContentAnnotationTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutomatedReasoningPolicyUpdateFromRuleFeedbackAnnotationOutput:
    boto3_raw_data: "type_defs.AutomatedReasoningPolicyUpdateFromRuleFeedbackAnnotationOutputTypeDef" = (dataclasses.field())

    feedback = field("feedback")
    ruleIds = field("ruleIds")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AutomatedReasoningPolicyUpdateFromRuleFeedbackAnnotationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.AutomatedReasoningPolicyUpdateFromRuleFeedbackAnnotationOutputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutomatedReasoningPolicyUpdateFromScenarioFeedbackAnnotationOutput:
    boto3_raw_data: "type_defs.AutomatedReasoningPolicyUpdateFromScenarioFeedbackAnnotationOutputTypeDef" = (dataclasses.field())

    scenarioExpression = field("scenarioExpression")
    ruleIds = field("ruleIds")
    feedback = field("feedback")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AutomatedReasoningPolicyUpdateFromScenarioFeedbackAnnotationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.AutomatedReasoningPolicyUpdateFromScenarioFeedbackAnnotationOutputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutomatedReasoningPolicyUpdateRuleAnnotation:
    boto3_raw_data: "type_defs.AutomatedReasoningPolicyUpdateRuleAnnotationTypeDef" = (
        dataclasses.field()
    )

    ruleId = field("ruleId")
    expression = field("expression")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AutomatedReasoningPolicyUpdateRuleAnnotationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutomatedReasoningPolicyUpdateRuleAnnotationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutomatedReasoningPolicyUpdateVariableAnnotation:
    boto3_raw_data: (
        "type_defs.AutomatedReasoningPolicyUpdateVariableAnnotationTypeDef"
    ) = dataclasses.field()

    name = field("name")
    newName = field("newName")
    description = field("description")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AutomatedReasoningPolicyUpdateVariableAnnotationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.AutomatedReasoningPolicyUpdateVariableAnnotationTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutomatedReasoningPolicyBuildStepMessage:
    boto3_raw_data: "type_defs.AutomatedReasoningPolicyBuildStepMessageTypeDef" = (
        dataclasses.field()
    )

    message = field("message")
    messageType = field("messageType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AutomatedReasoningPolicyBuildStepMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutomatedReasoningPolicyBuildStepMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutomatedReasoningPolicyBuildWorkflowSummary:
    boto3_raw_data: "type_defs.AutomatedReasoningPolicyBuildWorkflowSummaryTypeDef" = (
        dataclasses.field()
    )

    policyArn = field("policyArn")
    buildWorkflowId = field("buildWorkflowId")
    status = field("status")
    buildWorkflowType = field("buildWorkflowType")
    createdAt = field("createdAt")
    updatedAt = field("updatedAt")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AutomatedReasoningPolicyBuildWorkflowSummaryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutomatedReasoningPolicyBuildWorkflowSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutomatedReasoningPolicyDefinitionTypeValuePair:
    boto3_raw_data: (
        "type_defs.AutomatedReasoningPolicyDefinitionTypeValuePairTypeDef"
    ) = dataclasses.field()

    typeName = field("typeName")
    valueName = field("valueName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AutomatedReasoningPolicyDefinitionTypeValuePairTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.AutomatedReasoningPolicyDefinitionTypeValuePairTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutomatedReasoningPolicyDisjointRuleSet:
    boto3_raw_data: "type_defs.AutomatedReasoningPolicyDisjointRuleSetTypeDef" = (
        dataclasses.field()
    )

    variables = field("variables")
    rules = field("rules")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AutomatedReasoningPolicyDisjointRuleSetTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutomatedReasoningPolicyDisjointRuleSetTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutomatedReasoningPolicyDeleteRuleMutation:
    boto3_raw_data: "type_defs.AutomatedReasoningPolicyDeleteRuleMutationTypeDef" = (
        dataclasses.field()
    )

    id = field("id")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AutomatedReasoningPolicyDeleteRuleMutationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutomatedReasoningPolicyDeleteRuleMutationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutomatedReasoningPolicyDeleteTypeMutation:
    boto3_raw_data: "type_defs.AutomatedReasoningPolicyDeleteTypeMutationTypeDef" = (
        dataclasses.field()
    )

    name = field("name")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AutomatedReasoningPolicyDeleteTypeMutationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutomatedReasoningPolicyDeleteTypeMutationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutomatedReasoningPolicyDeleteTypeValue:
    boto3_raw_data: "type_defs.AutomatedReasoningPolicyDeleteTypeValueTypeDef" = (
        dataclasses.field()
    )

    value = field("value")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AutomatedReasoningPolicyDeleteTypeValueTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutomatedReasoningPolicyDeleteTypeValueTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutomatedReasoningPolicyDeleteVariableMutation:
    boto3_raw_data: (
        "type_defs.AutomatedReasoningPolicyDeleteVariableMutationTypeDef"
    ) = dataclasses.field()

    name = field("name")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AutomatedReasoningPolicyDeleteVariableMutationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.AutomatedReasoningPolicyDeleteVariableMutationTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutomatedReasoningPolicyScenario:
    boto3_raw_data: "type_defs.AutomatedReasoningPolicyScenarioTypeDef" = (
        dataclasses.field()
    )

    expression = field("expression")
    alternateExpression = field("alternateExpression")
    ruleIds = field("ruleIds")
    expectedResult = field("expectedResult")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AutomatedReasoningPolicyScenarioTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutomatedReasoningPolicyScenarioTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutomatedReasoningPolicySummary:
    boto3_raw_data: "type_defs.AutomatedReasoningPolicySummaryTypeDef" = (
        dataclasses.field()
    )

    policyArn = field("policyArn")
    name = field("name")
    version = field("version")
    policyId = field("policyId")
    createdAt = field("createdAt")
    updatedAt = field("updatedAt")
    description = field("description")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AutomatedReasoningPolicySummaryTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutomatedReasoningPolicySummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutomatedReasoningPolicyTestCase:
    boto3_raw_data: "type_defs.AutomatedReasoningPolicyTestCaseTypeDef" = (
        dataclasses.field()
    )

    testCaseId = field("testCaseId")
    guardContent = field("guardContent")
    createdAt = field("createdAt")
    updatedAt = field("updatedAt")
    queryContent = field("queryContent")
    expectedAggregatedFindingsResult = field("expectedAggregatedFindingsResult")
    confidenceThreshold = field("confidenceThreshold")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AutomatedReasoningPolicyTestCaseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutomatedReasoningPolicyTestCaseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutomatedReasoningPolicyUpdateTypeValue:
    boto3_raw_data: "type_defs.AutomatedReasoningPolicyUpdateTypeValueTypeDef" = (
        dataclasses.field()
    )

    value = field("value")
    newValue = field("newValue")
    description = field("description")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AutomatedReasoningPolicyUpdateTypeValueTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutomatedReasoningPolicyUpdateTypeValueTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutomatedReasoningPolicyUpdateFromRuleFeedbackAnnotation:
    boto3_raw_data: (
        "type_defs.AutomatedReasoningPolicyUpdateFromRuleFeedbackAnnotationTypeDef"
    ) = dataclasses.field()

    feedback = field("feedback")
    ruleIds = field("ruleIds")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AutomatedReasoningPolicyUpdateFromRuleFeedbackAnnotationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.AutomatedReasoningPolicyUpdateFromRuleFeedbackAnnotationTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutomatedReasoningPolicyUpdateFromScenarioFeedbackAnnotation:
    boto3_raw_data: (
        "type_defs.AutomatedReasoningPolicyUpdateFromScenarioFeedbackAnnotationTypeDef"
    ) = dataclasses.field()

    scenarioExpression = field("scenarioExpression")
    ruleIds = field("ruleIds")
    feedback = field("feedback")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AutomatedReasoningPolicyUpdateFromScenarioFeedbackAnnotationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.AutomatedReasoningPolicyUpdateFromScenarioFeedbackAnnotationTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchDeleteEvaluationJobError:
    boto3_raw_data: "type_defs.BatchDeleteEvaluationJobErrorTypeDef" = (
        dataclasses.field()
    )

    jobIdentifier = field("jobIdentifier")
    code = field("code")
    message = field("message")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BatchDeleteEvaluationJobErrorTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchDeleteEvaluationJobErrorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchDeleteEvaluationJobItem:
    boto3_raw_data: "type_defs.BatchDeleteEvaluationJobItemTypeDef" = (
        dataclasses.field()
    )

    jobIdentifier = field("jobIdentifier")
    jobStatus = field("jobStatus")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchDeleteEvaluationJobItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchDeleteEvaluationJobItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchDeleteEvaluationJobRequest:
    boto3_raw_data: "type_defs.BatchDeleteEvaluationJobRequestTypeDef" = (
        dataclasses.field()
    )

    jobIdentifiers = field("jobIdentifiers")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BatchDeleteEvaluationJobRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchDeleteEvaluationJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResponseMetadata:
    boto3_raw_data: "type_defs.ResponseMetadataTypeDef" = dataclasses.field()

    RequestId = field("RequestId")
    HTTPStatusCode = field("HTTPStatusCode")
    HTTPHeaders = field("HTTPHeaders")
    RetryAttempts = field("RetryAttempts")
    HostId = field("HostId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResponseMetadataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResponseMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BedrockEvaluatorModel:
    boto3_raw_data: "type_defs.BedrockEvaluatorModelTypeDef" = dataclasses.field()

    modelIdentifier = field("modelIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BedrockEvaluatorModelTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BedrockEvaluatorModelTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ByteContentDocOutput:
    boto3_raw_data: "type_defs.ByteContentDocOutputTypeDef" = dataclasses.field()

    identifier = field("identifier")
    contentType = field("contentType")
    data = field("data")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ByteContentDocOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ByteContentDocOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelAutomatedReasoningPolicyBuildWorkflowRequest:
    boto3_raw_data: (
        "type_defs.CancelAutomatedReasoningPolicyBuildWorkflowRequestTypeDef"
    ) = dataclasses.field()

    policyArn = field("policyArn")
    buildWorkflowId = field("buildWorkflowId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CancelAutomatedReasoningPolicyBuildWorkflowRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.CancelAutomatedReasoningPolicyBuildWorkflowRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3Config:
    boto3_raw_data: "type_defs.S3ConfigTypeDef" = dataclasses.field()

    bucketName = field("bucketName")
    keyPrefix = field("keyPrefix")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.S3ConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.S3ConfigTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Tag:
    boto3_raw_data: "type_defs.TagTypeDef" = dataclasses.field()

    key = field("key")
    value = field("value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TagTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TagTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAutomatedReasoningPolicyTestCaseRequest:
    boto3_raw_data: "type_defs.CreateAutomatedReasoningPolicyTestCaseRequestTypeDef" = (
        dataclasses.field()
    )

    policyArn = field("policyArn")
    guardContent = field("guardContent")
    expectedAggregatedFindingsResult = field("expectedAggregatedFindingsResult")
    queryContent = field("queryContent")
    clientRequestToken = field("clientRequestToken")
    confidenceThreshold = field("confidenceThreshold")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateAutomatedReasoningPolicyTestCaseRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAutomatedReasoningPolicyTestCaseRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EvaluationOutputDataConfig:
    boto3_raw_data: "type_defs.EvaluationOutputDataConfigTypeDef" = dataclasses.field()

    s3Uri = field("s3Uri")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EvaluationOutputDataConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EvaluationOutputDataConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateFoundationModelAgreementRequest:
    boto3_raw_data: "type_defs.CreateFoundationModelAgreementRequestTypeDef" = (
        dataclasses.field()
    )

    offerToken = field("offerToken")
    modelId = field("modelId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateFoundationModelAgreementRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateFoundationModelAgreementRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GuardrailAutomatedReasoningPolicyConfig:
    boto3_raw_data: "type_defs.GuardrailAutomatedReasoningPolicyConfigTypeDef" = (
        dataclasses.field()
    )

    policies = field("policies")
    confidenceThreshold = field("confidenceThreshold")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GuardrailAutomatedReasoningPolicyConfigTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GuardrailAutomatedReasoningPolicyConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GuardrailCrossRegionConfig:
    boto3_raw_data: "type_defs.GuardrailCrossRegionConfigTypeDef" = dataclasses.field()

    guardrailProfileIdentifier = field("guardrailProfileIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GuardrailCrossRegionConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GuardrailCrossRegionConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateGuardrailVersionRequest:
    boto3_raw_data: "type_defs.CreateGuardrailVersionRequestTypeDef" = (
        dataclasses.field()
    )

    guardrailIdentifier = field("guardrailIdentifier")
    description = field("description")
    clientRequestToken = field("clientRequestToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateGuardrailVersionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateGuardrailVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InferenceProfileModelSource:
    boto3_raw_data: "type_defs.InferenceProfileModelSourceTypeDef" = dataclasses.field()

    copyFrom = field("copyFrom")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InferenceProfileModelSourceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InferenceProfileModelSourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OutputDataConfig:
    boto3_raw_data: "type_defs.OutputDataConfigTypeDef" = dataclasses.field()

    s3Uri = field("s3Uri")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OutputDataConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OutputDataConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PromptRouterTargetModel:
    boto3_raw_data: "type_defs.PromptRouterTargetModelTypeDef" = dataclasses.field()

    modelArn = field("modelArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PromptRouterTargetModelTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PromptRouterTargetModelTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RoutingCriteria:
    boto3_raw_data: "type_defs.RoutingCriteriaTypeDef" = dataclasses.field()

    responseQualityDifference = field("responseQualityDifference")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RoutingCriteriaTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RoutingCriteriaTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomMetricBedrockEvaluatorModel:
    boto3_raw_data: "type_defs.CustomMetricBedrockEvaluatorModelTypeDef" = (
        dataclasses.field()
    )

    modelIdentifier = field("modelIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CustomMetricBedrockEvaluatorModelTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomMetricBedrockEvaluatorModelTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomModelDeploymentSummary:
    boto3_raw_data: "type_defs.CustomModelDeploymentSummaryTypeDef" = (
        dataclasses.field()
    )

    customModelDeploymentArn = field("customModelDeploymentArn")
    customModelDeploymentName = field("customModelDeploymentName")
    modelArn = field("modelArn")
    createdAt = field("createdAt")
    status = field("status")
    lastUpdatedAt = field("lastUpdatedAt")
    failureMessage = field("failureMessage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CustomModelDeploymentSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomModelDeploymentSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomModelSummary:
    boto3_raw_data: "type_defs.CustomModelSummaryTypeDef" = dataclasses.field()

    modelArn = field("modelArn")
    modelName = field("modelName")
    creationTime = field("creationTime")
    baseModelArn = field("baseModelArn")
    baseModelName = field("baseModelName")
    customizationType = field("customizationType")
    ownerAccountId = field("ownerAccountId")
    modelStatus = field("modelStatus")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CustomModelSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomModelSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomModelUnits:
    boto3_raw_data: "type_defs.CustomModelUnitsTypeDef" = dataclasses.field()

    customModelUnitsPerModelCopy = field("customModelUnitsPerModelCopy")
    customModelUnitsVersion = field("customModelUnitsVersion")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CustomModelUnitsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomModelUnitsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataProcessingDetails:
    boto3_raw_data: "type_defs.DataProcessingDetailsTypeDef" = dataclasses.field()

    status = field("status")
    creationTime = field("creationTime")
    lastModifiedTime = field("lastModifiedTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DataProcessingDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataProcessingDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAutomatedReasoningPolicyRequest:
    boto3_raw_data: "type_defs.DeleteAutomatedReasoningPolicyRequestTypeDef" = (
        dataclasses.field()
    )

    policyArn = field("policyArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteAutomatedReasoningPolicyRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAutomatedReasoningPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteCustomModelDeploymentRequest:
    boto3_raw_data: "type_defs.DeleteCustomModelDeploymentRequestTypeDef" = (
        dataclasses.field()
    )

    customModelDeploymentIdentifier = field("customModelDeploymentIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteCustomModelDeploymentRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteCustomModelDeploymentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteCustomModelRequest:
    boto3_raw_data: "type_defs.DeleteCustomModelRequestTypeDef" = dataclasses.field()

    modelIdentifier = field("modelIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteCustomModelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteCustomModelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteFoundationModelAgreementRequest:
    boto3_raw_data: "type_defs.DeleteFoundationModelAgreementRequestTypeDef" = (
        dataclasses.field()
    )

    modelId = field("modelId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteFoundationModelAgreementRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteFoundationModelAgreementRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteGuardrailRequest:
    boto3_raw_data: "type_defs.DeleteGuardrailRequestTypeDef" = dataclasses.field()

    guardrailIdentifier = field("guardrailIdentifier")
    guardrailVersion = field("guardrailVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteGuardrailRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteGuardrailRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteImportedModelRequest:
    boto3_raw_data: "type_defs.DeleteImportedModelRequestTypeDef" = dataclasses.field()

    modelIdentifier = field("modelIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteImportedModelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteImportedModelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteInferenceProfileRequest:
    boto3_raw_data: "type_defs.DeleteInferenceProfileRequestTypeDef" = (
        dataclasses.field()
    )

    inferenceProfileIdentifier = field("inferenceProfileIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteInferenceProfileRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteInferenceProfileRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteMarketplaceModelEndpointRequest:
    boto3_raw_data: "type_defs.DeleteMarketplaceModelEndpointRequestTypeDef" = (
        dataclasses.field()
    )

    endpointArn = field("endpointArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteMarketplaceModelEndpointRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteMarketplaceModelEndpointRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeletePromptRouterRequest:
    boto3_raw_data: "type_defs.DeletePromptRouterRequestTypeDef" = dataclasses.field()

    promptRouterArn = field("promptRouterArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeletePromptRouterRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeletePromptRouterRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteProvisionedModelThroughputRequest:
    boto3_raw_data: "type_defs.DeleteProvisionedModelThroughputRequestTypeDef" = (
        dataclasses.field()
    )

    provisionedModelId = field("provisionedModelId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteProvisionedModelThroughputRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteProvisionedModelThroughputRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeregisterMarketplaceModelEndpointRequest:
    boto3_raw_data: "type_defs.DeregisterMarketplaceModelEndpointRequestTypeDef" = (
        dataclasses.field()
    )

    endpointArn = field("endpointArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeregisterMarketplaceModelEndpointRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeregisterMarketplaceModelEndpointRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DimensionalPriceRate:
    boto3_raw_data: "type_defs.DimensionalPriceRateTypeDef" = dataclasses.field()

    dimension = field("dimension")
    price = field("price")
    description = field("description")
    unit = field("unit")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DimensionalPriceRateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DimensionalPriceRateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TeacherModelConfig:
    boto3_raw_data: "type_defs.TeacherModelConfigTypeDef" = dataclasses.field()

    teacherModelIdentifier = field("teacherModelIdentifier")
    maxResponseLengthForInference = field("maxResponseLengthForInference")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TeacherModelConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TeacherModelConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PerformanceConfiguration:
    boto3_raw_data: "type_defs.PerformanceConfigurationTypeDef" = dataclasses.field()

    latency = field("latency")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PerformanceConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PerformanceConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EvaluationDatasetLocation:
    boto3_raw_data: "type_defs.EvaluationDatasetLocationTypeDef" = dataclasses.field()

    s3Uri = field("s3Uri")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EvaluationDatasetLocationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EvaluationDatasetLocationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EvaluationModelConfigSummary:
    boto3_raw_data: "type_defs.EvaluationModelConfigSummaryTypeDef" = (
        dataclasses.field()
    )

    bedrockModelIdentifiers = field("bedrockModelIdentifiers")
    precomputedInferenceSourceIdentifiers = field(
        "precomputedInferenceSourceIdentifiers"
    )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EvaluationModelConfigSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EvaluationModelConfigSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EvaluationRagConfigSummary:
    boto3_raw_data: "type_defs.EvaluationRagConfigSummaryTypeDef" = dataclasses.field()

    bedrockKnowledgeBaseIdentifiers = field("bedrockKnowledgeBaseIdentifiers")
    precomputedRagSourceIdentifiers = field("precomputedRagSourceIdentifiers")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EvaluationRagConfigSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EvaluationRagConfigSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EvaluationPrecomputedInferenceSource:
    boto3_raw_data: "type_defs.EvaluationPrecomputedInferenceSourceTypeDef" = (
        dataclasses.field()
    )

    inferenceSourceIdentifier = field("inferenceSourceIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.EvaluationPrecomputedInferenceSourceTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EvaluationPrecomputedInferenceSourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EvaluationPrecomputedRetrieveAndGenerateSourceConfig:
    boto3_raw_data: (
        "type_defs.EvaluationPrecomputedRetrieveAndGenerateSourceConfigTypeDef"
    ) = dataclasses.field()

    ragSourceIdentifier = field("ragSourceIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.EvaluationPrecomputedRetrieveAndGenerateSourceConfigTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.EvaluationPrecomputedRetrieveAndGenerateSourceConfigTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EvaluationPrecomputedRetrieveSourceConfig:
    boto3_raw_data: "type_defs.EvaluationPrecomputedRetrieveSourceConfigTypeDef" = (
        dataclasses.field()
    )

    ragSourceIdentifier = field("ragSourceIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.EvaluationPrecomputedRetrieveSourceConfigTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EvaluationPrecomputedRetrieveSourceConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExportAutomatedReasoningPolicyVersionRequest:
    boto3_raw_data: "type_defs.ExportAutomatedReasoningPolicyVersionRequestTypeDef" = (
        dataclasses.field()
    )

    policyArn = field("policyArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ExportAutomatedReasoningPolicyVersionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExportAutomatedReasoningPolicyVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3ObjectDoc:
    boto3_raw_data: "type_defs.S3ObjectDocTypeDef" = dataclasses.field()

    uri = field("uri")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.S3ObjectDocTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.S3ObjectDocTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GuardrailConfiguration:
    boto3_raw_data: "type_defs.GuardrailConfigurationTypeDef" = dataclasses.field()

    guardrailId = field("guardrailId")
    guardrailVersion = field("guardrailVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GuardrailConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GuardrailConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PromptTemplate:
    boto3_raw_data: "type_defs.PromptTemplateTypeDef" = dataclasses.field()

    textPromptTemplate = field("textPromptTemplate")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PromptTemplateTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PromptTemplateTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FieldForReranking:
    boto3_raw_data: "type_defs.FieldForRerankingTypeDef" = dataclasses.field()

    fieldName = field("fieldName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FieldForRerankingTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FieldForRerankingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FilterAttributeOutput:
    boto3_raw_data: "type_defs.FilterAttributeOutputTypeDef" = dataclasses.field()

    key = field("key")
    value = field("value")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FilterAttributeOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FilterAttributeOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FilterAttribute:
    boto3_raw_data: "type_defs.FilterAttributeTypeDef" = dataclasses.field()

    key = field("key")
    value = field("value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FilterAttributeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FilterAttributeTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FoundationModelLifecycle:
    boto3_raw_data: "type_defs.FoundationModelLifecycleTypeDef" = dataclasses.field()

    status = field("status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FoundationModelLifecycleTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FoundationModelLifecycleTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAutomatedReasoningPolicyAnnotationsRequest:
    boto3_raw_data: "type_defs.GetAutomatedReasoningPolicyAnnotationsRequestTypeDef" = (
        dataclasses.field()
    )

    policyArn = field("policyArn")
    buildWorkflowId = field("buildWorkflowId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetAutomatedReasoningPolicyAnnotationsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAutomatedReasoningPolicyAnnotationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAutomatedReasoningPolicyBuildWorkflowRequest:
    boto3_raw_data: (
        "type_defs.GetAutomatedReasoningPolicyBuildWorkflowRequestTypeDef"
    ) = dataclasses.field()

    policyArn = field("policyArn")
    buildWorkflowId = field("buildWorkflowId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetAutomatedReasoningPolicyBuildWorkflowRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.GetAutomatedReasoningPolicyBuildWorkflowRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAutomatedReasoningPolicyBuildWorkflowResultAssetsRequest:
    boto3_raw_data: (
        "type_defs.GetAutomatedReasoningPolicyBuildWorkflowResultAssetsRequestTypeDef"
    ) = dataclasses.field()

    policyArn = field("policyArn")
    buildWorkflowId = field("buildWorkflowId")
    assetType = field("assetType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetAutomatedReasoningPolicyBuildWorkflowResultAssetsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.GetAutomatedReasoningPolicyBuildWorkflowResultAssetsRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAutomatedReasoningPolicyNextScenarioRequest:
    boto3_raw_data: (
        "type_defs.GetAutomatedReasoningPolicyNextScenarioRequestTypeDef"
    ) = dataclasses.field()

    policyArn = field("policyArn")
    buildWorkflowId = field("buildWorkflowId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetAutomatedReasoningPolicyNextScenarioRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.GetAutomatedReasoningPolicyNextScenarioRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAutomatedReasoningPolicyRequest:
    boto3_raw_data: "type_defs.GetAutomatedReasoningPolicyRequestTypeDef" = (
        dataclasses.field()
    )

    policyArn = field("policyArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetAutomatedReasoningPolicyRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAutomatedReasoningPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAutomatedReasoningPolicyTestCaseRequest:
    boto3_raw_data: "type_defs.GetAutomatedReasoningPolicyTestCaseRequestTypeDef" = (
        dataclasses.field()
    )

    policyArn = field("policyArn")
    testCaseId = field("testCaseId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetAutomatedReasoningPolicyTestCaseRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAutomatedReasoningPolicyTestCaseRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAutomatedReasoningPolicyTestResultRequest:
    boto3_raw_data: "type_defs.GetAutomatedReasoningPolicyTestResultRequestTypeDef" = (
        dataclasses.field()
    )

    policyArn = field("policyArn")
    buildWorkflowId = field("buildWorkflowId")
    testCaseId = field("testCaseId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetAutomatedReasoningPolicyTestResultRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAutomatedReasoningPolicyTestResultRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCustomModelDeploymentRequest:
    boto3_raw_data: "type_defs.GetCustomModelDeploymentRequestTypeDef" = (
        dataclasses.field()
    )

    customModelDeploymentIdentifier = field("customModelDeploymentIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetCustomModelDeploymentRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCustomModelDeploymentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCustomModelRequest:
    boto3_raw_data: "type_defs.GetCustomModelRequestTypeDef" = dataclasses.field()

    modelIdentifier = field("modelIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetCustomModelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCustomModelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TrainingMetrics:
    boto3_raw_data: "type_defs.TrainingMetricsTypeDef" = dataclasses.field()

    trainingLoss = field("trainingLoss")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TrainingMetricsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TrainingMetricsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ValidatorMetric:
    boto3_raw_data: "type_defs.ValidatorMetricTypeDef" = dataclasses.field()

    validationLoss = field("validationLoss")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ValidatorMetricTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ValidatorMetricTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEvaluationJobRequest:
    boto3_raw_data: "type_defs.GetEvaluationJobRequestTypeDef" = dataclasses.field()

    jobIdentifier = field("jobIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetEvaluationJobRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEvaluationJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFoundationModelAvailabilityRequest:
    boto3_raw_data: "type_defs.GetFoundationModelAvailabilityRequestTypeDef" = (
        dataclasses.field()
    )

    modelId = field("modelId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetFoundationModelAvailabilityRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFoundationModelAvailabilityRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFoundationModelRequest:
    boto3_raw_data: "type_defs.GetFoundationModelRequestTypeDef" = dataclasses.field()

    modelIdentifier = field("modelIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetFoundationModelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFoundationModelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetGuardrailRequest:
    boto3_raw_data: "type_defs.GetGuardrailRequestTypeDef" = dataclasses.field()

    guardrailIdentifier = field("guardrailIdentifier")
    guardrailVersion = field("guardrailVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetGuardrailRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetGuardrailRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GuardrailAutomatedReasoningPolicy:
    boto3_raw_data: "type_defs.GuardrailAutomatedReasoningPolicyTypeDef" = (
        dataclasses.field()
    )

    policies = field("policies")
    confidenceThreshold = field("confidenceThreshold")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GuardrailAutomatedReasoningPolicyTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GuardrailAutomatedReasoningPolicyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GuardrailCrossRegionDetails:
    boto3_raw_data: "type_defs.GuardrailCrossRegionDetailsTypeDef" = dataclasses.field()

    guardrailProfileId = field("guardrailProfileId")
    guardrailProfileArn = field("guardrailProfileArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GuardrailCrossRegionDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GuardrailCrossRegionDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetImportedModelRequest:
    boto3_raw_data: "type_defs.GetImportedModelRequestTypeDef" = dataclasses.field()

    modelIdentifier = field("modelIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetImportedModelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetImportedModelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetInferenceProfileRequest:
    boto3_raw_data: "type_defs.GetInferenceProfileRequestTypeDef" = dataclasses.field()

    inferenceProfileIdentifier = field("inferenceProfileIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetInferenceProfileRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetInferenceProfileRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InferenceProfileModel:
    boto3_raw_data: "type_defs.InferenceProfileModelTypeDef" = dataclasses.field()

    modelArn = field("modelArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InferenceProfileModelTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InferenceProfileModelTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMarketplaceModelEndpointRequest:
    boto3_raw_data: "type_defs.GetMarketplaceModelEndpointRequestTypeDef" = (
        dataclasses.field()
    )

    endpointArn = field("endpointArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetMarketplaceModelEndpointRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMarketplaceModelEndpointRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetModelCopyJobRequest:
    boto3_raw_data: "type_defs.GetModelCopyJobRequestTypeDef" = dataclasses.field()

    jobArn = field("jobArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetModelCopyJobRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetModelCopyJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetModelCustomizationJobRequest:
    boto3_raw_data: "type_defs.GetModelCustomizationJobRequestTypeDef" = (
        dataclasses.field()
    )

    jobIdentifier = field("jobIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetModelCustomizationJobRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetModelCustomizationJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VpcConfigOutput:
    boto3_raw_data: "type_defs.VpcConfigOutputTypeDef" = dataclasses.field()

    subnetIds = field("subnetIds")
    securityGroupIds = field("securityGroupIds")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VpcConfigOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VpcConfigOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetModelImportJobRequest:
    boto3_raw_data: "type_defs.GetModelImportJobRequestTypeDef" = dataclasses.field()

    jobIdentifier = field("jobIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetModelImportJobRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetModelImportJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetModelInvocationJobRequest:
    boto3_raw_data: "type_defs.GetModelInvocationJobRequestTypeDef" = (
        dataclasses.field()
    )

    jobIdentifier = field("jobIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetModelInvocationJobRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetModelInvocationJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPromptRouterRequest:
    boto3_raw_data: "type_defs.GetPromptRouterRequestTypeDef" = dataclasses.field()

    promptRouterArn = field("promptRouterArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetPromptRouterRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPromptRouterRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetProvisionedModelThroughputRequest:
    boto3_raw_data: "type_defs.GetProvisionedModelThroughputRequestTypeDef" = (
        dataclasses.field()
    )

    provisionedModelId = field("provisionedModelId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetProvisionedModelThroughputRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetProvisionedModelThroughputRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GuardrailContentFilterConfig:
    boto3_raw_data: "type_defs.GuardrailContentFilterConfigTypeDef" = (
        dataclasses.field()
    )

    type = field("type")
    inputStrength = field("inputStrength")
    outputStrength = field("outputStrength")
    inputModalities = field("inputModalities")
    outputModalities = field("outputModalities")
    inputAction = field("inputAction")
    outputAction = field("outputAction")
    inputEnabled = field("inputEnabled")
    outputEnabled = field("outputEnabled")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GuardrailContentFilterConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GuardrailContentFilterConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GuardrailContentFilter:
    boto3_raw_data: "type_defs.GuardrailContentFilterTypeDef" = dataclasses.field()

    type = field("type")
    inputStrength = field("inputStrength")
    outputStrength = field("outputStrength")
    inputModalities = field("inputModalities")
    outputModalities = field("outputModalities")
    inputAction = field("inputAction")
    outputAction = field("outputAction")
    inputEnabled = field("inputEnabled")
    outputEnabled = field("outputEnabled")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GuardrailContentFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GuardrailContentFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GuardrailContentFiltersTierConfig:
    boto3_raw_data: "type_defs.GuardrailContentFiltersTierConfigTypeDef" = (
        dataclasses.field()
    )

    tierName = field("tierName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GuardrailContentFiltersTierConfigTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GuardrailContentFiltersTierConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GuardrailContentFiltersTier:
    boto3_raw_data: "type_defs.GuardrailContentFiltersTierTypeDef" = dataclasses.field()

    tierName = field("tierName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GuardrailContentFiltersTierTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GuardrailContentFiltersTierTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GuardrailContextualGroundingFilterConfig:
    boto3_raw_data: "type_defs.GuardrailContextualGroundingFilterConfigTypeDef" = (
        dataclasses.field()
    )

    type = field("type")
    threshold = field("threshold")
    action = field("action")
    enabled = field("enabled")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GuardrailContextualGroundingFilterConfigTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GuardrailContextualGroundingFilterConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GuardrailContextualGroundingFilter:
    boto3_raw_data: "type_defs.GuardrailContextualGroundingFilterTypeDef" = (
        dataclasses.field()
    )

    type = field("type")
    threshold = field("threshold")
    action = field("action")
    enabled = field("enabled")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GuardrailContextualGroundingFilterTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GuardrailContextualGroundingFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GuardrailManagedWordsConfig:
    boto3_raw_data: "type_defs.GuardrailManagedWordsConfigTypeDef" = dataclasses.field()

    type = field("type")
    inputAction = field("inputAction")
    outputAction = field("outputAction")
    inputEnabled = field("inputEnabled")
    outputEnabled = field("outputEnabled")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GuardrailManagedWordsConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GuardrailManagedWordsConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GuardrailManagedWords:
    boto3_raw_data: "type_defs.GuardrailManagedWordsTypeDef" = dataclasses.field()

    type = field("type")
    inputAction = field("inputAction")
    outputAction = field("outputAction")
    inputEnabled = field("inputEnabled")
    outputEnabled = field("outputEnabled")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GuardrailManagedWordsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GuardrailManagedWordsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GuardrailPiiEntityConfig:
    boto3_raw_data: "type_defs.GuardrailPiiEntityConfigTypeDef" = dataclasses.field()

    type = field("type")
    action = field("action")
    inputAction = field("inputAction")
    outputAction = field("outputAction")
    inputEnabled = field("inputEnabled")
    outputEnabled = field("outputEnabled")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GuardrailPiiEntityConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GuardrailPiiEntityConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GuardrailPiiEntity:
    boto3_raw_data: "type_defs.GuardrailPiiEntityTypeDef" = dataclasses.field()

    type = field("type")
    action = field("action")
    inputAction = field("inputAction")
    outputAction = field("outputAction")
    inputEnabled = field("inputEnabled")
    outputEnabled = field("outputEnabled")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GuardrailPiiEntityTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GuardrailPiiEntityTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GuardrailRegexConfig:
    boto3_raw_data: "type_defs.GuardrailRegexConfigTypeDef" = dataclasses.field()

    name = field("name")
    pattern = field("pattern")
    action = field("action")
    description = field("description")
    inputAction = field("inputAction")
    outputAction = field("outputAction")
    inputEnabled = field("inputEnabled")
    outputEnabled = field("outputEnabled")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GuardrailRegexConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GuardrailRegexConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GuardrailRegex:
    boto3_raw_data: "type_defs.GuardrailRegexTypeDef" = dataclasses.field()

    name = field("name")
    pattern = field("pattern")
    action = field("action")
    description = field("description")
    inputAction = field("inputAction")
    outputAction = field("outputAction")
    inputEnabled = field("inputEnabled")
    outputEnabled = field("outputEnabled")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GuardrailRegexTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GuardrailRegexTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GuardrailTopicConfig:
    boto3_raw_data: "type_defs.GuardrailTopicConfigTypeDef" = dataclasses.field()

    name = field("name")
    definition = field("definition")
    type = field("type")
    examples = field("examples")
    inputAction = field("inputAction")
    outputAction = field("outputAction")
    inputEnabled = field("inputEnabled")
    outputEnabled = field("outputEnabled")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GuardrailTopicConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GuardrailTopicConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GuardrailTopicsTierConfig:
    boto3_raw_data: "type_defs.GuardrailTopicsTierConfigTypeDef" = dataclasses.field()

    tierName = field("tierName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GuardrailTopicsTierConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GuardrailTopicsTierConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GuardrailTopic:
    boto3_raw_data: "type_defs.GuardrailTopicTypeDef" = dataclasses.field()

    name = field("name")
    definition = field("definition")
    examples = field("examples")
    type = field("type")
    inputAction = field("inputAction")
    outputAction = field("outputAction")
    inputEnabled = field("inputEnabled")
    outputEnabled = field("outputEnabled")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GuardrailTopicTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GuardrailTopicTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GuardrailTopicsTier:
    boto3_raw_data: "type_defs.GuardrailTopicsTierTypeDef" = dataclasses.field()

    tierName = field("tierName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GuardrailTopicsTierTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GuardrailTopicsTierTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GuardrailWordConfig:
    boto3_raw_data: "type_defs.GuardrailWordConfigTypeDef" = dataclasses.field()

    text = field("text")
    inputAction = field("inputAction")
    outputAction = field("outputAction")
    inputEnabled = field("inputEnabled")
    outputEnabled = field("outputEnabled")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GuardrailWordConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GuardrailWordConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GuardrailWord:
    boto3_raw_data: "type_defs.GuardrailWordTypeDef" = dataclasses.field()

    text = field("text")
    inputAction = field("inputAction")
    outputAction = field("outputAction")
    inputEnabled = field("inputEnabled")
    outputEnabled = field("outputEnabled")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GuardrailWordTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GuardrailWordTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HumanEvaluationCustomMetric:
    boto3_raw_data: "type_defs.HumanEvaluationCustomMetricTypeDef" = dataclasses.field()

    name = field("name")
    ratingMethod = field("ratingMethod")
    description = field("description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.HumanEvaluationCustomMetricTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HumanEvaluationCustomMetricTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HumanWorkflowConfig:
    boto3_raw_data: "type_defs.HumanWorkflowConfigTypeDef" = dataclasses.field()

    flowDefinitionArn = field("flowDefinitionArn")
    instructions = field("instructions")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.HumanWorkflowConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HumanWorkflowConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetadataAttributeSchema:
    boto3_raw_data: "type_defs.MetadataAttributeSchemaTypeDef" = dataclasses.field()

    key = field("key")
    type = field("type")
    description = field("description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MetadataAttributeSchemaTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MetadataAttributeSchemaTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportedModelSummary:
    boto3_raw_data: "type_defs.ImportedModelSummaryTypeDef" = dataclasses.field()

    modelArn = field("modelArn")
    modelName = field("modelName")
    creationTime = field("creationTime")
    instructSupported = field("instructSupported")
    modelArchitecture = field("modelArchitecture")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImportedModelSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImportedModelSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InvocationLogSource:
    boto3_raw_data: "type_defs.InvocationLogSourceTypeDef" = dataclasses.field()

    s3Uri = field("s3Uri")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InvocationLogSourceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InvocationLogSourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TextInferenceConfigOutput:
    boto3_raw_data: "type_defs.TextInferenceConfigOutputTypeDef" = dataclasses.field()

    temperature = field("temperature")
    topP = field("topP")
    maxTokens = field("maxTokens")
    stopSequences = field("stopSequences")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TextInferenceConfigOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TextInferenceConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TextInferenceConfig:
    boto3_raw_data: "type_defs.TextInferenceConfigTypeDef" = dataclasses.field()

    temperature = field("temperature")
    topP = field("topP")
    maxTokens = field("maxTokens")
    stopSequences = field("stopSequences")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TextInferenceConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TextInferenceConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LegalTerm:
    boto3_raw_data: "type_defs.LegalTermTypeDef" = dataclasses.field()

    url = field("url")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LegalTermTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LegalTermTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PaginatorConfig:
    boto3_raw_data: "type_defs.PaginatorConfigTypeDef" = dataclasses.field()

    MaxItems = field("MaxItems")
    PageSize = field("PageSize")
    StartingToken = field("StartingToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PaginatorConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PaginatorConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAutomatedReasoningPoliciesRequest:
    boto3_raw_data: "type_defs.ListAutomatedReasoningPoliciesRequestTypeDef" = (
        dataclasses.field()
    )

    policyArn = field("policyArn")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAutomatedReasoningPoliciesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAutomatedReasoningPoliciesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAutomatedReasoningPolicyBuildWorkflowsRequest:
    boto3_raw_data: (
        "type_defs.ListAutomatedReasoningPolicyBuildWorkflowsRequestTypeDef"
    ) = dataclasses.field()

    policyArn = field("policyArn")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAutomatedReasoningPolicyBuildWorkflowsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.ListAutomatedReasoningPolicyBuildWorkflowsRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAutomatedReasoningPolicyTestCasesRequest:
    boto3_raw_data: "type_defs.ListAutomatedReasoningPolicyTestCasesRequestTypeDef" = (
        dataclasses.field()
    )

    policyArn = field("policyArn")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAutomatedReasoningPolicyTestCasesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAutomatedReasoningPolicyTestCasesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAutomatedReasoningPolicyTestResultsRequest:
    boto3_raw_data: (
        "type_defs.ListAutomatedReasoningPolicyTestResultsRequestTypeDef"
    ) = dataclasses.field()

    policyArn = field("policyArn")
    buildWorkflowId = field("buildWorkflowId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAutomatedReasoningPolicyTestResultsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.ListAutomatedReasoningPolicyTestResultsRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFoundationModelAgreementOffersRequest:
    boto3_raw_data: "type_defs.ListFoundationModelAgreementOffersRequestTypeDef" = (
        dataclasses.field()
    )

    modelId = field("modelId")
    offerType = field("offerType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListFoundationModelAgreementOffersRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFoundationModelAgreementOffersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFoundationModelsRequest:
    boto3_raw_data: "type_defs.ListFoundationModelsRequestTypeDef" = dataclasses.field()

    byProvider = field("byProvider")
    byCustomizationType = field("byCustomizationType")
    byOutputModality = field("byOutputModality")
    byInferenceType = field("byInferenceType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListFoundationModelsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFoundationModelsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGuardrailsRequest:
    boto3_raw_data: "type_defs.ListGuardrailsRequestTypeDef" = dataclasses.field()

    guardrailIdentifier = field("guardrailIdentifier")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListGuardrailsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGuardrailsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInferenceProfilesRequest:
    boto3_raw_data: "type_defs.ListInferenceProfilesRequestTypeDef" = (
        dataclasses.field()
    )

    maxResults = field("maxResults")
    nextToken = field("nextToken")
    typeEquals = field("typeEquals")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListInferenceProfilesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInferenceProfilesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMarketplaceModelEndpointsRequest:
    boto3_raw_data: "type_defs.ListMarketplaceModelEndpointsRequestTypeDef" = (
        dataclasses.field()
    )

    maxResults = field("maxResults")
    nextToken = field("nextToken")
    modelSourceEquals = field("modelSourceEquals")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListMarketplaceModelEndpointsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMarketplaceModelEndpointsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MarketplaceModelEndpointSummary:
    boto3_raw_data: "type_defs.MarketplaceModelEndpointSummaryTypeDef" = (
        dataclasses.field()
    )

    endpointArn = field("endpointArn")
    modelSourceIdentifier = field("modelSourceIdentifier")
    createdAt = field("createdAt")
    updatedAt = field("updatedAt")
    status = field("status")
    statusMessage = field("statusMessage")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.MarketplaceModelEndpointSummaryTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MarketplaceModelEndpointSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModelImportJobSummary:
    boto3_raw_data: "type_defs.ModelImportJobSummaryTypeDef" = dataclasses.field()

    jobArn = field("jobArn")
    jobName = field("jobName")
    status = field("status")
    creationTime = field("creationTime")
    lastModifiedTime = field("lastModifiedTime")
    endTime = field("endTime")
    importedModelArn = field("importedModelArn")
    importedModelName = field("importedModelName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ModelImportJobSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModelImportJobSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPromptRoutersRequest:
    boto3_raw_data: "type_defs.ListPromptRoutersRequestTypeDef" = dataclasses.field()

    maxResults = field("maxResults")
    nextToken = field("nextToken")
    type = field("type")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPromptRoutersRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPromptRoutersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProvisionedModelSummary:
    boto3_raw_data: "type_defs.ProvisionedModelSummaryTypeDef" = dataclasses.field()

    provisionedModelName = field("provisionedModelName")
    provisionedModelArn = field("provisionedModelArn")
    modelArn = field("modelArn")
    desiredModelArn = field("desiredModelArn")
    foundationModelArn = field("foundationModelArn")
    modelUnits = field("modelUnits")
    desiredModelUnits = field("desiredModelUnits")
    status = field("status")
    creationTime = field("creationTime")
    lastModifiedTime = field("lastModifiedTime")
    commitmentDuration = field("commitmentDuration")
    commitmentExpirationTime = field("commitmentExpirationTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProvisionedModelSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProvisionedModelSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceRequest:
    boto3_raw_data: "type_defs.ListTagsForResourceRequestTypeDef" = dataclasses.field()

    resourceARN = field("resourceARN")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTagsForResourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsForResourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3DataSource:
    boto3_raw_data: "type_defs.S3DataSourceTypeDef" = dataclasses.field()

    s3Uri = field("s3Uri")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.S3DataSourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.S3DataSourceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModelInvocationJobS3InputDataConfig:
    boto3_raw_data: "type_defs.ModelInvocationJobS3InputDataConfigTypeDef" = (
        dataclasses.field()
    )

    s3Uri = field("s3Uri")
    s3InputFormat = field("s3InputFormat")
    s3BucketOwner = field("s3BucketOwner")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ModelInvocationJobS3InputDataConfigTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModelInvocationJobS3InputDataConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModelInvocationJobS3OutputDataConfig:
    boto3_raw_data: "type_defs.ModelInvocationJobS3OutputDataConfigTypeDef" = (
        dataclasses.field()
    )

    s3Uri = field("s3Uri")
    s3EncryptionKeyId = field("s3EncryptionKeyId")
    s3BucketOwner = field("s3BucketOwner")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ModelInvocationJobS3OutputDataConfigTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModelInvocationJobS3OutputDataConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QueryTransformationConfiguration:
    boto3_raw_data: "type_defs.QueryTransformationConfigurationTypeDef" = (
        dataclasses.field()
    )

    type = field("type")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.QueryTransformationConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.QueryTransformationConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RatingScaleItemValue:
    boto3_raw_data: "type_defs.RatingScaleItemValueTypeDef" = dataclasses.field()

    stringValue = field("stringValue")
    floatValue = field("floatValue")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RatingScaleItemValueTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RatingScaleItemValueTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegisterMarketplaceModelEndpointRequest:
    boto3_raw_data: "type_defs.RegisterMarketplaceModelEndpointRequestTypeDef" = (
        dataclasses.field()
    )

    endpointIdentifier = field("endpointIdentifier")
    modelSourceIdentifier = field("modelSourceIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RegisterMarketplaceModelEndpointRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegisterMarketplaceModelEndpointRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RequestMetadataBaseFiltersOutput:
    boto3_raw_data: "type_defs.RequestMetadataBaseFiltersOutputTypeDef" = (
        dataclasses.field()
    )

    equals = field("equals")
    notEquals = field("notEquals")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RequestMetadataBaseFiltersOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RequestMetadataBaseFiltersOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RequestMetadataBaseFilters:
    boto3_raw_data: "type_defs.RequestMetadataBaseFiltersTypeDef" = dataclasses.field()

    equals = field("equals")
    notEquals = field("notEquals")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RequestMetadataBaseFiltersTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RequestMetadataBaseFiltersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VpcConfig:
    boto3_raw_data: "type_defs.VpcConfigTypeDef" = dataclasses.field()

    subnetIds = field("subnetIds")
    securityGroupIds = field("securityGroupIds")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VpcConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VpcConfigTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartAutomatedReasoningPolicyTestWorkflowRequest:
    boto3_raw_data: (
        "type_defs.StartAutomatedReasoningPolicyTestWorkflowRequestTypeDef"
    ) = dataclasses.field()

    policyArn = field("policyArn")
    buildWorkflowId = field("buildWorkflowId")
    testCaseIds = field("testCaseIds")
    clientRequestToken = field("clientRequestToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartAutomatedReasoningPolicyTestWorkflowRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.StartAutomatedReasoningPolicyTestWorkflowRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TrainingDetails:
    boto3_raw_data: "type_defs.TrainingDetailsTypeDef" = dataclasses.field()

    status = field("status")
    creationTime = field("creationTime")
    lastModifiedTime = field("lastModifiedTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TrainingDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TrainingDetailsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ValidationDetails:
    boto3_raw_data: "type_defs.ValidationDetailsTypeDef" = dataclasses.field()

    status = field("status")
    creationTime = field("creationTime")
    lastModifiedTime = field("lastModifiedTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ValidationDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ValidationDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopEvaluationJobRequest:
    boto3_raw_data: "type_defs.StopEvaluationJobRequestTypeDef" = dataclasses.field()

    jobIdentifier = field("jobIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopEvaluationJobRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopEvaluationJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopModelCustomizationJobRequest:
    boto3_raw_data: "type_defs.StopModelCustomizationJobRequestTypeDef" = (
        dataclasses.field()
    )

    jobIdentifier = field("jobIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StopModelCustomizationJobRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopModelCustomizationJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopModelInvocationJobRequest:
    boto3_raw_data: "type_defs.StopModelInvocationJobRequestTypeDef" = (
        dataclasses.field()
    )

    jobIdentifier = field("jobIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StopModelInvocationJobRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopModelInvocationJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SupportTerm:
    boto3_raw_data: "type_defs.SupportTermTypeDef" = dataclasses.field()

    refundPolicyDescription = field("refundPolicyDescription")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SupportTermTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SupportTermTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ValidityTerm:
    boto3_raw_data: "type_defs.ValidityTermTypeDef" = dataclasses.field()

    agreementDuration = field("agreementDuration")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ValidityTermTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ValidityTermTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UntagResourceRequest:
    boto3_raw_data: "type_defs.UntagResourceRequestTypeDef" = dataclasses.field()

    resourceARN = field("resourceARN")
    tagKeys = field("tagKeys")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UntagResourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UntagResourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateProvisionedModelThroughputRequest:
    boto3_raw_data: "type_defs.UpdateProvisionedModelThroughputRequestTypeDef" = (
        dataclasses.field()
    )

    provisionedModelId = field("provisionedModelId")
    desiredProvisionedModelName = field("desiredProvisionedModelName")
    desiredModelId = field("desiredModelId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateProvisionedModelThroughputRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateProvisionedModelThroughputRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Validator:
    boto3_raw_data: "type_defs.ValidatorTypeDef" = dataclasses.field()

    s3Uri = field("s3Uri")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ValidatorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ValidatorTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VectorSearchBedrockRerankingModelConfigurationOutput:
    boto3_raw_data: (
        "type_defs.VectorSearchBedrockRerankingModelConfigurationOutputTypeDef"
    ) = dataclasses.field()

    modelArn = field("modelArn")
    additionalModelRequestFields = field("additionalModelRequestFields")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.VectorSearchBedrockRerankingModelConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.VectorSearchBedrockRerankingModelConfigurationOutputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VectorSearchBedrockRerankingModelConfiguration:
    boto3_raw_data: (
        "type_defs.VectorSearchBedrockRerankingModelConfigurationTypeDef"
    ) = dataclasses.field()

    modelArn = field("modelArn")
    additionalModelRequestFields = field("additionalModelRequestFields")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.VectorSearchBedrockRerankingModelConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.VectorSearchBedrockRerankingModelConfigurationTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutomatedReasoningCheckLogicWarning:
    boto3_raw_data: "type_defs.AutomatedReasoningCheckLogicWarningTypeDef" = (
        dataclasses.field()
    )

    type = field("type")

    @cached_property
    def premises(self):  # pragma: no cover
        return AutomatedReasoningLogicStatement.make_many(
            self.boto3_raw_data["premises"]
        )

    @cached_property
    def claims(self):  # pragma: no cover
        return AutomatedReasoningLogicStatement.make_many(self.boto3_raw_data["claims"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AutomatedReasoningCheckLogicWarningTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutomatedReasoningCheckLogicWarningTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutomatedReasoningCheckScenario:
    boto3_raw_data: "type_defs.AutomatedReasoningCheckScenarioTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def statements(self):  # pragma: no cover
        return AutomatedReasoningLogicStatement.make_many(
            self.boto3_raw_data["statements"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AutomatedReasoningCheckScenarioTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutomatedReasoningCheckScenarioTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutomatedReasoningCheckTranslation:
    boto3_raw_data: "type_defs.AutomatedReasoningCheckTranslationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def claims(self):  # pragma: no cover
        return AutomatedReasoningLogicStatement.make_many(self.boto3_raw_data["claims"])

    confidence = field("confidence")

    @cached_property
    def premises(self):  # pragma: no cover
        return AutomatedReasoningLogicStatement.make_many(
            self.boto3_raw_data["premises"]
        )

    @cached_property
    def untranslatedPremises(self):  # pragma: no cover
        return AutomatedReasoningCheckInputTextReference.make_many(
            self.boto3_raw_data["untranslatedPremises"]
        )

    @cached_property
    def untranslatedClaims(self):  # pragma: no cover
        return AutomatedReasoningCheckInputTextReference.make_many(
            self.boto3_raw_data["untranslatedClaims"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AutomatedReasoningCheckTranslationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutomatedReasoningCheckTranslationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutomatedReasoningPolicyAddRuleMutation:
    boto3_raw_data: "type_defs.AutomatedReasoningPolicyAddRuleMutationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def rule(self):  # pragma: no cover
        return AutomatedReasoningPolicyDefinitionRule.make_one(
            self.boto3_raw_data["rule"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AutomatedReasoningPolicyAddRuleMutationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutomatedReasoningPolicyAddRuleMutationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutomatedReasoningPolicyUpdateRuleMutation:
    boto3_raw_data: "type_defs.AutomatedReasoningPolicyUpdateRuleMutationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def rule(self):  # pragma: no cover
        return AutomatedReasoningPolicyDefinitionRule.make_one(
            self.boto3_raw_data["rule"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AutomatedReasoningPolicyUpdateRuleMutationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutomatedReasoningPolicyUpdateRuleMutationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutomatedReasoningPolicyAddTypeAnnotationOutput:
    boto3_raw_data: (
        "type_defs.AutomatedReasoningPolicyAddTypeAnnotationOutputTypeDef"
    ) = dataclasses.field()

    name = field("name")
    description = field("description")

    @cached_property
    def values(self):  # pragma: no cover
        return AutomatedReasoningPolicyDefinitionTypeValue.make_many(
            self.boto3_raw_data["values"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AutomatedReasoningPolicyAddTypeAnnotationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.AutomatedReasoningPolicyAddTypeAnnotationOutputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutomatedReasoningPolicyAddTypeAnnotation:
    boto3_raw_data: "type_defs.AutomatedReasoningPolicyAddTypeAnnotationTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    description = field("description")

    @cached_property
    def values(self):  # pragma: no cover
        return AutomatedReasoningPolicyDefinitionTypeValue.make_many(
            self.boto3_raw_data["values"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AutomatedReasoningPolicyAddTypeAnnotationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutomatedReasoningPolicyAddTypeAnnotationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutomatedReasoningPolicyDefinitionTypeOutput:
    boto3_raw_data: "type_defs.AutomatedReasoningPolicyDefinitionTypeOutputTypeDef" = (
        dataclasses.field()
    )

    name = field("name")

    @cached_property
    def values(self):  # pragma: no cover
        return AutomatedReasoningPolicyDefinitionTypeValue.make_many(
            self.boto3_raw_data["values"]
        )

    description = field("description")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AutomatedReasoningPolicyDefinitionTypeOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutomatedReasoningPolicyDefinitionTypeOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutomatedReasoningPolicyDefinitionType:
    boto3_raw_data: "type_defs.AutomatedReasoningPolicyDefinitionTypeTypeDef" = (
        dataclasses.field()
    )

    name = field("name")

    @cached_property
    def values(self):  # pragma: no cover
        return AutomatedReasoningPolicyDefinitionTypeValue.make_many(
            self.boto3_raw_data["values"]
        )

    description = field("description")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AutomatedReasoningPolicyDefinitionTypeTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutomatedReasoningPolicyDefinitionTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutomatedReasoningPolicyAddVariableMutation:
    boto3_raw_data: "type_defs.AutomatedReasoningPolicyAddVariableMutationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def variable(self):  # pragma: no cover
        return AutomatedReasoningPolicyDefinitionVariable.make_one(
            self.boto3_raw_data["variable"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AutomatedReasoningPolicyAddVariableMutationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutomatedReasoningPolicyAddVariableMutationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutomatedReasoningPolicyUpdateVariableMutation:
    boto3_raw_data: (
        "type_defs.AutomatedReasoningPolicyUpdateVariableMutationTypeDef"
    ) = dataclasses.field()

    @cached_property
    def variable(self):  # pragma: no cover
        return AutomatedReasoningPolicyDefinitionVariable.make_one(
            self.boto3_raw_data["variable"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AutomatedReasoningPolicyUpdateVariableMutationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.AutomatedReasoningPolicyUpdateVariableMutationTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutomatedReasoningPolicyBuildWorkflowDocument:
    boto3_raw_data: "type_defs.AutomatedReasoningPolicyBuildWorkflowDocumentTypeDef" = (
        dataclasses.field()
    )

    document = field("document")
    documentContentType = field("documentContentType")
    documentName = field("documentName")
    documentDescription = field("documentDescription")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AutomatedReasoningPolicyBuildWorkflowDocumentTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutomatedReasoningPolicyBuildWorkflowDocumentTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ByteContentDoc:
    boto3_raw_data: "type_defs.ByteContentDocTypeDef" = dataclasses.field()

    identifier = field("identifier")
    contentType = field("contentType")
    data = field("data")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ByteContentDocTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ByteContentDocTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutUseCaseForModelAccessRequest:
    boto3_raw_data: "type_defs.PutUseCaseForModelAccessRequestTypeDef" = (
        dataclasses.field()
    )

    formData = field("formData")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PutUseCaseForModelAccessRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutUseCaseForModelAccessRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutomatedReasoningPolicyDefinitionQualityReport:
    boto3_raw_data: (
        "type_defs.AutomatedReasoningPolicyDefinitionQualityReportTypeDef"
    ) = dataclasses.field()

    typeCount = field("typeCount")
    variableCount = field("variableCount")
    ruleCount = field("ruleCount")
    unusedTypes = field("unusedTypes")

    @cached_property
    def unusedTypeValues(self):  # pragma: no cover
        return AutomatedReasoningPolicyDefinitionTypeValuePair.make_many(
            self.boto3_raw_data["unusedTypeValues"]
        )

    unusedVariables = field("unusedVariables")
    conflictingRules = field("conflictingRules")

    @cached_property
    def disjointRuleSets(self):  # pragma: no cover
        return AutomatedReasoningPolicyDisjointRuleSet.make_many(
            self.boto3_raw_data["disjointRuleSets"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AutomatedReasoningPolicyDefinitionQualityReportTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.AutomatedReasoningPolicyDefinitionQualityReportTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutomatedReasoningPolicyTypeValueAnnotation:
    boto3_raw_data: "type_defs.AutomatedReasoningPolicyTypeValueAnnotationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def addTypeValue(self):  # pragma: no cover
        return AutomatedReasoningPolicyAddTypeValue.make_one(
            self.boto3_raw_data["addTypeValue"]
        )

    @cached_property
    def updateTypeValue(self):  # pragma: no cover
        return AutomatedReasoningPolicyUpdateTypeValue.make_one(
            self.boto3_raw_data["updateTypeValue"]
        )

    @cached_property
    def deleteTypeValue(self):  # pragma: no cover
        return AutomatedReasoningPolicyDeleteTypeValue.make_one(
            self.boto3_raw_data["deleteTypeValue"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AutomatedReasoningPolicyTypeValueAnnotationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutomatedReasoningPolicyTypeValueAnnotationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchDeleteEvaluationJobResponse:
    boto3_raw_data: "type_defs.BatchDeleteEvaluationJobResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def errors(self):  # pragma: no cover
        return BatchDeleteEvaluationJobError.make_many(self.boto3_raw_data["errors"])

    @cached_property
    def evaluationJobs(self):  # pragma: no cover
        return BatchDeleteEvaluationJobItem.make_many(
            self.boto3_raw_data["evaluationJobs"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BatchDeleteEvaluationJobResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchDeleteEvaluationJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAutomatedReasoningPolicyResponse:
    boto3_raw_data: "type_defs.CreateAutomatedReasoningPolicyResponseTypeDef" = (
        dataclasses.field()
    )

    policyArn = field("policyArn")
    version = field("version")
    name = field("name")
    description = field("description")
    definitionHash = field("definitionHash")
    createdAt = field("createdAt")
    updatedAt = field("updatedAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateAutomatedReasoningPolicyResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAutomatedReasoningPolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAutomatedReasoningPolicyTestCaseResponse:
    boto3_raw_data: (
        "type_defs.CreateAutomatedReasoningPolicyTestCaseResponseTypeDef"
    ) = dataclasses.field()

    policyArn = field("policyArn")
    testCaseId = field("testCaseId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateAutomatedReasoningPolicyTestCaseResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.CreateAutomatedReasoningPolicyTestCaseResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAutomatedReasoningPolicyVersionResponse:
    boto3_raw_data: "type_defs.CreateAutomatedReasoningPolicyVersionResponseTypeDef" = (
        dataclasses.field()
    )

    policyArn = field("policyArn")
    version = field("version")
    name = field("name")
    description = field("description")
    definitionHash = field("definitionHash")
    createdAt = field("createdAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateAutomatedReasoningPolicyVersionResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAutomatedReasoningPolicyVersionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCustomModelDeploymentResponse:
    boto3_raw_data: "type_defs.CreateCustomModelDeploymentResponseTypeDef" = (
        dataclasses.field()
    )

    customModelDeploymentArn = field("customModelDeploymentArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateCustomModelDeploymentResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCustomModelDeploymentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCustomModelResponse:
    boto3_raw_data: "type_defs.CreateCustomModelResponseTypeDef" = dataclasses.field()

    modelArn = field("modelArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateCustomModelResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCustomModelResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateEvaluationJobResponse:
    boto3_raw_data: "type_defs.CreateEvaluationJobResponseTypeDef" = dataclasses.field()

    jobArn = field("jobArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateEvaluationJobResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateEvaluationJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateFoundationModelAgreementResponse:
    boto3_raw_data: "type_defs.CreateFoundationModelAgreementResponseTypeDef" = (
        dataclasses.field()
    )

    modelId = field("modelId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateFoundationModelAgreementResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateFoundationModelAgreementResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateGuardrailResponse:
    boto3_raw_data: "type_defs.CreateGuardrailResponseTypeDef" = dataclasses.field()

    guardrailId = field("guardrailId")
    guardrailArn = field("guardrailArn")
    version = field("version")
    createdAt = field("createdAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateGuardrailResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateGuardrailResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateGuardrailVersionResponse:
    boto3_raw_data: "type_defs.CreateGuardrailVersionResponseTypeDef" = (
        dataclasses.field()
    )

    guardrailId = field("guardrailId")
    version = field("version")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateGuardrailVersionResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateGuardrailVersionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateInferenceProfileResponse:
    boto3_raw_data: "type_defs.CreateInferenceProfileResponseTypeDef" = (
        dataclasses.field()
    )

    inferenceProfileArn = field("inferenceProfileArn")
    status = field("status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateInferenceProfileResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateInferenceProfileResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateModelCopyJobResponse:
    boto3_raw_data: "type_defs.CreateModelCopyJobResponseTypeDef" = dataclasses.field()

    jobArn = field("jobArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateModelCopyJobResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateModelCopyJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateModelCustomizationJobResponse:
    boto3_raw_data: "type_defs.CreateModelCustomizationJobResponseTypeDef" = (
        dataclasses.field()
    )

    jobArn = field("jobArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateModelCustomizationJobResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateModelCustomizationJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateModelImportJobResponse:
    boto3_raw_data: "type_defs.CreateModelImportJobResponseTypeDef" = (
        dataclasses.field()
    )

    jobArn = field("jobArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateModelImportJobResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateModelImportJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateModelInvocationJobResponse:
    boto3_raw_data: "type_defs.CreateModelInvocationJobResponseTypeDef" = (
        dataclasses.field()
    )

    jobArn = field("jobArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateModelInvocationJobResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateModelInvocationJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePromptRouterResponse:
    boto3_raw_data: "type_defs.CreatePromptRouterResponseTypeDef" = dataclasses.field()

    promptRouterArn = field("promptRouterArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreatePromptRouterResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePromptRouterResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateProvisionedModelThroughputResponse:
    boto3_raw_data: "type_defs.CreateProvisionedModelThroughputResponseTypeDef" = (
        dataclasses.field()
    )

    provisionedModelArn = field("provisionedModelArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateProvisionedModelThroughputResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateProvisionedModelThroughputResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAutomatedReasoningPolicyBuildWorkflowResponse:
    boto3_raw_data: (
        "type_defs.GetAutomatedReasoningPolicyBuildWorkflowResponseTypeDef"
    ) = dataclasses.field()

    policyArn = field("policyArn")
    buildWorkflowId = field("buildWorkflowId")
    status = field("status")
    buildWorkflowType = field("buildWorkflowType")
    documentName = field("documentName")
    documentContentType = field("documentContentType")
    documentDescription = field("documentDescription")
    createdAt = field("createdAt")
    updatedAt = field("updatedAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetAutomatedReasoningPolicyBuildWorkflowResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.GetAutomatedReasoningPolicyBuildWorkflowResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAutomatedReasoningPolicyNextScenarioResponse:
    boto3_raw_data: (
        "type_defs.GetAutomatedReasoningPolicyNextScenarioResponseTypeDef"
    ) = dataclasses.field()

    policyArn = field("policyArn")

    @cached_property
    def scenario(self):  # pragma: no cover
        return AutomatedReasoningPolicyScenario.make_one(
            self.boto3_raw_data["scenario"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetAutomatedReasoningPolicyNextScenarioResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.GetAutomatedReasoningPolicyNextScenarioResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAutomatedReasoningPolicyResponse:
    boto3_raw_data: "type_defs.GetAutomatedReasoningPolicyResponseTypeDef" = (
        dataclasses.field()
    )

    policyArn = field("policyArn")
    name = field("name")
    version = field("version")
    policyId = field("policyId")
    description = field("description")
    definitionHash = field("definitionHash")
    createdAt = field("createdAt")
    updatedAt = field("updatedAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetAutomatedReasoningPolicyResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAutomatedReasoningPolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAutomatedReasoningPolicyTestCaseResponse:
    boto3_raw_data: "type_defs.GetAutomatedReasoningPolicyTestCaseResponseTypeDef" = (
        dataclasses.field()
    )

    policyArn = field("policyArn")

    @cached_property
    def testCase(self):  # pragma: no cover
        return AutomatedReasoningPolicyTestCase.make_one(
            self.boto3_raw_data["testCase"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetAutomatedReasoningPolicyTestCaseResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAutomatedReasoningPolicyTestCaseResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCustomModelDeploymentResponse:
    boto3_raw_data: "type_defs.GetCustomModelDeploymentResponseTypeDef" = (
        dataclasses.field()
    )

    customModelDeploymentArn = field("customModelDeploymentArn")
    modelDeploymentName = field("modelDeploymentName")
    modelArn = field("modelArn")
    createdAt = field("createdAt")
    status = field("status")
    description = field("description")
    failureMessage = field("failureMessage")
    lastUpdatedAt = field("lastUpdatedAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetCustomModelDeploymentResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCustomModelDeploymentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFoundationModelAvailabilityResponse:
    boto3_raw_data: "type_defs.GetFoundationModelAvailabilityResponseTypeDef" = (
        dataclasses.field()
    )

    modelId = field("modelId")

    @cached_property
    def agreementAvailability(self):  # pragma: no cover
        return AgreementAvailability.make_one(
            self.boto3_raw_data["agreementAvailability"]
        )

    authorizationStatus = field("authorizationStatus")
    entitlementAvailability = field("entitlementAvailability")
    regionAvailability = field("regionAvailability")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetFoundationModelAvailabilityResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFoundationModelAvailabilityResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetProvisionedModelThroughputResponse:
    boto3_raw_data: "type_defs.GetProvisionedModelThroughputResponseTypeDef" = (
        dataclasses.field()
    )

    modelUnits = field("modelUnits")
    desiredModelUnits = field("desiredModelUnits")
    provisionedModelName = field("provisionedModelName")
    provisionedModelArn = field("provisionedModelArn")
    modelArn = field("modelArn")
    desiredModelArn = field("desiredModelArn")
    foundationModelArn = field("foundationModelArn")
    status = field("status")
    creationTime = field("creationTime")
    lastModifiedTime = field("lastModifiedTime")
    failureMessage = field("failureMessage")
    commitmentDuration = field("commitmentDuration")
    commitmentExpirationTime = field("commitmentExpirationTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetProvisionedModelThroughputResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetProvisionedModelThroughputResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetUseCaseForModelAccessResponse:
    boto3_raw_data: "type_defs.GetUseCaseForModelAccessResponseTypeDef" = (
        dataclasses.field()
    )

    formData = field("formData")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetUseCaseForModelAccessResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetUseCaseForModelAccessResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAutomatedReasoningPoliciesResponse:
    boto3_raw_data: "type_defs.ListAutomatedReasoningPoliciesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def automatedReasoningPolicySummaries(self):  # pragma: no cover
        return AutomatedReasoningPolicySummary.make_many(
            self.boto3_raw_data["automatedReasoningPolicySummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAutomatedReasoningPoliciesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAutomatedReasoningPoliciesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAutomatedReasoningPolicyBuildWorkflowsResponse:
    boto3_raw_data: (
        "type_defs.ListAutomatedReasoningPolicyBuildWorkflowsResponseTypeDef"
    ) = dataclasses.field()

    @cached_property
    def automatedReasoningPolicyBuildWorkflowSummaries(self):  # pragma: no cover
        return AutomatedReasoningPolicyBuildWorkflowSummary.make_many(
            self.boto3_raw_data["automatedReasoningPolicyBuildWorkflowSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAutomatedReasoningPolicyBuildWorkflowsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.ListAutomatedReasoningPolicyBuildWorkflowsResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAutomatedReasoningPolicyTestCasesResponse:
    boto3_raw_data: "type_defs.ListAutomatedReasoningPolicyTestCasesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def testCases(self):  # pragma: no cover
        return AutomatedReasoningPolicyTestCase.make_many(
            self.boto3_raw_data["testCases"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAutomatedReasoningPolicyTestCasesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAutomatedReasoningPolicyTestCasesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartAutomatedReasoningPolicyBuildWorkflowResponse:
    boto3_raw_data: (
        "type_defs.StartAutomatedReasoningPolicyBuildWorkflowResponseTypeDef"
    ) = dataclasses.field()

    policyArn = field("policyArn")
    buildWorkflowId = field("buildWorkflowId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartAutomatedReasoningPolicyBuildWorkflowResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.StartAutomatedReasoningPolicyBuildWorkflowResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartAutomatedReasoningPolicyTestWorkflowResponse:
    boto3_raw_data: (
        "type_defs.StartAutomatedReasoningPolicyTestWorkflowResponseTypeDef"
    ) = dataclasses.field()

    policyArn = field("policyArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartAutomatedReasoningPolicyTestWorkflowResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.StartAutomatedReasoningPolicyTestWorkflowResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAutomatedReasoningPolicyAnnotationsResponse:
    boto3_raw_data: (
        "type_defs.UpdateAutomatedReasoningPolicyAnnotationsResponseTypeDef"
    ) = dataclasses.field()

    policyArn = field("policyArn")
    buildWorkflowId = field("buildWorkflowId")
    annotationSetHash = field("annotationSetHash")
    updatedAt = field("updatedAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateAutomatedReasoningPolicyAnnotationsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.UpdateAutomatedReasoningPolicyAnnotationsResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAutomatedReasoningPolicyResponse:
    boto3_raw_data: "type_defs.UpdateAutomatedReasoningPolicyResponseTypeDef" = (
        dataclasses.field()
    )

    policyArn = field("policyArn")
    name = field("name")
    definitionHash = field("definitionHash")
    updatedAt = field("updatedAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateAutomatedReasoningPolicyResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAutomatedReasoningPolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAutomatedReasoningPolicyTestCaseResponse:
    boto3_raw_data: (
        "type_defs.UpdateAutomatedReasoningPolicyTestCaseResponseTypeDef"
    ) = dataclasses.field()

    policyArn = field("policyArn")
    testCaseId = field("testCaseId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateAutomatedReasoningPolicyTestCaseResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.UpdateAutomatedReasoningPolicyTestCaseResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateGuardrailResponse:
    boto3_raw_data: "type_defs.UpdateGuardrailResponseTypeDef" = dataclasses.field()

    guardrailId = field("guardrailId")
    guardrailArn = field("guardrailArn")
    version = field("version")
    updatedAt = field("updatedAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateGuardrailResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateGuardrailResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EvaluatorModelConfigOutput:
    boto3_raw_data: "type_defs.EvaluatorModelConfigOutputTypeDef" = dataclasses.field()

    @cached_property
    def bedrockEvaluatorModels(self):  # pragma: no cover
        return BedrockEvaluatorModel.make_many(
            self.boto3_raw_data["bedrockEvaluatorModels"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EvaluatorModelConfigOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EvaluatorModelConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EvaluatorModelConfig:
    boto3_raw_data: "type_defs.EvaluatorModelConfigTypeDef" = dataclasses.field()

    @cached_property
    def bedrockEvaluatorModels(self):  # pragma: no cover
        return BedrockEvaluatorModel.make_many(
            self.boto3_raw_data["bedrockEvaluatorModels"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EvaluatorModelConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EvaluatorModelConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CloudWatchConfig:
    boto3_raw_data: "type_defs.CloudWatchConfigTypeDef" = dataclasses.field()

    logGroupName = field("logGroupName")
    roleArn = field("roleArn")

    @cached_property
    def largeDataDeliveryS3Config(self):  # pragma: no cover
        return S3Config.make_one(self.boto3_raw_data["largeDataDeliveryS3Config"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CloudWatchConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CloudWatchConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAutomatedReasoningPolicyVersionRequest:
    boto3_raw_data: "type_defs.CreateAutomatedReasoningPolicyVersionRequestTypeDef" = (
        dataclasses.field()
    )

    policyArn = field("policyArn")
    lastUpdatedDefinitionHash = field("lastUpdatedDefinitionHash")
    clientRequestToken = field("clientRequestToken")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateAutomatedReasoningPolicyVersionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAutomatedReasoningPolicyVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCustomModelDeploymentRequest:
    boto3_raw_data: "type_defs.CreateCustomModelDeploymentRequestTypeDef" = (
        dataclasses.field()
    )

    modelDeploymentName = field("modelDeploymentName")
    modelArn = field("modelArn")
    description = field("description")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    clientRequestToken = field("clientRequestToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateCustomModelDeploymentRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCustomModelDeploymentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateModelCopyJobRequest:
    boto3_raw_data: "type_defs.CreateModelCopyJobRequestTypeDef" = dataclasses.field()

    sourceModelArn = field("sourceModelArn")
    targetModelName = field("targetModelName")
    modelKmsKeyId = field("modelKmsKeyId")

    @cached_property
    def targetModelTags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["targetModelTags"])

    clientRequestToken = field("clientRequestToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateModelCopyJobRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateModelCopyJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateProvisionedModelThroughputRequest:
    boto3_raw_data: "type_defs.CreateProvisionedModelThroughputRequestTypeDef" = (
        dataclasses.field()
    )

    modelUnits = field("modelUnits")
    provisionedModelName = field("provisionedModelName")
    modelId = field("modelId")
    clientRequestToken = field("clientRequestToken")
    commitmentDuration = field("commitmentDuration")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateProvisionedModelThroughputRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateProvisionedModelThroughputRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetModelCopyJobResponse:
    boto3_raw_data: "type_defs.GetModelCopyJobResponseTypeDef" = dataclasses.field()

    jobArn = field("jobArn")
    status = field("status")
    creationTime = field("creationTime")
    targetModelArn = field("targetModelArn")
    targetModelName = field("targetModelName")
    sourceAccountId = field("sourceAccountId")
    sourceModelArn = field("sourceModelArn")
    targetModelKmsKeyArn = field("targetModelKmsKeyArn")

    @cached_property
    def targetModelTags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["targetModelTags"])

    failureMessage = field("failureMessage")
    sourceModelName = field("sourceModelName")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetModelCopyJobResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetModelCopyJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceResponse:
    boto3_raw_data: "type_defs.ListTagsForResourceResponseTypeDef" = dataclasses.field()

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTagsForResourceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsForResourceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModelCopyJobSummary:
    boto3_raw_data: "type_defs.ModelCopyJobSummaryTypeDef" = dataclasses.field()

    jobArn = field("jobArn")
    status = field("status")
    creationTime = field("creationTime")
    targetModelArn = field("targetModelArn")
    sourceAccountId = field("sourceAccountId")
    sourceModelArn = field("sourceModelArn")
    targetModelName = field("targetModelName")
    targetModelKmsKeyArn = field("targetModelKmsKeyArn")

    @cached_property
    def targetModelTags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["targetModelTags"])

    failureMessage = field("failureMessage")
    sourceModelName = field("sourceModelName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ModelCopyJobSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModelCopyJobSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TagResourceRequest:
    boto3_raw_data: "type_defs.TagResourceRequestTypeDef" = dataclasses.field()

    resourceARN = field("resourceARN")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TagResourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TagResourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateInferenceProfileRequest:
    boto3_raw_data: "type_defs.CreateInferenceProfileRequestTypeDef" = (
        dataclasses.field()
    )

    inferenceProfileName = field("inferenceProfileName")

    @cached_property
    def modelSource(self):  # pragma: no cover
        return InferenceProfileModelSource.make_one(self.boto3_raw_data["modelSource"])

    description = field("description")
    clientRequestToken = field("clientRequestToken")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateInferenceProfileRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateInferenceProfileRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePromptRouterRequest:
    boto3_raw_data: "type_defs.CreatePromptRouterRequestTypeDef" = dataclasses.field()

    promptRouterName = field("promptRouterName")

    @cached_property
    def models(self):  # pragma: no cover
        return PromptRouterTargetModel.make_many(self.boto3_raw_data["models"])

    @cached_property
    def routingCriteria(self):  # pragma: no cover
        return RoutingCriteria.make_one(self.boto3_raw_data["routingCriteria"])

    @cached_property
    def fallbackModel(self):  # pragma: no cover
        return PromptRouterTargetModel.make_one(self.boto3_raw_data["fallbackModel"])

    clientRequestToken = field("clientRequestToken")
    description = field("description")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreatePromptRouterRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePromptRouterRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPromptRouterResponse:
    boto3_raw_data: "type_defs.GetPromptRouterResponseTypeDef" = dataclasses.field()

    promptRouterName = field("promptRouterName")

    @cached_property
    def routingCriteria(self):  # pragma: no cover
        return RoutingCriteria.make_one(self.boto3_raw_data["routingCriteria"])

    description = field("description")
    createdAt = field("createdAt")
    updatedAt = field("updatedAt")
    promptRouterArn = field("promptRouterArn")

    @cached_property
    def models(self):  # pragma: no cover
        return PromptRouterTargetModel.make_many(self.boto3_raw_data["models"])

    @cached_property
    def fallbackModel(self):  # pragma: no cover
        return PromptRouterTargetModel.make_one(self.boto3_raw_data["fallbackModel"])

    status = field("status")
    type = field("type")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetPromptRouterResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPromptRouterResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PromptRouterSummary:
    boto3_raw_data: "type_defs.PromptRouterSummaryTypeDef" = dataclasses.field()

    promptRouterName = field("promptRouterName")

    @cached_property
    def routingCriteria(self):  # pragma: no cover
        return RoutingCriteria.make_one(self.boto3_raw_data["routingCriteria"])

    promptRouterArn = field("promptRouterArn")

    @cached_property
    def models(self):  # pragma: no cover
        return PromptRouterTargetModel.make_many(self.boto3_raw_data["models"])

    @cached_property
    def fallbackModel(self):  # pragma: no cover
        return PromptRouterTargetModel.make_one(self.boto3_raw_data["fallbackModel"])

    status = field("status")
    type = field("type")
    description = field("description")
    createdAt = field("createdAt")
    updatedAt = field("updatedAt")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PromptRouterSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PromptRouterSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomMetricEvaluatorModelConfigOutput:
    boto3_raw_data: "type_defs.CustomMetricEvaluatorModelConfigOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def bedrockEvaluatorModels(self):  # pragma: no cover
        return CustomMetricBedrockEvaluatorModel.make_many(
            self.boto3_raw_data["bedrockEvaluatorModels"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CustomMetricEvaluatorModelConfigOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomMetricEvaluatorModelConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomMetricEvaluatorModelConfig:
    boto3_raw_data: "type_defs.CustomMetricEvaluatorModelConfigTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def bedrockEvaluatorModels(self):  # pragma: no cover
        return CustomMetricBedrockEvaluatorModel.make_many(
            self.boto3_raw_data["bedrockEvaluatorModels"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CustomMetricEvaluatorModelConfigTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomMetricEvaluatorModelConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCustomModelDeploymentsResponse:
    boto3_raw_data: "type_defs.ListCustomModelDeploymentsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def modelDeploymentSummaries(self):  # pragma: no cover
        return CustomModelDeploymentSummary.make_many(
            self.boto3_raw_data["modelDeploymentSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCustomModelDeploymentsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCustomModelDeploymentsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCustomModelsResponse:
    boto3_raw_data: "type_defs.ListCustomModelsResponseTypeDef" = dataclasses.field()

    @cached_property
    def modelSummaries(self):  # pragma: no cover
        return CustomModelSummary.make_many(self.boto3_raw_data["modelSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListCustomModelsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCustomModelsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAutomatedReasoningPolicyBuildWorkflowRequest:
    boto3_raw_data: (
        "type_defs.DeleteAutomatedReasoningPolicyBuildWorkflowRequestTypeDef"
    ) = dataclasses.field()

    policyArn = field("policyArn")
    buildWorkflowId = field("buildWorkflowId")
    lastUpdatedAt = field("lastUpdatedAt")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteAutomatedReasoningPolicyBuildWorkflowRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.DeleteAutomatedReasoningPolicyBuildWorkflowRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAutomatedReasoningPolicyTestCaseRequest:
    boto3_raw_data: "type_defs.DeleteAutomatedReasoningPolicyTestCaseRequestTypeDef" = (
        dataclasses.field()
    )

    policyArn = field("policyArn")
    testCaseId = field("testCaseId")
    lastUpdatedAt = field("lastUpdatedAt")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteAutomatedReasoningPolicyTestCaseRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAutomatedReasoningPolicyTestCaseRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCustomModelDeploymentsRequest:
    boto3_raw_data: "type_defs.ListCustomModelDeploymentsRequestTypeDef" = (
        dataclasses.field()
    )

    createdBefore = field("createdBefore")
    createdAfter = field("createdAfter")
    nameContains = field("nameContains")
    maxResults = field("maxResults")
    nextToken = field("nextToken")
    sortBy = field("sortBy")
    sortOrder = field("sortOrder")
    statusEquals = field("statusEquals")
    modelArnEquals = field("modelArnEquals")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCustomModelDeploymentsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCustomModelDeploymentsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCustomModelsRequest:
    boto3_raw_data: "type_defs.ListCustomModelsRequestTypeDef" = dataclasses.field()

    creationTimeBefore = field("creationTimeBefore")
    creationTimeAfter = field("creationTimeAfter")
    nameContains = field("nameContains")
    baseModelArnEquals = field("baseModelArnEquals")
    foundationModelArnEquals = field("foundationModelArnEquals")
    maxResults = field("maxResults")
    nextToken = field("nextToken")
    sortBy = field("sortBy")
    sortOrder = field("sortOrder")
    isOwned = field("isOwned")
    modelStatus = field("modelStatus")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListCustomModelsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCustomModelsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEvaluationJobsRequest:
    boto3_raw_data: "type_defs.ListEvaluationJobsRequestTypeDef" = dataclasses.field()

    creationTimeAfter = field("creationTimeAfter")
    creationTimeBefore = field("creationTimeBefore")
    statusEquals = field("statusEquals")
    applicationTypeEquals = field("applicationTypeEquals")
    nameContains = field("nameContains")
    maxResults = field("maxResults")
    nextToken = field("nextToken")
    sortBy = field("sortBy")
    sortOrder = field("sortOrder")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListEvaluationJobsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEvaluationJobsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListImportedModelsRequest:
    boto3_raw_data: "type_defs.ListImportedModelsRequestTypeDef" = dataclasses.field()

    creationTimeBefore = field("creationTimeBefore")
    creationTimeAfter = field("creationTimeAfter")
    nameContains = field("nameContains")
    maxResults = field("maxResults")
    nextToken = field("nextToken")
    sortBy = field("sortBy")
    sortOrder = field("sortOrder")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListImportedModelsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListImportedModelsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListModelCopyJobsRequest:
    boto3_raw_data: "type_defs.ListModelCopyJobsRequestTypeDef" = dataclasses.field()

    creationTimeAfter = field("creationTimeAfter")
    creationTimeBefore = field("creationTimeBefore")
    statusEquals = field("statusEquals")
    sourceAccountEquals = field("sourceAccountEquals")
    sourceModelArnEquals = field("sourceModelArnEquals")
    targetModelNameContains = field("targetModelNameContains")
    maxResults = field("maxResults")
    nextToken = field("nextToken")
    sortBy = field("sortBy")
    sortOrder = field("sortOrder")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListModelCopyJobsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListModelCopyJobsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListModelCustomizationJobsRequest:
    boto3_raw_data: "type_defs.ListModelCustomizationJobsRequestTypeDef" = (
        dataclasses.field()
    )

    creationTimeAfter = field("creationTimeAfter")
    creationTimeBefore = field("creationTimeBefore")
    statusEquals = field("statusEquals")
    nameContains = field("nameContains")
    maxResults = field("maxResults")
    nextToken = field("nextToken")
    sortBy = field("sortBy")
    sortOrder = field("sortOrder")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListModelCustomizationJobsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListModelCustomizationJobsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListModelImportJobsRequest:
    boto3_raw_data: "type_defs.ListModelImportJobsRequestTypeDef" = dataclasses.field()

    creationTimeAfter = field("creationTimeAfter")
    creationTimeBefore = field("creationTimeBefore")
    statusEquals = field("statusEquals")
    nameContains = field("nameContains")
    maxResults = field("maxResults")
    nextToken = field("nextToken")
    sortBy = field("sortBy")
    sortOrder = field("sortOrder")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListModelImportJobsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListModelImportJobsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListModelInvocationJobsRequest:
    boto3_raw_data: "type_defs.ListModelInvocationJobsRequestTypeDef" = (
        dataclasses.field()
    )

    submitTimeAfter = field("submitTimeAfter")
    submitTimeBefore = field("submitTimeBefore")
    statusEquals = field("statusEquals")
    nameContains = field("nameContains")
    maxResults = field("maxResults")
    nextToken = field("nextToken")
    sortBy = field("sortBy")
    sortOrder = field("sortOrder")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListModelInvocationJobsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListModelInvocationJobsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListProvisionedModelThroughputsRequest:
    boto3_raw_data: "type_defs.ListProvisionedModelThroughputsRequestTypeDef" = (
        dataclasses.field()
    )

    creationTimeAfter = field("creationTimeAfter")
    creationTimeBefore = field("creationTimeBefore")
    statusEquals = field("statusEquals")
    modelArnEquals = field("modelArnEquals")
    nameContains = field("nameContains")
    maxResults = field("maxResults")
    nextToken = field("nextToken")
    sortBy = field("sortBy")
    sortOrder = field("sortOrder")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListProvisionedModelThroughputsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListProvisionedModelThroughputsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAutomatedReasoningPolicyTestCaseRequest:
    boto3_raw_data: "type_defs.UpdateAutomatedReasoningPolicyTestCaseRequestTypeDef" = (
        dataclasses.field()
    )

    policyArn = field("policyArn")
    testCaseId = field("testCaseId")
    guardContent = field("guardContent")
    lastUpdatedAt = field("lastUpdatedAt")
    expectedAggregatedFindingsResult = field("expectedAggregatedFindingsResult")
    queryContent = field("queryContent")
    confidenceThreshold = field("confidenceThreshold")
    clientRequestToken = field("clientRequestToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateAutomatedReasoningPolicyTestCaseRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAutomatedReasoningPolicyTestCaseRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PricingTerm:
    boto3_raw_data: "type_defs.PricingTermTypeDef" = dataclasses.field()

    @cached_property
    def rateCard(self):  # pragma: no cover
        return DimensionalPriceRate.make_many(self.boto3_raw_data["rateCard"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PricingTermTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PricingTermTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DistillationConfig:
    boto3_raw_data: "type_defs.DistillationConfigTypeDef" = dataclasses.field()

    @cached_property
    def teacherModelConfig(self):  # pragma: no cover
        return TeacherModelConfig.make_one(self.boto3_raw_data["teacherModelConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DistillationConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DistillationConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EvaluationBedrockModel:
    boto3_raw_data: "type_defs.EvaluationBedrockModelTypeDef" = dataclasses.field()

    modelIdentifier = field("modelIdentifier")
    inferenceParams = field("inferenceParams")

    @cached_property
    def performanceConfig(self):  # pragma: no cover
        return PerformanceConfiguration.make_one(
            self.boto3_raw_data["performanceConfig"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EvaluationBedrockModelTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EvaluationBedrockModelTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EvaluationDataset:
    boto3_raw_data: "type_defs.EvaluationDatasetTypeDef" = dataclasses.field()

    name = field("name")

    @cached_property
    def datasetLocation(self):  # pragma: no cover
        return EvaluationDatasetLocation.make_one(
            self.boto3_raw_data["datasetLocation"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EvaluationDatasetTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EvaluationDatasetTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EvaluationInferenceConfigSummary:
    boto3_raw_data: "type_defs.EvaluationInferenceConfigSummaryTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def modelConfigSummary(self):  # pragma: no cover
        return EvaluationModelConfigSummary.make_one(
            self.boto3_raw_data["modelConfigSummary"]
        )

    @cached_property
    def ragConfigSummary(self):  # pragma: no cover
        return EvaluationRagConfigSummary.make_one(
            self.boto3_raw_data["ragConfigSummary"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.EvaluationInferenceConfigSummaryTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EvaluationInferenceConfigSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EvaluationPrecomputedRagSourceConfig:
    boto3_raw_data: "type_defs.EvaluationPrecomputedRagSourceConfigTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def retrieveSourceConfig(self):  # pragma: no cover
        return EvaluationPrecomputedRetrieveSourceConfig.make_one(
            self.boto3_raw_data["retrieveSourceConfig"]
        )

    @cached_property
    def retrieveAndGenerateSourceConfig(self):  # pragma: no cover
        return EvaluationPrecomputedRetrieveAndGenerateSourceConfig.make_one(
            self.boto3_raw_data["retrieveAndGenerateSourceConfig"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.EvaluationPrecomputedRagSourceConfigTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EvaluationPrecomputedRagSourceConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExternalSourceOutput:
    boto3_raw_data: "type_defs.ExternalSourceOutputTypeDef" = dataclasses.field()

    sourceType = field("sourceType")

    @cached_property
    def s3Location(self):  # pragma: no cover
        return S3ObjectDoc.make_one(self.boto3_raw_data["s3Location"])

    @cached_property
    def byteContent(self):  # pragma: no cover
        return ByteContentDocOutput.make_one(self.boto3_raw_data["byteContent"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExternalSourceOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExternalSourceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RerankingMetadataSelectiveModeConfigurationOutput:
    boto3_raw_data: (
        "type_defs.RerankingMetadataSelectiveModeConfigurationOutputTypeDef"
    ) = dataclasses.field()

    @cached_property
    def fieldsToInclude(self):  # pragma: no cover
        return FieldForReranking.make_many(self.boto3_raw_data["fieldsToInclude"])

    @cached_property
    def fieldsToExclude(self):  # pragma: no cover
        return FieldForReranking.make_many(self.boto3_raw_data["fieldsToExclude"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RerankingMetadataSelectiveModeConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.RerankingMetadataSelectiveModeConfigurationOutputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RerankingMetadataSelectiveModeConfiguration:
    boto3_raw_data: "type_defs.RerankingMetadataSelectiveModeConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def fieldsToInclude(self):  # pragma: no cover
        return FieldForReranking.make_many(self.boto3_raw_data["fieldsToInclude"])

    @cached_property
    def fieldsToExclude(self):  # pragma: no cover
        return FieldForReranking.make_many(self.boto3_raw_data["fieldsToExclude"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RerankingMetadataSelectiveModeConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RerankingMetadataSelectiveModeConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RetrievalFilterOutput:
    boto3_raw_data: "type_defs.RetrievalFilterOutputTypeDef" = dataclasses.field()

    @cached_property
    def equals(self):  # pragma: no cover
        return FilterAttributeOutput.make_one(self.boto3_raw_data["equals"])

    @cached_property
    def notEquals(self):  # pragma: no cover
        return FilterAttributeOutput.make_one(self.boto3_raw_data["notEquals"])

    @cached_property
    def greaterThan(self):  # pragma: no cover
        return FilterAttributeOutput.make_one(self.boto3_raw_data["greaterThan"])

    @cached_property
    def greaterThanOrEquals(self):  # pragma: no cover
        return FilterAttributeOutput.make_one(
            self.boto3_raw_data["greaterThanOrEquals"]
        )

    @cached_property
    def lessThan(self):  # pragma: no cover
        return FilterAttributeOutput.make_one(self.boto3_raw_data["lessThan"])

    @cached_property
    def lessThanOrEquals(self):  # pragma: no cover
        return FilterAttributeOutput.make_one(self.boto3_raw_data["lessThanOrEquals"])

    @cached_property
    def in_(self):  # pragma: no cover
        return FilterAttributeOutput.make_one(self.boto3_raw_data["in"])

    @cached_property
    def notIn(self):  # pragma: no cover
        return FilterAttributeOutput.make_one(self.boto3_raw_data["notIn"])

    @cached_property
    def startsWith(self):  # pragma: no cover
        return FilterAttributeOutput.make_one(self.boto3_raw_data["startsWith"])

    @cached_property
    def listContains(self):  # pragma: no cover
        return FilterAttributeOutput.make_one(self.boto3_raw_data["listContains"])

    @cached_property
    def stringContains(self):  # pragma: no cover
        return FilterAttributeOutput.make_one(self.boto3_raw_data["stringContains"])

    andAll = field("andAll")
    orAll = field("orAll")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RetrievalFilterOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RetrievalFilterOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RetrievalFilter:
    boto3_raw_data: "type_defs.RetrievalFilterTypeDef" = dataclasses.field()

    @cached_property
    def equals(self):  # pragma: no cover
        return FilterAttribute.make_one(self.boto3_raw_data["equals"])

    @cached_property
    def notEquals(self):  # pragma: no cover
        return FilterAttribute.make_one(self.boto3_raw_data["notEquals"])

    @cached_property
    def greaterThan(self):  # pragma: no cover
        return FilterAttribute.make_one(self.boto3_raw_data["greaterThan"])

    @cached_property
    def greaterThanOrEquals(self):  # pragma: no cover
        return FilterAttribute.make_one(self.boto3_raw_data["greaterThanOrEquals"])

    @cached_property
    def lessThan(self):  # pragma: no cover
        return FilterAttribute.make_one(self.boto3_raw_data["lessThan"])

    @cached_property
    def lessThanOrEquals(self):  # pragma: no cover
        return FilterAttribute.make_one(self.boto3_raw_data["lessThanOrEquals"])

    @cached_property
    def in_(self):  # pragma: no cover
        return FilterAttribute.make_one(self.boto3_raw_data["in"])

    @cached_property
    def notIn(self):  # pragma: no cover
        return FilterAttribute.make_one(self.boto3_raw_data["notIn"])

    @cached_property
    def startsWith(self):  # pragma: no cover
        return FilterAttribute.make_one(self.boto3_raw_data["startsWith"])

    @cached_property
    def listContains(self):  # pragma: no cover
        return FilterAttribute.make_one(self.boto3_raw_data["listContains"])

    @cached_property
    def stringContains(self):  # pragma: no cover
        return FilterAttribute.make_one(self.boto3_raw_data["stringContains"])

    andAll = field("andAll")
    orAll = field("orAll")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RetrievalFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RetrievalFilterTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FoundationModelDetails:
    boto3_raw_data: "type_defs.FoundationModelDetailsTypeDef" = dataclasses.field()

    modelArn = field("modelArn")
    modelId = field("modelId")
    modelName = field("modelName")
    providerName = field("providerName")
    inputModalities = field("inputModalities")
    outputModalities = field("outputModalities")
    responseStreamingSupported = field("responseStreamingSupported")
    customizationsSupported = field("customizationsSupported")
    inferenceTypesSupported = field("inferenceTypesSupported")

    @cached_property
    def modelLifecycle(self):  # pragma: no cover
        return FoundationModelLifecycle.make_one(self.boto3_raw_data["modelLifecycle"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FoundationModelDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FoundationModelDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FoundationModelSummary:
    boto3_raw_data: "type_defs.FoundationModelSummaryTypeDef" = dataclasses.field()

    modelArn = field("modelArn")
    modelId = field("modelId")
    modelName = field("modelName")
    providerName = field("providerName")
    inputModalities = field("inputModalities")
    outputModalities = field("outputModalities")
    responseStreamingSupported = field("responseStreamingSupported")
    customizationsSupported = field("customizationsSupported")
    inferenceTypesSupported = field("inferenceTypesSupported")

    @cached_property
    def modelLifecycle(self):  # pragma: no cover
        return FoundationModelLifecycle.make_one(self.boto3_raw_data["modelLifecycle"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FoundationModelSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FoundationModelSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GuardrailSummary:
    boto3_raw_data: "type_defs.GuardrailSummaryTypeDef" = dataclasses.field()

    id = field("id")
    arn = field("arn")
    status = field("status")
    name = field("name")
    version = field("version")
    createdAt = field("createdAt")
    updatedAt = field("updatedAt")
    description = field("description")

    @cached_property
    def crossRegionDetails(self):  # pragma: no cover
        return GuardrailCrossRegionDetails.make_one(
            self.boto3_raw_data["crossRegionDetails"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GuardrailSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GuardrailSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetInferenceProfileResponse:
    boto3_raw_data: "type_defs.GetInferenceProfileResponseTypeDef" = dataclasses.field()

    inferenceProfileName = field("inferenceProfileName")
    description = field("description")
    createdAt = field("createdAt")
    updatedAt = field("updatedAt")
    inferenceProfileArn = field("inferenceProfileArn")

    @cached_property
    def models(self):  # pragma: no cover
        return InferenceProfileModel.make_many(self.boto3_raw_data["models"])

    inferenceProfileId = field("inferenceProfileId")
    status = field("status")
    type = field("type")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetInferenceProfileResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetInferenceProfileResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InferenceProfileSummary:
    boto3_raw_data: "type_defs.InferenceProfileSummaryTypeDef" = dataclasses.field()

    inferenceProfileName = field("inferenceProfileName")
    inferenceProfileArn = field("inferenceProfileArn")

    @cached_property
    def models(self):  # pragma: no cover
        return InferenceProfileModel.make_many(self.boto3_raw_data["models"])

    inferenceProfileId = field("inferenceProfileId")
    status = field("status")
    type = field("type")
    description = field("description")
    createdAt = field("createdAt")
    updatedAt = field("updatedAt")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InferenceProfileSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InferenceProfileSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SageMakerEndpointOutput:
    boto3_raw_data: "type_defs.SageMakerEndpointOutputTypeDef" = dataclasses.field()

    initialInstanceCount = field("initialInstanceCount")
    instanceType = field("instanceType")
    executionRole = field("executionRole")
    kmsEncryptionKey = field("kmsEncryptionKey")

    @cached_property
    def vpc(self):  # pragma: no cover
        return VpcConfigOutput.make_one(self.boto3_raw_data["vpc"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SageMakerEndpointOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SageMakerEndpointOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GuardrailContentPolicyConfig:
    boto3_raw_data: "type_defs.GuardrailContentPolicyConfigTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def filtersConfig(self):  # pragma: no cover
        return GuardrailContentFilterConfig.make_many(
            self.boto3_raw_data["filtersConfig"]
        )

    @cached_property
    def tierConfig(self):  # pragma: no cover
        return GuardrailContentFiltersTierConfig.make_one(
            self.boto3_raw_data["tierConfig"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GuardrailContentPolicyConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GuardrailContentPolicyConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GuardrailContentPolicy:
    boto3_raw_data: "type_defs.GuardrailContentPolicyTypeDef" = dataclasses.field()

    @cached_property
    def filters(self):  # pragma: no cover
        return GuardrailContentFilter.make_many(self.boto3_raw_data["filters"])

    @cached_property
    def tier(self):  # pragma: no cover
        return GuardrailContentFiltersTier.make_one(self.boto3_raw_data["tier"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GuardrailContentPolicyTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GuardrailContentPolicyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GuardrailContextualGroundingPolicyConfig:
    boto3_raw_data: "type_defs.GuardrailContextualGroundingPolicyConfigTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def filtersConfig(self):  # pragma: no cover
        return GuardrailContextualGroundingFilterConfig.make_many(
            self.boto3_raw_data["filtersConfig"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GuardrailContextualGroundingPolicyConfigTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GuardrailContextualGroundingPolicyConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GuardrailContextualGroundingPolicy:
    boto3_raw_data: "type_defs.GuardrailContextualGroundingPolicyTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def filters(self):  # pragma: no cover
        return GuardrailContextualGroundingFilter.make_many(
            self.boto3_raw_data["filters"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GuardrailContextualGroundingPolicyTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GuardrailContextualGroundingPolicyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GuardrailSensitiveInformationPolicyConfig:
    boto3_raw_data: "type_defs.GuardrailSensitiveInformationPolicyConfigTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def piiEntitiesConfig(self):  # pragma: no cover
        return GuardrailPiiEntityConfig.make_many(
            self.boto3_raw_data["piiEntitiesConfig"]
        )

    @cached_property
    def regexesConfig(self):  # pragma: no cover
        return GuardrailRegexConfig.make_many(self.boto3_raw_data["regexesConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GuardrailSensitiveInformationPolicyConfigTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GuardrailSensitiveInformationPolicyConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GuardrailSensitiveInformationPolicy:
    boto3_raw_data: "type_defs.GuardrailSensitiveInformationPolicyTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def piiEntities(self):  # pragma: no cover
        return GuardrailPiiEntity.make_many(self.boto3_raw_data["piiEntities"])

    @cached_property
    def regexes(self):  # pragma: no cover
        return GuardrailRegex.make_many(self.boto3_raw_data["regexes"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GuardrailSensitiveInformationPolicyTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GuardrailSensitiveInformationPolicyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GuardrailTopicPolicyConfig:
    boto3_raw_data: "type_defs.GuardrailTopicPolicyConfigTypeDef" = dataclasses.field()

    @cached_property
    def topicsConfig(self):  # pragma: no cover
        return GuardrailTopicConfig.make_many(self.boto3_raw_data["topicsConfig"])

    @cached_property
    def tierConfig(self):  # pragma: no cover
        return GuardrailTopicsTierConfig.make_one(self.boto3_raw_data["tierConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GuardrailTopicPolicyConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GuardrailTopicPolicyConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GuardrailTopicPolicy:
    boto3_raw_data: "type_defs.GuardrailTopicPolicyTypeDef" = dataclasses.field()

    @cached_property
    def topics(self):  # pragma: no cover
        return GuardrailTopic.make_many(self.boto3_raw_data["topics"])

    @cached_property
    def tier(self):  # pragma: no cover
        return GuardrailTopicsTier.make_one(self.boto3_raw_data["tier"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GuardrailTopicPolicyTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GuardrailTopicPolicyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GuardrailWordPolicyConfig:
    boto3_raw_data: "type_defs.GuardrailWordPolicyConfigTypeDef" = dataclasses.field()

    @cached_property
    def wordsConfig(self):  # pragma: no cover
        return GuardrailWordConfig.make_many(self.boto3_raw_data["wordsConfig"])

    @cached_property
    def managedWordListsConfig(self):  # pragma: no cover
        return GuardrailManagedWordsConfig.make_many(
            self.boto3_raw_data["managedWordListsConfig"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GuardrailWordPolicyConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GuardrailWordPolicyConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GuardrailWordPolicy:
    boto3_raw_data: "type_defs.GuardrailWordPolicyTypeDef" = dataclasses.field()

    @cached_property
    def words(self):  # pragma: no cover
        return GuardrailWord.make_many(self.boto3_raw_data["words"])

    @cached_property
    def managedWordLists(self):  # pragma: no cover
        return GuardrailManagedWords.make_many(self.boto3_raw_data["managedWordLists"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GuardrailWordPolicyTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GuardrailWordPolicyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImplicitFilterConfigurationOutput:
    boto3_raw_data: "type_defs.ImplicitFilterConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def metadataAttributes(self):  # pragma: no cover
        return MetadataAttributeSchema.make_many(
            self.boto3_raw_data["metadataAttributes"]
        )

    modelArn = field("modelArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ImplicitFilterConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImplicitFilterConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImplicitFilterConfiguration:
    boto3_raw_data: "type_defs.ImplicitFilterConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def metadataAttributes(self):  # pragma: no cover
        return MetadataAttributeSchema.make_many(
            self.boto3_raw_data["metadataAttributes"]
        )

    modelArn = field("modelArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImplicitFilterConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImplicitFilterConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListImportedModelsResponse:
    boto3_raw_data: "type_defs.ListImportedModelsResponseTypeDef" = dataclasses.field()

    @cached_property
    def modelSummaries(self):  # pragma: no cover
        return ImportedModelSummary.make_many(self.boto3_raw_data["modelSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListImportedModelsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListImportedModelsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KbInferenceConfigOutput:
    boto3_raw_data: "type_defs.KbInferenceConfigOutputTypeDef" = dataclasses.field()

    @cached_property
    def textInferenceConfig(self):  # pragma: no cover
        return TextInferenceConfigOutput.make_one(
            self.boto3_raw_data["textInferenceConfig"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.KbInferenceConfigOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KbInferenceConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KbInferenceConfig:
    boto3_raw_data: "type_defs.KbInferenceConfigTypeDef" = dataclasses.field()

    @cached_property
    def textInferenceConfig(self):  # pragma: no cover
        return TextInferenceConfig.make_one(self.boto3_raw_data["textInferenceConfig"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.KbInferenceConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KbInferenceConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAutomatedReasoningPoliciesRequestPaginate:
    boto3_raw_data: "type_defs.ListAutomatedReasoningPoliciesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    policyArn = field("policyArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAutomatedReasoningPoliciesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAutomatedReasoningPoliciesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAutomatedReasoningPolicyBuildWorkflowsRequestPaginate:
    boto3_raw_data: (
        "type_defs.ListAutomatedReasoningPolicyBuildWorkflowsRequestPaginateTypeDef"
    ) = dataclasses.field()

    policyArn = field("policyArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAutomatedReasoningPolicyBuildWorkflowsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.ListAutomatedReasoningPolicyBuildWorkflowsRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAutomatedReasoningPolicyTestCasesRequestPaginate:
    boto3_raw_data: (
        "type_defs.ListAutomatedReasoningPolicyTestCasesRequestPaginateTypeDef"
    ) = dataclasses.field()

    policyArn = field("policyArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAutomatedReasoningPolicyTestCasesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.ListAutomatedReasoningPolicyTestCasesRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAutomatedReasoningPolicyTestResultsRequestPaginate:
    boto3_raw_data: (
        "type_defs.ListAutomatedReasoningPolicyTestResultsRequestPaginateTypeDef"
    ) = dataclasses.field()

    policyArn = field("policyArn")
    buildWorkflowId = field("buildWorkflowId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAutomatedReasoningPolicyTestResultsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.ListAutomatedReasoningPolicyTestResultsRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCustomModelDeploymentsRequestPaginate:
    boto3_raw_data: "type_defs.ListCustomModelDeploymentsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    createdBefore = field("createdBefore")
    createdAfter = field("createdAfter")
    nameContains = field("nameContains")
    sortBy = field("sortBy")
    sortOrder = field("sortOrder")
    statusEquals = field("statusEquals")
    modelArnEquals = field("modelArnEquals")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCustomModelDeploymentsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCustomModelDeploymentsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCustomModelsRequestPaginate:
    boto3_raw_data: "type_defs.ListCustomModelsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    creationTimeBefore = field("creationTimeBefore")
    creationTimeAfter = field("creationTimeAfter")
    nameContains = field("nameContains")
    baseModelArnEquals = field("baseModelArnEquals")
    foundationModelArnEquals = field("foundationModelArnEquals")
    sortBy = field("sortBy")
    sortOrder = field("sortOrder")
    isOwned = field("isOwned")
    modelStatus = field("modelStatus")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListCustomModelsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCustomModelsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEvaluationJobsRequestPaginate:
    boto3_raw_data: "type_defs.ListEvaluationJobsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    creationTimeAfter = field("creationTimeAfter")
    creationTimeBefore = field("creationTimeBefore")
    statusEquals = field("statusEquals")
    applicationTypeEquals = field("applicationTypeEquals")
    nameContains = field("nameContains")
    sortBy = field("sortBy")
    sortOrder = field("sortOrder")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListEvaluationJobsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEvaluationJobsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGuardrailsRequestPaginate:
    boto3_raw_data: "type_defs.ListGuardrailsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    guardrailIdentifier = field("guardrailIdentifier")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListGuardrailsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGuardrailsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListImportedModelsRequestPaginate:
    boto3_raw_data: "type_defs.ListImportedModelsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    creationTimeBefore = field("creationTimeBefore")
    creationTimeAfter = field("creationTimeAfter")
    nameContains = field("nameContains")
    sortBy = field("sortBy")
    sortOrder = field("sortOrder")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListImportedModelsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListImportedModelsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInferenceProfilesRequestPaginate:
    boto3_raw_data: "type_defs.ListInferenceProfilesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    typeEquals = field("typeEquals")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListInferenceProfilesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInferenceProfilesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMarketplaceModelEndpointsRequestPaginate:
    boto3_raw_data: "type_defs.ListMarketplaceModelEndpointsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    modelSourceEquals = field("modelSourceEquals")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListMarketplaceModelEndpointsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMarketplaceModelEndpointsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListModelCopyJobsRequestPaginate:
    boto3_raw_data: "type_defs.ListModelCopyJobsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    creationTimeAfter = field("creationTimeAfter")
    creationTimeBefore = field("creationTimeBefore")
    statusEquals = field("statusEquals")
    sourceAccountEquals = field("sourceAccountEquals")
    sourceModelArnEquals = field("sourceModelArnEquals")
    targetModelNameContains = field("targetModelNameContains")
    sortBy = field("sortBy")
    sortOrder = field("sortOrder")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListModelCopyJobsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListModelCopyJobsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListModelCustomizationJobsRequestPaginate:
    boto3_raw_data: "type_defs.ListModelCustomizationJobsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    creationTimeAfter = field("creationTimeAfter")
    creationTimeBefore = field("creationTimeBefore")
    statusEquals = field("statusEquals")
    nameContains = field("nameContains")
    sortBy = field("sortBy")
    sortOrder = field("sortOrder")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListModelCustomizationJobsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListModelCustomizationJobsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListModelImportJobsRequestPaginate:
    boto3_raw_data: "type_defs.ListModelImportJobsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    creationTimeAfter = field("creationTimeAfter")
    creationTimeBefore = field("creationTimeBefore")
    statusEquals = field("statusEquals")
    nameContains = field("nameContains")
    sortBy = field("sortBy")
    sortOrder = field("sortOrder")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListModelImportJobsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListModelImportJobsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListModelInvocationJobsRequestPaginate:
    boto3_raw_data: "type_defs.ListModelInvocationJobsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    submitTimeAfter = field("submitTimeAfter")
    submitTimeBefore = field("submitTimeBefore")
    statusEquals = field("statusEquals")
    nameContains = field("nameContains")
    sortBy = field("sortBy")
    sortOrder = field("sortOrder")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListModelInvocationJobsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListModelInvocationJobsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPromptRoutersRequestPaginate:
    boto3_raw_data: "type_defs.ListPromptRoutersRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    type = field("type")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListPromptRoutersRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPromptRoutersRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListProvisionedModelThroughputsRequestPaginate:
    boto3_raw_data: (
        "type_defs.ListProvisionedModelThroughputsRequestPaginateTypeDef"
    ) = dataclasses.field()

    creationTimeAfter = field("creationTimeAfter")
    creationTimeBefore = field("creationTimeBefore")
    statusEquals = field("statusEquals")
    modelArnEquals = field("modelArnEquals")
    nameContains = field("nameContains")
    sortBy = field("sortBy")
    sortOrder = field("sortOrder")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListProvisionedModelThroughputsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.ListProvisionedModelThroughputsRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMarketplaceModelEndpointsResponse:
    boto3_raw_data: "type_defs.ListMarketplaceModelEndpointsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def marketplaceModelEndpoints(self):  # pragma: no cover
        return MarketplaceModelEndpointSummary.make_many(
            self.boto3_raw_data["marketplaceModelEndpoints"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListMarketplaceModelEndpointsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMarketplaceModelEndpointsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListModelImportJobsResponse:
    boto3_raw_data: "type_defs.ListModelImportJobsResponseTypeDef" = dataclasses.field()

    @cached_property
    def modelImportJobSummaries(self):  # pragma: no cover
        return ModelImportJobSummary.make_many(
            self.boto3_raw_data["modelImportJobSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListModelImportJobsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListModelImportJobsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListProvisionedModelThroughputsResponse:
    boto3_raw_data: "type_defs.ListProvisionedModelThroughputsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def provisionedModelSummaries(self):  # pragma: no cover
        return ProvisionedModelSummary.make_many(
            self.boto3_raw_data["provisionedModelSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListProvisionedModelThroughputsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListProvisionedModelThroughputsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModelDataSource:
    boto3_raw_data: "type_defs.ModelDataSourceTypeDef" = dataclasses.field()

    @cached_property
    def s3DataSource(self):  # pragma: no cover
        return S3DataSource.make_one(self.boto3_raw_data["s3DataSource"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ModelDataSourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ModelDataSourceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModelInvocationJobInputDataConfig:
    boto3_raw_data: "type_defs.ModelInvocationJobInputDataConfigTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def s3InputDataConfig(self):  # pragma: no cover
        return ModelInvocationJobS3InputDataConfig.make_one(
            self.boto3_raw_data["s3InputDataConfig"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ModelInvocationJobInputDataConfigTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModelInvocationJobInputDataConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModelInvocationJobOutputDataConfig:
    boto3_raw_data: "type_defs.ModelInvocationJobOutputDataConfigTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def s3OutputDataConfig(self):  # pragma: no cover
        return ModelInvocationJobS3OutputDataConfig.make_one(
            self.boto3_raw_data["s3OutputDataConfig"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ModelInvocationJobOutputDataConfigTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModelInvocationJobOutputDataConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OrchestrationConfiguration:
    boto3_raw_data: "type_defs.OrchestrationConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def queryTransformationConfiguration(self):  # pragma: no cover
        return QueryTransformationConfiguration.make_one(
            self.boto3_raw_data["queryTransformationConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OrchestrationConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OrchestrationConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RatingScaleItem:
    boto3_raw_data: "type_defs.RatingScaleItemTypeDef" = dataclasses.field()

    definition = field("definition")

    @cached_property
    def value(self):  # pragma: no cover
        return RatingScaleItemValue.make_one(self.boto3_raw_data["value"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RatingScaleItemTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RatingScaleItemTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RequestMetadataFiltersOutput:
    boto3_raw_data: "type_defs.RequestMetadataFiltersOutputTypeDef" = (
        dataclasses.field()
    )

    equals = field("equals")
    notEquals = field("notEquals")

    @cached_property
    def andAll(self):  # pragma: no cover
        return RequestMetadataBaseFiltersOutput.make_many(self.boto3_raw_data["andAll"])

    @cached_property
    def orAll(self):  # pragma: no cover
        return RequestMetadataBaseFiltersOutput.make_many(self.boto3_raw_data["orAll"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RequestMetadataFiltersOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RequestMetadataFiltersOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RequestMetadataFilters:
    boto3_raw_data: "type_defs.RequestMetadataFiltersTypeDef" = dataclasses.field()

    equals = field("equals")
    notEquals = field("notEquals")

    @cached_property
    def andAll(self):  # pragma: no cover
        return RequestMetadataBaseFilters.make_many(self.boto3_raw_data["andAll"])

    @cached_property
    def orAll(self):  # pragma: no cover
        return RequestMetadataBaseFilters.make_many(self.boto3_raw_data["orAll"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RequestMetadataFiltersTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RequestMetadataFiltersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SageMakerEndpoint:
    boto3_raw_data: "type_defs.SageMakerEndpointTypeDef" = dataclasses.field()

    initialInstanceCount = field("initialInstanceCount")
    instanceType = field("instanceType")
    executionRole = field("executionRole")
    kmsEncryptionKey = field("kmsEncryptionKey")

    @cached_property
    def vpc(self):  # pragma: no cover
        return VpcConfig.make_one(self.boto3_raw_data["vpc"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SageMakerEndpointTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SageMakerEndpointTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StatusDetails:
    boto3_raw_data: "type_defs.StatusDetailsTypeDef" = dataclasses.field()

    @cached_property
    def validationDetails(self):  # pragma: no cover
        return ValidationDetails.make_one(self.boto3_raw_data["validationDetails"])

    @cached_property
    def dataProcessingDetails(self):  # pragma: no cover
        return DataProcessingDetails.make_one(
            self.boto3_raw_data["dataProcessingDetails"]
        )

    @cached_property
    def trainingDetails(self):  # pragma: no cover
        return TrainingDetails.make_one(self.boto3_raw_data["trainingDetails"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StatusDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StatusDetailsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ValidationDataConfigOutput:
    boto3_raw_data: "type_defs.ValidationDataConfigOutputTypeDef" = dataclasses.field()

    @cached_property
    def validators(self):  # pragma: no cover
        return Validator.make_many(self.boto3_raw_data["validators"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ValidationDataConfigOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ValidationDataConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ValidationDataConfig:
    boto3_raw_data: "type_defs.ValidationDataConfigTypeDef" = dataclasses.field()

    @cached_property
    def validators(self):  # pragma: no cover
        return Validator.make_many(self.boto3_raw_data["validators"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ValidationDataConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ValidationDataConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutomatedReasoningCheckImpossibleFinding:
    boto3_raw_data: "type_defs.AutomatedReasoningCheckImpossibleFindingTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def translation(self):  # pragma: no cover
        return AutomatedReasoningCheckTranslation.make_one(
            self.boto3_raw_data["translation"]
        )

    @cached_property
    def contradictingRules(self):  # pragma: no cover
        return AutomatedReasoningCheckRule.make_many(
            self.boto3_raw_data["contradictingRules"]
        )

    @cached_property
    def logicWarning(self):  # pragma: no cover
        return AutomatedReasoningCheckLogicWarning.make_one(
            self.boto3_raw_data["logicWarning"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AutomatedReasoningCheckImpossibleFindingTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutomatedReasoningCheckImpossibleFindingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutomatedReasoningCheckInvalidFinding:
    boto3_raw_data: "type_defs.AutomatedReasoningCheckInvalidFindingTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def translation(self):  # pragma: no cover
        return AutomatedReasoningCheckTranslation.make_one(
            self.boto3_raw_data["translation"]
        )

    @cached_property
    def contradictingRules(self):  # pragma: no cover
        return AutomatedReasoningCheckRule.make_many(
            self.boto3_raw_data["contradictingRules"]
        )

    @cached_property
    def logicWarning(self):  # pragma: no cover
        return AutomatedReasoningCheckLogicWarning.make_one(
            self.boto3_raw_data["logicWarning"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AutomatedReasoningCheckInvalidFindingTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutomatedReasoningCheckInvalidFindingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutomatedReasoningCheckSatisfiableFinding:
    boto3_raw_data: "type_defs.AutomatedReasoningCheckSatisfiableFindingTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def translation(self):  # pragma: no cover
        return AutomatedReasoningCheckTranslation.make_one(
            self.boto3_raw_data["translation"]
        )

    @cached_property
    def claimsTrueScenario(self):  # pragma: no cover
        return AutomatedReasoningCheckScenario.make_one(
            self.boto3_raw_data["claimsTrueScenario"]
        )

    @cached_property
    def claimsFalseScenario(self):  # pragma: no cover
        return AutomatedReasoningCheckScenario.make_one(
            self.boto3_raw_data["claimsFalseScenario"]
        )

    @cached_property
    def logicWarning(self):  # pragma: no cover
        return AutomatedReasoningCheckLogicWarning.make_one(
            self.boto3_raw_data["logicWarning"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AutomatedReasoningCheckSatisfiableFindingTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutomatedReasoningCheckSatisfiableFindingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutomatedReasoningCheckTranslationOption:
    boto3_raw_data: "type_defs.AutomatedReasoningCheckTranslationOptionTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def translations(self):  # pragma: no cover
        return AutomatedReasoningCheckTranslation.make_many(
            self.boto3_raw_data["translations"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AutomatedReasoningCheckTranslationOptionTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutomatedReasoningCheckTranslationOptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutomatedReasoningCheckValidFinding:
    boto3_raw_data: "type_defs.AutomatedReasoningCheckValidFindingTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def translation(self):  # pragma: no cover
        return AutomatedReasoningCheckTranslation.make_one(
            self.boto3_raw_data["translation"]
        )

    @cached_property
    def claimsTrueScenario(self):  # pragma: no cover
        return AutomatedReasoningCheckScenario.make_one(
            self.boto3_raw_data["claimsTrueScenario"]
        )

    @cached_property
    def supportingRules(self):  # pragma: no cover
        return AutomatedReasoningCheckRule.make_many(
            self.boto3_raw_data["supportingRules"]
        )

    @cached_property
    def logicWarning(self):  # pragma: no cover
        return AutomatedReasoningCheckLogicWarning.make_one(
            self.boto3_raw_data["logicWarning"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AutomatedReasoningCheckValidFindingTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutomatedReasoningCheckValidFindingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutomatedReasoningPolicyAddTypeMutation:
    boto3_raw_data: "type_defs.AutomatedReasoningPolicyAddTypeMutationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def type(self):  # pragma: no cover
        return AutomatedReasoningPolicyDefinitionTypeOutput.make_one(
            self.boto3_raw_data["type"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AutomatedReasoningPolicyAddTypeMutationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutomatedReasoningPolicyAddTypeMutationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutomatedReasoningPolicyDefinitionElement:
    boto3_raw_data: "type_defs.AutomatedReasoningPolicyDefinitionElementTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def policyDefinitionVariable(self):  # pragma: no cover
        return AutomatedReasoningPolicyDefinitionVariable.make_one(
            self.boto3_raw_data["policyDefinitionVariable"]
        )

    @cached_property
    def policyDefinitionType(self):  # pragma: no cover
        return AutomatedReasoningPolicyDefinitionTypeOutput.make_one(
            self.boto3_raw_data["policyDefinitionType"]
        )

    @cached_property
    def policyDefinitionRule(self):  # pragma: no cover
        return AutomatedReasoningPolicyDefinitionRule.make_one(
            self.boto3_raw_data["policyDefinitionRule"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AutomatedReasoningPolicyDefinitionElementTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutomatedReasoningPolicyDefinitionElementTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutomatedReasoningPolicyDefinitionOutput:
    boto3_raw_data: "type_defs.AutomatedReasoningPolicyDefinitionOutputTypeDef" = (
        dataclasses.field()
    )

    version = field("version")

    @cached_property
    def types(self):  # pragma: no cover
        return AutomatedReasoningPolicyDefinitionTypeOutput.make_many(
            self.boto3_raw_data["types"]
        )

    @cached_property
    def rules(self):  # pragma: no cover
        return AutomatedReasoningPolicyDefinitionRule.make_many(
            self.boto3_raw_data["rules"]
        )

    @cached_property
    def variables(self):  # pragma: no cover
        return AutomatedReasoningPolicyDefinitionVariable.make_many(
            self.boto3_raw_data["variables"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AutomatedReasoningPolicyDefinitionOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutomatedReasoningPolicyDefinitionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutomatedReasoningPolicyUpdateTypeMutation:
    boto3_raw_data: "type_defs.AutomatedReasoningPolicyUpdateTypeMutationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def type(self):  # pragma: no cover
        return AutomatedReasoningPolicyDefinitionTypeOutput.make_one(
            self.boto3_raw_data["type"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AutomatedReasoningPolicyUpdateTypeMutationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutomatedReasoningPolicyUpdateTypeMutationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExternalSource:
    boto3_raw_data: "type_defs.ExternalSourceTypeDef" = dataclasses.field()

    sourceType = field("sourceType")

    @cached_property
    def s3Location(self):  # pragma: no cover
        return S3ObjectDoc.make_one(self.boto3_raw_data["s3Location"])

    @cached_property
    def byteContent(self):  # pragma: no cover
        return ByteContentDoc.make_one(self.boto3_raw_data["byteContent"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExternalSourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ExternalSourceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutomatedReasoningPolicyUpdateTypeAnnotationOutput:
    boto3_raw_data: (
        "type_defs.AutomatedReasoningPolicyUpdateTypeAnnotationOutputTypeDef"
    ) = dataclasses.field()

    name = field("name")

    @cached_property
    def values(self):  # pragma: no cover
        return AutomatedReasoningPolicyTypeValueAnnotation.make_many(
            self.boto3_raw_data["values"]
        )

    newName = field("newName")
    description = field("description")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AutomatedReasoningPolicyUpdateTypeAnnotationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.AutomatedReasoningPolicyUpdateTypeAnnotationOutputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutomatedReasoningPolicyUpdateTypeAnnotation:
    boto3_raw_data: "type_defs.AutomatedReasoningPolicyUpdateTypeAnnotationTypeDef" = (
        dataclasses.field()
    )

    name = field("name")

    @cached_property
    def values(self):  # pragma: no cover
        return AutomatedReasoningPolicyTypeValueAnnotation.make_many(
            self.boto3_raw_data["values"]
        )

    newName = field("newName")
    description = field("description")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AutomatedReasoningPolicyUpdateTypeAnnotationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutomatedReasoningPolicyUpdateTypeAnnotationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LoggingConfig:
    boto3_raw_data: "type_defs.LoggingConfigTypeDef" = dataclasses.field()

    @cached_property
    def cloudWatchConfig(self):  # pragma: no cover
        return CloudWatchConfig.make_one(self.boto3_raw_data["cloudWatchConfig"])

    @cached_property
    def s3Config(self):  # pragma: no cover
        return S3Config.make_one(self.boto3_raw_data["s3Config"])

    textDataDeliveryEnabled = field("textDataDeliveryEnabled")
    imageDataDeliveryEnabled = field("imageDataDeliveryEnabled")
    embeddingDataDeliveryEnabled = field("embeddingDataDeliveryEnabled")
    videoDataDeliveryEnabled = field("videoDataDeliveryEnabled")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LoggingConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LoggingConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListModelCopyJobsResponse:
    boto3_raw_data: "type_defs.ListModelCopyJobsResponseTypeDef" = dataclasses.field()

    @cached_property
    def modelCopyJobSummaries(self):  # pragma: no cover
        return ModelCopyJobSummary.make_many(
            self.boto3_raw_data["modelCopyJobSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListModelCopyJobsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListModelCopyJobsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPromptRoutersResponse:
    boto3_raw_data: "type_defs.ListPromptRoutersResponseTypeDef" = dataclasses.field()

    @cached_property
    def promptRouterSummaries(self):  # pragma: no cover
        return PromptRouterSummary.make_many(
            self.boto3_raw_data["promptRouterSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPromptRoutersResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPromptRoutersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TermDetails:
    boto3_raw_data: "type_defs.TermDetailsTypeDef" = dataclasses.field()

    @cached_property
    def usageBasedPricingTerm(self):  # pragma: no cover
        return PricingTerm.make_one(self.boto3_raw_data["usageBasedPricingTerm"])

    @cached_property
    def legalTerm(self):  # pragma: no cover
        return LegalTerm.make_one(self.boto3_raw_data["legalTerm"])

    @cached_property
    def supportTerm(self):  # pragma: no cover
        return SupportTerm.make_one(self.boto3_raw_data["supportTerm"])

    @cached_property
    def validityTerm(self):  # pragma: no cover
        return ValidityTerm.make_one(self.boto3_raw_data["validityTerm"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TermDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TermDetailsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomizationConfig:
    boto3_raw_data: "type_defs.CustomizationConfigTypeDef" = dataclasses.field()

    @cached_property
    def distillationConfig(self):  # pragma: no cover
        return DistillationConfig.make_one(self.boto3_raw_data["distillationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CustomizationConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomizationConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EvaluationModelConfig:
    boto3_raw_data: "type_defs.EvaluationModelConfigTypeDef" = dataclasses.field()

    @cached_property
    def bedrockModel(self):  # pragma: no cover
        return EvaluationBedrockModel.make_one(self.boto3_raw_data["bedrockModel"])

    @cached_property
    def precomputedInferenceSource(self):  # pragma: no cover
        return EvaluationPrecomputedInferenceSource.make_one(
            self.boto3_raw_data["precomputedInferenceSource"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EvaluationModelConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EvaluationModelConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EvaluationDatasetMetricConfigOutput:
    boto3_raw_data: "type_defs.EvaluationDatasetMetricConfigOutputTypeDef" = (
        dataclasses.field()
    )

    taskType = field("taskType")

    @cached_property
    def dataset(self):  # pragma: no cover
        return EvaluationDataset.make_one(self.boto3_raw_data["dataset"])

    metricNames = field("metricNames")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.EvaluationDatasetMetricConfigOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EvaluationDatasetMetricConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EvaluationDatasetMetricConfig:
    boto3_raw_data: "type_defs.EvaluationDatasetMetricConfigTypeDef" = (
        dataclasses.field()
    )

    taskType = field("taskType")

    @cached_property
    def dataset(self):  # pragma: no cover
        return EvaluationDataset.make_one(self.boto3_raw_data["dataset"])

    metricNames = field("metricNames")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.EvaluationDatasetMetricConfigTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EvaluationDatasetMetricConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EvaluationSummary:
    boto3_raw_data: "type_defs.EvaluationSummaryTypeDef" = dataclasses.field()

    jobArn = field("jobArn")
    jobName = field("jobName")
    status = field("status")
    creationTime = field("creationTime")
    jobType = field("jobType")
    evaluationTaskTypes = field("evaluationTaskTypes")
    modelIdentifiers = field("modelIdentifiers")
    ragIdentifiers = field("ragIdentifiers")
    evaluatorModelIdentifiers = field("evaluatorModelIdentifiers")
    customMetricsEvaluatorModelIdentifiers = field(
        "customMetricsEvaluatorModelIdentifiers"
    )

    @cached_property
    def inferenceConfigSummary(self):  # pragma: no cover
        return EvaluationInferenceConfigSummary.make_one(
            self.boto3_raw_data["inferenceConfigSummary"]
        )

    applicationType = field("applicationType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EvaluationSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EvaluationSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetadataConfigurationForRerankingOutput:
    boto3_raw_data: "type_defs.MetadataConfigurationForRerankingOutputTypeDef" = (
        dataclasses.field()
    )

    selectionMode = field("selectionMode")

    @cached_property
    def selectiveModeConfiguration(self):  # pragma: no cover
        return RerankingMetadataSelectiveModeConfigurationOutput.make_one(
            self.boto3_raw_data["selectiveModeConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.MetadataConfigurationForRerankingOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MetadataConfigurationForRerankingOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetadataConfigurationForReranking:
    boto3_raw_data: "type_defs.MetadataConfigurationForRerankingTypeDef" = (
        dataclasses.field()
    )

    selectionMode = field("selectionMode")

    @cached_property
    def selectiveModeConfiguration(self):  # pragma: no cover
        return RerankingMetadataSelectiveModeConfiguration.make_one(
            self.boto3_raw_data["selectiveModeConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.MetadataConfigurationForRerankingTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MetadataConfigurationForRerankingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFoundationModelResponse:
    boto3_raw_data: "type_defs.GetFoundationModelResponseTypeDef" = dataclasses.field()

    @cached_property
    def modelDetails(self):  # pragma: no cover
        return FoundationModelDetails.make_one(self.boto3_raw_data["modelDetails"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetFoundationModelResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFoundationModelResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFoundationModelsResponse:
    boto3_raw_data: "type_defs.ListFoundationModelsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def modelSummaries(self):  # pragma: no cover
        return FoundationModelSummary.make_many(self.boto3_raw_data["modelSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListFoundationModelsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFoundationModelsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGuardrailsResponse:
    boto3_raw_data: "type_defs.ListGuardrailsResponseTypeDef" = dataclasses.field()

    @cached_property
    def guardrails(self):  # pragma: no cover
        return GuardrailSummary.make_many(self.boto3_raw_data["guardrails"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListGuardrailsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGuardrailsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInferenceProfilesResponse:
    boto3_raw_data: "type_defs.ListInferenceProfilesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def inferenceProfileSummaries(self):  # pragma: no cover
        return InferenceProfileSummary.make_many(
            self.boto3_raw_data["inferenceProfileSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListInferenceProfilesResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInferenceProfilesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EndpointConfigOutput:
    boto3_raw_data: "type_defs.EndpointConfigOutputTypeDef" = dataclasses.field()

    @cached_property
    def sageMaker(self):  # pragma: no cover
        return SageMakerEndpointOutput.make_one(self.boto3_raw_data["sageMaker"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EndpointConfigOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EndpointConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateGuardrailRequest:
    boto3_raw_data: "type_defs.CreateGuardrailRequestTypeDef" = dataclasses.field()

    name = field("name")
    blockedInputMessaging = field("blockedInputMessaging")
    blockedOutputsMessaging = field("blockedOutputsMessaging")
    description = field("description")

    @cached_property
    def topicPolicyConfig(self):  # pragma: no cover
        return GuardrailTopicPolicyConfig.make_one(
            self.boto3_raw_data["topicPolicyConfig"]
        )

    @cached_property
    def contentPolicyConfig(self):  # pragma: no cover
        return GuardrailContentPolicyConfig.make_one(
            self.boto3_raw_data["contentPolicyConfig"]
        )

    @cached_property
    def wordPolicyConfig(self):  # pragma: no cover
        return GuardrailWordPolicyConfig.make_one(
            self.boto3_raw_data["wordPolicyConfig"]
        )

    @cached_property
    def sensitiveInformationPolicyConfig(self):  # pragma: no cover
        return GuardrailSensitiveInformationPolicyConfig.make_one(
            self.boto3_raw_data["sensitiveInformationPolicyConfig"]
        )

    @cached_property
    def contextualGroundingPolicyConfig(self):  # pragma: no cover
        return GuardrailContextualGroundingPolicyConfig.make_one(
            self.boto3_raw_data["contextualGroundingPolicyConfig"]
        )

    @cached_property
    def automatedReasoningPolicyConfig(self):  # pragma: no cover
        return GuardrailAutomatedReasoningPolicyConfig.make_one(
            self.boto3_raw_data["automatedReasoningPolicyConfig"]
        )

    @cached_property
    def crossRegionConfig(self):  # pragma: no cover
        return GuardrailCrossRegionConfig.make_one(
            self.boto3_raw_data["crossRegionConfig"]
        )

    kmsKeyId = field("kmsKeyId")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    clientRequestToken = field("clientRequestToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateGuardrailRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateGuardrailRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateGuardrailRequest:
    boto3_raw_data: "type_defs.UpdateGuardrailRequestTypeDef" = dataclasses.field()

    guardrailIdentifier = field("guardrailIdentifier")
    name = field("name")
    blockedInputMessaging = field("blockedInputMessaging")
    blockedOutputsMessaging = field("blockedOutputsMessaging")
    description = field("description")

    @cached_property
    def topicPolicyConfig(self):  # pragma: no cover
        return GuardrailTopicPolicyConfig.make_one(
            self.boto3_raw_data["topicPolicyConfig"]
        )

    @cached_property
    def contentPolicyConfig(self):  # pragma: no cover
        return GuardrailContentPolicyConfig.make_one(
            self.boto3_raw_data["contentPolicyConfig"]
        )

    @cached_property
    def wordPolicyConfig(self):  # pragma: no cover
        return GuardrailWordPolicyConfig.make_one(
            self.boto3_raw_data["wordPolicyConfig"]
        )

    @cached_property
    def sensitiveInformationPolicyConfig(self):  # pragma: no cover
        return GuardrailSensitiveInformationPolicyConfig.make_one(
            self.boto3_raw_data["sensitiveInformationPolicyConfig"]
        )

    @cached_property
    def contextualGroundingPolicyConfig(self):  # pragma: no cover
        return GuardrailContextualGroundingPolicyConfig.make_one(
            self.boto3_raw_data["contextualGroundingPolicyConfig"]
        )

    @cached_property
    def automatedReasoningPolicyConfig(self):  # pragma: no cover
        return GuardrailAutomatedReasoningPolicyConfig.make_one(
            self.boto3_raw_data["automatedReasoningPolicyConfig"]
        )

    @cached_property
    def crossRegionConfig(self):  # pragma: no cover
        return GuardrailCrossRegionConfig.make_one(
            self.boto3_raw_data["crossRegionConfig"]
        )

    kmsKeyId = field("kmsKeyId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateGuardrailRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateGuardrailRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetGuardrailResponse:
    boto3_raw_data: "type_defs.GetGuardrailResponseTypeDef" = dataclasses.field()

    name = field("name")
    description = field("description")
    guardrailId = field("guardrailId")
    guardrailArn = field("guardrailArn")
    version = field("version")
    status = field("status")

    @cached_property
    def topicPolicy(self):  # pragma: no cover
        return GuardrailTopicPolicy.make_one(self.boto3_raw_data["topicPolicy"])

    @cached_property
    def contentPolicy(self):  # pragma: no cover
        return GuardrailContentPolicy.make_one(self.boto3_raw_data["contentPolicy"])

    @cached_property
    def wordPolicy(self):  # pragma: no cover
        return GuardrailWordPolicy.make_one(self.boto3_raw_data["wordPolicy"])

    @cached_property
    def sensitiveInformationPolicy(self):  # pragma: no cover
        return GuardrailSensitiveInformationPolicy.make_one(
            self.boto3_raw_data["sensitiveInformationPolicy"]
        )

    @cached_property
    def contextualGroundingPolicy(self):  # pragma: no cover
        return GuardrailContextualGroundingPolicy.make_one(
            self.boto3_raw_data["contextualGroundingPolicy"]
        )

    @cached_property
    def automatedReasoningPolicy(self):  # pragma: no cover
        return GuardrailAutomatedReasoningPolicy.make_one(
            self.boto3_raw_data["automatedReasoningPolicy"]
        )

    @cached_property
    def crossRegionDetails(self):  # pragma: no cover
        return GuardrailCrossRegionDetails.make_one(
            self.boto3_raw_data["crossRegionDetails"]
        )

    createdAt = field("createdAt")
    updatedAt = field("updatedAt")
    statusReasons = field("statusReasons")
    failureRecommendations = field("failureRecommendations")
    blockedInputMessaging = field("blockedInputMessaging")
    blockedOutputsMessaging = field("blockedOutputsMessaging")
    kmsKeyArn = field("kmsKeyArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetGuardrailResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetGuardrailResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExternalSourcesGenerationConfigurationOutput:
    boto3_raw_data: "type_defs.ExternalSourcesGenerationConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def promptTemplate(self):  # pragma: no cover
        return PromptTemplate.make_one(self.boto3_raw_data["promptTemplate"])

    @cached_property
    def guardrailConfiguration(self):  # pragma: no cover
        return GuardrailConfiguration.make_one(
            self.boto3_raw_data["guardrailConfiguration"]
        )

    @cached_property
    def kbInferenceConfig(self):  # pragma: no cover
        return KbInferenceConfigOutput.make_one(
            self.boto3_raw_data["kbInferenceConfig"]
        )

    additionalModelRequestFields = field("additionalModelRequestFields")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ExternalSourcesGenerationConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExternalSourcesGenerationConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GenerationConfigurationOutput:
    boto3_raw_data: "type_defs.GenerationConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def promptTemplate(self):  # pragma: no cover
        return PromptTemplate.make_one(self.boto3_raw_data["promptTemplate"])

    @cached_property
    def guardrailConfiguration(self):  # pragma: no cover
        return GuardrailConfiguration.make_one(
            self.boto3_raw_data["guardrailConfiguration"]
        )

    @cached_property
    def kbInferenceConfig(self):  # pragma: no cover
        return KbInferenceConfigOutput.make_one(
            self.boto3_raw_data["kbInferenceConfig"]
        )

    additionalModelRequestFields = field("additionalModelRequestFields")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GenerationConfigurationOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GenerationConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExternalSourcesGenerationConfiguration:
    boto3_raw_data: "type_defs.ExternalSourcesGenerationConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def promptTemplate(self):  # pragma: no cover
        return PromptTemplate.make_one(self.boto3_raw_data["promptTemplate"])

    @cached_property
    def guardrailConfiguration(self):  # pragma: no cover
        return GuardrailConfiguration.make_one(
            self.boto3_raw_data["guardrailConfiguration"]
        )

    @cached_property
    def kbInferenceConfig(self):  # pragma: no cover
        return KbInferenceConfig.make_one(self.boto3_raw_data["kbInferenceConfig"])

    additionalModelRequestFields = field("additionalModelRequestFields")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ExternalSourcesGenerationConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExternalSourcesGenerationConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GenerationConfiguration:
    boto3_raw_data: "type_defs.GenerationConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def promptTemplate(self):  # pragma: no cover
        return PromptTemplate.make_one(self.boto3_raw_data["promptTemplate"])

    @cached_property
    def guardrailConfiguration(self):  # pragma: no cover
        return GuardrailConfiguration.make_one(
            self.boto3_raw_data["guardrailConfiguration"]
        )

    @cached_property
    def kbInferenceConfig(self):  # pragma: no cover
        return KbInferenceConfig.make_one(self.boto3_raw_data["kbInferenceConfig"])

    additionalModelRequestFields = field("additionalModelRequestFields")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GenerationConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GenerationConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCustomModelRequest:
    boto3_raw_data: "type_defs.CreateCustomModelRequestTypeDef" = dataclasses.field()

    modelName = field("modelName")

    @cached_property
    def modelSourceConfig(self):  # pragma: no cover
        return ModelDataSource.make_one(self.boto3_raw_data["modelSourceConfig"])

    modelKmsKeyArn = field("modelKmsKeyArn")
    roleArn = field("roleArn")

    @cached_property
    def modelTags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["modelTags"])

    clientRequestToken = field("clientRequestToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateCustomModelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCustomModelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetImportedModelResponse:
    boto3_raw_data: "type_defs.GetImportedModelResponseTypeDef" = dataclasses.field()

    modelArn = field("modelArn")
    modelName = field("modelName")
    jobName = field("jobName")
    jobArn = field("jobArn")

    @cached_property
    def modelDataSource(self):  # pragma: no cover
        return ModelDataSource.make_one(self.boto3_raw_data["modelDataSource"])

    creationTime = field("creationTime")
    modelArchitecture = field("modelArchitecture")
    modelKmsKeyArn = field("modelKmsKeyArn")
    instructSupported = field("instructSupported")

    @cached_property
    def customModelUnits(self):  # pragma: no cover
        return CustomModelUnits.make_one(self.boto3_raw_data["customModelUnits"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetImportedModelResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetImportedModelResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetModelImportJobResponse:
    boto3_raw_data: "type_defs.GetModelImportJobResponseTypeDef" = dataclasses.field()

    jobArn = field("jobArn")
    jobName = field("jobName")
    importedModelName = field("importedModelName")
    importedModelArn = field("importedModelArn")
    roleArn = field("roleArn")

    @cached_property
    def modelDataSource(self):  # pragma: no cover
        return ModelDataSource.make_one(self.boto3_raw_data["modelDataSource"])

    status = field("status")
    failureMessage = field("failureMessage")
    creationTime = field("creationTime")
    lastModifiedTime = field("lastModifiedTime")
    endTime = field("endTime")

    @cached_property
    def vpcConfig(self):  # pragma: no cover
        return VpcConfigOutput.make_one(self.boto3_raw_data["vpcConfig"])

    importedModelKmsKeyArn = field("importedModelKmsKeyArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetModelImportJobResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetModelImportJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetModelInvocationJobResponse:
    boto3_raw_data: "type_defs.GetModelInvocationJobResponseTypeDef" = (
        dataclasses.field()
    )

    jobArn = field("jobArn")
    jobName = field("jobName")
    modelId = field("modelId")
    clientRequestToken = field("clientRequestToken")
    roleArn = field("roleArn")
    status = field("status")
    message = field("message")
    submitTime = field("submitTime")
    lastModifiedTime = field("lastModifiedTime")
    endTime = field("endTime")

    @cached_property
    def inputDataConfig(self):  # pragma: no cover
        return ModelInvocationJobInputDataConfig.make_one(
            self.boto3_raw_data["inputDataConfig"]
        )

    @cached_property
    def outputDataConfig(self):  # pragma: no cover
        return ModelInvocationJobOutputDataConfig.make_one(
            self.boto3_raw_data["outputDataConfig"]
        )

    @cached_property
    def vpcConfig(self):  # pragma: no cover
        return VpcConfigOutput.make_one(self.boto3_raw_data["vpcConfig"])

    timeoutDurationInHours = field("timeoutDurationInHours")
    jobExpirationTime = field("jobExpirationTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetModelInvocationJobResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetModelInvocationJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModelInvocationJobSummary:
    boto3_raw_data: "type_defs.ModelInvocationJobSummaryTypeDef" = dataclasses.field()

    jobArn = field("jobArn")
    jobName = field("jobName")
    modelId = field("modelId")
    roleArn = field("roleArn")
    submitTime = field("submitTime")

    @cached_property
    def inputDataConfig(self):  # pragma: no cover
        return ModelInvocationJobInputDataConfig.make_one(
            self.boto3_raw_data["inputDataConfig"]
        )

    @cached_property
    def outputDataConfig(self):  # pragma: no cover
        return ModelInvocationJobOutputDataConfig.make_one(
            self.boto3_raw_data["outputDataConfig"]
        )

    clientRequestToken = field("clientRequestToken")
    status = field("status")
    message = field("message")
    lastModifiedTime = field("lastModifiedTime")
    endTime = field("endTime")

    @cached_property
    def vpcConfig(self):  # pragma: no cover
        return VpcConfigOutput.make_one(self.boto3_raw_data["vpcConfig"])

    timeoutDurationInHours = field("timeoutDurationInHours")
    jobExpirationTime = field("jobExpirationTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ModelInvocationJobSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModelInvocationJobSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomMetricDefinitionOutput:
    boto3_raw_data: "type_defs.CustomMetricDefinitionOutputTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    instructions = field("instructions")

    @cached_property
    def ratingScale(self):  # pragma: no cover
        return RatingScaleItem.make_many(self.boto3_raw_data["ratingScale"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CustomMetricDefinitionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomMetricDefinitionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomMetricDefinition:
    boto3_raw_data: "type_defs.CustomMetricDefinitionTypeDef" = dataclasses.field()

    name = field("name")
    instructions = field("instructions")

    @cached_property
    def ratingScale(self):  # pragma: no cover
        return RatingScaleItem.make_many(self.boto3_raw_data["ratingScale"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CustomMetricDefinitionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomMetricDefinitionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InvocationLogsConfigOutput:
    boto3_raw_data: "type_defs.InvocationLogsConfigOutputTypeDef" = dataclasses.field()

    @cached_property
    def invocationLogSource(self):  # pragma: no cover
        return InvocationLogSource.make_one(self.boto3_raw_data["invocationLogSource"])

    usePromptResponse = field("usePromptResponse")

    @cached_property
    def requestMetadataFilters(self):  # pragma: no cover
        return RequestMetadataFiltersOutput.make_one(
            self.boto3_raw_data["requestMetadataFilters"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InvocationLogsConfigOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InvocationLogsConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InvocationLogsConfig:
    boto3_raw_data: "type_defs.InvocationLogsConfigTypeDef" = dataclasses.field()

    @cached_property
    def invocationLogSource(self):  # pragma: no cover
        return InvocationLogSource.make_one(self.boto3_raw_data["invocationLogSource"])

    usePromptResponse = field("usePromptResponse")

    @cached_property
    def requestMetadataFilters(self):  # pragma: no cover
        return RequestMetadataFilters.make_one(
            self.boto3_raw_data["requestMetadataFilters"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InvocationLogsConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InvocationLogsConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EndpointConfig:
    boto3_raw_data: "type_defs.EndpointConfigTypeDef" = dataclasses.field()

    @cached_property
    def sageMaker(self):  # pragma: no cover
        return SageMakerEndpoint.make_one(self.boto3_raw_data["sageMaker"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EndpointConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EndpointConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateModelImportJobRequest:
    boto3_raw_data: "type_defs.CreateModelImportJobRequestTypeDef" = dataclasses.field()

    jobName = field("jobName")
    importedModelName = field("importedModelName")
    roleArn = field("roleArn")

    @cached_property
    def modelDataSource(self):  # pragma: no cover
        return ModelDataSource.make_one(self.boto3_raw_data["modelDataSource"])

    @cached_property
    def jobTags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["jobTags"])

    @cached_property
    def importedModelTags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["importedModelTags"])

    clientRequestToken = field("clientRequestToken")
    vpcConfig = field("vpcConfig")
    importedModelKmsKeyId = field("importedModelKmsKeyId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateModelImportJobRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateModelImportJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateModelInvocationJobRequest:
    boto3_raw_data: "type_defs.CreateModelInvocationJobRequestTypeDef" = (
        dataclasses.field()
    )

    jobName = field("jobName")
    roleArn = field("roleArn")
    modelId = field("modelId")

    @cached_property
    def inputDataConfig(self):  # pragma: no cover
        return ModelInvocationJobInputDataConfig.make_one(
            self.boto3_raw_data["inputDataConfig"]
        )

    @cached_property
    def outputDataConfig(self):  # pragma: no cover
        return ModelInvocationJobOutputDataConfig.make_one(
            self.boto3_raw_data["outputDataConfig"]
        )

    clientRequestToken = field("clientRequestToken")
    vpcConfig = field("vpcConfig")
    timeoutDurationInHours = field("timeoutDurationInHours")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateModelInvocationJobRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateModelInvocationJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModelCustomizationJobSummary:
    boto3_raw_data: "type_defs.ModelCustomizationJobSummaryTypeDef" = (
        dataclasses.field()
    )

    jobArn = field("jobArn")
    baseModelArn = field("baseModelArn")
    jobName = field("jobName")
    status = field("status")
    creationTime = field("creationTime")

    @cached_property
    def statusDetails(self):  # pragma: no cover
        return StatusDetails.make_one(self.boto3_raw_data["statusDetails"])

    lastModifiedTime = field("lastModifiedTime")
    endTime = field("endTime")
    customModelArn = field("customModelArn")
    customModelName = field("customModelName")
    customizationType = field("customizationType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ModelCustomizationJobSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModelCustomizationJobSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutomatedReasoningCheckTranslationAmbiguousFinding:
    boto3_raw_data: (
        "type_defs.AutomatedReasoningCheckTranslationAmbiguousFindingTypeDef"
    ) = dataclasses.field()

    @cached_property
    def options(self):  # pragma: no cover
        return AutomatedReasoningCheckTranslationOption.make_many(
            self.boto3_raw_data["options"]
        )

    @cached_property
    def differenceScenarios(self):  # pragma: no cover
        return AutomatedReasoningCheckScenario.make_many(
            self.boto3_raw_data["differenceScenarios"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AutomatedReasoningCheckTranslationAmbiguousFindingTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.AutomatedReasoningCheckTranslationAmbiguousFindingTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExportAutomatedReasoningPolicyVersionResponse:
    boto3_raw_data: "type_defs.ExportAutomatedReasoningPolicyVersionResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def policyDefinition(self):  # pragma: no cover
        return AutomatedReasoningPolicyDefinitionOutput.make_one(
            self.boto3_raw_data["policyDefinition"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ExportAutomatedReasoningPolicyVersionResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExportAutomatedReasoningPolicyVersionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutomatedReasoningPolicyMutation:
    boto3_raw_data: "type_defs.AutomatedReasoningPolicyMutationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def addType(self):  # pragma: no cover
        return AutomatedReasoningPolicyAddTypeMutation.make_one(
            self.boto3_raw_data["addType"]
        )

    @cached_property
    def updateType(self):  # pragma: no cover
        return AutomatedReasoningPolicyUpdateTypeMutation.make_one(
            self.boto3_raw_data["updateType"]
        )

    @cached_property
    def deleteType(self):  # pragma: no cover
        return AutomatedReasoningPolicyDeleteTypeMutation.make_one(
            self.boto3_raw_data["deleteType"]
        )

    @cached_property
    def addVariable(self):  # pragma: no cover
        return AutomatedReasoningPolicyAddVariableMutation.make_one(
            self.boto3_raw_data["addVariable"]
        )

    @cached_property
    def updateVariable(self):  # pragma: no cover
        return AutomatedReasoningPolicyUpdateVariableMutation.make_one(
            self.boto3_raw_data["updateVariable"]
        )

    @cached_property
    def deleteVariable(self):  # pragma: no cover
        return AutomatedReasoningPolicyDeleteVariableMutation.make_one(
            self.boto3_raw_data["deleteVariable"]
        )

    @cached_property
    def addRule(self):  # pragma: no cover
        return AutomatedReasoningPolicyAddRuleMutation.make_one(
            self.boto3_raw_data["addRule"]
        )

    @cached_property
    def updateRule(self):  # pragma: no cover
        return AutomatedReasoningPolicyUpdateRuleMutation.make_one(
            self.boto3_raw_data["updateRule"]
        )

    @cached_property
    def deleteRule(self):  # pragma: no cover
        return AutomatedReasoningPolicyDeleteRuleMutation.make_one(
            self.boto3_raw_data["deleteRule"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AutomatedReasoningPolicyMutationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutomatedReasoningPolicyMutationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutomatedReasoningPolicyDefinition:
    boto3_raw_data: "type_defs.AutomatedReasoningPolicyDefinitionTypeDef" = (
        dataclasses.field()
    )

    version = field("version")
    types = field("types")

    @cached_property
    def rules(self):  # pragma: no cover
        return AutomatedReasoningPolicyDefinitionRule.make_many(
            self.boto3_raw_data["rules"]
        )

    @cached_property
    def variables(self):  # pragma: no cover
        return AutomatedReasoningPolicyDefinitionVariable.make_many(
            self.boto3_raw_data["variables"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AutomatedReasoningPolicyDefinitionTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutomatedReasoningPolicyDefinitionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutomatedReasoningPolicyAnnotationOutput:
    boto3_raw_data: "type_defs.AutomatedReasoningPolicyAnnotationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def addType(self):  # pragma: no cover
        return AutomatedReasoningPolicyAddTypeAnnotationOutput.make_one(
            self.boto3_raw_data["addType"]
        )

    @cached_property
    def updateType(self):  # pragma: no cover
        return AutomatedReasoningPolicyUpdateTypeAnnotationOutput.make_one(
            self.boto3_raw_data["updateType"]
        )

    @cached_property
    def deleteType(self):  # pragma: no cover
        return AutomatedReasoningPolicyDeleteTypeAnnotation.make_one(
            self.boto3_raw_data["deleteType"]
        )

    @cached_property
    def addVariable(self):  # pragma: no cover
        return AutomatedReasoningPolicyAddVariableAnnotation.make_one(
            self.boto3_raw_data["addVariable"]
        )

    @cached_property
    def updateVariable(self):  # pragma: no cover
        return AutomatedReasoningPolicyUpdateVariableAnnotation.make_one(
            self.boto3_raw_data["updateVariable"]
        )

    @cached_property
    def deleteVariable(self):  # pragma: no cover
        return AutomatedReasoningPolicyDeleteVariableAnnotation.make_one(
            self.boto3_raw_data["deleteVariable"]
        )

    @cached_property
    def addRule(self):  # pragma: no cover
        return AutomatedReasoningPolicyAddRuleAnnotation.make_one(
            self.boto3_raw_data["addRule"]
        )

    @cached_property
    def updateRule(self):  # pragma: no cover
        return AutomatedReasoningPolicyUpdateRuleAnnotation.make_one(
            self.boto3_raw_data["updateRule"]
        )

    @cached_property
    def deleteRule(self):  # pragma: no cover
        return AutomatedReasoningPolicyDeleteRuleAnnotation.make_one(
            self.boto3_raw_data["deleteRule"]
        )

    @cached_property
    def addRuleFromNaturalLanguage(self):  # pragma: no cover
        return AutomatedReasoningPolicyAddRuleFromNaturalLanguageAnnotation.make_one(
            self.boto3_raw_data["addRuleFromNaturalLanguage"]
        )

    @cached_property
    def updateFromRulesFeedback(self):  # pragma: no cover
        return AutomatedReasoningPolicyUpdateFromRuleFeedbackAnnotationOutput.make_one(
            self.boto3_raw_data["updateFromRulesFeedback"]
        )

    @cached_property
    def updateFromScenarioFeedback(self):  # pragma: no cover
        return (
            AutomatedReasoningPolicyUpdateFromScenarioFeedbackAnnotationOutput.make_one(
                self.boto3_raw_data["updateFromScenarioFeedback"]
            )
        )

    @cached_property
    def ingestContent(self):  # pragma: no cover
        return AutomatedReasoningPolicyIngestContentAnnotation.make_one(
            self.boto3_raw_data["ingestContent"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AutomatedReasoningPolicyAnnotationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutomatedReasoningPolicyAnnotationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetModelInvocationLoggingConfigurationResponse:
    boto3_raw_data: (
        "type_defs.GetModelInvocationLoggingConfigurationResponseTypeDef"
    ) = dataclasses.field()

    @cached_property
    def loggingConfig(self):  # pragma: no cover
        return LoggingConfig.make_one(self.boto3_raw_data["loggingConfig"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetModelInvocationLoggingConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.GetModelInvocationLoggingConfigurationResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutModelInvocationLoggingConfigurationRequest:
    boto3_raw_data: "type_defs.PutModelInvocationLoggingConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def loggingConfig(self):  # pragma: no cover
        return LoggingConfig.make_one(self.boto3_raw_data["loggingConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutModelInvocationLoggingConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutModelInvocationLoggingConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Offer:
    boto3_raw_data: "type_defs.OfferTypeDef" = dataclasses.field()

    offerToken = field("offerToken")

    @cached_property
    def termDetails(self):  # pragma: no cover
        return TermDetails.make_one(self.boto3_raw_data["termDetails"])

    offerId = field("offerId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OfferTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OfferTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HumanEvaluationConfigOutput:
    boto3_raw_data: "type_defs.HumanEvaluationConfigOutputTypeDef" = dataclasses.field()

    @cached_property
    def datasetMetricConfigs(self):  # pragma: no cover
        return EvaluationDatasetMetricConfigOutput.make_many(
            self.boto3_raw_data["datasetMetricConfigs"]
        )

    @cached_property
    def humanWorkflowConfig(self):  # pragma: no cover
        return HumanWorkflowConfig.make_one(self.boto3_raw_data["humanWorkflowConfig"])

    @cached_property
    def customMetrics(self):  # pragma: no cover
        return HumanEvaluationCustomMetric.make_many(
            self.boto3_raw_data["customMetrics"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.HumanEvaluationConfigOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HumanEvaluationConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HumanEvaluationConfig:
    boto3_raw_data: "type_defs.HumanEvaluationConfigTypeDef" = dataclasses.field()

    @cached_property
    def datasetMetricConfigs(self):  # pragma: no cover
        return EvaluationDatasetMetricConfig.make_many(
            self.boto3_raw_data["datasetMetricConfigs"]
        )

    @cached_property
    def humanWorkflowConfig(self):  # pragma: no cover
        return HumanWorkflowConfig.make_one(self.boto3_raw_data["humanWorkflowConfig"])

    @cached_property
    def customMetrics(self):  # pragma: no cover
        return HumanEvaluationCustomMetric.make_many(
            self.boto3_raw_data["customMetrics"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.HumanEvaluationConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HumanEvaluationConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEvaluationJobsResponse:
    boto3_raw_data: "type_defs.ListEvaluationJobsResponseTypeDef" = dataclasses.field()

    @cached_property
    def jobSummaries(self):  # pragma: no cover
        return EvaluationSummary.make_many(self.boto3_raw_data["jobSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListEvaluationJobsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEvaluationJobsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VectorSearchBedrockRerankingConfigurationOutput:
    boto3_raw_data: (
        "type_defs.VectorSearchBedrockRerankingConfigurationOutputTypeDef"
    ) = dataclasses.field()

    @cached_property
    def modelConfiguration(self):  # pragma: no cover
        return VectorSearchBedrockRerankingModelConfigurationOutput.make_one(
            self.boto3_raw_data["modelConfiguration"]
        )

    numberOfRerankedResults = field("numberOfRerankedResults")

    @cached_property
    def metadataConfiguration(self):  # pragma: no cover
        return MetadataConfigurationForRerankingOutput.make_one(
            self.boto3_raw_data["metadataConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.VectorSearchBedrockRerankingConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.VectorSearchBedrockRerankingConfigurationOutputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VectorSearchBedrockRerankingConfiguration:
    boto3_raw_data: "type_defs.VectorSearchBedrockRerankingConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def modelConfiguration(self):  # pragma: no cover
        return VectorSearchBedrockRerankingModelConfiguration.make_one(
            self.boto3_raw_data["modelConfiguration"]
        )

    numberOfRerankedResults = field("numberOfRerankedResults")

    @cached_property
    def metadataConfiguration(self):  # pragma: no cover
        return MetadataConfigurationForReranking.make_one(
            self.boto3_raw_data["metadataConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.VectorSearchBedrockRerankingConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VectorSearchBedrockRerankingConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MarketplaceModelEndpoint:
    boto3_raw_data: "type_defs.MarketplaceModelEndpointTypeDef" = dataclasses.field()

    endpointArn = field("endpointArn")
    modelSourceIdentifier = field("modelSourceIdentifier")
    createdAt = field("createdAt")
    updatedAt = field("updatedAt")

    @cached_property
    def endpointConfig(self):  # pragma: no cover
        return EndpointConfigOutput.make_one(self.boto3_raw_data["endpointConfig"])

    endpointStatus = field("endpointStatus")
    status = field("status")
    statusMessage = field("statusMessage")
    endpointStatusMessage = field("endpointStatusMessage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MarketplaceModelEndpointTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MarketplaceModelEndpointTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExternalSourcesRetrieveAndGenerateConfigurationOutput:
    boto3_raw_data: (
        "type_defs.ExternalSourcesRetrieveAndGenerateConfigurationOutputTypeDef"
    ) = dataclasses.field()

    modelArn = field("modelArn")

    @cached_property
    def sources(self):  # pragma: no cover
        return ExternalSourceOutput.make_many(self.boto3_raw_data["sources"])

    @cached_property
    def generationConfiguration(self):  # pragma: no cover
        return ExternalSourcesGenerationConfigurationOutput.make_one(
            self.boto3_raw_data["generationConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ExternalSourcesRetrieveAndGenerateConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.ExternalSourcesRetrieveAndGenerateConfigurationOutputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExternalSourcesRetrieveAndGenerateConfiguration:
    boto3_raw_data: (
        "type_defs.ExternalSourcesRetrieveAndGenerateConfigurationTypeDef"
    ) = dataclasses.field()

    modelArn = field("modelArn")

    @cached_property
    def sources(self):  # pragma: no cover
        return ExternalSource.make_many(self.boto3_raw_data["sources"])

    @cached_property
    def generationConfiguration(self):  # pragma: no cover
        return ExternalSourcesGenerationConfiguration.make_one(
            self.boto3_raw_data["generationConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ExternalSourcesRetrieveAndGenerateConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.ExternalSourcesRetrieveAndGenerateConfigurationTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListModelInvocationJobsResponse:
    boto3_raw_data: "type_defs.ListModelInvocationJobsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def invocationJobSummaries(self):  # pragma: no cover
        return ModelInvocationJobSummary.make_many(
            self.boto3_raw_data["invocationJobSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListModelInvocationJobsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListModelInvocationJobsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutomatedEvaluationCustomMetricSourceOutput:
    boto3_raw_data: "type_defs.AutomatedEvaluationCustomMetricSourceOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def customMetricDefinition(self):  # pragma: no cover
        return CustomMetricDefinitionOutput.make_one(
            self.boto3_raw_data["customMetricDefinition"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AutomatedEvaluationCustomMetricSourceOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutomatedEvaluationCustomMetricSourceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutomatedEvaluationCustomMetricSource:
    boto3_raw_data: "type_defs.AutomatedEvaluationCustomMetricSourceTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def customMetricDefinition(self):  # pragma: no cover
        return CustomMetricDefinition.make_one(
            self.boto3_raw_data["customMetricDefinition"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AutomatedEvaluationCustomMetricSourceTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutomatedEvaluationCustomMetricSourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TrainingDataConfigOutput:
    boto3_raw_data: "type_defs.TrainingDataConfigOutputTypeDef" = dataclasses.field()

    s3Uri = field("s3Uri")

    @cached_property
    def invocationLogsConfig(self):  # pragma: no cover
        return InvocationLogsConfigOutput.make_one(
            self.boto3_raw_data["invocationLogsConfig"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TrainingDataConfigOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TrainingDataConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TrainingDataConfig:
    boto3_raw_data: "type_defs.TrainingDataConfigTypeDef" = dataclasses.field()

    s3Uri = field("s3Uri")

    @cached_property
    def invocationLogsConfig(self):  # pragma: no cover
        return InvocationLogsConfig.make_one(
            self.boto3_raw_data["invocationLogsConfig"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TrainingDataConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TrainingDataConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListModelCustomizationJobsResponse:
    boto3_raw_data: "type_defs.ListModelCustomizationJobsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def modelCustomizationJobSummaries(self):  # pragma: no cover
        return ModelCustomizationJobSummary.make_many(
            self.boto3_raw_data["modelCustomizationJobSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListModelCustomizationJobsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListModelCustomizationJobsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutomatedReasoningCheckFinding:
    boto3_raw_data: "type_defs.AutomatedReasoningCheckFindingTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def valid(self):  # pragma: no cover
        return AutomatedReasoningCheckValidFinding.make_one(
            self.boto3_raw_data["valid"]
        )

    @cached_property
    def invalid(self):  # pragma: no cover
        return AutomatedReasoningCheckInvalidFinding.make_one(
            self.boto3_raw_data["invalid"]
        )

    @cached_property
    def satisfiable(self):  # pragma: no cover
        return AutomatedReasoningCheckSatisfiableFinding.make_one(
            self.boto3_raw_data["satisfiable"]
        )

    @cached_property
    def impossible(self):  # pragma: no cover
        return AutomatedReasoningCheckImpossibleFinding.make_one(
            self.boto3_raw_data["impossible"]
        )

    @cached_property
    def translationAmbiguous(self):  # pragma: no cover
        return AutomatedReasoningCheckTranslationAmbiguousFinding.make_one(
            self.boto3_raw_data["translationAmbiguous"]
        )

    tooComplex = field("tooComplex")
    noTranslations = field("noTranslations")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AutomatedReasoningCheckFindingTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutomatedReasoningCheckFindingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutomatedReasoningPolicyBuildStepContext:
    boto3_raw_data: "type_defs.AutomatedReasoningPolicyBuildStepContextTypeDef" = (
        dataclasses.field()
    )

    planning = field("planning")

    @cached_property
    def mutation(self):  # pragma: no cover
        return AutomatedReasoningPolicyMutation.make_one(
            self.boto3_raw_data["mutation"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AutomatedReasoningPolicyBuildStepContextTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutomatedReasoningPolicyBuildStepContextTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAutomatedReasoningPolicyAnnotationsResponse:
    boto3_raw_data: (
        "type_defs.GetAutomatedReasoningPolicyAnnotationsResponseTypeDef"
    ) = dataclasses.field()

    policyArn = field("policyArn")
    name = field("name")
    buildWorkflowId = field("buildWorkflowId")

    @cached_property
    def annotations(self):  # pragma: no cover
        return AutomatedReasoningPolicyAnnotationOutput.make_many(
            self.boto3_raw_data["annotations"]
        )

    annotationSetHash = field("annotationSetHash")
    updatedAt = field("updatedAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetAutomatedReasoningPolicyAnnotationsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.GetAutomatedReasoningPolicyAnnotationsResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutomatedReasoningPolicyAnnotation:
    boto3_raw_data: "type_defs.AutomatedReasoningPolicyAnnotationTypeDef" = (
        dataclasses.field()
    )

    addType = field("addType")
    updateType = field("updateType")

    @cached_property
    def deleteType(self):  # pragma: no cover
        return AutomatedReasoningPolicyDeleteTypeAnnotation.make_one(
            self.boto3_raw_data["deleteType"]
        )

    @cached_property
    def addVariable(self):  # pragma: no cover
        return AutomatedReasoningPolicyAddVariableAnnotation.make_one(
            self.boto3_raw_data["addVariable"]
        )

    @cached_property
    def updateVariable(self):  # pragma: no cover
        return AutomatedReasoningPolicyUpdateVariableAnnotation.make_one(
            self.boto3_raw_data["updateVariable"]
        )

    @cached_property
    def deleteVariable(self):  # pragma: no cover
        return AutomatedReasoningPolicyDeleteVariableAnnotation.make_one(
            self.boto3_raw_data["deleteVariable"]
        )

    @cached_property
    def addRule(self):  # pragma: no cover
        return AutomatedReasoningPolicyAddRuleAnnotation.make_one(
            self.boto3_raw_data["addRule"]
        )

    @cached_property
    def updateRule(self):  # pragma: no cover
        return AutomatedReasoningPolicyUpdateRuleAnnotation.make_one(
            self.boto3_raw_data["updateRule"]
        )

    @cached_property
    def deleteRule(self):  # pragma: no cover
        return AutomatedReasoningPolicyDeleteRuleAnnotation.make_one(
            self.boto3_raw_data["deleteRule"]
        )

    @cached_property
    def addRuleFromNaturalLanguage(self):  # pragma: no cover
        return AutomatedReasoningPolicyAddRuleFromNaturalLanguageAnnotation.make_one(
            self.boto3_raw_data["addRuleFromNaturalLanguage"]
        )

    updateFromRulesFeedback = field("updateFromRulesFeedback")
    updateFromScenarioFeedback = field("updateFromScenarioFeedback")

    @cached_property
    def ingestContent(self):  # pragma: no cover
        return AutomatedReasoningPolicyIngestContentAnnotation.make_one(
            self.boto3_raw_data["ingestContent"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AutomatedReasoningPolicyAnnotationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutomatedReasoningPolicyAnnotationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFoundationModelAgreementOffersResponse:
    boto3_raw_data: "type_defs.ListFoundationModelAgreementOffersResponseTypeDef" = (
        dataclasses.field()
    )

    modelId = field("modelId")

    @cached_property
    def offers(self):  # pragma: no cover
        return Offer.make_many(self.boto3_raw_data["offers"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListFoundationModelAgreementOffersResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFoundationModelAgreementOffersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VectorSearchRerankingConfigurationOutput:
    boto3_raw_data: "type_defs.VectorSearchRerankingConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    type = field("type")

    @cached_property
    def bedrockRerankingConfiguration(self):  # pragma: no cover
        return VectorSearchBedrockRerankingConfigurationOutput.make_one(
            self.boto3_raw_data["bedrockRerankingConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.VectorSearchRerankingConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VectorSearchRerankingConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VectorSearchRerankingConfiguration:
    boto3_raw_data: "type_defs.VectorSearchRerankingConfigurationTypeDef" = (
        dataclasses.field()
    )

    type = field("type")

    @cached_property
    def bedrockRerankingConfiguration(self):  # pragma: no cover
        return VectorSearchBedrockRerankingConfiguration.make_one(
            self.boto3_raw_data["bedrockRerankingConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.VectorSearchRerankingConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VectorSearchRerankingConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateMarketplaceModelEndpointResponse:
    boto3_raw_data: "type_defs.CreateMarketplaceModelEndpointResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def marketplaceModelEndpoint(self):  # pragma: no cover
        return MarketplaceModelEndpoint.make_one(
            self.boto3_raw_data["marketplaceModelEndpoint"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateMarketplaceModelEndpointResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateMarketplaceModelEndpointResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMarketplaceModelEndpointResponse:
    boto3_raw_data: "type_defs.GetMarketplaceModelEndpointResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def marketplaceModelEndpoint(self):  # pragma: no cover
        return MarketplaceModelEndpoint.make_one(
            self.boto3_raw_data["marketplaceModelEndpoint"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetMarketplaceModelEndpointResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMarketplaceModelEndpointResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegisterMarketplaceModelEndpointResponse:
    boto3_raw_data: "type_defs.RegisterMarketplaceModelEndpointResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def marketplaceModelEndpoint(self):  # pragma: no cover
        return MarketplaceModelEndpoint.make_one(
            self.boto3_raw_data["marketplaceModelEndpoint"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RegisterMarketplaceModelEndpointResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegisterMarketplaceModelEndpointResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateMarketplaceModelEndpointResponse:
    boto3_raw_data: "type_defs.UpdateMarketplaceModelEndpointResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def marketplaceModelEndpoint(self):  # pragma: no cover
        return MarketplaceModelEndpoint.make_one(
            self.boto3_raw_data["marketplaceModelEndpoint"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateMarketplaceModelEndpointResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateMarketplaceModelEndpointResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutomatedEvaluationCustomMetricConfigOutput:
    boto3_raw_data: "type_defs.AutomatedEvaluationCustomMetricConfigOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def customMetrics(self):  # pragma: no cover
        return AutomatedEvaluationCustomMetricSourceOutput.make_many(
            self.boto3_raw_data["customMetrics"]
        )

    @cached_property
    def evaluatorModelConfig(self):  # pragma: no cover
        return CustomMetricEvaluatorModelConfigOutput.make_one(
            self.boto3_raw_data["evaluatorModelConfig"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AutomatedEvaluationCustomMetricConfigOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutomatedEvaluationCustomMetricConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutomatedEvaluationCustomMetricConfig:
    boto3_raw_data: "type_defs.AutomatedEvaluationCustomMetricConfigTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def customMetrics(self):  # pragma: no cover
        return AutomatedEvaluationCustomMetricSource.make_many(
            self.boto3_raw_data["customMetrics"]
        )

    @cached_property
    def evaluatorModelConfig(self):  # pragma: no cover
        return CustomMetricEvaluatorModelConfig.make_one(
            self.boto3_raw_data["evaluatorModelConfig"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AutomatedEvaluationCustomMetricConfigTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutomatedEvaluationCustomMetricConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCustomModelResponse:
    boto3_raw_data: "type_defs.GetCustomModelResponseTypeDef" = dataclasses.field()

    modelArn = field("modelArn")
    modelName = field("modelName")
    jobName = field("jobName")
    jobArn = field("jobArn")
    baseModelArn = field("baseModelArn")
    customizationType = field("customizationType")
    modelKmsKeyArn = field("modelKmsKeyArn")
    hyperParameters = field("hyperParameters")

    @cached_property
    def trainingDataConfig(self):  # pragma: no cover
        return TrainingDataConfigOutput.make_one(
            self.boto3_raw_data["trainingDataConfig"]
        )

    @cached_property
    def validationDataConfig(self):  # pragma: no cover
        return ValidationDataConfigOutput.make_one(
            self.boto3_raw_data["validationDataConfig"]
        )

    @cached_property
    def outputDataConfig(self):  # pragma: no cover
        return OutputDataConfig.make_one(self.boto3_raw_data["outputDataConfig"])

    @cached_property
    def trainingMetrics(self):  # pragma: no cover
        return TrainingMetrics.make_one(self.boto3_raw_data["trainingMetrics"])

    @cached_property
    def validationMetrics(self):  # pragma: no cover
        return ValidatorMetric.make_many(self.boto3_raw_data["validationMetrics"])

    creationTime = field("creationTime")

    @cached_property
    def customizationConfig(self):  # pragma: no cover
        return CustomizationConfig.make_one(self.boto3_raw_data["customizationConfig"])

    modelStatus = field("modelStatus")
    failureMessage = field("failureMessage")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetCustomModelResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCustomModelResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetModelCustomizationJobResponse:
    boto3_raw_data: "type_defs.GetModelCustomizationJobResponseTypeDef" = (
        dataclasses.field()
    )

    jobArn = field("jobArn")
    jobName = field("jobName")
    outputModelName = field("outputModelName")
    outputModelArn = field("outputModelArn")
    clientRequestToken = field("clientRequestToken")
    roleArn = field("roleArn")
    status = field("status")

    @cached_property
    def statusDetails(self):  # pragma: no cover
        return StatusDetails.make_one(self.boto3_raw_data["statusDetails"])

    failureMessage = field("failureMessage")
    creationTime = field("creationTime")
    lastModifiedTime = field("lastModifiedTime")
    endTime = field("endTime")
    baseModelArn = field("baseModelArn")
    hyperParameters = field("hyperParameters")

    @cached_property
    def trainingDataConfig(self):  # pragma: no cover
        return TrainingDataConfigOutput.make_one(
            self.boto3_raw_data["trainingDataConfig"]
        )

    @cached_property
    def validationDataConfig(self):  # pragma: no cover
        return ValidationDataConfigOutput.make_one(
            self.boto3_raw_data["validationDataConfig"]
        )

    @cached_property
    def outputDataConfig(self):  # pragma: no cover
        return OutputDataConfig.make_one(self.boto3_raw_data["outputDataConfig"])

    customizationType = field("customizationType")
    outputModelKmsKeyArn = field("outputModelKmsKeyArn")

    @cached_property
    def trainingMetrics(self):  # pragma: no cover
        return TrainingMetrics.make_one(self.boto3_raw_data["trainingMetrics"])

    @cached_property
    def validationMetrics(self):  # pragma: no cover
        return ValidatorMetric.make_many(self.boto3_raw_data["validationMetrics"])

    @cached_property
    def vpcConfig(self):  # pragma: no cover
        return VpcConfigOutput.make_one(self.boto3_raw_data["vpcConfig"])

    @cached_property
    def customizationConfig(self):  # pragma: no cover
        return CustomizationConfig.make_one(self.boto3_raw_data["customizationConfig"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetModelCustomizationJobResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetModelCustomizationJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateMarketplaceModelEndpointRequest:
    boto3_raw_data: "type_defs.CreateMarketplaceModelEndpointRequestTypeDef" = (
        dataclasses.field()
    )

    modelSourceIdentifier = field("modelSourceIdentifier")
    endpointConfig = field("endpointConfig")
    endpointName = field("endpointName")
    acceptEula = field("acceptEula")
    clientRequestToken = field("clientRequestToken")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateMarketplaceModelEndpointRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateMarketplaceModelEndpointRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateMarketplaceModelEndpointRequest:
    boto3_raw_data: "type_defs.UpdateMarketplaceModelEndpointRequestTypeDef" = (
        dataclasses.field()
    )

    endpointArn = field("endpointArn")
    endpointConfig = field("endpointConfig")
    clientRequestToken = field("clientRequestToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateMarketplaceModelEndpointRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateMarketplaceModelEndpointRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutomatedReasoningPolicyTestResult:
    boto3_raw_data: "type_defs.AutomatedReasoningPolicyTestResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def testCase(self):  # pragma: no cover
        return AutomatedReasoningPolicyTestCase.make_one(
            self.boto3_raw_data["testCase"]
        )

    policyArn = field("policyArn")
    testRunStatus = field("testRunStatus")
    updatedAt = field("updatedAt")

    @cached_property
    def testFindings(self):  # pragma: no cover
        return AutomatedReasoningCheckFinding.make_many(
            self.boto3_raw_data["testFindings"]
        )

    testRunResult = field("testRunResult")
    aggregatedTestFindingsResult = field("aggregatedTestFindingsResult")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AutomatedReasoningPolicyTestResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutomatedReasoningPolicyTestResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutomatedReasoningPolicyBuildStep:
    boto3_raw_data: "type_defs.AutomatedReasoningPolicyBuildStepTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def context(self):  # pragma: no cover
        return AutomatedReasoningPolicyBuildStepContext.make_one(
            self.boto3_raw_data["context"]
        )

    @cached_property
    def messages(self):  # pragma: no cover
        return AutomatedReasoningPolicyBuildStepMessage.make_many(
            self.boto3_raw_data["messages"]
        )

    @cached_property
    def priorElement(self):  # pragma: no cover
        return AutomatedReasoningPolicyDefinitionElement.make_one(
            self.boto3_raw_data["priorElement"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AutomatedReasoningPolicyBuildStepTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutomatedReasoningPolicyBuildStepTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAutomatedReasoningPolicyRequest:
    boto3_raw_data: "type_defs.CreateAutomatedReasoningPolicyRequestTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    description = field("description")
    clientRequestToken = field("clientRequestToken")
    policyDefinition = field("policyDefinition")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateAutomatedReasoningPolicyRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAutomatedReasoningPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAutomatedReasoningPolicyRequest:
    boto3_raw_data: "type_defs.UpdateAutomatedReasoningPolicyRequestTypeDef" = (
        dataclasses.field()
    )

    policyArn = field("policyArn")
    policyDefinition = field("policyDefinition")
    name = field("name")
    description = field("description")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateAutomatedReasoningPolicyRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAutomatedReasoningPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KnowledgeBaseVectorSearchConfigurationOutput:
    boto3_raw_data: "type_defs.KnowledgeBaseVectorSearchConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    numberOfResults = field("numberOfResults")
    overrideSearchType = field("overrideSearchType")

    @cached_property
    def filter(self):  # pragma: no cover
        return RetrievalFilterOutput.make_one(self.boto3_raw_data["filter"])

    @cached_property
    def implicitFilterConfiguration(self):  # pragma: no cover
        return ImplicitFilterConfigurationOutput.make_one(
            self.boto3_raw_data["implicitFilterConfiguration"]
        )

    @cached_property
    def rerankingConfiguration(self):  # pragma: no cover
        return VectorSearchRerankingConfigurationOutput.make_one(
            self.boto3_raw_data["rerankingConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.KnowledgeBaseVectorSearchConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KnowledgeBaseVectorSearchConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KnowledgeBaseVectorSearchConfiguration:
    boto3_raw_data: "type_defs.KnowledgeBaseVectorSearchConfigurationTypeDef" = (
        dataclasses.field()
    )

    numberOfResults = field("numberOfResults")
    overrideSearchType = field("overrideSearchType")

    @cached_property
    def filter(self):  # pragma: no cover
        return RetrievalFilter.make_one(self.boto3_raw_data["filter"])

    @cached_property
    def implicitFilterConfiguration(self):  # pragma: no cover
        return ImplicitFilterConfiguration.make_one(
            self.boto3_raw_data["implicitFilterConfiguration"]
        )

    @cached_property
    def rerankingConfiguration(self):  # pragma: no cover
        return VectorSearchRerankingConfiguration.make_one(
            self.boto3_raw_data["rerankingConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.KnowledgeBaseVectorSearchConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KnowledgeBaseVectorSearchConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutomatedEvaluationConfigOutput:
    boto3_raw_data: "type_defs.AutomatedEvaluationConfigOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def datasetMetricConfigs(self):  # pragma: no cover
        return EvaluationDatasetMetricConfigOutput.make_many(
            self.boto3_raw_data["datasetMetricConfigs"]
        )

    @cached_property
    def evaluatorModelConfig(self):  # pragma: no cover
        return EvaluatorModelConfigOutput.make_one(
            self.boto3_raw_data["evaluatorModelConfig"]
        )

    @cached_property
    def customMetricConfig(self):  # pragma: no cover
        return AutomatedEvaluationCustomMetricConfigOutput.make_one(
            self.boto3_raw_data["customMetricConfig"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AutomatedEvaluationConfigOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutomatedEvaluationConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutomatedEvaluationConfig:
    boto3_raw_data: "type_defs.AutomatedEvaluationConfigTypeDef" = dataclasses.field()

    @cached_property
    def datasetMetricConfigs(self):  # pragma: no cover
        return EvaluationDatasetMetricConfig.make_many(
            self.boto3_raw_data["datasetMetricConfigs"]
        )

    @cached_property
    def evaluatorModelConfig(self):  # pragma: no cover
        return EvaluatorModelConfig.make_one(
            self.boto3_raw_data["evaluatorModelConfig"]
        )

    @cached_property
    def customMetricConfig(self):  # pragma: no cover
        return AutomatedEvaluationCustomMetricConfig.make_one(
            self.boto3_raw_data["customMetricConfig"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AutomatedEvaluationConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutomatedEvaluationConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateModelCustomizationJobRequest:
    boto3_raw_data: "type_defs.CreateModelCustomizationJobRequestTypeDef" = (
        dataclasses.field()
    )

    jobName = field("jobName")
    customModelName = field("customModelName")
    roleArn = field("roleArn")
    baseModelIdentifier = field("baseModelIdentifier")
    trainingDataConfig = field("trainingDataConfig")

    @cached_property
    def outputDataConfig(self):  # pragma: no cover
        return OutputDataConfig.make_one(self.boto3_raw_data["outputDataConfig"])

    clientRequestToken = field("clientRequestToken")
    customizationType = field("customizationType")
    customModelKmsKeyId = field("customModelKmsKeyId")

    @cached_property
    def jobTags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["jobTags"])

    @cached_property
    def customModelTags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["customModelTags"])

    validationDataConfig = field("validationDataConfig")
    hyperParameters = field("hyperParameters")
    vpcConfig = field("vpcConfig")

    @cached_property
    def customizationConfig(self):  # pragma: no cover
        return CustomizationConfig.make_one(self.boto3_raw_data["customizationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateModelCustomizationJobRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateModelCustomizationJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAutomatedReasoningPolicyTestResultResponse:
    boto3_raw_data: "type_defs.GetAutomatedReasoningPolicyTestResultResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def testResult(self):  # pragma: no cover
        return AutomatedReasoningPolicyTestResult.make_one(
            self.boto3_raw_data["testResult"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetAutomatedReasoningPolicyTestResultResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAutomatedReasoningPolicyTestResultResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAutomatedReasoningPolicyTestResultsResponse:
    boto3_raw_data: (
        "type_defs.ListAutomatedReasoningPolicyTestResultsResponseTypeDef"
    ) = dataclasses.field()

    @cached_property
    def testResults(self):  # pragma: no cover
        return AutomatedReasoningPolicyTestResult.make_many(
            self.boto3_raw_data["testResults"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAutomatedReasoningPolicyTestResultsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.ListAutomatedReasoningPolicyTestResultsResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutomatedReasoningPolicyBuildLogEntry:
    boto3_raw_data: "type_defs.AutomatedReasoningPolicyBuildLogEntryTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def annotation(self):  # pragma: no cover
        return AutomatedReasoningPolicyAnnotationOutput.make_one(
            self.boto3_raw_data["annotation"]
        )

    status = field("status")

    @cached_property
    def buildSteps(self):  # pragma: no cover
        return AutomatedReasoningPolicyBuildStep.make_many(
            self.boto3_raw_data["buildSteps"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AutomatedReasoningPolicyBuildLogEntryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutomatedReasoningPolicyBuildLogEntryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutomatedReasoningPolicyBuildWorkflowRepairContent:
    boto3_raw_data: (
        "type_defs.AutomatedReasoningPolicyBuildWorkflowRepairContentTypeDef"
    ) = dataclasses.field()

    annotations = field("annotations")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AutomatedReasoningPolicyBuildWorkflowRepairContentTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.AutomatedReasoningPolicyBuildWorkflowRepairContentTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAutomatedReasoningPolicyAnnotationsRequest:
    boto3_raw_data: (
        "type_defs.UpdateAutomatedReasoningPolicyAnnotationsRequestTypeDef"
    ) = dataclasses.field()

    policyArn = field("policyArn")
    buildWorkflowId = field("buildWorkflowId")
    annotations = field("annotations")
    lastUpdatedAnnotationSetHash = field("lastUpdatedAnnotationSetHash")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateAutomatedReasoningPolicyAnnotationsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.UpdateAutomatedReasoningPolicyAnnotationsRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KnowledgeBaseRetrievalConfigurationOutput:
    boto3_raw_data: "type_defs.KnowledgeBaseRetrievalConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def vectorSearchConfiguration(self):  # pragma: no cover
        return KnowledgeBaseVectorSearchConfigurationOutput.make_one(
            self.boto3_raw_data["vectorSearchConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.KnowledgeBaseRetrievalConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KnowledgeBaseRetrievalConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KnowledgeBaseRetrievalConfiguration:
    boto3_raw_data: "type_defs.KnowledgeBaseRetrievalConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def vectorSearchConfiguration(self):  # pragma: no cover
        return KnowledgeBaseVectorSearchConfiguration.make_one(
            self.boto3_raw_data["vectorSearchConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.KnowledgeBaseRetrievalConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KnowledgeBaseRetrievalConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EvaluationConfigOutput:
    boto3_raw_data: "type_defs.EvaluationConfigOutputTypeDef" = dataclasses.field()

    @cached_property
    def automated(self):  # pragma: no cover
        return AutomatedEvaluationConfigOutput.make_one(
            self.boto3_raw_data["automated"]
        )

    @cached_property
    def human(self):  # pragma: no cover
        return HumanEvaluationConfigOutput.make_one(self.boto3_raw_data["human"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EvaluationConfigOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EvaluationConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EvaluationConfig:
    boto3_raw_data: "type_defs.EvaluationConfigTypeDef" = dataclasses.field()

    @cached_property
    def automated(self):  # pragma: no cover
        return AutomatedEvaluationConfig.make_one(self.boto3_raw_data["automated"])

    @cached_property
    def human(self):  # pragma: no cover
        return HumanEvaluationConfig.make_one(self.boto3_raw_data["human"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EvaluationConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EvaluationConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutomatedReasoningPolicyBuildLog:
    boto3_raw_data: "type_defs.AutomatedReasoningPolicyBuildLogTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def entries(self):  # pragma: no cover
        return AutomatedReasoningPolicyBuildLogEntry.make_many(
            self.boto3_raw_data["entries"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AutomatedReasoningPolicyBuildLogTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutomatedReasoningPolicyBuildLogTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutomatedReasoningPolicyWorkflowTypeContent:
    boto3_raw_data: "type_defs.AutomatedReasoningPolicyWorkflowTypeContentTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def documents(self):  # pragma: no cover
        return AutomatedReasoningPolicyBuildWorkflowDocument.make_many(
            self.boto3_raw_data["documents"]
        )

    @cached_property
    def policyRepairAssets(self):  # pragma: no cover
        return AutomatedReasoningPolicyBuildWorkflowRepairContent.make_one(
            self.boto3_raw_data["policyRepairAssets"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AutomatedReasoningPolicyWorkflowTypeContentTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutomatedReasoningPolicyWorkflowTypeContentTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KnowledgeBaseRetrieveAndGenerateConfigurationOutput:
    boto3_raw_data: (
        "type_defs.KnowledgeBaseRetrieveAndGenerateConfigurationOutputTypeDef"
    ) = dataclasses.field()

    knowledgeBaseId = field("knowledgeBaseId")
    modelArn = field("modelArn")

    @cached_property
    def retrievalConfiguration(self):  # pragma: no cover
        return KnowledgeBaseRetrievalConfigurationOutput.make_one(
            self.boto3_raw_data["retrievalConfiguration"]
        )

    @cached_property
    def generationConfiguration(self):  # pragma: no cover
        return GenerationConfigurationOutput.make_one(
            self.boto3_raw_data["generationConfiguration"]
        )

    @cached_property
    def orchestrationConfiguration(self):  # pragma: no cover
        return OrchestrationConfiguration.make_one(
            self.boto3_raw_data["orchestrationConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.KnowledgeBaseRetrieveAndGenerateConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.KnowledgeBaseRetrieveAndGenerateConfigurationOutputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RetrieveConfigOutput:
    boto3_raw_data: "type_defs.RetrieveConfigOutputTypeDef" = dataclasses.field()

    knowledgeBaseId = field("knowledgeBaseId")

    @cached_property
    def knowledgeBaseRetrievalConfiguration(self):  # pragma: no cover
        return KnowledgeBaseRetrievalConfigurationOutput.make_one(
            self.boto3_raw_data["knowledgeBaseRetrievalConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RetrieveConfigOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RetrieveConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KnowledgeBaseRetrieveAndGenerateConfiguration:
    boto3_raw_data: "type_defs.KnowledgeBaseRetrieveAndGenerateConfigurationTypeDef" = (
        dataclasses.field()
    )

    knowledgeBaseId = field("knowledgeBaseId")
    modelArn = field("modelArn")

    @cached_property
    def retrievalConfiguration(self):  # pragma: no cover
        return KnowledgeBaseRetrievalConfiguration.make_one(
            self.boto3_raw_data["retrievalConfiguration"]
        )

    @cached_property
    def generationConfiguration(self):  # pragma: no cover
        return GenerationConfiguration.make_one(
            self.boto3_raw_data["generationConfiguration"]
        )

    @cached_property
    def orchestrationConfiguration(self):  # pragma: no cover
        return OrchestrationConfiguration.make_one(
            self.boto3_raw_data["orchestrationConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.KnowledgeBaseRetrieveAndGenerateConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KnowledgeBaseRetrieveAndGenerateConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RetrieveConfig:
    boto3_raw_data: "type_defs.RetrieveConfigTypeDef" = dataclasses.field()

    knowledgeBaseId = field("knowledgeBaseId")

    @cached_property
    def knowledgeBaseRetrievalConfiguration(self):  # pragma: no cover
        return KnowledgeBaseRetrievalConfiguration.make_one(
            self.boto3_raw_data["knowledgeBaseRetrievalConfiguration"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RetrieveConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RetrieveConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutomatedReasoningPolicyBuildResultAssets:
    boto3_raw_data: "type_defs.AutomatedReasoningPolicyBuildResultAssetsTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def policyDefinition(self):  # pragma: no cover
        return AutomatedReasoningPolicyDefinitionOutput.make_one(
            self.boto3_raw_data["policyDefinition"]
        )

    @cached_property
    def qualityReport(self):  # pragma: no cover
        return AutomatedReasoningPolicyDefinitionQualityReport.make_one(
            self.boto3_raw_data["qualityReport"]
        )

    @cached_property
    def buildLog(self):  # pragma: no cover
        return AutomatedReasoningPolicyBuildLog.make_one(
            self.boto3_raw_data["buildLog"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AutomatedReasoningPolicyBuildResultAssetsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutomatedReasoningPolicyBuildResultAssetsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutomatedReasoningPolicyBuildWorkflowSource:
    boto3_raw_data: "type_defs.AutomatedReasoningPolicyBuildWorkflowSourceTypeDef" = (
        dataclasses.field()
    )

    policyDefinition = field("policyDefinition")

    @cached_property
    def workflowContent(self):  # pragma: no cover
        return AutomatedReasoningPolicyWorkflowTypeContent.make_one(
            self.boto3_raw_data["workflowContent"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AutomatedReasoningPolicyBuildWorkflowSourceTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutomatedReasoningPolicyBuildWorkflowSourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RetrieveAndGenerateConfigurationOutput:
    boto3_raw_data: "type_defs.RetrieveAndGenerateConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    type = field("type")

    @cached_property
    def knowledgeBaseConfiguration(self):  # pragma: no cover
        return KnowledgeBaseRetrieveAndGenerateConfigurationOutput.make_one(
            self.boto3_raw_data["knowledgeBaseConfiguration"]
        )

    @cached_property
    def externalSourcesConfiguration(self):  # pragma: no cover
        return ExternalSourcesRetrieveAndGenerateConfigurationOutput.make_one(
            self.boto3_raw_data["externalSourcesConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RetrieveAndGenerateConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RetrieveAndGenerateConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RetrieveAndGenerateConfiguration:
    boto3_raw_data: "type_defs.RetrieveAndGenerateConfigurationTypeDef" = (
        dataclasses.field()
    )

    type = field("type")

    @cached_property
    def knowledgeBaseConfiguration(self):  # pragma: no cover
        return KnowledgeBaseRetrieveAndGenerateConfiguration.make_one(
            self.boto3_raw_data["knowledgeBaseConfiguration"]
        )

    @cached_property
    def externalSourcesConfiguration(self):  # pragma: no cover
        return ExternalSourcesRetrieveAndGenerateConfiguration.make_one(
            self.boto3_raw_data["externalSourcesConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RetrieveAndGenerateConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RetrieveAndGenerateConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAutomatedReasoningPolicyBuildWorkflowResultAssetsResponse:
    boto3_raw_data: (
        "type_defs.GetAutomatedReasoningPolicyBuildWorkflowResultAssetsResponseTypeDef"
    ) = dataclasses.field()

    policyArn = field("policyArn")
    buildWorkflowId = field("buildWorkflowId")

    @cached_property
    def buildWorkflowAssets(self):  # pragma: no cover
        return AutomatedReasoningPolicyBuildResultAssets.make_one(
            self.boto3_raw_data["buildWorkflowAssets"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetAutomatedReasoningPolicyBuildWorkflowResultAssetsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.GetAutomatedReasoningPolicyBuildWorkflowResultAssetsResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartAutomatedReasoningPolicyBuildWorkflowRequest:
    boto3_raw_data: (
        "type_defs.StartAutomatedReasoningPolicyBuildWorkflowRequestTypeDef"
    ) = dataclasses.field()

    policyArn = field("policyArn")
    buildWorkflowType = field("buildWorkflowType")

    @cached_property
    def sourceContent(self):  # pragma: no cover
        return AutomatedReasoningPolicyBuildWorkflowSource.make_one(
            self.boto3_raw_data["sourceContent"]
        )

    clientRequestToken = field("clientRequestToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartAutomatedReasoningPolicyBuildWorkflowRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.StartAutomatedReasoningPolicyBuildWorkflowRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KnowledgeBaseConfigOutput:
    boto3_raw_data: "type_defs.KnowledgeBaseConfigOutputTypeDef" = dataclasses.field()

    @cached_property
    def retrieveConfig(self):  # pragma: no cover
        return RetrieveConfigOutput.make_one(self.boto3_raw_data["retrieveConfig"])

    @cached_property
    def retrieveAndGenerateConfig(self):  # pragma: no cover
        return RetrieveAndGenerateConfigurationOutput.make_one(
            self.boto3_raw_data["retrieveAndGenerateConfig"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.KnowledgeBaseConfigOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KnowledgeBaseConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KnowledgeBaseConfig:
    boto3_raw_data: "type_defs.KnowledgeBaseConfigTypeDef" = dataclasses.field()

    @cached_property
    def retrieveConfig(self):  # pragma: no cover
        return RetrieveConfig.make_one(self.boto3_raw_data["retrieveConfig"])

    @cached_property
    def retrieveAndGenerateConfig(self):  # pragma: no cover
        return RetrieveAndGenerateConfiguration.make_one(
            self.boto3_raw_data["retrieveAndGenerateConfig"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.KnowledgeBaseConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KnowledgeBaseConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RAGConfigOutput:
    boto3_raw_data: "type_defs.RAGConfigOutputTypeDef" = dataclasses.field()

    @cached_property
    def knowledgeBaseConfig(self):  # pragma: no cover
        return KnowledgeBaseConfigOutput.make_one(
            self.boto3_raw_data["knowledgeBaseConfig"]
        )

    @cached_property
    def precomputedRagSourceConfig(self):  # pragma: no cover
        return EvaluationPrecomputedRagSourceConfig.make_one(
            self.boto3_raw_data["precomputedRagSourceConfig"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RAGConfigOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RAGConfigOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RAGConfig:
    boto3_raw_data: "type_defs.RAGConfigTypeDef" = dataclasses.field()

    @cached_property
    def knowledgeBaseConfig(self):  # pragma: no cover
        return KnowledgeBaseConfig.make_one(self.boto3_raw_data["knowledgeBaseConfig"])

    @cached_property
    def precomputedRagSourceConfig(self):  # pragma: no cover
        return EvaluationPrecomputedRagSourceConfig.make_one(
            self.boto3_raw_data["precomputedRagSourceConfig"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RAGConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RAGConfigTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EvaluationInferenceConfigOutput:
    boto3_raw_data: "type_defs.EvaluationInferenceConfigOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def models(self):  # pragma: no cover
        return EvaluationModelConfig.make_many(self.boto3_raw_data["models"])

    @cached_property
    def ragConfigs(self):  # pragma: no cover
        return RAGConfigOutput.make_many(self.boto3_raw_data["ragConfigs"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.EvaluationInferenceConfigOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EvaluationInferenceConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EvaluationInferenceConfig:
    boto3_raw_data: "type_defs.EvaluationInferenceConfigTypeDef" = dataclasses.field()

    @cached_property
    def models(self):  # pragma: no cover
        return EvaluationModelConfig.make_many(self.boto3_raw_data["models"])

    @cached_property
    def ragConfigs(self):  # pragma: no cover
        return RAGConfig.make_many(self.boto3_raw_data["ragConfigs"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EvaluationInferenceConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EvaluationInferenceConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEvaluationJobResponse:
    boto3_raw_data: "type_defs.GetEvaluationJobResponseTypeDef" = dataclasses.field()

    jobName = field("jobName")
    status = field("status")
    jobArn = field("jobArn")
    jobDescription = field("jobDescription")
    roleArn = field("roleArn")
    customerEncryptionKeyId = field("customerEncryptionKeyId")
    jobType = field("jobType")
    applicationType = field("applicationType")

    @cached_property
    def evaluationConfig(self):  # pragma: no cover
        return EvaluationConfigOutput.make_one(self.boto3_raw_data["evaluationConfig"])

    @cached_property
    def inferenceConfig(self):  # pragma: no cover
        return EvaluationInferenceConfigOutput.make_one(
            self.boto3_raw_data["inferenceConfig"]
        )

    @cached_property
    def outputDataConfig(self):  # pragma: no cover
        return EvaluationOutputDataConfig.make_one(
            self.boto3_raw_data["outputDataConfig"]
        )

    creationTime = field("creationTime")
    lastModifiedTime = field("lastModifiedTime")
    failureMessages = field("failureMessages")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetEvaluationJobResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEvaluationJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateEvaluationJobRequest:
    boto3_raw_data: "type_defs.CreateEvaluationJobRequestTypeDef" = dataclasses.field()

    jobName = field("jobName")
    roleArn = field("roleArn")
    evaluationConfig = field("evaluationConfig")
    inferenceConfig = field("inferenceConfig")

    @cached_property
    def outputDataConfig(self):  # pragma: no cover
        return EvaluationOutputDataConfig.make_one(
            self.boto3_raw_data["outputDataConfig"]
        )

    jobDescription = field("jobDescription")
    clientRequestToken = field("clientRequestToken")
    customerEncryptionKeyId = field("customerEncryptionKeyId")

    @cached_property
    def jobTags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["jobTags"])

    applicationType = field("applicationType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateEvaluationJobRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateEvaluationJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
