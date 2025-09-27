# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_ec2_instance_connect import type_defs as bs_td


class EC2_INSTANCE_CONNECTCaster:

    def send_ssh_public_key(
        self,
        res: "bs_td.SendSSHPublicKeyResponseTypeDef",
    ) -> "dc_td.SendSSHPublicKeyResponse":
        return dc_td.SendSSHPublicKeyResponse.make_one(res)

    def send_serial_console_ssh_public_key(
        self,
        res: "bs_td.SendSerialConsoleSSHPublicKeyResponseTypeDef",
    ) -> "dc_td.SendSerialConsoleSSHPublicKeyResponse":
        return dc_td.SendSerialConsoleSSHPublicKeyResponse.make_one(res)


ec2_instance_connect_caster = EC2_INSTANCE_CONNECTCaster()
