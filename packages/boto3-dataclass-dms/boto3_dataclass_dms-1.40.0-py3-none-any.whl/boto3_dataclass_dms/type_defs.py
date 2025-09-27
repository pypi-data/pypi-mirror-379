# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_dms import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AccountQuota:
    boto3_raw_data: "type_defs.AccountQuotaTypeDef" = dataclasses.field()

    AccountQuotaName = field("AccountQuotaName")
    Used = field("Used")
    Max = field("Max")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AccountQuotaTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AccountQuotaTypeDef"]],
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
    ResourceArn = field("ResourceArn")

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
class ApplyPendingMaintenanceActionMessage:
    boto3_raw_data: "type_defs.ApplyPendingMaintenanceActionMessageTypeDef" = (
        dataclasses.field()
    )

    ReplicationInstanceArn = field("ReplicationInstanceArn")
    ApplyAction = field("ApplyAction")
    OptInType = field("OptInType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ApplyPendingMaintenanceActionMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ApplyPendingMaintenanceActionMessageTypeDef"]
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
class AvailabilityZone:
    boto3_raw_data: "type_defs.AvailabilityZoneTypeDef" = dataclasses.field()

    Name = field("Name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AvailabilityZoneTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AvailabilityZoneTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchStartRecommendationsErrorEntry:
    boto3_raw_data: "type_defs.BatchStartRecommendationsErrorEntryTypeDef" = (
        dataclasses.field()
    )

    DatabaseId = field("DatabaseId")
    Message = field("Message")
    Code = field("Code")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchStartRecommendationsErrorEntryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchStartRecommendationsErrorEntryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelReplicationTaskAssessmentRunMessage:
    boto3_raw_data: "type_defs.CancelReplicationTaskAssessmentRunMessageTypeDef" = (
        dataclasses.field()
    )

    ReplicationTaskAssessmentRunArn = field("ReplicationTaskAssessmentRunArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CancelReplicationTaskAssessmentRunMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelReplicationTaskAssessmentRunMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Certificate:
    boto3_raw_data: "type_defs.CertificateTypeDef" = dataclasses.field()

    CertificateIdentifier = field("CertificateIdentifier")
    CertificateCreationDate = field("CertificateCreationDate")
    CertificatePem = field("CertificatePem")
    CertificateWallet = field("CertificateWallet")
    CertificateArn = field("CertificateArn")
    CertificateOwner = field("CertificateOwner")
    ValidFromDate = field("ValidFromDate")
    ValidToDate = field("ValidToDate")
    SigningAlgorithm = field("SigningAlgorithm")
    KeyLength = field("KeyLength")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CertificateTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CertificateTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CollectorHealthCheck:
    boto3_raw_data: "type_defs.CollectorHealthCheckTypeDef" = dataclasses.field()

    CollectorStatus = field("CollectorStatus")
    LocalCollectorS3Access = field("LocalCollectorS3Access")
    WebCollectorS3Access = field("WebCollectorS3Access")
    WebCollectorGrantedRoleBasedAccess = field("WebCollectorGrantedRoleBasedAccess")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CollectorHealthCheckTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CollectorHealthCheckTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InventoryData:
    boto3_raw_data: "type_defs.InventoryDataTypeDef" = dataclasses.field()

    NumberOfDatabases = field("NumberOfDatabases")
    NumberOfSchemas = field("NumberOfSchemas")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InventoryDataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.InventoryDataTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CollectorShortInfoResponse:
    boto3_raw_data: "type_defs.CollectorShortInfoResponseTypeDef" = dataclasses.field()

    CollectorReferencedId = field("CollectorReferencedId")
    CollectorName = field("CollectorName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CollectorShortInfoResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CollectorShortInfoResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ComputeConfigOutput:
    boto3_raw_data: "type_defs.ComputeConfigOutputTypeDef" = dataclasses.field()

    AvailabilityZone = field("AvailabilityZone")
    DnsNameServers = field("DnsNameServers")
    KmsKeyId = field("KmsKeyId")
    MaxCapacityUnits = field("MaxCapacityUnits")
    MinCapacityUnits = field("MinCapacityUnits")
    MultiAZ = field("MultiAZ")
    PreferredMaintenanceWindow = field("PreferredMaintenanceWindow")
    ReplicationSubnetGroupId = field("ReplicationSubnetGroupId")
    VpcSecurityGroupIds = field("VpcSecurityGroupIds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ComputeConfigOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ComputeConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ComputeConfig:
    boto3_raw_data: "type_defs.ComputeConfigTypeDef" = dataclasses.field()

    AvailabilityZone = field("AvailabilityZone")
    DnsNameServers = field("DnsNameServers")
    KmsKeyId = field("KmsKeyId")
    MaxCapacityUnits = field("MaxCapacityUnits")
    MinCapacityUnits = field("MinCapacityUnits")
    MultiAZ = field("MultiAZ")
    PreferredMaintenanceWindow = field("PreferredMaintenanceWindow")
    ReplicationSubnetGroupId = field("ReplicationSubnetGroupId")
    VpcSecurityGroupIds = field("VpcSecurityGroupIds")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ComputeConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ComputeConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Connection:
    boto3_raw_data: "type_defs.ConnectionTypeDef" = dataclasses.field()

    ReplicationInstanceArn = field("ReplicationInstanceArn")
    EndpointArn = field("EndpointArn")
    Status = field("Status")
    LastFailureMessage = field("LastFailureMessage")
    EndpointIdentifier = field("EndpointIdentifier")
    ReplicationInstanceIdentifier = field("ReplicationInstanceIdentifier")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ConnectionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ConnectionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TargetDataSetting:
    boto3_raw_data: "type_defs.TargetDataSettingTypeDef" = dataclasses.field()

    TablePreparationMode = field("TablePreparationMode")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TargetDataSettingTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TargetDataSettingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DmsTransferSettings:
    boto3_raw_data: "type_defs.DmsTransferSettingsTypeDef" = dataclasses.field()

    ServiceAccessRoleArn = field("ServiceAccessRoleArn")
    BucketName = field("BucketName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DmsTransferSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DmsTransferSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DocDbSettings:
    boto3_raw_data: "type_defs.DocDbSettingsTypeDef" = dataclasses.field()

    Username = field("Username")
    Password = field("Password")
    ServerName = field("ServerName")
    Port = field("Port")
    DatabaseName = field("DatabaseName")
    NestingLevel = field("NestingLevel")
    ExtractDocId = field("ExtractDocId")
    DocsToInvestigate = field("DocsToInvestigate")
    KmsKeyId = field("KmsKeyId")
    SecretsManagerAccessRoleArn = field("SecretsManagerAccessRoleArn")
    SecretsManagerSecretId = field("SecretsManagerSecretId")
    UseUpdateLookUp = field("UseUpdateLookUp")
    ReplicateShardCollections = field("ReplicateShardCollections")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DocDbSettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DocDbSettingsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DynamoDbSettings:
    boto3_raw_data: "type_defs.DynamoDbSettingsTypeDef" = dataclasses.field()

    ServiceAccessRoleArn = field("ServiceAccessRoleArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DynamoDbSettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DynamoDbSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ElasticsearchSettings:
    boto3_raw_data: "type_defs.ElasticsearchSettingsTypeDef" = dataclasses.field()

    ServiceAccessRoleArn = field("ServiceAccessRoleArn")
    EndpointUri = field("EndpointUri")
    FullLoadErrorPercentage = field("FullLoadErrorPercentage")
    ErrorRetryDuration = field("ErrorRetryDuration")
    UseNewMappingType = field("UseNewMappingType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ElasticsearchSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ElasticsearchSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GcpMySQLSettings:
    boto3_raw_data: "type_defs.GcpMySQLSettingsTypeDef" = dataclasses.field()

    AfterConnectScript = field("AfterConnectScript")
    CleanSourceMetadataOnMismatch = field("CleanSourceMetadataOnMismatch")
    DatabaseName = field("DatabaseName")
    EventsPollInterval = field("EventsPollInterval")
    TargetDbType = field("TargetDbType")
    MaxFileSize = field("MaxFileSize")
    ParallelLoadThreads = field("ParallelLoadThreads")
    Password = field("Password")
    Port = field("Port")
    ServerName = field("ServerName")
    ServerTimezone = field("ServerTimezone")
    Username = field("Username")
    SecretsManagerAccessRoleArn = field("SecretsManagerAccessRoleArn")
    SecretsManagerSecretId = field("SecretsManagerSecretId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GcpMySQLSettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GcpMySQLSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IBMDb2Settings:
    boto3_raw_data: "type_defs.IBMDb2SettingsTypeDef" = dataclasses.field()

    DatabaseName = field("DatabaseName")
    Password = field("Password")
    Port = field("Port")
    ServerName = field("ServerName")
    SetDataCaptureChanges = field("SetDataCaptureChanges")
    CurrentLsn = field("CurrentLsn")
    MaxKBytesPerRead = field("MaxKBytesPerRead")
    Username = field("Username")
    SecretsManagerAccessRoleArn = field("SecretsManagerAccessRoleArn")
    SecretsManagerSecretId = field("SecretsManagerSecretId")
    LoadTimeout = field("LoadTimeout")
    WriteBufferSize = field("WriteBufferSize")
    MaxFileSize = field("MaxFileSize")
    KeepCsvFiles = field("KeepCsvFiles")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IBMDb2SettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.IBMDb2SettingsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KafkaSettings:
    boto3_raw_data: "type_defs.KafkaSettingsTypeDef" = dataclasses.field()

    Broker = field("Broker")
    Topic = field("Topic")
    MessageFormat = field("MessageFormat")
    IncludeTransactionDetails = field("IncludeTransactionDetails")
    IncludePartitionValue = field("IncludePartitionValue")
    PartitionIncludeSchemaTable = field("PartitionIncludeSchemaTable")
    IncludeTableAlterOperations = field("IncludeTableAlterOperations")
    IncludeControlDetails = field("IncludeControlDetails")
    MessageMaxBytes = field("MessageMaxBytes")
    IncludeNullAndEmpty = field("IncludeNullAndEmpty")
    SecurityProtocol = field("SecurityProtocol")
    SslClientCertificateArn = field("SslClientCertificateArn")
    SslClientKeyArn = field("SslClientKeyArn")
    SslClientKeyPassword = field("SslClientKeyPassword")
    SslCaCertificateArn = field("SslCaCertificateArn")
    SaslUsername = field("SaslUsername")
    SaslPassword = field("SaslPassword")
    NoHexPrefix = field("NoHexPrefix")
    SaslMechanism = field("SaslMechanism")
    SslEndpointIdentificationAlgorithm = field("SslEndpointIdentificationAlgorithm")
    UseLargeIntegerValue = field("UseLargeIntegerValue")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.KafkaSettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.KafkaSettingsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KinesisSettings:
    boto3_raw_data: "type_defs.KinesisSettingsTypeDef" = dataclasses.field()

    StreamArn = field("StreamArn")
    MessageFormat = field("MessageFormat")
    ServiceAccessRoleArn = field("ServiceAccessRoleArn")
    IncludeTransactionDetails = field("IncludeTransactionDetails")
    IncludePartitionValue = field("IncludePartitionValue")
    PartitionIncludeSchemaTable = field("PartitionIncludeSchemaTable")
    IncludeTableAlterOperations = field("IncludeTableAlterOperations")
    IncludeControlDetails = field("IncludeControlDetails")
    IncludeNullAndEmpty = field("IncludeNullAndEmpty")
    NoHexPrefix = field("NoHexPrefix")
    UseLargeIntegerValue = field("UseLargeIntegerValue")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.KinesisSettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.KinesisSettingsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MicrosoftSQLServerSettings:
    boto3_raw_data: "type_defs.MicrosoftSQLServerSettingsTypeDef" = dataclasses.field()

    Port = field("Port")
    BcpPacketSize = field("BcpPacketSize")
    DatabaseName = field("DatabaseName")
    ControlTablesFileGroup = field("ControlTablesFileGroup")
    Password = field("Password")
    QuerySingleAlwaysOnNode = field("QuerySingleAlwaysOnNode")
    ReadBackupOnly = field("ReadBackupOnly")
    SafeguardPolicy = field("SafeguardPolicy")
    ServerName = field("ServerName")
    Username = field("Username")
    UseBcpFullLoad = field("UseBcpFullLoad")
    UseThirdPartyBackupDevice = field("UseThirdPartyBackupDevice")
    SecretsManagerAccessRoleArn = field("SecretsManagerAccessRoleArn")
    SecretsManagerSecretId = field("SecretsManagerSecretId")
    TrimSpaceInChar = field("TrimSpaceInChar")
    TlogAccessMode = field("TlogAccessMode")
    ForceLobLookup = field("ForceLobLookup")
    AuthenticationMethod = field("AuthenticationMethod")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MicrosoftSQLServerSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MicrosoftSQLServerSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MongoDbSettings:
    boto3_raw_data: "type_defs.MongoDbSettingsTypeDef" = dataclasses.field()

    Username = field("Username")
    Password = field("Password")
    ServerName = field("ServerName")
    Port = field("Port")
    DatabaseName = field("DatabaseName")
    AuthType = field("AuthType")
    AuthMechanism = field("AuthMechanism")
    NestingLevel = field("NestingLevel")
    ExtractDocId = field("ExtractDocId")
    DocsToInvestigate = field("DocsToInvestigate")
    AuthSource = field("AuthSource")
    KmsKeyId = field("KmsKeyId")
    SecretsManagerAccessRoleArn = field("SecretsManagerAccessRoleArn")
    SecretsManagerSecretId = field("SecretsManagerSecretId")
    UseUpdateLookUp = field("UseUpdateLookUp")
    ReplicateShardCollections = field("ReplicateShardCollections")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MongoDbSettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MongoDbSettingsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MySQLSettings:
    boto3_raw_data: "type_defs.MySQLSettingsTypeDef" = dataclasses.field()

    AfterConnectScript = field("AfterConnectScript")
    CleanSourceMetadataOnMismatch = field("CleanSourceMetadataOnMismatch")
    DatabaseName = field("DatabaseName")
    EventsPollInterval = field("EventsPollInterval")
    TargetDbType = field("TargetDbType")
    MaxFileSize = field("MaxFileSize")
    ParallelLoadThreads = field("ParallelLoadThreads")
    Password = field("Password")
    Port = field("Port")
    ServerName = field("ServerName")
    ServerTimezone = field("ServerTimezone")
    Username = field("Username")
    SecretsManagerAccessRoleArn = field("SecretsManagerAccessRoleArn")
    SecretsManagerSecretId = field("SecretsManagerSecretId")
    ExecuteTimeout = field("ExecuteTimeout")
    ServiceAccessRoleArn = field("ServiceAccessRoleArn")
    AuthenticationMethod = field("AuthenticationMethod")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MySQLSettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MySQLSettingsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NeptuneSettings:
    boto3_raw_data: "type_defs.NeptuneSettingsTypeDef" = dataclasses.field()

    S3BucketName = field("S3BucketName")
    S3BucketFolder = field("S3BucketFolder")
    ServiceAccessRoleArn = field("ServiceAccessRoleArn")
    ErrorRetryDuration = field("ErrorRetryDuration")
    MaxFileSize = field("MaxFileSize")
    MaxRetryCount = field("MaxRetryCount")
    IamAuthEnabled = field("IamAuthEnabled")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.NeptuneSettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.NeptuneSettingsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PostgreSQLSettings:
    boto3_raw_data: "type_defs.PostgreSQLSettingsTypeDef" = dataclasses.field()

    AfterConnectScript = field("AfterConnectScript")
    CaptureDdls = field("CaptureDdls")
    MaxFileSize = field("MaxFileSize")
    DatabaseName = field("DatabaseName")
    DdlArtifactsSchema = field("DdlArtifactsSchema")
    ExecuteTimeout = field("ExecuteTimeout")
    FailTasksOnLobTruncation = field("FailTasksOnLobTruncation")
    HeartbeatEnable = field("HeartbeatEnable")
    HeartbeatSchema = field("HeartbeatSchema")
    HeartbeatFrequency = field("HeartbeatFrequency")
    Password = field("Password")
    Port = field("Port")
    ServerName = field("ServerName")
    Username = field("Username")
    SlotName = field("SlotName")
    PluginName = field("PluginName")
    SecretsManagerAccessRoleArn = field("SecretsManagerAccessRoleArn")
    SecretsManagerSecretId = field("SecretsManagerSecretId")
    TrimSpaceInChar = field("TrimSpaceInChar")
    MapBooleanAsBoolean = field("MapBooleanAsBoolean")
    MapJsonbAsClob = field("MapJsonbAsClob")
    MapLongVarcharAs = field("MapLongVarcharAs")
    DatabaseMode = field("DatabaseMode")
    BabelfishDatabaseName = field("BabelfishDatabaseName")
    DisableUnicodeSourceFilter = field("DisableUnicodeSourceFilter")
    ServiceAccessRoleArn = field("ServiceAccessRoleArn")
    AuthenticationMethod = field("AuthenticationMethod")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PostgreSQLSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PostgreSQLSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RedisSettings:
    boto3_raw_data: "type_defs.RedisSettingsTypeDef" = dataclasses.field()

    ServerName = field("ServerName")
    Port = field("Port")
    SslSecurityProtocol = field("SslSecurityProtocol")
    AuthType = field("AuthType")
    AuthUserName = field("AuthUserName")
    AuthPassword = field("AuthPassword")
    SslCaCertificateArn = field("SslCaCertificateArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RedisSettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RedisSettingsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RedshiftSettings:
    boto3_raw_data: "type_defs.RedshiftSettingsTypeDef" = dataclasses.field()

    AcceptAnyDate = field("AcceptAnyDate")
    AfterConnectScript = field("AfterConnectScript")
    BucketFolder = field("BucketFolder")
    BucketName = field("BucketName")
    CaseSensitiveNames = field("CaseSensitiveNames")
    CompUpdate = field("CompUpdate")
    ConnectionTimeout = field("ConnectionTimeout")
    DatabaseName = field("DatabaseName")
    DateFormat = field("DateFormat")
    EmptyAsNull = field("EmptyAsNull")
    EncryptionMode = field("EncryptionMode")
    ExplicitIds = field("ExplicitIds")
    FileTransferUploadStreams = field("FileTransferUploadStreams")
    LoadTimeout = field("LoadTimeout")
    MaxFileSize = field("MaxFileSize")
    Password = field("Password")
    Port = field("Port")
    RemoveQuotes = field("RemoveQuotes")
    ReplaceInvalidChars = field("ReplaceInvalidChars")
    ReplaceChars = field("ReplaceChars")
    ServerName = field("ServerName")
    ServiceAccessRoleArn = field("ServiceAccessRoleArn")
    ServerSideEncryptionKmsKeyId = field("ServerSideEncryptionKmsKeyId")
    TimeFormat = field("TimeFormat")
    TrimBlanks = field("TrimBlanks")
    TruncateColumns = field("TruncateColumns")
    Username = field("Username")
    WriteBufferSize = field("WriteBufferSize")
    SecretsManagerAccessRoleArn = field("SecretsManagerAccessRoleArn")
    SecretsManagerSecretId = field("SecretsManagerSecretId")
    MapBooleanAsBoolean = field("MapBooleanAsBoolean")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RedshiftSettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RedshiftSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3Settings:
    boto3_raw_data: "type_defs.S3SettingsTypeDef" = dataclasses.field()

    ServiceAccessRoleArn = field("ServiceAccessRoleArn")
    ExternalTableDefinition = field("ExternalTableDefinition")
    CsvRowDelimiter = field("CsvRowDelimiter")
    CsvDelimiter = field("CsvDelimiter")
    BucketFolder = field("BucketFolder")
    BucketName = field("BucketName")
    CompressionType = field("CompressionType")
    EncryptionMode = field("EncryptionMode")
    ServerSideEncryptionKmsKeyId = field("ServerSideEncryptionKmsKeyId")
    DataFormat = field("DataFormat")
    EncodingType = field("EncodingType")
    DictPageSizeLimit = field("DictPageSizeLimit")
    RowGroupLength = field("RowGroupLength")
    DataPageSize = field("DataPageSize")
    ParquetVersion = field("ParquetVersion")
    EnableStatistics = field("EnableStatistics")
    IncludeOpForFullLoad = field("IncludeOpForFullLoad")
    CdcInsertsOnly = field("CdcInsertsOnly")
    TimestampColumnName = field("TimestampColumnName")
    ParquetTimestampInMillisecond = field("ParquetTimestampInMillisecond")
    CdcInsertsAndUpdates = field("CdcInsertsAndUpdates")
    DatePartitionEnabled = field("DatePartitionEnabled")
    DatePartitionSequence = field("DatePartitionSequence")
    DatePartitionDelimiter = field("DatePartitionDelimiter")
    UseCsvNoSupValue = field("UseCsvNoSupValue")
    CsvNoSupValue = field("CsvNoSupValue")
    PreserveTransactions = field("PreserveTransactions")
    CdcPath = field("CdcPath")
    UseTaskStartTimeForFullLoadTimestamp = field("UseTaskStartTimeForFullLoadTimestamp")
    CannedAclForObjects = field("CannedAclForObjects")
    AddColumnName = field("AddColumnName")
    CdcMaxBatchInterval = field("CdcMaxBatchInterval")
    CdcMinFileSize = field("CdcMinFileSize")
    CsvNullValue = field("CsvNullValue")
    IgnoreHeaderRows = field("IgnoreHeaderRows")
    MaxFileSize = field("MaxFileSize")
    Rfc4180 = field("Rfc4180")
    DatePartitionTimezone = field("DatePartitionTimezone")
    AddTrailingPaddingCharacter = field("AddTrailingPaddingCharacter")
    ExpectedBucketOwner = field("ExpectedBucketOwner")
    GlueCatalogGeneration = field("GlueCatalogGeneration")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.S3SettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.S3SettingsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SybaseSettings:
    boto3_raw_data: "type_defs.SybaseSettingsTypeDef" = dataclasses.field()

    DatabaseName = field("DatabaseName")
    Password = field("Password")
    Port = field("Port")
    ServerName = field("ServerName")
    Username = field("Username")
    SecretsManagerAccessRoleArn = field("SecretsManagerAccessRoleArn")
    SecretsManagerSecretId = field("SecretsManagerSecretId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SybaseSettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SybaseSettingsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TimestreamSettings:
    boto3_raw_data: "type_defs.TimestreamSettingsTypeDef" = dataclasses.field()

    DatabaseName = field("DatabaseName")
    MemoryDuration = field("MemoryDuration")
    MagneticDuration = field("MagneticDuration")
    CdcInsertsAndUpdates = field("CdcInsertsAndUpdates")
    EnableMagneticStoreWrites = field("EnableMagneticStoreWrites")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TimestreamSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TimestreamSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EventSubscription:
    boto3_raw_data: "type_defs.EventSubscriptionTypeDef" = dataclasses.field()

    CustomerAwsId = field("CustomerAwsId")
    CustSubscriptionId = field("CustSubscriptionId")
    SnsTopicArn = field("SnsTopicArn")
    Status = field("Status")
    SubscriptionCreationTime = field("SubscriptionCreationTime")
    SourceType = field("SourceType")
    SourceIdsList = field("SourceIdsList")
    EventCategoriesList = field("EventCategoriesList")
    Enabled = field("Enabled")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EventSubscriptionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EventSubscriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateFleetAdvisorCollectorRequest:
    boto3_raw_data: "type_defs.CreateFleetAdvisorCollectorRequestTypeDef" = (
        dataclasses.field()
    )

    CollectorName = field("CollectorName")
    ServiceAccessRoleArn = field("ServiceAccessRoleArn")
    S3BucketName = field("S3BucketName")
    Description = field("Description")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateFleetAdvisorCollectorRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateFleetAdvisorCollectorRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstanceProfile:
    boto3_raw_data: "type_defs.InstanceProfileTypeDef" = dataclasses.field()

    InstanceProfileArn = field("InstanceProfileArn")
    AvailabilityZone = field("AvailabilityZone")
    KmsKeyArn = field("KmsKeyArn")
    PubliclyAccessible = field("PubliclyAccessible")
    NetworkType = field("NetworkType")
    InstanceProfileName = field("InstanceProfileName")
    Description = field("Description")
    InstanceProfileCreationTime = field("InstanceProfileCreationTime")
    SubnetGroupIdentifier = field("SubnetGroupIdentifier")
    VpcSecurityGroups = field("VpcSecurityGroups")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InstanceProfileTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.InstanceProfileTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataProviderDescriptorDefinition:
    boto3_raw_data: "type_defs.DataProviderDescriptorDefinitionTypeDef" = (
        dataclasses.field()
    )

    DataProviderIdentifier = field("DataProviderIdentifier")
    SecretsManagerSecretId = field("SecretsManagerSecretId")
    SecretsManagerAccessRoleArn = field("SecretsManagerAccessRoleArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DataProviderDescriptorDefinitionTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataProviderDescriptorDefinitionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SCApplicationAttributes:
    boto3_raw_data: "type_defs.SCApplicationAttributesTypeDef" = dataclasses.field()

    S3BucketPath = field("S3BucketPath")
    S3BucketRoleArn = field("S3BucketRoleArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SCApplicationAttributesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SCApplicationAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KerberosAuthenticationSettings:
    boto3_raw_data: "type_defs.KerberosAuthenticationSettingsTypeDef" = (
        dataclasses.field()
    )

    KeyCacheSecretId = field("KeyCacheSecretId")
    KeyCacheSecretIamArn = field("KeyCacheSecretIamArn")
    Krb5FileContents = field("Krb5FileContents")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.KerberosAuthenticationSettingsTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KerberosAuthenticationSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataMigrationSettings:
    boto3_raw_data: "type_defs.DataMigrationSettingsTypeDef" = dataclasses.field()

    NumberOfJobs = field("NumberOfJobs")
    CloudwatchLogsEnabled = field("CloudwatchLogsEnabled")
    SelectionRules = field("SelectionRules")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DataMigrationSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataMigrationSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataMigrationStatistics:
    boto3_raw_data: "type_defs.DataMigrationStatisticsTypeDef" = dataclasses.field()

    TablesLoaded = field("TablesLoaded")
    ElapsedTimeMillis = field("ElapsedTimeMillis")
    TablesLoading = field("TablesLoading")
    FullLoadPercentage = field("FullLoadPercentage")
    CDCLatency = field("CDCLatency")
    TablesQueued = field("TablesQueued")
    TablesErrored = field("TablesErrored")
    StartTime = field("StartTime")
    StopTime = field("StopTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DataMigrationStatisticsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataMigrationStatisticsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SourceDataSettingOutput:
    boto3_raw_data: "type_defs.SourceDataSettingOutputTypeDef" = dataclasses.field()

    CDCStartPosition = field("CDCStartPosition")
    CDCStartTime = field("CDCStartTime")
    CDCStopTime = field("CDCStopTime")
    SlotName = field("SlotName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SourceDataSettingOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SourceDataSettingOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataProviderDescriptor:
    boto3_raw_data: "type_defs.DataProviderDescriptorTypeDef" = dataclasses.field()

    SecretsManagerSecretId = field("SecretsManagerSecretId")
    SecretsManagerAccessRoleArn = field("SecretsManagerAccessRoleArn")
    DataProviderName = field("DataProviderName")
    DataProviderArn = field("DataProviderArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DataProviderDescriptorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataProviderDescriptorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DocDbDataProviderSettings:
    boto3_raw_data: "type_defs.DocDbDataProviderSettingsTypeDef" = dataclasses.field()

    ServerName = field("ServerName")
    Port = field("Port")
    DatabaseName = field("DatabaseName")
    SslMode = field("SslMode")
    CertificateArn = field("CertificateArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DocDbDataProviderSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DocDbDataProviderSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IbmDb2LuwDataProviderSettings:
    boto3_raw_data: "type_defs.IbmDb2LuwDataProviderSettingsTypeDef" = (
        dataclasses.field()
    )

    ServerName = field("ServerName")
    Port = field("Port")
    DatabaseName = field("DatabaseName")
    SslMode = field("SslMode")
    CertificateArn = field("CertificateArn")
    S3Path = field("S3Path")
    S3AccessRoleArn = field("S3AccessRoleArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.IbmDb2LuwDataProviderSettingsTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IbmDb2LuwDataProviderSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IbmDb2zOsDataProviderSettings:
    boto3_raw_data: "type_defs.IbmDb2zOsDataProviderSettingsTypeDef" = (
        dataclasses.field()
    )

    ServerName = field("ServerName")
    Port = field("Port")
    DatabaseName = field("DatabaseName")
    SslMode = field("SslMode")
    CertificateArn = field("CertificateArn")
    S3Path = field("S3Path")
    S3AccessRoleArn = field("S3AccessRoleArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.IbmDb2zOsDataProviderSettingsTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IbmDb2zOsDataProviderSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MariaDbDataProviderSettings:
    boto3_raw_data: "type_defs.MariaDbDataProviderSettingsTypeDef" = dataclasses.field()

    ServerName = field("ServerName")
    Port = field("Port")
    SslMode = field("SslMode")
    CertificateArn = field("CertificateArn")
    S3Path = field("S3Path")
    S3AccessRoleArn = field("S3AccessRoleArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MariaDbDataProviderSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MariaDbDataProviderSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MicrosoftSqlServerDataProviderSettings:
    boto3_raw_data: "type_defs.MicrosoftSqlServerDataProviderSettingsTypeDef" = (
        dataclasses.field()
    )

    ServerName = field("ServerName")
    Port = field("Port")
    DatabaseName = field("DatabaseName")
    SslMode = field("SslMode")
    CertificateArn = field("CertificateArn")
    S3Path = field("S3Path")
    S3AccessRoleArn = field("S3AccessRoleArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.MicrosoftSqlServerDataProviderSettingsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MicrosoftSqlServerDataProviderSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MongoDbDataProviderSettings:
    boto3_raw_data: "type_defs.MongoDbDataProviderSettingsTypeDef" = dataclasses.field()

    ServerName = field("ServerName")
    Port = field("Port")
    DatabaseName = field("DatabaseName")
    SslMode = field("SslMode")
    CertificateArn = field("CertificateArn")
    AuthType = field("AuthType")
    AuthSource = field("AuthSource")
    AuthMechanism = field("AuthMechanism")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MongoDbDataProviderSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MongoDbDataProviderSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MySqlDataProviderSettings:
    boto3_raw_data: "type_defs.MySqlDataProviderSettingsTypeDef" = dataclasses.field()

    ServerName = field("ServerName")
    Port = field("Port")
    SslMode = field("SslMode")
    CertificateArn = field("CertificateArn")
    S3Path = field("S3Path")
    S3AccessRoleArn = field("S3AccessRoleArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MySqlDataProviderSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MySqlDataProviderSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OracleDataProviderSettings:
    boto3_raw_data: "type_defs.OracleDataProviderSettingsTypeDef" = dataclasses.field()

    ServerName = field("ServerName")
    Port = field("Port")
    DatabaseName = field("DatabaseName")
    SslMode = field("SslMode")
    CertificateArn = field("CertificateArn")
    AsmServer = field("AsmServer")
    SecretsManagerOracleAsmSecretId = field("SecretsManagerOracleAsmSecretId")
    SecretsManagerOracleAsmAccessRoleArn = field("SecretsManagerOracleAsmAccessRoleArn")
    SecretsManagerSecurityDbEncryptionSecretId = field(
        "SecretsManagerSecurityDbEncryptionSecretId"
    )
    SecretsManagerSecurityDbEncryptionAccessRoleArn = field(
        "SecretsManagerSecurityDbEncryptionAccessRoleArn"
    )
    S3Path = field("S3Path")
    S3AccessRoleArn = field("S3AccessRoleArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OracleDataProviderSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OracleDataProviderSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PostgreSqlDataProviderSettings:
    boto3_raw_data: "type_defs.PostgreSqlDataProviderSettingsTypeDef" = (
        dataclasses.field()
    )

    ServerName = field("ServerName")
    Port = field("Port")
    DatabaseName = field("DatabaseName")
    SslMode = field("SslMode")
    CertificateArn = field("CertificateArn")
    S3Path = field("S3Path")
    S3AccessRoleArn = field("S3AccessRoleArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PostgreSqlDataProviderSettingsTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PostgreSqlDataProviderSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RedshiftDataProviderSettings:
    boto3_raw_data: "type_defs.RedshiftDataProviderSettingsTypeDef" = (
        dataclasses.field()
    )

    ServerName = field("ServerName")
    Port = field("Port")
    DatabaseName = field("DatabaseName")
    S3Path = field("S3Path")
    S3AccessRoleArn = field("S3AccessRoleArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RedshiftDataProviderSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RedshiftDataProviderSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DatabaseInstanceSoftwareDetailsResponse:
    boto3_raw_data: "type_defs.DatabaseInstanceSoftwareDetailsResponseTypeDef" = (
        dataclasses.field()
    )

    Engine = field("Engine")
    EngineVersion = field("EngineVersion")
    EngineEdition = field("EngineEdition")
    ServicePack = field("ServicePack")
    SupportLevel = field("SupportLevel")
    OsArchitecture = field("OsArchitecture")
    Tooltip = field("Tooltip")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DatabaseInstanceSoftwareDetailsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DatabaseInstanceSoftwareDetailsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServerShortInfoResponse:
    boto3_raw_data: "type_defs.ServerShortInfoResponseTypeDef" = dataclasses.field()

    ServerId = field("ServerId")
    IpAddress = field("IpAddress")
    ServerName = field("ServerName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ServerShortInfoResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServerShortInfoResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DatabaseShortInfoResponse:
    boto3_raw_data: "type_defs.DatabaseShortInfoResponseTypeDef" = dataclasses.field()

    DatabaseId = field("DatabaseId")
    DatabaseName = field("DatabaseName")
    DatabaseIpAddress = field("DatabaseIpAddress")
    DatabaseEngine = field("DatabaseEngine")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DatabaseShortInfoResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DatabaseShortInfoResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DefaultErrorDetails:
    boto3_raw_data: "type_defs.DefaultErrorDetailsTypeDef" = dataclasses.field()

    Message = field("Message")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DefaultErrorDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DefaultErrorDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteCertificateMessage:
    boto3_raw_data: "type_defs.DeleteCertificateMessageTypeDef" = dataclasses.field()

    CertificateArn = field("CertificateArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteCertificateMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteCertificateMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteCollectorRequest:
    boto3_raw_data: "type_defs.DeleteCollectorRequestTypeDef" = dataclasses.field()

    CollectorReferencedId = field("CollectorReferencedId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteCollectorRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteCollectorRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteConnectionMessage:
    boto3_raw_data: "type_defs.DeleteConnectionMessageTypeDef" = dataclasses.field()

    EndpointArn = field("EndpointArn")
    ReplicationInstanceArn = field("ReplicationInstanceArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteConnectionMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteConnectionMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDataMigrationMessage:
    boto3_raw_data: "type_defs.DeleteDataMigrationMessageTypeDef" = dataclasses.field()

    DataMigrationIdentifier = field("DataMigrationIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDataMigrationMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDataMigrationMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDataProviderMessage:
    boto3_raw_data: "type_defs.DeleteDataProviderMessageTypeDef" = dataclasses.field()

    DataProviderIdentifier = field("DataProviderIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDataProviderMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDataProviderMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteEndpointMessage:
    boto3_raw_data: "type_defs.DeleteEndpointMessageTypeDef" = dataclasses.field()

    EndpointArn = field("EndpointArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteEndpointMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteEndpointMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteEventSubscriptionMessage:
    boto3_raw_data: "type_defs.DeleteEventSubscriptionMessageTypeDef" = (
        dataclasses.field()
    )

    SubscriptionName = field("SubscriptionName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteEventSubscriptionMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteEventSubscriptionMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteFleetAdvisorDatabasesRequest:
    boto3_raw_data: "type_defs.DeleteFleetAdvisorDatabasesRequestTypeDef" = (
        dataclasses.field()
    )

    DatabaseIds = field("DatabaseIds")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteFleetAdvisorDatabasesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteFleetAdvisorDatabasesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteInstanceProfileMessage:
    boto3_raw_data: "type_defs.DeleteInstanceProfileMessageTypeDef" = (
        dataclasses.field()
    )

    InstanceProfileIdentifier = field("InstanceProfileIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteInstanceProfileMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteInstanceProfileMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteMigrationProjectMessage:
    boto3_raw_data: "type_defs.DeleteMigrationProjectMessageTypeDef" = (
        dataclasses.field()
    )

    MigrationProjectIdentifier = field("MigrationProjectIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteMigrationProjectMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteMigrationProjectMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteReplicationConfigMessage:
    boto3_raw_data: "type_defs.DeleteReplicationConfigMessageTypeDef" = (
        dataclasses.field()
    )

    ReplicationConfigArn = field("ReplicationConfigArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteReplicationConfigMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteReplicationConfigMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteReplicationInstanceMessage:
    boto3_raw_data: "type_defs.DeleteReplicationInstanceMessageTypeDef" = (
        dataclasses.field()
    )

    ReplicationInstanceArn = field("ReplicationInstanceArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteReplicationInstanceMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteReplicationInstanceMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteReplicationSubnetGroupMessage:
    boto3_raw_data: "type_defs.DeleteReplicationSubnetGroupMessageTypeDef" = (
        dataclasses.field()
    )

    ReplicationSubnetGroupIdentifier = field("ReplicationSubnetGroupIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteReplicationSubnetGroupMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteReplicationSubnetGroupMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteReplicationTaskAssessmentRunMessage:
    boto3_raw_data: "type_defs.DeleteReplicationTaskAssessmentRunMessageTypeDef" = (
        dataclasses.field()
    )

    ReplicationTaskAssessmentRunArn = field("ReplicationTaskAssessmentRunArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteReplicationTaskAssessmentRunMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteReplicationTaskAssessmentRunMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteReplicationTaskMessage:
    boto3_raw_data: "type_defs.DeleteReplicationTaskMessageTypeDef" = (
        dataclasses.field()
    )

    ReplicationTaskArn = field("ReplicationTaskArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteReplicationTaskMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteReplicationTaskMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeApplicableIndividualAssessmentsMessage:
    boto3_raw_data: (
        "type_defs.DescribeApplicableIndividualAssessmentsMessageTypeDef"
    ) = dataclasses.field()

    ReplicationTaskArn = field("ReplicationTaskArn")
    ReplicationInstanceArn = field("ReplicationInstanceArn")
    ReplicationConfigArn = field("ReplicationConfigArn")
    SourceEngineName = field("SourceEngineName")
    TargetEngineName = field("TargetEngineName")
    MigrationType = field("MigrationType")
    MaxRecords = field("MaxRecords")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeApplicableIndividualAssessmentsMessageTypeDef"
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
                "type_defs.DescribeApplicableIndividualAssessmentsMessageTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Filter:
    boto3_raw_data: "type_defs.FilterTypeDef" = dataclasses.field()

    Name = field("Name")
    Values = field("Values")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FilterTypeDef"]]
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
class WaiterConfig:
    boto3_raw_data: "type_defs.WaiterConfigTypeDef" = dataclasses.field()

    Delay = field("Delay")
    MaxAttempts = field("MaxAttempts")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WaiterConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.WaiterConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeConversionConfigurationMessage:
    boto3_raw_data: "type_defs.DescribeConversionConfigurationMessageTypeDef" = (
        dataclasses.field()
    )

    MigrationProjectIdentifier = field("MigrationProjectIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeConversionConfigurationMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeConversionConfigurationMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEndpointSettingsMessage:
    boto3_raw_data: "type_defs.DescribeEndpointSettingsMessageTypeDef" = (
        dataclasses.field()
    )

    EngineName = field("EngineName")
    MaxRecords = field("MaxRecords")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeEndpointSettingsMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEndpointSettingsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EndpointSetting:
    boto3_raw_data: "type_defs.EndpointSettingTypeDef" = dataclasses.field()

    Name = field("Name")
    Type = field("Type")
    EnumValues = field("EnumValues")
    Sensitive = field("Sensitive")
    Units = field("Units")
    Applicability = field("Applicability")
    IntValueMin = field("IntValueMin")
    IntValueMax = field("IntValueMax")
    DefaultValue = field("DefaultValue")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EndpointSettingTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EndpointSettingTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SupportedEndpointType:
    boto3_raw_data: "type_defs.SupportedEndpointTypeTypeDef" = dataclasses.field()

    EngineName = field("EngineName")
    SupportsCDC = field("SupportsCDC")
    EndpointType = field("EndpointType")
    ReplicationInstanceEngineMinimumVersion = field(
        "ReplicationInstanceEngineMinimumVersion"
    )
    EngineDisplayName = field("EngineDisplayName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SupportedEndpointTypeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SupportedEndpointTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEngineVersionsMessage:
    boto3_raw_data: "type_defs.DescribeEngineVersionsMessageTypeDef" = (
        dataclasses.field()
    )

    MaxRecords = field("MaxRecords")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeEngineVersionsMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEngineVersionsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EngineVersion:
    boto3_raw_data: "type_defs.EngineVersionTypeDef" = dataclasses.field()

    Version = field("Version")
    Lifecycle = field("Lifecycle")
    ReleaseStatus = field("ReleaseStatus")
    LaunchDate = field("LaunchDate")
    AutoUpgradeDate = field("AutoUpgradeDate")
    DeprecationDate = field("DeprecationDate")
    ForceUpgradeDate = field("ForceUpgradeDate")
    AvailableUpgrades = field("AvailableUpgrades")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EngineVersionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EngineVersionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EventCategoryGroup:
    boto3_raw_data: "type_defs.EventCategoryGroupTypeDef" = dataclasses.field()

    SourceType = field("SourceType")
    EventCategories = field("EventCategories")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EventCategoryGroupTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EventCategoryGroupTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Event:
    boto3_raw_data: "type_defs.EventTypeDef" = dataclasses.field()

    SourceIdentifier = field("SourceIdentifier")
    SourceType = field("SourceType")
    Message = field("Message")
    EventCategories = field("EventCategories")
    Date = field("Date")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EventTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EventTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFleetAdvisorLsaAnalysisRequest:
    boto3_raw_data: "type_defs.DescribeFleetAdvisorLsaAnalysisRequestTypeDef" = (
        dataclasses.field()
    )

    MaxRecords = field("MaxRecords")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeFleetAdvisorLsaAnalysisRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFleetAdvisorLsaAnalysisRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FleetAdvisorLsaAnalysisResponse:
    boto3_raw_data: "type_defs.FleetAdvisorLsaAnalysisResponseTypeDef" = (
        dataclasses.field()
    )

    LsaAnalysisId = field("LsaAnalysisId")
    Status = field("Status")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.FleetAdvisorLsaAnalysisResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FleetAdvisorLsaAnalysisResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FleetAdvisorSchemaObjectResponse:
    boto3_raw_data: "type_defs.FleetAdvisorSchemaObjectResponseTypeDef" = (
        dataclasses.field()
    )

    SchemaId = field("SchemaId")
    ObjectType = field("ObjectType")
    NumberOfObjects = field("NumberOfObjects")
    CodeLineCount = field("CodeLineCount")
    CodeSize = field("CodeSize")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.FleetAdvisorSchemaObjectResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FleetAdvisorSchemaObjectResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeOrderableReplicationInstancesMessage:
    boto3_raw_data: "type_defs.DescribeOrderableReplicationInstancesMessageTypeDef" = (
        dataclasses.field()
    )

    MaxRecords = field("MaxRecords")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeOrderableReplicationInstancesMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeOrderableReplicationInstancesMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OrderableReplicationInstance:
    boto3_raw_data: "type_defs.OrderableReplicationInstanceTypeDef" = (
        dataclasses.field()
    )

    EngineVersion = field("EngineVersion")
    ReplicationInstanceClass = field("ReplicationInstanceClass")
    StorageType = field("StorageType")
    MinAllocatedStorage = field("MinAllocatedStorage")
    MaxAllocatedStorage = field("MaxAllocatedStorage")
    DefaultAllocatedStorage = field("DefaultAllocatedStorage")
    IncludedAllocatedStorage = field("IncludedAllocatedStorage")
    AvailabilityZones = field("AvailabilityZones")
    ReleaseStatus = field("ReleaseStatus")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OrderableReplicationInstanceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OrderableReplicationInstanceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Limitation:
    boto3_raw_data: "type_defs.LimitationTypeDef" = dataclasses.field()

    DatabaseId = field("DatabaseId")
    EngineName = field("EngineName")
    Name = field("Name")
    Description = field("Description")
    Impact = field("Impact")
    Type = field("Type")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LimitationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LimitationTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRefreshSchemasStatusMessage:
    boto3_raw_data: "type_defs.DescribeRefreshSchemasStatusMessageTypeDef" = (
        dataclasses.field()
    )

    EndpointArn = field("EndpointArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeRefreshSchemasStatusMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRefreshSchemasStatusMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RefreshSchemasStatus:
    boto3_raw_data: "type_defs.RefreshSchemasStatusTypeDef" = dataclasses.field()

    EndpointArn = field("EndpointArn")
    ReplicationInstanceArn = field("ReplicationInstanceArn")
    Status = field("Status")
    LastRefreshDate = field("LastRefreshDate")
    LastFailureMessage = field("LastFailureMessage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RefreshSchemasStatusTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RefreshSchemasStatusTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeReplicationInstanceTaskLogsMessage:
    boto3_raw_data: "type_defs.DescribeReplicationInstanceTaskLogsMessageTypeDef" = (
        dataclasses.field()
    )

    ReplicationInstanceArn = field("ReplicationInstanceArn")
    MaxRecords = field("MaxRecords")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeReplicationInstanceTaskLogsMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeReplicationInstanceTaskLogsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReplicationInstanceTaskLog:
    boto3_raw_data: "type_defs.ReplicationInstanceTaskLogTypeDef" = dataclasses.field()

    ReplicationTaskName = field("ReplicationTaskName")
    ReplicationTaskArn = field("ReplicationTaskArn")
    ReplicationInstanceTaskLogSize = field("ReplicationInstanceTaskLogSize")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReplicationInstanceTaskLogTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReplicationInstanceTaskLogTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TableStatistics:
    boto3_raw_data: "type_defs.TableStatisticsTypeDef" = dataclasses.field()

    SchemaName = field("SchemaName")
    TableName = field("TableName")
    Inserts = field("Inserts")
    Deletes = field("Deletes")
    Updates = field("Updates")
    Ddls = field("Ddls")
    AppliedInserts = field("AppliedInserts")
    AppliedDeletes = field("AppliedDeletes")
    AppliedUpdates = field("AppliedUpdates")
    AppliedDdls = field("AppliedDdls")
    FullLoadRows = field("FullLoadRows")
    FullLoadCondtnlChkFailedRows = field("FullLoadCondtnlChkFailedRows")
    FullLoadErrorRows = field("FullLoadErrorRows")
    FullLoadStartTime = field("FullLoadStartTime")
    FullLoadEndTime = field("FullLoadEndTime")
    FullLoadReloaded = field("FullLoadReloaded")
    LastUpdateTime = field("LastUpdateTime")
    TableState = field("TableState")
    ValidationPendingRecords = field("ValidationPendingRecords")
    ValidationFailedRecords = field("ValidationFailedRecords")
    ValidationSuspendedRecords = field("ValidationSuspendedRecords")
    ValidationState = field("ValidationState")
    ValidationStateDetails = field("ValidationStateDetails")
    ResyncState = field("ResyncState")
    ResyncRowsAttempted = field("ResyncRowsAttempted")
    ResyncRowsSucceeded = field("ResyncRowsSucceeded")
    ResyncRowsFailed = field("ResyncRowsFailed")
    ResyncProgress = field("ResyncProgress")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TableStatisticsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TableStatisticsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeReplicationTaskAssessmentResultsMessage:
    boto3_raw_data: (
        "type_defs.DescribeReplicationTaskAssessmentResultsMessageTypeDef"
    ) = dataclasses.field()

    ReplicationTaskArn = field("ReplicationTaskArn")
    MaxRecords = field("MaxRecords")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeReplicationTaskAssessmentResultsMessageTypeDef"
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
                "type_defs.DescribeReplicationTaskAssessmentResultsMessageTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReplicationTaskAssessmentResult:
    boto3_raw_data: "type_defs.ReplicationTaskAssessmentResultTypeDef" = (
        dataclasses.field()
    )

    ReplicationTaskIdentifier = field("ReplicationTaskIdentifier")
    ReplicationTaskArn = field("ReplicationTaskArn")
    ReplicationTaskLastAssessmentDate = field("ReplicationTaskLastAssessmentDate")
    AssessmentStatus = field("AssessmentStatus")
    AssessmentResultsFile = field("AssessmentResultsFile")
    AssessmentResults = field("AssessmentResults")
    S3ObjectUrl = field("S3ObjectUrl")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ReplicationTaskAssessmentResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReplicationTaskAssessmentResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReplicationTaskIndividualAssessment:
    boto3_raw_data: "type_defs.ReplicationTaskIndividualAssessmentTypeDef" = (
        dataclasses.field()
    )

    ReplicationTaskIndividualAssessmentArn = field(
        "ReplicationTaskIndividualAssessmentArn"
    )
    ReplicationTaskAssessmentRunArn = field("ReplicationTaskAssessmentRunArn")
    IndividualAssessmentName = field("IndividualAssessmentName")
    Status = field("Status")
    ReplicationTaskIndividualAssessmentStartDate = field(
        "ReplicationTaskIndividualAssessmentStartDate"
    )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ReplicationTaskIndividualAssessmentTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReplicationTaskIndividualAssessmentTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSchemasMessage:
    boto3_raw_data: "type_defs.DescribeSchemasMessageTypeDef" = dataclasses.field()

    EndpointArn = field("EndpointArn")
    MaxRecords = field("MaxRecords")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeSchemasMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSchemasMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OracleSettingsOutput:
    boto3_raw_data: "type_defs.OracleSettingsOutputTypeDef" = dataclasses.field()

    AddSupplementalLogging = field("AddSupplementalLogging")
    ArchivedLogDestId = field("ArchivedLogDestId")
    AdditionalArchivedLogDestId = field("AdditionalArchivedLogDestId")
    ExtraArchivedLogDestIds = field("ExtraArchivedLogDestIds")
    AllowSelectNestedTables = field("AllowSelectNestedTables")
    ParallelAsmReadThreads = field("ParallelAsmReadThreads")
    ReadAheadBlocks = field("ReadAheadBlocks")
    AccessAlternateDirectly = field("AccessAlternateDirectly")
    UseAlternateFolderForOnline = field("UseAlternateFolderForOnline")
    OraclePathPrefix = field("OraclePathPrefix")
    UsePathPrefix = field("UsePathPrefix")
    ReplacePathPrefix = field("ReplacePathPrefix")
    EnableHomogenousTablespace = field("EnableHomogenousTablespace")
    DirectPathNoLog = field("DirectPathNoLog")
    ArchivedLogsOnly = field("ArchivedLogsOnly")
    AsmPassword = field("AsmPassword")
    AsmServer = field("AsmServer")
    AsmUser = field("AsmUser")
    CharLengthSemantics = field("CharLengthSemantics")
    DatabaseName = field("DatabaseName")
    DirectPathParallelLoad = field("DirectPathParallelLoad")
    FailTasksOnLobTruncation = field("FailTasksOnLobTruncation")
    NumberDatatypeScale = field("NumberDatatypeScale")
    Password = field("Password")
    Port = field("Port")
    ReadTableSpaceName = field("ReadTableSpaceName")
    RetryInterval = field("RetryInterval")
    SecurityDbEncryption = field("SecurityDbEncryption")
    SecurityDbEncryptionName = field("SecurityDbEncryptionName")
    ServerName = field("ServerName")
    SpatialDataOptionToGeoJsonFunctionName = field(
        "SpatialDataOptionToGeoJsonFunctionName"
    )
    StandbyDelayTime = field("StandbyDelayTime")
    Username = field("Username")
    UseBFile = field("UseBFile")
    UseDirectPathFullLoad = field("UseDirectPathFullLoad")
    UseLogminerReader = field("UseLogminerReader")
    SecretsManagerAccessRoleArn = field("SecretsManagerAccessRoleArn")
    SecretsManagerSecretId = field("SecretsManagerSecretId")
    SecretsManagerOracleAsmAccessRoleArn = field("SecretsManagerOracleAsmAccessRoleArn")
    SecretsManagerOracleAsmSecretId = field("SecretsManagerOracleAsmSecretId")
    TrimSpaceInChar = field("TrimSpaceInChar")
    ConvertTimestampWithZoneToUTC = field("ConvertTimestampWithZoneToUTC")
    OpenTransactionWindow = field("OpenTransactionWindow")
    AuthenticationMethod = field("AuthenticationMethod")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OracleSettingsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OracleSettingsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExportMetadataModelAssessmentMessage:
    boto3_raw_data: "type_defs.ExportMetadataModelAssessmentMessageTypeDef" = (
        dataclasses.field()
    )

    MigrationProjectIdentifier = field("MigrationProjectIdentifier")
    SelectionRules = field("SelectionRules")
    FileName = field("FileName")
    AssessmentReportTypes = field("AssessmentReportTypes")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ExportMetadataModelAssessmentMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExportMetadataModelAssessmentMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExportMetadataModelAssessmentResultEntry:
    boto3_raw_data: "type_defs.ExportMetadataModelAssessmentResultEntryTypeDef" = (
        dataclasses.field()
    )

    S3ObjectKey = field("S3ObjectKey")
    ObjectURL = field("ObjectURL")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ExportMetadataModelAssessmentResultEntryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExportMetadataModelAssessmentResultEntryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExportSqlDetails:
    boto3_raw_data: "type_defs.ExportSqlDetailsTypeDef" = dataclasses.field()

    S3ObjectKey = field("S3ObjectKey")
    ObjectURL = field("ObjectURL")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExportSqlDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExportSqlDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceMessage:
    boto3_raw_data: "type_defs.ListTagsForResourceMessageTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")
    ResourceArnList = field("ResourceArnList")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTagsForResourceMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsForResourceMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyConversionConfigurationMessage:
    boto3_raw_data: "type_defs.ModifyConversionConfigurationMessageTypeDef" = (
        dataclasses.field()
    )

    MigrationProjectIdentifier = field("MigrationProjectIdentifier")
    ConversionConfiguration = field("ConversionConfiguration")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ModifyConversionConfigurationMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyConversionConfigurationMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyEventSubscriptionMessage:
    boto3_raw_data: "type_defs.ModifyEventSubscriptionMessageTypeDef" = (
        dataclasses.field()
    )

    SubscriptionName = field("SubscriptionName")
    SnsTopicArn = field("SnsTopicArn")
    SourceType = field("SourceType")
    EventCategories = field("EventCategories")
    Enabled = field("Enabled")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ModifyEventSubscriptionMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyEventSubscriptionMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyInstanceProfileMessage:
    boto3_raw_data: "type_defs.ModifyInstanceProfileMessageTypeDef" = (
        dataclasses.field()
    )

    InstanceProfileIdentifier = field("InstanceProfileIdentifier")
    AvailabilityZone = field("AvailabilityZone")
    KmsKeyArn = field("KmsKeyArn")
    PubliclyAccessible = field("PubliclyAccessible")
    NetworkType = field("NetworkType")
    InstanceProfileName = field("InstanceProfileName")
    Description = field("Description")
    SubnetGroupIdentifier = field("SubnetGroupIdentifier")
    VpcSecurityGroups = field("VpcSecurityGroups")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ModifyInstanceProfileMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyInstanceProfileMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyReplicationSubnetGroupMessage:
    boto3_raw_data: "type_defs.ModifyReplicationSubnetGroupMessageTypeDef" = (
        dataclasses.field()
    )

    ReplicationSubnetGroupIdentifier = field("ReplicationSubnetGroupIdentifier")
    SubnetIds = field("SubnetIds")
    ReplicationSubnetGroupDescription = field("ReplicationSubnetGroupDescription")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ModifyReplicationSubnetGroupMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyReplicationSubnetGroupMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MoveReplicationTaskMessage:
    boto3_raw_data: "type_defs.MoveReplicationTaskMessageTypeDef" = dataclasses.field()

    ReplicationTaskArn = field("ReplicationTaskArn")
    TargetReplicationInstanceArn = field("TargetReplicationInstanceArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MoveReplicationTaskMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MoveReplicationTaskMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OracleSettings:
    boto3_raw_data: "type_defs.OracleSettingsTypeDef" = dataclasses.field()

    AddSupplementalLogging = field("AddSupplementalLogging")
    ArchivedLogDestId = field("ArchivedLogDestId")
    AdditionalArchivedLogDestId = field("AdditionalArchivedLogDestId")
    ExtraArchivedLogDestIds = field("ExtraArchivedLogDestIds")
    AllowSelectNestedTables = field("AllowSelectNestedTables")
    ParallelAsmReadThreads = field("ParallelAsmReadThreads")
    ReadAheadBlocks = field("ReadAheadBlocks")
    AccessAlternateDirectly = field("AccessAlternateDirectly")
    UseAlternateFolderForOnline = field("UseAlternateFolderForOnline")
    OraclePathPrefix = field("OraclePathPrefix")
    UsePathPrefix = field("UsePathPrefix")
    ReplacePathPrefix = field("ReplacePathPrefix")
    EnableHomogenousTablespace = field("EnableHomogenousTablespace")
    DirectPathNoLog = field("DirectPathNoLog")
    ArchivedLogsOnly = field("ArchivedLogsOnly")
    AsmPassword = field("AsmPassword")
    AsmServer = field("AsmServer")
    AsmUser = field("AsmUser")
    CharLengthSemantics = field("CharLengthSemantics")
    DatabaseName = field("DatabaseName")
    DirectPathParallelLoad = field("DirectPathParallelLoad")
    FailTasksOnLobTruncation = field("FailTasksOnLobTruncation")
    NumberDatatypeScale = field("NumberDatatypeScale")
    Password = field("Password")
    Port = field("Port")
    ReadTableSpaceName = field("ReadTableSpaceName")
    RetryInterval = field("RetryInterval")
    SecurityDbEncryption = field("SecurityDbEncryption")
    SecurityDbEncryptionName = field("SecurityDbEncryptionName")
    ServerName = field("ServerName")
    SpatialDataOptionToGeoJsonFunctionName = field(
        "SpatialDataOptionToGeoJsonFunctionName"
    )
    StandbyDelayTime = field("StandbyDelayTime")
    Username = field("Username")
    UseBFile = field("UseBFile")
    UseDirectPathFullLoad = field("UseDirectPathFullLoad")
    UseLogminerReader = field("UseLogminerReader")
    SecretsManagerAccessRoleArn = field("SecretsManagerAccessRoleArn")
    SecretsManagerSecretId = field("SecretsManagerSecretId")
    SecretsManagerOracleAsmAccessRoleArn = field("SecretsManagerOracleAsmAccessRoleArn")
    SecretsManagerOracleAsmSecretId = field("SecretsManagerOracleAsmSecretId")
    TrimSpaceInChar = field("TrimSpaceInChar")
    ConvertTimestampWithZoneToUTC = field("ConvertTimestampWithZoneToUTC")
    OpenTransactionWindow = field("OpenTransactionWindow")
    AuthenticationMethod = field("AuthenticationMethod")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OracleSettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OracleSettingsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PendingMaintenanceAction:
    boto3_raw_data: "type_defs.PendingMaintenanceActionTypeDef" = dataclasses.field()

    Action = field("Action")
    AutoAppliedAfterDate = field("AutoAppliedAfterDate")
    ForcedApplyDate = field("ForcedApplyDate")
    OptInStatus = field("OptInStatus")
    CurrentApplyDate = field("CurrentApplyDate")
    Description = field("Description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PendingMaintenanceActionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PendingMaintenanceActionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReplicationTaskAssessmentRunProgress:
    boto3_raw_data: "type_defs.ReplicationTaskAssessmentRunProgressTypeDef" = (
        dataclasses.field()
    )

    IndividualAssessmentCount = field("IndividualAssessmentCount")
    IndividualAssessmentCompletedCount = field("IndividualAssessmentCompletedCount")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ReplicationTaskAssessmentRunProgressTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReplicationTaskAssessmentRunProgressTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReplicationTaskAssessmentRunResultStatistic:
    boto3_raw_data: "type_defs.ReplicationTaskAssessmentRunResultStatisticTypeDef" = (
        dataclasses.field()
    )

    Passed = field("Passed")
    Failed = field("Failed")
    Error = field("Error")
    Warning = field("Warning")
    Cancelled = field("Cancelled")
    Skipped = field("Skipped")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ReplicationTaskAssessmentRunResultStatisticTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReplicationTaskAssessmentRunResultStatisticTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProvisionData:
    boto3_raw_data: "type_defs.ProvisionDataTypeDef" = dataclasses.field()

    ProvisionState = field("ProvisionState")
    ProvisionedCapacityUnits = field("ProvisionedCapacityUnits")
    DateProvisioned = field("DateProvisioned")
    IsNewProvisioningAvailable = field("IsNewProvisioningAvailable")
    DateNewProvisioningDataAvailable = field("DateNewProvisioningDataAvailable")
    ReasonForNewProvisioningData = field("ReasonForNewProvisioningData")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ProvisionDataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ProvisionDataTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RdsConfiguration:
    boto3_raw_data: "type_defs.RdsConfigurationTypeDef" = dataclasses.field()

    EngineEdition = field("EngineEdition")
    InstanceType = field("InstanceType")
    InstanceVcpu = field("InstanceVcpu")
    InstanceMemory = field("InstanceMemory")
    StorageType = field("StorageType")
    StorageSize = field("StorageSize")
    StorageIops = field("StorageIops")
    DeploymentOption = field("DeploymentOption")
    EngineVersion = field("EngineVersion")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RdsConfigurationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RdsConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RdsRequirements:
    boto3_raw_data: "type_defs.RdsRequirementsTypeDef" = dataclasses.field()

    EngineEdition = field("EngineEdition")
    InstanceVcpu = field("InstanceVcpu")
    InstanceMemory = field("InstanceMemory")
    StorageSize = field("StorageSize")
    StorageIops = field("StorageIops")
    DeploymentOption = field("DeploymentOption")
    EngineVersion = field("EngineVersion")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RdsRequirementsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RdsRequirementsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RebootReplicationInstanceMessage:
    boto3_raw_data: "type_defs.RebootReplicationInstanceMessageTypeDef" = (
        dataclasses.field()
    )

    ReplicationInstanceArn = field("ReplicationInstanceArn")
    ForceFailover = field("ForceFailover")
    ForcePlannedFailover = field("ForcePlannedFailover")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RebootReplicationInstanceMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RebootReplicationInstanceMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecommendationSettings:
    boto3_raw_data: "type_defs.RecommendationSettingsTypeDef" = dataclasses.field()

    InstanceSizingType = field("InstanceSizingType")
    WorkloadType = field("WorkloadType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RecommendationSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RecommendationSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RefreshSchemasMessage:
    boto3_raw_data: "type_defs.RefreshSchemasMessageTypeDef" = dataclasses.field()

    EndpointArn = field("EndpointArn")
    ReplicationInstanceArn = field("ReplicationInstanceArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RefreshSchemasMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RefreshSchemasMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TableToReload:
    boto3_raw_data: "type_defs.TableToReloadTypeDef" = dataclasses.field()

    SchemaName = field("SchemaName")
    TableName = field("TableName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TableToReloadTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TableToReloadTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemoveTagsFromResourceMessage:
    boto3_raw_data: "type_defs.RemoveTagsFromResourceMessageTypeDef" = (
        dataclasses.field()
    )

    ResourceArn = field("ResourceArn")
    TagKeys = field("TagKeys")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RemoveTagsFromResourceMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemoveTagsFromResourceMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReplicationPendingModifiedValues:
    boto3_raw_data: "type_defs.ReplicationPendingModifiedValuesTypeDef" = (
        dataclasses.field()
    )

    ReplicationInstanceClass = field("ReplicationInstanceClass")
    AllocatedStorage = field("AllocatedStorage")
    MultiAZ = field("MultiAZ")
    EngineVersion = field("EngineVersion")
    NetworkType = field("NetworkType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ReplicationPendingModifiedValuesTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReplicationPendingModifiedValuesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VpcSecurityGroupMembership:
    boto3_raw_data: "type_defs.VpcSecurityGroupMembershipTypeDef" = dataclasses.field()

    VpcSecurityGroupId = field("VpcSecurityGroupId")
    Status = field("Status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VpcSecurityGroupMembershipTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VpcSecurityGroupMembershipTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReplicationStats:
    boto3_raw_data: "type_defs.ReplicationStatsTypeDef" = dataclasses.field()

    FullLoadProgressPercent = field("FullLoadProgressPercent")
    ElapsedTimeMillis = field("ElapsedTimeMillis")
    TablesLoaded = field("TablesLoaded")
    TablesLoading = field("TablesLoading")
    TablesQueued = field("TablesQueued")
    TablesErrored = field("TablesErrored")
    FreshStartDate = field("FreshStartDate")
    StartDate = field("StartDate")
    StopDate = field("StopDate")
    FullLoadStartDate = field("FullLoadStartDate")
    FullLoadFinishDate = field("FullLoadFinishDate")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ReplicationStatsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReplicationStatsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReplicationTaskStats:
    boto3_raw_data: "type_defs.ReplicationTaskStatsTypeDef" = dataclasses.field()

    FullLoadProgressPercent = field("FullLoadProgressPercent")
    ElapsedTimeMillis = field("ElapsedTimeMillis")
    TablesLoaded = field("TablesLoaded")
    TablesLoading = field("TablesLoading")
    TablesQueued = field("TablesQueued")
    TablesErrored = field("TablesErrored")
    FreshStartDate = field("FreshStartDate")
    StartDate = field("StartDate")
    StopDate = field("StopDate")
    FullLoadStartDate = field("FullLoadStartDate")
    FullLoadFinishDate = field("FullLoadFinishDate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReplicationTaskStatsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReplicationTaskStatsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SchemaShortInfoResponse:
    boto3_raw_data: "type_defs.SchemaShortInfoResponseTypeDef" = dataclasses.field()

    SchemaId = field("SchemaId")
    SchemaName = field("SchemaName")
    DatabaseId = field("DatabaseId")
    DatabaseName = field("DatabaseName")
    DatabaseIpAddress = field("DatabaseIpAddress")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SchemaShortInfoResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SchemaShortInfoResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartDataMigrationMessage:
    boto3_raw_data: "type_defs.StartDataMigrationMessageTypeDef" = dataclasses.field()

    DataMigrationIdentifier = field("DataMigrationIdentifier")
    StartType = field("StartType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartDataMigrationMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartDataMigrationMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartExtensionPackAssociationMessage:
    boto3_raw_data: "type_defs.StartExtensionPackAssociationMessageTypeDef" = (
        dataclasses.field()
    )

    MigrationProjectIdentifier = field("MigrationProjectIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartExtensionPackAssociationMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartExtensionPackAssociationMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartMetadataModelAssessmentMessage:
    boto3_raw_data: "type_defs.StartMetadataModelAssessmentMessageTypeDef" = (
        dataclasses.field()
    )

    MigrationProjectIdentifier = field("MigrationProjectIdentifier")
    SelectionRules = field("SelectionRules")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartMetadataModelAssessmentMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartMetadataModelAssessmentMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartMetadataModelConversionMessage:
    boto3_raw_data: "type_defs.StartMetadataModelConversionMessageTypeDef" = (
        dataclasses.field()
    )

    MigrationProjectIdentifier = field("MigrationProjectIdentifier")
    SelectionRules = field("SelectionRules")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartMetadataModelConversionMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartMetadataModelConversionMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartMetadataModelExportAsScriptMessage:
    boto3_raw_data: "type_defs.StartMetadataModelExportAsScriptMessageTypeDef" = (
        dataclasses.field()
    )

    MigrationProjectIdentifier = field("MigrationProjectIdentifier")
    SelectionRules = field("SelectionRules")
    Origin = field("Origin")
    FileName = field("FileName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartMetadataModelExportAsScriptMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartMetadataModelExportAsScriptMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartMetadataModelExportToTargetMessage:
    boto3_raw_data: "type_defs.StartMetadataModelExportToTargetMessageTypeDef" = (
        dataclasses.field()
    )

    MigrationProjectIdentifier = field("MigrationProjectIdentifier")
    SelectionRules = field("SelectionRules")
    OverwriteExtensionPack = field("OverwriteExtensionPack")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartMetadataModelExportToTargetMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartMetadataModelExportToTargetMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartMetadataModelImportMessage:
    boto3_raw_data: "type_defs.StartMetadataModelImportMessageTypeDef" = (
        dataclasses.field()
    )

    MigrationProjectIdentifier = field("MigrationProjectIdentifier")
    SelectionRules = field("SelectionRules")
    Origin = field("Origin")
    Refresh = field("Refresh")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartMetadataModelImportMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartMetadataModelImportMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartReplicationTaskAssessmentMessage:
    boto3_raw_data: "type_defs.StartReplicationTaskAssessmentMessageTypeDef" = (
        dataclasses.field()
    )

    ReplicationTaskArn = field("ReplicationTaskArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartReplicationTaskAssessmentMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartReplicationTaskAssessmentMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopDataMigrationMessage:
    boto3_raw_data: "type_defs.StopDataMigrationMessageTypeDef" = dataclasses.field()

    DataMigrationIdentifier = field("DataMigrationIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopDataMigrationMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopDataMigrationMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopReplicationMessage:
    boto3_raw_data: "type_defs.StopReplicationMessageTypeDef" = dataclasses.field()

    ReplicationConfigArn = field("ReplicationConfigArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopReplicationMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopReplicationMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopReplicationTaskMessage:
    boto3_raw_data: "type_defs.StopReplicationTaskMessageTypeDef" = dataclasses.field()

    ReplicationTaskArn = field("ReplicationTaskArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopReplicationTaskMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopReplicationTaskMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TestConnectionMessage:
    boto3_raw_data: "type_defs.TestConnectionMessageTypeDef" = dataclasses.field()

    ReplicationInstanceArn = field("ReplicationInstanceArn")
    EndpointArn = field("EndpointArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TestConnectionMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TestConnectionMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSubscriptionsToEventBridgeMessage:
    boto3_raw_data: "type_defs.UpdateSubscriptionsToEventBridgeMessageTypeDef" = (
        dataclasses.field()
    )

    ForceMove = field("ForceMove")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateSubscriptionsToEventBridgeMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSubscriptionsToEventBridgeMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddTagsToResourceMessage:
    boto3_raw_data: "type_defs.AddTagsToResourceMessageTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AddTagsToResourceMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddTagsToResourceMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateEventSubscriptionMessage:
    boto3_raw_data: "type_defs.CreateEventSubscriptionMessageTypeDef" = (
        dataclasses.field()
    )

    SubscriptionName = field("SubscriptionName")
    SnsTopicArn = field("SnsTopicArn")
    SourceType = field("SourceType")
    EventCategories = field("EventCategories")
    SourceIds = field("SourceIds")
    Enabled = field("Enabled")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateEventSubscriptionMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateEventSubscriptionMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateInstanceProfileMessage:
    boto3_raw_data: "type_defs.CreateInstanceProfileMessageTypeDef" = (
        dataclasses.field()
    )

    AvailabilityZone = field("AvailabilityZone")
    KmsKeyArn = field("KmsKeyArn")
    PubliclyAccessible = field("PubliclyAccessible")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    NetworkType = field("NetworkType")
    InstanceProfileName = field("InstanceProfileName")
    Description = field("Description")
    SubnetGroupIdentifier = field("SubnetGroupIdentifier")
    VpcSecurityGroups = field("VpcSecurityGroups")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateInstanceProfileMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateInstanceProfileMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateReplicationSubnetGroupMessage:
    boto3_raw_data: "type_defs.CreateReplicationSubnetGroupMessageTypeDef" = (
        dataclasses.field()
    )

    ReplicationSubnetGroupIdentifier = field("ReplicationSubnetGroupIdentifier")
    ReplicationSubnetGroupDescription = field("ReplicationSubnetGroupDescription")
    SubnetIds = field("SubnetIds")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateReplicationSubnetGroupMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateReplicationSubnetGroupMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartReplicationTaskAssessmentRunMessage:
    boto3_raw_data: "type_defs.StartReplicationTaskAssessmentRunMessageTypeDef" = (
        dataclasses.field()
    )

    ReplicationTaskArn = field("ReplicationTaskArn")
    ServiceAccessRoleArn = field("ServiceAccessRoleArn")
    ResultLocationBucket = field("ResultLocationBucket")
    AssessmentRunName = field("AssessmentRunName")
    ResultLocationFolder = field("ResultLocationFolder")
    ResultEncryptionMode = field("ResultEncryptionMode")
    ResultKmsKeyArn = field("ResultKmsKeyArn")
    IncludeOnly = field("IncludeOnly")
    Exclude = field("Exclude")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartReplicationTaskAssessmentRunMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartReplicationTaskAssessmentRunMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateFleetAdvisorCollectorResponse:
    boto3_raw_data: "type_defs.CreateFleetAdvisorCollectorResponseTypeDef" = (
        dataclasses.field()
    )

    CollectorReferencedId = field("CollectorReferencedId")
    CollectorName = field("CollectorName")
    Description = field("Description")
    ServiceAccessRoleArn = field("ServiceAccessRoleArn")
    S3BucketName = field("S3BucketName")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateFleetAdvisorCollectorResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateFleetAdvisorCollectorResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteFleetAdvisorDatabasesResponse:
    boto3_raw_data: "type_defs.DeleteFleetAdvisorDatabasesResponseTypeDef" = (
        dataclasses.field()
    )

    DatabaseIds = field("DatabaseIds")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteFleetAdvisorDatabasesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteFleetAdvisorDatabasesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAccountAttributesResponse:
    boto3_raw_data: "type_defs.DescribeAccountAttributesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AccountQuotas(self):  # pragma: no cover
        return AccountQuota.make_many(self.boto3_raw_data["AccountQuotas"])

    UniqueAccountIdentifier = field("UniqueAccountIdentifier")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeAccountAttributesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAccountAttributesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeApplicableIndividualAssessmentsResponse:
    boto3_raw_data: (
        "type_defs.DescribeApplicableIndividualAssessmentsResponseTypeDef"
    ) = dataclasses.field()

    IndividualAssessmentNames = field("IndividualAssessmentNames")
    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeApplicableIndividualAssessmentsResponseTypeDef"
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
                "type_defs.DescribeApplicableIndividualAssessmentsResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeConversionConfigurationResponse:
    boto3_raw_data: "type_defs.DescribeConversionConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    MigrationProjectIdentifier = field("MigrationProjectIdentifier")
    ConversionConfiguration = field("ConversionConfiguration")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeConversionConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeConversionConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSchemasResponse:
    boto3_raw_data: "type_defs.DescribeSchemasResponseTypeDef" = dataclasses.field()

    Marker = field("Marker")
    Schemas = field("Schemas")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeSchemasResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSchemasResponseTypeDef"]
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
class ListTagsForResourceResponse:
    boto3_raw_data: "type_defs.ListTagsForResourceResponseTypeDef" = dataclasses.field()

    @cached_property
    def TagList(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["TagList"])

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
class ModifyConversionConfigurationResponse:
    boto3_raw_data: "type_defs.ModifyConversionConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    MigrationProjectIdentifier = field("MigrationProjectIdentifier")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ModifyConversionConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyConversionConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReloadReplicationTablesResponse:
    boto3_raw_data: "type_defs.ReloadReplicationTablesResponseTypeDef" = (
        dataclasses.field()
    )

    ReplicationConfigArn = field("ReplicationConfigArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ReloadReplicationTablesResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReloadReplicationTablesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReloadTablesResponse:
    boto3_raw_data: "type_defs.ReloadTablesResponseTypeDef" = dataclasses.field()

    ReplicationTaskArn = field("ReplicationTaskArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReloadTablesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReloadTablesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RunFleetAdvisorLsaAnalysisResponse:
    boto3_raw_data: "type_defs.RunFleetAdvisorLsaAnalysisResponseTypeDef" = (
        dataclasses.field()
    )

    LsaAnalysisId = field("LsaAnalysisId")
    Status = field("Status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RunFleetAdvisorLsaAnalysisResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RunFleetAdvisorLsaAnalysisResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartExtensionPackAssociationResponse:
    boto3_raw_data: "type_defs.StartExtensionPackAssociationResponseTypeDef" = (
        dataclasses.field()
    )

    RequestIdentifier = field("RequestIdentifier")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartExtensionPackAssociationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartExtensionPackAssociationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartMetadataModelAssessmentResponse:
    boto3_raw_data: "type_defs.StartMetadataModelAssessmentResponseTypeDef" = (
        dataclasses.field()
    )

    RequestIdentifier = field("RequestIdentifier")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartMetadataModelAssessmentResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartMetadataModelAssessmentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartMetadataModelConversionResponse:
    boto3_raw_data: "type_defs.StartMetadataModelConversionResponseTypeDef" = (
        dataclasses.field()
    )

    RequestIdentifier = field("RequestIdentifier")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartMetadataModelConversionResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartMetadataModelConversionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartMetadataModelExportAsScriptResponse:
    boto3_raw_data: "type_defs.StartMetadataModelExportAsScriptResponseTypeDef" = (
        dataclasses.field()
    )

    RequestIdentifier = field("RequestIdentifier")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartMetadataModelExportAsScriptResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartMetadataModelExportAsScriptResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartMetadataModelExportToTargetResponse:
    boto3_raw_data: "type_defs.StartMetadataModelExportToTargetResponseTypeDef" = (
        dataclasses.field()
    )

    RequestIdentifier = field("RequestIdentifier")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartMetadataModelExportToTargetResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartMetadataModelExportToTargetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartMetadataModelImportResponse:
    boto3_raw_data: "type_defs.StartMetadataModelImportResponseTypeDef" = (
        dataclasses.field()
    )

    RequestIdentifier = field("RequestIdentifier")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartMetadataModelImportResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartMetadataModelImportResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSubscriptionsToEventBridgeResponse:
    boto3_raw_data: "type_defs.UpdateSubscriptionsToEventBridgeResponseTypeDef" = (
        dataclasses.field()
    )

    Result = field("Result")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateSubscriptionsToEventBridgeResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSubscriptionsToEventBridgeResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Subnet:
    boto3_raw_data: "type_defs.SubnetTypeDef" = dataclasses.field()

    SubnetIdentifier = field("SubnetIdentifier")

    @cached_property
    def SubnetAvailabilityZone(self):  # pragma: no cover
        return AvailabilityZone.make_one(self.boto3_raw_data["SubnetAvailabilityZone"])

    SubnetStatus = field("SubnetStatus")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SubnetTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SubnetTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchStartRecommendationsResponse:
    boto3_raw_data: "type_defs.BatchStartRecommendationsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ErrorEntries(self):  # pragma: no cover
        return BatchStartRecommendationsErrorEntry.make_many(
            self.boto3_raw_data["ErrorEntries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchStartRecommendationsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchStartRecommendationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportCertificateMessage:
    boto3_raw_data: "type_defs.ImportCertificateMessageTypeDef" = dataclasses.field()

    CertificateIdentifier = field("CertificateIdentifier")
    CertificatePem = field("CertificatePem")
    CertificateWallet = field("CertificateWallet")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImportCertificateMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImportCertificateMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteCertificateResponse:
    boto3_raw_data: "type_defs.DeleteCertificateResponseTypeDef" = dataclasses.field()

    @cached_property
    def Certificate(self):  # pragma: no cover
        return Certificate.make_one(self.boto3_raw_data["Certificate"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteCertificateResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteCertificateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeCertificatesResponse:
    boto3_raw_data: "type_defs.DescribeCertificatesResponseTypeDef" = (
        dataclasses.field()
    )

    Marker = field("Marker")

    @cached_property
    def Certificates(self):  # pragma: no cover
        return Certificate.make_many(self.boto3_raw_data["Certificates"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeCertificatesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeCertificatesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportCertificateResponse:
    boto3_raw_data: "type_defs.ImportCertificateResponseTypeDef" = dataclasses.field()

    @cached_property
    def Certificate(self):  # pragma: no cover
        return Certificate.make_one(self.boto3_raw_data["Certificate"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImportCertificateResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImportCertificateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CollectorResponse:
    boto3_raw_data: "type_defs.CollectorResponseTypeDef" = dataclasses.field()

    CollectorReferencedId = field("CollectorReferencedId")
    CollectorName = field("CollectorName")
    CollectorVersion = field("CollectorVersion")
    VersionStatus = field("VersionStatus")
    Description = field("Description")
    S3BucketName = field("S3BucketName")
    ServiceAccessRoleArn = field("ServiceAccessRoleArn")

    @cached_property
    def CollectorHealthCheck(self):  # pragma: no cover
        return CollectorHealthCheck.make_one(
            self.boto3_raw_data["CollectorHealthCheck"]
        )

    LastDataReceived = field("LastDataReceived")
    RegisteredDate = field("RegisteredDate")
    CreatedDate = field("CreatedDate")
    ModifiedDate = field("ModifiedDate")

    @cached_property
    def InventoryData(self):  # pragma: no cover
        return InventoryData.make_one(self.boto3_raw_data["InventoryData"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CollectorResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CollectorResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReplicationConfig:
    boto3_raw_data: "type_defs.ReplicationConfigTypeDef" = dataclasses.field()

    ReplicationConfigIdentifier = field("ReplicationConfigIdentifier")
    ReplicationConfigArn = field("ReplicationConfigArn")
    SourceEndpointArn = field("SourceEndpointArn")
    TargetEndpointArn = field("TargetEndpointArn")
    ReplicationType = field("ReplicationType")

    @cached_property
    def ComputeConfig(self):  # pragma: no cover
        return ComputeConfigOutput.make_one(self.boto3_raw_data["ComputeConfig"])

    ReplicationSettings = field("ReplicationSettings")
    SupplementalSettings = field("SupplementalSettings")
    TableMappings = field("TableMappings")
    ReplicationConfigCreateTime = field("ReplicationConfigCreateTime")
    ReplicationConfigUpdateTime = field("ReplicationConfigUpdateTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ReplicationConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReplicationConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteConnectionResponse:
    boto3_raw_data: "type_defs.DeleteConnectionResponseTypeDef" = dataclasses.field()

    @cached_property
    def Connection(self):  # pragma: no cover
        return Connection.make_one(self.boto3_raw_data["Connection"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteConnectionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteConnectionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeConnectionsResponse:
    boto3_raw_data: "type_defs.DescribeConnectionsResponseTypeDef" = dataclasses.field()

    Marker = field("Marker")

    @cached_property
    def Connections(self):  # pragma: no cover
        return Connection.make_many(self.boto3_raw_data["Connections"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeConnectionsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeConnectionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TestConnectionResponse:
    boto3_raw_data: "type_defs.TestConnectionResponseTypeDef" = dataclasses.field()

    @cached_property
    def Connection(self):  # pragma: no cover
        return Connection.make_one(self.boto3_raw_data["Connection"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TestConnectionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TestConnectionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateEventSubscriptionResponse:
    boto3_raw_data: "type_defs.CreateEventSubscriptionResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def EventSubscription(self):  # pragma: no cover
        return EventSubscription.make_one(self.boto3_raw_data["EventSubscription"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateEventSubscriptionResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateEventSubscriptionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteEventSubscriptionResponse:
    boto3_raw_data: "type_defs.DeleteEventSubscriptionResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def EventSubscription(self):  # pragma: no cover
        return EventSubscription.make_one(self.boto3_raw_data["EventSubscription"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteEventSubscriptionResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteEventSubscriptionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEventSubscriptionsResponse:
    boto3_raw_data: "type_defs.DescribeEventSubscriptionsResponseTypeDef" = (
        dataclasses.field()
    )

    Marker = field("Marker")

    @cached_property
    def EventSubscriptionsList(self):  # pragma: no cover
        return EventSubscription.make_many(
            self.boto3_raw_data["EventSubscriptionsList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeEventSubscriptionsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEventSubscriptionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyEventSubscriptionResponse:
    boto3_raw_data: "type_defs.ModifyEventSubscriptionResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def EventSubscription(self):  # pragma: no cover
        return EventSubscription.make_one(self.boto3_raw_data["EventSubscription"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ModifyEventSubscriptionResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyEventSubscriptionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateInstanceProfileResponse:
    boto3_raw_data: "type_defs.CreateInstanceProfileResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def InstanceProfile(self):  # pragma: no cover
        return InstanceProfile.make_one(self.boto3_raw_data["InstanceProfile"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateInstanceProfileResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateInstanceProfileResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteInstanceProfileResponse:
    boto3_raw_data: "type_defs.DeleteInstanceProfileResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def InstanceProfile(self):  # pragma: no cover
        return InstanceProfile.make_one(self.boto3_raw_data["InstanceProfile"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteInstanceProfileResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteInstanceProfileResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeInstanceProfilesResponse:
    boto3_raw_data: "type_defs.DescribeInstanceProfilesResponseTypeDef" = (
        dataclasses.field()
    )

    Marker = field("Marker")

    @cached_property
    def InstanceProfiles(self):  # pragma: no cover
        return InstanceProfile.make_many(self.boto3_raw_data["InstanceProfiles"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeInstanceProfilesResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeInstanceProfilesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyInstanceProfileResponse:
    boto3_raw_data: "type_defs.ModifyInstanceProfileResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def InstanceProfile(self):  # pragma: no cover
        return InstanceProfile.make_one(self.boto3_raw_data["InstanceProfile"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ModifyInstanceProfileResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyInstanceProfileResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateMigrationProjectMessage:
    boto3_raw_data: "type_defs.CreateMigrationProjectMessageTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def SourceDataProviderDescriptors(self):  # pragma: no cover
        return DataProviderDescriptorDefinition.make_many(
            self.boto3_raw_data["SourceDataProviderDescriptors"]
        )

    @cached_property
    def TargetDataProviderDescriptors(self):  # pragma: no cover
        return DataProviderDescriptorDefinition.make_many(
            self.boto3_raw_data["TargetDataProviderDescriptors"]
        )

    InstanceProfileIdentifier = field("InstanceProfileIdentifier")
    MigrationProjectName = field("MigrationProjectName")
    TransformationRules = field("TransformationRules")
    Description = field("Description")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @cached_property
    def SchemaConversionApplicationAttributes(self):  # pragma: no cover
        return SCApplicationAttributes.make_one(
            self.boto3_raw_data["SchemaConversionApplicationAttributes"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateMigrationProjectMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateMigrationProjectMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyMigrationProjectMessage:
    boto3_raw_data: "type_defs.ModifyMigrationProjectMessageTypeDef" = (
        dataclasses.field()
    )

    MigrationProjectIdentifier = field("MigrationProjectIdentifier")
    MigrationProjectName = field("MigrationProjectName")

    @cached_property
    def SourceDataProviderDescriptors(self):  # pragma: no cover
        return DataProviderDescriptorDefinition.make_many(
            self.boto3_raw_data["SourceDataProviderDescriptors"]
        )

    @cached_property
    def TargetDataProviderDescriptors(self):  # pragma: no cover
        return DataProviderDescriptorDefinition.make_many(
            self.boto3_raw_data["TargetDataProviderDescriptors"]
        )

    InstanceProfileIdentifier = field("InstanceProfileIdentifier")
    TransformationRules = field("TransformationRules")
    Description = field("Description")

    @cached_property
    def SchemaConversionApplicationAttributes(self):  # pragma: no cover
        return SCApplicationAttributes.make_one(
            self.boto3_raw_data["SchemaConversionApplicationAttributes"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ModifyMigrationProjectMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyMigrationProjectMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateReplicationInstanceMessage:
    boto3_raw_data: "type_defs.CreateReplicationInstanceMessageTypeDef" = (
        dataclasses.field()
    )

    ReplicationInstanceIdentifier = field("ReplicationInstanceIdentifier")
    ReplicationInstanceClass = field("ReplicationInstanceClass")
    AllocatedStorage = field("AllocatedStorage")
    VpcSecurityGroupIds = field("VpcSecurityGroupIds")
    AvailabilityZone = field("AvailabilityZone")
    ReplicationSubnetGroupIdentifier = field("ReplicationSubnetGroupIdentifier")
    PreferredMaintenanceWindow = field("PreferredMaintenanceWindow")
    MultiAZ = field("MultiAZ")
    EngineVersion = field("EngineVersion")
    AutoMinorVersionUpgrade = field("AutoMinorVersionUpgrade")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    KmsKeyId = field("KmsKeyId")
    PubliclyAccessible = field("PubliclyAccessible")
    DnsNameServers = field("DnsNameServers")
    ResourceIdentifier = field("ResourceIdentifier")
    NetworkType = field("NetworkType")

    @cached_property
    def KerberosAuthenticationSettings(self):  # pragma: no cover
        return KerberosAuthenticationSettings.make_one(
            self.boto3_raw_data["KerberosAuthenticationSettings"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateReplicationInstanceMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateReplicationInstanceMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyReplicationInstanceMessage:
    boto3_raw_data: "type_defs.ModifyReplicationInstanceMessageTypeDef" = (
        dataclasses.field()
    )

    ReplicationInstanceArn = field("ReplicationInstanceArn")
    AllocatedStorage = field("AllocatedStorage")
    ApplyImmediately = field("ApplyImmediately")
    ReplicationInstanceClass = field("ReplicationInstanceClass")
    VpcSecurityGroupIds = field("VpcSecurityGroupIds")
    PreferredMaintenanceWindow = field("PreferredMaintenanceWindow")
    MultiAZ = field("MultiAZ")
    EngineVersion = field("EngineVersion")
    AllowMajorVersionUpgrade = field("AllowMajorVersionUpgrade")
    AutoMinorVersionUpgrade = field("AutoMinorVersionUpgrade")
    ReplicationInstanceIdentifier = field("ReplicationInstanceIdentifier")
    NetworkType = field("NetworkType")

    @cached_property
    def KerberosAuthenticationSettings(self):  # pragma: no cover
        return KerberosAuthenticationSettings.make_one(
            self.boto3_raw_data["KerberosAuthenticationSettings"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ModifyReplicationInstanceMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyReplicationInstanceMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateReplicationTaskMessage:
    boto3_raw_data: "type_defs.CreateReplicationTaskMessageTypeDef" = (
        dataclasses.field()
    )

    ReplicationTaskIdentifier = field("ReplicationTaskIdentifier")
    SourceEndpointArn = field("SourceEndpointArn")
    TargetEndpointArn = field("TargetEndpointArn")
    ReplicationInstanceArn = field("ReplicationInstanceArn")
    MigrationType = field("MigrationType")
    TableMappings = field("TableMappings")
    ReplicationTaskSettings = field("ReplicationTaskSettings")
    CdcStartTime = field("CdcStartTime")
    CdcStartPosition = field("CdcStartPosition")
    CdcStopPosition = field("CdcStopPosition")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    TaskData = field("TaskData")
    ResourceIdentifier = field("ResourceIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateReplicationTaskMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateReplicationTaskMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyReplicationTaskMessage:
    boto3_raw_data: "type_defs.ModifyReplicationTaskMessageTypeDef" = (
        dataclasses.field()
    )

    ReplicationTaskArn = field("ReplicationTaskArn")
    ReplicationTaskIdentifier = field("ReplicationTaskIdentifier")
    MigrationType = field("MigrationType")
    TableMappings = field("TableMappings")
    ReplicationTaskSettings = field("ReplicationTaskSettings")
    CdcStartTime = field("CdcStartTime")
    CdcStartPosition = field("CdcStartPosition")
    CdcStopPosition = field("CdcStopPosition")
    TaskData = field("TaskData")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ModifyReplicationTaskMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyReplicationTaskMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SourceDataSetting:
    boto3_raw_data: "type_defs.SourceDataSettingTypeDef" = dataclasses.field()

    CDCStartPosition = field("CDCStartPosition")
    CDCStartTime = field("CDCStartTime")
    CDCStopTime = field("CDCStopTime")
    SlotName = field("SlotName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SourceDataSettingTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SourceDataSettingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartReplicationMessage:
    boto3_raw_data: "type_defs.StartReplicationMessageTypeDef" = dataclasses.field()

    ReplicationConfigArn = field("ReplicationConfigArn")
    StartReplicationType = field("StartReplicationType")
    PremigrationAssessmentSettings = field("PremigrationAssessmentSettings")
    CdcStartTime = field("CdcStartTime")
    CdcStartPosition = field("CdcStartPosition")
    CdcStopPosition = field("CdcStopPosition")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartReplicationMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartReplicationMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartReplicationTaskMessage:
    boto3_raw_data: "type_defs.StartReplicationTaskMessageTypeDef" = dataclasses.field()

    ReplicationTaskArn = field("ReplicationTaskArn")
    StartReplicationTaskType = field("StartReplicationTaskType")
    CdcStartTime = field("CdcStartTime")
    CdcStartPosition = field("CdcStartPosition")
    CdcStopPosition = field("CdcStopPosition")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartReplicationTaskMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartReplicationTaskMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataMigration:
    boto3_raw_data: "type_defs.DataMigrationTypeDef" = dataclasses.field()

    DataMigrationName = field("DataMigrationName")
    DataMigrationArn = field("DataMigrationArn")
    DataMigrationCreateTime = field("DataMigrationCreateTime")
    DataMigrationStartTime = field("DataMigrationStartTime")
    DataMigrationEndTime = field("DataMigrationEndTime")
    ServiceAccessRoleArn = field("ServiceAccessRoleArn")
    MigrationProjectArn = field("MigrationProjectArn")
    DataMigrationType = field("DataMigrationType")

    @cached_property
    def DataMigrationSettings(self):  # pragma: no cover
        return DataMigrationSettings.make_one(
            self.boto3_raw_data["DataMigrationSettings"]
        )

    @cached_property
    def SourceDataSettings(self):  # pragma: no cover
        return SourceDataSettingOutput.make_many(
            self.boto3_raw_data["SourceDataSettings"]
        )

    @cached_property
    def TargetDataSettings(self):  # pragma: no cover
        return TargetDataSetting.make_many(self.boto3_raw_data["TargetDataSettings"])

    @cached_property
    def DataMigrationStatistics(self):  # pragma: no cover
        return DataMigrationStatistics.make_one(
            self.boto3_raw_data["DataMigrationStatistics"]
        )

    DataMigrationStatus = field("DataMigrationStatus")
    PublicIpAddresses = field("PublicIpAddresses")
    DataMigrationCidrBlocks = field("DataMigrationCidrBlocks")
    LastFailureMessage = field("LastFailureMessage")
    StopReason = field("StopReason")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DataMigrationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DataMigrationTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MigrationProject:
    boto3_raw_data: "type_defs.MigrationProjectTypeDef" = dataclasses.field()

    MigrationProjectName = field("MigrationProjectName")
    MigrationProjectArn = field("MigrationProjectArn")
    MigrationProjectCreationTime = field("MigrationProjectCreationTime")

    @cached_property
    def SourceDataProviderDescriptors(self):  # pragma: no cover
        return DataProviderDescriptor.make_many(
            self.boto3_raw_data["SourceDataProviderDescriptors"]
        )

    @cached_property
    def TargetDataProviderDescriptors(self):  # pragma: no cover
        return DataProviderDescriptor.make_many(
            self.boto3_raw_data["TargetDataProviderDescriptors"]
        )

    InstanceProfileArn = field("InstanceProfileArn")
    InstanceProfileName = field("InstanceProfileName")
    TransformationRules = field("TransformationRules")
    Description = field("Description")

    @cached_property
    def SchemaConversionApplicationAttributes(self):  # pragma: no cover
        return SCApplicationAttributes.make_one(
            self.boto3_raw_data["SchemaConversionApplicationAttributes"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MigrationProjectTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MigrationProjectTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataProviderSettings:
    boto3_raw_data: "type_defs.DataProviderSettingsTypeDef" = dataclasses.field()

    @cached_property
    def RedshiftSettings(self):  # pragma: no cover
        return RedshiftDataProviderSettings.make_one(
            self.boto3_raw_data["RedshiftSettings"]
        )

    @cached_property
    def PostgreSqlSettings(self):  # pragma: no cover
        return PostgreSqlDataProviderSettings.make_one(
            self.boto3_raw_data["PostgreSqlSettings"]
        )

    @cached_property
    def MySqlSettings(self):  # pragma: no cover
        return MySqlDataProviderSettings.make_one(self.boto3_raw_data["MySqlSettings"])

    @cached_property
    def OracleSettings(self):  # pragma: no cover
        return OracleDataProviderSettings.make_one(
            self.boto3_raw_data["OracleSettings"]
        )

    @cached_property
    def MicrosoftSqlServerSettings(self):  # pragma: no cover
        return MicrosoftSqlServerDataProviderSettings.make_one(
            self.boto3_raw_data["MicrosoftSqlServerSettings"]
        )

    @cached_property
    def DocDbSettings(self):  # pragma: no cover
        return DocDbDataProviderSettings.make_one(self.boto3_raw_data["DocDbSettings"])

    @cached_property
    def MariaDbSettings(self):  # pragma: no cover
        return MariaDbDataProviderSettings.make_one(
            self.boto3_raw_data["MariaDbSettings"]
        )

    @cached_property
    def IbmDb2LuwSettings(self):  # pragma: no cover
        return IbmDb2LuwDataProviderSettings.make_one(
            self.boto3_raw_data["IbmDb2LuwSettings"]
        )

    @cached_property
    def IbmDb2zOsSettings(self):  # pragma: no cover
        return IbmDb2zOsDataProviderSettings.make_one(
            self.boto3_raw_data["IbmDb2zOsSettings"]
        )

    @cached_property
    def MongoDbSettings(self):  # pragma: no cover
        return MongoDbDataProviderSettings.make_one(
            self.boto3_raw_data["MongoDbSettings"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DataProviderSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataProviderSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DatabaseResponse:
    boto3_raw_data: "type_defs.DatabaseResponseTypeDef" = dataclasses.field()

    DatabaseId = field("DatabaseId")
    DatabaseName = field("DatabaseName")
    IpAddress = field("IpAddress")
    NumberOfSchemas = field("NumberOfSchemas")

    @cached_property
    def Server(self):  # pragma: no cover
        return ServerShortInfoResponse.make_one(self.boto3_raw_data["Server"])

    @cached_property
    def SoftwareDetails(self):  # pragma: no cover
        return DatabaseInstanceSoftwareDetailsResponse.make_one(
            self.boto3_raw_data["SoftwareDetails"]
        )

    @cached_property
    def Collectors(self):  # pragma: no cover
        return CollectorShortInfoResponse.make_many(self.boto3_raw_data["Collectors"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DatabaseResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DatabaseResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ErrorDetails:
    boto3_raw_data: "type_defs.ErrorDetailsTypeDef" = dataclasses.field()

    @cached_property
    def defaultErrorDetails(self):  # pragma: no cover
        return DefaultErrorDetails.make_one(self.boto3_raw_data["defaultErrorDetails"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ErrorDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ErrorDetailsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeCertificatesMessage:
    boto3_raw_data: "type_defs.DescribeCertificatesMessageTypeDef" = dataclasses.field()

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    MaxRecords = field("MaxRecords")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeCertificatesMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeCertificatesMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeConnectionsMessage:
    boto3_raw_data: "type_defs.DescribeConnectionsMessageTypeDef" = dataclasses.field()

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    MaxRecords = field("MaxRecords")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeConnectionsMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeConnectionsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDataMigrationsMessage:
    boto3_raw_data: "type_defs.DescribeDataMigrationsMessageTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    MaxRecords = field("MaxRecords")
    Marker = field("Marker")
    WithoutSettings = field("WithoutSettings")
    WithoutStatistics = field("WithoutStatistics")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeDataMigrationsMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDataMigrationsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDataProvidersMessage:
    boto3_raw_data: "type_defs.DescribeDataProvidersMessageTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    MaxRecords = field("MaxRecords")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeDataProvidersMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDataProvidersMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEndpointTypesMessage:
    boto3_raw_data: "type_defs.DescribeEndpointTypesMessageTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    MaxRecords = field("MaxRecords")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeEndpointTypesMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEndpointTypesMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEndpointsMessage:
    boto3_raw_data: "type_defs.DescribeEndpointsMessageTypeDef" = dataclasses.field()

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    MaxRecords = field("MaxRecords")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeEndpointsMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEndpointsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEventCategoriesMessage:
    boto3_raw_data: "type_defs.DescribeEventCategoriesMessageTypeDef" = (
        dataclasses.field()
    )

    SourceType = field("SourceType")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeEventCategoriesMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEventCategoriesMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEventSubscriptionsMessage:
    boto3_raw_data: "type_defs.DescribeEventSubscriptionsMessageTypeDef" = (
        dataclasses.field()
    )

    SubscriptionName = field("SubscriptionName")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    MaxRecords = field("MaxRecords")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeEventSubscriptionsMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEventSubscriptionsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEventsMessage:
    boto3_raw_data: "type_defs.DescribeEventsMessageTypeDef" = dataclasses.field()

    SourceIdentifier = field("SourceIdentifier")
    SourceType = field("SourceType")
    StartTime = field("StartTime")
    EndTime = field("EndTime")
    Duration = field("Duration")
    EventCategories = field("EventCategories")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    MaxRecords = field("MaxRecords")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeEventsMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEventsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeExtensionPackAssociationsMessage:
    boto3_raw_data: "type_defs.DescribeExtensionPackAssociationsMessageTypeDef" = (
        dataclasses.field()
    )

    MigrationProjectIdentifier = field("MigrationProjectIdentifier")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    Marker = field("Marker")
    MaxRecords = field("MaxRecords")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeExtensionPackAssociationsMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeExtensionPackAssociationsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFleetAdvisorCollectorsRequest:
    boto3_raw_data: "type_defs.DescribeFleetAdvisorCollectorsRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    MaxRecords = field("MaxRecords")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeFleetAdvisorCollectorsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFleetAdvisorCollectorsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFleetAdvisorDatabasesRequest:
    boto3_raw_data: "type_defs.DescribeFleetAdvisorDatabasesRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    MaxRecords = field("MaxRecords")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeFleetAdvisorDatabasesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFleetAdvisorDatabasesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFleetAdvisorSchemaObjectSummaryRequest:
    boto3_raw_data: (
        "type_defs.DescribeFleetAdvisorSchemaObjectSummaryRequestTypeDef"
    ) = dataclasses.field()

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    MaxRecords = field("MaxRecords")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeFleetAdvisorSchemaObjectSummaryRequestTypeDef"
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
                "type_defs.DescribeFleetAdvisorSchemaObjectSummaryRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFleetAdvisorSchemasRequest:
    boto3_raw_data: "type_defs.DescribeFleetAdvisorSchemasRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    MaxRecords = field("MaxRecords")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeFleetAdvisorSchemasRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFleetAdvisorSchemasRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeInstanceProfilesMessage:
    boto3_raw_data: "type_defs.DescribeInstanceProfilesMessageTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    MaxRecords = field("MaxRecords")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeInstanceProfilesMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeInstanceProfilesMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeMetadataModelAssessmentsMessage:
    boto3_raw_data: "type_defs.DescribeMetadataModelAssessmentsMessageTypeDef" = (
        dataclasses.field()
    )

    MigrationProjectIdentifier = field("MigrationProjectIdentifier")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    Marker = field("Marker")
    MaxRecords = field("MaxRecords")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeMetadataModelAssessmentsMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeMetadataModelAssessmentsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeMetadataModelConversionsMessage:
    boto3_raw_data: "type_defs.DescribeMetadataModelConversionsMessageTypeDef" = (
        dataclasses.field()
    )

    MigrationProjectIdentifier = field("MigrationProjectIdentifier")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    Marker = field("Marker")
    MaxRecords = field("MaxRecords")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeMetadataModelConversionsMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeMetadataModelConversionsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeMetadataModelExportsAsScriptMessage:
    boto3_raw_data: "type_defs.DescribeMetadataModelExportsAsScriptMessageTypeDef" = (
        dataclasses.field()
    )

    MigrationProjectIdentifier = field("MigrationProjectIdentifier")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    Marker = field("Marker")
    MaxRecords = field("MaxRecords")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeMetadataModelExportsAsScriptMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeMetadataModelExportsAsScriptMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeMetadataModelExportsToTargetMessage:
    boto3_raw_data: "type_defs.DescribeMetadataModelExportsToTargetMessageTypeDef" = (
        dataclasses.field()
    )

    MigrationProjectIdentifier = field("MigrationProjectIdentifier")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    Marker = field("Marker")
    MaxRecords = field("MaxRecords")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeMetadataModelExportsToTargetMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeMetadataModelExportsToTargetMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeMetadataModelImportsMessage:
    boto3_raw_data: "type_defs.DescribeMetadataModelImportsMessageTypeDef" = (
        dataclasses.field()
    )

    MigrationProjectIdentifier = field("MigrationProjectIdentifier")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    Marker = field("Marker")
    MaxRecords = field("MaxRecords")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeMetadataModelImportsMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeMetadataModelImportsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeMigrationProjectsMessage:
    boto3_raw_data: "type_defs.DescribeMigrationProjectsMessageTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    MaxRecords = field("MaxRecords")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeMigrationProjectsMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeMigrationProjectsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribePendingMaintenanceActionsMessage:
    boto3_raw_data: "type_defs.DescribePendingMaintenanceActionsMessageTypeDef" = (
        dataclasses.field()
    )

    ReplicationInstanceArn = field("ReplicationInstanceArn")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    Marker = field("Marker")
    MaxRecords = field("MaxRecords")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribePendingMaintenanceActionsMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribePendingMaintenanceActionsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRecommendationLimitationsRequest:
    boto3_raw_data: "type_defs.DescribeRecommendationLimitationsRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    MaxRecords = field("MaxRecords")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeRecommendationLimitationsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRecommendationLimitationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRecommendationsRequest:
    boto3_raw_data: "type_defs.DescribeRecommendationsRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    MaxRecords = field("MaxRecords")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeRecommendationsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRecommendationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeReplicationConfigsMessage:
    boto3_raw_data: "type_defs.DescribeReplicationConfigsMessageTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    MaxRecords = field("MaxRecords")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeReplicationConfigsMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeReplicationConfigsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeReplicationInstancesMessage:
    boto3_raw_data: "type_defs.DescribeReplicationInstancesMessageTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    MaxRecords = field("MaxRecords")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeReplicationInstancesMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeReplicationInstancesMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeReplicationSubnetGroupsMessage:
    boto3_raw_data: "type_defs.DescribeReplicationSubnetGroupsMessageTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    MaxRecords = field("MaxRecords")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeReplicationSubnetGroupsMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeReplicationSubnetGroupsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeReplicationTableStatisticsMessage:
    boto3_raw_data: "type_defs.DescribeReplicationTableStatisticsMessageTypeDef" = (
        dataclasses.field()
    )

    ReplicationConfigArn = field("ReplicationConfigArn")
    MaxRecords = field("MaxRecords")
    Marker = field("Marker")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeReplicationTableStatisticsMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeReplicationTableStatisticsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeReplicationTaskAssessmentRunsMessage:
    boto3_raw_data: "type_defs.DescribeReplicationTaskAssessmentRunsMessageTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    MaxRecords = field("MaxRecords")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeReplicationTaskAssessmentRunsMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeReplicationTaskAssessmentRunsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeReplicationTaskIndividualAssessmentsMessage:
    boto3_raw_data: (
        "type_defs.DescribeReplicationTaskIndividualAssessmentsMessageTypeDef"
    ) = dataclasses.field()

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    MaxRecords = field("MaxRecords")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeReplicationTaskIndividualAssessmentsMessageTypeDef"
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
                "type_defs.DescribeReplicationTaskIndividualAssessmentsMessageTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeReplicationTasksMessage:
    boto3_raw_data: "type_defs.DescribeReplicationTasksMessageTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    MaxRecords = field("MaxRecords")
    Marker = field("Marker")
    WithoutSettings = field("WithoutSettings")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeReplicationTasksMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeReplicationTasksMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeReplicationsMessage:
    boto3_raw_data: "type_defs.DescribeReplicationsMessageTypeDef" = dataclasses.field()

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    MaxRecords = field("MaxRecords")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeReplicationsMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeReplicationsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTableStatisticsMessage:
    boto3_raw_data: "type_defs.DescribeTableStatisticsMessageTypeDef" = (
        dataclasses.field()
    )

    ReplicationTaskArn = field("ReplicationTaskArn")
    MaxRecords = field("MaxRecords")
    Marker = field("Marker")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeTableStatisticsMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTableStatisticsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeCertificatesMessagePaginate:
    boto3_raw_data: "type_defs.DescribeCertificatesMessagePaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeCertificatesMessagePaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeCertificatesMessagePaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeConnectionsMessagePaginate:
    boto3_raw_data: "type_defs.DescribeConnectionsMessagePaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeConnectionsMessagePaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeConnectionsMessagePaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDataMigrationsMessagePaginate:
    boto3_raw_data: "type_defs.DescribeDataMigrationsMessagePaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    WithoutSettings = field("WithoutSettings")
    WithoutStatistics = field("WithoutStatistics")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeDataMigrationsMessagePaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDataMigrationsMessagePaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEndpointTypesMessagePaginate:
    boto3_raw_data: "type_defs.DescribeEndpointTypesMessagePaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeEndpointTypesMessagePaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEndpointTypesMessagePaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEndpointsMessagePaginate:
    boto3_raw_data: "type_defs.DescribeEndpointsMessagePaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeEndpointsMessagePaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEndpointsMessagePaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEventSubscriptionsMessagePaginate:
    boto3_raw_data: "type_defs.DescribeEventSubscriptionsMessagePaginateTypeDef" = (
        dataclasses.field()
    )

    SubscriptionName = field("SubscriptionName")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeEventSubscriptionsMessagePaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEventSubscriptionsMessagePaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEventsMessagePaginate:
    boto3_raw_data: "type_defs.DescribeEventsMessagePaginateTypeDef" = (
        dataclasses.field()
    )

    SourceIdentifier = field("SourceIdentifier")
    SourceType = field("SourceType")
    StartTime = field("StartTime")
    EndTime = field("EndTime")
    Duration = field("Duration")
    EventCategories = field("EventCategories")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeEventsMessagePaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEventsMessagePaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeOrderableReplicationInstancesMessagePaginate:
    boto3_raw_data: (
        "type_defs.DescribeOrderableReplicationInstancesMessagePaginateTypeDef"
    ) = dataclasses.field()

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeOrderableReplicationInstancesMessagePaginateTypeDef"
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
                "type_defs.DescribeOrderableReplicationInstancesMessagePaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeReplicationInstancesMessagePaginate:
    boto3_raw_data: "type_defs.DescribeReplicationInstancesMessagePaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeReplicationInstancesMessagePaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeReplicationInstancesMessagePaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeReplicationSubnetGroupsMessagePaginate:
    boto3_raw_data: (
        "type_defs.DescribeReplicationSubnetGroupsMessagePaginateTypeDef"
    ) = dataclasses.field()

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeReplicationSubnetGroupsMessagePaginateTypeDef"
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
                "type_defs.DescribeReplicationSubnetGroupsMessagePaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeReplicationTaskAssessmentResultsMessagePaginate:
    boto3_raw_data: (
        "type_defs.DescribeReplicationTaskAssessmentResultsMessagePaginateTypeDef"
    ) = dataclasses.field()

    ReplicationTaskArn = field("ReplicationTaskArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeReplicationTaskAssessmentResultsMessagePaginateTypeDef"
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
                "type_defs.DescribeReplicationTaskAssessmentResultsMessagePaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeReplicationTasksMessagePaginate:
    boto3_raw_data: "type_defs.DescribeReplicationTasksMessagePaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    WithoutSettings = field("WithoutSettings")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeReplicationTasksMessagePaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeReplicationTasksMessagePaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSchemasMessagePaginate:
    boto3_raw_data: "type_defs.DescribeSchemasMessagePaginateTypeDef" = (
        dataclasses.field()
    )

    EndpointArn = field("EndpointArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeSchemasMessagePaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSchemasMessagePaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTableStatisticsMessagePaginate:
    boto3_raw_data: "type_defs.DescribeTableStatisticsMessagePaginateTypeDef" = (
        dataclasses.field()
    )

    ReplicationTaskArn = field("ReplicationTaskArn")

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeTableStatisticsMessagePaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTableStatisticsMessagePaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeConnectionsMessageWait:
    boto3_raw_data: "type_defs.DescribeConnectionsMessageWaitTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    MaxRecords = field("MaxRecords")
    Marker = field("Marker")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeConnectionsMessageWaitTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeConnectionsMessageWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEndpointsMessageWait:
    boto3_raw_data: "type_defs.DescribeEndpointsMessageWaitTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    MaxRecords = field("MaxRecords")
    Marker = field("Marker")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeEndpointsMessageWaitTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEndpointsMessageWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeReplicationInstancesMessageWaitExtra:
    boto3_raw_data: "type_defs.DescribeReplicationInstancesMessageWaitExtraTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    MaxRecords = field("MaxRecords")
    Marker = field("Marker")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeReplicationInstancesMessageWaitExtraTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeReplicationInstancesMessageWaitExtraTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeReplicationInstancesMessageWait:
    boto3_raw_data: "type_defs.DescribeReplicationInstancesMessageWaitTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    MaxRecords = field("MaxRecords")
    Marker = field("Marker")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeReplicationInstancesMessageWaitTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeReplicationInstancesMessageWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeReplicationTasksMessageWaitExtraExtraExtra:
    boto3_raw_data: (
        "type_defs.DescribeReplicationTasksMessageWaitExtraExtraExtraTypeDef"
    ) = dataclasses.field()

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    MaxRecords = field("MaxRecords")
    Marker = field("Marker")
    WithoutSettings = field("WithoutSettings")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeReplicationTasksMessageWaitExtraExtraExtraTypeDef"
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
                "type_defs.DescribeReplicationTasksMessageWaitExtraExtraExtraTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeReplicationTasksMessageWaitExtraExtra:
    boto3_raw_data: "type_defs.DescribeReplicationTasksMessageWaitExtraExtraTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    MaxRecords = field("MaxRecords")
    Marker = field("Marker")
    WithoutSettings = field("WithoutSettings")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeReplicationTasksMessageWaitExtraExtraTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeReplicationTasksMessageWaitExtraExtraTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeReplicationTasksMessageWaitExtra:
    boto3_raw_data: "type_defs.DescribeReplicationTasksMessageWaitExtraTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    MaxRecords = field("MaxRecords")
    Marker = field("Marker")
    WithoutSettings = field("WithoutSettings")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeReplicationTasksMessageWaitExtraTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeReplicationTasksMessageWaitExtraTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeReplicationTasksMessageWait:
    boto3_raw_data: "type_defs.DescribeReplicationTasksMessageWaitTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Filters(self):  # pragma: no cover
        return Filter.make_many(self.boto3_raw_data["Filters"])

    MaxRecords = field("MaxRecords")
    Marker = field("Marker")
    WithoutSettings = field("WithoutSettings")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeReplicationTasksMessageWaitTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeReplicationTasksMessageWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEndpointSettingsResponse:
    boto3_raw_data: "type_defs.DescribeEndpointSettingsResponseTypeDef" = (
        dataclasses.field()
    )

    Marker = field("Marker")

    @cached_property
    def EndpointSettings(self):  # pragma: no cover
        return EndpointSetting.make_many(self.boto3_raw_data["EndpointSettings"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeEndpointSettingsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEndpointSettingsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEndpointTypesResponse:
    boto3_raw_data: "type_defs.DescribeEndpointTypesResponseTypeDef" = (
        dataclasses.field()
    )

    Marker = field("Marker")

    @cached_property
    def SupportedEndpointTypes(self):  # pragma: no cover
        return SupportedEndpointType.make_many(
            self.boto3_raw_data["SupportedEndpointTypes"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeEndpointTypesResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEndpointTypesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEngineVersionsResponse:
    boto3_raw_data: "type_defs.DescribeEngineVersionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def EngineVersions(self):  # pragma: no cover
        return EngineVersion.make_many(self.boto3_raw_data["EngineVersions"])

    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeEngineVersionsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEngineVersionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEventCategoriesResponse:
    boto3_raw_data: "type_defs.DescribeEventCategoriesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def EventCategoryGroupList(self):  # pragma: no cover
        return EventCategoryGroup.make_many(
            self.boto3_raw_data["EventCategoryGroupList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeEventCategoriesResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEventCategoriesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEventsResponse:
    boto3_raw_data: "type_defs.DescribeEventsResponseTypeDef" = dataclasses.field()

    Marker = field("Marker")

    @cached_property
    def Events(self):  # pragma: no cover
        return Event.make_many(self.boto3_raw_data["Events"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeEventsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEventsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFleetAdvisorLsaAnalysisResponse:
    boto3_raw_data: "type_defs.DescribeFleetAdvisorLsaAnalysisResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Analysis(self):  # pragma: no cover
        return FleetAdvisorLsaAnalysisResponse.make_many(
            self.boto3_raw_data["Analysis"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeFleetAdvisorLsaAnalysisResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFleetAdvisorLsaAnalysisResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFleetAdvisorSchemaObjectSummaryResponse:
    boto3_raw_data: (
        "type_defs.DescribeFleetAdvisorSchemaObjectSummaryResponseTypeDef"
    ) = dataclasses.field()

    @cached_property
    def FleetAdvisorSchemaObjects(self):  # pragma: no cover
        return FleetAdvisorSchemaObjectResponse.make_many(
            self.boto3_raw_data["FleetAdvisorSchemaObjects"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeFleetAdvisorSchemaObjectSummaryResponseTypeDef"
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
                "type_defs.DescribeFleetAdvisorSchemaObjectSummaryResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeOrderableReplicationInstancesResponse:
    boto3_raw_data: "type_defs.DescribeOrderableReplicationInstancesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def OrderableReplicationInstances(self):  # pragma: no cover
        return OrderableReplicationInstance.make_many(
            self.boto3_raw_data["OrderableReplicationInstances"]
        )

    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeOrderableReplicationInstancesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeOrderableReplicationInstancesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRecommendationLimitationsResponse:
    boto3_raw_data: "type_defs.DescribeRecommendationLimitationsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Limitations(self):  # pragma: no cover
        return Limitation.make_many(self.boto3_raw_data["Limitations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeRecommendationLimitationsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRecommendationLimitationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRefreshSchemasStatusResponse:
    boto3_raw_data: "type_defs.DescribeRefreshSchemasStatusResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def RefreshSchemasStatus(self):  # pragma: no cover
        return RefreshSchemasStatus.make_one(
            self.boto3_raw_data["RefreshSchemasStatus"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeRefreshSchemasStatusResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRefreshSchemasStatusResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RefreshSchemasResponse:
    boto3_raw_data: "type_defs.RefreshSchemasResponseTypeDef" = dataclasses.field()

    @cached_property
    def RefreshSchemasStatus(self):  # pragma: no cover
        return RefreshSchemasStatus.make_one(
            self.boto3_raw_data["RefreshSchemasStatus"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RefreshSchemasResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RefreshSchemasResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeReplicationInstanceTaskLogsResponse:
    boto3_raw_data: "type_defs.DescribeReplicationInstanceTaskLogsResponseTypeDef" = (
        dataclasses.field()
    )

    ReplicationInstanceArn = field("ReplicationInstanceArn")

    @cached_property
    def ReplicationInstanceTaskLogs(self):  # pragma: no cover
        return ReplicationInstanceTaskLog.make_many(
            self.boto3_raw_data["ReplicationInstanceTaskLogs"]
        )

    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeReplicationInstanceTaskLogsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeReplicationInstanceTaskLogsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeReplicationTableStatisticsResponse:
    boto3_raw_data: "type_defs.DescribeReplicationTableStatisticsResponseTypeDef" = (
        dataclasses.field()
    )

    ReplicationConfigArn = field("ReplicationConfigArn")
    Marker = field("Marker")

    @cached_property
    def ReplicationTableStatistics(self):  # pragma: no cover
        return TableStatistics.make_many(
            self.boto3_raw_data["ReplicationTableStatistics"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeReplicationTableStatisticsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeReplicationTableStatisticsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTableStatisticsResponse:
    boto3_raw_data: "type_defs.DescribeTableStatisticsResponseTypeDef" = (
        dataclasses.field()
    )

    ReplicationTaskArn = field("ReplicationTaskArn")

    @cached_property
    def TableStatistics(self):  # pragma: no cover
        return TableStatistics.make_many(self.boto3_raw_data["TableStatistics"])

    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeTableStatisticsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTableStatisticsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeReplicationTaskAssessmentResultsResponse:
    boto3_raw_data: (
        "type_defs.DescribeReplicationTaskAssessmentResultsResponseTypeDef"
    ) = dataclasses.field()

    Marker = field("Marker")
    BucketName = field("BucketName")

    @cached_property
    def ReplicationTaskAssessmentResults(self):  # pragma: no cover
        return ReplicationTaskAssessmentResult.make_many(
            self.boto3_raw_data["ReplicationTaskAssessmentResults"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeReplicationTaskAssessmentResultsResponseTypeDef"
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
                "type_defs.DescribeReplicationTaskAssessmentResultsResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeReplicationTaskIndividualAssessmentsResponse:
    boto3_raw_data: (
        "type_defs.DescribeReplicationTaskIndividualAssessmentsResponseTypeDef"
    ) = dataclasses.field()

    Marker = field("Marker")

    @cached_property
    def ReplicationTaskIndividualAssessments(self):  # pragma: no cover
        return ReplicationTaskIndividualAssessment.make_many(
            self.boto3_raw_data["ReplicationTaskIndividualAssessments"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeReplicationTaskIndividualAssessmentsResponseTypeDef"
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
                "type_defs.DescribeReplicationTaskIndividualAssessmentsResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Endpoint:
    boto3_raw_data: "type_defs.EndpointTypeDef" = dataclasses.field()

    EndpointIdentifier = field("EndpointIdentifier")
    EndpointType = field("EndpointType")
    EngineName = field("EngineName")
    EngineDisplayName = field("EngineDisplayName")
    Username = field("Username")
    ServerName = field("ServerName")
    Port = field("Port")
    DatabaseName = field("DatabaseName")
    ExtraConnectionAttributes = field("ExtraConnectionAttributes")
    Status = field("Status")
    KmsKeyId = field("KmsKeyId")
    EndpointArn = field("EndpointArn")
    CertificateArn = field("CertificateArn")
    SslMode = field("SslMode")
    ServiceAccessRoleArn = field("ServiceAccessRoleArn")
    ExternalTableDefinition = field("ExternalTableDefinition")
    ExternalId = field("ExternalId")

    @cached_property
    def DynamoDbSettings(self):  # pragma: no cover
        return DynamoDbSettings.make_one(self.boto3_raw_data["DynamoDbSettings"])

    @cached_property
    def S3Settings(self):  # pragma: no cover
        return S3Settings.make_one(self.boto3_raw_data["S3Settings"])

    @cached_property
    def DmsTransferSettings(self):  # pragma: no cover
        return DmsTransferSettings.make_one(self.boto3_raw_data["DmsTransferSettings"])

    @cached_property
    def MongoDbSettings(self):  # pragma: no cover
        return MongoDbSettings.make_one(self.boto3_raw_data["MongoDbSettings"])

    @cached_property
    def KinesisSettings(self):  # pragma: no cover
        return KinesisSettings.make_one(self.boto3_raw_data["KinesisSettings"])

    @cached_property
    def KafkaSettings(self):  # pragma: no cover
        return KafkaSettings.make_one(self.boto3_raw_data["KafkaSettings"])

    @cached_property
    def ElasticsearchSettings(self):  # pragma: no cover
        return ElasticsearchSettings.make_one(
            self.boto3_raw_data["ElasticsearchSettings"]
        )

    @cached_property
    def NeptuneSettings(self):  # pragma: no cover
        return NeptuneSettings.make_one(self.boto3_raw_data["NeptuneSettings"])

    @cached_property
    def RedshiftSettings(self):  # pragma: no cover
        return RedshiftSettings.make_one(self.boto3_raw_data["RedshiftSettings"])

    @cached_property
    def PostgreSQLSettings(self):  # pragma: no cover
        return PostgreSQLSettings.make_one(self.boto3_raw_data["PostgreSQLSettings"])

    @cached_property
    def MySQLSettings(self):  # pragma: no cover
        return MySQLSettings.make_one(self.boto3_raw_data["MySQLSettings"])

    @cached_property
    def OracleSettings(self):  # pragma: no cover
        return OracleSettingsOutput.make_one(self.boto3_raw_data["OracleSettings"])

    @cached_property
    def SybaseSettings(self):  # pragma: no cover
        return SybaseSettings.make_one(self.boto3_raw_data["SybaseSettings"])

    @cached_property
    def MicrosoftSQLServerSettings(self):  # pragma: no cover
        return MicrosoftSQLServerSettings.make_one(
            self.boto3_raw_data["MicrosoftSQLServerSettings"]
        )

    @cached_property
    def IBMDb2Settings(self):  # pragma: no cover
        return IBMDb2Settings.make_one(self.boto3_raw_data["IBMDb2Settings"])

    @cached_property
    def DocDbSettings(self):  # pragma: no cover
        return DocDbSettings.make_one(self.boto3_raw_data["DocDbSettings"])

    @cached_property
    def RedisSettings(self):  # pragma: no cover
        return RedisSettings.make_one(self.boto3_raw_data["RedisSettings"])

    @cached_property
    def GcpMySQLSettings(self):  # pragma: no cover
        return GcpMySQLSettings.make_one(self.boto3_raw_data["GcpMySQLSettings"])

    @cached_property
    def TimestreamSettings(self):  # pragma: no cover
        return TimestreamSettings.make_one(self.boto3_raw_data["TimestreamSettings"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EndpointTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EndpointTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExportMetadataModelAssessmentResponse:
    boto3_raw_data: "type_defs.ExportMetadataModelAssessmentResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PdfReport(self):  # pragma: no cover
        return ExportMetadataModelAssessmentResultEntry.make_one(
            self.boto3_raw_data["PdfReport"]
        )

    @cached_property
    def CsvReport(self):  # pragma: no cover
        return ExportMetadataModelAssessmentResultEntry.make_one(
            self.boto3_raw_data["CsvReport"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ExportMetadataModelAssessmentResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExportMetadataModelAssessmentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourcePendingMaintenanceActions:
    boto3_raw_data: "type_defs.ResourcePendingMaintenanceActionsTypeDef" = (
        dataclasses.field()
    )

    ResourceIdentifier = field("ResourceIdentifier")

    @cached_property
    def PendingMaintenanceActionDetails(self):  # pragma: no cover
        return PendingMaintenanceAction.make_many(
            self.boto3_raw_data["PendingMaintenanceActionDetails"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ResourcePendingMaintenanceActionsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResourcePendingMaintenanceActionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PremigrationAssessmentStatus:
    boto3_raw_data: "type_defs.PremigrationAssessmentStatusTypeDef" = (
        dataclasses.field()
    )

    PremigrationAssessmentRunArn = field("PremigrationAssessmentRunArn")
    FailOnAssessmentFailure = field("FailOnAssessmentFailure")
    Status = field("Status")
    PremigrationAssessmentRunCreationDate = field(
        "PremigrationAssessmentRunCreationDate"
    )

    @cached_property
    def AssessmentProgress(self):  # pragma: no cover
        return ReplicationTaskAssessmentRunProgress.make_one(
            self.boto3_raw_data["AssessmentProgress"]
        )

    LastFailureMessage = field("LastFailureMessage")
    ResultLocationBucket = field("ResultLocationBucket")
    ResultLocationFolder = field("ResultLocationFolder")
    ResultEncryptionMode = field("ResultEncryptionMode")
    ResultKmsKeyArn = field("ResultKmsKeyArn")

    @cached_property
    def ResultStatistic(self):  # pragma: no cover
        return ReplicationTaskAssessmentRunResultStatistic.make_one(
            self.boto3_raw_data["ResultStatistic"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PremigrationAssessmentStatusTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PremigrationAssessmentStatusTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReplicationTaskAssessmentRun:
    boto3_raw_data: "type_defs.ReplicationTaskAssessmentRunTypeDef" = (
        dataclasses.field()
    )

    ReplicationTaskAssessmentRunArn = field("ReplicationTaskAssessmentRunArn")
    ReplicationTaskArn = field("ReplicationTaskArn")
    Status = field("Status")
    ReplicationTaskAssessmentRunCreationDate = field(
        "ReplicationTaskAssessmentRunCreationDate"
    )

    @cached_property
    def AssessmentProgress(self):  # pragma: no cover
        return ReplicationTaskAssessmentRunProgress.make_one(
            self.boto3_raw_data["AssessmentProgress"]
        )

    LastFailureMessage = field("LastFailureMessage")
    ServiceAccessRoleArn = field("ServiceAccessRoleArn")
    ResultLocationBucket = field("ResultLocationBucket")
    ResultLocationFolder = field("ResultLocationFolder")
    ResultEncryptionMode = field("ResultEncryptionMode")
    ResultKmsKeyArn = field("ResultKmsKeyArn")
    AssessmentRunName = field("AssessmentRunName")
    IsLatestTaskAssessmentRun = field("IsLatestTaskAssessmentRun")

    @cached_property
    def ResultStatistic(self):  # pragma: no cover
        return ReplicationTaskAssessmentRunResultStatistic.make_one(
            self.boto3_raw_data["ResultStatistic"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReplicationTaskAssessmentRunTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReplicationTaskAssessmentRunTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RdsRecommendation:
    boto3_raw_data: "type_defs.RdsRecommendationTypeDef" = dataclasses.field()

    @cached_property
    def RequirementsToTarget(self):  # pragma: no cover
        return RdsRequirements.make_one(self.boto3_raw_data["RequirementsToTarget"])

    @cached_property
    def TargetConfiguration(self):  # pragma: no cover
        return RdsConfiguration.make_one(self.boto3_raw_data["TargetConfiguration"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RdsRecommendationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RdsRecommendationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartRecommendationsRequestEntry:
    boto3_raw_data: "type_defs.StartRecommendationsRequestEntryTypeDef" = (
        dataclasses.field()
    )

    DatabaseId = field("DatabaseId")

    @cached_property
    def Settings(self):  # pragma: no cover
        return RecommendationSettings.make_one(self.boto3_raw_data["Settings"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartRecommendationsRequestEntryTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartRecommendationsRequestEntryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartRecommendationsRequest:
    boto3_raw_data: "type_defs.StartRecommendationsRequestTypeDef" = dataclasses.field()

    DatabaseId = field("DatabaseId")

    @cached_property
    def Settings(self):  # pragma: no cover
        return RecommendationSettings.make_one(self.boto3_raw_data["Settings"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartRecommendationsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartRecommendationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReloadReplicationTablesMessage:
    boto3_raw_data: "type_defs.ReloadReplicationTablesMessageTypeDef" = (
        dataclasses.field()
    )

    ReplicationConfigArn = field("ReplicationConfigArn")

    @cached_property
    def TablesToReload(self):  # pragma: no cover
        return TableToReload.make_many(self.boto3_raw_data["TablesToReload"])

    ReloadOption = field("ReloadOption")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ReloadReplicationTablesMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReloadReplicationTablesMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReloadTablesMessage:
    boto3_raw_data: "type_defs.ReloadTablesMessageTypeDef" = dataclasses.field()

    ReplicationTaskArn = field("ReplicationTaskArn")

    @cached_property
    def TablesToReload(self):  # pragma: no cover
        return TableToReload.make_many(self.boto3_raw_data["TablesToReload"])

    ReloadOption = field("ReloadOption")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReloadTablesMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReloadTablesMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReplicationTask:
    boto3_raw_data: "type_defs.ReplicationTaskTypeDef" = dataclasses.field()

    ReplicationTaskIdentifier = field("ReplicationTaskIdentifier")
    SourceEndpointArn = field("SourceEndpointArn")
    TargetEndpointArn = field("TargetEndpointArn")
    ReplicationInstanceArn = field("ReplicationInstanceArn")
    MigrationType = field("MigrationType")
    TableMappings = field("TableMappings")
    ReplicationTaskSettings = field("ReplicationTaskSettings")
    Status = field("Status")
    LastFailureMessage = field("LastFailureMessage")
    StopReason = field("StopReason")
    ReplicationTaskCreationDate = field("ReplicationTaskCreationDate")
    ReplicationTaskStartDate = field("ReplicationTaskStartDate")
    CdcStartPosition = field("CdcStartPosition")
    CdcStopPosition = field("CdcStopPosition")
    RecoveryCheckpoint = field("RecoveryCheckpoint")
    ReplicationTaskArn = field("ReplicationTaskArn")

    @cached_property
    def ReplicationTaskStats(self):  # pragma: no cover
        return ReplicationTaskStats.make_one(
            self.boto3_raw_data["ReplicationTaskStats"]
        )

    TaskData = field("TaskData")
    TargetReplicationInstanceArn = field("TargetReplicationInstanceArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ReplicationTaskTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ReplicationTaskTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SchemaResponse:
    boto3_raw_data: "type_defs.SchemaResponseTypeDef" = dataclasses.field()

    CodeLineCount = field("CodeLineCount")
    CodeSize = field("CodeSize")
    Complexity = field("Complexity")

    @cached_property
    def Server(self):  # pragma: no cover
        return ServerShortInfoResponse.make_one(self.boto3_raw_data["Server"])

    @cached_property
    def DatabaseInstance(self):  # pragma: no cover
        return DatabaseShortInfoResponse.make_one(
            self.boto3_raw_data["DatabaseInstance"]
        )

    SchemaId = field("SchemaId")
    SchemaName = field("SchemaName")

    @cached_property
    def OriginalSchema(self):  # pragma: no cover
        return SchemaShortInfoResponse.make_one(self.boto3_raw_data["OriginalSchema"])

    Similarity = field("Similarity")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SchemaResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SchemaResponseTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReplicationSubnetGroup:
    boto3_raw_data: "type_defs.ReplicationSubnetGroupTypeDef" = dataclasses.field()

    ReplicationSubnetGroupIdentifier = field("ReplicationSubnetGroupIdentifier")
    ReplicationSubnetGroupDescription = field("ReplicationSubnetGroupDescription")
    VpcId = field("VpcId")
    SubnetGroupStatus = field("SubnetGroupStatus")

    @cached_property
    def Subnets(self):  # pragma: no cover
        return Subnet.make_many(self.boto3_raw_data["Subnets"])

    SupportedNetworkTypes = field("SupportedNetworkTypes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReplicationSubnetGroupTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReplicationSubnetGroupTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFleetAdvisorCollectorsResponse:
    boto3_raw_data: "type_defs.DescribeFleetAdvisorCollectorsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Collectors(self):  # pragma: no cover
        return CollectorResponse.make_many(self.boto3_raw_data["Collectors"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeFleetAdvisorCollectorsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFleetAdvisorCollectorsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateReplicationConfigResponse:
    boto3_raw_data: "type_defs.CreateReplicationConfigResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ReplicationConfig(self):  # pragma: no cover
        return ReplicationConfig.make_one(self.boto3_raw_data["ReplicationConfig"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateReplicationConfigResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateReplicationConfigResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteReplicationConfigResponse:
    boto3_raw_data: "type_defs.DeleteReplicationConfigResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ReplicationConfig(self):  # pragma: no cover
        return ReplicationConfig.make_one(self.boto3_raw_data["ReplicationConfig"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteReplicationConfigResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteReplicationConfigResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeReplicationConfigsResponse:
    boto3_raw_data: "type_defs.DescribeReplicationConfigsResponseTypeDef" = (
        dataclasses.field()
    )

    Marker = field("Marker")

    @cached_property
    def ReplicationConfigs(self):  # pragma: no cover
        return ReplicationConfig.make_many(self.boto3_raw_data["ReplicationConfigs"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeReplicationConfigsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeReplicationConfigsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyReplicationConfigResponse:
    boto3_raw_data: "type_defs.ModifyReplicationConfigResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ReplicationConfig(self):  # pragma: no cover
        return ReplicationConfig.make_one(self.boto3_raw_data["ReplicationConfig"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ModifyReplicationConfigResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyReplicationConfigResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateReplicationConfigMessage:
    boto3_raw_data: "type_defs.CreateReplicationConfigMessageTypeDef" = (
        dataclasses.field()
    )

    ReplicationConfigIdentifier = field("ReplicationConfigIdentifier")
    SourceEndpointArn = field("SourceEndpointArn")
    TargetEndpointArn = field("TargetEndpointArn")
    ComputeConfig = field("ComputeConfig")
    ReplicationType = field("ReplicationType")
    TableMappings = field("TableMappings")
    ReplicationSettings = field("ReplicationSettings")
    SupplementalSettings = field("SupplementalSettings")
    ResourceIdentifier = field("ResourceIdentifier")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateReplicationConfigMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateReplicationConfigMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyReplicationConfigMessage:
    boto3_raw_data: "type_defs.ModifyReplicationConfigMessageTypeDef" = (
        dataclasses.field()
    )

    ReplicationConfigArn = field("ReplicationConfigArn")
    ReplicationConfigIdentifier = field("ReplicationConfigIdentifier")
    ReplicationType = field("ReplicationType")
    TableMappings = field("TableMappings")
    ReplicationSettings = field("ReplicationSettings")
    SupplementalSettings = field("SupplementalSettings")
    ComputeConfig = field("ComputeConfig")
    SourceEndpointArn = field("SourceEndpointArn")
    TargetEndpointArn = field("TargetEndpointArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ModifyReplicationConfigMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyReplicationConfigMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDataMigrationResponse:
    boto3_raw_data: "type_defs.CreateDataMigrationResponseTypeDef" = dataclasses.field()

    @cached_property
    def DataMigration(self):  # pragma: no cover
        return DataMigration.make_one(self.boto3_raw_data["DataMigration"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDataMigrationResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDataMigrationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDataMigrationResponse:
    boto3_raw_data: "type_defs.DeleteDataMigrationResponseTypeDef" = dataclasses.field()

    @cached_property
    def DataMigration(self):  # pragma: no cover
        return DataMigration.make_one(self.boto3_raw_data["DataMigration"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDataMigrationResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDataMigrationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDataMigrationsResponse:
    boto3_raw_data: "type_defs.DescribeDataMigrationsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DataMigrations(self):  # pragma: no cover
        return DataMigration.make_many(self.boto3_raw_data["DataMigrations"])

    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeDataMigrationsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDataMigrationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyDataMigrationResponse:
    boto3_raw_data: "type_defs.ModifyDataMigrationResponseTypeDef" = dataclasses.field()

    @cached_property
    def DataMigration(self):  # pragma: no cover
        return DataMigration.make_one(self.boto3_raw_data["DataMigration"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ModifyDataMigrationResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyDataMigrationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartDataMigrationResponse:
    boto3_raw_data: "type_defs.StartDataMigrationResponseTypeDef" = dataclasses.field()

    @cached_property
    def DataMigration(self):  # pragma: no cover
        return DataMigration.make_one(self.boto3_raw_data["DataMigration"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartDataMigrationResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartDataMigrationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopDataMigrationResponse:
    boto3_raw_data: "type_defs.StopDataMigrationResponseTypeDef" = dataclasses.field()

    @cached_property
    def DataMigration(self):  # pragma: no cover
        return DataMigration.make_one(self.boto3_raw_data["DataMigration"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopDataMigrationResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopDataMigrationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateMigrationProjectResponse:
    boto3_raw_data: "type_defs.CreateMigrationProjectResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def MigrationProject(self):  # pragma: no cover
        return MigrationProject.make_one(self.boto3_raw_data["MigrationProject"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateMigrationProjectResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateMigrationProjectResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteMigrationProjectResponse:
    boto3_raw_data: "type_defs.DeleteMigrationProjectResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def MigrationProject(self):  # pragma: no cover
        return MigrationProject.make_one(self.boto3_raw_data["MigrationProject"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteMigrationProjectResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteMigrationProjectResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeMigrationProjectsResponse:
    boto3_raw_data: "type_defs.DescribeMigrationProjectsResponseTypeDef" = (
        dataclasses.field()
    )

    Marker = field("Marker")

    @cached_property
    def MigrationProjects(self):  # pragma: no cover
        return MigrationProject.make_many(self.boto3_raw_data["MigrationProjects"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeMigrationProjectsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeMigrationProjectsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyMigrationProjectResponse:
    boto3_raw_data: "type_defs.ModifyMigrationProjectResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def MigrationProject(self):  # pragma: no cover
        return MigrationProject.make_one(self.boto3_raw_data["MigrationProject"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ModifyMigrationProjectResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyMigrationProjectResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDataProviderMessage:
    boto3_raw_data: "type_defs.CreateDataProviderMessageTypeDef" = dataclasses.field()

    Engine = field("Engine")

    @cached_property
    def Settings(self):  # pragma: no cover
        return DataProviderSettings.make_one(self.boto3_raw_data["Settings"])

    DataProviderName = field("DataProviderName")
    Description = field("Description")
    Virtual = field("Virtual")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDataProviderMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDataProviderMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataProvider:
    boto3_raw_data: "type_defs.DataProviderTypeDef" = dataclasses.field()

    DataProviderName = field("DataProviderName")
    DataProviderArn = field("DataProviderArn")
    DataProviderCreationTime = field("DataProviderCreationTime")
    Description = field("Description")
    Engine = field("Engine")
    Virtual = field("Virtual")

    @cached_property
    def Settings(self):  # pragma: no cover
        return DataProviderSettings.make_one(self.boto3_raw_data["Settings"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DataProviderTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DataProviderTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyDataProviderMessage:
    boto3_raw_data: "type_defs.ModifyDataProviderMessageTypeDef" = dataclasses.field()

    DataProviderIdentifier = field("DataProviderIdentifier")
    DataProviderName = field("DataProviderName")
    Description = field("Description")
    Engine = field("Engine")
    Virtual = field("Virtual")
    ExactSettings = field("ExactSettings")

    @cached_property
    def Settings(self):  # pragma: no cover
        return DataProviderSettings.make_one(self.boto3_raw_data["Settings"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ModifyDataProviderMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyDataProviderMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFleetAdvisorDatabasesResponse:
    boto3_raw_data: "type_defs.DescribeFleetAdvisorDatabasesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Databases(self):  # pragma: no cover
        return DatabaseResponse.make_many(self.boto3_raw_data["Databases"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeFleetAdvisorDatabasesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFleetAdvisorDatabasesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SchemaConversionRequest:
    boto3_raw_data: "type_defs.SchemaConversionRequestTypeDef" = dataclasses.field()

    Status = field("Status")
    RequestIdentifier = field("RequestIdentifier")
    MigrationProjectArn = field("MigrationProjectArn")

    @cached_property
    def Error(self):  # pragma: no cover
        return ErrorDetails.make_one(self.boto3_raw_data["Error"])

    @cached_property
    def ExportSqlDetails(self):  # pragma: no cover
        return ExportSqlDetails.make_one(self.boto3_raw_data["ExportSqlDetails"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SchemaConversionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SchemaConversionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateEndpointResponse:
    boto3_raw_data: "type_defs.CreateEndpointResponseTypeDef" = dataclasses.field()

    @cached_property
    def Endpoint(self):  # pragma: no cover
        return Endpoint.make_one(self.boto3_raw_data["Endpoint"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateEndpointResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateEndpointResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteEndpointResponse:
    boto3_raw_data: "type_defs.DeleteEndpointResponseTypeDef" = dataclasses.field()

    @cached_property
    def Endpoint(self):  # pragma: no cover
        return Endpoint.make_one(self.boto3_raw_data["Endpoint"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteEndpointResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteEndpointResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEndpointsResponse:
    boto3_raw_data: "type_defs.DescribeEndpointsResponseTypeDef" = dataclasses.field()

    Marker = field("Marker")

    @cached_property
    def Endpoints(self):  # pragma: no cover
        return Endpoint.make_many(self.boto3_raw_data["Endpoints"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeEndpointsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEndpointsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyEndpointResponse:
    boto3_raw_data: "type_defs.ModifyEndpointResponseTypeDef" = dataclasses.field()

    @cached_property
    def Endpoint(self):  # pragma: no cover
        return Endpoint.make_one(self.boto3_raw_data["Endpoint"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ModifyEndpointResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyEndpointResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateEndpointMessage:
    boto3_raw_data: "type_defs.CreateEndpointMessageTypeDef" = dataclasses.field()

    EndpointIdentifier = field("EndpointIdentifier")
    EndpointType = field("EndpointType")
    EngineName = field("EngineName")
    Username = field("Username")
    Password = field("Password")
    ServerName = field("ServerName")
    Port = field("Port")
    DatabaseName = field("DatabaseName")
    ExtraConnectionAttributes = field("ExtraConnectionAttributes")
    KmsKeyId = field("KmsKeyId")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    CertificateArn = field("CertificateArn")
    SslMode = field("SslMode")
    ServiceAccessRoleArn = field("ServiceAccessRoleArn")
    ExternalTableDefinition = field("ExternalTableDefinition")

    @cached_property
    def DynamoDbSettings(self):  # pragma: no cover
        return DynamoDbSettings.make_one(self.boto3_raw_data["DynamoDbSettings"])

    @cached_property
    def S3Settings(self):  # pragma: no cover
        return S3Settings.make_one(self.boto3_raw_data["S3Settings"])

    @cached_property
    def DmsTransferSettings(self):  # pragma: no cover
        return DmsTransferSettings.make_one(self.boto3_raw_data["DmsTransferSettings"])

    @cached_property
    def MongoDbSettings(self):  # pragma: no cover
        return MongoDbSettings.make_one(self.boto3_raw_data["MongoDbSettings"])

    @cached_property
    def KinesisSettings(self):  # pragma: no cover
        return KinesisSettings.make_one(self.boto3_raw_data["KinesisSettings"])

    @cached_property
    def KafkaSettings(self):  # pragma: no cover
        return KafkaSettings.make_one(self.boto3_raw_data["KafkaSettings"])

    @cached_property
    def ElasticsearchSettings(self):  # pragma: no cover
        return ElasticsearchSettings.make_one(
            self.boto3_raw_data["ElasticsearchSettings"]
        )

    @cached_property
    def NeptuneSettings(self):  # pragma: no cover
        return NeptuneSettings.make_one(self.boto3_raw_data["NeptuneSettings"])

    @cached_property
    def RedshiftSettings(self):  # pragma: no cover
        return RedshiftSettings.make_one(self.boto3_raw_data["RedshiftSettings"])

    @cached_property
    def PostgreSQLSettings(self):  # pragma: no cover
        return PostgreSQLSettings.make_one(self.boto3_raw_data["PostgreSQLSettings"])

    @cached_property
    def MySQLSettings(self):  # pragma: no cover
        return MySQLSettings.make_one(self.boto3_raw_data["MySQLSettings"])

    OracleSettings = field("OracleSettings")

    @cached_property
    def SybaseSettings(self):  # pragma: no cover
        return SybaseSettings.make_one(self.boto3_raw_data["SybaseSettings"])

    @cached_property
    def MicrosoftSQLServerSettings(self):  # pragma: no cover
        return MicrosoftSQLServerSettings.make_one(
            self.boto3_raw_data["MicrosoftSQLServerSettings"]
        )

    @cached_property
    def IBMDb2Settings(self):  # pragma: no cover
        return IBMDb2Settings.make_one(self.boto3_raw_data["IBMDb2Settings"])

    ResourceIdentifier = field("ResourceIdentifier")

    @cached_property
    def DocDbSettings(self):  # pragma: no cover
        return DocDbSettings.make_one(self.boto3_raw_data["DocDbSettings"])

    @cached_property
    def RedisSettings(self):  # pragma: no cover
        return RedisSettings.make_one(self.boto3_raw_data["RedisSettings"])

    @cached_property
    def GcpMySQLSettings(self):  # pragma: no cover
        return GcpMySQLSettings.make_one(self.boto3_raw_data["GcpMySQLSettings"])

    @cached_property
    def TimestreamSettings(self):  # pragma: no cover
        return TimestreamSettings.make_one(self.boto3_raw_data["TimestreamSettings"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateEndpointMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateEndpointMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyEndpointMessage:
    boto3_raw_data: "type_defs.ModifyEndpointMessageTypeDef" = dataclasses.field()

    EndpointArn = field("EndpointArn")
    EndpointIdentifier = field("EndpointIdentifier")
    EndpointType = field("EndpointType")
    EngineName = field("EngineName")
    Username = field("Username")
    Password = field("Password")
    ServerName = field("ServerName")
    Port = field("Port")
    DatabaseName = field("DatabaseName")
    ExtraConnectionAttributes = field("ExtraConnectionAttributes")
    CertificateArn = field("CertificateArn")
    SslMode = field("SslMode")
    ServiceAccessRoleArn = field("ServiceAccessRoleArn")
    ExternalTableDefinition = field("ExternalTableDefinition")

    @cached_property
    def DynamoDbSettings(self):  # pragma: no cover
        return DynamoDbSettings.make_one(self.boto3_raw_data["DynamoDbSettings"])

    @cached_property
    def S3Settings(self):  # pragma: no cover
        return S3Settings.make_one(self.boto3_raw_data["S3Settings"])

    @cached_property
    def DmsTransferSettings(self):  # pragma: no cover
        return DmsTransferSettings.make_one(self.boto3_raw_data["DmsTransferSettings"])

    @cached_property
    def MongoDbSettings(self):  # pragma: no cover
        return MongoDbSettings.make_one(self.boto3_raw_data["MongoDbSettings"])

    @cached_property
    def KinesisSettings(self):  # pragma: no cover
        return KinesisSettings.make_one(self.boto3_raw_data["KinesisSettings"])

    @cached_property
    def KafkaSettings(self):  # pragma: no cover
        return KafkaSettings.make_one(self.boto3_raw_data["KafkaSettings"])

    @cached_property
    def ElasticsearchSettings(self):  # pragma: no cover
        return ElasticsearchSettings.make_one(
            self.boto3_raw_data["ElasticsearchSettings"]
        )

    @cached_property
    def NeptuneSettings(self):  # pragma: no cover
        return NeptuneSettings.make_one(self.boto3_raw_data["NeptuneSettings"])

    @cached_property
    def RedshiftSettings(self):  # pragma: no cover
        return RedshiftSettings.make_one(self.boto3_raw_data["RedshiftSettings"])

    @cached_property
    def PostgreSQLSettings(self):  # pragma: no cover
        return PostgreSQLSettings.make_one(self.boto3_raw_data["PostgreSQLSettings"])

    @cached_property
    def MySQLSettings(self):  # pragma: no cover
        return MySQLSettings.make_one(self.boto3_raw_data["MySQLSettings"])

    OracleSettings = field("OracleSettings")

    @cached_property
    def SybaseSettings(self):  # pragma: no cover
        return SybaseSettings.make_one(self.boto3_raw_data["SybaseSettings"])

    @cached_property
    def MicrosoftSQLServerSettings(self):  # pragma: no cover
        return MicrosoftSQLServerSettings.make_one(
            self.boto3_raw_data["MicrosoftSQLServerSettings"]
        )

    @cached_property
    def IBMDb2Settings(self):  # pragma: no cover
        return IBMDb2Settings.make_one(self.boto3_raw_data["IBMDb2Settings"])

    @cached_property
    def DocDbSettings(self):  # pragma: no cover
        return DocDbSettings.make_one(self.boto3_raw_data["DocDbSettings"])

    @cached_property
    def RedisSettings(self):  # pragma: no cover
        return RedisSettings.make_one(self.boto3_raw_data["RedisSettings"])

    ExactSettings = field("ExactSettings")

    @cached_property
    def GcpMySQLSettings(self):  # pragma: no cover
        return GcpMySQLSettings.make_one(self.boto3_raw_data["GcpMySQLSettings"])

    @cached_property
    def TimestreamSettings(self):  # pragma: no cover
        return TimestreamSettings.make_one(self.boto3_raw_data["TimestreamSettings"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ModifyEndpointMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyEndpointMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApplyPendingMaintenanceActionResponse:
    boto3_raw_data: "type_defs.ApplyPendingMaintenanceActionResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ResourcePendingMaintenanceActions(self):  # pragma: no cover
        return ResourcePendingMaintenanceActions.make_one(
            self.boto3_raw_data["ResourcePendingMaintenanceActions"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ApplyPendingMaintenanceActionResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ApplyPendingMaintenanceActionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribePendingMaintenanceActionsResponse:
    boto3_raw_data: "type_defs.DescribePendingMaintenanceActionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PendingMaintenanceActions(self):  # pragma: no cover
        return ResourcePendingMaintenanceActions.make_many(
            self.boto3_raw_data["PendingMaintenanceActions"]
        )

    Marker = field("Marker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribePendingMaintenanceActionsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribePendingMaintenanceActionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Replication:
    boto3_raw_data: "type_defs.ReplicationTypeDef" = dataclasses.field()

    ReplicationConfigIdentifier = field("ReplicationConfigIdentifier")
    ReplicationConfigArn = field("ReplicationConfigArn")
    SourceEndpointArn = field("SourceEndpointArn")
    TargetEndpointArn = field("TargetEndpointArn")
    ReplicationType = field("ReplicationType")
    Status = field("Status")

    @cached_property
    def ProvisionData(self):  # pragma: no cover
        return ProvisionData.make_one(self.boto3_raw_data["ProvisionData"])

    @cached_property
    def PremigrationAssessmentStatuses(self):  # pragma: no cover
        return PremigrationAssessmentStatus.make_many(
            self.boto3_raw_data["PremigrationAssessmentStatuses"]
        )

    StopReason = field("StopReason")
    FailureMessages = field("FailureMessages")

    @cached_property
    def ReplicationStats(self):  # pragma: no cover
        return ReplicationStats.make_one(self.boto3_raw_data["ReplicationStats"])

    StartReplicationType = field("StartReplicationType")
    CdcStartTime = field("CdcStartTime")
    CdcStartPosition = field("CdcStartPosition")
    CdcStopPosition = field("CdcStopPosition")
    RecoveryCheckpoint = field("RecoveryCheckpoint")
    ReplicationCreateTime = field("ReplicationCreateTime")
    ReplicationUpdateTime = field("ReplicationUpdateTime")
    ReplicationLastStopTime = field("ReplicationLastStopTime")
    ReplicationDeprovisionTime = field("ReplicationDeprovisionTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ReplicationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ReplicationTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelReplicationTaskAssessmentRunResponse:
    boto3_raw_data: "type_defs.CancelReplicationTaskAssessmentRunResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ReplicationTaskAssessmentRun(self):  # pragma: no cover
        return ReplicationTaskAssessmentRun.make_one(
            self.boto3_raw_data["ReplicationTaskAssessmentRun"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CancelReplicationTaskAssessmentRunResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelReplicationTaskAssessmentRunResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteReplicationTaskAssessmentRunResponse:
    boto3_raw_data: "type_defs.DeleteReplicationTaskAssessmentRunResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ReplicationTaskAssessmentRun(self):  # pragma: no cover
        return ReplicationTaskAssessmentRun.make_one(
            self.boto3_raw_data["ReplicationTaskAssessmentRun"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteReplicationTaskAssessmentRunResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteReplicationTaskAssessmentRunResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeReplicationTaskAssessmentRunsResponse:
    boto3_raw_data: "type_defs.DescribeReplicationTaskAssessmentRunsResponseTypeDef" = (
        dataclasses.field()
    )

    Marker = field("Marker")

    @cached_property
    def ReplicationTaskAssessmentRuns(self):  # pragma: no cover
        return ReplicationTaskAssessmentRun.make_many(
            self.boto3_raw_data["ReplicationTaskAssessmentRuns"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeReplicationTaskAssessmentRunsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeReplicationTaskAssessmentRunsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartReplicationTaskAssessmentRunResponse:
    boto3_raw_data: "type_defs.StartReplicationTaskAssessmentRunResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ReplicationTaskAssessmentRun(self):  # pragma: no cover
        return ReplicationTaskAssessmentRun.make_one(
            self.boto3_raw_data["ReplicationTaskAssessmentRun"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartReplicationTaskAssessmentRunResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartReplicationTaskAssessmentRunResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecommendationData:
    boto3_raw_data: "type_defs.RecommendationDataTypeDef" = dataclasses.field()

    @cached_property
    def RdsEngine(self):  # pragma: no cover
        return RdsRecommendation.make_one(self.boto3_raw_data["RdsEngine"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RecommendationDataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RecommendationDataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchStartRecommendationsRequest:
    boto3_raw_data: "type_defs.BatchStartRecommendationsRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Data(self):  # pragma: no cover
        return StartRecommendationsRequestEntry.make_many(self.boto3_raw_data["Data"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BatchStartRecommendationsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchStartRecommendationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateReplicationTaskResponse:
    boto3_raw_data: "type_defs.CreateReplicationTaskResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ReplicationTask(self):  # pragma: no cover
        return ReplicationTask.make_one(self.boto3_raw_data["ReplicationTask"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateReplicationTaskResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateReplicationTaskResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteReplicationTaskResponse:
    boto3_raw_data: "type_defs.DeleteReplicationTaskResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ReplicationTask(self):  # pragma: no cover
        return ReplicationTask.make_one(self.boto3_raw_data["ReplicationTask"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteReplicationTaskResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteReplicationTaskResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeReplicationTasksResponse:
    boto3_raw_data: "type_defs.DescribeReplicationTasksResponseTypeDef" = (
        dataclasses.field()
    )

    Marker = field("Marker")

    @cached_property
    def ReplicationTasks(self):  # pragma: no cover
        return ReplicationTask.make_many(self.boto3_raw_data["ReplicationTasks"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeReplicationTasksResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeReplicationTasksResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyReplicationTaskResponse:
    boto3_raw_data: "type_defs.ModifyReplicationTaskResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ReplicationTask(self):  # pragma: no cover
        return ReplicationTask.make_one(self.boto3_raw_data["ReplicationTask"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ModifyReplicationTaskResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyReplicationTaskResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MoveReplicationTaskResponse:
    boto3_raw_data: "type_defs.MoveReplicationTaskResponseTypeDef" = dataclasses.field()

    @cached_property
    def ReplicationTask(self):  # pragma: no cover
        return ReplicationTask.make_one(self.boto3_raw_data["ReplicationTask"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MoveReplicationTaskResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MoveReplicationTaskResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartReplicationTaskAssessmentResponse:
    boto3_raw_data: "type_defs.StartReplicationTaskAssessmentResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ReplicationTask(self):  # pragma: no cover
        return ReplicationTask.make_one(self.boto3_raw_data["ReplicationTask"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartReplicationTaskAssessmentResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartReplicationTaskAssessmentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartReplicationTaskResponse:
    boto3_raw_data: "type_defs.StartReplicationTaskResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ReplicationTask(self):  # pragma: no cover
        return ReplicationTask.make_one(self.boto3_raw_data["ReplicationTask"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartReplicationTaskResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartReplicationTaskResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopReplicationTaskResponse:
    boto3_raw_data: "type_defs.StopReplicationTaskResponseTypeDef" = dataclasses.field()

    @cached_property
    def ReplicationTask(self):  # pragma: no cover
        return ReplicationTask.make_one(self.boto3_raw_data["ReplicationTask"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopReplicationTaskResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopReplicationTaskResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFleetAdvisorSchemasResponse:
    boto3_raw_data: "type_defs.DescribeFleetAdvisorSchemasResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def FleetAdvisorSchemas(self):  # pragma: no cover
        return SchemaResponse.make_many(self.boto3_raw_data["FleetAdvisorSchemas"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeFleetAdvisorSchemasResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFleetAdvisorSchemasResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateReplicationSubnetGroupResponse:
    boto3_raw_data: "type_defs.CreateReplicationSubnetGroupResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ReplicationSubnetGroup(self):  # pragma: no cover
        return ReplicationSubnetGroup.make_one(
            self.boto3_raw_data["ReplicationSubnetGroup"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateReplicationSubnetGroupResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateReplicationSubnetGroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeReplicationSubnetGroupsResponse:
    boto3_raw_data: "type_defs.DescribeReplicationSubnetGroupsResponseTypeDef" = (
        dataclasses.field()
    )

    Marker = field("Marker")

    @cached_property
    def ReplicationSubnetGroups(self):  # pragma: no cover
        return ReplicationSubnetGroup.make_many(
            self.boto3_raw_data["ReplicationSubnetGroups"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeReplicationSubnetGroupsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeReplicationSubnetGroupsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyReplicationSubnetGroupResponse:
    boto3_raw_data: "type_defs.ModifyReplicationSubnetGroupResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ReplicationSubnetGroup(self):  # pragma: no cover
        return ReplicationSubnetGroup.make_one(
            self.boto3_raw_data["ReplicationSubnetGroup"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ModifyReplicationSubnetGroupResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyReplicationSubnetGroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReplicationInstance:
    boto3_raw_data: "type_defs.ReplicationInstanceTypeDef" = dataclasses.field()

    ReplicationInstanceIdentifier = field("ReplicationInstanceIdentifier")
    ReplicationInstanceClass = field("ReplicationInstanceClass")
    ReplicationInstanceStatus = field("ReplicationInstanceStatus")
    AllocatedStorage = field("AllocatedStorage")
    InstanceCreateTime = field("InstanceCreateTime")

    @cached_property
    def VpcSecurityGroups(self):  # pragma: no cover
        return VpcSecurityGroupMembership.make_many(
            self.boto3_raw_data["VpcSecurityGroups"]
        )

    AvailabilityZone = field("AvailabilityZone")

    @cached_property
    def ReplicationSubnetGroup(self):  # pragma: no cover
        return ReplicationSubnetGroup.make_one(
            self.boto3_raw_data["ReplicationSubnetGroup"]
        )

    PreferredMaintenanceWindow = field("PreferredMaintenanceWindow")

    @cached_property
    def PendingModifiedValues(self):  # pragma: no cover
        return ReplicationPendingModifiedValues.make_one(
            self.boto3_raw_data["PendingModifiedValues"]
        )

    MultiAZ = field("MultiAZ")
    EngineVersion = field("EngineVersion")
    AutoMinorVersionUpgrade = field("AutoMinorVersionUpgrade")
    KmsKeyId = field("KmsKeyId")
    ReplicationInstanceArn = field("ReplicationInstanceArn")
    ReplicationInstancePublicIpAddress = field("ReplicationInstancePublicIpAddress")
    ReplicationInstancePrivateIpAddress = field("ReplicationInstancePrivateIpAddress")
    ReplicationInstancePublicIpAddresses = field("ReplicationInstancePublicIpAddresses")
    ReplicationInstancePrivateIpAddresses = field(
        "ReplicationInstancePrivateIpAddresses"
    )
    ReplicationInstanceIpv6Addresses = field("ReplicationInstanceIpv6Addresses")
    PubliclyAccessible = field("PubliclyAccessible")
    SecondaryAvailabilityZone = field("SecondaryAvailabilityZone")
    FreeUntil = field("FreeUntil")
    DnsNameServers = field("DnsNameServers")
    NetworkType = field("NetworkType")

    @cached_property
    def KerberosAuthenticationSettings(self):  # pragma: no cover
        return KerberosAuthenticationSettings.make_one(
            self.boto3_raw_data["KerberosAuthenticationSettings"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReplicationInstanceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReplicationInstanceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDataMigrationMessage:
    boto3_raw_data: "type_defs.CreateDataMigrationMessageTypeDef" = dataclasses.field()

    MigrationProjectIdentifier = field("MigrationProjectIdentifier")
    DataMigrationType = field("DataMigrationType")
    ServiceAccessRoleArn = field("ServiceAccessRoleArn")
    DataMigrationName = field("DataMigrationName")
    EnableCloudwatchLogs = field("EnableCloudwatchLogs")
    SourceDataSettings = field("SourceDataSettings")

    @cached_property
    def TargetDataSettings(self):  # pragma: no cover
        return TargetDataSetting.make_many(self.boto3_raw_data["TargetDataSettings"])

    NumberOfJobs = field("NumberOfJobs")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    SelectionRules = field("SelectionRules")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDataMigrationMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDataMigrationMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyDataMigrationMessage:
    boto3_raw_data: "type_defs.ModifyDataMigrationMessageTypeDef" = dataclasses.field()

    DataMigrationIdentifier = field("DataMigrationIdentifier")
    DataMigrationName = field("DataMigrationName")
    EnableCloudwatchLogs = field("EnableCloudwatchLogs")
    ServiceAccessRoleArn = field("ServiceAccessRoleArn")
    DataMigrationType = field("DataMigrationType")
    SourceDataSettings = field("SourceDataSettings")

    @cached_property
    def TargetDataSettings(self):  # pragma: no cover
        return TargetDataSetting.make_many(self.boto3_raw_data["TargetDataSettings"])

    NumberOfJobs = field("NumberOfJobs")
    SelectionRules = field("SelectionRules")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ModifyDataMigrationMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyDataMigrationMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDataProviderResponse:
    boto3_raw_data: "type_defs.CreateDataProviderResponseTypeDef" = dataclasses.field()

    @cached_property
    def DataProvider(self):  # pragma: no cover
        return DataProvider.make_one(self.boto3_raw_data["DataProvider"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDataProviderResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDataProviderResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDataProviderResponse:
    boto3_raw_data: "type_defs.DeleteDataProviderResponseTypeDef" = dataclasses.field()

    @cached_property
    def DataProvider(self):  # pragma: no cover
        return DataProvider.make_one(self.boto3_raw_data["DataProvider"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDataProviderResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDataProviderResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDataProvidersResponse:
    boto3_raw_data: "type_defs.DescribeDataProvidersResponseTypeDef" = (
        dataclasses.field()
    )

    Marker = field("Marker")

    @cached_property
    def DataProviders(self):  # pragma: no cover
        return DataProvider.make_many(self.boto3_raw_data["DataProviders"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeDataProvidersResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDataProvidersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyDataProviderResponse:
    boto3_raw_data: "type_defs.ModifyDataProviderResponseTypeDef" = dataclasses.field()

    @cached_property
    def DataProvider(self):  # pragma: no cover
        return DataProvider.make_one(self.boto3_raw_data["DataProvider"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ModifyDataProviderResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyDataProviderResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeExtensionPackAssociationsResponse:
    boto3_raw_data: "type_defs.DescribeExtensionPackAssociationsResponseTypeDef" = (
        dataclasses.field()
    )

    Marker = field("Marker")

    @cached_property
    def Requests(self):  # pragma: no cover
        return SchemaConversionRequest.make_many(self.boto3_raw_data["Requests"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeExtensionPackAssociationsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeExtensionPackAssociationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeMetadataModelAssessmentsResponse:
    boto3_raw_data: "type_defs.DescribeMetadataModelAssessmentsResponseTypeDef" = (
        dataclasses.field()
    )

    Marker = field("Marker")

    @cached_property
    def Requests(self):  # pragma: no cover
        return SchemaConversionRequest.make_many(self.boto3_raw_data["Requests"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeMetadataModelAssessmentsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeMetadataModelAssessmentsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeMetadataModelConversionsResponse:
    boto3_raw_data: "type_defs.DescribeMetadataModelConversionsResponseTypeDef" = (
        dataclasses.field()
    )

    Marker = field("Marker")

    @cached_property
    def Requests(self):  # pragma: no cover
        return SchemaConversionRequest.make_many(self.boto3_raw_data["Requests"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeMetadataModelConversionsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeMetadataModelConversionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeMetadataModelExportsAsScriptResponse:
    boto3_raw_data: "type_defs.DescribeMetadataModelExportsAsScriptResponseTypeDef" = (
        dataclasses.field()
    )

    Marker = field("Marker")

    @cached_property
    def Requests(self):  # pragma: no cover
        return SchemaConversionRequest.make_many(self.boto3_raw_data["Requests"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeMetadataModelExportsAsScriptResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeMetadataModelExportsAsScriptResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeMetadataModelExportsToTargetResponse:
    boto3_raw_data: "type_defs.DescribeMetadataModelExportsToTargetResponseTypeDef" = (
        dataclasses.field()
    )

    Marker = field("Marker")

    @cached_property
    def Requests(self):  # pragma: no cover
        return SchemaConversionRequest.make_many(self.boto3_raw_data["Requests"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeMetadataModelExportsToTargetResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeMetadataModelExportsToTargetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeMetadataModelImportsResponse:
    boto3_raw_data: "type_defs.DescribeMetadataModelImportsResponseTypeDef" = (
        dataclasses.field()
    )

    Marker = field("Marker")

    @cached_property
    def Requests(self):  # pragma: no cover
        return SchemaConversionRequest.make_many(self.boto3_raw_data["Requests"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeMetadataModelImportsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeMetadataModelImportsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeReplicationsResponse:
    boto3_raw_data: "type_defs.DescribeReplicationsResponseTypeDef" = (
        dataclasses.field()
    )

    Marker = field("Marker")

    @cached_property
    def Replications(self):  # pragma: no cover
        return Replication.make_many(self.boto3_raw_data["Replications"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeReplicationsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeReplicationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartReplicationResponse:
    boto3_raw_data: "type_defs.StartReplicationResponseTypeDef" = dataclasses.field()

    @cached_property
    def Replication(self):  # pragma: no cover
        return Replication.make_one(self.boto3_raw_data["Replication"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartReplicationResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartReplicationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopReplicationResponse:
    boto3_raw_data: "type_defs.StopReplicationResponseTypeDef" = dataclasses.field()

    @cached_property
    def Replication(self):  # pragma: no cover
        return Replication.make_one(self.boto3_raw_data["Replication"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopReplicationResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopReplicationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Recommendation:
    boto3_raw_data: "type_defs.RecommendationTypeDef" = dataclasses.field()

    DatabaseId = field("DatabaseId")
    EngineName = field("EngineName")
    CreatedDate = field("CreatedDate")
    Status = field("Status")
    Preferred = field("Preferred")

    @cached_property
    def Settings(self):  # pragma: no cover
        return RecommendationSettings.make_one(self.boto3_raw_data["Settings"])

    @cached_property
    def Data(self):  # pragma: no cover
        return RecommendationData.make_one(self.boto3_raw_data["Data"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RecommendationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RecommendationTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateReplicationInstanceResponse:
    boto3_raw_data: "type_defs.CreateReplicationInstanceResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ReplicationInstance(self):  # pragma: no cover
        return ReplicationInstance.make_one(self.boto3_raw_data["ReplicationInstance"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateReplicationInstanceResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateReplicationInstanceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteReplicationInstanceResponse:
    boto3_raw_data: "type_defs.DeleteReplicationInstanceResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ReplicationInstance(self):  # pragma: no cover
        return ReplicationInstance.make_one(self.boto3_raw_data["ReplicationInstance"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteReplicationInstanceResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteReplicationInstanceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeReplicationInstancesResponse:
    boto3_raw_data: "type_defs.DescribeReplicationInstancesResponseTypeDef" = (
        dataclasses.field()
    )

    Marker = field("Marker")

    @cached_property
    def ReplicationInstances(self):  # pragma: no cover
        return ReplicationInstance.make_many(
            self.boto3_raw_data["ReplicationInstances"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeReplicationInstancesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeReplicationInstancesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyReplicationInstanceResponse:
    boto3_raw_data: "type_defs.ModifyReplicationInstanceResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ReplicationInstance(self):  # pragma: no cover
        return ReplicationInstance.make_one(self.boto3_raw_data["ReplicationInstance"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ModifyReplicationInstanceResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyReplicationInstanceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RebootReplicationInstanceResponse:
    boto3_raw_data: "type_defs.RebootReplicationInstanceResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ReplicationInstance(self):  # pragma: no cover
        return ReplicationInstance.make_one(self.boto3_raw_data["ReplicationInstance"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RebootReplicationInstanceResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RebootReplicationInstanceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRecommendationsResponse:
    boto3_raw_data: "type_defs.DescribeRecommendationsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Recommendations(self):  # pragma: no cover
        return Recommendation.make_many(self.boto3_raw_data["Recommendations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeRecommendationsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRecommendationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
