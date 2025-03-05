# Copyright 2025 DeepMind Technologies Limited
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""Defines HAL robot constants."""

from etils import epath

from mujoco_playground._src import mjx_env

ROOT_PATH = mjx_env.ROOT_PATH / "locomotion" / "hal"
FULL_FLAT_TERRAIN_XML = ROOT_PATH / "xmls" / "HAL.xml"


def task_to_xml(task_name: str) -> epath.Path:
  return {
      "flat_terrain": FULL_FLAT_TERRAIN_XML,
  }[task_name]


FEET_SITES = [
    "fshin",
    "bshin",
]

FEET_GEOMS = [
    "fshin",
    "bshin",
]

ROOT_BODY = "torso"


