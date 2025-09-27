# SPDX-FileCopyrightText: Copyright (c) 2025 The Newton Developers
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# ==================================================================================
# core
# ==================================================================================
from ._src.core import (
    Axis,
    AxisType,
)
from ._version import __version__

__all__ = [
    "Axis",
    "AxisType",
    "__version__",
]

# ==================================================================================
# geometry
# ==================================================================================
from ._src.geometry import (
    SDF,
    GeoType,
    Mesh,
    ParticleFlags,
    ShapeFlags,
)

__all__ += [
    "SDF",
    "GeoType",
    "Mesh",
    "ParticleFlags",
    "ShapeFlags",
]

# ==================================================================================
# sim
# ==================================================================================
from ._src.sim import (  # noqa: E402
    CollisionPipeline,
    Contacts,
    Control,
    EqType,
    JointMode,
    JointType,
    Model,
    ModelBuilder,
    State,
    count_rigid_contact_points,
    eval_fk,
    eval_ik,
    get_joint_dof_count,
)

__all__ += [
    "CollisionPipeline",
    "Contacts",
    "Control",
    "EqType",
    "JointMode",
    "JointType",
    "Model",
    "ModelBuilder",
    "State",
    "count_rigid_contact_points",
    "eval_fk",
    "eval_ik",
    "get_joint_dof_count",
]

# ==================================================================================
# Style3D helpers
# TODO: eliminate these and roll the functionality into Model and ModelBuilder?
# ==================================================================================
from ._src.sim.style3d import Style3DModel, Style3DModelBuilder  # noqa: E402

__all__ += [
    "Style3DModel",
    "Style3DModelBuilder",
]

# ==================================================================================
# submodule APIs
# ==================================================================================
from . import geometry, ik, selection, sensors, solvers, utils, viewer  # noqa: E402

__all__ += [
    "geometry",
    "ik",
    "selection",
    "sensors",
    "solvers",
    "utils",
    "viewer",
]
