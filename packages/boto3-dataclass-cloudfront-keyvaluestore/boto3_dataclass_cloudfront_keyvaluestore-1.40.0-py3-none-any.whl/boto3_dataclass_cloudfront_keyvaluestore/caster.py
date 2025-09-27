# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_cloudfront_keyvaluestore import type_defs as bs_td


class CLOUDFRONT_KEYVALUESTORECaster:

    def delete_key(
        self,
        res: "bs_td.DeleteKeyResponseTypeDef",
    ) -> "dc_td.DeleteKeyResponse":
        return dc_td.DeleteKeyResponse.make_one(res)

    def describe_key_value_store(
        self,
        res: "bs_td.DescribeKeyValueStoreResponseTypeDef",
    ) -> "dc_td.DescribeKeyValueStoreResponse":
        return dc_td.DescribeKeyValueStoreResponse.make_one(res)

    def get_key(
        self,
        res: "bs_td.GetKeyResponseTypeDef",
    ) -> "dc_td.GetKeyResponse":
        return dc_td.GetKeyResponse.make_one(res)

    def list_keys(
        self,
        res: "bs_td.ListKeysResponseTypeDef",
    ) -> "dc_td.ListKeysResponse":
        return dc_td.ListKeysResponse.make_one(res)

    def put_key(
        self,
        res: "bs_td.PutKeyResponseTypeDef",
    ) -> "dc_td.PutKeyResponse":
        return dc_td.PutKeyResponse.make_one(res)

    def update_keys(
        self,
        res: "bs_td.UpdateKeysResponseTypeDef",
    ) -> "dc_td.UpdateKeysResponse":
        return dc_td.UpdateKeysResponse.make_one(res)


cloudfront_keyvaluestore_caster = CLOUDFRONT_KEYVALUESTORECaster()
