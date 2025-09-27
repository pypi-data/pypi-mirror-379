# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_dlm import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class RetentionArchiveTier:
    boto3_raw_data: "type_defs.RetentionArchiveTierTypeDef" = dataclasses.field()

    Count = field("Count")
    Interval = field("Interval")
    IntervalUnit = field("IntervalUnit")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RetentionArchiveTierTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RetentionArchiveTierTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CrossRegionCopyTarget:
    boto3_raw_data: "type_defs.CrossRegionCopyTargetTypeDef" = dataclasses.field()

    TargetRegion = field("TargetRegion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CrossRegionCopyTargetTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CrossRegionCopyTargetTypeDef"]
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
class ScriptOutput:
    boto3_raw_data: "type_defs.ScriptOutputTypeDef" = dataclasses.field()

    ExecutionHandler = field("ExecutionHandler")
    Stages = field("Stages")
    ExecutionHandlerService = field("ExecutionHandlerService")
    ExecuteOperationOnScriptFailure = field("ExecuteOperationOnScriptFailure")
    ExecutionTimeout = field("ExecutionTimeout")
    MaximumRetryCount = field("MaximumRetryCount")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ScriptOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ScriptOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Script:
    boto3_raw_data: "type_defs.ScriptTypeDef" = dataclasses.field()

    ExecutionHandler = field("ExecutionHandler")
    Stages = field("Stages")
    ExecutionHandlerService = field("ExecutionHandlerService")
    ExecuteOperationOnScriptFailure = field("ExecuteOperationOnScriptFailure")
    ExecutionTimeout = field("ExecutionTimeout")
    MaximumRetryCount = field("MaximumRetryCount")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ScriptTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ScriptTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CrossRegionCopyRetainRule:
    boto3_raw_data: "type_defs.CrossRegionCopyRetainRuleTypeDef" = dataclasses.field()

    Interval = field("Interval")
    IntervalUnit = field("IntervalUnit")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CrossRegionCopyRetainRuleTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CrossRegionCopyRetainRuleTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EncryptionConfiguration:
    boto3_raw_data: "type_defs.EncryptionConfigurationTypeDef" = dataclasses.field()

    Encrypted = field("Encrypted")
    CmkArn = field("CmkArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EncryptionConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EncryptionConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CrossRegionCopyDeprecateRule:
    boto3_raw_data: "type_defs.CrossRegionCopyDeprecateRuleTypeDef" = (
        dataclasses.field()
    )

    Interval = field("Interval")
    IntervalUnit = field("IntervalUnit")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CrossRegionCopyDeprecateRuleTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CrossRegionCopyDeprecateRuleTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteLifecyclePolicyRequest:
    boto3_raw_data: "type_defs.DeleteLifecyclePolicyRequestTypeDef" = (
        dataclasses.field()
    )

    PolicyId = field("PolicyId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteLifecyclePolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteLifecyclePolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeprecateRule:
    boto3_raw_data: "type_defs.DeprecateRuleTypeDef" = dataclasses.field()

    Count = field("Count")
    Interval = field("Interval")
    IntervalUnit = field("IntervalUnit")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeprecateRuleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DeprecateRuleTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EventParametersOutput:
    boto3_raw_data: "type_defs.EventParametersOutputTypeDef" = dataclasses.field()

    EventType = field("EventType")
    SnapshotOwner = field("SnapshotOwner")
    DescriptionRegex = field("DescriptionRegex")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EventParametersOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EventParametersOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EventParameters:
    boto3_raw_data: "type_defs.EventParametersTypeDef" = dataclasses.field()

    EventType = field("EventType")
    SnapshotOwner = field("SnapshotOwner")
    DescriptionRegex = field("DescriptionRegex")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EventParametersTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EventParametersTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Tag:
    boto3_raw_data: "type_defs.TagTypeDef" = dataclasses.field()

    Key = field("Key")
    Value = field("Value")

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
class FastRestoreRuleOutput:
    boto3_raw_data: "type_defs.FastRestoreRuleOutputTypeDef" = dataclasses.field()

    AvailabilityZones = field("AvailabilityZones")
    Count = field("Count")
    Interval = field("Interval")
    IntervalUnit = field("IntervalUnit")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FastRestoreRuleOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FastRestoreRuleOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FastRestoreRule:
    boto3_raw_data: "type_defs.FastRestoreRuleTypeDef" = dataclasses.field()

    AvailabilityZones = field("AvailabilityZones")
    Count = field("Count")
    Interval = field("Interval")
    IntervalUnit = field("IntervalUnit")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FastRestoreRuleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FastRestoreRuleTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLifecyclePoliciesRequest:
    boto3_raw_data: "type_defs.GetLifecyclePoliciesRequestTypeDef" = dataclasses.field()

    PolicyIds = field("PolicyIds")
    State = field("State")
    ResourceTypes = field("ResourceTypes")
    TargetTags = field("TargetTags")
    TagsToAdd = field("TagsToAdd")
    DefaultPolicyType = field("DefaultPolicyType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetLifecyclePoliciesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLifecyclePoliciesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LifecyclePolicySummary:
    boto3_raw_data: "type_defs.LifecyclePolicySummaryTypeDef" = dataclasses.field()

    PolicyId = field("PolicyId")
    Description = field("Description")
    State = field("State")
    Tags = field("Tags")
    PolicyType = field("PolicyType")
    DefaultPolicy = field("DefaultPolicy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LifecyclePolicySummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LifecyclePolicySummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLifecyclePolicyRequest:
    boto3_raw_data: "type_defs.GetLifecyclePolicyRequestTypeDef" = dataclasses.field()

    PolicyId = field("PolicyId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetLifecyclePolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLifecyclePolicyRequestTypeDef"]
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

    ResourceArn = field("ResourceArn")

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
class RetainRule:
    boto3_raw_data: "type_defs.RetainRuleTypeDef" = dataclasses.field()

    Count = field("Count")
    Interval = field("Interval")
    IntervalUnit = field("IntervalUnit")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RetainRuleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RetainRuleTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ShareRuleOutput:
    boto3_raw_data: "type_defs.ShareRuleOutputTypeDef" = dataclasses.field()

    TargetAccounts = field("TargetAccounts")
    UnshareInterval = field("UnshareInterval")
    UnshareIntervalUnit = field("UnshareIntervalUnit")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ShareRuleOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ShareRuleOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ShareRule:
    boto3_raw_data: "type_defs.ShareRuleTypeDef" = dataclasses.field()

    TargetAccounts = field("TargetAccounts")
    UnshareInterval = field("UnshareInterval")
    UnshareIntervalUnit = field("UnshareIntervalUnit")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ShareRuleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ShareRuleTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TagResourceRequest:
    boto3_raw_data: "type_defs.TagResourceRequestTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")
    Tags = field("Tags")

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
class UntagResourceRequest:
    boto3_raw_data: "type_defs.UntagResourceRequestTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")
    TagKeys = field("TagKeys")

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
class ArchiveRetainRule:
    boto3_raw_data: "type_defs.ArchiveRetainRuleTypeDef" = dataclasses.field()

    @cached_property
    def RetentionArchiveTier(self):  # pragma: no cover
        return RetentionArchiveTier.make_one(
            self.boto3_raw_data["RetentionArchiveTier"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ArchiveRetainRuleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ArchiveRetainRuleTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateLifecyclePolicyResponse:
    boto3_raw_data: "type_defs.CreateLifecyclePolicyResponseTypeDef" = (
        dataclasses.field()
    )

    PolicyId = field("PolicyId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateLifecyclePolicyResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateLifecyclePolicyResponseTypeDef"]
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

    Tags = field("Tags")

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
class CreateRuleOutput:
    boto3_raw_data: "type_defs.CreateRuleOutputTypeDef" = dataclasses.field()

    Location = field("Location")
    Interval = field("Interval")
    IntervalUnit = field("IntervalUnit")
    Times = field("Times")
    CronExpression = field("CronExpression")

    @cached_property
    def Scripts(self):  # pragma: no cover
        return ScriptOutput.make_many(self.boto3_raw_data["Scripts"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateRuleOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRuleOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRule:
    boto3_raw_data: "type_defs.CreateRuleTypeDef" = dataclasses.field()

    Location = field("Location")
    Interval = field("Interval")
    IntervalUnit = field("IntervalUnit")
    Times = field("Times")
    CronExpression = field("CronExpression")

    @cached_property
    def Scripts(self):  # pragma: no cover
        return Script.make_many(self.boto3_raw_data["Scripts"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateRuleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CreateRuleTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CrossRegionCopyAction:
    boto3_raw_data: "type_defs.CrossRegionCopyActionTypeDef" = dataclasses.field()

    Target = field("Target")

    @cached_property
    def EncryptionConfiguration(self):  # pragma: no cover
        return EncryptionConfiguration.make_one(
            self.boto3_raw_data["EncryptionConfiguration"]
        )

    @cached_property
    def RetainRule(self):  # pragma: no cover
        return CrossRegionCopyRetainRule.make_one(self.boto3_raw_data["RetainRule"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CrossRegionCopyActionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CrossRegionCopyActionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CrossRegionCopyRule:
    boto3_raw_data: "type_defs.CrossRegionCopyRuleTypeDef" = dataclasses.field()

    Encrypted = field("Encrypted")
    TargetRegion = field("TargetRegion")
    Target = field("Target")
    CmkArn = field("CmkArn")
    CopyTags = field("CopyTags")

    @cached_property
    def RetainRule(self):  # pragma: no cover
        return CrossRegionCopyRetainRule.make_one(self.boto3_raw_data["RetainRule"])

    @cached_property
    def DeprecateRule(self):  # pragma: no cover
        return CrossRegionCopyDeprecateRule.make_one(
            self.boto3_raw_data["DeprecateRule"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CrossRegionCopyRuleTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CrossRegionCopyRuleTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EventSourceOutput:
    boto3_raw_data: "type_defs.EventSourceOutputTypeDef" = dataclasses.field()

    Type = field("Type")

    @cached_property
    def Parameters(self):  # pragma: no cover
        return EventParametersOutput.make_one(self.boto3_raw_data["Parameters"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EventSourceOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EventSourceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EventSource:
    boto3_raw_data: "type_defs.EventSourceTypeDef" = dataclasses.field()

    Type = field("Type")

    @cached_property
    def Parameters(self):  # pragma: no cover
        return EventParameters.make_one(self.boto3_raw_data["Parameters"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EventSourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EventSourceTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExclusionsOutput:
    boto3_raw_data: "type_defs.ExclusionsOutputTypeDef" = dataclasses.field()

    ExcludeBootVolumes = field("ExcludeBootVolumes")
    ExcludeVolumeTypes = field("ExcludeVolumeTypes")

    @cached_property
    def ExcludeTags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["ExcludeTags"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExclusionsOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExclusionsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Exclusions:
    boto3_raw_data: "type_defs.ExclusionsTypeDef" = dataclasses.field()

    ExcludeBootVolumes = field("ExcludeBootVolumes")
    ExcludeVolumeTypes = field("ExcludeVolumeTypes")

    @cached_property
    def ExcludeTags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["ExcludeTags"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExclusionsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ExclusionsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ParametersOutput:
    boto3_raw_data: "type_defs.ParametersOutputTypeDef" = dataclasses.field()

    ExcludeBootVolume = field("ExcludeBootVolume")
    NoReboot = field("NoReboot")

    @cached_property
    def ExcludeDataVolumeTags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["ExcludeDataVolumeTags"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ParametersOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ParametersOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Parameters:
    boto3_raw_data: "type_defs.ParametersTypeDef" = dataclasses.field()

    ExcludeBootVolume = field("ExcludeBootVolume")
    NoReboot = field("NoReboot")

    @cached_property
    def ExcludeDataVolumeTags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["ExcludeDataVolumeTags"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ParametersTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ParametersTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLifecyclePoliciesResponse:
    boto3_raw_data: "type_defs.GetLifecyclePoliciesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Policies(self):  # pragma: no cover
        return LifecyclePolicySummary.make_many(self.boto3_raw_data["Policies"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetLifecyclePoliciesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLifecyclePoliciesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ArchiveRule:
    boto3_raw_data: "type_defs.ArchiveRuleTypeDef" = dataclasses.field()

    @cached_property
    def RetainRule(self):  # pragma: no cover
        return ArchiveRetainRule.make_one(self.boto3_raw_data["RetainRule"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ArchiveRuleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ArchiveRuleTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActionOutput:
    boto3_raw_data: "type_defs.ActionOutputTypeDef" = dataclasses.field()

    Name = field("Name")

    @cached_property
    def CrossRegionCopy(self):  # pragma: no cover
        return CrossRegionCopyAction.make_many(self.boto3_raw_data["CrossRegionCopy"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ActionOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ActionOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Action:
    boto3_raw_data: "type_defs.ActionTypeDef" = dataclasses.field()

    Name = field("Name")

    @cached_property
    def CrossRegionCopy(self):  # pragma: no cover
        return CrossRegionCopyAction.make_many(self.boto3_raw_data["CrossRegionCopy"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ActionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ActionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScheduleOutput:
    boto3_raw_data: "type_defs.ScheduleOutputTypeDef" = dataclasses.field()

    Name = field("Name")
    CopyTags = field("CopyTags")

    @cached_property
    def TagsToAdd(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["TagsToAdd"])

    @cached_property
    def VariableTags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["VariableTags"])

    @cached_property
    def CreateRule(self):  # pragma: no cover
        return CreateRuleOutput.make_one(self.boto3_raw_data["CreateRule"])

    @cached_property
    def RetainRule(self):  # pragma: no cover
        return RetainRule.make_one(self.boto3_raw_data["RetainRule"])

    @cached_property
    def FastRestoreRule(self):  # pragma: no cover
        return FastRestoreRuleOutput.make_one(self.boto3_raw_data["FastRestoreRule"])

    @cached_property
    def CrossRegionCopyRules(self):  # pragma: no cover
        return CrossRegionCopyRule.make_many(
            self.boto3_raw_data["CrossRegionCopyRules"]
        )

    @cached_property
    def ShareRules(self):  # pragma: no cover
        return ShareRuleOutput.make_many(self.boto3_raw_data["ShareRules"])

    @cached_property
    def DeprecateRule(self):  # pragma: no cover
        return DeprecateRule.make_one(self.boto3_raw_data["DeprecateRule"])

    @cached_property
    def ArchiveRule(self):  # pragma: no cover
        return ArchiveRule.make_one(self.boto3_raw_data["ArchiveRule"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ScheduleOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ScheduleOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Schedule:
    boto3_raw_data: "type_defs.ScheduleTypeDef" = dataclasses.field()

    Name = field("Name")
    CopyTags = field("CopyTags")

    @cached_property
    def TagsToAdd(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["TagsToAdd"])

    @cached_property
    def VariableTags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["VariableTags"])

    @cached_property
    def CreateRule(self):  # pragma: no cover
        return CreateRule.make_one(self.boto3_raw_data["CreateRule"])

    @cached_property
    def RetainRule(self):  # pragma: no cover
        return RetainRule.make_one(self.boto3_raw_data["RetainRule"])

    @cached_property
    def FastRestoreRule(self):  # pragma: no cover
        return FastRestoreRule.make_one(self.boto3_raw_data["FastRestoreRule"])

    @cached_property
    def CrossRegionCopyRules(self):  # pragma: no cover
        return CrossRegionCopyRule.make_many(
            self.boto3_raw_data["CrossRegionCopyRules"]
        )

    @cached_property
    def ShareRules(self):  # pragma: no cover
        return ShareRule.make_many(self.boto3_raw_data["ShareRules"])

    @cached_property
    def DeprecateRule(self):  # pragma: no cover
        return DeprecateRule.make_one(self.boto3_raw_data["DeprecateRule"])

    @cached_property
    def ArchiveRule(self):  # pragma: no cover
        return ArchiveRule.make_one(self.boto3_raw_data["ArchiveRule"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ScheduleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ScheduleTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PolicyDetailsOutput:
    boto3_raw_data: "type_defs.PolicyDetailsOutputTypeDef" = dataclasses.field()

    PolicyType = field("PolicyType")
    ResourceTypes = field("ResourceTypes")
    ResourceLocations = field("ResourceLocations")

    @cached_property
    def TargetTags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["TargetTags"])

    @cached_property
    def Schedules(self):  # pragma: no cover
        return ScheduleOutput.make_many(self.boto3_raw_data["Schedules"])

    @cached_property
    def Parameters(self):  # pragma: no cover
        return ParametersOutput.make_one(self.boto3_raw_data["Parameters"])

    @cached_property
    def EventSource(self):  # pragma: no cover
        return EventSourceOutput.make_one(self.boto3_raw_data["EventSource"])

    @cached_property
    def Actions(self):  # pragma: no cover
        return ActionOutput.make_many(self.boto3_raw_data["Actions"])

    PolicyLanguage = field("PolicyLanguage")
    ResourceType = field("ResourceType")
    CreateInterval = field("CreateInterval")
    RetainInterval = field("RetainInterval")
    CopyTags = field("CopyTags")

    @cached_property
    def CrossRegionCopyTargets(self):  # pragma: no cover
        return CrossRegionCopyTarget.make_many(
            self.boto3_raw_data["CrossRegionCopyTargets"]
        )

    ExtendDeletion = field("ExtendDeletion")

    @cached_property
    def Exclusions(self):  # pragma: no cover
        return ExclusionsOutput.make_one(self.boto3_raw_data["Exclusions"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PolicyDetailsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PolicyDetailsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PolicyDetails:
    boto3_raw_data: "type_defs.PolicyDetailsTypeDef" = dataclasses.field()

    PolicyType = field("PolicyType")
    ResourceTypes = field("ResourceTypes")
    ResourceLocations = field("ResourceLocations")

    @cached_property
    def TargetTags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["TargetTags"])

    @cached_property
    def Schedules(self):  # pragma: no cover
        return Schedule.make_many(self.boto3_raw_data["Schedules"])

    @cached_property
    def Parameters(self):  # pragma: no cover
        return Parameters.make_one(self.boto3_raw_data["Parameters"])

    @cached_property
    def EventSource(self):  # pragma: no cover
        return EventSource.make_one(self.boto3_raw_data["EventSource"])

    @cached_property
    def Actions(self):  # pragma: no cover
        return Action.make_many(self.boto3_raw_data["Actions"])

    PolicyLanguage = field("PolicyLanguage")
    ResourceType = field("ResourceType")
    CreateInterval = field("CreateInterval")
    RetainInterval = field("RetainInterval")
    CopyTags = field("CopyTags")

    @cached_property
    def CrossRegionCopyTargets(self):  # pragma: no cover
        return CrossRegionCopyTarget.make_many(
            self.boto3_raw_data["CrossRegionCopyTargets"]
        )

    ExtendDeletion = field("ExtendDeletion")

    @cached_property
    def Exclusions(self):  # pragma: no cover
        return Exclusions.make_one(self.boto3_raw_data["Exclusions"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PolicyDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PolicyDetailsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LifecyclePolicy:
    boto3_raw_data: "type_defs.LifecyclePolicyTypeDef" = dataclasses.field()

    PolicyId = field("PolicyId")
    Description = field("Description")
    State = field("State")
    StatusMessage = field("StatusMessage")
    ExecutionRoleArn = field("ExecutionRoleArn")
    DateCreated = field("DateCreated")
    DateModified = field("DateModified")

    @cached_property
    def PolicyDetails(self):  # pragma: no cover
        return PolicyDetailsOutput.make_one(self.boto3_raw_data["PolicyDetails"])

    Tags = field("Tags")
    PolicyArn = field("PolicyArn")
    DefaultPolicy = field("DefaultPolicy")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LifecyclePolicyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LifecyclePolicyTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLifecyclePolicyResponse:
    boto3_raw_data: "type_defs.GetLifecyclePolicyResponseTypeDef" = dataclasses.field()

    @cached_property
    def Policy(self):  # pragma: no cover
        return LifecyclePolicy.make_one(self.boto3_raw_data["Policy"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetLifecyclePolicyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLifecyclePolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateLifecyclePolicyRequest:
    boto3_raw_data: "type_defs.CreateLifecyclePolicyRequestTypeDef" = (
        dataclasses.field()
    )

    ExecutionRoleArn = field("ExecutionRoleArn")
    Description = field("Description")
    State = field("State")
    PolicyDetails = field("PolicyDetails")
    Tags = field("Tags")
    DefaultPolicy = field("DefaultPolicy")
    CreateInterval = field("CreateInterval")
    RetainInterval = field("RetainInterval")
    CopyTags = field("CopyTags")
    ExtendDeletion = field("ExtendDeletion")

    @cached_property
    def CrossRegionCopyTargets(self):  # pragma: no cover
        return CrossRegionCopyTarget.make_many(
            self.boto3_raw_data["CrossRegionCopyTargets"]
        )

    Exclusions = field("Exclusions")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateLifecyclePolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateLifecyclePolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateLifecyclePolicyRequest:
    boto3_raw_data: "type_defs.UpdateLifecyclePolicyRequestTypeDef" = (
        dataclasses.field()
    )

    PolicyId = field("PolicyId")
    ExecutionRoleArn = field("ExecutionRoleArn")
    State = field("State")
    Description = field("Description")
    PolicyDetails = field("PolicyDetails")
    CreateInterval = field("CreateInterval")
    RetainInterval = field("RetainInterval")
    CopyTags = field("CopyTags")
    ExtendDeletion = field("ExtendDeletion")

    @cached_property
    def CrossRegionCopyTargets(self):  # pragma: no cover
        return CrossRegionCopyTarget.make_many(
            self.boto3_raw_data["CrossRegionCopyTargets"]
        )

    Exclusions = field("Exclusions")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateLifecyclePolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateLifecyclePolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
