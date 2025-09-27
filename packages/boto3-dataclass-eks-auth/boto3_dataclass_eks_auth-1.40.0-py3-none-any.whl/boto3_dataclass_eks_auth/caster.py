# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_eks_auth import type_defs as bs_td


class EKS_AUTHCaster:

    def assume_role_for_pod_identity(
        self,
        res: "bs_td.AssumeRoleForPodIdentityResponseTypeDef",
    ) -> "dc_td.AssumeRoleForPodIdentityResponse":
        return dc_td.AssumeRoleForPodIdentityResponse.make_one(res)


eks_auth_caster = EKS_AUTHCaster()
