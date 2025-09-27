# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_amplifyuibuilder import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class GraphQLRenderConfig:
    boto3_raw_data: "type_defs.GraphQLRenderConfigTypeDef" = dataclasses.field()

    typesFilePath = field("typesFilePath")
    queriesFilePath = field("queriesFilePath")
    mutationsFilePath = field("mutationsFilePath")
    subscriptionsFilePath = field("subscriptionsFilePath")
    fragmentsFilePath = field("fragmentsFilePath")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GraphQLRenderConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GraphQLRenderConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CodegenDependency:
    boto3_raw_data: "type_defs.CodegenDependencyTypeDef" = dataclasses.field()

    name = field("name")
    supportedVersion = field("supportedVersion")
    isSemVer = field("isSemVer")
    reason = field("reason")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CodegenDependencyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CodegenDependencyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CodegenFeatureFlags:
    boto3_raw_data: "type_defs.CodegenFeatureFlagsTypeDef" = dataclasses.field()

    isRelationshipSupported = field("isRelationshipSupported")
    isNonModelSupported = field("isNonModelSupported")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CodegenFeatureFlagsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CodegenFeatureFlagsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CodegenGenericDataEnumOutput:
    boto3_raw_data: "type_defs.CodegenGenericDataEnumOutputTypeDef" = (
        dataclasses.field()
    )

    values = field("values")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CodegenGenericDataEnumOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CodegenGenericDataEnumOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CodegenGenericDataEnum:
    boto3_raw_data: "type_defs.CodegenGenericDataEnumTypeDef" = dataclasses.field()

    values = field("values")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CodegenGenericDataEnumTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CodegenGenericDataEnumTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CodegenGenericDataRelationshipTypeOutput:
    boto3_raw_data: "type_defs.CodegenGenericDataRelationshipTypeOutputTypeDef" = (
        dataclasses.field()
    )

    type = field("type")
    relatedModelName = field("relatedModelName")
    relatedModelFields = field("relatedModelFields")
    canUnlinkAssociatedModel = field("canUnlinkAssociatedModel")
    relatedJoinFieldName = field("relatedJoinFieldName")
    relatedJoinTableName = field("relatedJoinTableName")
    belongsToFieldOnRelatedModel = field("belongsToFieldOnRelatedModel")
    associatedFields = field("associatedFields")
    isHasManyIndex = field("isHasManyIndex")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CodegenGenericDataRelationshipTypeOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CodegenGenericDataRelationshipTypeOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CodegenGenericDataRelationshipType:
    boto3_raw_data: "type_defs.CodegenGenericDataRelationshipTypeTypeDef" = (
        dataclasses.field()
    )

    type = field("type")
    relatedModelName = field("relatedModelName")
    relatedModelFields = field("relatedModelFields")
    canUnlinkAssociatedModel = field("canUnlinkAssociatedModel")
    relatedJoinFieldName = field("relatedJoinFieldName")
    relatedJoinTableName = field("relatedJoinTableName")
    belongsToFieldOnRelatedModel = field("belongsToFieldOnRelatedModel")
    associatedFields = field("associatedFields")
    isHasManyIndex = field("isHasManyIndex")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CodegenGenericDataRelationshipTypeTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CodegenGenericDataRelationshipTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CodegenJobAsset:
    boto3_raw_data: "type_defs.CodegenJobAssetTypeDef" = dataclasses.field()

    downloadUrl = field("downloadUrl")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CodegenJobAssetTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CodegenJobAssetTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CodegenJobSummary:
    boto3_raw_data: "type_defs.CodegenJobSummaryTypeDef" = dataclasses.field()

    appId = field("appId")
    environmentName = field("environmentName")
    id = field("id")
    createdAt = field("createdAt")
    modifiedAt = field("modifiedAt")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CodegenJobSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CodegenJobSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PredicateOutput:
    boto3_raw_data: "type_defs.PredicateOutputTypeDef" = dataclasses.field()

    or_ = field("or")
    and_ = field("and")
    field = field("field")
    operator = field("operator")
    operand = field("operand")
    operandType = field("operandType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PredicateOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PredicateOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PredicatePaginator:
    boto3_raw_data: "type_defs.PredicatePaginatorTypeDef" = dataclasses.field()

    or_ = field("or")
    and_ = field("and")
    field = field("field")
    operator = field("operator")
    operand = field("operand")
    operandType = field("operandType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PredicatePaginatorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PredicatePaginatorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ComponentConditionPropertyOutput:
    boto3_raw_data: "type_defs.ComponentConditionPropertyOutputTypeDef" = (
        dataclasses.field()
    )

    property = field("property")
    field = field("field")
    operator = field("operator")
    operand = field("operand")
    then = field("then")
    else_ = field("else")
    operandType = field("operandType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ComponentConditionPropertyOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ComponentConditionPropertyOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ComponentConditionPropertyPaginator:
    boto3_raw_data: "type_defs.ComponentConditionPropertyPaginatorTypeDef" = (
        dataclasses.field()
    )

    property = field("property")
    field = field("field")
    operator = field("operator")
    operand = field("operand")
    then = field("then")
    else_ = field("else")
    operandType = field("operandType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ComponentConditionPropertyPaginatorTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ComponentConditionPropertyPaginatorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ComponentConditionProperty:
    boto3_raw_data: "type_defs.ComponentConditionPropertyTypeDef" = dataclasses.field()

    property = field("property")
    field = field("field")
    operator = field("operator")
    operand = field("operand")
    then = field("then")
    else_ = field("else")
    operandType = field("operandType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ComponentConditionPropertyTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ComponentConditionPropertyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SortProperty:
    boto3_raw_data: "type_defs.SortPropertyTypeDef" = dataclasses.field()

    field = field("field")
    direction = field("direction")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SortPropertyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SortPropertyTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ComponentVariantOutput:
    boto3_raw_data: "type_defs.ComponentVariantOutputTypeDef" = dataclasses.field()

    variantValues = field("variantValues")
    overrides = field("overrides")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ComponentVariantOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ComponentVariantOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ComponentPropertyBindingProperties:
    boto3_raw_data: "type_defs.ComponentPropertyBindingPropertiesTypeDef" = (
        dataclasses.field()
    )

    property = field("property")
    field = field("field")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ComponentPropertyBindingPropertiesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ComponentPropertyBindingPropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FormBindingElement:
    boto3_raw_data: "type_defs.FormBindingElementTypeDef" = dataclasses.field()

    element = field("element")
    property = field("property")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FormBindingElementTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FormBindingElementTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ComponentSummary:
    boto3_raw_data: "type_defs.ComponentSummaryTypeDef" = dataclasses.field()

    appId = field("appId")
    environmentName = field("environmentName")
    id = field("id")
    name = field("name")
    componentType = field("componentType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ComponentSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ComponentSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ComponentVariant:
    boto3_raw_data: "type_defs.ComponentVariantTypeDef" = dataclasses.field()

    variantValues = field("variantValues")
    overrides = field("overrides")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ComponentVariantTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ComponentVariantTypeDef"]
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
class FormDataTypeConfig:
    boto3_raw_data: "type_defs.FormDataTypeConfigTypeDef" = dataclasses.field()

    dataSourceType = field("dataSourceType")
    dataTypeName = field("dataTypeName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FormDataTypeConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FormDataTypeConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteComponentRequest:
    boto3_raw_data: "type_defs.DeleteComponentRequestTypeDef" = dataclasses.field()

    appId = field("appId")
    environmentName = field("environmentName")
    id = field("id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteComponentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteComponentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteFormRequest:
    boto3_raw_data: "type_defs.DeleteFormRequestTypeDef" = dataclasses.field()

    appId = field("appId")
    environmentName = field("environmentName")
    id = field("id")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteFormRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteFormRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteThemeRequest:
    boto3_raw_data: "type_defs.DeleteThemeRequestTypeDef" = dataclasses.field()

    appId = field("appId")
    environmentName = field("environmentName")
    id = field("id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteThemeRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteThemeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExchangeCodeForTokenRequestBody:
    boto3_raw_data: "type_defs.ExchangeCodeForTokenRequestBodyTypeDef" = (
        dataclasses.field()
    )

    code = field("code")
    redirectUri = field("redirectUri")
    clientId = field("clientId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ExchangeCodeForTokenRequestBodyTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExchangeCodeForTokenRequestBodyTypeDef"]
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
class ExportComponentsRequest:
    boto3_raw_data: "type_defs.ExportComponentsRequestTypeDef" = dataclasses.field()

    appId = field("appId")
    environmentName = field("environmentName")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExportComponentsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExportComponentsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExportFormsRequest:
    boto3_raw_data: "type_defs.ExportFormsRequestTypeDef" = dataclasses.field()

    appId = field("appId")
    environmentName = field("environmentName")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExportFormsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExportFormsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExportThemesRequest:
    boto3_raw_data: "type_defs.ExportThemesRequestTypeDef" = dataclasses.field()

    appId = field("appId")
    environmentName = field("environmentName")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExportThemesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExportThemesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FieldPosition:
    boto3_raw_data: "type_defs.FieldPositionTypeDef" = dataclasses.field()

    fixed = field("fixed")
    rightOf = field("rightOf")
    below = field("below")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FieldPositionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FieldPositionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FieldValidationConfigurationOutput:
    boto3_raw_data: "type_defs.FieldValidationConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    type = field("type")
    strValues = field("strValues")
    numValues = field("numValues")
    validationMessage = field("validationMessage")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.FieldValidationConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FieldValidationConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FileUploaderFieldConfigOutput:
    boto3_raw_data: "type_defs.FileUploaderFieldConfigOutputTypeDef" = (
        dataclasses.field()
    )

    accessLevel = field("accessLevel")
    acceptedFileTypes = field("acceptedFileTypes")
    showThumbnails = field("showThumbnails")
    isResumable = field("isResumable")
    maxFileCount = field("maxFileCount")
    maxSize = field("maxSize")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.FileUploaderFieldConfigOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FileUploaderFieldConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FieldValidationConfiguration:
    boto3_raw_data: "type_defs.FieldValidationConfigurationTypeDef" = (
        dataclasses.field()
    )

    type = field("type")
    strValues = field("strValues")
    numValues = field("numValues")
    validationMessage = field("validationMessage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FieldValidationConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FieldValidationConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FileUploaderFieldConfig:
    boto3_raw_data: "type_defs.FileUploaderFieldConfigTypeDef" = dataclasses.field()

    accessLevel = field("accessLevel")
    acceptedFileTypes = field("acceptedFileTypes")
    showThumbnails = field("showThumbnails")
    isResumable = field("isResumable")
    maxFileCount = field("maxFileCount")
    maxSize = field("maxSize")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FileUploaderFieldConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FileUploaderFieldConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FormInputBindingPropertiesValueProperties:
    boto3_raw_data: "type_defs.FormInputBindingPropertiesValuePropertiesTypeDef" = (
        dataclasses.field()
    )

    model = field("model")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.FormInputBindingPropertiesValuePropertiesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FormInputBindingPropertiesValuePropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FormInputValuePropertyBindingProperties:
    boto3_raw_data: "type_defs.FormInputValuePropertyBindingPropertiesTypeDef" = (
        dataclasses.field()
    )

    property = field("property")
    field = field("field")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.FormInputValuePropertyBindingPropertiesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FormInputValuePropertyBindingPropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FormStyleConfig:
    boto3_raw_data: "type_defs.FormStyleConfigTypeDef" = dataclasses.field()

    tokenReference = field("tokenReference")
    value = field("value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FormStyleConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FormStyleConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCodegenJobRequest:
    boto3_raw_data: "type_defs.GetCodegenJobRequestTypeDef" = dataclasses.field()

    appId = field("appId")
    environmentName = field("environmentName")
    id = field("id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetCodegenJobRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCodegenJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetComponentRequest:
    boto3_raw_data: "type_defs.GetComponentRequestTypeDef" = dataclasses.field()

    appId = field("appId")
    environmentName = field("environmentName")
    id = field("id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetComponentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetComponentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFormRequest:
    boto3_raw_data: "type_defs.GetFormRequestTypeDef" = dataclasses.field()

    appId = field("appId")
    environmentName = field("environmentName")
    id = field("id")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetFormRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetFormRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMetadataRequest:
    boto3_raw_data: "type_defs.GetMetadataRequestTypeDef" = dataclasses.field()

    appId = field("appId")
    environmentName = field("environmentName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetMetadataRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMetadataRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetThemeRequest:
    boto3_raw_data: "type_defs.GetThemeRequestTypeDef" = dataclasses.field()

    appId = field("appId")
    environmentName = field("environmentName")
    id = field("id")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetThemeRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetThemeRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCodegenJobsRequest:
    boto3_raw_data: "type_defs.ListCodegenJobsRequestTypeDef" = dataclasses.field()

    appId = field("appId")
    environmentName = field("environmentName")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListCodegenJobsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCodegenJobsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListComponentsRequest:
    boto3_raw_data: "type_defs.ListComponentsRequestTypeDef" = dataclasses.field()

    appId = field("appId")
    environmentName = field("environmentName")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListComponentsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListComponentsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFormsRequest:
    boto3_raw_data: "type_defs.ListFormsRequestTypeDef" = dataclasses.field()

    appId = field("appId")
    environmentName = field("environmentName")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListFormsRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFormsRequestTypeDef"]
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

    resourceArn = field("resourceArn")

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
class ListThemesRequest:
    boto3_raw_data: "type_defs.ListThemesRequestTypeDef" = dataclasses.field()

    appId = field("appId")
    environmentName = field("environmentName")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListThemesRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListThemesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ThemeSummary:
    boto3_raw_data: "type_defs.ThemeSummaryTypeDef" = dataclasses.field()

    appId = field("appId")
    environmentName = field("environmentName")
    id = field("id")
    name = field("name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ThemeSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ThemeSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Predicate:
    boto3_raw_data: "type_defs.PredicateTypeDef" = dataclasses.field()

    or_ = field("or")
    and_ = field("and")
    field = field("field")
    operator = field("operator")
    operand = field("operand")
    operandType = field("operandType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PredicateTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PredicateTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutMetadataFlagBody:
    boto3_raw_data: "type_defs.PutMetadataFlagBodyTypeDef" = dataclasses.field()

    newValue = field("newValue")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutMetadataFlagBodyTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutMetadataFlagBodyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RefreshTokenRequestBody:
    boto3_raw_data: "type_defs.RefreshTokenRequestBodyTypeDef" = dataclasses.field()

    token = field("token")
    clientId = field("clientId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RefreshTokenRequestBodyTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RefreshTokenRequestBodyTypeDef"]
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

    resourceArn = field("resourceArn")
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
class ThemeValueOutput:
    boto3_raw_data: "type_defs.ThemeValueOutputTypeDef" = dataclasses.field()

    value = field("value")
    children = field("children")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ThemeValueOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ThemeValueOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ThemeValuePaginator:
    boto3_raw_data: "type_defs.ThemeValuePaginatorTypeDef" = dataclasses.field()

    value = field("value")
    children = field("children")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ThemeValuePaginatorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ThemeValuePaginatorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ThemeValue:
    boto3_raw_data: "type_defs.ThemeValueTypeDef" = dataclasses.field()

    value = field("value")
    children = field("children")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ThemeValueTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ThemeValueTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UntagResourceRequest:
    boto3_raw_data: "type_defs.UntagResourceRequestTypeDef" = dataclasses.field()

    resourceArn = field("resourceArn")
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
class ApiConfigurationOutput:
    boto3_raw_data: "type_defs.ApiConfigurationOutputTypeDef" = dataclasses.field()

    @cached_property
    def graphQLConfig(self):  # pragma: no cover
        return GraphQLRenderConfig.make_one(self.boto3_raw_data["graphQLConfig"])

    dataStoreConfig = field("dataStoreConfig")
    noApiConfig = field("noApiConfig")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ApiConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ApiConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApiConfiguration:
    boto3_raw_data: "type_defs.ApiConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def graphQLConfig(self):  # pragma: no cover
        return GraphQLRenderConfig.make_one(self.boto3_raw_data["graphQLConfig"])

    dataStoreConfig = field("dataStoreConfig")
    noApiConfig = field("noApiConfig")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ApiConfigurationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ApiConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CodegenGenericDataFieldOutput:
    boto3_raw_data: "type_defs.CodegenGenericDataFieldOutputTypeDef" = (
        dataclasses.field()
    )

    dataType = field("dataType")
    dataTypeValue = field("dataTypeValue")
    required = field("required")
    readOnly = field("readOnly")
    isArray = field("isArray")

    @cached_property
    def relationship(self):  # pragma: no cover
        return CodegenGenericDataRelationshipTypeOutput.make_one(
            self.boto3_raw_data["relationship"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CodegenGenericDataFieldOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CodegenGenericDataFieldOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ComponentBindingPropertiesValuePropertiesOutput:
    boto3_raw_data: (
        "type_defs.ComponentBindingPropertiesValuePropertiesOutputTypeDef"
    ) = dataclasses.field()

    model = field("model")
    field = field("field")

    @cached_property
    def predicates(self):  # pragma: no cover
        return PredicateOutput.make_many(self.boto3_raw_data["predicates"])

    userAttribute = field("userAttribute")
    bucket = field("bucket")
    key = field("key")
    defaultValue = field("defaultValue")
    slotName = field("slotName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ComponentBindingPropertiesValuePropertiesOutputTypeDef"
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
                "type_defs.ComponentBindingPropertiesValuePropertiesOutputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ComponentBindingPropertiesValuePropertiesPaginator:
    boto3_raw_data: (
        "type_defs.ComponentBindingPropertiesValuePropertiesPaginatorTypeDef"
    ) = dataclasses.field()

    model = field("model")
    field = field("field")

    @cached_property
    def predicates(self):  # pragma: no cover
        return PredicatePaginator.make_many(self.boto3_raw_data["predicates"])

    userAttribute = field("userAttribute")
    bucket = field("bucket")
    key = field("key")
    defaultValue = field("defaultValue")
    slotName = field("slotName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ComponentBindingPropertiesValuePropertiesPaginatorTypeDef"
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
                "type_defs.ComponentBindingPropertiesValuePropertiesPaginatorTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ComponentDataConfigurationOutput:
    boto3_raw_data: "type_defs.ComponentDataConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    model = field("model")

    @cached_property
    def sort(self):  # pragma: no cover
        return SortProperty.make_many(self.boto3_raw_data["sort"])

    @cached_property
    def predicate(self):  # pragma: no cover
        return PredicateOutput.make_one(self.boto3_raw_data["predicate"])

    identifiers = field("identifiers")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ComponentDataConfigurationOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ComponentDataConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ComponentDataConfigurationPaginator:
    boto3_raw_data: "type_defs.ComponentDataConfigurationPaginatorTypeDef" = (
        dataclasses.field()
    )

    model = field("model")

    @cached_property
    def sort(self):  # pragma: no cover
        return SortProperty.make_many(self.boto3_raw_data["sort"])

    @cached_property
    def predicate(self):  # pragma: no cover
        return PredicatePaginator.make_one(self.boto3_raw_data["predicate"])

    identifiers = field("identifiers")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ComponentDataConfigurationPaginatorTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ComponentDataConfigurationPaginatorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ComponentPropertyOutput:
    boto3_raw_data: "type_defs.ComponentPropertyOutputTypeDef" = dataclasses.field()

    value = field("value")

    @cached_property
    def bindingProperties(self):  # pragma: no cover
        return ComponentPropertyBindingProperties.make_one(
            self.boto3_raw_data["bindingProperties"]
        )

    @cached_property
    def collectionBindingProperties(self):  # pragma: no cover
        return ComponentPropertyBindingProperties.make_one(
            self.boto3_raw_data["collectionBindingProperties"]
        )

    defaultValue = field("defaultValue")
    model = field("model")
    bindings = field("bindings")
    event = field("event")
    userAttribute = field("userAttribute")
    concat = field("concat")

    @cached_property
    def condition(self):  # pragma: no cover
        return ComponentConditionPropertyOutput.make_one(
            self.boto3_raw_data["condition"]
        )

    configured = field("configured")
    type = field("type")
    importedValue = field("importedValue")
    componentName = field("componentName")
    property = field("property")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ComponentPropertyOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ComponentPropertyOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ComponentPropertyPaginator:
    boto3_raw_data: "type_defs.ComponentPropertyPaginatorTypeDef" = dataclasses.field()

    value = field("value")

    @cached_property
    def bindingProperties(self):  # pragma: no cover
        return ComponentPropertyBindingProperties.make_one(
            self.boto3_raw_data["bindingProperties"]
        )

    @cached_property
    def collectionBindingProperties(self):  # pragma: no cover
        return ComponentPropertyBindingProperties.make_one(
            self.boto3_raw_data["collectionBindingProperties"]
        )

    defaultValue = field("defaultValue")
    model = field("model")
    bindings = field("bindings")
    event = field("event")
    userAttribute = field("userAttribute")
    concat = field("concat")

    @cached_property
    def condition(self):  # pragma: no cover
        return ComponentConditionPropertyPaginator.make_one(
            self.boto3_raw_data["condition"]
        )

    configured = field("configured")
    type = field("type")
    importedValue = field("importedValue")
    componentName = field("componentName")
    property = field("property")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ComponentPropertyPaginatorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ComponentPropertyPaginatorTypeDef"]
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
class ExchangeCodeForTokenResponse:
    boto3_raw_data: "type_defs.ExchangeCodeForTokenResponseTypeDef" = (
        dataclasses.field()
    )

    accessToken = field("accessToken")
    expiresIn = field("expiresIn")
    refreshToken = field("refreshToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExchangeCodeForTokenResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExchangeCodeForTokenResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMetadataResponse:
    boto3_raw_data: "type_defs.GetMetadataResponseTypeDef" = dataclasses.field()

    features = field("features")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetMetadataResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMetadataResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCodegenJobsResponse:
    boto3_raw_data: "type_defs.ListCodegenJobsResponseTypeDef" = dataclasses.field()

    @cached_property
    def entities(self):  # pragma: no cover
        return CodegenJobSummary.make_many(self.boto3_raw_data["entities"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListCodegenJobsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCodegenJobsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListComponentsResponse:
    boto3_raw_data: "type_defs.ListComponentsResponseTypeDef" = dataclasses.field()

    @cached_property
    def entities(self):  # pragma: no cover
        return ComponentSummary.make_many(self.boto3_raw_data["entities"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListComponentsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListComponentsResponseTypeDef"]
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
class RefreshTokenResponse:
    boto3_raw_data: "type_defs.RefreshTokenResponseTypeDef" = dataclasses.field()

    accessToken = field("accessToken")
    expiresIn = field("expiresIn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RefreshTokenResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RefreshTokenResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FormSummary:
    boto3_raw_data: "type_defs.FormSummaryTypeDef" = dataclasses.field()

    appId = field("appId")

    @cached_property
    def dataType(self):  # pragma: no cover
        return FormDataTypeConfig.make_one(self.boto3_raw_data["dataType"])

    environmentName = field("environmentName")
    formActionType = field("formActionType")
    id = field("id")
    name = field("name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FormSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FormSummaryTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExchangeCodeForTokenRequest:
    boto3_raw_data: "type_defs.ExchangeCodeForTokenRequestTypeDef" = dataclasses.field()

    provider = field("provider")

    @cached_property
    def request(self):  # pragma: no cover
        return ExchangeCodeForTokenRequestBody.make_one(self.boto3_raw_data["request"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExchangeCodeForTokenRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExchangeCodeForTokenRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExportComponentsRequestPaginate:
    boto3_raw_data: "type_defs.ExportComponentsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    appId = field("appId")
    environmentName = field("environmentName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ExportComponentsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExportComponentsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExportFormsRequestPaginate:
    boto3_raw_data: "type_defs.ExportFormsRequestPaginateTypeDef" = dataclasses.field()

    appId = field("appId")
    environmentName = field("environmentName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExportFormsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExportFormsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExportThemesRequestPaginate:
    boto3_raw_data: "type_defs.ExportThemesRequestPaginateTypeDef" = dataclasses.field()

    appId = field("appId")
    environmentName = field("environmentName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExportThemesRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExportThemesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCodegenJobsRequestPaginate:
    boto3_raw_data: "type_defs.ListCodegenJobsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    appId = field("appId")
    environmentName = field("environmentName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListCodegenJobsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCodegenJobsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListComponentsRequestPaginate:
    boto3_raw_data: "type_defs.ListComponentsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    appId = field("appId")
    environmentName = field("environmentName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListComponentsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListComponentsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFormsRequestPaginate:
    boto3_raw_data: "type_defs.ListFormsRequestPaginateTypeDef" = dataclasses.field()

    appId = field("appId")
    environmentName = field("environmentName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListFormsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFormsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListThemesRequestPaginate:
    boto3_raw_data: "type_defs.ListThemesRequestPaginateTypeDef" = dataclasses.field()

    appId = field("appId")
    environmentName = field("environmentName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListThemesRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListThemesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FormButton:
    boto3_raw_data: "type_defs.FormButtonTypeDef" = dataclasses.field()

    excluded = field("excluded")
    children = field("children")

    @cached_property
    def position(self):  # pragma: no cover
        return FieldPosition.make_one(self.boto3_raw_data["position"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FormButtonTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FormButtonTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SectionalElement:
    boto3_raw_data: "type_defs.SectionalElementTypeDef" = dataclasses.field()

    type = field("type")

    @cached_property
    def position(self):  # pragma: no cover
        return FieldPosition.make_one(self.boto3_raw_data["position"])

    text = field("text")
    level = field("level")
    orientation = field("orientation")
    excluded = field("excluded")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SectionalElementTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SectionalElementTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FormInputBindingPropertiesValue:
    boto3_raw_data: "type_defs.FormInputBindingPropertiesValueTypeDef" = (
        dataclasses.field()
    )

    type = field("type")

    @cached_property
    def bindingProperties(self):  # pragma: no cover
        return FormInputBindingPropertiesValueProperties.make_one(
            self.boto3_raw_data["bindingProperties"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.FormInputBindingPropertiesValueTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FormInputBindingPropertiesValueTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FormInputValuePropertyOutput:
    boto3_raw_data: "type_defs.FormInputValuePropertyOutputTypeDef" = (
        dataclasses.field()
    )

    value = field("value")

    @cached_property
    def bindingProperties(self):  # pragma: no cover
        return FormInputValuePropertyBindingProperties.make_one(
            self.boto3_raw_data["bindingProperties"]
        )

    concat = field("concat")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FormInputValuePropertyOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FormInputValuePropertyOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FormInputValuePropertyPaginator:
    boto3_raw_data: "type_defs.FormInputValuePropertyPaginatorTypeDef" = (
        dataclasses.field()
    )

    value = field("value")

    @cached_property
    def bindingProperties(self):  # pragma: no cover
        return FormInputValuePropertyBindingProperties.make_one(
            self.boto3_raw_data["bindingProperties"]
        )

    concat = field("concat")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.FormInputValuePropertyPaginatorTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FormInputValuePropertyPaginatorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FormInputValueProperty:
    boto3_raw_data: "type_defs.FormInputValuePropertyTypeDef" = dataclasses.field()

    value = field("value")

    @cached_property
    def bindingProperties(self):  # pragma: no cover
        return FormInputValuePropertyBindingProperties.make_one(
            self.boto3_raw_data["bindingProperties"]
        )

    concat = field("concat")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FormInputValuePropertyTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FormInputValuePropertyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FormStyle:
    boto3_raw_data: "type_defs.FormStyleTypeDef" = dataclasses.field()

    @cached_property
    def horizontalGap(self):  # pragma: no cover
        return FormStyleConfig.make_one(self.boto3_raw_data["horizontalGap"])

    @cached_property
    def verticalGap(self):  # pragma: no cover
        return FormStyleConfig.make_one(self.boto3_raw_data["verticalGap"])

    @cached_property
    def outerPadding(self):  # pragma: no cover
        return FormStyleConfig.make_one(self.boto3_raw_data["outerPadding"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FormStyleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FormStyleTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListThemesResponse:
    boto3_raw_data: "type_defs.ListThemesResponseTypeDef" = dataclasses.field()

    @cached_property
    def entities(self):  # pragma: no cover
        return ThemeSummary.make_many(self.boto3_raw_data["entities"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListThemesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListThemesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutMetadataFlagRequest:
    boto3_raw_data: "type_defs.PutMetadataFlagRequestTypeDef" = dataclasses.field()

    appId = field("appId")
    environmentName = field("environmentName")
    featureName = field("featureName")

    @cached_property
    def body(self):  # pragma: no cover
        return PutMetadataFlagBody.make_one(self.boto3_raw_data["body"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutMetadataFlagRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutMetadataFlagRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RefreshTokenRequest:
    boto3_raw_data: "type_defs.RefreshTokenRequestTypeDef" = dataclasses.field()

    provider = field("provider")

    @cached_property
    def refreshTokenBody(self):  # pragma: no cover
        return RefreshTokenRequestBody.make_one(self.boto3_raw_data["refreshTokenBody"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RefreshTokenRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RefreshTokenRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ThemeValuesOutput:
    boto3_raw_data: "type_defs.ThemeValuesOutputTypeDef" = dataclasses.field()

    key = field("key")

    @cached_property
    def value(self):  # pragma: no cover
        return ThemeValueOutput.make_one(self.boto3_raw_data["value"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ThemeValuesOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ThemeValuesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ThemeValuesPaginator:
    boto3_raw_data: "type_defs.ThemeValuesPaginatorTypeDef" = dataclasses.field()

    key = field("key")

    @cached_property
    def value(self):  # pragma: no cover
        return ThemeValuePaginator.make_one(self.boto3_raw_data["value"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ThemeValuesPaginatorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ThemeValuesPaginatorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReactStartCodegenJobDataOutput:
    boto3_raw_data: "type_defs.ReactStartCodegenJobDataOutputTypeDef" = (
        dataclasses.field()
    )

    module = field("module")
    target = field("target")
    script = field("script")
    renderTypeDeclarations = field("renderTypeDeclarations")
    inlineSourceMap = field("inlineSourceMap")

    @cached_property
    def apiConfiguration(self):  # pragma: no cover
        return ApiConfigurationOutput.make_one(self.boto3_raw_data["apiConfiguration"])

    dependencies = field("dependencies")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ReactStartCodegenJobDataOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReactStartCodegenJobDataOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CodegenGenericDataModelOutput:
    boto3_raw_data: "type_defs.CodegenGenericDataModelOutputTypeDef" = (
        dataclasses.field()
    )

    fields = field("fields")
    primaryKeys = field("primaryKeys")
    isJoinTable = field("isJoinTable")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CodegenGenericDataModelOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CodegenGenericDataModelOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CodegenGenericDataNonModelOutput:
    boto3_raw_data: "type_defs.CodegenGenericDataNonModelOutputTypeDef" = (
        dataclasses.field()
    )

    fields = field("fields")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CodegenGenericDataNonModelOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CodegenGenericDataNonModelOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CodegenGenericDataField:
    boto3_raw_data: "type_defs.CodegenGenericDataFieldTypeDef" = dataclasses.field()

    dataType = field("dataType")
    dataTypeValue = field("dataTypeValue")
    required = field("required")
    readOnly = field("readOnly")
    isArray = field("isArray")
    relationship = field("relationship")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CodegenGenericDataFieldTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CodegenGenericDataFieldTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ComponentBindingPropertiesValueOutput:
    boto3_raw_data: "type_defs.ComponentBindingPropertiesValueOutputTypeDef" = (
        dataclasses.field()
    )

    type = field("type")

    @cached_property
    def bindingProperties(self):  # pragma: no cover
        return ComponentBindingPropertiesValuePropertiesOutput.make_one(
            self.boto3_raw_data["bindingProperties"]
        )

    defaultValue = field("defaultValue")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ComponentBindingPropertiesValueOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ComponentBindingPropertiesValueOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ComponentBindingPropertiesValuePaginator:
    boto3_raw_data: "type_defs.ComponentBindingPropertiesValuePaginatorTypeDef" = (
        dataclasses.field()
    )

    type = field("type")

    @cached_property
    def bindingProperties(self):  # pragma: no cover
        return ComponentBindingPropertiesValuePropertiesPaginator.make_one(
            self.boto3_raw_data["bindingProperties"]
        )

    defaultValue = field("defaultValue")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ComponentBindingPropertiesValuePaginatorTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ComponentBindingPropertiesValuePaginatorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ComponentProperty:
    boto3_raw_data: "type_defs.ComponentPropertyTypeDef" = dataclasses.field()

    value = field("value")

    @cached_property
    def bindingProperties(self):  # pragma: no cover
        return ComponentPropertyBindingProperties.make_one(
            self.boto3_raw_data["bindingProperties"]
        )

    @cached_property
    def collectionBindingProperties(self):  # pragma: no cover
        return ComponentPropertyBindingProperties.make_one(
            self.boto3_raw_data["collectionBindingProperties"]
        )

    defaultValue = field("defaultValue")
    model = field("model")
    bindings = field("bindings")
    event = field("event")
    userAttribute = field("userAttribute")
    concat = field("concat")
    condition = field("condition")
    configured = field("configured")
    type = field("type")
    importedValue = field("importedValue")
    componentName = field("componentName")
    property = field("property")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ComponentPropertyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ComponentPropertyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MutationActionSetStateParameterOutput:
    boto3_raw_data: "type_defs.MutationActionSetStateParameterOutputTypeDef" = (
        dataclasses.field()
    )

    componentName = field("componentName")
    property = field("property")

    @cached_property
    def set(self):  # pragma: no cover
        return ComponentPropertyOutput.make_one(self.boto3_raw_data["set"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.MutationActionSetStateParameterOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MutationActionSetStateParameterOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MutationActionSetStateParameterPaginator:
    boto3_raw_data: "type_defs.MutationActionSetStateParameterPaginatorTypeDef" = (
        dataclasses.field()
    )

    componentName = field("componentName")
    property = field("property")

    @cached_property
    def set(self):  # pragma: no cover
        return ComponentPropertyPaginator.make_one(self.boto3_raw_data["set"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.MutationActionSetStateParameterPaginatorTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MutationActionSetStateParameterPaginatorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFormsResponse:
    boto3_raw_data: "type_defs.ListFormsResponseTypeDef" = dataclasses.field()

    @cached_property
    def entities(self):  # pragma: no cover
        return FormSummary.make_many(self.boto3_raw_data["entities"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListFormsResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFormsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FormCTA:
    boto3_raw_data: "type_defs.FormCTATypeDef" = dataclasses.field()

    position = field("position")

    @cached_property
    def clear(self):  # pragma: no cover
        return FormButton.make_one(self.boto3_raw_data["clear"])

    @cached_property
    def cancel(self):  # pragma: no cover
        return FormButton.make_one(self.boto3_raw_data["cancel"])

    @cached_property
    def submit(self):  # pragma: no cover
        return FormButton.make_one(self.boto3_raw_data["submit"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FormCTATypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FormCTATypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ValueMappingOutput:
    boto3_raw_data: "type_defs.ValueMappingOutputTypeDef" = dataclasses.field()

    @cached_property
    def value(self):  # pragma: no cover
        return FormInputValuePropertyOutput.make_one(self.boto3_raw_data["value"])

    @cached_property
    def displayValue(self):  # pragma: no cover
        return FormInputValuePropertyOutput.make_one(
            self.boto3_raw_data["displayValue"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ValueMappingOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ValueMappingOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ValueMappingPaginator:
    boto3_raw_data: "type_defs.ValueMappingPaginatorTypeDef" = dataclasses.field()

    @cached_property
    def value(self):  # pragma: no cover
        return FormInputValuePropertyPaginator.make_one(self.boto3_raw_data["value"])

    @cached_property
    def displayValue(self):  # pragma: no cover
        return FormInputValuePropertyPaginator.make_one(
            self.boto3_raw_data["displayValue"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ValueMappingPaginatorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ValueMappingPaginatorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ComponentBindingPropertiesValueProperties:
    boto3_raw_data: "type_defs.ComponentBindingPropertiesValuePropertiesTypeDef" = (
        dataclasses.field()
    )

    model = field("model")
    field = field("field")
    predicates = field("predicates")
    userAttribute = field("userAttribute")
    bucket = field("bucket")
    key = field("key")
    defaultValue = field("defaultValue")
    slotName = field("slotName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ComponentBindingPropertiesValuePropertiesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ComponentBindingPropertiesValuePropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ComponentDataConfiguration:
    boto3_raw_data: "type_defs.ComponentDataConfigurationTypeDef" = dataclasses.field()

    model = field("model")

    @cached_property
    def sort(self):  # pragma: no cover
        return SortProperty.make_many(self.boto3_raw_data["sort"])

    predicate = field("predicate")
    identifiers = field("identifiers")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ComponentDataConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ComponentDataConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Theme:
    boto3_raw_data: "type_defs.ThemeTypeDef" = dataclasses.field()

    appId = field("appId")
    environmentName = field("environmentName")
    id = field("id")
    name = field("name")
    createdAt = field("createdAt")

    @cached_property
    def values(self):  # pragma: no cover
        return ThemeValuesOutput.make_many(self.boto3_raw_data["values"])

    modifiedAt = field("modifiedAt")

    @cached_property
    def overrides(self):  # pragma: no cover
        return ThemeValuesOutput.make_many(self.boto3_raw_data["overrides"])

    tags = field("tags")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ThemeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ThemeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ThemePaginator:
    boto3_raw_data: "type_defs.ThemePaginatorTypeDef" = dataclasses.field()

    appId = field("appId")
    environmentName = field("environmentName")
    id = field("id")
    name = field("name")
    createdAt = field("createdAt")

    @cached_property
    def values(self):  # pragma: no cover
        return ThemeValuesPaginator.make_many(self.boto3_raw_data["values"])

    modifiedAt = field("modifiedAt")

    @cached_property
    def overrides(self):  # pragma: no cover
        return ThemeValuesPaginator.make_many(self.boto3_raw_data["overrides"])

    tags = field("tags")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ThemePaginatorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ThemePaginatorTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ThemeValues:
    boto3_raw_data: "type_defs.ThemeValuesTypeDef" = dataclasses.field()

    key = field("key")
    value = field("value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ThemeValuesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ThemeValuesTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CodegenJobRenderConfigOutput:
    boto3_raw_data: "type_defs.CodegenJobRenderConfigOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def react(self):  # pragma: no cover
        return ReactStartCodegenJobDataOutput.make_one(self.boto3_raw_data["react"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CodegenJobRenderConfigOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CodegenJobRenderConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReactStartCodegenJobData:
    boto3_raw_data: "type_defs.ReactStartCodegenJobDataTypeDef" = dataclasses.field()

    module = field("module")
    target = field("target")
    script = field("script")
    renderTypeDeclarations = field("renderTypeDeclarations")
    inlineSourceMap = field("inlineSourceMap")
    apiConfiguration = field("apiConfiguration")
    dependencies = field("dependencies")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReactStartCodegenJobDataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReactStartCodegenJobDataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CodegenJobGenericDataSchemaOutput:
    boto3_raw_data: "type_defs.CodegenJobGenericDataSchemaOutputTypeDef" = (
        dataclasses.field()
    )

    dataSourceType = field("dataSourceType")
    models = field("models")
    enums = field("enums")
    nonModels = field("nonModels")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CodegenJobGenericDataSchemaOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CodegenJobGenericDataSchemaOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CodegenGenericDataModel:
    boto3_raw_data: "type_defs.CodegenGenericDataModelTypeDef" = dataclasses.field()

    fields = field("fields")
    primaryKeys = field("primaryKeys")
    isJoinTable = field("isJoinTable")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CodegenGenericDataModelTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CodegenGenericDataModelTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActionParametersOutput:
    boto3_raw_data: "type_defs.ActionParametersOutputTypeDef" = dataclasses.field()

    @cached_property
    def type(self):  # pragma: no cover
        return ComponentPropertyOutput.make_one(self.boto3_raw_data["type"])

    @cached_property
    def url(self):  # pragma: no cover
        return ComponentPropertyOutput.make_one(self.boto3_raw_data["url"])

    @cached_property
    def anchor(self):  # pragma: no cover
        return ComponentPropertyOutput.make_one(self.boto3_raw_data["anchor"])

    @cached_property
    def target(self):  # pragma: no cover
        return ComponentPropertyOutput.make_one(self.boto3_raw_data["target"])

    @cached_property
    def global_(self):  # pragma: no cover
        return ComponentPropertyOutput.make_one(self.boto3_raw_data["global"])

    model = field("model")

    @cached_property
    def id(self):  # pragma: no cover
        return ComponentPropertyOutput.make_one(self.boto3_raw_data["id"])

    fields = field("fields")

    @cached_property
    def state(self):  # pragma: no cover
        return MutationActionSetStateParameterOutput.make_one(
            self.boto3_raw_data["state"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ActionParametersOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ActionParametersOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActionParametersPaginator:
    boto3_raw_data: "type_defs.ActionParametersPaginatorTypeDef" = dataclasses.field()

    @cached_property
    def type(self):  # pragma: no cover
        return ComponentPropertyPaginator.make_one(self.boto3_raw_data["type"])

    @cached_property
    def url(self):  # pragma: no cover
        return ComponentPropertyPaginator.make_one(self.boto3_raw_data["url"])

    @cached_property
    def anchor(self):  # pragma: no cover
        return ComponentPropertyPaginator.make_one(self.boto3_raw_data["anchor"])

    @cached_property
    def target(self):  # pragma: no cover
        return ComponentPropertyPaginator.make_one(self.boto3_raw_data["target"])

    @cached_property
    def global_(self):  # pragma: no cover
        return ComponentPropertyPaginator.make_one(self.boto3_raw_data["global"])

    model = field("model")

    @cached_property
    def id(self):  # pragma: no cover
        return ComponentPropertyPaginator.make_one(self.boto3_raw_data["id"])

    fields = field("fields")

    @cached_property
    def state(self):  # pragma: no cover
        return MutationActionSetStateParameterPaginator.make_one(
            self.boto3_raw_data["state"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ActionParametersPaginatorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ActionParametersPaginatorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ValueMappingsOutput:
    boto3_raw_data: "type_defs.ValueMappingsOutputTypeDef" = dataclasses.field()

    @cached_property
    def values(self):  # pragma: no cover
        return ValueMappingOutput.make_many(self.boto3_raw_data["values"])

    bindingProperties = field("bindingProperties")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ValueMappingsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ValueMappingsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ValueMappingsPaginator:
    boto3_raw_data: "type_defs.ValueMappingsPaginatorTypeDef" = dataclasses.field()

    @cached_property
    def values(self):  # pragma: no cover
        return ValueMappingPaginator.make_many(self.boto3_raw_data["values"])

    bindingProperties = field("bindingProperties")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ValueMappingsPaginatorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ValueMappingsPaginatorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ValueMapping:
    boto3_raw_data: "type_defs.ValueMappingTypeDef" = dataclasses.field()

    value = field("value")
    displayValue = field("displayValue")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ValueMappingTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ValueMappingTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateThemeResponse:
    boto3_raw_data: "type_defs.CreateThemeResponseTypeDef" = dataclasses.field()

    @cached_property
    def entity(self):  # pragma: no cover
        return Theme.make_one(self.boto3_raw_data["entity"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateThemeResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateThemeResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExportThemesResponse:
    boto3_raw_data: "type_defs.ExportThemesResponseTypeDef" = dataclasses.field()

    @cached_property
    def entities(self):  # pragma: no cover
        return Theme.make_many(self.boto3_raw_data["entities"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExportThemesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExportThemesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetThemeResponse:
    boto3_raw_data: "type_defs.GetThemeResponseTypeDef" = dataclasses.field()

    @cached_property
    def theme(self):  # pragma: no cover
        return Theme.make_one(self.boto3_raw_data["theme"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetThemeResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetThemeResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateThemeResponse:
    boto3_raw_data: "type_defs.UpdateThemeResponseTypeDef" = dataclasses.field()

    @cached_property
    def entity(self):  # pragma: no cover
        return Theme.make_one(self.boto3_raw_data["entity"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateThemeResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateThemeResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExportThemesResponsePaginator:
    boto3_raw_data: "type_defs.ExportThemesResponsePaginatorTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def entities(self):  # pragma: no cover
        return ThemePaginator.make_many(self.boto3_raw_data["entities"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ExportThemesResponsePaginatorTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExportThemesResponsePaginatorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CodegenJob:
    boto3_raw_data: "type_defs.CodegenJobTypeDef" = dataclasses.field()

    id = field("id")
    appId = field("appId")
    environmentName = field("environmentName")

    @cached_property
    def renderConfig(self):  # pragma: no cover
        return CodegenJobRenderConfigOutput.make_one(
            self.boto3_raw_data["renderConfig"]
        )

    @cached_property
    def genericDataSchema(self):  # pragma: no cover
        return CodegenJobGenericDataSchemaOutput.make_one(
            self.boto3_raw_data["genericDataSchema"]
        )

    autoGenerateForms = field("autoGenerateForms")

    @cached_property
    def features(self):  # pragma: no cover
        return CodegenFeatureFlags.make_one(self.boto3_raw_data["features"])

    status = field("status")
    statusMessage = field("statusMessage")

    @cached_property
    def asset(self):  # pragma: no cover
        return CodegenJobAsset.make_one(self.boto3_raw_data["asset"])

    tags = field("tags")
    createdAt = field("createdAt")
    modifiedAt = field("modifiedAt")

    @cached_property
    def dependencies(self):  # pragma: no cover
        return CodegenDependency.make_many(self.boto3_raw_data["dependencies"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CodegenJobTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CodegenJobTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CodegenGenericDataNonModel:
    boto3_raw_data: "type_defs.CodegenGenericDataNonModelTypeDef" = dataclasses.field()

    fields = field("fields")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CodegenGenericDataNonModelTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CodegenGenericDataNonModelTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MutationActionSetStateParameter:
    boto3_raw_data: "type_defs.MutationActionSetStateParameterTypeDef" = (
        dataclasses.field()
    )

    componentName = field("componentName")
    property = field("property")
    set = field("set")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.MutationActionSetStateParameterTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MutationActionSetStateParameterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ComponentEventOutput:
    boto3_raw_data: "type_defs.ComponentEventOutputTypeDef" = dataclasses.field()

    action = field("action")

    @cached_property
    def parameters(self):  # pragma: no cover
        return ActionParametersOutput.make_one(self.boto3_raw_data["parameters"])

    bindingEvent = field("bindingEvent")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ComponentEventOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ComponentEventOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ComponentEventPaginator:
    boto3_raw_data: "type_defs.ComponentEventPaginatorTypeDef" = dataclasses.field()

    action = field("action")

    @cached_property
    def parameters(self):  # pragma: no cover
        return ActionParametersPaginator.make_one(self.boto3_raw_data["parameters"])

    bindingEvent = field("bindingEvent")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ComponentEventPaginatorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ComponentEventPaginatorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FieldInputConfigOutput:
    boto3_raw_data: "type_defs.FieldInputConfigOutputTypeDef" = dataclasses.field()

    type = field("type")
    required = field("required")
    readOnly = field("readOnly")
    placeholder = field("placeholder")
    defaultValue = field("defaultValue")
    descriptiveText = field("descriptiveText")
    defaultChecked = field("defaultChecked")
    defaultCountryCode = field("defaultCountryCode")

    @cached_property
    def valueMappings(self):  # pragma: no cover
        return ValueMappingsOutput.make_one(self.boto3_raw_data["valueMappings"])

    name = field("name")
    minValue = field("minValue")
    maxValue = field("maxValue")
    step = field("step")
    value = field("value")
    isArray = field("isArray")

    @cached_property
    def fileUploaderConfig(self):  # pragma: no cover
        return FileUploaderFieldConfigOutput.make_one(
            self.boto3_raw_data["fileUploaderConfig"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FieldInputConfigOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FieldInputConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FieldInputConfigPaginator:
    boto3_raw_data: "type_defs.FieldInputConfigPaginatorTypeDef" = dataclasses.field()

    type = field("type")
    required = field("required")
    readOnly = field("readOnly")
    placeholder = field("placeholder")
    defaultValue = field("defaultValue")
    descriptiveText = field("descriptiveText")
    defaultChecked = field("defaultChecked")
    defaultCountryCode = field("defaultCountryCode")

    @cached_property
    def valueMappings(self):  # pragma: no cover
        return ValueMappingsPaginator.make_one(self.boto3_raw_data["valueMappings"])

    name = field("name")
    minValue = field("minValue")
    maxValue = field("maxValue")
    step = field("step")
    value = field("value")
    isArray = field("isArray")

    @cached_property
    def fileUploaderConfig(self):  # pragma: no cover
        return FileUploaderFieldConfigOutput.make_one(
            self.boto3_raw_data["fileUploaderConfig"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FieldInputConfigPaginatorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FieldInputConfigPaginatorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ComponentBindingPropertiesValue:
    boto3_raw_data: "type_defs.ComponentBindingPropertiesValueTypeDef" = (
        dataclasses.field()
    )

    type = field("type")
    bindingProperties = field("bindingProperties")
    defaultValue = field("defaultValue")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ComponentBindingPropertiesValueTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ComponentBindingPropertiesValueTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateThemeData:
    boto3_raw_data: "type_defs.CreateThemeDataTypeDef" = dataclasses.field()

    name = field("name")
    values = field("values")

    @cached_property
    def overrides(self):  # pragma: no cover
        return ThemeValues.make_many(self.boto3_raw_data["overrides"])

    tags = field("tags")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateThemeDataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CreateThemeDataTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateThemeData:
    boto3_raw_data: "type_defs.UpdateThemeDataTypeDef" = dataclasses.field()

    values = field("values")
    id = field("id")
    name = field("name")

    @cached_property
    def overrides(self):  # pragma: no cover
        return ThemeValues.make_many(self.boto3_raw_data["overrides"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateThemeDataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UpdateThemeDataTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CodegenJobRenderConfig:
    boto3_raw_data: "type_defs.CodegenJobRenderConfigTypeDef" = dataclasses.field()

    react = field("react")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CodegenJobRenderConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CodegenJobRenderConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCodegenJobResponse:
    boto3_raw_data: "type_defs.GetCodegenJobResponseTypeDef" = dataclasses.field()

    @cached_property
    def job(self):  # pragma: no cover
        return CodegenJob.make_one(self.boto3_raw_data["job"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetCodegenJobResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCodegenJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartCodegenJobResponse:
    boto3_raw_data: "type_defs.StartCodegenJobResponseTypeDef" = dataclasses.field()

    @cached_property
    def entity(self):  # pragma: no cover
        return CodegenJob.make_one(self.boto3_raw_data["entity"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartCodegenJobResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartCodegenJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ComponentChildOutput:
    boto3_raw_data: "type_defs.ComponentChildOutputTypeDef" = dataclasses.field()

    componentType = field("componentType")
    name = field("name")
    properties = field("properties")
    children = field("children")
    events = field("events")
    sourceId = field("sourceId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ComponentChildOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ComponentChildOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ComponentChildPaginator:
    boto3_raw_data: "type_defs.ComponentChildPaginatorTypeDef" = dataclasses.field()

    componentType = field("componentType")
    name = field("name")
    properties = field("properties")
    children = field("children")
    events = field("events")
    sourceId = field("sourceId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ComponentChildPaginatorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ComponentChildPaginatorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FieldConfigOutput:
    boto3_raw_data: "type_defs.FieldConfigOutputTypeDef" = dataclasses.field()

    label = field("label")

    @cached_property
    def position(self):  # pragma: no cover
        return FieldPosition.make_one(self.boto3_raw_data["position"])

    excluded = field("excluded")

    @cached_property
    def inputType(self):  # pragma: no cover
        return FieldInputConfigOutput.make_one(self.boto3_raw_data["inputType"])

    @cached_property
    def validations(self):  # pragma: no cover
        return FieldValidationConfigurationOutput.make_many(
            self.boto3_raw_data["validations"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FieldConfigOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FieldConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FieldConfigPaginator:
    boto3_raw_data: "type_defs.FieldConfigPaginatorTypeDef" = dataclasses.field()

    label = field("label")

    @cached_property
    def position(self):  # pragma: no cover
        return FieldPosition.make_one(self.boto3_raw_data["position"])

    excluded = field("excluded")

    @cached_property
    def inputType(self):  # pragma: no cover
        return FieldInputConfigPaginator.make_one(self.boto3_raw_data["inputType"])

    @cached_property
    def validations(self):  # pragma: no cover
        return FieldValidationConfigurationOutput.make_many(
            self.boto3_raw_data["validations"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FieldConfigPaginatorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FieldConfigPaginatorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ValueMappings:
    boto3_raw_data: "type_defs.ValueMappingsTypeDef" = dataclasses.field()

    values = field("values")
    bindingProperties = field("bindingProperties")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ValueMappingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ValueMappingsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateThemeRequest:
    boto3_raw_data: "type_defs.CreateThemeRequestTypeDef" = dataclasses.field()

    appId = field("appId")
    environmentName = field("environmentName")

    @cached_property
    def themeToCreate(self):  # pragma: no cover
        return CreateThemeData.make_one(self.boto3_raw_data["themeToCreate"])

    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateThemeRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateThemeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateThemeRequest:
    boto3_raw_data: "type_defs.UpdateThemeRequestTypeDef" = dataclasses.field()

    appId = field("appId")
    environmentName = field("environmentName")
    id = field("id")

    @cached_property
    def updatedTheme(self):  # pragma: no cover
        return UpdateThemeData.make_one(self.boto3_raw_data["updatedTheme"])

    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateThemeRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateThemeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CodegenJobGenericDataSchema:
    boto3_raw_data: "type_defs.CodegenJobGenericDataSchemaTypeDef" = dataclasses.field()

    dataSourceType = field("dataSourceType")
    models = field("models")
    enums = field("enums")
    nonModels = field("nonModels")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CodegenJobGenericDataSchemaTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CodegenJobGenericDataSchemaTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActionParameters:
    boto3_raw_data: "type_defs.ActionParametersTypeDef" = dataclasses.field()

    type = field("type")
    url = field("url")
    anchor = field("anchor")
    target = field("target")
    global_ = field("global")
    model = field("model")
    id = field("id")
    fields = field("fields")
    state = field("state")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ActionParametersTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ActionParametersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Component:
    boto3_raw_data: "type_defs.ComponentTypeDef" = dataclasses.field()

    appId = field("appId")
    environmentName = field("environmentName")
    id = field("id")
    name = field("name")
    componentType = field("componentType")
    properties = field("properties")

    @cached_property
    def variants(self):  # pragma: no cover
        return ComponentVariantOutput.make_many(self.boto3_raw_data["variants"])

    overrides = field("overrides")
    bindingProperties = field("bindingProperties")
    createdAt = field("createdAt")
    sourceId = field("sourceId")

    @cached_property
    def children(self):  # pragma: no cover
        return ComponentChildOutput.make_many(self.boto3_raw_data["children"])

    collectionProperties = field("collectionProperties")
    modifiedAt = field("modifiedAt")
    tags = field("tags")
    events = field("events")
    schemaVersion = field("schemaVersion")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ComponentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ComponentTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ComponentPaginator:
    boto3_raw_data: "type_defs.ComponentPaginatorTypeDef" = dataclasses.field()

    appId = field("appId")
    environmentName = field("environmentName")
    id = field("id")
    name = field("name")
    componentType = field("componentType")
    properties = field("properties")

    @cached_property
    def variants(self):  # pragma: no cover
        return ComponentVariantOutput.make_many(self.boto3_raw_data["variants"])

    overrides = field("overrides")
    bindingProperties = field("bindingProperties")
    createdAt = field("createdAt")
    sourceId = field("sourceId")

    @cached_property
    def children(self):  # pragma: no cover
        return ComponentChildPaginator.make_many(self.boto3_raw_data["children"])

    collectionProperties = field("collectionProperties")
    modifiedAt = field("modifiedAt")
    tags = field("tags")
    events = field("events")
    schemaVersion = field("schemaVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ComponentPaginatorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ComponentPaginatorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Form:
    boto3_raw_data: "type_defs.FormTypeDef" = dataclasses.field()

    appId = field("appId")
    environmentName = field("environmentName")
    id = field("id")
    name = field("name")
    formActionType = field("formActionType")

    @cached_property
    def style(self):  # pragma: no cover
        return FormStyle.make_one(self.boto3_raw_data["style"])

    @cached_property
    def dataType(self):  # pragma: no cover
        return FormDataTypeConfig.make_one(self.boto3_raw_data["dataType"])

    fields = field("fields")
    sectionalElements = field("sectionalElements")
    schemaVersion = field("schemaVersion")
    tags = field("tags")

    @cached_property
    def cta(self):  # pragma: no cover
        return FormCTA.make_one(self.boto3_raw_data["cta"])

    labelDecorator = field("labelDecorator")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FormTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FormTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FormPaginator:
    boto3_raw_data: "type_defs.FormPaginatorTypeDef" = dataclasses.field()

    appId = field("appId")
    environmentName = field("environmentName")
    id = field("id")
    name = field("name")
    formActionType = field("formActionType")

    @cached_property
    def style(self):  # pragma: no cover
        return FormStyle.make_one(self.boto3_raw_data["style"])

    @cached_property
    def dataType(self):  # pragma: no cover
        return FormDataTypeConfig.make_one(self.boto3_raw_data["dataType"])

    fields = field("fields")
    sectionalElements = field("sectionalElements")
    schemaVersion = field("schemaVersion")
    tags = field("tags")

    @cached_property
    def cta(self):  # pragma: no cover
        return FormCTA.make_one(self.boto3_raw_data["cta"])

    labelDecorator = field("labelDecorator")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FormPaginatorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FormPaginatorTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateComponentResponse:
    boto3_raw_data: "type_defs.CreateComponentResponseTypeDef" = dataclasses.field()

    @cached_property
    def entity(self):  # pragma: no cover
        return Component.make_one(self.boto3_raw_data["entity"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateComponentResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateComponentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExportComponentsResponse:
    boto3_raw_data: "type_defs.ExportComponentsResponseTypeDef" = dataclasses.field()

    @cached_property
    def entities(self):  # pragma: no cover
        return Component.make_many(self.boto3_raw_data["entities"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExportComponentsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExportComponentsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetComponentResponse:
    boto3_raw_data: "type_defs.GetComponentResponseTypeDef" = dataclasses.field()

    @cached_property
    def component(self):  # pragma: no cover
        return Component.make_one(self.boto3_raw_data["component"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetComponentResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetComponentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateComponentResponse:
    boto3_raw_data: "type_defs.UpdateComponentResponseTypeDef" = dataclasses.field()

    @cached_property
    def entity(self):  # pragma: no cover
        return Component.make_one(self.boto3_raw_data["entity"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateComponentResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateComponentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExportComponentsResponsePaginator:
    boto3_raw_data: "type_defs.ExportComponentsResponsePaginatorTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def entities(self):  # pragma: no cover
        return ComponentPaginator.make_many(self.boto3_raw_data["entities"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ExportComponentsResponsePaginatorTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExportComponentsResponsePaginatorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateFormResponse:
    boto3_raw_data: "type_defs.CreateFormResponseTypeDef" = dataclasses.field()

    @cached_property
    def entity(self):  # pragma: no cover
        return Form.make_one(self.boto3_raw_data["entity"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateFormResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateFormResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExportFormsResponse:
    boto3_raw_data: "type_defs.ExportFormsResponseTypeDef" = dataclasses.field()

    @cached_property
    def entities(self):  # pragma: no cover
        return Form.make_many(self.boto3_raw_data["entities"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExportFormsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExportFormsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFormResponse:
    boto3_raw_data: "type_defs.GetFormResponseTypeDef" = dataclasses.field()

    @cached_property
    def form(self):  # pragma: no cover
        return Form.make_one(self.boto3_raw_data["form"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetFormResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetFormResponseTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateFormResponse:
    boto3_raw_data: "type_defs.UpdateFormResponseTypeDef" = dataclasses.field()

    @cached_property
    def entity(self):  # pragma: no cover
        return Form.make_one(self.boto3_raw_data["entity"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateFormResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateFormResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExportFormsResponsePaginator:
    boto3_raw_data: "type_defs.ExportFormsResponsePaginatorTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def entities(self):  # pragma: no cover
        return FormPaginator.make_many(self.boto3_raw_data["entities"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExportFormsResponsePaginatorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExportFormsResponsePaginatorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FieldInputConfig:
    boto3_raw_data: "type_defs.FieldInputConfigTypeDef" = dataclasses.field()

    type = field("type")
    required = field("required")
    readOnly = field("readOnly")
    placeholder = field("placeholder")
    defaultValue = field("defaultValue")
    descriptiveText = field("descriptiveText")
    defaultChecked = field("defaultChecked")
    defaultCountryCode = field("defaultCountryCode")
    valueMappings = field("valueMappings")
    name = field("name")
    minValue = field("minValue")
    maxValue = field("maxValue")
    step = field("step")
    value = field("value")
    isArray = field("isArray")
    fileUploaderConfig = field("fileUploaderConfig")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FieldInputConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FieldInputConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartCodegenJobData:
    boto3_raw_data: "type_defs.StartCodegenJobDataTypeDef" = dataclasses.field()

    renderConfig = field("renderConfig")
    genericDataSchema = field("genericDataSchema")
    autoGenerateForms = field("autoGenerateForms")

    @cached_property
    def features(self):  # pragma: no cover
        return CodegenFeatureFlags.make_one(self.boto3_raw_data["features"])

    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartCodegenJobDataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartCodegenJobDataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ComponentEvent:
    boto3_raw_data: "type_defs.ComponentEventTypeDef" = dataclasses.field()

    action = field("action")
    parameters = field("parameters")
    bindingEvent = field("bindingEvent")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ComponentEventTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ComponentEventTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartCodegenJobRequest:
    boto3_raw_data: "type_defs.StartCodegenJobRequestTypeDef" = dataclasses.field()

    appId = field("appId")
    environmentName = field("environmentName")

    @cached_property
    def codegenJobToCreate(self):  # pragma: no cover
        return StartCodegenJobData.make_one(self.boto3_raw_data["codegenJobToCreate"])

    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartCodegenJobRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartCodegenJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ComponentChild:
    boto3_raw_data: "type_defs.ComponentChildTypeDef" = dataclasses.field()

    componentType = field("componentType")
    name = field("name")
    properties = field("properties")
    children = field("children")
    events = field("events")
    sourceId = field("sourceId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ComponentChildTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ComponentChildTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FieldConfig:
    boto3_raw_data: "type_defs.FieldConfigTypeDef" = dataclasses.field()

    label = field("label")

    @cached_property
    def position(self):  # pragma: no cover
        return FieldPosition.make_one(self.boto3_raw_data["position"])

    excluded = field("excluded")
    inputType = field("inputType")
    validations = field("validations")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FieldConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FieldConfigTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateComponentData:
    boto3_raw_data: "type_defs.CreateComponentDataTypeDef" = dataclasses.field()

    name = field("name")
    componentType = field("componentType")
    properties = field("properties")
    variants = field("variants")
    overrides = field("overrides")
    bindingProperties = field("bindingProperties")
    sourceId = field("sourceId")
    children = field("children")
    collectionProperties = field("collectionProperties")
    tags = field("tags")
    events = field("events")
    schemaVersion = field("schemaVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateComponentDataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateComponentDataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateComponentData:
    boto3_raw_data: "type_defs.UpdateComponentDataTypeDef" = dataclasses.field()

    id = field("id")
    name = field("name")
    sourceId = field("sourceId")
    componentType = field("componentType")
    properties = field("properties")
    children = field("children")
    variants = field("variants")
    overrides = field("overrides")
    bindingProperties = field("bindingProperties")
    collectionProperties = field("collectionProperties")
    events = field("events")
    schemaVersion = field("schemaVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateComponentDataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateComponentDataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateFormData:
    boto3_raw_data: "type_defs.CreateFormDataTypeDef" = dataclasses.field()

    name = field("name")

    @cached_property
    def dataType(self):  # pragma: no cover
        return FormDataTypeConfig.make_one(self.boto3_raw_data["dataType"])

    formActionType = field("formActionType")
    fields = field("fields")

    @cached_property
    def style(self):  # pragma: no cover
        return FormStyle.make_one(self.boto3_raw_data["style"])

    sectionalElements = field("sectionalElements")
    schemaVersion = field("schemaVersion")

    @cached_property
    def cta(self):  # pragma: no cover
        return FormCTA.make_one(self.boto3_raw_data["cta"])

    tags = field("tags")
    labelDecorator = field("labelDecorator")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateFormDataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CreateFormDataTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateFormData:
    boto3_raw_data: "type_defs.UpdateFormDataTypeDef" = dataclasses.field()

    name = field("name")

    @cached_property
    def dataType(self):  # pragma: no cover
        return FormDataTypeConfig.make_one(self.boto3_raw_data["dataType"])

    formActionType = field("formActionType")
    fields = field("fields")

    @cached_property
    def style(self):  # pragma: no cover
        return FormStyle.make_one(self.boto3_raw_data["style"])

    sectionalElements = field("sectionalElements")
    schemaVersion = field("schemaVersion")

    @cached_property
    def cta(self):  # pragma: no cover
        return FormCTA.make_one(self.boto3_raw_data["cta"])

    labelDecorator = field("labelDecorator")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateFormDataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UpdateFormDataTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateComponentRequest:
    boto3_raw_data: "type_defs.CreateComponentRequestTypeDef" = dataclasses.field()

    appId = field("appId")
    environmentName = field("environmentName")

    @cached_property
    def componentToCreate(self):  # pragma: no cover
        return CreateComponentData.make_one(self.boto3_raw_data["componentToCreate"])

    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateComponentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateComponentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateComponentRequest:
    boto3_raw_data: "type_defs.UpdateComponentRequestTypeDef" = dataclasses.field()

    appId = field("appId")
    environmentName = field("environmentName")
    id = field("id")

    @cached_property
    def updatedComponent(self):  # pragma: no cover
        return UpdateComponentData.make_one(self.boto3_raw_data["updatedComponent"])

    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateComponentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateComponentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateFormRequest:
    boto3_raw_data: "type_defs.CreateFormRequestTypeDef" = dataclasses.field()

    appId = field("appId")
    environmentName = field("environmentName")

    @cached_property
    def formToCreate(self):  # pragma: no cover
        return CreateFormData.make_one(self.boto3_raw_data["formToCreate"])

    clientToken = field("clientToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateFormRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateFormRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateFormRequest:
    boto3_raw_data: "type_defs.UpdateFormRequestTypeDef" = dataclasses.field()

    appId = field("appId")
    environmentName = field("environmentName")
    id = field("id")

    @cached_property
    def updatedForm(self):  # pragma: no cover
        return UpdateFormData.make_one(self.boto3_raw_data["updatedForm"])

    clientToken = field("clientToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateFormRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateFormRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
