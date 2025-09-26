#!/usr/bin/env python3
# -*- coding:utf-8 -*-
################################################################
# Copyright 2025 Dong Zhaorui. All rights reserved.
# Author: Dong Zhaorui 847235539@qq.com
# Date  : 2025-09-14
################################################################

import numpy as np

from ..robot_base import HexRobotServerBase
from .gello_robot import HexGelloRobot

NET_CONFIG = {
    "ip": "127.0.0.1",
    "port": 12345,
    "client_timeout_ms": 200,
    "server_timeout_ms": 1_000,
    "server_num_workers": 4,
}

ROBOT_CONFIG = {
    "idxs": [0, 1, 2, 3, 4, 5, 6],
    "invs": [1.0, -1.0, 1.0, 1.0, -1.0, 1.0, -4.0],
    "limits": [[[-2.7, 2.7], [-1.57, 2.09], [0, 3.14], [-1.57, 1.57],
                [-1.57, 1.57], [-1.57, 1.57], [0.0, 1.0]]],
    "device":
    "/dev/ttyUSB0",
    "baudrate":
    115200,
    "max_retries":
    3,
    "torque_enabled":
    False,
    "sens_ts":
    True,
}


class HexGelloRobotServer(HexRobotServerBase):

    def __init__(
        self,
        net_config: dict = NET_CONFIG,
        params_config: dict = ROBOT_CONFIG,
    ):
        HexRobotServerBase.__init__(self, net_config)

        # robot
        self._device = HexGelloRobot(params_config)

    def _process_request(self, recv_hdr: dict, recv_buf: np.ndarray):
        if recv_hdr["cmd"] == "is_working":
            return self.no_ts_hdr(recv_hdr, self._device.is_working()), None
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
        else:
            raise ValueError(f"unknown command: {recv_hdr['cmd']}")
