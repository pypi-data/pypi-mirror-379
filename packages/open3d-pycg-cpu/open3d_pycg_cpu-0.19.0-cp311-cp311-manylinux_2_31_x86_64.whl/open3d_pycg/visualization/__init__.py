# ----------------------------------------------------------------------------
# -                        Open3D: www.open3d_pycg.org                            -
# ----------------------------------------------------------------------------
# Copyright (c) 2018-2024 www.open3d_pycg.org
# SPDX-License-Identifier: MIT
# ----------------------------------------------------------------------------

import open3d_pycg
if open3d_pycg.__DEVICE_API__ == "cuda":
    if open3d_pycg._build_config["BUILD_GUI"]:
        from open3d_pycg.cuda.pybind.visualization import gui
    from open3d_pycg.cuda.pybind.visualization import *
else:
    if open3d_pycg._build_config["BUILD_GUI"]:
        from open3d_pycg.cpu.pybind.visualization import gui
    from open3d_pycg.cpu.pybind.visualization import *






if open3d_pycg._build_config["BUILD_GUI"]:
    from .draw import draw
