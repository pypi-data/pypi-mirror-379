# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_chime_sdk_voice import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class Address:
    boto3_raw_data: "type_defs.AddressTypeDef" = dataclasses.field()

    streetName = field("streetName")
    streetSuffix = field("streetSuffix")
    postDirectional = field("postDirectional")
    preDirectional = field("preDirectional")
    streetNumber = field("streetNumber")
    city = field("city")
    state = field("state")
    postalCode = field("postalCode")
    postalCodePlus4 = field("postalCodePlus4")
    country = field("country")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AddressTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AddressTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociatePhoneNumbersWithVoiceConnectorGroupRequest:
    boto3_raw_data: (
        "type_defs.AssociatePhoneNumbersWithVoiceConnectorGroupRequestTypeDef"
    ) = dataclasses.field()

    VoiceConnectorGroupId = field("VoiceConnectorGroupId")
    E164PhoneNumbers = field("E164PhoneNumbers")
    ForceAssociate = field("ForceAssociate")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssociatePhoneNumbersWithVoiceConnectorGroupRequestTypeDef"
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
                "type_defs.AssociatePhoneNumbersWithVoiceConnectorGroupRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PhoneNumberError:
    boto3_raw_data: "type_defs.PhoneNumberErrorTypeDef" = dataclasses.field()

    PhoneNumberId = field("PhoneNumberId")
    ErrorCode = field("ErrorCode")
    ErrorMessage = field("ErrorMessage")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PhoneNumberErrorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PhoneNumberErrorTypeDef"]
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
class AssociatePhoneNumbersWithVoiceConnectorRequest:
    boto3_raw_data: (
        "type_defs.AssociatePhoneNumbersWithVoiceConnectorRequestTypeDef"
    ) = dataclasses.field()

    VoiceConnectorId = field("VoiceConnectorId")
    E164PhoneNumbers = field("E164PhoneNumbers")
    ForceAssociate = field("ForceAssociate")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssociatePhoneNumbersWithVoiceConnectorRequestTypeDef"
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
                "type_defs.AssociatePhoneNumbersWithVoiceConnectorRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchDeletePhoneNumberRequest:
    boto3_raw_data: "type_defs.BatchDeletePhoneNumberRequestTypeDef" = (
        dataclasses.field()
    )

    PhoneNumberIds = field("PhoneNumberIds")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BatchDeletePhoneNumberRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchDeletePhoneNumberRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdatePhoneNumberRequestItem:
    boto3_raw_data: "type_defs.UpdatePhoneNumberRequestItemTypeDef" = (
        dataclasses.field()
    )

    PhoneNumberId = field("PhoneNumberId")
    ProductType = field("ProductType")
    CallingName = field("CallingName")
    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdatePhoneNumberRequestItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePhoneNumberRequestItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CallDetails:
    boto3_raw_data: "type_defs.CallDetailsTypeDef" = dataclasses.field()

    VoiceConnectorId = field("VoiceConnectorId")
    TransactionId = field("TransactionId")
    IsCaller = field("IsCaller")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CallDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CallDetailsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CandidateAddress:
    boto3_raw_data: "type_defs.CandidateAddressTypeDef" = dataclasses.field()

    streetInfo = field("streetInfo")
    streetNumber = field("streetNumber")
    city = field("city")
    state = field("state")
    postalCode = field("postalCode")
    postalCodePlus4 = field("postalCodePlus4")
    country = field("country")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CandidateAddressTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CandidateAddressTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePhoneNumberOrderRequest:
    boto3_raw_data: "type_defs.CreatePhoneNumberOrderRequestTypeDef" = (
        dataclasses.field()
    )

    ProductType = field("ProductType")
    E164PhoneNumbers = field("E164PhoneNumbers")
    Name = field("Name")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreatePhoneNumberOrderRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePhoneNumberOrderRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GeoMatchParams:
    boto3_raw_data: "type_defs.GeoMatchParamsTypeDef" = dataclasses.field()

    Country = field("Country")
    AreaCode = field("AreaCode")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GeoMatchParamsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GeoMatchParamsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSipMediaApplicationCallRequest:
    boto3_raw_data: "type_defs.CreateSipMediaApplicationCallRequestTypeDef" = (
        dataclasses.field()
    )

    FromPhoneNumber = field("FromPhoneNumber")
    ToPhoneNumber = field("ToPhoneNumber")
    SipMediaApplicationId = field("SipMediaApplicationId")
    SipHeaders = field("SipHeaders")
    ArgumentsMap = field("ArgumentsMap")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateSipMediaApplicationCallRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSipMediaApplicationCallRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SipMediaApplicationCall:
    boto3_raw_data: "type_defs.SipMediaApplicationCallTypeDef" = dataclasses.field()

    TransactionId = field("TransactionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SipMediaApplicationCallTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SipMediaApplicationCallTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SipMediaApplicationEndpoint:
    boto3_raw_data: "type_defs.SipMediaApplicationEndpointTypeDef" = dataclasses.field()

    LambdaArn = field("LambdaArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SipMediaApplicationEndpointTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SipMediaApplicationEndpointTypeDef"]
        ],
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
class SipRuleTargetApplication:
    boto3_raw_data: "type_defs.SipRuleTargetApplicationTypeDef" = dataclasses.field()

    SipMediaApplicationId = field("SipMediaApplicationId")
    Priority = field("Priority")
    AwsRegion = field("AwsRegion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SipRuleTargetApplicationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SipRuleTargetApplicationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VoiceConnectorItem:
    boto3_raw_data: "type_defs.VoiceConnectorItemTypeDef" = dataclasses.field()

    VoiceConnectorId = field("VoiceConnectorId")
    Priority = field("Priority")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VoiceConnectorItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VoiceConnectorItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VoiceConnector:
    boto3_raw_data: "type_defs.VoiceConnectorTypeDef" = dataclasses.field()

    VoiceConnectorId = field("VoiceConnectorId")
    AwsRegion = field("AwsRegion")
    Name = field("Name")
    OutboundHostName = field("OutboundHostName")
    RequireEncryption = field("RequireEncryption")
    CreatedTimestamp = field("CreatedTimestamp")
    UpdatedTimestamp = field("UpdatedTimestamp")
    VoiceConnectorArn = field("VoiceConnectorArn")
    IntegrationType = field("IntegrationType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VoiceConnectorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VoiceConnectorTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServerSideEncryptionConfiguration:
    boto3_raw_data: "type_defs.ServerSideEncryptionConfigurationTypeDef" = (
        dataclasses.field()
    )

    KmsKeyArn = field("KmsKeyArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ServerSideEncryptionConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServerSideEncryptionConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateVoiceProfileRequest:
    boto3_raw_data: "type_defs.CreateVoiceProfileRequestTypeDef" = dataclasses.field()

    SpeakerSearchTaskId = field("SpeakerSearchTaskId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateVoiceProfileRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateVoiceProfileRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VoiceProfile:
    boto3_raw_data: "type_defs.VoiceProfileTypeDef" = dataclasses.field()

    VoiceProfileId = field("VoiceProfileId")
    VoiceProfileArn = field("VoiceProfileArn")
    VoiceProfileDomainId = field("VoiceProfileDomainId")
    CreatedTimestamp = field("CreatedTimestamp")
    UpdatedTimestamp = field("UpdatedTimestamp")
    ExpirationTimestamp = field("ExpirationTimestamp")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VoiceProfileTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VoiceProfileTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Credential:
    boto3_raw_data: "type_defs.CredentialTypeDef" = dataclasses.field()

    Username = field("Username")
    Password = field("Password")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CredentialTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CredentialTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DNISEmergencyCallingConfiguration:
    boto3_raw_data: "type_defs.DNISEmergencyCallingConfigurationTypeDef" = (
        dataclasses.field()
    )

    EmergencyPhoneNumber = field("EmergencyPhoneNumber")
    CallingCountry = field("CallingCountry")
    TestPhoneNumber = field("TestPhoneNumber")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DNISEmergencyCallingConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DNISEmergencyCallingConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeletePhoneNumberRequest:
    boto3_raw_data: "type_defs.DeletePhoneNumberRequestTypeDef" = dataclasses.field()

    PhoneNumberId = field("PhoneNumberId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeletePhoneNumberRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeletePhoneNumberRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteProxySessionRequest:
    boto3_raw_data: "type_defs.DeleteProxySessionRequestTypeDef" = dataclasses.field()

    VoiceConnectorId = field("VoiceConnectorId")
    ProxySessionId = field("ProxySessionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteProxySessionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteProxySessionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteSipMediaApplicationRequest:
    boto3_raw_data: "type_defs.DeleteSipMediaApplicationRequestTypeDef" = (
        dataclasses.field()
    )

    SipMediaApplicationId = field("SipMediaApplicationId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteSipMediaApplicationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteSipMediaApplicationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteSipRuleRequest:
    boto3_raw_data: "type_defs.DeleteSipRuleRequestTypeDef" = dataclasses.field()

    SipRuleId = field("SipRuleId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteSipRuleRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteSipRuleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteVoiceConnectorEmergencyCallingConfigurationRequest:
    boto3_raw_data: (
        "type_defs.DeleteVoiceConnectorEmergencyCallingConfigurationRequestTypeDef"
    ) = dataclasses.field()

    VoiceConnectorId = field("VoiceConnectorId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteVoiceConnectorEmergencyCallingConfigurationRequestTypeDef"
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
                "type_defs.DeleteVoiceConnectorEmergencyCallingConfigurationRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteVoiceConnectorExternalSystemsConfigurationRequest:
    boto3_raw_data: (
        "type_defs.DeleteVoiceConnectorExternalSystemsConfigurationRequestTypeDef"
    ) = dataclasses.field()

    VoiceConnectorId = field("VoiceConnectorId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteVoiceConnectorExternalSystemsConfigurationRequestTypeDef"
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
                "type_defs.DeleteVoiceConnectorExternalSystemsConfigurationRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteVoiceConnectorGroupRequest:
    boto3_raw_data: "type_defs.DeleteVoiceConnectorGroupRequestTypeDef" = (
        dataclasses.field()
    )

    VoiceConnectorGroupId = field("VoiceConnectorGroupId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteVoiceConnectorGroupRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteVoiceConnectorGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteVoiceConnectorOriginationRequest:
    boto3_raw_data: "type_defs.DeleteVoiceConnectorOriginationRequestTypeDef" = (
        dataclasses.field()
    )

    VoiceConnectorId = field("VoiceConnectorId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteVoiceConnectorOriginationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteVoiceConnectorOriginationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteVoiceConnectorProxyRequest:
    boto3_raw_data: "type_defs.DeleteVoiceConnectorProxyRequestTypeDef" = (
        dataclasses.field()
    )

    VoiceConnectorId = field("VoiceConnectorId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteVoiceConnectorProxyRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteVoiceConnectorProxyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteVoiceConnectorRequest:
    boto3_raw_data: "type_defs.DeleteVoiceConnectorRequestTypeDef" = dataclasses.field()

    VoiceConnectorId = field("VoiceConnectorId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteVoiceConnectorRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteVoiceConnectorRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteVoiceConnectorStreamingConfigurationRequest:
    boto3_raw_data: (
        "type_defs.DeleteVoiceConnectorStreamingConfigurationRequestTypeDef"
    ) = dataclasses.field()

    VoiceConnectorId = field("VoiceConnectorId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteVoiceConnectorStreamingConfigurationRequestTypeDef"
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
                "type_defs.DeleteVoiceConnectorStreamingConfigurationRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteVoiceConnectorTerminationCredentialsRequest:
    boto3_raw_data: (
        "type_defs.DeleteVoiceConnectorTerminationCredentialsRequestTypeDef"
    ) = dataclasses.field()

    VoiceConnectorId = field("VoiceConnectorId")
    Usernames = field("Usernames")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteVoiceConnectorTerminationCredentialsRequestTypeDef"
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
                "type_defs.DeleteVoiceConnectorTerminationCredentialsRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteVoiceConnectorTerminationRequest:
    boto3_raw_data: "type_defs.DeleteVoiceConnectorTerminationRequestTypeDef" = (
        dataclasses.field()
    )

    VoiceConnectorId = field("VoiceConnectorId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteVoiceConnectorTerminationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteVoiceConnectorTerminationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteVoiceProfileDomainRequest:
    boto3_raw_data: "type_defs.DeleteVoiceProfileDomainRequestTypeDef" = (
        dataclasses.field()
    )

    VoiceProfileDomainId = field("VoiceProfileDomainId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteVoiceProfileDomainRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteVoiceProfileDomainRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteVoiceProfileRequest:
    boto3_raw_data: "type_defs.DeleteVoiceProfileRequestTypeDef" = dataclasses.field()

    VoiceProfileId = field("VoiceProfileId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteVoiceProfileRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteVoiceProfileRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociatePhoneNumbersFromVoiceConnectorGroupRequest:
    boto3_raw_data: (
        "type_defs.DisassociatePhoneNumbersFromVoiceConnectorGroupRequestTypeDef"
    ) = dataclasses.field()

    VoiceConnectorGroupId = field("VoiceConnectorGroupId")
    E164PhoneNumbers = field("E164PhoneNumbers")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisassociatePhoneNumbersFromVoiceConnectorGroupRequestTypeDef"
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
                "type_defs.DisassociatePhoneNumbersFromVoiceConnectorGroupRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociatePhoneNumbersFromVoiceConnectorRequest:
    boto3_raw_data: (
        "type_defs.DisassociatePhoneNumbersFromVoiceConnectorRequestTypeDef"
    ) = dataclasses.field()

    VoiceConnectorId = field("VoiceConnectorId")
    E164PhoneNumbers = field("E164PhoneNumbers")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisassociatePhoneNumbersFromVoiceConnectorRequestTypeDef"
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
                "type_defs.DisassociatePhoneNumbersFromVoiceConnectorRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExternalSystemsConfiguration:
    boto3_raw_data: "type_defs.ExternalSystemsConfigurationTypeDef" = (
        dataclasses.field()
    )

    SessionBorderControllerTypes = field("SessionBorderControllerTypes")
    ContactCenterSystemTypes = field("ContactCenterSystemTypes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExternalSystemsConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExternalSystemsConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VoiceConnectorSettings:
    boto3_raw_data: "type_defs.VoiceConnectorSettingsTypeDef" = dataclasses.field()

    CdrBucket = field("CdrBucket")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VoiceConnectorSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VoiceConnectorSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPhoneNumberOrderRequest:
    boto3_raw_data: "type_defs.GetPhoneNumberOrderRequestTypeDef" = dataclasses.field()

    PhoneNumberOrderId = field("PhoneNumberOrderId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetPhoneNumberOrderRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPhoneNumberOrderRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPhoneNumberRequest:
    boto3_raw_data: "type_defs.GetPhoneNumberRequestTypeDef" = dataclasses.field()

    PhoneNumberId = field("PhoneNumberId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetPhoneNumberRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPhoneNumberRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetProxySessionRequest:
    boto3_raw_data: "type_defs.GetProxySessionRequestTypeDef" = dataclasses.field()

    VoiceConnectorId = field("VoiceConnectorId")
    ProxySessionId = field("ProxySessionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetProxySessionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetProxySessionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSipMediaApplicationAlexaSkillConfigurationRequest:
    boto3_raw_data: (
        "type_defs.GetSipMediaApplicationAlexaSkillConfigurationRequestTypeDef"
    ) = dataclasses.field()

    SipMediaApplicationId = field("SipMediaApplicationId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetSipMediaApplicationAlexaSkillConfigurationRequestTypeDef"
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
                "type_defs.GetSipMediaApplicationAlexaSkillConfigurationRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SipMediaApplicationAlexaSkillConfigurationOutput:
    boto3_raw_data: (
        "type_defs.SipMediaApplicationAlexaSkillConfigurationOutputTypeDef"
    ) = dataclasses.field()

    AlexaSkillStatus = field("AlexaSkillStatus")
    AlexaSkillIds = field("AlexaSkillIds")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SipMediaApplicationAlexaSkillConfigurationOutputTypeDef"
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
                "type_defs.SipMediaApplicationAlexaSkillConfigurationOutputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSipMediaApplicationLoggingConfigurationRequest:
    boto3_raw_data: (
        "type_defs.GetSipMediaApplicationLoggingConfigurationRequestTypeDef"
    ) = dataclasses.field()

    SipMediaApplicationId = field("SipMediaApplicationId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetSipMediaApplicationLoggingConfigurationRequestTypeDef"
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
                "type_defs.GetSipMediaApplicationLoggingConfigurationRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SipMediaApplicationLoggingConfiguration:
    boto3_raw_data: "type_defs.SipMediaApplicationLoggingConfigurationTypeDef" = (
        dataclasses.field()
    )

    EnableSipMediaApplicationMessageLogs = field("EnableSipMediaApplicationMessageLogs")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SipMediaApplicationLoggingConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SipMediaApplicationLoggingConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSipMediaApplicationRequest:
    boto3_raw_data: "type_defs.GetSipMediaApplicationRequestTypeDef" = (
        dataclasses.field()
    )

    SipMediaApplicationId = field("SipMediaApplicationId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetSipMediaApplicationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSipMediaApplicationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSipRuleRequest:
    boto3_raw_data: "type_defs.GetSipRuleRequestTypeDef" = dataclasses.field()

    SipRuleId = field("SipRuleId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetSipRuleRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSipRuleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSpeakerSearchTaskRequest:
    boto3_raw_data: "type_defs.GetSpeakerSearchTaskRequestTypeDef" = dataclasses.field()

    VoiceConnectorId = field("VoiceConnectorId")
    SpeakerSearchTaskId = field("SpeakerSearchTaskId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSpeakerSearchTaskRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSpeakerSearchTaskRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetVoiceConnectorEmergencyCallingConfigurationRequest:
    boto3_raw_data: (
        "type_defs.GetVoiceConnectorEmergencyCallingConfigurationRequestTypeDef"
    ) = dataclasses.field()

    VoiceConnectorId = field("VoiceConnectorId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetVoiceConnectorEmergencyCallingConfigurationRequestTypeDef"
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
                "type_defs.GetVoiceConnectorEmergencyCallingConfigurationRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetVoiceConnectorExternalSystemsConfigurationRequest:
    boto3_raw_data: (
        "type_defs.GetVoiceConnectorExternalSystemsConfigurationRequestTypeDef"
    ) = dataclasses.field()

    VoiceConnectorId = field("VoiceConnectorId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetVoiceConnectorExternalSystemsConfigurationRequestTypeDef"
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
                "type_defs.GetVoiceConnectorExternalSystemsConfigurationRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetVoiceConnectorGroupRequest:
    boto3_raw_data: "type_defs.GetVoiceConnectorGroupRequestTypeDef" = (
        dataclasses.field()
    )

    VoiceConnectorGroupId = field("VoiceConnectorGroupId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetVoiceConnectorGroupRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetVoiceConnectorGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetVoiceConnectorLoggingConfigurationRequest:
    boto3_raw_data: "type_defs.GetVoiceConnectorLoggingConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    VoiceConnectorId = field("VoiceConnectorId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetVoiceConnectorLoggingConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetVoiceConnectorLoggingConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LoggingConfiguration:
    boto3_raw_data: "type_defs.LoggingConfigurationTypeDef" = dataclasses.field()

    EnableSIPLogs = field("EnableSIPLogs")
    EnableMediaMetricLogs = field("EnableMediaMetricLogs")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LoggingConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LoggingConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetVoiceConnectorOriginationRequest:
    boto3_raw_data: "type_defs.GetVoiceConnectorOriginationRequestTypeDef" = (
        dataclasses.field()
    )

    VoiceConnectorId = field("VoiceConnectorId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetVoiceConnectorOriginationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetVoiceConnectorOriginationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetVoiceConnectorProxyRequest:
    boto3_raw_data: "type_defs.GetVoiceConnectorProxyRequestTypeDef" = (
        dataclasses.field()
    )

    VoiceConnectorId = field("VoiceConnectorId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetVoiceConnectorProxyRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetVoiceConnectorProxyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Proxy:
    boto3_raw_data: "type_defs.ProxyTypeDef" = dataclasses.field()

    DefaultSessionExpiryMinutes = field("DefaultSessionExpiryMinutes")
    Disabled = field("Disabled")
    FallBackPhoneNumber = field("FallBackPhoneNumber")
    PhoneNumberCountries = field("PhoneNumberCountries")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ProxyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ProxyTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetVoiceConnectorRequest:
    boto3_raw_data: "type_defs.GetVoiceConnectorRequestTypeDef" = dataclasses.field()

    VoiceConnectorId = field("VoiceConnectorId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetVoiceConnectorRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetVoiceConnectorRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetVoiceConnectorStreamingConfigurationRequest:
    boto3_raw_data: (
        "type_defs.GetVoiceConnectorStreamingConfigurationRequestTypeDef"
    ) = dataclasses.field()

    VoiceConnectorId = field("VoiceConnectorId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetVoiceConnectorStreamingConfigurationRequestTypeDef"
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
                "type_defs.GetVoiceConnectorStreamingConfigurationRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetVoiceConnectorTerminationHealthRequest:
    boto3_raw_data: "type_defs.GetVoiceConnectorTerminationHealthRequestTypeDef" = (
        dataclasses.field()
    )

    VoiceConnectorId = field("VoiceConnectorId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetVoiceConnectorTerminationHealthRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetVoiceConnectorTerminationHealthRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TerminationHealth:
    boto3_raw_data: "type_defs.TerminationHealthTypeDef" = dataclasses.field()

    Timestamp = field("Timestamp")
    Source = field("Source")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TerminationHealthTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TerminationHealthTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetVoiceConnectorTerminationRequest:
    boto3_raw_data: "type_defs.GetVoiceConnectorTerminationRequestTypeDef" = (
        dataclasses.field()
    )

    VoiceConnectorId = field("VoiceConnectorId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetVoiceConnectorTerminationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetVoiceConnectorTerminationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TerminationOutput:
    boto3_raw_data: "type_defs.TerminationOutputTypeDef" = dataclasses.field()

    CpsLimit = field("CpsLimit")
    DefaultPhoneNumber = field("DefaultPhoneNumber")
    CallingRegions = field("CallingRegions")
    CidrAllowedList = field("CidrAllowedList")
    Disabled = field("Disabled")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TerminationOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TerminationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetVoiceProfileDomainRequest:
    boto3_raw_data: "type_defs.GetVoiceProfileDomainRequestTypeDef" = (
        dataclasses.field()
    )

    VoiceProfileDomainId = field("VoiceProfileDomainId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetVoiceProfileDomainRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetVoiceProfileDomainRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetVoiceProfileRequest:
    boto3_raw_data: "type_defs.GetVoiceProfileRequestTypeDef" = dataclasses.field()

    VoiceProfileId = field("VoiceProfileId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetVoiceProfileRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetVoiceProfileRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetVoiceToneAnalysisTaskRequest:
    boto3_raw_data: "type_defs.GetVoiceToneAnalysisTaskRequestTypeDef" = (
        dataclasses.field()
    )

    VoiceConnectorId = field("VoiceConnectorId")
    VoiceToneAnalysisTaskId = field("VoiceToneAnalysisTaskId")
    IsCaller = field("IsCaller")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetVoiceToneAnalysisTaskRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetVoiceToneAnalysisTaskRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPhoneNumberOrdersRequest:
    boto3_raw_data: "type_defs.ListPhoneNumberOrdersRequestTypeDef" = (
        dataclasses.field()
    )

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPhoneNumberOrdersRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPhoneNumberOrdersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPhoneNumbersRequest:
    boto3_raw_data: "type_defs.ListPhoneNumbersRequestTypeDef" = dataclasses.field()

    Status = field("Status")
    ProductType = field("ProductType")
    FilterName = field("FilterName")
    FilterValue = field("FilterValue")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPhoneNumbersRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPhoneNumbersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListProxySessionsRequest:
    boto3_raw_data: "type_defs.ListProxySessionsRequestTypeDef" = dataclasses.field()

    VoiceConnectorId = field("VoiceConnectorId")
    Status = field("Status")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListProxySessionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListProxySessionsRequestTypeDef"]
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
class ListSipMediaApplicationsRequest:
    boto3_raw_data: "type_defs.ListSipMediaApplicationsRequestTypeDef" = (
        dataclasses.field()
    )

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListSipMediaApplicationsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSipMediaApplicationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSipRulesRequest:
    boto3_raw_data: "type_defs.ListSipRulesRequestTypeDef" = dataclasses.field()

    SipMediaApplicationId = field("SipMediaApplicationId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSipRulesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSipRulesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSupportedPhoneNumberCountriesRequest:
    boto3_raw_data: "type_defs.ListSupportedPhoneNumberCountriesRequestTypeDef" = (
        dataclasses.field()
    )

    ProductType = field("ProductType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListSupportedPhoneNumberCountriesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSupportedPhoneNumberCountriesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PhoneNumberCountry:
    boto3_raw_data: "type_defs.PhoneNumberCountryTypeDef" = dataclasses.field()

    CountryCode = field("CountryCode")
    SupportedPhoneNumberTypes = field("SupportedPhoneNumberTypes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PhoneNumberCountryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PhoneNumberCountryTypeDef"]
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

    ResourceARN = field("ResourceARN")

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
class ListVoiceConnectorGroupsRequest:
    boto3_raw_data: "type_defs.ListVoiceConnectorGroupsRequestTypeDef" = (
        dataclasses.field()
    )

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListVoiceConnectorGroupsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListVoiceConnectorGroupsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListVoiceConnectorTerminationCredentialsRequest:
    boto3_raw_data: (
        "type_defs.ListVoiceConnectorTerminationCredentialsRequestTypeDef"
    ) = dataclasses.field()

    VoiceConnectorId = field("VoiceConnectorId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListVoiceConnectorTerminationCredentialsRequestTypeDef"
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
                "type_defs.ListVoiceConnectorTerminationCredentialsRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListVoiceConnectorsRequest:
    boto3_raw_data: "type_defs.ListVoiceConnectorsRequestTypeDef" = dataclasses.field()

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListVoiceConnectorsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListVoiceConnectorsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListVoiceProfileDomainsRequest:
    boto3_raw_data: "type_defs.ListVoiceProfileDomainsRequestTypeDef" = (
        dataclasses.field()
    )

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListVoiceProfileDomainsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListVoiceProfileDomainsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VoiceProfileDomainSummary:
    boto3_raw_data: "type_defs.VoiceProfileDomainSummaryTypeDef" = dataclasses.field()

    VoiceProfileDomainId = field("VoiceProfileDomainId")
    VoiceProfileDomainArn = field("VoiceProfileDomainArn")
    Name = field("Name")
    Description = field("Description")
    CreatedTimestamp = field("CreatedTimestamp")
    UpdatedTimestamp = field("UpdatedTimestamp")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VoiceProfileDomainSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VoiceProfileDomainSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListVoiceProfilesRequest:
    boto3_raw_data: "type_defs.ListVoiceProfilesRequestTypeDef" = dataclasses.field()

    VoiceProfileDomainId = field("VoiceProfileDomainId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListVoiceProfilesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListVoiceProfilesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VoiceProfileSummary:
    boto3_raw_data: "type_defs.VoiceProfileSummaryTypeDef" = dataclasses.field()

    VoiceProfileId = field("VoiceProfileId")
    VoiceProfileArn = field("VoiceProfileArn")
    VoiceProfileDomainId = field("VoiceProfileDomainId")
    CreatedTimestamp = field("CreatedTimestamp")
    UpdatedTimestamp = field("UpdatedTimestamp")
    ExpirationTimestamp = field("ExpirationTimestamp")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VoiceProfileSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VoiceProfileSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MediaInsightsConfiguration:
    boto3_raw_data: "type_defs.MediaInsightsConfigurationTypeDef" = dataclasses.field()

    Disabled = field("Disabled")
    ConfigurationArn = field("ConfigurationArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MediaInsightsConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MediaInsightsConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OrderedPhoneNumber:
    boto3_raw_data: "type_defs.OrderedPhoneNumberTypeDef" = dataclasses.field()

    E164PhoneNumber = field("E164PhoneNumber")
    Status = field("Status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OrderedPhoneNumberTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OrderedPhoneNumberTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OriginationRoute:
    boto3_raw_data: "type_defs.OriginationRouteTypeDef" = dataclasses.field()

    Host = field("Host")
    Port = field("Port")
    Protocol = field("Protocol")
    Priority = field("Priority")
    Weight = field("Weight")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OriginationRouteTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OriginationRouteTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Participant:
    boto3_raw_data: "type_defs.ParticipantTypeDef" = dataclasses.field()

    PhoneNumber = field("PhoneNumber")
    ProxyPhoneNumber = field("ProxyPhoneNumber")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ParticipantTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ParticipantTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PhoneNumberAssociation:
    boto3_raw_data: "type_defs.PhoneNumberAssociationTypeDef" = dataclasses.field()

    Value = field("Value")
    Name = field("Name")
    AssociatedTimestamp = field("AssociatedTimestamp")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PhoneNumberAssociationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PhoneNumberAssociationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PhoneNumberCapabilities:
    boto3_raw_data: "type_defs.PhoneNumberCapabilitiesTypeDef" = dataclasses.field()

    InboundCall = field("InboundCall")
    OutboundCall = field("OutboundCall")
    InboundSMS = field("InboundSMS")
    OutboundSMS = field("OutboundSMS")
    InboundMMS = field("InboundMMS")
    OutboundMMS = field("OutboundMMS")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PhoneNumberCapabilitiesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PhoneNumberCapabilitiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutVoiceConnectorExternalSystemsConfigurationRequest:
    boto3_raw_data: (
        "type_defs.PutVoiceConnectorExternalSystemsConfigurationRequestTypeDef"
    ) = dataclasses.field()

    VoiceConnectorId = field("VoiceConnectorId")
    SessionBorderControllerTypes = field("SessionBorderControllerTypes")
    ContactCenterSystemTypes = field("ContactCenterSystemTypes")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutVoiceConnectorExternalSystemsConfigurationRequestTypeDef"
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
                "type_defs.PutVoiceConnectorExternalSystemsConfigurationRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutVoiceConnectorProxyRequest:
    boto3_raw_data: "type_defs.PutVoiceConnectorProxyRequestTypeDef" = (
        dataclasses.field()
    )

    VoiceConnectorId = field("VoiceConnectorId")
    DefaultSessionExpiryMinutes = field("DefaultSessionExpiryMinutes")
    PhoneNumberPoolCountries = field("PhoneNumberPoolCountries")
    FallBackPhoneNumber = field("FallBackPhoneNumber")
    Disabled = field("Disabled")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PutVoiceConnectorProxyRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutVoiceConnectorProxyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RestorePhoneNumberRequest:
    boto3_raw_data: "type_defs.RestorePhoneNumberRequestTypeDef" = dataclasses.field()

    PhoneNumberId = field("PhoneNumberId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RestorePhoneNumberRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RestorePhoneNumberRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchAvailablePhoneNumbersRequest:
    boto3_raw_data: "type_defs.SearchAvailablePhoneNumbersRequestTypeDef" = (
        dataclasses.field()
    )

    AreaCode = field("AreaCode")
    City = field("City")
    Country = field("Country")
    State = field("State")
    TollFreePrefix = field("TollFreePrefix")
    PhoneNumberType = field("PhoneNumberType")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SearchAvailablePhoneNumbersRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchAvailablePhoneNumbersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SipMediaApplicationAlexaSkillConfiguration:
    boto3_raw_data: "type_defs.SipMediaApplicationAlexaSkillConfigurationTypeDef" = (
        dataclasses.field()
    )

    AlexaSkillStatus = field("AlexaSkillStatus")
    AlexaSkillIds = field("AlexaSkillIds")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SipMediaApplicationAlexaSkillConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SipMediaApplicationAlexaSkillConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SpeakerSearchResult:
    boto3_raw_data: "type_defs.SpeakerSearchResultTypeDef" = dataclasses.field()

    ConfidenceScore = field("ConfidenceScore")
    VoiceProfileId = field("VoiceProfileId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SpeakerSearchResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SpeakerSearchResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartSpeakerSearchTaskRequest:
    boto3_raw_data: "type_defs.StartSpeakerSearchTaskRequestTypeDef" = (
        dataclasses.field()
    )

    VoiceConnectorId = field("VoiceConnectorId")
    TransactionId = field("TransactionId")
    VoiceProfileDomainId = field("VoiceProfileDomainId")
    ClientRequestToken = field("ClientRequestToken")
    CallLeg = field("CallLeg")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartSpeakerSearchTaskRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartSpeakerSearchTaskRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartVoiceToneAnalysisTaskRequest:
    boto3_raw_data: "type_defs.StartVoiceToneAnalysisTaskRequestTypeDef" = (
        dataclasses.field()
    )

    VoiceConnectorId = field("VoiceConnectorId")
    TransactionId = field("TransactionId")
    LanguageCode = field("LanguageCode")
    ClientRequestToken = field("ClientRequestToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartVoiceToneAnalysisTaskRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartVoiceToneAnalysisTaskRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopSpeakerSearchTaskRequest:
    boto3_raw_data: "type_defs.StopSpeakerSearchTaskRequestTypeDef" = (
        dataclasses.field()
    )

    VoiceConnectorId = field("VoiceConnectorId")
    SpeakerSearchTaskId = field("SpeakerSearchTaskId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopSpeakerSearchTaskRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopSpeakerSearchTaskRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopVoiceToneAnalysisTaskRequest:
    boto3_raw_data: "type_defs.StopVoiceToneAnalysisTaskRequestTypeDef" = (
        dataclasses.field()
    )

    VoiceConnectorId = field("VoiceConnectorId")
    VoiceToneAnalysisTaskId = field("VoiceToneAnalysisTaskId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StopVoiceToneAnalysisTaskRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopVoiceToneAnalysisTaskRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StreamingNotificationTarget:
    boto3_raw_data: "type_defs.StreamingNotificationTargetTypeDef" = dataclasses.field()

    NotificationTarget = field("NotificationTarget")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StreamingNotificationTargetTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StreamingNotificationTargetTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Termination:
    boto3_raw_data: "type_defs.TerminationTypeDef" = dataclasses.field()

    CpsLimit = field("CpsLimit")
    DefaultPhoneNumber = field("DefaultPhoneNumber")
    CallingRegions = field("CallingRegions")
    CidrAllowedList = field("CidrAllowedList")
    Disabled = field("Disabled")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TerminationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TerminationTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UntagResourceRequest:
    boto3_raw_data: "type_defs.UntagResourceRequestTypeDef" = dataclasses.field()

    ResourceARN = field("ResourceARN")
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
class UpdatePhoneNumberRequest:
    boto3_raw_data: "type_defs.UpdatePhoneNumberRequestTypeDef" = dataclasses.field()

    PhoneNumberId = field("PhoneNumberId")
    ProductType = field("ProductType")
    CallingName = field("CallingName")
    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdatePhoneNumberRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePhoneNumberRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdatePhoneNumberSettingsRequest:
    boto3_raw_data: "type_defs.UpdatePhoneNumberSettingsRequestTypeDef" = (
        dataclasses.field()
    )

    CallingName = field("CallingName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdatePhoneNumberSettingsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePhoneNumberSettingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateProxySessionRequest:
    boto3_raw_data: "type_defs.UpdateProxySessionRequestTypeDef" = dataclasses.field()

    VoiceConnectorId = field("VoiceConnectorId")
    ProxySessionId = field("ProxySessionId")
    Capabilities = field("Capabilities")
    ExpiryMinutes = field("ExpiryMinutes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateProxySessionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateProxySessionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSipMediaApplicationCallRequest:
    boto3_raw_data: "type_defs.UpdateSipMediaApplicationCallRequestTypeDef" = (
        dataclasses.field()
    )

    SipMediaApplicationId = field("SipMediaApplicationId")
    TransactionId = field("TransactionId")
    Arguments = field("Arguments")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateSipMediaApplicationCallRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSipMediaApplicationCallRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateVoiceConnectorRequest:
    boto3_raw_data: "type_defs.UpdateVoiceConnectorRequestTypeDef" = dataclasses.field()

    VoiceConnectorId = field("VoiceConnectorId")
    Name = field("Name")
    RequireEncryption = field("RequireEncryption")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateVoiceConnectorRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateVoiceConnectorRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateVoiceProfileDomainRequest:
    boto3_raw_data: "type_defs.UpdateVoiceProfileDomainRequestTypeDef" = (
        dataclasses.field()
    )

    VoiceProfileDomainId = field("VoiceProfileDomainId")
    Name = field("Name")
    Description = field("Description")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateVoiceProfileDomainRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateVoiceProfileDomainRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateVoiceProfileRequest:
    boto3_raw_data: "type_defs.UpdateVoiceProfileRequestTypeDef" = dataclasses.field()

    VoiceProfileId = field("VoiceProfileId")
    SpeakerSearchTaskId = field("SpeakerSearchTaskId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateVoiceProfileRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateVoiceProfileRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ValidateE911AddressRequest:
    boto3_raw_data: "type_defs.ValidateE911AddressRequestTypeDef" = dataclasses.field()

    AwsAccountId = field("AwsAccountId")
    StreetNumber = field("StreetNumber")
    StreetInfo = field("StreetInfo")
    City = field("City")
    State = field("State")
    Country = field("Country")
    PostalCode = field("PostalCode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ValidateE911AddressRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ValidateE911AddressRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociatePhoneNumbersWithVoiceConnectorGroupResponse:
    boto3_raw_data: (
        "type_defs.AssociatePhoneNumbersWithVoiceConnectorGroupResponseTypeDef"
    ) = dataclasses.field()

    @cached_property
    def PhoneNumberErrors(self):  # pragma: no cover
        return PhoneNumberError.make_many(self.boto3_raw_data["PhoneNumberErrors"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssociatePhoneNumbersWithVoiceConnectorGroupResponseTypeDef"
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
                "type_defs.AssociatePhoneNumbersWithVoiceConnectorGroupResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociatePhoneNumbersWithVoiceConnectorResponse:
    boto3_raw_data: (
        "type_defs.AssociatePhoneNumbersWithVoiceConnectorResponseTypeDef"
    ) = dataclasses.field()

    @cached_property
    def PhoneNumberErrors(self):  # pragma: no cover
        return PhoneNumberError.make_many(self.boto3_raw_data["PhoneNumberErrors"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssociatePhoneNumbersWithVoiceConnectorResponseTypeDef"
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
                "type_defs.AssociatePhoneNumbersWithVoiceConnectorResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchDeletePhoneNumberResponse:
    boto3_raw_data: "type_defs.BatchDeletePhoneNumberResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PhoneNumberErrors(self):  # pragma: no cover
        return PhoneNumberError.make_many(self.boto3_raw_data["PhoneNumberErrors"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BatchDeletePhoneNumberResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchDeletePhoneNumberResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchUpdatePhoneNumberResponse:
    boto3_raw_data: "type_defs.BatchUpdatePhoneNumberResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PhoneNumberErrors(self):  # pragma: no cover
        return PhoneNumberError.make_many(self.boto3_raw_data["PhoneNumberErrors"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BatchUpdatePhoneNumberResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchUpdatePhoneNumberResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociatePhoneNumbersFromVoiceConnectorGroupResponse:
    boto3_raw_data: (
        "type_defs.DisassociatePhoneNumbersFromVoiceConnectorGroupResponseTypeDef"
    ) = dataclasses.field()

    @cached_property
    def PhoneNumberErrors(self):  # pragma: no cover
        return PhoneNumberError.make_many(self.boto3_raw_data["PhoneNumberErrors"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisassociatePhoneNumbersFromVoiceConnectorGroupResponseTypeDef"
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
                "type_defs.DisassociatePhoneNumbersFromVoiceConnectorGroupResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociatePhoneNumbersFromVoiceConnectorResponse:
    boto3_raw_data: (
        "type_defs.DisassociatePhoneNumbersFromVoiceConnectorResponseTypeDef"
    ) = dataclasses.field()

    @cached_property
    def PhoneNumberErrors(self):  # pragma: no cover
        return PhoneNumberError.make_many(self.boto3_raw_data["PhoneNumberErrors"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisassociatePhoneNumbersFromVoiceConnectorResponseTypeDef"
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
                "type_defs.DisassociatePhoneNumbersFromVoiceConnectorResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EmptyResponseMetadata:
    boto3_raw_data: "type_defs.EmptyResponseMetadataTypeDef" = dataclasses.field()

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EmptyResponseMetadataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EmptyResponseMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPhoneNumberSettingsResponse:
    boto3_raw_data: "type_defs.GetPhoneNumberSettingsResponseTypeDef" = (
        dataclasses.field()
    )

    CallingName = field("CallingName")
    CallingNameUpdatedTimestamp = field("CallingNameUpdatedTimestamp")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetPhoneNumberSettingsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPhoneNumberSettingsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAvailableVoiceConnectorRegionsResponse:
    boto3_raw_data: "type_defs.ListAvailableVoiceConnectorRegionsResponseTypeDef" = (
        dataclasses.field()
    )

    VoiceConnectorRegions = field("VoiceConnectorRegions")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAvailableVoiceConnectorRegionsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAvailableVoiceConnectorRegionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListVoiceConnectorTerminationCredentialsResponse:
    boto3_raw_data: (
        "type_defs.ListVoiceConnectorTerminationCredentialsResponseTypeDef"
    ) = dataclasses.field()

    Usernames = field("Usernames")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListVoiceConnectorTerminationCredentialsResponseTypeDef"
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
                "type_defs.ListVoiceConnectorTerminationCredentialsResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchAvailablePhoneNumbersResponse:
    boto3_raw_data: "type_defs.SearchAvailablePhoneNumbersResponseTypeDef" = (
        dataclasses.field()
    )

    E164PhoneNumbers = field("E164PhoneNumbers")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SearchAvailablePhoneNumbersResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchAvailablePhoneNumbersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchUpdatePhoneNumberRequest:
    boto3_raw_data: "type_defs.BatchUpdatePhoneNumberRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def UpdatePhoneNumberRequestItems(self):  # pragma: no cover
        return UpdatePhoneNumberRequestItem.make_many(
            self.boto3_raw_data["UpdatePhoneNumberRequestItems"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BatchUpdatePhoneNumberRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchUpdatePhoneNumberRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VoiceToneAnalysisTask:
    boto3_raw_data: "type_defs.VoiceToneAnalysisTaskTypeDef" = dataclasses.field()

    VoiceToneAnalysisTaskId = field("VoiceToneAnalysisTaskId")
    VoiceToneAnalysisTaskStatus = field("VoiceToneAnalysisTaskStatus")

    @cached_property
    def CallDetails(self):  # pragma: no cover
        return CallDetails.make_one(self.boto3_raw_data["CallDetails"])

    CreatedTimestamp = field("CreatedTimestamp")
    UpdatedTimestamp = field("UpdatedTimestamp")
    StartedTimestamp = field("StartedTimestamp")
    StatusMessage = field("StatusMessage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VoiceToneAnalysisTaskTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VoiceToneAnalysisTaskTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ValidateE911AddressResponse:
    boto3_raw_data: "type_defs.ValidateE911AddressResponseTypeDef" = dataclasses.field()

    ValidationResult = field("ValidationResult")
    AddressExternalId = field("AddressExternalId")

    @cached_property
    def Address(self):  # pragma: no cover
        return Address.make_one(self.boto3_raw_data["Address"])

    @cached_property
    def CandidateAddressList(self):  # pragma: no cover
        return CandidateAddress.make_many(self.boto3_raw_data["CandidateAddressList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ValidateE911AddressResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ValidateE911AddressResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateProxySessionRequest:
    boto3_raw_data: "type_defs.CreateProxySessionRequestTypeDef" = dataclasses.field()

    VoiceConnectorId = field("VoiceConnectorId")
    ParticipantPhoneNumbers = field("ParticipantPhoneNumbers")
    Capabilities = field("Capabilities")
    Name = field("Name")
    ExpiryMinutes = field("ExpiryMinutes")
    NumberSelectionBehavior = field("NumberSelectionBehavior")
    GeoMatchLevel = field("GeoMatchLevel")

    @cached_property
    def GeoMatchParams(self):  # pragma: no cover
        return GeoMatchParams.make_one(self.boto3_raw_data["GeoMatchParams"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateProxySessionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateProxySessionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSipMediaApplicationCallResponse:
    boto3_raw_data: "type_defs.CreateSipMediaApplicationCallResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def SipMediaApplicationCall(self):  # pragma: no cover
        return SipMediaApplicationCall.make_one(
            self.boto3_raw_data["SipMediaApplicationCall"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateSipMediaApplicationCallResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSipMediaApplicationCallResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSipMediaApplicationCallResponse:
    boto3_raw_data: "type_defs.UpdateSipMediaApplicationCallResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def SipMediaApplicationCall(self):  # pragma: no cover
        return SipMediaApplicationCall.make_one(
            self.boto3_raw_data["SipMediaApplicationCall"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateSipMediaApplicationCallResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSipMediaApplicationCallResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SipMediaApplication:
    boto3_raw_data: "type_defs.SipMediaApplicationTypeDef" = dataclasses.field()

    SipMediaApplicationId = field("SipMediaApplicationId")
    AwsRegion = field("AwsRegion")
    Name = field("Name")

    @cached_property
    def Endpoints(self):  # pragma: no cover
        return SipMediaApplicationEndpoint.make_many(self.boto3_raw_data["Endpoints"])

    CreatedTimestamp = field("CreatedTimestamp")
    UpdatedTimestamp = field("UpdatedTimestamp")
    SipMediaApplicationArn = field("SipMediaApplicationArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SipMediaApplicationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SipMediaApplicationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSipMediaApplicationRequest:
    boto3_raw_data: "type_defs.UpdateSipMediaApplicationRequestTypeDef" = (
        dataclasses.field()
    )

    SipMediaApplicationId = field("SipMediaApplicationId")
    Name = field("Name")

    @cached_property
    def Endpoints(self):  # pragma: no cover
        return SipMediaApplicationEndpoint.make_many(self.boto3_raw_data["Endpoints"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateSipMediaApplicationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSipMediaApplicationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSipMediaApplicationRequest:
    boto3_raw_data: "type_defs.CreateSipMediaApplicationRequestTypeDef" = (
        dataclasses.field()
    )

    AwsRegion = field("AwsRegion")
    Name = field("Name")

    @cached_property
    def Endpoints(self):  # pragma: no cover
        return SipMediaApplicationEndpoint.make_many(self.boto3_raw_data["Endpoints"])

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateSipMediaApplicationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSipMediaApplicationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateVoiceConnectorRequest:
    boto3_raw_data: "type_defs.CreateVoiceConnectorRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    RequireEncryption = field("RequireEncryption")
    AwsRegion = field("AwsRegion")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    IntegrationType = field("IntegrationType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateVoiceConnectorRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateVoiceConnectorRequestTypeDef"]
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
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

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
class TagResourceRequest:
    boto3_raw_data: "type_defs.TagResourceRequestTypeDef" = dataclasses.field()

    ResourceARN = field("ResourceARN")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

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
class CreateSipRuleRequest:
    boto3_raw_data: "type_defs.CreateSipRuleRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    TriggerType = field("TriggerType")
    TriggerValue = field("TriggerValue")
    Disabled = field("Disabled")

    @cached_property
    def TargetApplications(self):  # pragma: no cover
        return SipRuleTargetApplication.make_many(
            self.boto3_raw_data["TargetApplications"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateSipRuleRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSipRuleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SipRule:
    boto3_raw_data: "type_defs.SipRuleTypeDef" = dataclasses.field()

    SipRuleId = field("SipRuleId")
    Name = field("Name")
    Disabled = field("Disabled")
    TriggerType = field("TriggerType")
    TriggerValue = field("TriggerValue")

    @cached_property
    def TargetApplications(self):  # pragma: no cover
        return SipRuleTargetApplication.make_many(
            self.boto3_raw_data["TargetApplications"]
        )

    CreatedTimestamp = field("CreatedTimestamp")
    UpdatedTimestamp = field("UpdatedTimestamp")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SipRuleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SipRuleTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSipRuleRequest:
    boto3_raw_data: "type_defs.UpdateSipRuleRequestTypeDef" = dataclasses.field()

    SipRuleId = field("SipRuleId")
    Name = field("Name")
    Disabled = field("Disabled")

    @cached_property
    def TargetApplications(self):  # pragma: no cover
        return SipRuleTargetApplication.make_many(
            self.boto3_raw_data["TargetApplications"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateSipRuleRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSipRuleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateVoiceConnectorGroupRequest:
    boto3_raw_data: "type_defs.CreateVoiceConnectorGroupRequestTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")

    @cached_property
    def VoiceConnectorItems(self):  # pragma: no cover
        return VoiceConnectorItem.make_many(self.boto3_raw_data["VoiceConnectorItems"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateVoiceConnectorGroupRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateVoiceConnectorGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateVoiceConnectorGroupRequest:
    boto3_raw_data: "type_defs.UpdateVoiceConnectorGroupRequestTypeDef" = (
        dataclasses.field()
    )

    VoiceConnectorGroupId = field("VoiceConnectorGroupId")
    Name = field("Name")

    @cached_property
    def VoiceConnectorItems(self):  # pragma: no cover
        return VoiceConnectorItem.make_many(self.boto3_raw_data["VoiceConnectorItems"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateVoiceConnectorGroupRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateVoiceConnectorGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VoiceConnectorGroup:
    boto3_raw_data: "type_defs.VoiceConnectorGroupTypeDef" = dataclasses.field()

    VoiceConnectorGroupId = field("VoiceConnectorGroupId")
    Name = field("Name")

    @cached_property
    def VoiceConnectorItems(self):  # pragma: no cover
        return VoiceConnectorItem.make_many(self.boto3_raw_data["VoiceConnectorItems"])

    CreatedTimestamp = field("CreatedTimestamp")
    UpdatedTimestamp = field("UpdatedTimestamp")
    VoiceConnectorGroupArn = field("VoiceConnectorGroupArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VoiceConnectorGroupTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VoiceConnectorGroupTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateVoiceConnectorResponse:
    boto3_raw_data: "type_defs.CreateVoiceConnectorResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def VoiceConnector(self):  # pragma: no cover
        return VoiceConnector.make_one(self.boto3_raw_data["VoiceConnector"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateVoiceConnectorResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateVoiceConnectorResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetVoiceConnectorResponse:
    boto3_raw_data: "type_defs.GetVoiceConnectorResponseTypeDef" = dataclasses.field()

    @cached_property
    def VoiceConnector(self):  # pragma: no cover
        return VoiceConnector.make_one(self.boto3_raw_data["VoiceConnector"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetVoiceConnectorResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetVoiceConnectorResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListVoiceConnectorsResponse:
    boto3_raw_data: "type_defs.ListVoiceConnectorsResponseTypeDef" = dataclasses.field()

    @cached_property
    def VoiceConnectors(self):  # pragma: no cover
        return VoiceConnector.make_many(self.boto3_raw_data["VoiceConnectors"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListVoiceConnectorsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListVoiceConnectorsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateVoiceConnectorResponse:
    boto3_raw_data: "type_defs.UpdateVoiceConnectorResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def VoiceConnector(self):  # pragma: no cover
        return VoiceConnector.make_one(self.boto3_raw_data["VoiceConnector"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateVoiceConnectorResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateVoiceConnectorResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateVoiceProfileDomainRequest:
    boto3_raw_data: "type_defs.CreateVoiceProfileDomainRequestTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")

    @cached_property
    def ServerSideEncryptionConfiguration(self):  # pragma: no cover
        return ServerSideEncryptionConfiguration.make_one(
            self.boto3_raw_data["ServerSideEncryptionConfiguration"]
        )

    Description = field("Description")
    ClientRequestToken = field("ClientRequestToken")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateVoiceProfileDomainRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateVoiceProfileDomainRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VoiceProfileDomain:
    boto3_raw_data: "type_defs.VoiceProfileDomainTypeDef" = dataclasses.field()

    VoiceProfileDomainId = field("VoiceProfileDomainId")
    VoiceProfileDomainArn = field("VoiceProfileDomainArn")
    Name = field("Name")
    Description = field("Description")

    @cached_property
    def ServerSideEncryptionConfiguration(self):  # pragma: no cover
        return ServerSideEncryptionConfiguration.make_one(
            self.boto3_raw_data["ServerSideEncryptionConfiguration"]
        )

    CreatedTimestamp = field("CreatedTimestamp")
    UpdatedTimestamp = field("UpdatedTimestamp")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VoiceProfileDomainTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VoiceProfileDomainTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateVoiceProfileResponse:
    boto3_raw_data: "type_defs.CreateVoiceProfileResponseTypeDef" = dataclasses.field()

    @cached_property
    def VoiceProfile(self):  # pragma: no cover
        return VoiceProfile.make_one(self.boto3_raw_data["VoiceProfile"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateVoiceProfileResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateVoiceProfileResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetVoiceProfileResponse:
    boto3_raw_data: "type_defs.GetVoiceProfileResponseTypeDef" = dataclasses.field()

    @cached_property
    def VoiceProfile(self):  # pragma: no cover
        return VoiceProfile.make_one(self.boto3_raw_data["VoiceProfile"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetVoiceProfileResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetVoiceProfileResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateVoiceProfileResponse:
    boto3_raw_data: "type_defs.UpdateVoiceProfileResponseTypeDef" = dataclasses.field()

    @cached_property
    def VoiceProfile(self):  # pragma: no cover
        return VoiceProfile.make_one(self.boto3_raw_data["VoiceProfile"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateVoiceProfileResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateVoiceProfileResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutVoiceConnectorTerminationCredentialsRequest:
    boto3_raw_data: (
        "type_defs.PutVoiceConnectorTerminationCredentialsRequestTypeDef"
    ) = dataclasses.field()

    VoiceConnectorId = field("VoiceConnectorId")

    @cached_property
    def Credentials(self):  # pragma: no cover
        return Credential.make_many(self.boto3_raw_data["Credentials"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutVoiceConnectorTerminationCredentialsRequestTypeDef"
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
                "type_defs.PutVoiceConnectorTerminationCredentialsRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EmergencyCallingConfigurationOutput:
    boto3_raw_data: "type_defs.EmergencyCallingConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DNIS(self):  # pragma: no cover
        return DNISEmergencyCallingConfiguration.make_many(self.boto3_raw_data["DNIS"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.EmergencyCallingConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EmergencyCallingConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EmergencyCallingConfiguration:
    boto3_raw_data: "type_defs.EmergencyCallingConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DNIS(self):  # pragma: no cover
        return DNISEmergencyCallingConfiguration.make_many(self.boto3_raw_data["DNIS"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.EmergencyCallingConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EmergencyCallingConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetVoiceConnectorExternalSystemsConfigurationResponse:
    boto3_raw_data: (
        "type_defs.GetVoiceConnectorExternalSystemsConfigurationResponseTypeDef"
    ) = dataclasses.field()

    @cached_property
    def ExternalSystemsConfiguration(self):  # pragma: no cover
        return ExternalSystemsConfiguration.make_one(
            self.boto3_raw_data["ExternalSystemsConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetVoiceConnectorExternalSystemsConfigurationResponseTypeDef"
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
                "type_defs.GetVoiceConnectorExternalSystemsConfigurationResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutVoiceConnectorExternalSystemsConfigurationResponse:
    boto3_raw_data: (
        "type_defs.PutVoiceConnectorExternalSystemsConfigurationResponseTypeDef"
    ) = dataclasses.field()

    @cached_property
    def ExternalSystemsConfiguration(self):  # pragma: no cover
        return ExternalSystemsConfiguration.make_one(
            self.boto3_raw_data["ExternalSystemsConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutVoiceConnectorExternalSystemsConfigurationResponseTypeDef"
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
                "type_defs.PutVoiceConnectorExternalSystemsConfigurationResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetGlobalSettingsResponse:
    boto3_raw_data: "type_defs.GetGlobalSettingsResponseTypeDef" = dataclasses.field()

    @cached_property
    def VoiceConnector(self):  # pragma: no cover
        return VoiceConnectorSettings.make_one(self.boto3_raw_data["VoiceConnector"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetGlobalSettingsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetGlobalSettingsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateGlobalSettingsRequest:
    boto3_raw_data: "type_defs.UpdateGlobalSettingsRequestTypeDef" = dataclasses.field()

    @cached_property
    def VoiceConnector(self):  # pragma: no cover
        return VoiceConnectorSettings.make_one(self.boto3_raw_data["VoiceConnector"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateGlobalSettingsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateGlobalSettingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSipMediaApplicationAlexaSkillConfigurationResponse:
    boto3_raw_data: (
        "type_defs.GetSipMediaApplicationAlexaSkillConfigurationResponseTypeDef"
    ) = dataclasses.field()

    @cached_property
    def SipMediaApplicationAlexaSkillConfiguration(self):  # pragma: no cover
        return SipMediaApplicationAlexaSkillConfigurationOutput.make_one(
            self.boto3_raw_data["SipMediaApplicationAlexaSkillConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetSipMediaApplicationAlexaSkillConfigurationResponseTypeDef"
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
                "type_defs.GetSipMediaApplicationAlexaSkillConfigurationResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutSipMediaApplicationAlexaSkillConfigurationResponse:
    boto3_raw_data: (
        "type_defs.PutSipMediaApplicationAlexaSkillConfigurationResponseTypeDef"
    ) = dataclasses.field()

    @cached_property
    def SipMediaApplicationAlexaSkillConfiguration(self):  # pragma: no cover
        return SipMediaApplicationAlexaSkillConfigurationOutput.make_one(
            self.boto3_raw_data["SipMediaApplicationAlexaSkillConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutSipMediaApplicationAlexaSkillConfigurationResponseTypeDef"
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
                "type_defs.PutSipMediaApplicationAlexaSkillConfigurationResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSipMediaApplicationLoggingConfigurationResponse:
    boto3_raw_data: (
        "type_defs.GetSipMediaApplicationLoggingConfigurationResponseTypeDef"
    ) = dataclasses.field()

    @cached_property
    def SipMediaApplicationLoggingConfiguration(self):  # pragma: no cover
        return SipMediaApplicationLoggingConfiguration.make_one(
            self.boto3_raw_data["SipMediaApplicationLoggingConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetSipMediaApplicationLoggingConfigurationResponseTypeDef"
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
                "type_defs.GetSipMediaApplicationLoggingConfigurationResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutSipMediaApplicationLoggingConfigurationRequest:
    boto3_raw_data: (
        "type_defs.PutSipMediaApplicationLoggingConfigurationRequestTypeDef"
    ) = dataclasses.field()

    SipMediaApplicationId = field("SipMediaApplicationId")

    @cached_property
    def SipMediaApplicationLoggingConfiguration(self):  # pragma: no cover
        return SipMediaApplicationLoggingConfiguration.make_one(
            self.boto3_raw_data["SipMediaApplicationLoggingConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutSipMediaApplicationLoggingConfigurationRequestTypeDef"
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
                "type_defs.PutSipMediaApplicationLoggingConfigurationRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutSipMediaApplicationLoggingConfigurationResponse:
    boto3_raw_data: (
        "type_defs.PutSipMediaApplicationLoggingConfigurationResponseTypeDef"
    ) = dataclasses.field()

    @cached_property
    def SipMediaApplicationLoggingConfiguration(self):  # pragma: no cover
        return SipMediaApplicationLoggingConfiguration.make_one(
            self.boto3_raw_data["SipMediaApplicationLoggingConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutSipMediaApplicationLoggingConfigurationResponseTypeDef"
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
                "type_defs.PutSipMediaApplicationLoggingConfigurationResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetVoiceConnectorLoggingConfigurationResponse:
    boto3_raw_data: "type_defs.GetVoiceConnectorLoggingConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def LoggingConfiguration(self):  # pragma: no cover
        return LoggingConfiguration.make_one(
            self.boto3_raw_data["LoggingConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetVoiceConnectorLoggingConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetVoiceConnectorLoggingConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutVoiceConnectorLoggingConfigurationRequest:
    boto3_raw_data: "type_defs.PutVoiceConnectorLoggingConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    VoiceConnectorId = field("VoiceConnectorId")

    @cached_property
    def LoggingConfiguration(self):  # pragma: no cover
        return LoggingConfiguration.make_one(
            self.boto3_raw_data["LoggingConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutVoiceConnectorLoggingConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutVoiceConnectorLoggingConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutVoiceConnectorLoggingConfigurationResponse:
    boto3_raw_data: "type_defs.PutVoiceConnectorLoggingConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def LoggingConfiguration(self):  # pragma: no cover
        return LoggingConfiguration.make_one(
            self.boto3_raw_data["LoggingConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutVoiceConnectorLoggingConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutVoiceConnectorLoggingConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetVoiceConnectorProxyResponse:
    boto3_raw_data: "type_defs.GetVoiceConnectorProxyResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Proxy(self):  # pragma: no cover
        return Proxy.make_one(self.boto3_raw_data["Proxy"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetVoiceConnectorProxyResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetVoiceConnectorProxyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutVoiceConnectorProxyResponse:
    boto3_raw_data: "type_defs.PutVoiceConnectorProxyResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Proxy(self):  # pragma: no cover
        return Proxy.make_one(self.boto3_raw_data["Proxy"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PutVoiceConnectorProxyResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutVoiceConnectorProxyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetVoiceConnectorTerminationHealthResponse:
    boto3_raw_data: "type_defs.GetVoiceConnectorTerminationHealthResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def TerminationHealth(self):  # pragma: no cover
        return TerminationHealth.make_one(self.boto3_raw_data["TerminationHealth"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetVoiceConnectorTerminationHealthResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetVoiceConnectorTerminationHealthResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetVoiceConnectorTerminationResponse:
    boto3_raw_data: "type_defs.GetVoiceConnectorTerminationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Termination(self):  # pragma: no cover
        return TerminationOutput.make_one(self.boto3_raw_data["Termination"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetVoiceConnectorTerminationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetVoiceConnectorTerminationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutVoiceConnectorTerminationResponse:
    boto3_raw_data: "type_defs.PutVoiceConnectorTerminationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Termination(self):  # pragma: no cover
        return TerminationOutput.make_one(self.boto3_raw_data["Termination"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutVoiceConnectorTerminationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutVoiceConnectorTerminationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSipMediaApplicationsRequestPaginate:
    boto3_raw_data: "type_defs.ListSipMediaApplicationsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListSipMediaApplicationsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSipMediaApplicationsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSipRulesRequestPaginate:
    boto3_raw_data: "type_defs.ListSipRulesRequestPaginateTypeDef" = dataclasses.field()

    SipMediaApplicationId = field("SipMediaApplicationId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSipRulesRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSipRulesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSupportedPhoneNumberCountriesResponse:
    boto3_raw_data: "type_defs.ListSupportedPhoneNumberCountriesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PhoneNumberCountries(self):  # pragma: no cover
        return PhoneNumberCountry.make_many(self.boto3_raw_data["PhoneNumberCountries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListSupportedPhoneNumberCountriesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSupportedPhoneNumberCountriesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListVoiceProfileDomainsResponse:
    boto3_raw_data: "type_defs.ListVoiceProfileDomainsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def VoiceProfileDomains(self):  # pragma: no cover
        return VoiceProfileDomainSummary.make_many(
            self.boto3_raw_data["VoiceProfileDomains"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListVoiceProfileDomainsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListVoiceProfileDomainsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListVoiceProfilesResponse:
    boto3_raw_data: "type_defs.ListVoiceProfilesResponseTypeDef" = dataclasses.field()

    @cached_property
    def VoiceProfiles(self):  # pragma: no cover
        return VoiceProfileSummary.make_many(self.boto3_raw_data["VoiceProfiles"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListVoiceProfilesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListVoiceProfilesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PhoneNumberOrder:
    boto3_raw_data: "type_defs.PhoneNumberOrderTypeDef" = dataclasses.field()

    PhoneNumberOrderId = field("PhoneNumberOrderId")
    ProductType = field("ProductType")
    Status = field("Status")
    OrderType = field("OrderType")

    @cached_property
    def OrderedPhoneNumbers(self):  # pragma: no cover
        return OrderedPhoneNumber.make_many(self.boto3_raw_data["OrderedPhoneNumbers"])

    CreatedTimestamp = field("CreatedTimestamp")
    UpdatedTimestamp = field("UpdatedTimestamp")
    FocDate = field("FocDate")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PhoneNumberOrderTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PhoneNumberOrderTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OriginationOutput:
    boto3_raw_data: "type_defs.OriginationOutputTypeDef" = dataclasses.field()

    @cached_property
    def Routes(self):  # pragma: no cover
        return OriginationRoute.make_many(self.boto3_raw_data["Routes"])

    Disabled = field("Disabled")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OriginationOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OriginationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Origination:
    boto3_raw_data: "type_defs.OriginationTypeDef" = dataclasses.field()

    @cached_property
    def Routes(self):  # pragma: no cover
        return OriginationRoute.make_many(self.boto3_raw_data["Routes"])

    Disabled = field("Disabled")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OriginationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OriginationTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProxySession:
    boto3_raw_data: "type_defs.ProxySessionTypeDef" = dataclasses.field()

    VoiceConnectorId = field("VoiceConnectorId")
    ProxySessionId = field("ProxySessionId")
    Name = field("Name")
    Status = field("Status")
    ExpiryMinutes = field("ExpiryMinutes")
    Capabilities = field("Capabilities")
    CreatedTimestamp = field("CreatedTimestamp")
    UpdatedTimestamp = field("UpdatedTimestamp")
    EndedTimestamp = field("EndedTimestamp")

    @cached_property
    def Participants(self):  # pragma: no cover
        return Participant.make_many(self.boto3_raw_data["Participants"])

    NumberSelectionBehavior = field("NumberSelectionBehavior")
    GeoMatchLevel = field("GeoMatchLevel")

    @cached_property
    def GeoMatchParams(self):  # pragma: no cover
        return GeoMatchParams.make_one(self.boto3_raw_data["GeoMatchParams"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ProxySessionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ProxySessionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PhoneNumber:
    boto3_raw_data: "type_defs.PhoneNumberTypeDef" = dataclasses.field()

    PhoneNumberId = field("PhoneNumberId")
    E164PhoneNumber = field("E164PhoneNumber")
    Country = field("Country")
    Type = field("Type")
    ProductType = field("ProductType")
    Status = field("Status")

    @cached_property
    def Capabilities(self):  # pragma: no cover
        return PhoneNumberCapabilities.make_one(self.boto3_raw_data["Capabilities"])

    @cached_property
    def Associations(self):  # pragma: no cover
        return PhoneNumberAssociation.make_many(self.boto3_raw_data["Associations"])

    CallingName = field("CallingName")
    CallingNameStatus = field("CallingNameStatus")
    CreatedTimestamp = field("CreatedTimestamp")
    UpdatedTimestamp = field("UpdatedTimestamp")
    DeletionTimestamp = field("DeletionTimestamp")
    OrderId = field("OrderId")
    Name = field("Name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PhoneNumberTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PhoneNumberTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SpeakerSearchDetails:
    boto3_raw_data: "type_defs.SpeakerSearchDetailsTypeDef" = dataclasses.field()

    @cached_property
    def Results(self):  # pragma: no cover
        return SpeakerSearchResult.make_many(self.boto3_raw_data["Results"])

    VoiceprintGenerationStatus = field("VoiceprintGenerationStatus")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SpeakerSearchDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SpeakerSearchDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StreamingConfigurationOutput:
    boto3_raw_data: "type_defs.StreamingConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    DataRetentionInHours = field("DataRetentionInHours")
    Disabled = field("Disabled")

    @cached_property
    def StreamingNotificationTargets(self):  # pragma: no cover
        return StreamingNotificationTarget.make_many(
            self.boto3_raw_data["StreamingNotificationTargets"]
        )

    @cached_property
    def MediaInsightsConfiguration(self):  # pragma: no cover
        return MediaInsightsConfiguration.make_one(
            self.boto3_raw_data["MediaInsightsConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StreamingConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StreamingConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StreamingConfiguration:
    boto3_raw_data: "type_defs.StreamingConfigurationTypeDef" = dataclasses.field()

    DataRetentionInHours = field("DataRetentionInHours")
    Disabled = field("Disabled")

    @cached_property
    def StreamingNotificationTargets(self):  # pragma: no cover
        return StreamingNotificationTarget.make_many(
            self.boto3_raw_data["StreamingNotificationTargets"]
        )

    @cached_property
    def MediaInsightsConfiguration(self):  # pragma: no cover
        return MediaInsightsConfiguration.make_one(
            self.boto3_raw_data["MediaInsightsConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StreamingConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StreamingConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetVoiceToneAnalysisTaskResponse:
    boto3_raw_data: "type_defs.GetVoiceToneAnalysisTaskResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def VoiceToneAnalysisTask(self):  # pragma: no cover
        return VoiceToneAnalysisTask.make_one(
            self.boto3_raw_data["VoiceToneAnalysisTask"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetVoiceToneAnalysisTaskResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetVoiceToneAnalysisTaskResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartVoiceToneAnalysisTaskResponse:
    boto3_raw_data: "type_defs.StartVoiceToneAnalysisTaskResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def VoiceToneAnalysisTask(self):  # pragma: no cover
        return VoiceToneAnalysisTask.make_one(
            self.boto3_raw_data["VoiceToneAnalysisTask"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartVoiceToneAnalysisTaskResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartVoiceToneAnalysisTaskResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSipMediaApplicationResponse:
    boto3_raw_data: "type_defs.CreateSipMediaApplicationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def SipMediaApplication(self):  # pragma: no cover
        return SipMediaApplication.make_one(self.boto3_raw_data["SipMediaApplication"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateSipMediaApplicationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSipMediaApplicationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSipMediaApplicationResponse:
    boto3_raw_data: "type_defs.GetSipMediaApplicationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def SipMediaApplication(self):  # pragma: no cover
        return SipMediaApplication.make_one(self.boto3_raw_data["SipMediaApplication"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetSipMediaApplicationResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSipMediaApplicationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSipMediaApplicationsResponse:
    boto3_raw_data: "type_defs.ListSipMediaApplicationsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def SipMediaApplications(self):  # pragma: no cover
        return SipMediaApplication.make_many(
            self.boto3_raw_data["SipMediaApplications"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListSipMediaApplicationsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSipMediaApplicationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSipMediaApplicationResponse:
    boto3_raw_data: "type_defs.UpdateSipMediaApplicationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def SipMediaApplication(self):  # pragma: no cover
        return SipMediaApplication.make_one(self.boto3_raw_data["SipMediaApplication"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateSipMediaApplicationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSipMediaApplicationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSipRuleResponse:
    boto3_raw_data: "type_defs.CreateSipRuleResponseTypeDef" = dataclasses.field()

    @cached_property
    def SipRule(self):  # pragma: no cover
        return SipRule.make_one(self.boto3_raw_data["SipRule"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateSipRuleResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSipRuleResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSipRuleResponse:
    boto3_raw_data: "type_defs.GetSipRuleResponseTypeDef" = dataclasses.field()

    @cached_property
    def SipRule(self):  # pragma: no cover
        return SipRule.make_one(self.boto3_raw_data["SipRule"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSipRuleResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSipRuleResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSipRulesResponse:
    boto3_raw_data: "type_defs.ListSipRulesResponseTypeDef" = dataclasses.field()

    @cached_property
    def SipRules(self):  # pragma: no cover
        return SipRule.make_many(self.boto3_raw_data["SipRules"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSipRulesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSipRulesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSipRuleResponse:
    boto3_raw_data: "type_defs.UpdateSipRuleResponseTypeDef" = dataclasses.field()

    @cached_property
    def SipRule(self):  # pragma: no cover
        return SipRule.make_one(self.boto3_raw_data["SipRule"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateSipRuleResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSipRuleResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateVoiceConnectorGroupResponse:
    boto3_raw_data: "type_defs.CreateVoiceConnectorGroupResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def VoiceConnectorGroup(self):  # pragma: no cover
        return VoiceConnectorGroup.make_one(self.boto3_raw_data["VoiceConnectorGroup"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateVoiceConnectorGroupResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateVoiceConnectorGroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetVoiceConnectorGroupResponse:
    boto3_raw_data: "type_defs.GetVoiceConnectorGroupResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def VoiceConnectorGroup(self):  # pragma: no cover
        return VoiceConnectorGroup.make_one(self.boto3_raw_data["VoiceConnectorGroup"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetVoiceConnectorGroupResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetVoiceConnectorGroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListVoiceConnectorGroupsResponse:
    boto3_raw_data: "type_defs.ListVoiceConnectorGroupsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def VoiceConnectorGroups(self):  # pragma: no cover
        return VoiceConnectorGroup.make_many(
            self.boto3_raw_data["VoiceConnectorGroups"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListVoiceConnectorGroupsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListVoiceConnectorGroupsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateVoiceConnectorGroupResponse:
    boto3_raw_data: "type_defs.UpdateVoiceConnectorGroupResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def VoiceConnectorGroup(self):  # pragma: no cover
        return VoiceConnectorGroup.make_one(self.boto3_raw_data["VoiceConnectorGroup"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateVoiceConnectorGroupResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateVoiceConnectorGroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateVoiceProfileDomainResponse:
    boto3_raw_data: "type_defs.CreateVoiceProfileDomainResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def VoiceProfileDomain(self):  # pragma: no cover
        return VoiceProfileDomain.make_one(self.boto3_raw_data["VoiceProfileDomain"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateVoiceProfileDomainResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateVoiceProfileDomainResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetVoiceProfileDomainResponse:
    boto3_raw_data: "type_defs.GetVoiceProfileDomainResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def VoiceProfileDomain(self):  # pragma: no cover
        return VoiceProfileDomain.make_one(self.boto3_raw_data["VoiceProfileDomain"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetVoiceProfileDomainResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetVoiceProfileDomainResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateVoiceProfileDomainResponse:
    boto3_raw_data: "type_defs.UpdateVoiceProfileDomainResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def VoiceProfileDomain(self):  # pragma: no cover
        return VoiceProfileDomain.make_one(self.boto3_raw_data["VoiceProfileDomain"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateVoiceProfileDomainResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateVoiceProfileDomainResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetVoiceConnectorEmergencyCallingConfigurationResponse:
    boto3_raw_data: (
        "type_defs.GetVoiceConnectorEmergencyCallingConfigurationResponseTypeDef"
    ) = dataclasses.field()

    @cached_property
    def EmergencyCallingConfiguration(self):  # pragma: no cover
        return EmergencyCallingConfigurationOutput.make_one(
            self.boto3_raw_data["EmergencyCallingConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetVoiceConnectorEmergencyCallingConfigurationResponseTypeDef"
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
                "type_defs.GetVoiceConnectorEmergencyCallingConfigurationResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutVoiceConnectorEmergencyCallingConfigurationResponse:
    boto3_raw_data: (
        "type_defs.PutVoiceConnectorEmergencyCallingConfigurationResponseTypeDef"
    ) = dataclasses.field()

    @cached_property
    def EmergencyCallingConfiguration(self):  # pragma: no cover
        return EmergencyCallingConfigurationOutput.make_one(
            self.boto3_raw_data["EmergencyCallingConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutVoiceConnectorEmergencyCallingConfigurationResponseTypeDef"
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
                "type_defs.PutVoiceConnectorEmergencyCallingConfigurationResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePhoneNumberOrderResponse:
    boto3_raw_data: "type_defs.CreatePhoneNumberOrderResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PhoneNumberOrder(self):  # pragma: no cover
        return PhoneNumberOrder.make_one(self.boto3_raw_data["PhoneNumberOrder"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreatePhoneNumberOrderResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePhoneNumberOrderResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPhoneNumberOrderResponse:
    boto3_raw_data: "type_defs.GetPhoneNumberOrderResponseTypeDef" = dataclasses.field()

    @cached_property
    def PhoneNumberOrder(self):  # pragma: no cover
        return PhoneNumberOrder.make_one(self.boto3_raw_data["PhoneNumberOrder"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetPhoneNumberOrderResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPhoneNumberOrderResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPhoneNumberOrdersResponse:
    boto3_raw_data: "type_defs.ListPhoneNumberOrdersResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PhoneNumberOrders(self):  # pragma: no cover
        return PhoneNumberOrder.make_many(self.boto3_raw_data["PhoneNumberOrders"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListPhoneNumberOrdersResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPhoneNumberOrdersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetVoiceConnectorOriginationResponse:
    boto3_raw_data: "type_defs.GetVoiceConnectorOriginationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Origination(self):  # pragma: no cover
        return OriginationOutput.make_one(self.boto3_raw_data["Origination"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetVoiceConnectorOriginationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetVoiceConnectorOriginationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutVoiceConnectorOriginationResponse:
    boto3_raw_data: "type_defs.PutVoiceConnectorOriginationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Origination(self):  # pragma: no cover
        return OriginationOutput.make_one(self.boto3_raw_data["Origination"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutVoiceConnectorOriginationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutVoiceConnectorOriginationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateProxySessionResponse:
    boto3_raw_data: "type_defs.CreateProxySessionResponseTypeDef" = dataclasses.field()

    @cached_property
    def ProxySession(self):  # pragma: no cover
        return ProxySession.make_one(self.boto3_raw_data["ProxySession"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateProxySessionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateProxySessionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetProxySessionResponse:
    boto3_raw_data: "type_defs.GetProxySessionResponseTypeDef" = dataclasses.field()

    @cached_property
    def ProxySession(self):  # pragma: no cover
        return ProxySession.make_one(self.boto3_raw_data["ProxySession"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetProxySessionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetProxySessionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListProxySessionsResponse:
    boto3_raw_data: "type_defs.ListProxySessionsResponseTypeDef" = dataclasses.field()

    @cached_property
    def ProxySessions(self):  # pragma: no cover
        return ProxySession.make_many(self.boto3_raw_data["ProxySessions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListProxySessionsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListProxySessionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateProxySessionResponse:
    boto3_raw_data: "type_defs.UpdateProxySessionResponseTypeDef" = dataclasses.field()

    @cached_property
    def ProxySession(self):  # pragma: no cover
        return ProxySession.make_one(self.boto3_raw_data["ProxySession"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateProxySessionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateProxySessionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPhoneNumberResponse:
    boto3_raw_data: "type_defs.GetPhoneNumberResponseTypeDef" = dataclasses.field()

    @cached_property
    def PhoneNumber(self):  # pragma: no cover
        return PhoneNumber.make_one(self.boto3_raw_data["PhoneNumber"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetPhoneNumberResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPhoneNumberResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPhoneNumbersResponse:
    boto3_raw_data: "type_defs.ListPhoneNumbersResponseTypeDef" = dataclasses.field()

    @cached_property
    def PhoneNumbers(self):  # pragma: no cover
        return PhoneNumber.make_many(self.boto3_raw_data["PhoneNumbers"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPhoneNumbersResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPhoneNumbersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RestorePhoneNumberResponse:
    boto3_raw_data: "type_defs.RestorePhoneNumberResponseTypeDef" = dataclasses.field()

    @cached_property
    def PhoneNumber(self):  # pragma: no cover
        return PhoneNumber.make_one(self.boto3_raw_data["PhoneNumber"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RestorePhoneNumberResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RestorePhoneNumberResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdatePhoneNumberResponse:
    boto3_raw_data: "type_defs.UpdatePhoneNumberResponseTypeDef" = dataclasses.field()

    @cached_property
    def PhoneNumber(self):  # pragma: no cover
        return PhoneNumber.make_one(self.boto3_raw_data["PhoneNumber"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdatePhoneNumberResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePhoneNumberResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutSipMediaApplicationAlexaSkillConfigurationRequest:
    boto3_raw_data: (
        "type_defs.PutSipMediaApplicationAlexaSkillConfigurationRequestTypeDef"
    ) = dataclasses.field()

    SipMediaApplicationId = field("SipMediaApplicationId")
    SipMediaApplicationAlexaSkillConfiguration = field(
        "SipMediaApplicationAlexaSkillConfiguration"
    )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutSipMediaApplicationAlexaSkillConfigurationRequestTypeDef"
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
                "type_defs.PutSipMediaApplicationAlexaSkillConfigurationRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SpeakerSearchTask:
    boto3_raw_data: "type_defs.SpeakerSearchTaskTypeDef" = dataclasses.field()

    SpeakerSearchTaskId = field("SpeakerSearchTaskId")
    SpeakerSearchTaskStatus = field("SpeakerSearchTaskStatus")

    @cached_property
    def CallDetails(self):  # pragma: no cover
        return CallDetails.make_one(self.boto3_raw_data["CallDetails"])

    @cached_property
    def SpeakerSearchDetails(self):  # pragma: no cover
        return SpeakerSearchDetails.make_one(
            self.boto3_raw_data["SpeakerSearchDetails"]
        )

    CreatedTimestamp = field("CreatedTimestamp")
    UpdatedTimestamp = field("UpdatedTimestamp")
    StartedTimestamp = field("StartedTimestamp")
    StatusMessage = field("StatusMessage")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SpeakerSearchTaskTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SpeakerSearchTaskTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetVoiceConnectorStreamingConfigurationResponse:
    boto3_raw_data: (
        "type_defs.GetVoiceConnectorStreamingConfigurationResponseTypeDef"
    ) = dataclasses.field()

    @cached_property
    def StreamingConfiguration(self):  # pragma: no cover
        return StreamingConfigurationOutput.make_one(
            self.boto3_raw_data["StreamingConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetVoiceConnectorStreamingConfigurationResponseTypeDef"
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
                "type_defs.GetVoiceConnectorStreamingConfigurationResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutVoiceConnectorStreamingConfigurationResponse:
    boto3_raw_data: (
        "type_defs.PutVoiceConnectorStreamingConfigurationResponseTypeDef"
    ) = dataclasses.field()

    @cached_property
    def StreamingConfiguration(self):  # pragma: no cover
        return StreamingConfigurationOutput.make_one(
            self.boto3_raw_data["StreamingConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutVoiceConnectorStreamingConfigurationResponseTypeDef"
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
                "type_defs.PutVoiceConnectorStreamingConfigurationResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutVoiceConnectorTerminationRequest:
    boto3_raw_data: "type_defs.PutVoiceConnectorTerminationRequestTypeDef" = (
        dataclasses.field()
    )

    VoiceConnectorId = field("VoiceConnectorId")
    Termination = field("Termination")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutVoiceConnectorTerminationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutVoiceConnectorTerminationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutVoiceConnectorEmergencyCallingConfigurationRequest:
    boto3_raw_data: (
        "type_defs.PutVoiceConnectorEmergencyCallingConfigurationRequestTypeDef"
    ) = dataclasses.field()

    VoiceConnectorId = field("VoiceConnectorId")
    EmergencyCallingConfiguration = field("EmergencyCallingConfiguration")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutVoiceConnectorEmergencyCallingConfigurationRequestTypeDef"
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
                "type_defs.PutVoiceConnectorEmergencyCallingConfigurationRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutVoiceConnectorOriginationRequest:
    boto3_raw_data: "type_defs.PutVoiceConnectorOriginationRequestTypeDef" = (
        dataclasses.field()
    )

    VoiceConnectorId = field("VoiceConnectorId")
    Origination = field("Origination")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutVoiceConnectorOriginationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutVoiceConnectorOriginationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSpeakerSearchTaskResponse:
    boto3_raw_data: "type_defs.GetSpeakerSearchTaskResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def SpeakerSearchTask(self):  # pragma: no cover
        return SpeakerSearchTask.make_one(self.boto3_raw_data["SpeakerSearchTask"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSpeakerSearchTaskResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSpeakerSearchTaskResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartSpeakerSearchTaskResponse:
    boto3_raw_data: "type_defs.StartSpeakerSearchTaskResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def SpeakerSearchTask(self):  # pragma: no cover
        return SpeakerSearchTask.make_one(self.boto3_raw_data["SpeakerSearchTask"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartSpeakerSearchTaskResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartSpeakerSearchTaskResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutVoiceConnectorStreamingConfigurationRequest:
    boto3_raw_data: (
        "type_defs.PutVoiceConnectorStreamingConfigurationRequestTypeDef"
    ) = dataclasses.field()

    VoiceConnectorId = field("VoiceConnectorId")
    StreamingConfiguration = field("StreamingConfiguration")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutVoiceConnectorStreamingConfigurationRequestTypeDef"
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
                "type_defs.PutVoiceConnectorStreamingConfigurationRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
