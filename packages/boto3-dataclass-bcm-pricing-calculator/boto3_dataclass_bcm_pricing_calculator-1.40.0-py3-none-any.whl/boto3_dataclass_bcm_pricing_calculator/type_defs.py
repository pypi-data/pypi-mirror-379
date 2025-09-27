# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_bcm_pricing_calculator import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AddReservedInstanceAction:
    boto3_raw_data: "type_defs.AddReservedInstanceActionTypeDef" = dataclasses.field()

    reservedInstancesOfferingId = field("reservedInstancesOfferingId")
    instanceCount = field("instanceCount")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AddReservedInstanceActionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddReservedInstanceActionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddSavingsPlanAction:
    boto3_raw_data: "type_defs.AddSavingsPlanActionTypeDef" = dataclasses.field()

    savingsPlanOfferingId = field("savingsPlanOfferingId")
    commitment = field("commitment")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AddSavingsPlanActionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddSavingsPlanActionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchCreateBillScenarioCommitmentModificationError:
    boto3_raw_data: (
        "type_defs.BatchCreateBillScenarioCommitmentModificationErrorTypeDef"
    ) = dataclasses.field()

    key = field("key")
    errorMessage = field("errorMessage")
    errorCode = field("errorCode")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchCreateBillScenarioCommitmentModificationErrorTypeDef"
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
                "type_defs.BatchCreateBillScenarioCommitmentModificationErrorTypeDef"
            ]
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
class BatchCreateBillScenarioUsageModificationError:
    boto3_raw_data: "type_defs.BatchCreateBillScenarioUsageModificationErrorTypeDef" = (
        dataclasses.field()
    )

    key = field("key")
    errorMessage = field("errorMessage")
    errorCode = field("errorCode")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchCreateBillScenarioUsageModificationErrorTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchCreateBillScenarioUsageModificationErrorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UsageQuantity:
    boto3_raw_data: "type_defs.UsageQuantityTypeDef" = dataclasses.field()

    startHour = field("startHour")
    unit = field("unit")
    amount = field("amount")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UsageQuantityTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UsageQuantityTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchCreateWorkloadEstimateUsageError:
    boto3_raw_data: "type_defs.BatchCreateWorkloadEstimateUsageErrorTypeDef" = (
        dataclasses.field()
    )

    key = field("key")
    errorCode = field("errorCode")
    errorMessage = field("errorMessage")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchCreateWorkloadEstimateUsageErrorTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchCreateWorkloadEstimateUsageErrorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkloadEstimateUsageQuantity:
    boto3_raw_data: "type_defs.WorkloadEstimateUsageQuantityTypeDef" = (
        dataclasses.field()
    )

    unit = field("unit")
    amount = field("amount")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.WorkloadEstimateUsageQuantityTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WorkloadEstimateUsageQuantityTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchDeleteBillScenarioCommitmentModificationError:
    boto3_raw_data: (
        "type_defs.BatchDeleteBillScenarioCommitmentModificationErrorTypeDef"
    ) = dataclasses.field()

    id = field("id")
    errorCode = field("errorCode")
    errorMessage = field("errorMessage")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchDeleteBillScenarioCommitmentModificationErrorTypeDef"
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
                "type_defs.BatchDeleteBillScenarioCommitmentModificationErrorTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchDeleteBillScenarioCommitmentModificationRequest:
    boto3_raw_data: (
        "type_defs.BatchDeleteBillScenarioCommitmentModificationRequestTypeDef"
    ) = dataclasses.field()

    billScenarioId = field("billScenarioId")
    ids = field("ids")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchDeleteBillScenarioCommitmentModificationRequestTypeDef"
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
                "type_defs.BatchDeleteBillScenarioCommitmentModificationRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchDeleteBillScenarioUsageModificationError:
    boto3_raw_data: "type_defs.BatchDeleteBillScenarioUsageModificationErrorTypeDef" = (
        dataclasses.field()
    )

    id = field("id")
    errorMessage = field("errorMessage")
    errorCode = field("errorCode")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchDeleteBillScenarioUsageModificationErrorTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchDeleteBillScenarioUsageModificationErrorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchDeleteBillScenarioUsageModificationRequest:
    boto3_raw_data: (
        "type_defs.BatchDeleteBillScenarioUsageModificationRequestTypeDef"
    ) = dataclasses.field()

    billScenarioId = field("billScenarioId")
    ids = field("ids")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchDeleteBillScenarioUsageModificationRequestTypeDef"
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
                "type_defs.BatchDeleteBillScenarioUsageModificationRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchDeleteWorkloadEstimateUsageError:
    boto3_raw_data: "type_defs.BatchDeleteWorkloadEstimateUsageErrorTypeDef" = (
        dataclasses.field()
    )

    id = field("id")
    errorMessage = field("errorMessage")
    errorCode = field("errorCode")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchDeleteWorkloadEstimateUsageErrorTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchDeleteWorkloadEstimateUsageErrorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchDeleteWorkloadEstimateUsageRequest:
    boto3_raw_data: "type_defs.BatchDeleteWorkloadEstimateUsageRequestTypeDef" = (
        dataclasses.field()
    )

    workloadEstimateId = field("workloadEstimateId")
    ids = field("ids")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchDeleteWorkloadEstimateUsageRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchDeleteWorkloadEstimateUsageRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchUpdateBillScenarioCommitmentModificationEntry:
    boto3_raw_data: (
        "type_defs.BatchUpdateBillScenarioCommitmentModificationEntryTypeDef"
    ) = dataclasses.field()

    id = field("id")
    group = field("group")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchUpdateBillScenarioCommitmentModificationEntryTypeDef"
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
                "type_defs.BatchUpdateBillScenarioCommitmentModificationEntryTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchUpdateBillScenarioCommitmentModificationError:
    boto3_raw_data: (
        "type_defs.BatchUpdateBillScenarioCommitmentModificationErrorTypeDef"
    ) = dataclasses.field()

    id = field("id")
    errorCode = field("errorCode")
    errorMessage = field("errorMessage")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchUpdateBillScenarioCommitmentModificationErrorTypeDef"
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
                "type_defs.BatchUpdateBillScenarioCommitmentModificationErrorTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchUpdateBillScenarioUsageModificationError:
    boto3_raw_data: "type_defs.BatchUpdateBillScenarioUsageModificationErrorTypeDef" = (
        dataclasses.field()
    )

    id = field("id")
    errorMessage = field("errorMessage")
    errorCode = field("errorCode")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchUpdateBillScenarioUsageModificationErrorTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchUpdateBillScenarioUsageModificationErrorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchUpdateWorkloadEstimateUsageEntry:
    boto3_raw_data: "type_defs.BatchUpdateWorkloadEstimateUsageEntryTypeDef" = (
        dataclasses.field()
    )

    id = field("id")
    group = field("group")
    amount = field("amount")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchUpdateWorkloadEstimateUsageEntryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchUpdateWorkloadEstimateUsageEntryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchUpdateWorkloadEstimateUsageError:
    boto3_raw_data: "type_defs.BatchUpdateWorkloadEstimateUsageErrorTypeDef" = (
        dataclasses.field()
    )

    id = field("id")
    errorMessage = field("errorMessage")
    errorCode = field("errorCode")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchUpdateWorkloadEstimateUsageErrorTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchUpdateWorkloadEstimateUsageErrorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CostAmount:
    boto3_raw_data: "type_defs.CostAmountTypeDef" = dataclasses.field()

    amount = field("amount")
    currency = field("currency")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CostAmountTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CostAmountTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UsageQuantityResult:
    boto3_raw_data: "type_defs.UsageQuantityResultTypeDef" = dataclasses.field()

    amount = field("amount")
    unit = field("unit")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UsageQuantityResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UsageQuantityResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BillIntervalOutput:
    boto3_raw_data: "type_defs.BillIntervalOutputTypeDef" = dataclasses.field()

    start = field("start")
    end = field("end")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BillIntervalOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BillIntervalOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NegateReservedInstanceAction:
    boto3_raw_data: "type_defs.NegateReservedInstanceActionTypeDef" = (
        dataclasses.field()
    )

    reservedInstancesId = field("reservedInstancesId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NegateReservedInstanceActionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NegateReservedInstanceActionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NegateSavingsPlanAction:
    boto3_raw_data: "type_defs.NegateSavingsPlanActionTypeDef" = dataclasses.field()

    savingsPlanId = field("savingsPlanId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NegateSavingsPlanActionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NegateSavingsPlanActionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateBillEstimateRequest:
    boto3_raw_data: "type_defs.CreateBillEstimateRequestTypeDef" = dataclasses.field()

    billScenarioId = field("billScenarioId")
    name = field("name")
    clientToken = field("clientToken")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateBillEstimateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateBillEstimateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateBillScenarioRequest:
    boto3_raw_data: "type_defs.CreateBillScenarioRequestTypeDef" = dataclasses.field()

    name = field("name")
    clientToken = field("clientToken")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateBillScenarioRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateBillScenarioRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateWorkloadEstimateRequest:
    boto3_raw_data: "type_defs.CreateWorkloadEstimateRequestTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    clientToken = field("clientToken")
    rateType = field("rateType")
    tags = field("tags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateWorkloadEstimateRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateWorkloadEstimateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteBillEstimateRequest:
    boto3_raw_data: "type_defs.DeleteBillEstimateRequestTypeDef" = dataclasses.field()

    identifier = field("identifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteBillEstimateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteBillEstimateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteBillScenarioRequest:
    boto3_raw_data: "type_defs.DeleteBillScenarioRequestTypeDef" = dataclasses.field()

    identifier = field("identifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteBillScenarioRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteBillScenarioRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteWorkloadEstimateRequest:
    boto3_raw_data: "type_defs.DeleteWorkloadEstimateRequestTypeDef" = (
        dataclasses.field()
    )

    identifier = field("identifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteWorkloadEstimateRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteWorkloadEstimateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExpressionFilterOutput:
    boto3_raw_data: "type_defs.ExpressionFilterOutputTypeDef" = dataclasses.field()

    key = field("key")
    matchOptions = field("matchOptions")
    values = field("values")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExpressionFilterOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExpressionFilterOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExpressionFilter:
    boto3_raw_data: "type_defs.ExpressionFilterTypeDef" = dataclasses.field()

    key = field("key")
    matchOptions = field("matchOptions")
    values = field("values")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExpressionFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExpressionFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBillEstimateRequest:
    boto3_raw_data: "type_defs.GetBillEstimateRequestTypeDef" = dataclasses.field()

    identifier = field("identifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetBillEstimateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBillEstimateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBillScenarioRequest:
    boto3_raw_data: "type_defs.GetBillScenarioRequestTypeDef" = dataclasses.field()

    identifier = field("identifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetBillScenarioRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBillScenarioRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetWorkloadEstimateRequest:
    boto3_raw_data: "type_defs.GetWorkloadEstimateRequestTypeDef" = dataclasses.field()

    identifier = field("identifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetWorkloadEstimateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetWorkloadEstimateRequestTypeDef"]
        ],
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
class ListBillEstimateCommitmentsRequest:
    boto3_raw_data: "type_defs.ListBillEstimateCommitmentsRequestTypeDef" = (
        dataclasses.field()
    )

    billEstimateId = field("billEstimateId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListBillEstimateCommitmentsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBillEstimateCommitmentsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBillEstimateInputCommitmentModificationsRequest:
    boto3_raw_data: (
        "type_defs.ListBillEstimateInputCommitmentModificationsRequestTypeDef"
    ) = dataclasses.field()

    billEstimateId = field("billEstimateId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListBillEstimateInputCommitmentModificationsRequestTypeDef"
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
                "type_defs.ListBillEstimateInputCommitmentModificationsRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListUsageFilter:
    boto3_raw_data: "type_defs.ListUsageFilterTypeDef" = dataclasses.field()

    name = field("name")
    values = field("values")
    matchOption = field("matchOption")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListUsageFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ListUsageFilterTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBillEstimateLineItemsFilter:
    boto3_raw_data: "type_defs.ListBillEstimateLineItemsFilterTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    values = field("values")
    matchOption = field("matchOption")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListBillEstimateLineItemsFilterTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBillEstimateLineItemsFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBillEstimatesFilter:
    boto3_raw_data: "type_defs.ListBillEstimatesFilterTypeDef" = dataclasses.field()

    name = field("name")
    values = field("values")
    matchOption = field("matchOption")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListBillEstimatesFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBillEstimatesFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBillScenarioCommitmentModificationsRequest:
    boto3_raw_data: (
        "type_defs.ListBillScenarioCommitmentModificationsRequestTypeDef"
    ) = dataclasses.field()

    billScenarioId = field("billScenarioId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListBillScenarioCommitmentModificationsRequestTypeDef"
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
                "type_defs.ListBillScenarioCommitmentModificationsRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBillScenariosFilter:
    boto3_raw_data: "type_defs.ListBillScenariosFilterTypeDef" = dataclasses.field()

    name = field("name")
    values = field("values")
    matchOption = field("matchOption")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListBillScenariosFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBillScenariosFilterTypeDef"]
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

    arn = field("arn")

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
class ListWorkloadEstimatesFilter:
    boto3_raw_data: "type_defs.ListWorkloadEstimatesFilterTypeDef" = dataclasses.field()

    name = field("name")
    values = field("values")
    matchOption = field("matchOption")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListWorkloadEstimatesFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWorkloadEstimatesFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkloadEstimateSummary:
    boto3_raw_data: "type_defs.WorkloadEstimateSummaryTypeDef" = dataclasses.field()

    id = field("id")
    name = field("name")
    createdAt = field("createdAt")
    expiresAt = field("expiresAt")
    rateType = field("rateType")
    rateTimestamp = field("rateTimestamp")
    status = field("status")
    totalCost = field("totalCost")
    costCurrency = field("costCurrency")
    failureMessage = field("failureMessage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.WorkloadEstimateSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WorkloadEstimateSummaryTypeDef"]
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

    arn = field("arn")
    tags = field("tags")

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

    arn = field("arn")
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
class UpdatePreferencesRequest:
    boto3_raw_data: "type_defs.UpdatePreferencesRequestTypeDef" = dataclasses.field()

    managementAccountRateTypeSelections = field("managementAccountRateTypeSelections")
    memberAccountRateTypeSelections = field("memberAccountRateTypeSelections")
    standaloneAccountRateTypeSelections = field("standaloneAccountRateTypeSelections")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdatePreferencesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePreferencesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateWorkloadEstimateResponse:
    boto3_raw_data: "type_defs.CreateWorkloadEstimateResponseTypeDef" = (
        dataclasses.field()
    )

    id = field("id")
    name = field("name")
    createdAt = field("createdAt")
    expiresAt = field("expiresAt")
    rateType = field("rateType")
    rateTimestamp = field("rateTimestamp")
    status = field("status")
    totalCost = field("totalCost")
    costCurrency = field("costCurrency")
    failureMessage = field("failureMessage")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateWorkloadEstimateResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateWorkloadEstimateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPreferencesResponse:
    boto3_raw_data: "type_defs.GetPreferencesResponseTypeDef" = dataclasses.field()

    managementAccountRateTypeSelections = field("managementAccountRateTypeSelections")
    memberAccountRateTypeSelections = field("memberAccountRateTypeSelections")
    standaloneAccountRateTypeSelections = field("standaloneAccountRateTypeSelections")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetPreferencesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPreferencesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetWorkloadEstimateResponse:
    boto3_raw_data: "type_defs.GetWorkloadEstimateResponseTypeDef" = dataclasses.field()

    id = field("id")
    name = field("name")
    createdAt = field("createdAt")
    expiresAt = field("expiresAt")
    rateType = field("rateType")
    rateTimestamp = field("rateTimestamp")
    status = field("status")
    totalCost = field("totalCost")
    costCurrency = field("costCurrency")
    failureMessage = field("failureMessage")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetWorkloadEstimateResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetWorkloadEstimateResponseTypeDef"]
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

    tags = field("tags")

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
class UpdatePreferencesResponse:
    boto3_raw_data: "type_defs.UpdatePreferencesResponseTypeDef" = dataclasses.field()

    managementAccountRateTypeSelections = field("managementAccountRateTypeSelections")
    memberAccountRateTypeSelections = field("memberAccountRateTypeSelections")
    standaloneAccountRateTypeSelections = field("standaloneAccountRateTypeSelections")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdatePreferencesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePreferencesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateWorkloadEstimateResponse:
    boto3_raw_data: "type_defs.UpdateWorkloadEstimateResponseTypeDef" = (
        dataclasses.field()
    )

    id = field("id")
    name = field("name")
    createdAt = field("createdAt")
    expiresAt = field("expiresAt")
    rateType = field("rateType")
    rateTimestamp = field("rateTimestamp")
    status = field("status")
    totalCost = field("totalCost")
    costCurrency = field("costCurrency")
    failureMessage = field("failureMessage")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateWorkloadEstimateResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateWorkloadEstimateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchDeleteBillScenarioCommitmentModificationResponse:
    boto3_raw_data: (
        "type_defs.BatchDeleteBillScenarioCommitmentModificationResponseTypeDef"
    ) = dataclasses.field()

    @cached_property
    def errors(self):  # pragma: no cover
        return BatchDeleteBillScenarioCommitmentModificationError.make_many(
            self.boto3_raw_data["errors"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchDeleteBillScenarioCommitmentModificationResponseTypeDef"
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
                "type_defs.BatchDeleteBillScenarioCommitmentModificationResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchDeleteBillScenarioUsageModificationResponse:
    boto3_raw_data: (
        "type_defs.BatchDeleteBillScenarioUsageModificationResponseTypeDef"
    ) = dataclasses.field()

    @cached_property
    def errors(self):  # pragma: no cover
        return BatchDeleteBillScenarioUsageModificationError.make_many(
            self.boto3_raw_data["errors"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchDeleteBillScenarioUsageModificationResponseTypeDef"
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
                "type_defs.BatchDeleteBillScenarioUsageModificationResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchDeleteWorkloadEstimateUsageResponse:
    boto3_raw_data: "type_defs.BatchDeleteWorkloadEstimateUsageResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def errors(self):  # pragma: no cover
        return BatchDeleteWorkloadEstimateUsageError.make_many(
            self.boto3_raw_data["errors"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchDeleteWorkloadEstimateUsageResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchDeleteWorkloadEstimateUsageResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchUpdateBillScenarioCommitmentModificationRequest:
    boto3_raw_data: (
        "type_defs.BatchUpdateBillScenarioCommitmentModificationRequestTypeDef"
    ) = dataclasses.field()

    billScenarioId = field("billScenarioId")

    @cached_property
    def commitmentModifications(self):  # pragma: no cover
        return BatchUpdateBillScenarioCommitmentModificationEntry.make_many(
            self.boto3_raw_data["commitmentModifications"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchUpdateBillScenarioCommitmentModificationRequestTypeDef"
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
                "type_defs.BatchUpdateBillScenarioCommitmentModificationRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchUpdateWorkloadEstimateUsageRequest:
    boto3_raw_data: "type_defs.BatchUpdateWorkloadEstimateUsageRequestTypeDef" = (
        dataclasses.field()
    )

    workloadEstimateId = field("workloadEstimateId")

    @cached_property
    def usage(self):  # pragma: no cover
        return BatchUpdateWorkloadEstimateUsageEntry.make_many(
            self.boto3_raw_data["usage"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchUpdateWorkloadEstimateUsageRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchUpdateWorkloadEstimateUsageRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BillEstimateCommitmentSummary:
    boto3_raw_data: "type_defs.BillEstimateCommitmentSummaryTypeDef" = (
        dataclasses.field()
    )

    id = field("id")
    purchaseAgreementType = field("purchaseAgreementType")
    offeringId = field("offeringId")
    usageAccountId = field("usageAccountId")
    region = field("region")
    termLength = field("termLength")
    paymentOption = field("paymentOption")

    @cached_property
    def upfrontPayment(self):  # pragma: no cover
        return CostAmount.make_one(self.boto3_raw_data["upfrontPayment"])

    @cached_property
    def monthlyPayment(self):  # pragma: no cover
        return CostAmount.make_one(self.boto3_raw_data["monthlyPayment"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BillEstimateCommitmentSummaryTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BillEstimateCommitmentSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CostDifference:
    boto3_raw_data: "type_defs.CostDifferenceTypeDef" = dataclasses.field()

    @cached_property
    def historicalCost(self):  # pragma: no cover
        return CostAmount.make_one(self.boto3_raw_data["historicalCost"])

    @cached_property
    def estimatedCost(self):  # pragma: no cover
        return CostAmount.make_one(self.boto3_raw_data["estimatedCost"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CostDifferenceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CostDifferenceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BillEstimateLineItemSummary:
    boto3_raw_data: "type_defs.BillEstimateLineItemSummaryTypeDef" = dataclasses.field()

    serviceCode = field("serviceCode")
    usageType = field("usageType")
    operation = field("operation")
    location = field("location")
    availabilityZone = field("availabilityZone")
    id = field("id")
    lineItemId = field("lineItemId")
    lineItemType = field("lineItemType")
    payerAccountId = field("payerAccountId")
    usageAccountId = field("usageAccountId")

    @cached_property
    def estimatedUsageQuantity(self):  # pragma: no cover
        return UsageQuantityResult.make_one(
            self.boto3_raw_data["estimatedUsageQuantity"]
        )

    @cached_property
    def estimatedCost(self):  # pragma: no cover
        return CostAmount.make_one(self.boto3_raw_data["estimatedCost"])

    @cached_property
    def historicalUsageQuantity(self):  # pragma: no cover
        return UsageQuantityResult.make_one(
            self.boto3_raw_data["historicalUsageQuantity"]
        )

    @cached_property
    def historicalCost(self):  # pragma: no cover
        return CostAmount.make_one(self.boto3_raw_data["historicalCost"])

    savingsPlanArns = field("savingsPlanArns")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BillEstimateLineItemSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BillEstimateLineItemSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BillEstimateSummary:
    boto3_raw_data: "type_defs.BillEstimateSummaryTypeDef" = dataclasses.field()

    id = field("id")
    name = field("name")
    status = field("status")

    @cached_property
    def billInterval(self):  # pragma: no cover
        return BillIntervalOutput.make_one(self.boto3_raw_data["billInterval"])

    createdAt = field("createdAt")
    expiresAt = field("expiresAt")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BillEstimateSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BillEstimateSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BillScenarioSummary:
    boto3_raw_data: "type_defs.BillScenarioSummaryTypeDef" = dataclasses.field()

    id = field("id")
    name = field("name")

    @cached_property
    def billInterval(self):  # pragma: no cover
        return BillIntervalOutput.make_one(self.boto3_raw_data["billInterval"])

    status = field("status")
    createdAt = field("createdAt")
    expiresAt = field("expiresAt")
    failureMessage = field("failureMessage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BillScenarioSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BillScenarioSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateBillScenarioResponse:
    boto3_raw_data: "type_defs.CreateBillScenarioResponseTypeDef" = dataclasses.field()

    id = field("id")
    name = field("name")

    @cached_property
    def billInterval(self):  # pragma: no cover
        return BillIntervalOutput.make_one(self.boto3_raw_data["billInterval"])

    status = field("status")
    createdAt = field("createdAt")
    expiresAt = field("expiresAt")
    failureMessage = field("failureMessage")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateBillScenarioResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateBillScenarioResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBillScenarioResponse:
    boto3_raw_data: "type_defs.GetBillScenarioResponseTypeDef" = dataclasses.field()

    id = field("id")
    name = field("name")

    @cached_property
    def billInterval(self):  # pragma: no cover
        return BillIntervalOutput.make_one(self.boto3_raw_data["billInterval"])

    status = field("status")
    createdAt = field("createdAt")
    expiresAt = field("expiresAt")
    failureMessage = field("failureMessage")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetBillScenarioResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBillScenarioResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateBillScenarioResponse:
    boto3_raw_data: "type_defs.UpdateBillScenarioResponseTypeDef" = dataclasses.field()

    id = field("id")
    name = field("name")

    @cached_property
    def billInterval(self):  # pragma: no cover
        return BillIntervalOutput.make_one(self.boto3_raw_data["billInterval"])

    status = field("status")
    createdAt = field("createdAt")
    expiresAt = field("expiresAt")
    failureMessage = field("failureMessage")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateBillScenarioResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateBillScenarioResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BillInterval:
    boto3_raw_data: "type_defs.BillIntervalTypeDef" = dataclasses.field()

    start = field("start")
    end = field("end")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BillIntervalTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BillIntervalTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FilterTimestamp:
    boto3_raw_data: "type_defs.FilterTimestampTypeDef" = dataclasses.field()

    afterTimestamp = field("afterTimestamp")
    beforeTimestamp = field("beforeTimestamp")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FilterTimestampTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FilterTimestampTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateBillEstimateRequest:
    boto3_raw_data: "type_defs.UpdateBillEstimateRequestTypeDef" = dataclasses.field()

    identifier = field("identifier")
    name = field("name")
    expiresAt = field("expiresAt")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateBillEstimateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateBillEstimateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateBillScenarioRequest:
    boto3_raw_data: "type_defs.UpdateBillScenarioRequestTypeDef" = dataclasses.field()

    identifier = field("identifier")
    name = field("name")
    expiresAt = field("expiresAt")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateBillScenarioRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateBillScenarioRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateWorkloadEstimateRequest:
    boto3_raw_data: "type_defs.UpdateWorkloadEstimateRequestTypeDef" = (
        dataclasses.field()
    )

    identifier = field("identifier")
    name = field("name")
    expiresAt = field("expiresAt")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateWorkloadEstimateRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateWorkloadEstimateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UsageAmount:
    boto3_raw_data: "type_defs.UsageAmountTypeDef" = dataclasses.field()

    startHour = field("startHour")
    amount = field("amount")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UsageAmountTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UsageAmountTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BillScenarioCommitmentModificationAction:
    boto3_raw_data: "type_defs.BillScenarioCommitmentModificationActionTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def addReservedInstanceAction(self):  # pragma: no cover
        return AddReservedInstanceAction.make_one(
            self.boto3_raw_data["addReservedInstanceAction"]
        )

    @cached_property
    def addSavingsPlanAction(self):  # pragma: no cover
        return AddSavingsPlanAction.make_one(
            self.boto3_raw_data["addSavingsPlanAction"]
        )

    @cached_property
    def negateReservedInstanceAction(self):  # pragma: no cover
        return NegateReservedInstanceAction.make_one(
            self.boto3_raw_data["negateReservedInstanceAction"]
        )

    @cached_property
    def negateSavingsPlanAction(self):  # pragma: no cover
        return NegateSavingsPlanAction.make_one(
            self.boto3_raw_data["negateSavingsPlanAction"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BillScenarioCommitmentModificationActionTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BillScenarioCommitmentModificationActionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExpressionOutput:
    boto3_raw_data: "type_defs.ExpressionOutputTypeDef" = dataclasses.field()

    and_ = field("and")
    or_ = field("or")
    not_ = field("not")

    @cached_property
    def costCategories(self):  # pragma: no cover
        return ExpressionFilterOutput.make_one(self.boto3_raw_data["costCategories"])

    @cached_property
    def dimensions(self):  # pragma: no cover
        return ExpressionFilterOutput.make_one(self.boto3_raw_data["dimensions"])

    @cached_property
    def tags(self):  # pragma: no cover
        return ExpressionFilterOutput.make_one(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExpressionOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExpressionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExpressionPaginator:
    boto3_raw_data: "type_defs.ExpressionPaginatorTypeDef" = dataclasses.field()

    and_ = field("and")
    or_ = field("or")
    not_ = field("not")

    @cached_property
    def costCategories(self):  # pragma: no cover
        return ExpressionFilterOutput.make_one(self.boto3_raw_data["costCategories"])

    @cached_property
    def dimensions(self):  # pragma: no cover
        return ExpressionFilterOutput.make_one(self.boto3_raw_data["dimensions"])

    @cached_property
    def tags(self):  # pragma: no cover
        return ExpressionFilterOutput.make_one(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExpressionPaginatorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExpressionPaginatorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBillEstimateCommitmentsRequestPaginate:
    boto3_raw_data: "type_defs.ListBillEstimateCommitmentsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    billEstimateId = field("billEstimateId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListBillEstimateCommitmentsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBillEstimateCommitmentsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBillEstimateInputCommitmentModificationsRequestPaginate:
    boto3_raw_data: (
        "type_defs.ListBillEstimateInputCommitmentModificationsRequestPaginateTypeDef"
    ) = dataclasses.field()

    billEstimateId = field("billEstimateId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListBillEstimateInputCommitmentModificationsRequestPaginateTypeDef"
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
                "type_defs.ListBillEstimateInputCommitmentModificationsRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBillScenarioCommitmentModificationsRequestPaginate:
    boto3_raw_data: (
        "type_defs.ListBillScenarioCommitmentModificationsRequestPaginateTypeDef"
    ) = dataclasses.field()

    billScenarioId = field("billScenarioId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListBillScenarioCommitmentModificationsRequestPaginateTypeDef"
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
                "type_defs.ListBillScenarioCommitmentModificationsRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBillEstimateInputUsageModificationsRequestPaginate:
    boto3_raw_data: (
        "type_defs.ListBillEstimateInputUsageModificationsRequestPaginateTypeDef"
    ) = dataclasses.field()

    billEstimateId = field("billEstimateId")

    @cached_property
    def filters(self):  # pragma: no cover
        return ListUsageFilter.make_many(self.boto3_raw_data["filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListBillEstimateInputUsageModificationsRequestPaginateTypeDef"
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
                "type_defs.ListBillEstimateInputUsageModificationsRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBillEstimateInputUsageModificationsRequest:
    boto3_raw_data: (
        "type_defs.ListBillEstimateInputUsageModificationsRequestTypeDef"
    ) = dataclasses.field()

    billEstimateId = field("billEstimateId")

    @cached_property
    def filters(self):  # pragma: no cover
        return ListUsageFilter.make_many(self.boto3_raw_data["filters"])

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListBillEstimateInputUsageModificationsRequestTypeDef"
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
                "type_defs.ListBillEstimateInputUsageModificationsRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBillScenarioUsageModificationsRequestPaginate:
    boto3_raw_data: (
        "type_defs.ListBillScenarioUsageModificationsRequestPaginateTypeDef"
    ) = dataclasses.field()

    billScenarioId = field("billScenarioId")

    @cached_property
    def filters(self):  # pragma: no cover
        return ListUsageFilter.make_many(self.boto3_raw_data["filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListBillScenarioUsageModificationsRequestPaginateTypeDef"
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
                "type_defs.ListBillScenarioUsageModificationsRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBillScenarioUsageModificationsRequest:
    boto3_raw_data: "type_defs.ListBillScenarioUsageModificationsRequestTypeDef" = (
        dataclasses.field()
    )

    billScenarioId = field("billScenarioId")

    @cached_property
    def filters(self):  # pragma: no cover
        return ListUsageFilter.make_many(self.boto3_raw_data["filters"])

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListBillScenarioUsageModificationsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBillScenarioUsageModificationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWorkloadEstimateUsageRequestPaginate:
    boto3_raw_data: "type_defs.ListWorkloadEstimateUsageRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    workloadEstimateId = field("workloadEstimateId")

    @cached_property
    def filters(self):  # pragma: no cover
        return ListUsageFilter.make_many(self.boto3_raw_data["filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListWorkloadEstimateUsageRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWorkloadEstimateUsageRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWorkloadEstimateUsageRequest:
    boto3_raw_data: "type_defs.ListWorkloadEstimateUsageRequestTypeDef" = (
        dataclasses.field()
    )

    workloadEstimateId = field("workloadEstimateId")

    @cached_property
    def filters(self):  # pragma: no cover
        return ListUsageFilter.make_many(self.boto3_raw_data["filters"])

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListWorkloadEstimateUsageRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWorkloadEstimateUsageRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBillEstimateLineItemsRequestPaginate:
    boto3_raw_data: "type_defs.ListBillEstimateLineItemsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    billEstimateId = field("billEstimateId")

    @cached_property
    def filters(self):  # pragma: no cover
        return ListBillEstimateLineItemsFilter.make_many(self.boto3_raw_data["filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListBillEstimateLineItemsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBillEstimateLineItemsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBillEstimateLineItemsRequest:
    boto3_raw_data: "type_defs.ListBillEstimateLineItemsRequestTypeDef" = (
        dataclasses.field()
    )

    billEstimateId = field("billEstimateId")

    @cached_property
    def filters(self):  # pragma: no cover
        return ListBillEstimateLineItemsFilter.make_many(self.boto3_raw_data["filters"])

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListBillEstimateLineItemsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBillEstimateLineItemsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWorkloadEstimatesResponse:
    boto3_raw_data: "type_defs.ListWorkloadEstimatesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def items(self):  # pragma: no cover
        return WorkloadEstimateSummary.make_many(self.boto3_raw_data["items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListWorkloadEstimatesResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWorkloadEstimatesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBillEstimateCommitmentsResponse:
    boto3_raw_data: "type_defs.ListBillEstimateCommitmentsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def items(self):  # pragma: no cover
        return BillEstimateCommitmentSummary.make_many(self.boto3_raw_data["items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListBillEstimateCommitmentsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBillEstimateCommitmentsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BillEstimateCostSummary:
    boto3_raw_data: "type_defs.BillEstimateCostSummaryTypeDef" = dataclasses.field()

    @cached_property
    def totalCostDifference(self):  # pragma: no cover
        return CostDifference.make_one(self.boto3_raw_data["totalCostDifference"])

    serviceCostDifferences = field("serviceCostDifferences")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BillEstimateCostSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BillEstimateCostSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBillEstimateLineItemsResponse:
    boto3_raw_data: "type_defs.ListBillEstimateLineItemsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def items(self):  # pragma: no cover
        return BillEstimateLineItemSummary.make_many(self.boto3_raw_data["items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListBillEstimateLineItemsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBillEstimateLineItemsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBillEstimatesResponse:
    boto3_raw_data: "type_defs.ListBillEstimatesResponseTypeDef" = dataclasses.field()

    @cached_property
    def items(self):  # pragma: no cover
        return BillEstimateSummary.make_many(self.boto3_raw_data["items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListBillEstimatesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBillEstimatesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBillScenariosResponse:
    boto3_raw_data: "type_defs.ListBillScenariosResponseTypeDef" = dataclasses.field()

    @cached_property
    def items(self):  # pragma: no cover
        return BillScenarioSummary.make_many(self.boto3_raw_data["items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListBillScenariosResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBillScenariosResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBillEstimatesRequestPaginate:
    boto3_raw_data: "type_defs.ListBillEstimatesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def filters(self):  # pragma: no cover
        return ListBillEstimatesFilter.make_many(self.boto3_raw_data["filters"])

    @cached_property
    def createdAtFilter(self):  # pragma: no cover
        return FilterTimestamp.make_one(self.boto3_raw_data["createdAtFilter"])

    @cached_property
    def expiresAtFilter(self):  # pragma: no cover
        return FilterTimestamp.make_one(self.boto3_raw_data["expiresAtFilter"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListBillEstimatesRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBillEstimatesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBillEstimatesRequest:
    boto3_raw_data: "type_defs.ListBillEstimatesRequestTypeDef" = dataclasses.field()

    @cached_property
    def filters(self):  # pragma: no cover
        return ListBillEstimatesFilter.make_many(self.boto3_raw_data["filters"])

    @cached_property
    def createdAtFilter(self):  # pragma: no cover
        return FilterTimestamp.make_one(self.boto3_raw_data["createdAtFilter"])

    @cached_property
    def expiresAtFilter(self):  # pragma: no cover
        return FilterTimestamp.make_one(self.boto3_raw_data["expiresAtFilter"])

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListBillEstimatesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBillEstimatesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBillScenariosRequestPaginate:
    boto3_raw_data: "type_defs.ListBillScenariosRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def filters(self):  # pragma: no cover
        return ListBillScenariosFilter.make_many(self.boto3_raw_data["filters"])

    @cached_property
    def createdAtFilter(self):  # pragma: no cover
        return FilterTimestamp.make_one(self.boto3_raw_data["createdAtFilter"])

    @cached_property
    def expiresAtFilter(self):  # pragma: no cover
        return FilterTimestamp.make_one(self.boto3_raw_data["expiresAtFilter"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListBillScenariosRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBillScenariosRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBillScenariosRequest:
    boto3_raw_data: "type_defs.ListBillScenariosRequestTypeDef" = dataclasses.field()

    @cached_property
    def filters(self):  # pragma: no cover
        return ListBillScenariosFilter.make_many(self.boto3_raw_data["filters"])

    @cached_property
    def createdAtFilter(self):  # pragma: no cover
        return FilterTimestamp.make_one(self.boto3_raw_data["createdAtFilter"])

    @cached_property
    def expiresAtFilter(self):  # pragma: no cover
        return FilterTimestamp.make_one(self.boto3_raw_data["expiresAtFilter"])

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListBillScenariosRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBillScenariosRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWorkloadEstimatesRequestPaginate:
    boto3_raw_data: "type_defs.ListWorkloadEstimatesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def createdAtFilter(self):  # pragma: no cover
        return FilterTimestamp.make_one(self.boto3_raw_data["createdAtFilter"])

    @cached_property
    def expiresAtFilter(self):  # pragma: no cover
        return FilterTimestamp.make_one(self.boto3_raw_data["expiresAtFilter"])

    @cached_property
    def filters(self):  # pragma: no cover
        return ListWorkloadEstimatesFilter.make_many(self.boto3_raw_data["filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListWorkloadEstimatesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWorkloadEstimatesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWorkloadEstimatesRequest:
    boto3_raw_data: "type_defs.ListWorkloadEstimatesRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def createdAtFilter(self):  # pragma: no cover
        return FilterTimestamp.make_one(self.boto3_raw_data["createdAtFilter"])

    @cached_property
    def expiresAtFilter(self):  # pragma: no cover
        return FilterTimestamp.make_one(self.boto3_raw_data["expiresAtFilter"])

    @cached_property
    def filters(self):  # pragma: no cover
        return ListWorkloadEstimatesFilter.make_many(self.boto3_raw_data["filters"])

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListWorkloadEstimatesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWorkloadEstimatesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchUpdateBillScenarioUsageModificationEntry:
    boto3_raw_data: "type_defs.BatchUpdateBillScenarioUsageModificationEntryTypeDef" = (
        dataclasses.field()
    )

    id = field("id")
    group = field("group")

    @cached_property
    def amounts(self):  # pragma: no cover
        return UsageAmount.make_many(self.boto3_raw_data["amounts"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchUpdateBillScenarioUsageModificationEntryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchUpdateBillScenarioUsageModificationEntryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchCreateBillScenarioCommitmentModificationEntry:
    boto3_raw_data: (
        "type_defs.BatchCreateBillScenarioCommitmentModificationEntryTypeDef"
    ) = dataclasses.field()

    key = field("key")
    usageAccountId = field("usageAccountId")

    @cached_property
    def commitmentAction(self):  # pragma: no cover
        return BillScenarioCommitmentModificationAction.make_one(
            self.boto3_raw_data["commitmentAction"]
        )

    group = field("group")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchCreateBillScenarioCommitmentModificationEntryTypeDef"
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
                "type_defs.BatchCreateBillScenarioCommitmentModificationEntryTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchCreateBillScenarioCommitmentModificationItem:
    boto3_raw_data: (
        "type_defs.BatchCreateBillScenarioCommitmentModificationItemTypeDef"
    ) = dataclasses.field()

    key = field("key")
    id = field("id")
    group = field("group")
    usageAccountId = field("usageAccountId")

    @cached_property
    def commitmentAction(self):  # pragma: no cover
        return BillScenarioCommitmentModificationAction.make_one(
            self.boto3_raw_data["commitmentAction"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchCreateBillScenarioCommitmentModificationItemTypeDef"
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
                "type_defs.BatchCreateBillScenarioCommitmentModificationItemTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BillEstimateInputCommitmentModificationSummary:
    boto3_raw_data: (
        "type_defs.BillEstimateInputCommitmentModificationSummaryTypeDef"
    ) = dataclasses.field()

    id = field("id")
    group = field("group")
    usageAccountId = field("usageAccountId")

    @cached_property
    def commitmentAction(self):  # pragma: no cover
        return BillScenarioCommitmentModificationAction.make_one(
            self.boto3_raw_data["commitmentAction"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BillEstimateInputCommitmentModificationSummaryTypeDef"
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
                "type_defs.BillEstimateInputCommitmentModificationSummaryTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BillScenarioCommitmentModificationItem:
    boto3_raw_data: "type_defs.BillScenarioCommitmentModificationItemTypeDef" = (
        dataclasses.field()
    )

    id = field("id")
    usageAccountId = field("usageAccountId")
    group = field("group")

    @cached_property
    def commitmentAction(self):  # pragma: no cover
        return BillScenarioCommitmentModificationAction.make_one(
            self.boto3_raw_data["commitmentAction"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BillScenarioCommitmentModificationItemTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BillScenarioCommitmentModificationItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HistoricalUsageEntityOutput:
    boto3_raw_data: "type_defs.HistoricalUsageEntityOutputTypeDef" = dataclasses.field()

    serviceCode = field("serviceCode")
    usageType = field("usageType")
    operation = field("operation")
    usageAccountId = field("usageAccountId")

    @cached_property
    def billInterval(self):  # pragma: no cover
        return BillIntervalOutput.make_one(self.boto3_raw_data["billInterval"])

    @cached_property
    def filterExpression(self):  # pragma: no cover
        return ExpressionOutput.make_one(self.boto3_raw_data["filterExpression"])

    location = field("location")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.HistoricalUsageEntityOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HistoricalUsageEntityOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HistoricalUsageEntityPaginator:
    boto3_raw_data: "type_defs.HistoricalUsageEntityPaginatorTypeDef" = (
        dataclasses.field()
    )

    serviceCode = field("serviceCode")
    usageType = field("usageType")
    operation = field("operation")
    usageAccountId = field("usageAccountId")

    @cached_property
    def billInterval(self):  # pragma: no cover
        return BillIntervalOutput.make_one(self.boto3_raw_data["billInterval"])

    @cached_property
    def filterExpression(self):  # pragma: no cover
        return ExpressionPaginator.make_one(self.boto3_raw_data["filterExpression"])

    location = field("location")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.HistoricalUsageEntityPaginatorTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HistoricalUsageEntityPaginatorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Expression:
    boto3_raw_data: "type_defs.ExpressionTypeDef" = dataclasses.field()

    and_ = field("and")
    or_ = field("or")
    not_ = field("not")
    costCategories = field("costCategories")
    dimensions = field("dimensions")
    tags = field("tags")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExpressionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ExpressionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateBillEstimateResponse:
    boto3_raw_data: "type_defs.CreateBillEstimateResponseTypeDef" = dataclasses.field()

    id = field("id")
    name = field("name")
    status = field("status")
    failureMessage = field("failureMessage")

    @cached_property
    def billInterval(self):  # pragma: no cover
        return BillIntervalOutput.make_one(self.boto3_raw_data["billInterval"])

    @cached_property
    def costSummary(self):  # pragma: no cover
        return BillEstimateCostSummary.make_one(self.boto3_raw_data["costSummary"])

    createdAt = field("createdAt")
    expiresAt = field("expiresAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateBillEstimateResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateBillEstimateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBillEstimateResponse:
    boto3_raw_data: "type_defs.GetBillEstimateResponseTypeDef" = dataclasses.field()

    id = field("id")
    name = field("name")
    status = field("status")
    failureMessage = field("failureMessage")

    @cached_property
    def billInterval(self):  # pragma: no cover
        return BillIntervalOutput.make_one(self.boto3_raw_data["billInterval"])

    @cached_property
    def costSummary(self):  # pragma: no cover
        return BillEstimateCostSummary.make_one(self.boto3_raw_data["costSummary"])

    createdAt = field("createdAt")
    expiresAt = field("expiresAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetBillEstimateResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBillEstimateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateBillEstimateResponse:
    boto3_raw_data: "type_defs.UpdateBillEstimateResponseTypeDef" = dataclasses.field()

    id = field("id")
    name = field("name")
    status = field("status")
    failureMessage = field("failureMessage")

    @cached_property
    def billInterval(self):  # pragma: no cover
        return BillIntervalOutput.make_one(self.boto3_raw_data["billInterval"])

    @cached_property
    def costSummary(self):  # pragma: no cover
        return BillEstimateCostSummary.make_one(self.boto3_raw_data["costSummary"])

    createdAt = field("createdAt")
    expiresAt = field("expiresAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateBillEstimateResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateBillEstimateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchUpdateBillScenarioUsageModificationRequest:
    boto3_raw_data: (
        "type_defs.BatchUpdateBillScenarioUsageModificationRequestTypeDef"
    ) = dataclasses.field()

    billScenarioId = field("billScenarioId")

    @cached_property
    def usageModifications(self):  # pragma: no cover
        return BatchUpdateBillScenarioUsageModificationEntry.make_many(
            self.boto3_raw_data["usageModifications"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchUpdateBillScenarioUsageModificationRequestTypeDef"
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
                "type_defs.BatchUpdateBillScenarioUsageModificationRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchCreateBillScenarioCommitmentModificationRequest:
    boto3_raw_data: (
        "type_defs.BatchCreateBillScenarioCommitmentModificationRequestTypeDef"
    ) = dataclasses.field()

    billScenarioId = field("billScenarioId")

    @cached_property
    def commitmentModifications(self):  # pragma: no cover
        return BatchCreateBillScenarioCommitmentModificationEntry.make_many(
            self.boto3_raw_data["commitmentModifications"]
        )

    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchCreateBillScenarioCommitmentModificationRequestTypeDef"
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
                "type_defs.BatchCreateBillScenarioCommitmentModificationRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchCreateBillScenarioCommitmentModificationResponse:
    boto3_raw_data: (
        "type_defs.BatchCreateBillScenarioCommitmentModificationResponseTypeDef"
    ) = dataclasses.field()

    @cached_property
    def items(self):  # pragma: no cover
        return BatchCreateBillScenarioCommitmentModificationItem.make_many(
            self.boto3_raw_data["items"]
        )

    @cached_property
    def errors(self):  # pragma: no cover
        return BatchCreateBillScenarioCommitmentModificationError.make_many(
            self.boto3_raw_data["errors"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchCreateBillScenarioCommitmentModificationResponseTypeDef"
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
                "type_defs.BatchCreateBillScenarioCommitmentModificationResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBillEstimateInputCommitmentModificationsResponse:
    boto3_raw_data: (
        "type_defs.ListBillEstimateInputCommitmentModificationsResponseTypeDef"
    ) = dataclasses.field()

    @cached_property
    def items(self):  # pragma: no cover
        return BillEstimateInputCommitmentModificationSummary.make_many(
            self.boto3_raw_data["items"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListBillEstimateInputCommitmentModificationsResponseTypeDef"
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
                "type_defs.ListBillEstimateInputCommitmentModificationsResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchUpdateBillScenarioCommitmentModificationResponse:
    boto3_raw_data: (
        "type_defs.BatchUpdateBillScenarioCommitmentModificationResponseTypeDef"
    ) = dataclasses.field()

    @cached_property
    def items(self):  # pragma: no cover
        return BillScenarioCommitmentModificationItem.make_many(
            self.boto3_raw_data["items"]
        )

    @cached_property
    def errors(self):  # pragma: no cover
        return BatchUpdateBillScenarioCommitmentModificationError.make_many(
            self.boto3_raw_data["errors"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchUpdateBillScenarioCommitmentModificationResponseTypeDef"
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
                "type_defs.BatchUpdateBillScenarioCommitmentModificationResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBillScenarioCommitmentModificationsResponse:
    boto3_raw_data: (
        "type_defs.ListBillScenarioCommitmentModificationsResponseTypeDef"
    ) = dataclasses.field()

    @cached_property
    def items(self):  # pragma: no cover
        return BillScenarioCommitmentModificationItem.make_many(
            self.boto3_raw_data["items"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListBillScenarioCommitmentModificationsResponseTypeDef"
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
                "type_defs.ListBillScenarioCommitmentModificationsResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchCreateBillScenarioUsageModificationItem:
    boto3_raw_data: "type_defs.BatchCreateBillScenarioUsageModificationItemTypeDef" = (
        dataclasses.field()
    )

    serviceCode = field("serviceCode")
    usageType = field("usageType")
    operation = field("operation")
    location = field("location")
    availabilityZone = field("availabilityZone")
    id = field("id")
    group = field("group")
    usageAccountId = field("usageAccountId")

    @cached_property
    def quantities(self):  # pragma: no cover
        return UsageQuantity.make_many(self.boto3_raw_data["quantities"])

    @cached_property
    def historicalUsage(self):  # pragma: no cover
        return HistoricalUsageEntityOutput.make_one(
            self.boto3_raw_data["historicalUsage"]
        )

    key = field("key")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchCreateBillScenarioUsageModificationItemTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchCreateBillScenarioUsageModificationItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchCreateWorkloadEstimateUsageItem:
    boto3_raw_data: "type_defs.BatchCreateWorkloadEstimateUsageItemTypeDef" = (
        dataclasses.field()
    )

    serviceCode = field("serviceCode")
    usageType = field("usageType")
    operation = field("operation")
    location = field("location")
    id = field("id")
    usageAccountId = field("usageAccountId")
    group = field("group")

    @cached_property
    def quantity(self):  # pragma: no cover
        return WorkloadEstimateUsageQuantity.make_one(self.boto3_raw_data["quantity"])

    cost = field("cost")
    currency = field("currency")
    status = field("status")

    @cached_property
    def historicalUsage(self):  # pragma: no cover
        return HistoricalUsageEntityOutput.make_one(
            self.boto3_raw_data["historicalUsage"]
        )

    key = field("key")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchCreateWorkloadEstimateUsageItemTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchCreateWorkloadEstimateUsageItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BillEstimateInputUsageModificationSummary:
    boto3_raw_data: "type_defs.BillEstimateInputUsageModificationSummaryTypeDef" = (
        dataclasses.field()
    )

    serviceCode = field("serviceCode")
    usageType = field("usageType")
    operation = field("operation")
    location = field("location")
    availabilityZone = field("availabilityZone")
    id = field("id")
    group = field("group")
    usageAccountId = field("usageAccountId")

    @cached_property
    def quantities(self):  # pragma: no cover
        return UsageQuantity.make_many(self.boto3_raw_data["quantities"])

    @cached_property
    def historicalUsage(self):  # pragma: no cover
        return HistoricalUsageEntityOutput.make_one(
            self.boto3_raw_data["historicalUsage"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BillEstimateInputUsageModificationSummaryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BillEstimateInputUsageModificationSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BillScenarioUsageModificationItem:
    boto3_raw_data: "type_defs.BillScenarioUsageModificationItemTypeDef" = (
        dataclasses.field()
    )

    serviceCode = field("serviceCode")
    usageType = field("usageType")
    operation = field("operation")
    location = field("location")
    availabilityZone = field("availabilityZone")
    id = field("id")
    group = field("group")
    usageAccountId = field("usageAccountId")

    @cached_property
    def quantities(self):  # pragma: no cover
        return UsageQuantity.make_many(self.boto3_raw_data["quantities"])

    @cached_property
    def historicalUsage(self):  # pragma: no cover
        return HistoricalUsageEntityOutput.make_one(
            self.boto3_raw_data["historicalUsage"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BillScenarioUsageModificationItemTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BillScenarioUsageModificationItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkloadEstimateUsageItem:
    boto3_raw_data: "type_defs.WorkloadEstimateUsageItemTypeDef" = dataclasses.field()

    serviceCode = field("serviceCode")
    usageType = field("usageType")
    operation = field("operation")
    location = field("location")
    id = field("id")
    usageAccountId = field("usageAccountId")
    group = field("group")

    @cached_property
    def quantity(self):  # pragma: no cover
        return WorkloadEstimateUsageQuantity.make_one(self.boto3_raw_data["quantity"])

    cost = field("cost")
    currency = field("currency")
    status = field("status")

    @cached_property
    def historicalUsage(self):  # pragma: no cover
        return HistoricalUsageEntityOutput.make_one(
            self.boto3_raw_data["historicalUsage"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.WorkloadEstimateUsageItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WorkloadEstimateUsageItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BillEstimateInputUsageModificationSummaryPaginator:
    boto3_raw_data: (
        "type_defs.BillEstimateInputUsageModificationSummaryPaginatorTypeDef"
    ) = dataclasses.field()

    serviceCode = field("serviceCode")
    usageType = field("usageType")
    operation = field("operation")
    location = field("location")
    availabilityZone = field("availabilityZone")
    id = field("id")
    group = field("group")
    usageAccountId = field("usageAccountId")

    @cached_property
    def quantities(self):  # pragma: no cover
        return UsageQuantity.make_many(self.boto3_raw_data["quantities"])

    @cached_property
    def historicalUsage(self):  # pragma: no cover
        return HistoricalUsageEntityPaginator.make_one(
            self.boto3_raw_data["historicalUsage"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BillEstimateInputUsageModificationSummaryPaginatorTypeDef"
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
                "type_defs.BillEstimateInputUsageModificationSummaryPaginatorTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BillScenarioUsageModificationItemPaginator:
    boto3_raw_data: "type_defs.BillScenarioUsageModificationItemPaginatorTypeDef" = (
        dataclasses.field()
    )

    serviceCode = field("serviceCode")
    usageType = field("usageType")
    operation = field("operation")
    location = field("location")
    availabilityZone = field("availabilityZone")
    id = field("id")
    group = field("group")
    usageAccountId = field("usageAccountId")

    @cached_property
    def quantities(self):  # pragma: no cover
        return UsageQuantity.make_many(self.boto3_raw_data["quantities"])

    @cached_property
    def historicalUsage(self):  # pragma: no cover
        return HistoricalUsageEntityPaginator.make_one(
            self.boto3_raw_data["historicalUsage"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BillScenarioUsageModificationItemPaginatorTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BillScenarioUsageModificationItemPaginatorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkloadEstimateUsageItemPaginator:
    boto3_raw_data: "type_defs.WorkloadEstimateUsageItemPaginatorTypeDef" = (
        dataclasses.field()
    )

    serviceCode = field("serviceCode")
    usageType = field("usageType")
    operation = field("operation")
    location = field("location")
    id = field("id")
    usageAccountId = field("usageAccountId")
    group = field("group")

    @cached_property
    def quantity(self):  # pragma: no cover
        return WorkloadEstimateUsageQuantity.make_one(self.boto3_raw_data["quantity"])

    cost = field("cost")
    currency = field("currency")
    status = field("status")

    @cached_property
    def historicalUsage(self):  # pragma: no cover
        return HistoricalUsageEntityPaginator.make_one(
            self.boto3_raw_data["historicalUsage"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.WorkloadEstimateUsageItemPaginatorTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WorkloadEstimateUsageItemPaginatorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchCreateBillScenarioUsageModificationResponse:
    boto3_raw_data: (
        "type_defs.BatchCreateBillScenarioUsageModificationResponseTypeDef"
    ) = dataclasses.field()

    @cached_property
    def items(self):  # pragma: no cover
        return BatchCreateBillScenarioUsageModificationItem.make_many(
            self.boto3_raw_data["items"]
        )

    @cached_property
    def errors(self):  # pragma: no cover
        return BatchCreateBillScenarioUsageModificationError.make_many(
            self.boto3_raw_data["errors"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchCreateBillScenarioUsageModificationResponseTypeDef"
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
                "type_defs.BatchCreateBillScenarioUsageModificationResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchCreateWorkloadEstimateUsageResponse:
    boto3_raw_data: "type_defs.BatchCreateWorkloadEstimateUsageResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def items(self):  # pragma: no cover
        return BatchCreateWorkloadEstimateUsageItem.make_many(
            self.boto3_raw_data["items"]
        )

    @cached_property
    def errors(self):  # pragma: no cover
        return BatchCreateWorkloadEstimateUsageError.make_many(
            self.boto3_raw_data["errors"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchCreateWorkloadEstimateUsageResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchCreateWorkloadEstimateUsageResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBillEstimateInputUsageModificationsResponse:
    boto3_raw_data: (
        "type_defs.ListBillEstimateInputUsageModificationsResponseTypeDef"
    ) = dataclasses.field()

    @cached_property
    def items(self):  # pragma: no cover
        return BillEstimateInputUsageModificationSummary.make_many(
            self.boto3_raw_data["items"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListBillEstimateInputUsageModificationsResponseTypeDef"
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
                "type_defs.ListBillEstimateInputUsageModificationsResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchUpdateBillScenarioUsageModificationResponse:
    boto3_raw_data: (
        "type_defs.BatchUpdateBillScenarioUsageModificationResponseTypeDef"
    ) = dataclasses.field()

    @cached_property
    def items(self):  # pragma: no cover
        return BillScenarioUsageModificationItem.make_many(self.boto3_raw_data["items"])

    @cached_property
    def errors(self):  # pragma: no cover
        return BatchUpdateBillScenarioUsageModificationError.make_many(
            self.boto3_raw_data["errors"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchUpdateBillScenarioUsageModificationResponseTypeDef"
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
                "type_defs.BatchUpdateBillScenarioUsageModificationResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBillScenarioUsageModificationsResponse:
    boto3_raw_data: "type_defs.ListBillScenarioUsageModificationsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def items(self):  # pragma: no cover
        return BillScenarioUsageModificationItem.make_many(self.boto3_raw_data["items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListBillScenarioUsageModificationsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBillScenarioUsageModificationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchUpdateWorkloadEstimateUsageResponse:
    boto3_raw_data: "type_defs.BatchUpdateWorkloadEstimateUsageResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def items(self):  # pragma: no cover
        return WorkloadEstimateUsageItem.make_many(self.boto3_raw_data["items"])

    @cached_property
    def errors(self):  # pragma: no cover
        return BatchUpdateWorkloadEstimateUsageError.make_many(
            self.boto3_raw_data["errors"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchUpdateWorkloadEstimateUsageResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchUpdateWorkloadEstimateUsageResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWorkloadEstimateUsageResponse:
    boto3_raw_data: "type_defs.ListWorkloadEstimateUsageResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def items(self):  # pragma: no cover
        return WorkloadEstimateUsageItem.make_many(self.boto3_raw_data["items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListWorkloadEstimateUsageResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWorkloadEstimateUsageResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBillEstimateInputUsageModificationsResponsePaginator:
    boto3_raw_data: (
        "type_defs.ListBillEstimateInputUsageModificationsResponsePaginatorTypeDef"
    ) = dataclasses.field()

    @cached_property
    def items(self):  # pragma: no cover
        return BillEstimateInputUsageModificationSummaryPaginator.make_many(
            self.boto3_raw_data["items"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListBillEstimateInputUsageModificationsResponsePaginatorTypeDef"
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
                "type_defs.ListBillEstimateInputUsageModificationsResponsePaginatorTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBillScenarioUsageModificationsResponsePaginator:
    boto3_raw_data: (
        "type_defs.ListBillScenarioUsageModificationsResponsePaginatorTypeDef"
    ) = dataclasses.field()

    @cached_property
    def items(self):  # pragma: no cover
        return BillScenarioUsageModificationItemPaginator.make_many(
            self.boto3_raw_data["items"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListBillScenarioUsageModificationsResponsePaginatorTypeDef"
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
                "type_defs.ListBillScenarioUsageModificationsResponsePaginatorTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWorkloadEstimateUsageResponsePaginator:
    boto3_raw_data: "type_defs.ListWorkloadEstimateUsageResponsePaginatorTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def items(self):  # pragma: no cover
        return WorkloadEstimateUsageItemPaginator.make_many(
            self.boto3_raw_data["items"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListWorkloadEstimateUsageResponsePaginatorTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWorkloadEstimateUsageResponsePaginatorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HistoricalUsageEntity:
    boto3_raw_data: "type_defs.HistoricalUsageEntityTypeDef" = dataclasses.field()

    serviceCode = field("serviceCode")
    usageType = field("usageType")
    operation = field("operation")
    usageAccountId = field("usageAccountId")
    billInterval = field("billInterval")
    filterExpression = field("filterExpression")
    location = field("location")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.HistoricalUsageEntityTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HistoricalUsageEntityTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchCreateBillScenarioUsageModificationEntry:
    boto3_raw_data: "type_defs.BatchCreateBillScenarioUsageModificationEntryTypeDef" = (
        dataclasses.field()
    )

    serviceCode = field("serviceCode")
    usageType = field("usageType")
    operation = field("operation")
    key = field("key")
    usageAccountId = field("usageAccountId")
    availabilityZone = field("availabilityZone")
    group = field("group")

    @cached_property
    def amounts(self):  # pragma: no cover
        return UsageAmount.make_many(self.boto3_raw_data["amounts"])

    historicalUsage = field("historicalUsage")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchCreateBillScenarioUsageModificationEntryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchCreateBillScenarioUsageModificationEntryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchCreateWorkloadEstimateUsageEntry:
    boto3_raw_data: "type_defs.BatchCreateWorkloadEstimateUsageEntryTypeDef" = (
        dataclasses.field()
    )

    serviceCode = field("serviceCode")
    usageType = field("usageType")
    operation = field("operation")
    key = field("key")
    usageAccountId = field("usageAccountId")
    amount = field("amount")
    group = field("group")
    historicalUsage = field("historicalUsage")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchCreateWorkloadEstimateUsageEntryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchCreateWorkloadEstimateUsageEntryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchCreateBillScenarioUsageModificationRequest:
    boto3_raw_data: (
        "type_defs.BatchCreateBillScenarioUsageModificationRequestTypeDef"
    ) = dataclasses.field()

    billScenarioId = field("billScenarioId")

    @cached_property
    def usageModifications(self):  # pragma: no cover
        return BatchCreateBillScenarioUsageModificationEntry.make_many(
            self.boto3_raw_data["usageModifications"]
        )

    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchCreateBillScenarioUsageModificationRequestTypeDef"
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
                "type_defs.BatchCreateBillScenarioUsageModificationRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchCreateWorkloadEstimateUsageRequest:
    boto3_raw_data: "type_defs.BatchCreateWorkloadEstimateUsageRequestTypeDef" = (
        dataclasses.field()
    )

    workloadEstimateId = field("workloadEstimateId")

    @cached_property
    def usage(self):  # pragma: no cover
        return BatchCreateWorkloadEstimateUsageEntry.make_many(
            self.boto3_raw_data["usage"]
        )

    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchCreateWorkloadEstimateUsageRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchCreateWorkloadEstimateUsageRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
