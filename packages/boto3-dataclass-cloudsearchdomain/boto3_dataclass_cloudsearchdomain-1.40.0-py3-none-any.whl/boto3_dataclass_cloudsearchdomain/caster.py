# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_cloudsearchdomain import type_defs as bs_td


class CLOUDSEARCHDOMAINCaster:

    def search(
        self,
        res: "bs_td.SearchResponseTypeDef",
    ) -> "dc_td.SearchResponse":
        return dc_td.SearchResponse.make_one(res)

    def suggest(
        self,
        res: "bs_td.SuggestResponseTypeDef",
    ) -> "dc_td.SuggestResponse":
        return dc_td.SuggestResponse.make_one(res)

    def upload_documents(
        self,
        res: "bs_td.UploadDocumentsResponseTypeDef",
    ) -> "dc_td.UploadDocumentsResponse":
        return dc_td.UploadDocumentsResponse.make_one(res)


cloudsearchdomain_caster = CLOUDSEARCHDOMAINCaster()
