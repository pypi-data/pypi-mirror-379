# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_amplifybackend import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class BackendAPIAppSyncAuthSettings:
    boto3_raw_data: "type_defs.BackendAPIAppSyncAuthSettingsTypeDef" = (
        dataclasses.field()
    )

    CognitoUserPoolId = field("CognitoUserPoolId")
    Description = field("Description")
    ExpirationTime = field("ExpirationTime")
    OpenIDAuthTTL = field("OpenIDAuthTTL")
    OpenIDClientId = field("OpenIDClientId")
    OpenIDIatTTL = field("OpenIDIatTTL")
    OpenIDIssueURL = field("OpenIDIssueURL")
    OpenIDProviderName = field("OpenIDProviderName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BackendAPIAppSyncAuthSettingsTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BackendAPIAppSyncAuthSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BackendAPIConflictResolution:
    boto3_raw_data: "type_defs.BackendAPIConflictResolutionTypeDef" = (
        dataclasses.field()
    )

    ResolutionStrategy = field("ResolutionStrategy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BackendAPIConflictResolutionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BackendAPIConflictResolutionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BackendAuthAppleProviderConfig:
    boto3_raw_data: "type_defs.BackendAuthAppleProviderConfigTypeDef" = (
        dataclasses.field()
    )

    ClientId = field("ClientId")
    KeyId = field("KeyId")
    PrivateKey = field("PrivateKey")
    TeamId = field("TeamId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BackendAuthAppleProviderConfigTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BackendAuthAppleProviderConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BackendAuthSocialProviderConfig:
    boto3_raw_data: "type_defs.BackendAuthSocialProviderConfigTypeDef" = (
        dataclasses.field()
    )

    ClientId = field("ClientId")
    ClientSecret = field("ClientSecret")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BackendAuthSocialProviderConfigTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BackendAuthSocialProviderConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BackendJobRespObj:
    boto3_raw_data: "type_defs.BackendJobRespObjTypeDef" = dataclasses.field()

    AppId = field("AppId")
    BackendEnvironmentName = field("BackendEnvironmentName")
    CreateTime = field("CreateTime")
    Error = field("Error")
    JobId = field("JobId")
    Operation = field("Operation")
    Status = field("Status")
    UpdateTime = field("UpdateTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BackendJobRespObjTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BackendJobRespObjTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BackendStoragePermissionsOutput:
    boto3_raw_data: "type_defs.BackendStoragePermissionsOutputTypeDef" = (
        dataclasses.field()
    )

    Authenticated = field("Authenticated")
    UnAuthenticated = field("UnAuthenticated")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BackendStoragePermissionsOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BackendStoragePermissionsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BackendStoragePermissions:
    boto3_raw_data: "type_defs.BackendStoragePermissionsTypeDef" = dataclasses.field()

    Authenticated = field("Authenticated")
    UnAuthenticated = field("UnAuthenticated")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BackendStoragePermissionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BackendStoragePermissionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CloneBackendRequest:
    boto3_raw_data: "type_defs.CloneBackendRequestTypeDef" = dataclasses.field()

    AppId = field("AppId")
    BackendEnvironmentName = field("BackendEnvironmentName")
    TargetEnvironmentName = field("TargetEnvironmentName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CloneBackendRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CloneBackendRequestTypeDef"]
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
class EmailSettings:
    boto3_raw_data: "type_defs.EmailSettingsTypeDef" = dataclasses.field()

    EmailMessage = field("EmailMessage")
    EmailSubject = field("EmailSubject")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EmailSettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EmailSettingsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SmsSettings:
    boto3_raw_data: "type_defs.SmsSettingsTypeDef" = dataclasses.field()

    SmsMessage = field("SmsMessage")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SmsSettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SmsSettingsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateBackendAuthIdentityPoolConfig:
    boto3_raw_data: "type_defs.CreateBackendAuthIdentityPoolConfigTypeDef" = (
        dataclasses.field()
    )

    IdentityPoolName = field("IdentityPoolName")
    UnauthenticatedLogin = field("UnauthenticatedLogin")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateBackendAuthIdentityPoolConfigTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateBackendAuthIdentityPoolConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SettingsOutput:
    boto3_raw_data: "type_defs.SettingsOutputTypeDef" = dataclasses.field()

    MfaTypes = field("MfaTypes")
    SmsMessage = field("SmsMessage")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SettingsOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SettingsOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Settings:
    boto3_raw_data: "type_defs.SettingsTypeDef" = dataclasses.field()

    MfaTypes = field("MfaTypes")
    SmsMessage = field("SmsMessage")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SettingsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateBackendAuthPasswordPolicyConfigOutput:
    boto3_raw_data: "type_defs.CreateBackendAuthPasswordPolicyConfigOutputTypeDef" = (
        dataclasses.field()
    )

    MinimumLength = field("MinimumLength")
    AdditionalConstraints = field("AdditionalConstraints")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateBackendAuthPasswordPolicyConfigOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateBackendAuthPasswordPolicyConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateBackendAuthPasswordPolicyConfig:
    boto3_raw_data: "type_defs.CreateBackendAuthPasswordPolicyConfigTypeDef" = (
        dataclasses.field()
    )

    MinimumLength = field("MinimumLength")
    AdditionalConstraints = field("AdditionalConstraints")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateBackendAuthPasswordPolicyConfigTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateBackendAuthPasswordPolicyConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateBackendConfigRequest:
    boto3_raw_data: "type_defs.CreateBackendConfigRequestTypeDef" = dataclasses.field()

    AppId = field("AppId")
    BackendManagerAppId = field("BackendManagerAppId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateBackendConfigRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateBackendConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateBackendRequest:
    boto3_raw_data: "type_defs.CreateBackendRequestTypeDef" = dataclasses.field()

    AppId = field("AppId")
    AppName = field("AppName")
    BackendEnvironmentName = field("BackendEnvironmentName")
    ResourceConfig = field("ResourceConfig")
    ResourceName = field("ResourceName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateBackendRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateBackendRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateTokenRequest:
    boto3_raw_data: "type_defs.CreateTokenRequestTypeDef" = dataclasses.field()

    AppId = field("AppId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateTokenRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTokenRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteBackendAuthRequest:
    boto3_raw_data: "type_defs.DeleteBackendAuthRequestTypeDef" = dataclasses.field()

    AppId = field("AppId")
    BackendEnvironmentName = field("BackendEnvironmentName")
    ResourceName = field("ResourceName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteBackendAuthRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteBackendAuthRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteBackendRequest:
    boto3_raw_data: "type_defs.DeleteBackendRequestTypeDef" = dataclasses.field()

    AppId = field("AppId")
    BackendEnvironmentName = field("BackendEnvironmentName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteBackendRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteBackendRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteBackendStorageRequest:
    boto3_raw_data: "type_defs.DeleteBackendStorageRequestTypeDef" = dataclasses.field()

    AppId = field("AppId")
    BackendEnvironmentName = field("BackendEnvironmentName")
    ResourceName = field("ResourceName")
    ServiceName = field("ServiceName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteBackendStorageRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteBackendStorageRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteTokenRequest:
    boto3_raw_data: "type_defs.DeleteTokenRequestTypeDef" = dataclasses.field()

    AppId = field("AppId")
    SessionId = field("SessionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteTokenRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteTokenRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GenerateBackendAPIModelsRequest:
    boto3_raw_data: "type_defs.GenerateBackendAPIModelsRequestTypeDef" = (
        dataclasses.field()
    )

    AppId = field("AppId")
    BackendEnvironmentName = field("BackendEnvironmentName")
    ResourceName = field("ResourceName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GenerateBackendAPIModelsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GenerateBackendAPIModelsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBackendAPIModelsRequest:
    boto3_raw_data: "type_defs.GetBackendAPIModelsRequestTypeDef" = dataclasses.field()

    AppId = field("AppId")
    BackendEnvironmentName = field("BackendEnvironmentName")
    ResourceName = field("ResourceName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetBackendAPIModelsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBackendAPIModelsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBackendAuthRequest:
    boto3_raw_data: "type_defs.GetBackendAuthRequestTypeDef" = dataclasses.field()

    AppId = field("AppId")
    BackendEnvironmentName = field("BackendEnvironmentName")
    ResourceName = field("ResourceName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetBackendAuthRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBackendAuthRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBackendJobRequest:
    boto3_raw_data: "type_defs.GetBackendJobRequestTypeDef" = dataclasses.field()

    AppId = field("AppId")
    BackendEnvironmentName = field("BackendEnvironmentName")
    JobId = field("JobId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetBackendJobRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBackendJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBackendRequest:
    boto3_raw_data: "type_defs.GetBackendRequestTypeDef" = dataclasses.field()

    AppId = field("AppId")
    BackendEnvironmentName = field("BackendEnvironmentName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetBackendRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBackendRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBackendStorageRequest:
    boto3_raw_data: "type_defs.GetBackendStorageRequestTypeDef" = dataclasses.field()

    AppId = field("AppId")
    BackendEnvironmentName = field("BackendEnvironmentName")
    ResourceName = field("ResourceName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetBackendStorageRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBackendStorageRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTokenRequest:
    boto3_raw_data: "type_defs.GetTokenRequestTypeDef" = dataclasses.field()

    AppId = field("AppId")
    SessionId = field("SessionId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetTokenRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetTokenRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportBackendAuthRequest:
    boto3_raw_data: "type_defs.ImportBackendAuthRequestTypeDef" = dataclasses.field()

    AppId = field("AppId")
    BackendEnvironmentName = field("BackendEnvironmentName")
    NativeClientId = field("NativeClientId")
    UserPoolId = field("UserPoolId")
    WebClientId = field("WebClientId")
    IdentityPoolId = field("IdentityPoolId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImportBackendAuthRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImportBackendAuthRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportBackendStorageRequest:
    boto3_raw_data: "type_defs.ImportBackendStorageRequestTypeDef" = dataclasses.field()

    AppId = field("AppId")
    BackendEnvironmentName = field("BackendEnvironmentName")
    ServiceName = field("ServiceName")
    BucketName = field("BucketName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImportBackendStorageRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImportBackendStorageRequestTypeDef"]
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
class ListBackendJobsRequest:
    boto3_raw_data: "type_defs.ListBackendJobsRequestTypeDef" = dataclasses.field()

    AppId = field("AppId")
    BackendEnvironmentName = field("BackendEnvironmentName")
    JobId = field("JobId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")
    Operation = field("Operation")
    Status = field("Status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListBackendJobsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBackendJobsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListS3BucketsRequest:
    boto3_raw_data: "type_defs.ListS3BucketsRequestTypeDef" = dataclasses.field()

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListS3BucketsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListS3BucketsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3BucketInfo:
    boto3_raw_data: "type_defs.S3BucketInfoTypeDef" = dataclasses.field()

    CreationDate = field("CreationDate")
    Name = field("Name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.S3BucketInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.S3BucketInfoTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LoginAuthConfigReqObj:
    boto3_raw_data: "type_defs.LoginAuthConfigReqObjTypeDef" = dataclasses.field()

    AwsCognitoIdentityPoolId = field("AwsCognitoIdentityPoolId")
    AwsCognitoRegion = field("AwsCognitoRegion")
    AwsUserPoolsId = field("AwsUserPoolsId")
    AwsUserPoolsWebClientId = field("AwsUserPoolsWebClientId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LoginAuthConfigReqObjTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LoginAuthConfigReqObjTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemoveAllBackendsRequest:
    boto3_raw_data: "type_defs.RemoveAllBackendsRequestTypeDef" = dataclasses.field()

    AppId = field("AppId")
    CleanAmplifyApp = field("CleanAmplifyApp")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RemoveAllBackendsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemoveAllBackendsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemoveBackendConfigRequest:
    boto3_raw_data: "type_defs.RemoveBackendConfigRequestTypeDef" = dataclasses.field()

    AppId = field("AppId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RemoveBackendConfigRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemoveBackendConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateBackendAuthIdentityPoolConfig:
    boto3_raw_data: "type_defs.UpdateBackendAuthIdentityPoolConfigTypeDef" = (
        dataclasses.field()
    )

    UnauthenticatedLogin = field("UnauthenticatedLogin")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateBackendAuthIdentityPoolConfigTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateBackendAuthIdentityPoolConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateBackendAuthPasswordPolicyConfig:
    boto3_raw_data: "type_defs.UpdateBackendAuthPasswordPolicyConfigTypeDef" = (
        dataclasses.field()
    )

    AdditionalConstraints = field("AdditionalConstraints")
    MinimumLength = field("MinimumLength")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateBackendAuthPasswordPolicyConfigTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateBackendAuthPasswordPolicyConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateBackendJobRequest:
    boto3_raw_data: "type_defs.UpdateBackendJobRequestTypeDef" = dataclasses.field()

    AppId = field("AppId")
    BackendEnvironmentName = field("BackendEnvironmentName")
    JobId = field("JobId")
    Operation = field("Operation")
    Status = field("Status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateBackendJobRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateBackendJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BackendAPIAuthType:
    boto3_raw_data: "type_defs.BackendAPIAuthTypeTypeDef" = dataclasses.field()

    Mode = field("Mode")

    @cached_property
    def Settings(self):  # pragma: no cover
        return BackendAPIAppSyncAuthSettings.make_one(self.boto3_raw_data["Settings"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BackendAPIAuthTypeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BackendAPIAuthTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SocialProviderSettings:
    boto3_raw_data: "type_defs.SocialProviderSettingsTypeDef" = dataclasses.field()

    @cached_property
    def Facebook(self):  # pragma: no cover
        return BackendAuthSocialProviderConfig.make_one(self.boto3_raw_data["Facebook"])

    @cached_property
    def Google(self):  # pragma: no cover
        return BackendAuthSocialProviderConfig.make_one(self.boto3_raw_data["Google"])

    @cached_property
    def LoginWithAmazon(self):  # pragma: no cover
        return BackendAuthSocialProviderConfig.make_one(
            self.boto3_raw_data["LoginWithAmazon"]
        )

    @cached_property
    def SignInWithApple(self):  # pragma: no cover
        return BackendAuthAppleProviderConfig.make_one(
            self.boto3_raw_data["SignInWithApple"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SocialProviderSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SocialProviderSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBackendStorageResourceConfig:
    boto3_raw_data: "type_defs.GetBackendStorageResourceConfigTypeDef" = (
        dataclasses.field()
    )

    Imported = field("Imported")
    ServiceName = field("ServiceName")
    BucketName = field("BucketName")

    @cached_property
    def Permissions(self):  # pragma: no cover
        return BackendStoragePermissionsOutput.make_one(
            self.boto3_raw_data["Permissions"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetBackendStorageResourceConfigTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBackendStorageResourceConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CloneBackendResponse:
    boto3_raw_data: "type_defs.CloneBackendResponseTypeDef" = dataclasses.field()

    AppId = field("AppId")
    BackendEnvironmentName = field("BackendEnvironmentName")
    Error = field("Error")
    JobId = field("JobId")
    Operation = field("Operation")
    Status = field("Status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CloneBackendResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CloneBackendResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateBackendAPIResponse:
    boto3_raw_data: "type_defs.CreateBackendAPIResponseTypeDef" = dataclasses.field()

    AppId = field("AppId")
    BackendEnvironmentName = field("BackendEnvironmentName")
    Error = field("Error")
    JobId = field("JobId")
    Operation = field("Operation")
    Status = field("Status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateBackendAPIResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateBackendAPIResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateBackendAuthResponse:
    boto3_raw_data: "type_defs.CreateBackendAuthResponseTypeDef" = dataclasses.field()

    AppId = field("AppId")
    BackendEnvironmentName = field("BackendEnvironmentName")
    Error = field("Error")
    JobId = field("JobId")
    Operation = field("Operation")
    Status = field("Status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateBackendAuthResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateBackendAuthResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateBackendConfigResponse:
    boto3_raw_data: "type_defs.CreateBackendConfigResponseTypeDef" = dataclasses.field()

    AppId = field("AppId")
    BackendEnvironmentName = field("BackendEnvironmentName")
    JobId = field("JobId")
    Status = field("Status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateBackendConfigResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateBackendConfigResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateBackendResponse:
    boto3_raw_data: "type_defs.CreateBackendResponseTypeDef" = dataclasses.field()

    AppId = field("AppId")
    BackendEnvironmentName = field("BackendEnvironmentName")
    Error = field("Error")
    JobId = field("JobId")
    Operation = field("Operation")
    Status = field("Status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateBackendResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateBackendResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateBackendStorageResponse:
    boto3_raw_data: "type_defs.CreateBackendStorageResponseTypeDef" = (
        dataclasses.field()
    )

    AppId = field("AppId")
    BackendEnvironmentName = field("BackendEnvironmentName")
    JobId = field("JobId")
    Status = field("Status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateBackendStorageResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateBackendStorageResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateTokenResponse:
    boto3_raw_data: "type_defs.CreateTokenResponseTypeDef" = dataclasses.field()

    AppId = field("AppId")
    ChallengeCode = field("ChallengeCode")
    SessionId = field("SessionId")
    Ttl = field("Ttl")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateTokenResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTokenResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteBackendAPIResponse:
    boto3_raw_data: "type_defs.DeleteBackendAPIResponseTypeDef" = dataclasses.field()

    AppId = field("AppId")
    BackendEnvironmentName = field("BackendEnvironmentName")
    Error = field("Error")
    JobId = field("JobId")
    Operation = field("Operation")
    Status = field("Status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteBackendAPIResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteBackendAPIResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteBackendAuthResponse:
    boto3_raw_data: "type_defs.DeleteBackendAuthResponseTypeDef" = dataclasses.field()

    AppId = field("AppId")
    BackendEnvironmentName = field("BackendEnvironmentName")
    Error = field("Error")
    JobId = field("JobId")
    Operation = field("Operation")
    Status = field("Status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteBackendAuthResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteBackendAuthResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteBackendResponse:
    boto3_raw_data: "type_defs.DeleteBackendResponseTypeDef" = dataclasses.field()

    AppId = field("AppId")
    BackendEnvironmentName = field("BackendEnvironmentName")
    Error = field("Error")
    JobId = field("JobId")
    Operation = field("Operation")
    Status = field("Status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteBackendResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteBackendResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteBackendStorageResponse:
    boto3_raw_data: "type_defs.DeleteBackendStorageResponseTypeDef" = (
        dataclasses.field()
    )

    AppId = field("AppId")
    BackendEnvironmentName = field("BackendEnvironmentName")
    JobId = field("JobId")
    Status = field("Status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteBackendStorageResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteBackendStorageResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteTokenResponse:
    boto3_raw_data: "type_defs.DeleteTokenResponseTypeDef" = dataclasses.field()

    IsSuccess = field("IsSuccess")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteTokenResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteTokenResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GenerateBackendAPIModelsResponse:
    boto3_raw_data: "type_defs.GenerateBackendAPIModelsResponseTypeDef" = (
        dataclasses.field()
    )

    AppId = field("AppId")
    BackendEnvironmentName = field("BackendEnvironmentName")
    Error = field("Error")
    JobId = field("JobId")
    Operation = field("Operation")
    Status = field("Status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GenerateBackendAPIModelsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GenerateBackendAPIModelsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBackendAPIModelsResponse:
    boto3_raw_data: "type_defs.GetBackendAPIModelsResponseTypeDef" = dataclasses.field()

    Models = field("Models")
    Status = field("Status")
    ModelIntrospectionSchema = field("ModelIntrospectionSchema")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetBackendAPIModelsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBackendAPIModelsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBackendJobResponse:
    boto3_raw_data: "type_defs.GetBackendJobResponseTypeDef" = dataclasses.field()

    AppId = field("AppId")
    BackendEnvironmentName = field("BackendEnvironmentName")
    CreateTime = field("CreateTime")
    Error = field("Error")
    JobId = field("JobId")
    Operation = field("Operation")
    Status = field("Status")
    UpdateTime = field("UpdateTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetBackendJobResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBackendJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBackendResponse:
    boto3_raw_data: "type_defs.GetBackendResponseTypeDef" = dataclasses.field()

    AmplifyFeatureFlags = field("AmplifyFeatureFlags")
    AmplifyMetaConfig = field("AmplifyMetaConfig")
    AppId = field("AppId")
    AppName = field("AppName")
    BackendEnvironmentList = field("BackendEnvironmentList")
    BackendEnvironmentName = field("BackendEnvironmentName")
    Error = field("Error")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetBackendResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBackendResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTokenResponse:
    boto3_raw_data: "type_defs.GetTokenResponseTypeDef" = dataclasses.field()

    AppId = field("AppId")
    ChallengeCode = field("ChallengeCode")
    SessionId = field("SessionId")
    Ttl = field("Ttl")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetTokenResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTokenResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportBackendAuthResponse:
    boto3_raw_data: "type_defs.ImportBackendAuthResponseTypeDef" = dataclasses.field()

    AppId = field("AppId")
    BackendEnvironmentName = field("BackendEnvironmentName")
    Error = field("Error")
    JobId = field("JobId")
    Operation = field("Operation")
    Status = field("Status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImportBackendAuthResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImportBackendAuthResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportBackendStorageResponse:
    boto3_raw_data: "type_defs.ImportBackendStorageResponseTypeDef" = (
        dataclasses.field()
    )

    AppId = field("AppId")
    BackendEnvironmentName = field("BackendEnvironmentName")
    JobId = field("JobId")
    Status = field("Status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImportBackendStorageResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImportBackendStorageResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBackendJobsResponse:
    boto3_raw_data: "type_defs.ListBackendJobsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Jobs(self):  # pragma: no cover
        return BackendJobRespObj.make_many(self.boto3_raw_data["Jobs"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListBackendJobsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBackendJobsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemoveAllBackendsResponse:
    boto3_raw_data: "type_defs.RemoveAllBackendsResponseTypeDef" = dataclasses.field()

    AppId = field("AppId")
    Error = field("Error")
    JobId = field("JobId")
    Operation = field("Operation")
    Status = field("Status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RemoveAllBackendsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemoveAllBackendsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemoveBackendConfigResponse:
    boto3_raw_data: "type_defs.RemoveBackendConfigResponseTypeDef" = dataclasses.field()

    Error = field("Error")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RemoveBackendConfigResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemoveBackendConfigResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateBackendAPIResponse:
    boto3_raw_data: "type_defs.UpdateBackendAPIResponseTypeDef" = dataclasses.field()

    AppId = field("AppId")
    BackendEnvironmentName = field("BackendEnvironmentName")
    Error = field("Error")
    JobId = field("JobId")
    Operation = field("Operation")
    Status = field("Status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateBackendAPIResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateBackendAPIResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateBackendAuthResponse:
    boto3_raw_data: "type_defs.UpdateBackendAuthResponseTypeDef" = dataclasses.field()

    AppId = field("AppId")
    BackendEnvironmentName = field("BackendEnvironmentName")
    Error = field("Error")
    JobId = field("JobId")
    Operation = field("Operation")
    Status = field("Status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateBackendAuthResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateBackendAuthResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateBackendJobResponse:
    boto3_raw_data: "type_defs.UpdateBackendJobResponseTypeDef" = dataclasses.field()

    AppId = field("AppId")
    BackendEnvironmentName = field("BackendEnvironmentName")
    CreateTime = field("CreateTime")
    Error = field("Error")
    JobId = field("JobId")
    Operation = field("Operation")
    Status = field("Status")
    UpdateTime = field("UpdateTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateBackendJobResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateBackendJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateBackendStorageResponse:
    boto3_raw_data: "type_defs.UpdateBackendStorageResponseTypeDef" = (
        dataclasses.field()
    )

    AppId = field("AppId")
    BackendEnvironmentName = field("BackendEnvironmentName")
    JobId = field("JobId")
    Status = field("Status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateBackendStorageResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateBackendStorageResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateBackendAuthForgotPasswordConfig:
    boto3_raw_data: "type_defs.CreateBackendAuthForgotPasswordConfigTypeDef" = (
        dataclasses.field()
    )

    DeliveryMethod = field("DeliveryMethod")

    @cached_property
    def EmailSettings(self):  # pragma: no cover
        return EmailSettings.make_one(self.boto3_raw_data["EmailSettings"])

    @cached_property
    def SmsSettings(self):  # pragma: no cover
        return SmsSettings.make_one(self.boto3_raw_data["SmsSettings"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateBackendAuthForgotPasswordConfigTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateBackendAuthForgotPasswordConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateBackendAuthVerificationMessageConfig:
    boto3_raw_data: "type_defs.CreateBackendAuthVerificationMessageConfigTypeDef" = (
        dataclasses.field()
    )

    DeliveryMethod = field("DeliveryMethod")

    @cached_property
    def EmailSettings(self):  # pragma: no cover
        return EmailSettings.make_one(self.boto3_raw_data["EmailSettings"])

    @cached_property
    def SmsSettings(self):  # pragma: no cover
        return SmsSettings.make_one(self.boto3_raw_data["SmsSettings"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateBackendAuthVerificationMessageConfigTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateBackendAuthVerificationMessageConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateBackendAuthForgotPasswordConfig:
    boto3_raw_data: "type_defs.UpdateBackendAuthForgotPasswordConfigTypeDef" = (
        dataclasses.field()
    )

    DeliveryMethod = field("DeliveryMethod")

    @cached_property
    def EmailSettings(self):  # pragma: no cover
        return EmailSettings.make_one(self.boto3_raw_data["EmailSettings"])

    @cached_property
    def SmsSettings(self):  # pragma: no cover
        return SmsSettings.make_one(self.boto3_raw_data["SmsSettings"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateBackendAuthForgotPasswordConfigTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateBackendAuthForgotPasswordConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateBackendAuthVerificationMessageConfig:
    boto3_raw_data: "type_defs.UpdateBackendAuthVerificationMessageConfigTypeDef" = (
        dataclasses.field()
    )

    DeliveryMethod = field("DeliveryMethod")

    @cached_property
    def EmailSettings(self):  # pragma: no cover
        return EmailSettings.make_one(self.boto3_raw_data["EmailSettings"])

    @cached_property
    def SmsSettings(self):  # pragma: no cover
        return SmsSettings.make_one(self.boto3_raw_data["SmsSettings"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateBackendAuthVerificationMessageConfigTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateBackendAuthVerificationMessageConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateBackendAuthMFAConfigOutput:
    boto3_raw_data: "type_defs.CreateBackendAuthMFAConfigOutputTypeDef" = (
        dataclasses.field()
    )

    MFAMode = field("MFAMode")

    @cached_property
    def Settings(self):  # pragma: no cover
        return SettingsOutput.make_one(self.boto3_raw_data["Settings"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateBackendAuthMFAConfigOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateBackendAuthMFAConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateBackendAuthMFAConfig:
    boto3_raw_data: "type_defs.CreateBackendAuthMFAConfigTypeDef" = dataclasses.field()

    MFAMode = field("MFAMode")

    @cached_property
    def Settings(self):  # pragma: no cover
        return Settings.make_one(self.boto3_raw_data["Settings"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateBackendAuthMFAConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateBackendAuthMFAConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListBackendJobsRequestPaginate:
    boto3_raw_data: "type_defs.ListBackendJobsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    AppId = field("AppId")
    BackendEnvironmentName = field("BackendEnvironmentName")
    JobId = field("JobId")
    Operation = field("Operation")
    Status = field("Status")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListBackendJobsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListBackendJobsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListS3BucketsResponse:
    boto3_raw_data: "type_defs.ListS3BucketsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Buckets(self):  # pragma: no cover
        return S3BucketInfo.make_many(self.boto3_raw_data["Buckets"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListS3BucketsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListS3BucketsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateBackendConfigRequest:
    boto3_raw_data: "type_defs.UpdateBackendConfigRequestTypeDef" = dataclasses.field()

    AppId = field("AppId")

    @cached_property
    def LoginAuthConfig(self):  # pragma: no cover
        return LoginAuthConfigReqObj.make_one(self.boto3_raw_data["LoginAuthConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateBackendConfigRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateBackendConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateBackendConfigResponse:
    boto3_raw_data: "type_defs.UpdateBackendConfigResponseTypeDef" = dataclasses.field()

    AppId = field("AppId")
    BackendManagerAppId = field("BackendManagerAppId")
    Error = field("Error")

    @cached_property
    def LoginAuthConfig(self):  # pragma: no cover
        return LoginAuthConfigReqObj.make_one(self.boto3_raw_data["LoginAuthConfig"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateBackendConfigResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateBackendConfigResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BackendAPIResourceConfigOutput:
    boto3_raw_data: "type_defs.BackendAPIResourceConfigOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AdditionalAuthTypes(self):  # pragma: no cover
        return BackendAPIAuthType.make_many(self.boto3_raw_data["AdditionalAuthTypes"])

    ApiName = field("ApiName")

    @cached_property
    def ConflictResolution(self):  # pragma: no cover
        return BackendAPIConflictResolution.make_one(
            self.boto3_raw_data["ConflictResolution"]
        )

    @cached_property
    def DefaultAuthType(self):  # pragma: no cover
        return BackendAPIAuthType.make_one(self.boto3_raw_data["DefaultAuthType"])

    Service = field("Service")
    TransformSchema = field("TransformSchema")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BackendAPIResourceConfigOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BackendAPIResourceConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BackendAPIResourceConfig:
    boto3_raw_data: "type_defs.BackendAPIResourceConfigTypeDef" = dataclasses.field()

    @cached_property
    def AdditionalAuthTypes(self):  # pragma: no cover
        return BackendAPIAuthType.make_many(self.boto3_raw_data["AdditionalAuthTypes"])

    ApiName = field("ApiName")

    @cached_property
    def ConflictResolution(self):  # pragma: no cover
        return BackendAPIConflictResolution.make_one(
            self.boto3_raw_data["ConflictResolution"]
        )

    @cached_property
    def DefaultAuthType(self):  # pragma: no cover
        return BackendAPIAuthType.make_one(self.boto3_raw_data["DefaultAuthType"])

    Service = field("Service")
    TransformSchema = field("TransformSchema")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BackendAPIResourceConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BackendAPIResourceConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateBackendAuthOAuthConfigOutput:
    boto3_raw_data: "type_defs.CreateBackendAuthOAuthConfigOutputTypeDef" = (
        dataclasses.field()
    )

    OAuthGrantType = field("OAuthGrantType")
    OAuthScopes = field("OAuthScopes")
    RedirectSignInURIs = field("RedirectSignInURIs")
    RedirectSignOutURIs = field("RedirectSignOutURIs")
    DomainPrefix = field("DomainPrefix")

    @cached_property
    def SocialProviderSettings(self):  # pragma: no cover
        return SocialProviderSettings.make_one(
            self.boto3_raw_data["SocialProviderSettings"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateBackendAuthOAuthConfigOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateBackendAuthOAuthConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateBackendAuthOAuthConfig:
    boto3_raw_data: "type_defs.CreateBackendAuthOAuthConfigTypeDef" = (
        dataclasses.field()
    )

    OAuthGrantType = field("OAuthGrantType")
    OAuthScopes = field("OAuthScopes")
    RedirectSignInURIs = field("RedirectSignInURIs")
    RedirectSignOutURIs = field("RedirectSignOutURIs")
    DomainPrefix = field("DomainPrefix")

    @cached_property
    def SocialProviderSettings(self):  # pragma: no cover
        return SocialProviderSettings.make_one(
            self.boto3_raw_data["SocialProviderSettings"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateBackendAuthOAuthConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateBackendAuthOAuthConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateBackendAuthOAuthConfig:
    boto3_raw_data: "type_defs.UpdateBackendAuthOAuthConfigTypeDef" = (
        dataclasses.field()
    )

    DomainPrefix = field("DomainPrefix")
    OAuthGrantType = field("OAuthGrantType")
    OAuthScopes = field("OAuthScopes")
    RedirectSignInURIs = field("RedirectSignInURIs")
    RedirectSignOutURIs = field("RedirectSignOutURIs")

    @cached_property
    def SocialProviderSettings(self):  # pragma: no cover
        return SocialProviderSettings.make_one(
            self.boto3_raw_data["SocialProviderSettings"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateBackendAuthOAuthConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateBackendAuthOAuthConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBackendStorageResponse:
    boto3_raw_data: "type_defs.GetBackendStorageResponseTypeDef" = dataclasses.field()

    AppId = field("AppId")
    BackendEnvironmentName = field("BackendEnvironmentName")

    @cached_property
    def ResourceConfig(self):  # pragma: no cover
        return GetBackendStorageResourceConfig.make_one(
            self.boto3_raw_data["ResourceConfig"]
        )

    ResourceName = field("ResourceName")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetBackendStorageResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBackendStorageResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateBackendStorageResourceConfig:
    boto3_raw_data: "type_defs.CreateBackendStorageResourceConfigTypeDef" = (
        dataclasses.field()
    )

    Permissions = field("Permissions")
    ServiceName = field("ServiceName")
    BucketName = field("BucketName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateBackendStorageResourceConfigTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateBackendStorageResourceConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateBackendStorageResourceConfig:
    boto3_raw_data: "type_defs.UpdateBackendStorageResourceConfigTypeDef" = (
        dataclasses.field()
    )

    Permissions = field("Permissions")
    ServiceName = field("ServiceName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateBackendStorageResourceConfigTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateBackendStorageResourceConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateBackendAuthMFAConfig:
    boto3_raw_data: "type_defs.UpdateBackendAuthMFAConfigTypeDef" = dataclasses.field()

    MFAMode = field("MFAMode")
    Settings = field("Settings")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateBackendAuthMFAConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateBackendAuthMFAConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBackendAPIResponse:
    boto3_raw_data: "type_defs.GetBackendAPIResponseTypeDef" = dataclasses.field()

    AppId = field("AppId")
    BackendEnvironmentName = field("BackendEnvironmentName")
    Error = field("Error")

    @cached_property
    def ResourceConfig(self):  # pragma: no cover
        return BackendAPIResourceConfigOutput.make_one(
            self.boto3_raw_data["ResourceConfig"]
        )

    ResourceName = field("ResourceName")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetBackendAPIResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBackendAPIResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateBackendAuthUserPoolConfigOutput:
    boto3_raw_data: "type_defs.CreateBackendAuthUserPoolConfigOutputTypeDef" = (
        dataclasses.field()
    )

    RequiredSignUpAttributes = field("RequiredSignUpAttributes")
    SignInMethod = field("SignInMethod")
    UserPoolName = field("UserPoolName")

    @cached_property
    def ForgotPassword(self):  # pragma: no cover
        return CreateBackendAuthForgotPasswordConfig.make_one(
            self.boto3_raw_data["ForgotPassword"]
        )

    @cached_property
    def Mfa(self):  # pragma: no cover
        return CreateBackendAuthMFAConfigOutput.make_one(self.boto3_raw_data["Mfa"])

    @cached_property
    def OAuth(self):  # pragma: no cover
        return CreateBackendAuthOAuthConfigOutput.make_one(self.boto3_raw_data["OAuth"])

    @cached_property
    def PasswordPolicy(self):  # pragma: no cover
        return CreateBackendAuthPasswordPolicyConfigOutput.make_one(
            self.boto3_raw_data["PasswordPolicy"]
        )

    @cached_property
    def VerificationMessage(self):  # pragma: no cover
        return CreateBackendAuthVerificationMessageConfig.make_one(
            self.boto3_raw_data["VerificationMessage"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateBackendAuthUserPoolConfigOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateBackendAuthUserPoolConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateBackendAuthUserPoolConfig:
    boto3_raw_data: "type_defs.CreateBackendAuthUserPoolConfigTypeDef" = (
        dataclasses.field()
    )

    RequiredSignUpAttributes = field("RequiredSignUpAttributes")
    SignInMethod = field("SignInMethod")
    UserPoolName = field("UserPoolName")

    @cached_property
    def ForgotPassword(self):  # pragma: no cover
        return CreateBackendAuthForgotPasswordConfig.make_one(
            self.boto3_raw_data["ForgotPassword"]
        )

    @cached_property
    def Mfa(self):  # pragma: no cover
        return CreateBackendAuthMFAConfig.make_one(self.boto3_raw_data["Mfa"])

    @cached_property
    def OAuth(self):  # pragma: no cover
        return CreateBackendAuthOAuthConfig.make_one(self.boto3_raw_data["OAuth"])

    @cached_property
    def PasswordPolicy(self):  # pragma: no cover
        return CreateBackendAuthPasswordPolicyConfig.make_one(
            self.boto3_raw_data["PasswordPolicy"]
        )

    @cached_property
    def VerificationMessage(self):  # pragma: no cover
        return CreateBackendAuthVerificationMessageConfig.make_one(
            self.boto3_raw_data["VerificationMessage"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateBackendAuthUserPoolConfigTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateBackendAuthUserPoolConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateBackendStorageRequest:
    boto3_raw_data: "type_defs.CreateBackendStorageRequestTypeDef" = dataclasses.field()

    AppId = field("AppId")
    BackendEnvironmentName = field("BackendEnvironmentName")

    @cached_property
    def ResourceConfig(self):  # pragma: no cover
        return CreateBackendStorageResourceConfig.make_one(
            self.boto3_raw_data["ResourceConfig"]
        )

    ResourceName = field("ResourceName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateBackendStorageRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateBackendStorageRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateBackendStorageRequest:
    boto3_raw_data: "type_defs.UpdateBackendStorageRequestTypeDef" = dataclasses.field()

    AppId = field("AppId")
    BackendEnvironmentName = field("BackendEnvironmentName")

    @cached_property
    def ResourceConfig(self):  # pragma: no cover
        return UpdateBackendStorageResourceConfig.make_one(
            self.boto3_raw_data["ResourceConfig"]
        )

    ResourceName = field("ResourceName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateBackendStorageRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateBackendStorageRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateBackendAuthUserPoolConfig:
    boto3_raw_data: "type_defs.UpdateBackendAuthUserPoolConfigTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ForgotPassword(self):  # pragma: no cover
        return UpdateBackendAuthForgotPasswordConfig.make_one(
            self.boto3_raw_data["ForgotPassword"]
        )

    @cached_property
    def Mfa(self):  # pragma: no cover
        return UpdateBackendAuthMFAConfig.make_one(self.boto3_raw_data["Mfa"])

    @cached_property
    def OAuth(self):  # pragma: no cover
        return UpdateBackendAuthOAuthConfig.make_one(self.boto3_raw_data["OAuth"])

    @cached_property
    def PasswordPolicy(self):  # pragma: no cover
        return UpdateBackendAuthPasswordPolicyConfig.make_one(
            self.boto3_raw_data["PasswordPolicy"]
        )

    @cached_property
    def VerificationMessage(self):  # pragma: no cover
        return UpdateBackendAuthVerificationMessageConfig.make_one(
            self.boto3_raw_data["VerificationMessage"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateBackendAuthUserPoolConfigTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateBackendAuthUserPoolConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateBackendAPIRequest:
    boto3_raw_data: "type_defs.CreateBackendAPIRequestTypeDef" = dataclasses.field()

    AppId = field("AppId")
    BackendEnvironmentName = field("BackendEnvironmentName")
    ResourceConfig = field("ResourceConfig")
    ResourceName = field("ResourceName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateBackendAPIRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateBackendAPIRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteBackendAPIRequest:
    boto3_raw_data: "type_defs.DeleteBackendAPIRequestTypeDef" = dataclasses.field()

    AppId = field("AppId")
    BackendEnvironmentName = field("BackendEnvironmentName")
    ResourceName = field("ResourceName")
    ResourceConfig = field("ResourceConfig")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteBackendAPIRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteBackendAPIRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBackendAPIRequest:
    boto3_raw_data: "type_defs.GetBackendAPIRequestTypeDef" = dataclasses.field()

    AppId = field("AppId")
    BackendEnvironmentName = field("BackendEnvironmentName")
    ResourceName = field("ResourceName")
    ResourceConfig = field("ResourceConfig")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetBackendAPIRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBackendAPIRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateBackendAPIRequest:
    boto3_raw_data: "type_defs.UpdateBackendAPIRequestTypeDef" = dataclasses.field()

    AppId = field("AppId")
    BackendEnvironmentName = field("BackendEnvironmentName")
    ResourceName = field("ResourceName")
    ResourceConfig = field("ResourceConfig")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateBackendAPIRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateBackendAPIRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateBackendAuthResourceConfigOutput:
    boto3_raw_data: "type_defs.CreateBackendAuthResourceConfigOutputTypeDef" = (
        dataclasses.field()
    )

    AuthResources = field("AuthResources")
    Service = field("Service")

    @cached_property
    def UserPoolConfigs(self):  # pragma: no cover
        return CreateBackendAuthUserPoolConfigOutput.make_one(
            self.boto3_raw_data["UserPoolConfigs"]
        )

    @cached_property
    def IdentityPoolConfigs(self):  # pragma: no cover
        return CreateBackendAuthIdentityPoolConfig.make_one(
            self.boto3_raw_data["IdentityPoolConfigs"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateBackendAuthResourceConfigOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateBackendAuthResourceConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateBackendAuthResourceConfig:
    boto3_raw_data: "type_defs.CreateBackendAuthResourceConfigTypeDef" = (
        dataclasses.field()
    )

    AuthResources = field("AuthResources")
    Service = field("Service")

    @cached_property
    def UserPoolConfigs(self):  # pragma: no cover
        return CreateBackendAuthUserPoolConfig.make_one(
            self.boto3_raw_data["UserPoolConfigs"]
        )

    @cached_property
    def IdentityPoolConfigs(self):  # pragma: no cover
        return CreateBackendAuthIdentityPoolConfig.make_one(
            self.boto3_raw_data["IdentityPoolConfigs"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateBackendAuthResourceConfigTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateBackendAuthResourceConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateBackendAuthResourceConfig:
    boto3_raw_data: "type_defs.UpdateBackendAuthResourceConfigTypeDef" = (
        dataclasses.field()
    )

    AuthResources = field("AuthResources")
    Service = field("Service")

    @cached_property
    def UserPoolConfigs(self):  # pragma: no cover
        return UpdateBackendAuthUserPoolConfig.make_one(
            self.boto3_raw_data["UserPoolConfigs"]
        )

    @cached_property
    def IdentityPoolConfigs(self):  # pragma: no cover
        return UpdateBackendAuthIdentityPoolConfig.make_one(
            self.boto3_raw_data["IdentityPoolConfigs"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateBackendAuthResourceConfigTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateBackendAuthResourceConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetBackendAuthResponse:
    boto3_raw_data: "type_defs.GetBackendAuthResponseTypeDef" = dataclasses.field()

    AppId = field("AppId")
    BackendEnvironmentName = field("BackendEnvironmentName")
    Error = field("Error")

    @cached_property
    def ResourceConfig(self):  # pragma: no cover
        return CreateBackendAuthResourceConfigOutput.make_one(
            self.boto3_raw_data["ResourceConfig"]
        )

    ResourceName = field("ResourceName")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetBackendAuthResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetBackendAuthResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateBackendAuthRequest:
    boto3_raw_data: "type_defs.UpdateBackendAuthRequestTypeDef" = dataclasses.field()

    AppId = field("AppId")
    BackendEnvironmentName = field("BackendEnvironmentName")

    @cached_property
    def ResourceConfig(self):  # pragma: no cover
        return UpdateBackendAuthResourceConfig.make_one(
            self.boto3_raw_data["ResourceConfig"]
        )

    ResourceName = field("ResourceName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateBackendAuthRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateBackendAuthRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateBackendAuthRequest:
    boto3_raw_data: "type_defs.CreateBackendAuthRequestTypeDef" = dataclasses.field()

    AppId = field("AppId")
    BackendEnvironmentName = field("BackendEnvironmentName")
    ResourceConfig = field("ResourceConfig")
    ResourceName = field("ResourceName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateBackendAuthRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateBackendAuthRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
