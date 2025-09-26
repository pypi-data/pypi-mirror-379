# SPDX-FileCopyrightText: Copyright (c) 2024 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: MIT
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

# coding: utf-8

"""
    USD Search and Asset Graph Search APIs

    # USD Search API Overview **USD Search API** is a collection of cloud-native microservices that enable developers, creators, and workflow specialists to efficiently search through vast collections of OpenUSD data, images, and other assets using natural language or image-based inputs. With these production-ready microservices, developers can deploy USD Search API onto their own infrastructure. With USD Search API’s artificial intelligence (AI) features, you can quickly locate untagged and unstructured 3D data and digital assets, saving time navigating unstructured, untagged 3D data. USD Search API is capable of searching and indexing 3D asset databases, as well as navigating complex 3D scenes to perform spatial searches, without requiring manual tagging of assets. ## Features - **Natural Language Searches:** - Utilize AI to search for images and USD-based 3D models using simple, descriptive language. - **Image Similarity Searches:** - Find images similar to a reference image through AI-driven image comparisons. - **Metadata Filtering:** - Filter search results by file name, file type, creation/modification dates, file size, and creator/modifier metadata. - **USD Content Filtering with Asset Graph Search:** - When used with the Asset Graph Search, search capabilities are expanded to include filtering based on USD properties and object dimensions. - **Multiple Storage Backend Support:** - Compatible with various storage backends, including AWS S3 buckets and Omniverse Nucleus server. - **Advanced File Name, Extension, and Path Filters:** - Use wildcards for broad or specific file name and extension searches. - **Date and Size Range Filtering:** - Specify assets created or modified within certain date ranges or file sizes larger or smaller than a designated threshold. - **User-based Filtering:** - Filter assets based on their creator or modifier, allowing for searches tailored to particular users' contributions. - **Embedding-based Similarity Threshold:** - Set a similarity threshold for more nuanced control over search results in embedding-based searches. - **Custom Search Paths and Scenes:** - Specify search locations within the storage backend or conduct searches within specific scenes for targeted results. - **Return Detailed Results:** - Option to include images, metadata, root prims, and predictions in the search results.  # Asset Graph Search (AGS) API Overview **Asset Graph Search (AGS)** provides advanced querying capabilities for assets and USD trees indexed in a graph database. It supports proximity queries based on coordinates or prims to find objects within specified areas or radii, sorted by distance, and includes transformation options for vector alignment. The API also offers dependency and reverse dependency searches, helping to identify all assets referenced in a scene or scenes containing a particular asset, which can optimize scene loading and track dependency changes. By combining different query types, the AGS API enables complex scenarios for scene understanding, manipulation, and generation. Integrated with USD Search it provides in-scene search functionality. ## Features - **Proximity Queries:** - Find objects within a specified bounding box or radius. - Results sorted by distance with options for vector alignment using a transformation matrix. - **USD Property Queries:** - Enables querying objects in a 3D scene using USD properties, such as finding all assets with a specific semantic label. - **Asset Dependency Searches:** - Identify all assets referenced in a scene — including USD references, material references, or textures. - Reverse search to find all scenes containing a particular asset. - **Combined Query Capabilities:** - Enable complex scenarios for enhanced scene understanding, manipulation, and generation. - **Integration with USD Search:** - Provides in-scene search functionality. 

    The version of the OpenAPI document: 1.2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class Prim(BaseModel):
    """
    Prim
    """ # noqa: E501
    scene_url: StrictStr = Field(description="URL of the Prim's scene")
    scene_mpu: Optional[Union[StrictFloat, StrictInt]] = Field(default=1, description="MPU of the Prim's scene")
    usd_path: StrictStr = Field(description="USD path of the prim withn scene `scene_url`. Unique within a single scene.")
    prim_type: StrictStr = Field(description="Prim type")
    source_asset_url: Optional[StrictStr] = None
    properties: Optional[Dict[str, StrictStr]] = None
    translate: Optional[List[Union[StrictFloat, StrictInt]]] = Field(default=None, description="Translate X, Y, Z world coordinates of the prim")
    rotate_x: Optional[Union[StrictFloat, StrictInt]] = None
    rotate_y: Optional[Union[StrictFloat, StrictInt]] = None
    rotate_z: Optional[Union[StrictFloat, StrictInt]] = None
    scale_x: Optional[Union[StrictFloat, StrictInt]] = None
    scale_y: Optional[Union[StrictFloat, StrictInt]] = None
    scale_z: Optional[Union[StrictFloat, StrictInt]] = None
    bbox_max: List[Union[StrictFloat, StrictInt]] = Field(description="Max X, Y, Z coordinates of the bounding box")
    bbox_min: List[Union[StrictFloat, StrictInt]] = Field(description="Min X, Y, Z coordinates of the bounding box")
    bbox_midpoint: List[Union[StrictFloat, StrictInt]] = Field(description="Midpoint X, Y, Z coordinates of the bounding box, i.e. Prim's location within the scene `scene_url`.")
    root_prim: Optional[StrictBool] = None
    default_prim: Optional[StrictBool] = None
    bbox_dimension_x: Union[StrictFloat, StrictInt] = Field(description="X axis dimension of prim's bounding box")
    bbox_dimension_y: Union[StrictFloat, StrictInt] = Field(description="Y axis dimension of prim's bounding box")
    bbox_dimension_z: Union[StrictFloat, StrictInt] = Field(description="Z axis dimension of prim's bounding box")
    scaled_bbox_dimension_x: Union[StrictFloat, StrictInt] = Field(description="X axis dimension of prim's bounding box scaled by the MPU")
    scaled_bbox_dimension_y: Union[StrictFloat, StrictInt] = Field(description="Y axis dimension of prim's bounding box scaled by the MPU")
    scaled_bbox_dimension_z: Union[StrictFloat, StrictInt] = Field(description="Z axis dimension of prim's bounding box scaled by the MPU")
    __properties: ClassVar[List[str]] = ["scene_url", "scene_mpu", "usd_path", "prim_type", "source_asset_url", "properties", "translate", "rotate_x", "rotate_y", "rotate_z", "scale_x", "scale_y", "scale_z", "bbox_max", "bbox_min", "bbox_midpoint", "root_prim", "default_prim", "bbox_dimension_x", "bbox_dimension_y", "bbox_dimension_z", "scaled_bbox_dimension_x", "scaled_bbox_dimension_y", "scaled_bbox_dimension_z"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of Prim from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "bbox_dimension_x",
            "bbox_dimension_y",
            "bbox_dimension_z",
            "scaled_bbox_dimension_x",
            "scaled_bbox_dimension_y",
            "scaled_bbox_dimension_z",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if source_asset_url (nullable) is None
        # and model_fields_set contains the field
        if self.source_asset_url is None and "source_asset_url" in self.model_fields_set:
            _dict['source_asset_url'] = None

        # set to None if properties (nullable) is None
        # and model_fields_set contains the field
        if self.properties is None and "properties" in self.model_fields_set:
            _dict['properties'] = None

        # set to None if rotate_x (nullable) is None
        # and model_fields_set contains the field
        if self.rotate_x is None and "rotate_x" in self.model_fields_set:
            _dict['rotate_x'] = None

        # set to None if rotate_y (nullable) is None
        # and model_fields_set contains the field
        if self.rotate_y is None and "rotate_y" in self.model_fields_set:
            _dict['rotate_y'] = None

        # set to None if rotate_z (nullable) is None
        # and model_fields_set contains the field
        if self.rotate_z is None and "rotate_z" in self.model_fields_set:
            _dict['rotate_z'] = None

        # set to None if scale_x (nullable) is None
        # and model_fields_set contains the field
        if self.scale_x is None and "scale_x" in self.model_fields_set:
            _dict['scale_x'] = None

        # set to None if scale_y (nullable) is None
        # and model_fields_set contains the field
        if self.scale_y is None and "scale_y" in self.model_fields_set:
            _dict['scale_y'] = None

        # set to None if scale_z (nullable) is None
        # and model_fields_set contains the field
        if self.scale_z is None and "scale_z" in self.model_fields_set:
            _dict['scale_z'] = None

        # set to None if root_prim (nullable) is None
        # and model_fields_set contains the field
        if self.root_prim is None and "root_prim" in self.model_fields_set:
            _dict['root_prim'] = None

        # set to None if default_prim (nullable) is None
        # and model_fields_set contains the field
        if self.default_prim is None and "default_prim" in self.model_fields_set:
            _dict['default_prim'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Prim from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "scene_url": obj.get("scene_url"),
            "scene_mpu": obj.get("scene_mpu") if obj.get("scene_mpu") is not None else 1,
            "usd_path": obj.get("usd_path"),
            "prim_type": obj.get("prim_type"),
            "source_asset_url": obj.get("source_asset_url"),
            "properties": obj.get("properties"),
            "translate": obj.get("translate"),
            "rotate_x": obj.get("rotate_x"),
            "rotate_y": obj.get("rotate_y"),
            "rotate_z": obj.get("rotate_z"),
            "scale_x": obj.get("scale_x"),
            "scale_y": obj.get("scale_y"),
            "scale_z": obj.get("scale_z"),
            "bbox_max": obj.get("bbox_max"),
            "bbox_min": obj.get("bbox_min"),
            "bbox_midpoint": obj.get("bbox_midpoint"),
            "root_prim": obj.get("root_prim"),
            "default_prim": obj.get("default_prim"),
            "bbox_dimension_x": obj.get("bbox_dimension_x"),
            "bbox_dimension_y": obj.get("bbox_dimension_y"),
            "bbox_dimension_z": obj.get("bbox_dimension_z"),
            "scaled_bbox_dimension_x": obj.get("scaled_bbox_dimension_x"),
            "scaled_bbox_dimension_y": obj.get("scaled_bbox_dimension_y"),
            "scaled_bbox_dimension_z": obj.get("scaled_bbox_dimension_z")
        })
        return _obj


