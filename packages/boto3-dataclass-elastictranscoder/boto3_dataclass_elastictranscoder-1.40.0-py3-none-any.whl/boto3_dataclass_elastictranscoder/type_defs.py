# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_elastictranscoder import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class Encryption:
    boto3_raw_data: "type_defs.EncryptionTypeDef" = dataclasses.field()

    Mode = field("Mode")
    Key = field("Key")
    KeyMd5 = field("KeyMd5")
    InitializationVector = field("InitializationVector")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EncryptionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EncryptionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AudioCodecOptions:
    boto3_raw_data: "type_defs.AudioCodecOptionsTypeDef" = dataclasses.field()

    Profile = field("Profile")
    BitDepth = field("BitDepth")
    BitOrder = field("BitOrder")
    Signed = field("Signed")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AudioCodecOptionsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AudioCodecOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelJobRequest:
    boto3_raw_data: "type_defs.CancelJobRequestTypeDef" = dataclasses.field()

    Id = field("Id")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CancelJobRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TimeSpan:
    boto3_raw_data: "type_defs.TimeSpanTypeDef" = dataclasses.field()

    StartTime = field("StartTime")
    Duration = field("Duration")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TimeSpanTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TimeSpanTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HlsContentProtection:
    boto3_raw_data: "type_defs.HlsContentProtectionTypeDef" = dataclasses.field()

    Method = field("Method")
    Key = field("Key")
    KeyMd5 = field("KeyMd5")
    InitializationVector = field("InitializationVector")
    LicenseAcquisitionUrl = field("LicenseAcquisitionUrl")
    KeyStoragePolicy = field("KeyStoragePolicy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.HlsContentProtectionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HlsContentProtectionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PlayReadyDrm:
    boto3_raw_data: "type_defs.PlayReadyDrmTypeDef" = dataclasses.field()

    Format = field("Format")
    Key = field("Key")
    KeyMd5 = field("KeyMd5")
    KeyId = field("KeyId")
    InitializationVector = field("InitializationVector")
    LicenseAcquisitionUrl = field("LicenseAcquisitionUrl")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PlayReadyDrmTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PlayReadyDrmTypeDef"]],
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
class Notifications:
    boto3_raw_data: "type_defs.NotificationsTypeDef" = dataclasses.field()

    Progressing = field("Progressing")
    Completed = field("Completed")
    Warning = field("Warning")
    Error = field("Error")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.NotificationsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.NotificationsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Warning:
    boto3_raw_data: "type_defs.WarningTypeDef" = dataclasses.field()

    Code = field("Code")
    Message = field("Message")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WarningTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.WarningTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Thumbnails:
    boto3_raw_data: "type_defs.ThumbnailsTypeDef" = dataclasses.field()

    Format = field("Format")
    Interval = field("Interval")
    Resolution = field("Resolution")
    AspectRatio = field("AspectRatio")
    MaxWidth = field("MaxWidth")
    MaxHeight = field("MaxHeight")
    SizingPolicy = field("SizingPolicy")
    PaddingPolicy = field("PaddingPolicy")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ThumbnailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ThumbnailsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeletePipelineRequest:
    boto3_raw_data: "type_defs.DeletePipelineRequestTypeDef" = dataclasses.field()

    Id = field("Id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeletePipelineRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeletePipelineRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeletePresetRequest:
    boto3_raw_data: "type_defs.DeletePresetRequestTypeDef" = dataclasses.field()

    Id = field("Id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeletePresetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeletePresetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetectedProperties:
    boto3_raw_data: "type_defs.DetectedPropertiesTypeDef" = dataclasses.field()

    Width = field("Width")
    Height = field("Height")
    FrameRate = field("FrameRate")
    FileSize = field("FileSize")
    DurationMillis = field("DurationMillis")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DetectedPropertiesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetectedPropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Timing:
    boto3_raw_data: "type_defs.TimingTypeDef" = dataclasses.field()

    SubmitTimeMillis = field("SubmitTimeMillis")
    StartTimeMillis = field("StartTimeMillis")
    FinishTimeMillis = field("FinishTimeMillis")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TimingTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TimingTypeDef"]]
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
class ListJobsByPipelineRequest:
    boto3_raw_data: "type_defs.ListJobsByPipelineRequestTypeDef" = dataclasses.field()

    PipelineId = field("PipelineId")
    Ascending = field("Ascending")
    PageToken = field("PageToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListJobsByPipelineRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListJobsByPipelineRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListJobsByStatusRequest:
    boto3_raw_data: "type_defs.ListJobsByStatusRequestTypeDef" = dataclasses.field()

    Status = field("Status")
    Ascending = field("Ascending")
    PageToken = field("PageToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListJobsByStatusRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListJobsByStatusRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPipelinesRequest:
    boto3_raw_data: "type_defs.ListPipelinesRequestTypeDef" = dataclasses.field()

    Ascending = field("Ascending")
    PageToken = field("PageToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPipelinesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPipelinesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPresetsRequest:
    boto3_raw_data: "type_defs.ListPresetsRequestTypeDef" = dataclasses.field()

    Ascending = field("Ascending")
    PageToken = field("PageToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPresetsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPresetsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PermissionOutput:
    boto3_raw_data: "type_defs.PermissionOutputTypeDef" = dataclasses.field()

    GranteeType = field("GranteeType")
    Grantee = field("Grantee")
    Access = field("Access")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PermissionOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PermissionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Permission:
    boto3_raw_data: "type_defs.PermissionTypeDef" = dataclasses.field()

    GranteeType = field("GranteeType")
    Grantee = field("Grantee")
    Access = field("Access")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PermissionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PermissionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PresetWatermark:
    boto3_raw_data: "type_defs.PresetWatermarkTypeDef" = dataclasses.field()

    Id = field("Id")
    MaxWidth = field("MaxWidth")
    MaxHeight = field("MaxHeight")
    SizingPolicy = field("SizingPolicy")
    HorizontalAlign = field("HorizontalAlign")
    HorizontalOffset = field("HorizontalOffset")
    VerticalAlign = field("VerticalAlign")
    VerticalOffset = field("VerticalOffset")
    Opacity = field("Opacity")
    Target = field("Target")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PresetWatermarkTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PresetWatermarkTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReadJobRequest:
    boto3_raw_data: "type_defs.ReadJobRequestTypeDef" = dataclasses.field()

    Id = field("Id")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ReadJobRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ReadJobRequestTypeDef"]],
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
class ReadPipelineRequest:
    boto3_raw_data: "type_defs.ReadPipelineRequestTypeDef" = dataclasses.field()

    Id = field("Id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReadPipelineRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReadPipelineRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReadPresetRequest:
    boto3_raw_data: "type_defs.ReadPresetRequestTypeDef" = dataclasses.field()

    Id = field("Id")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ReadPresetRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReadPresetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TestRoleRequest:
    boto3_raw_data: "type_defs.TestRoleRequestTypeDef" = dataclasses.field()

    Role = field("Role")
    InputBucket = field("InputBucket")
    OutputBucket = field("OutputBucket")
    Topics = field("Topics")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TestRoleRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TestRoleRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdatePipelineStatusRequest:
    boto3_raw_data: "type_defs.UpdatePipelineStatusRequestTypeDef" = dataclasses.field()

    Id = field("Id")
    Status = field("Status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdatePipelineStatusRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePipelineStatusRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Artwork:
    boto3_raw_data: "type_defs.ArtworkTypeDef" = dataclasses.field()

    InputKey = field("InputKey")
    MaxWidth = field("MaxWidth")
    MaxHeight = field("MaxHeight")
    SizingPolicy = field("SizingPolicy")
    PaddingPolicy = field("PaddingPolicy")
    AlbumArtFormat = field("AlbumArtFormat")

    @cached_property
    def Encryption(self):  # pragma: no cover
        return Encryption.make_one(self.boto3_raw_data["Encryption"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ArtworkTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ArtworkTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CaptionFormat:
    boto3_raw_data: "type_defs.CaptionFormatTypeDef" = dataclasses.field()

    Format = field("Format")
    Pattern = field("Pattern")

    @cached_property
    def Encryption(self):  # pragma: no cover
        return Encryption.make_one(self.boto3_raw_data["Encryption"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CaptionFormatTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CaptionFormatTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CaptionSource:
    boto3_raw_data: "type_defs.CaptionSourceTypeDef" = dataclasses.field()

    Key = field("Key")
    Language = field("Language")
    TimeOffset = field("TimeOffset")
    Label = field("Label")

    @cached_property
    def Encryption(self):  # pragma: no cover
        return Encryption.make_one(self.boto3_raw_data["Encryption"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CaptionSourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CaptionSourceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobWatermark:
    boto3_raw_data: "type_defs.JobWatermarkTypeDef" = dataclasses.field()

    PresetWatermarkId = field("PresetWatermarkId")
    InputKey = field("InputKey")

    @cached_property
    def Encryption(self):  # pragma: no cover
        return Encryption.make_one(self.boto3_raw_data["Encryption"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JobWatermarkTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.JobWatermarkTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AudioParameters:
    boto3_raw_data: "type_defs.AudioParametersTypeDef" = dataclasses.field()

    Codec = field("Codec")
    SampleRate = field("SampleRate")
    BitRate = field("BitRate")
    Channels = field("Channels")
    AudioPackingMode = field("AudioPackingMode")

    @cached_property
    def CodecOptions(self):  # pragma: no cover
        return AudioCodecOptions.make_one(self.boto3_raw_data["CodecOptions"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AudioParametersTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AudioParametersTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Clip:
    boto3_raw_data: "type_defs.ClipTypeDef" = dataclasses.field()

    @cached_property
    def TimeSpan(self):  # pragma: no cover
        return TimeSpan.make_one(self.boto3_raw_data["TimeSpan"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ClipTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ClipTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateJobPlaylist:
    boto3_raw_data: "type_defs.CreateJobPlaylistTypeDef" = dataclasses.field()

    Name = field("Name")
    Format = field("Format")
    OutputKeys = field("OutputKeys")

    @cached_property
    def HlsContentProtection(self):  # pragma: no cover
        return HlsContentProtection.make_one(
            self.boto3_raw_data["HlsContentProtection"]
        )

    @cached_property
    def PlayReadyDrm(self):  # pragma: no cover
        return PlayReadyDrm.make_one(self.boto3_raw_data["PlayReadyDrm"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateJobPlaylistTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateJobPlaylistTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Playlist:
    boto3_raw_data: "type_defs.PlaylistTypeDef" = dataclasses.field()

    Name = field("Name")
    Format = field("Format")
    OutputKeys = field("OutputKeys")

    @cached_property
    def HlsContentProtection(self):  # pragma: no cover
        return HlsContentProtection.make_one(
            self.boto3_raw_data["HlsContentProtection"]
        )

    @cached_property
    def PlayReadyDrm(self):  # pragma: no cover
        return PlayReadyDrm.make_one(self.boto3_raw_data["PlayReadyDrm"])

    Status = field("Status")
    StatusDetail = field("StatusDetail")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PlaylistTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PlaylistTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TestRoleResponse:
    boto3_raw_data: "type_defs.TestRoleResponseTypeDef" = dataclasses.field()

    Success = field("Success")
    Messages = field("Messages")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TestRoleResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TestRoleResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdatePipelineNotificationsRequest:
    boto3_raw_data: "type_defs.UpdatePipelineNotificationsRequestTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")

    @cached_property
    def Notifications(self):  # pragma: no cover
        return Notifications.make_one(self.boto3_raw_data["Notifications"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdatePipelineNotificationsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePipelineNotificationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListJobsByPipelineRequestPaginate:
    boto3_raw_data: "type_defs.ListJobsByPipelineRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    PipelineId = field("PipelineId")
    Ascending = field("Ascending")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListJobsByPipelineRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListJobsByPipelineRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListJobsByStatusRequestPaginate:
    boto3_raw_data: "type_defs.ListJobsByStatusRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    Status = field("Status")
    Ascending = field("Ascending")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListJobsByStatusRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListJobsByStatusRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPipelinesRequestPaginate:
    boto3_raw_data: "type_defs.ListPipelinesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    Ascending = field("Ascending")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPipelinesRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPipelinesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPresetsRequestPaginate:
    boto3_raw_data: "type_defs.ListPresetsRequestPaginateTypeDef" = dataclasses.field()

    Ascending = field("Ascending")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPresetsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPresetsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PipelineOutputConfigOutput:
    boto3_raw_data: "type_defs.PipelineOutputConfigOutputTypeDef" = dataclasses.field()

    Bucket = field("Bucket")
    StorageClass = field("StorageClass")

    @cached_property
    def Permissions(self):  # pragma: no cover
        return PermissionOutput.make_many(self.boto3_raw_data["Permissions"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PipelineOutputConfigOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PipelineOutputConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PipelineOutputConfig:
    boto3_raw_data: "type_defs.PipelineOutputConfigTypeDef" = dataclasses.field()

    Bucket = field("Bucket")
    StorageClass = field("StorageClass")

    @cached_property
    def Permissions(self):  # pragma: no cover
        return Permission.make_many(self.boto3_raw_data["Permissions"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PipelineOutputConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PipelineOutputConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VideoParametersOutput:
    boto3_raw_data: "type_defs.VideoParametersOutputTypeDef" = dataclasses.field()

    Codec = field("Codec")
    CodecOptions = field("CodecOptions")
    KeyframesMaxDist = field("KeyframesMaxDist")
    FixedGOP = field("FixedGOP")
    BitRate = field("BitRate")
    FrameRate = field("FrameRate")
    MaxFrameRate = field("MaxFrameRate")
    Resolution = field("Resolution")
    AspectRatio = field("AspectRatio")
    MaxWidth = field("MaxWidth")
    MaxHeight = field("MaxHeight")
    DisplayAspectRatio = field("DisplayAspectRatio")
    SizingPolicy = field("SizingPolicy")
    PaddingPolicy = field("PaddingPolicy")

    @cached_property
    def Watermarks(self):  # pragma: no cover
        return PresetWatermark.make_many(self.boto3_raw_data["Watermarks"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VideoParametersOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VideoParametersOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VideoParameters:
    boto3_raw_data: "type_defs.VideoParametersTypeDef" = dataclasses.field()

    Codec = field("Codec")
    CodecOptions = field("CodecOptions")
    KeyframesMaxDist = field("KeyframesMaxDist")
    FixedGOP = field("FixedGOP")
    BitRate = field("BitRate")
    FrameRate = field("FrameRate")
    MaxFrameRate = field("MaxFrameRate")
    Resolution = field("Resolution")
    AspectRatio = field("AspectRatio")
    MaxWidth = field("MaxWidth")
    MaxHeight = field("MaxHeight")
    DisplayAspectRatio = field("DisplayAspectRatio")
    SizingPolicy = field("SizingPolicy")
    PaddingPolicy = field("PaddingPolicy")

    @cached_property
    def Watermarks(self):  # pragma: no cover
        return PresetWatermark.make_many(self.boto3_raw_data["Watermarks"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VideoParametersTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VideoParametersTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReadJobRequestWait:
    boto3_raw_data: "type_defs.ReadJobRequestWaitTypeDef" = dataclasses.field()

    Id = field("Id")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReadJobRequestWaitTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReadJobRequestWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobAlbumArtOutput:
    boto3_raw_data: "type_defs.JobAlbumArtOutputTypeDef" = dataclasses.field()

    MergePolicy = field("MergePolicy")

    @cached_property
    def Artwork(self):  # pragma: no cover
        return Artwork.make_many(self.boto3_raw_data["Artwork"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JobAlbumArtOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.JobAlbumArtOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobAlbumArt:
    boto3_raw_data: "type_defs.JobAlbumArtTypeDef" = dataclasses.field()

    MergePolicy = field("MergePolicy")

    @cached_property
    def Artwork(self):  # pragma: no cover
        return Artwork.make_many(self.boto3_raw_data["Artwork"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JobAlbumArtTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.JobAlbumArtTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CaptionsOutput:
    boto3_raw_data: "type_defs.CaptionsOutputTypeDef" = dataclasses.field()

    MergePolicy = field("MergePolicy")

    @cached_property
    def CaptionSources(self):  # pragma: no cover
        return CaptionSource.make_many(self.boto3_raw_data["CaptionSources"])

    @cached_property
    def CaptionFormats(self):  # pragma: no cover
        return CaptionFormat.make_many(self.boto3_raw_data["CaptionFormats"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CaptionsOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CaptionsOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Captions:
    boto3_raw_data: "type_defs.CaptionsTypeDef" = dataclasses.field()

    MergePolicy = field("MergePolicy")

    @cached_property
    def CaptionSources(self):  # pragma: no cover
        return CaptionSource.make_many(self.boto3_raw_data["CaptionSources"])

    @cached_property
    def CaptionFormats(self):  # pragma: no cover
        return CaptionFormat.make_many(self.boto3_raw_data["CaptionFormats"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CaptionsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CaptionsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InputCaptionsOutput:
    boto3_raw_data: "type_defs.InputCaptionsOutputTypeDef" = dataclasses.field()

    MergePolicy = field("MergePolicy")

    @cached_property
    def CaptionSources(self):  # pragma: no cover
        return CaptionSource.make_many(self.boto3_raw_data["CaptionSources"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InputCaptionsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InputCaptionsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InputCaptions:
    boto3_raw_data: "type_defs.InputCaptionsTypeDef" = dataclasses.field()

    MergePolicy = field("MergePolicy")

    @cached_property
    def CaptionSources(self):  # pragma: no cover
        return CaptionSource.make_many(self.boto3_raw_data["CaptionSources"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InputCaptionsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.InputCaptionsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Pipeline:
    boto3_raw_data: "type_defs.PipelineTypeDef" = dataclasses.field()

    Id = field("Id")
    Arn = field("Arn")
    Name = field("Name")
    Status = field("Status")
    InputBucket = field("InputBucket")
    OutputBucket = field("OutputBucket")
    Role = field("Role")
    AwsKmsKeyArn = field("AwsKmsKeyArn")

    @cached_property
    def Notifications(self):  # pragma: no cover
        return Notifications.make_one(self.boto3_raw_data["Notifications"])

    @cached_property
    def ContentConfig(self):  # pragma: no cover
        return PipelineOutputConfigOutput.make_one(self.boto3_raw_data["ContentConfig"])

    @cached_property
    def ThumbnailConfig(self):  # pragma: no cover
        return PipelineOutputConfigOutput.make_one(
            self.boto3_raw_data["ThumbnailConfig"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PipelineTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PipelineTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Preset:
    boto3_raw_data: "type_defs.PresetTypeDef" = dataclasses.field()

    Id = field("Id")
    Arn = field("Arn")
    Name = field("Name")
    Description = field("Description")
    Container = field("Container")

    @cached_property
    def Audio(self):  # pragma: no cover
        return AudioParameters.make_one(self.boto3_raw_data["Audio"])

    @cached_property
    def Video(self):  # pragma: no cover
        return VideoParametersOutput.make_one(self.boto3_raw_data["Video"])

    @cached_property
    def Thumbnails(self):  # pragma: no cover
        return Thumbnails.make_one(self.boto3_raw_data["Thumbnails"])

    Type = field("Type")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PresetTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PresetTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobOutput:
    boto3_raw_data: "type_defs.JobOutputTypeDef" = dataclasses.field()

    Id = field("Id")
    Key = field("Key")
    ThumbnailPattern = field("ThumbnailPattern")

    @cached_property
    def ThumbnailEncryption(self):  # pragma: no cover
        return Encryption.make_one(self.boto3_raw_data["ThumbnailEncryption"])

    Rotate = field("Rotate")
    PresetId = field("PresetId")
    SegmentDuration = field("SegmentDuration")
    Status = field("Status")
    StatusDetail = field("StatusDetail")
    Duration = field("Duration")
    Width = field("Width")
    Height = field("Height")
    FrameRate = field("FrameRate")
    FileSize = field("FileSize")
    DurationMillis = field("DurationMillis")

    @cached_property
    def Watermarks(self):  # pragma: no cover
        return JobWatermark.make_many(self.boto3_raw_data["Watermarks"])

    @cached_property
    def AlbumArt(self):  # pragma: no cover
        return JobAlbumArtOutput.make_one(self.boto3_raw_data["AlbumArt"])

    @cached_property
    def Composition(self):  # pragma: no cover
        return Clip.make_many(self.boto3_raw_data["Composition"])

    @cached_property
    def Captions(self):  # pragma: no cover
        return CaptionsOutput.make_one(self.boto3_raw_data["Captions"])

    @cached_property
    def Encryption(self):  # pragma: no cover
        return Encryption.make_one(self.boto3_raw_data["Encryption"])

    AppliedColorSpaceConversion = field("AppliedColorSpaceConversion")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JobOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.JobOutputTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobInputOutput:
    boto3_raw_data: "type_defs.JobInputOutputTypeDef" = dataclasses.field()

    Key = field("Key")
    FrameRate = field("FrameRate")
    Resolution = field("Resolution")
    AspectRatio = field("AspectRatio")
    Interlaced = field("Interlaced")
    Container = field("Container")

    @cached_property
    def Encryption(self):  # pragma: no cover
        return Encryption.make_one(self.boto3_raw_data["Encryption"])

    @cached_property
    def TimeSpan(self):  # pragma: no cover
        return TimeSpan.make_one(self.boto3_raw_data["TimeSpan"])

    @cached_property
    def InputCaptions(self):  # pragma: no cover
        return InputCaptionsOutput.make_one(self.boto3_raw_data["InputCaptions"])

    @cached_property
    def DetectedProperties(self):  # pragma: no cover
        return DetectedProperties.make_one(self.boto3_raw_data["DetectedProperties"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JobInputOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.JobInputOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePipelineResponse:
    boto3_raw_data: "type_defs.CreatePipelineResponseTypeDef" = dataclasses.field()

    @cached_property
    def Pipeline(self):  # pragma: no cover
        return Pipeline.make_one(self.boto3_raw_data["Pipeline"])

    @cached_property
    def Warnings(self):  # pragma: no cover
        return Warning.make_many(self.boto3_raw_data["Warnings"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreatePipelineResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePipelineResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPipelinesResponse:
    boto3_raw_data: "type_defs.ListPipelinesResponseTypeDef" = dataclasses.field()

    @cached_property
    def Pipelines(self):  # pragma: no cover
        return Pipeline.make_many(self.boto3_raw_data["Pipelines"])

    NextPageToken = field("NextPageToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPipelinesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPipelinesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReadPipelineResponse:
    boto3_raw_data: "type_defs.ReadPipelineResponseTypeDef" = dataclasses.field()

    @cached_property
    def Pipeline(self):  # pragma: no cover
        return Pipeline.make_one(self.boto3_raw_data["Pipeline"])

    @cached_property
    def Warnings(self):  # pragma: no cover
        return Warning.make_many(self.boto3_raw_data["Warnings"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReadPipelineResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReadPipelineResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdatePipelineNotificationsResponse:
    boto3_raw_data: "type_defs.UpdatePipelineNotificationsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Pipeline(self):  # pragma: no cover
        return Pipeline.make_one(self.boto3_raw_data["Pipeline"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdatePipelineNotificationsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePipelineNotificationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdatePipelineResponse:
    boto3_raw_data: "type_defs.UpdatePipelineResponseTypeDef" = dataclasses.field()

    @cached_property
    def Pipeline(self):  # pragma: no cover
        return Pipeline.make_one(self.boto3_raw_data["Pipeline"])

    @cached_property
    def Warnings(self):  # pragma: no cover
        return Warning.make_many(self.boto3_raw_data["Warnings"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdatePipelineResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePipelineResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdatePipelineStatusResponse:
    boto3_raw_data: "type_defs.UpdatePipelineStatusResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Pipeline(self):  # pragma: no cover
        return Pipeline.make_one(self.boto3_raw_data["Pipeline"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdatePipelineStatusResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePipelineStatusResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePipelineRequest:
    boto3_raw_data: "type_defs.CreatePipelineRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    InputBucket = field("InputBucket")
    Role = field("Role")
    OutputBucket = field("OutputBucket")
    AwsKmsKeyArn = field("AwsKmsKeyArn")

    @cached_property
    def Notifications(self):  # pragma: no cover
        return Notifications.make_one(self.boto3_raw_data["Notifications"])

    ContentConfig = field("ContentConfig")
    ThumbnailConfig = field("ThumbnailConfig")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreatePipelineRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePipelineRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdatePipelineRequest:
    boto3_raw_data: "type_defs.UpdatePipelineRequestTypeDef" = dataclasses.field()

    Id = field("Id")
    Name = field("Name")
    InputBucket = field("InputBucket")
    Role = field("Role")
    AwsKmsKeyArn = field("AwsKmsKeyArn")

    @cached_property
    def Notifications(self):  # pragma: no cover
        return Notifications.make_one(self.boto3_raw_data["Notifications"])

    ContentConfig = field("ContentConfig")
    ThumbnailConfig = field("ThumbnailConfig")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdatePipelineRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePipelineRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePresetResponse:
    boto3_raw_data: "type_defs.CreatePresetResponseTypeDef" = dataclasses.field()

    @cached_property
    def Preset(self):  # pragma: no cover
        return Preset.make_one(self.boto3_raw_data["Preset"])

    Warning = field("Warning")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreatePresetResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePresetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPresetsResponse:
    boto3_raw_data: "type_defs.ListPresetsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Presets(self):  # pragma: no cover
        return Preset.make_many(self.boto3_raw_data["Presets"])

    NextPageToken = field("NextPageToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPresetsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPresetsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReadPresetResponse:
    boto3_raw_data: "type_defs.ReadPresetResponseTypeDef" = dataclasses.field()

    @cached_property
    def Preset(self):  # pragma: no cover
        return Preset.make_one(self.boto3_raw_data["Preset"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReadPresetResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReadPresetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePresetRequest:
    boto3_raw_data: "type_defs.CreatePresetRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    Container = field("Container")
    Description = field("Description")
    Video = field("Video")

    @cached_property
    def Audio(self):  # pragma: no cover
        return AudioParameters.make_one(self.boto3_raw_data["Audio"])

    @cached_property
    def Thumbnails(self):  # pragma: no cover
        return Thumbnails.make_one(self.boto3_raw_data["Thumbnails"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreatePresetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePresetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateJobOutput:
    boto3_raw_data: "type_defs.CreateJobOutputTypeDef" = dataclasses.field()

    Key = field("Key")
    ThumbnailPattern = field("ThumbnailPattern")

    @cached_property
    def ThumbnailEncryption(self):  # pragma: no cover
        return Encryption.make_one(self.boto3_raw_data["ThumbnailEncryption"])

    Rotate = field("Rotate")
    PresetId = field("PresetId")
    SegmentDuration = field("SegmentDuration")

    @cached_property
    def Watermarks(self):  # pragma: no cover
        return JobWatermark.make_many(self.boto3_raw_data["Watermarks"])

    AlbumArt = field("AlbumArt")

    @cached_property
    def Composition(self):  # pragma: no cover
        return Clip.make_many(self.boto3_raw_data["Composition"])

    Captions = field("Captions")

    @cached_property
    def Encryption(self):  # pragma: no cover
        return Encryption.make_one(self.boto3_raw_data["Encryption"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateJobOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CreateJobOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Job:
    boto3_raw_data: "type_defs.JobTypeDef" = dataclasses.field()

    Id = field("Id")
    Arn = field("Arn")
    PipelineId = field("PipelineId")

    @cached_property
    def Input(self):  # pragma: no cover
        return JobInputOutput.make_one(self.boto3_raw_data["Input"])

    @cached_property
    def Inputs(self):  # pragma: no cover
        return JobInputOutput.make_many(self.boto3_raw_data["Inputs"])

    @cached_property
    def Output(self):  # pragma: no cover
        return JobOutput.make_one(self.boto3_raw_data["Output"])

    @cached_property
    def Outputs(self):  # pragma: no cover
        return JobOutput.make_many(self.boto3_raw_data["Outputs"])

    OutputKeyPrefix = field("OutputKeyPrefix")

    @cached_property
    def Playlists(self):  # pragma: no cover
        return Playlist.make_many(self.boto3_raw_data["Playlists"])

    Status = field("Status")
    UserMetadata = field("UserMetadata")

    @cached_property
    def Timing(self):  # pragma: no cover
        return Timing.make_one(self.boto3_raw_data["Timing"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JobTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.JobTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobInput:
    boto3_raw_data: "type_defs.JobInputTypeDef" = dataclasses.field()

    Key = field("Key")
    FrameRate = field("FrameRate")
    Resolution = field("Resolution")
    AspectRatio = field("AspectRatio")
    Interlaced = field("Interlaced")
    Container = field("Container")

    @cached_property
    def Encryption(self):  # pragma: no cover
        return Encryption.make_one(self.boto3_raw_data["Encryption"])

    @cached_property
    def TimeSpan(self):  # pragma: no cover
        return TimeSpan.make_one(self.boto3_raw_data["TimeSpan"])

    InputCaptions = field("InputCaptions")

    @cached_property
    def DetectedProperties(self):  # pragma: no cover
        return DetectedProperties.make_one(self.boto3_raw_data["DetectedProperties"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JobInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.JobInputTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateJobResponse:
    boto3_raw_data: "type_defs.CreateJobResponseTypeDef" = dataclasses.field()

    @cached_property
    def Job(self):  # pragma: no cover
        return Job.make_one(self.boto3_raw_data["Job"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateJobResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListJobsByPipelineResponse:
    boto3_raw_data: "type_defs.ListJobsByPipelineResponseTypeDef" = dataclasses.field()

    @cached_property
    def Jobs(self):  # pragma: no cover
        return Job.make_many(self.boto3_raw_data["Jobs"])

    NextPageToken = field("NextPageToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListJobsByPipelineResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListJobsByPipelineResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListJobsByStatusResponse:
    boto3_raw_data: "type_defs.ListJobsByStatusResponseTypeDef" = dataclasses.field()

    @cached_property
    def Jobs(self):  # pragma: no cover
        return Job.make_many(self.boto3_raw_data["Jobs"])

    NextPageToken = field("NextPageToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListJobsByStatusResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListJobsByStatusResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReadJobResponse:
    boto3_raw_data: "type_defs.ReadJobResponseTypeDef" = dataclasses.field()

    @cached_property
    def Job(self):  # pragma: no cover
        return Job.make_one(self.boto3_raw_data["Job"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ReadJobResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ReadJobResponseTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateJobRequest:
    boto3_raw_data: "type_defs.CreateJobRequestTypeDef" = dataclasses.field()

    PipelineId = field("PipelineId")
    Input = field("Input")
    Inputs = field("Inputs")

    @cached_property
    def Output(self):  # pragma: no cover
        return CreateJobOutput.make_one(self.boto3_raw_data["Output"])

    @cached_property
    def Outputs(self):  # pragma: no cover
        return CreateJobOutput.make_many(self.boto3_raw_data["Outputs"])

    OutputKeyPrefix = field("OutputKeyPrefix")

    @cached_property
    def Playlists(self):  # pragma: no cover
        return CreateJobPlaylist.make_many(self.boto3_raw_data["Playlists"])

    UserMetadata = field("UserMetadata")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateJobRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
