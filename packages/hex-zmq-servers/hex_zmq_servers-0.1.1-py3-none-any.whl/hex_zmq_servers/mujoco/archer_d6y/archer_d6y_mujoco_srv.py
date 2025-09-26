#!/usr/bin/env python3
# -*- coding:utf-8 -*-
################################################################
# Copyright 2025 Dong Zhaorui. All rights reserved.
# Author: Dong Zhaorui 847235539@qq.com
# Date  : 2025-09-16
################################################################

import numpy as np

from ..mujoco_base import HexMujocoServerBase
from .archer_d6y_mujoco import HexArcherD6yMujoco

NET_CONFIG = {
    "ip": "127.0.0.1",
    "port": 12345,
    "client_timeout_ms": 200,
    "server_timeout_ms": 1_000,
    "server_num_workers": 4,
}

MUJOCO_CONFIG = {
    "states_rate": 250,
    "img_rate": 30,
    "headless": False,
    "sens_ts": True,
}


class HexArcherD6yMujocoServer(HexMujocoServerBase):

    def __init__(
        self,
        net_config: dict = NET_CONFIG,
        params_config: dict = MUJOCO_CONFIG,
    ):
        HexMujocoServerBase.__init__(self, net_config)

        # mujoco
        self._device = HexArcherD6yMujoco(params_config)

    def _process_request(self, recv_hdr: dict, recv_buf: np.ndarray):
        if recv_hdr["cmd"] == "is_working":
            return self.no_ts_hdr(recv_hdr, self._device.is_working()), None
        elif recv_hdr["cmd"] == "reset":
            return self.no_ts_hdr(recv_hdr, self._device.reset()), None
        elif recv_hdr["cmd"] == "get_dofs":
            dofs = self._device.get_dofs()
            return self.no_ts_hdr(recv_hdr, dofs is not None), dofs
        elif recv_hdr["cmd"] == "get_limits":
            limits = self._device.get_limits()
            return self.no_ts_hdr(recv_hdr, limits is not None), limits
        elif recv_hdr["cmd"] == "get_states":
            return self._get_states(recv_hdr)
        elif recv_hdr["cmd"] == "set_cmds":
            return self._set_cmds(recv_hdr, recv_buf)
        elif recv_hdr["cmd"] == "get_intri":
            intri = self._device.get_intri()
            return self.no_ts_hdr(recv_hdr, intri is not None), intri
        elif recv_hdr["cmd"] == "get_rgb":
            return self._get_frame(recv_hdr, False)
        elif recv_hdr["cmd"] == "get_depth":
            return self._get_frame(recv_hdr, True)
        else:
            raise ValueError(f"unknown command: {recv_hdr['cmd']}")
