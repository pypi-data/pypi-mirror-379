# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_eks_auth import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AssumeRoleForPodIdentityRequest:
    boto3_raw_data: "type_defs.AssumeRoleForPodIdentityRequestTypeDef" = (
        dataclasses.field()
    )

    clusterName = field("clusterName")
    token = field("token")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AssumeRoleForPodIdentityRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssumeRoleForPodIdentityRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssumedRoleUser:
    boto3_raw_data: "type_defs.AssumedRoleUserTypeDef" = dataclasses.field()

    arn = field("arn")
    assumeRoleId = field("assumeRoleId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AssumedRoleUserTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AssumedRoleUserTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Credentials:
    boto3_raw_data: "type_defs.CredentialsTypeDef" = dataclasses.field()

    sessionToken = field("sessionToken")
    secretAccessKey = field("secretAccessKey")
    accessKeyId = field("accessKeyId")
    expiration = field("expiration")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CredentialsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CredentialsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PodIdentityAssociation:
    boto3_raw_data: "type_defs.PodIdentityAssociationTypeDef" = dataclasses.field()

    associationArn = field("associationArn")
    associationId = field("associationId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PodIdentityAssociationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PodIdentityAssociationTypeDef"]
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
class Subject:
    boto3_raw_data: "type_defs.SubjectTypeDef" = dataclasses.field()

    namespace = field("namespace")
    serviceAccount = field("serviceAccount")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SubjectTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SubjectTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssumeRoleForPodIdentityResponse:
    boto3_raw_data: "type_defs.AssumeRoleForPodIdentityResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def subject(self):  # pragma: no cover
        return Subject.make_one(self.boto3_raw_data["subject"])

    audience = field("audience")

    @cached_property
    def podIdentityAssociation(self):  # pragma: no cover
        return PodIdentityAssociation.make_one(
            self.boto3_raw_data["podIdentityAssociation"]
        )

    @cached_property
    def assumedRoleUser(self):  # pragma: no cover
        return AssumedRoleUser.make_one(self.boto3_raw_data["assumedRoleUser"])

    @cached_property
    def credentials(self):  # pragma: no cover
        return Credentials.make_one(self.boto3_raw_data["credentials"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AssumeRoleForPodIdentityResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssumeRoleForPodIdentityResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
