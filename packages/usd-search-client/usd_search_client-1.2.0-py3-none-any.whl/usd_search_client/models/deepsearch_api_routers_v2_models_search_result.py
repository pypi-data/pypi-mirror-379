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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from usd_search_client.models.metadata import Metadata
from usd_search_client.models.prediction import Prediction
from usd_search_client.models.prim1 import Prim1
from typing import Optional, Set
from typing_extensions import Self

class DeepsearchApiRoutersV2ModelsSearchResult(BaseModel):
    """
    DeepsearchApiRoutersV2ModelsSearchResult
    """ # noqa: E501
    url: StrictStr = Field(description="URL of the asset")
    score: Union[StrictFloat, StrictInt]
    embed: Optional[StrictStr] = None
    root_prims: Optional[List[Prim1]] = None
    default_prims: Optional[List[Prim1]] = None
    image: Optional[StrictStr] = None
    predictions: Optional[List[Prediction]] = None
    vision_generated_metadata: Optional[Dict[str, Any]] = None
    metadata: Optional[Metadata] = None
    in_scene_instance_prims: Optional[List[Prim1]] = None
    usd_dimensions: Optional[Dict[str, Any]] = None
    __properties: ClassVar[List[str]] = ["url", "score", "embed", "root_prims", "default_prims", "image", "predictions", "vision_generated_metadata", "metadata", "in_scene_instance_prims", "usd_dimensions"]

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
        """Create an instance of DeepsearchApiRoutersV2ModelsSearchResult from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in root_prims (list)
        _items = []
        if self.root_prims:
            for _item_root_prims in self.root_prims:
                if _item_root_prims:
                    _items.append(_item_root_prims.to_dict())
            _dict['root_prims'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in default_prims (list)
        _items = []
        if self.default_prims:
            for _item_default_prims in self.default_prims:
                if _item_default_prims:
                    _items.append(_item_default_prims.to_dict())
            _dict['default_prims'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in predictions (list)
        _items = []
        if self.predictions:
            for _item_predictions in self.predictions:
                if _item_predictions:
                    _items.append(_item_predictions.to_dict())
            _dict['predictions'] = _items
        # override the default output from pydantic by calling `to_dict()` of metadata
        if self.metadata:
            _dict['metadata'] = self.metadata.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in in_scene_instance_prims (list)
        _items = []
        if self.in_scene_instance_prims:
            for _item_in_scene_instance_prims in self.in_scene_instance_prims:
                if _item_in_scene_instance_prims:
                    _items.append(_item_in_scene_instance_prims.to_dict())
            _dict['in_scene_instance_prims'] = _items
        # set to None if embed (nullable) is None
        # and model_fields_set contains the field
        if self.embed is None and "embed" in self.model_fields_set:
            _dict['embed'] = None

        # set to None if root_prims (nullable) is None
        # and model_fields_set contains the field
        if self.root_prims is None and "root_prims" in self.model_fields_set:
            _dict['root_prims'] = None

        # set to None if default_prims (nullable) is None
        # and model_fields_set contains the field
        if self.default_prims is None and "default_prims" in self.model_fields_set:
            _dict['default_prims'] = None

        # set to None if image (nullable) is None
        # and model_fields_set contains the field
        if self.image is None and "image" in self.model_fields_set:
            _dict['image'] = None

        # set to None if predictions (nullable) is None
        # and model_fields_set contains the field
        if self.predictions is None and "predictions" in self.model_fields_set:
            _dict['predictions'] = None

        # set to None if vision_generated_metadata (nullable) is None
        # and model_fields_set contains the field
        if self.vision_generated_metadata is None and "vision_generated_metadata" in self.model_fields_set:
            _dict['vision_generated_metadata'] = None

        # set to None if metadata (nullable) is None
        # and model_fields_set contains the field
        if self.metadata is None and "metadata" in self.model_fields_set:
            _dict['metadata'] = None

        # set to None if in_scene_instance_prims (nullable) is None
        # and model_fields_set contains the field
        if self.in_scene_instance_prims is None and "in_scene_instance_prims" in self.model_fields_set:
            _dict['in_scene_instance_prims'] = None

        # set to None if usd_dimensions (nullable) is None
        # and model_fields_set contains the field
        if self.usd_dimensions is None and "usd_dimensions" in self.model_fields_set:
            _dict['usd_dimensions'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DeepsearchApiRoutersV2ModelsSearchResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "url": obj.get("url"),
            "score": obj.get("score"),
            "embed": obj.get("embed"),
            "root_prims": [Prim1.from_dict(_item) for _item in obj["root_prims"]] if obj.get("root_prims") is not None else None,
            "default_prims": [Prim1.from_dict(_item) for _item in obj["default_prims"]] if obj.get("default_prims") is not None else None,
            "image": obj.get("image"),
            "predictions": [Prediction.from_dict(_item) for _item in obj["predictions"]] if obj.get("predictions") is not None else None,
            "vision_generated_metadata": obj.get("vision_generated_metadata"),
            "metadata": Metadata.from_dict(obj["metadata"]) if obj.get("metadata") is not None else None,
            "in_scene_instance_prims": [Prim1.from_dict(_item) for _item in obj["in_scene_instance_prims"]] if obj.get("in_scene_instance_prims") is not None else None,
            "usd_dimensions": obj.get("usd_dimensions")
        })
        return _obj


