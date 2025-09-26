#!/usr/bin/env python3
# -*- coding:utf-8 -*-
################################################################
# Copyright 2025 Dong Zhaorui. All rights reserved.
# Author: Dong Zhaorui 847235539@qq.com
# Date  : 2025-09-12
################################################################

import numpy as np

from ..cam_base import HexCamServerBase
from .dummy_cam import HexDummyCam

NET_CONFIG = {
    "ip": "127.0.0.1",
    "port": 12345,
    "client_timeout_ms": 200,
    "server_timeout_ms": 1_000,
    "server_num_workers": 4,
}


class HexDummyCamServer(HexCamServerBase):

    def __init__(
        self,
        net_config: dict = NET_CONFIG,
        params_config: dict = {},
    ):
        HexCamServerBase.__init__(self, net_config)

        # camera
        self._device = HexDummyCam(params_config)

    def _process_request(self, recv_hdr: dict, recv_buf: np.ndarray):
        if recv_hdr["cmd"] == "is_working":
            return self.no_ts_hdr(recv_hdr, self._device.is_working()), None
        elif recv_hdr["cmd"] == "get_rgb":
            return self._get_frame(recv_hdr, False)
        elif recv_hdr["cmd"] == "get_depth":
            return self._get_frame(recv_hdr, True)
        else:
            raise ValueError(f"unknown command: {recv_hdr['cmd']}")
