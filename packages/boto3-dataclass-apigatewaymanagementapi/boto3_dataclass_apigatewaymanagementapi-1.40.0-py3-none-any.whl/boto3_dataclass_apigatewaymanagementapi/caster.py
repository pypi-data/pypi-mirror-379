# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_apigatewaymanagementapi import type_defs as bs_td


class APIGATEWAYMANAGEMENTAPICaster:

    def delete_connection(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def get_connection(
        self,
        res: "bs_td.GetConnectionResponseTypeDef",
    ) -> "dc_td.GetConnectionResponse":
        return dc_td.GetConnectionResponse.make_one(res)

    def post_to_connection(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)


apigatewaymanagementapi_caster = APIGATEWAYMANAGEMENTAPICaster()
