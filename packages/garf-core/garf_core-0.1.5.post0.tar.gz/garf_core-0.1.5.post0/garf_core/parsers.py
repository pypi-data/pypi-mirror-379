# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Module for defining various parsing strategy for API response."""

from __future__ import annotations

import abc
import contextlib
import functools
import operator
from collections.abc import Mapping, MutableSequence
from typing import Any

from typing_extensions import override

from garf_core import api_clients, exceptions, query_editor


class BaseParser(abc.ABC):
  """An interface for all parsers to implement."""

  def __init__(
    self, query_specification: query_editor.BaseQueryElements
  ) -> None:
    """Initializes BaseParser."""
    self.query_spec = query_specification

  def parse_response(
    self,
    response: api_clients.GarfApiResponse,
  ) -> list[list[api_clients.ApiRowElement]]:
    """Parses response."""
    if not response.results:
      return [[]]
    results = []
    for result in response.results:
      results.append(self.parse_row(result))
    return results

  @abc.abstractmethod
  def parse_row(self, row):
    """Parses single row from response."""


class ListParser(BaseParser):
  """Returns API results as is."""

  @override
  def parse_row(
    self,
    row: list,
  ) -> list[list[api_clients.ApiRowElement]]:
    return row


class DictParser(BaseParser):
  """Extracts nested dict elements."""

  @override
  def parse_row(
    self,
    row: list,
  ) -> list[list[api_clients.ApiRowElement]]:
    if not isinstance(row, Mapping):
      raise GarfParserError
    result = []
    for field in self.query_spec.fields:
      result.append(self.get_nested_field(row, field))
    return result

  def get_nested_field(self, dictionary: dict[str, Any], key: str):
    """Returns nested fields from a dictionary."""
    if result := dictionary.get(key):
      return result
    key = key.split('.')
    try:
      return functools.reduce(operator.getitem, key, dictionary)
    except (TypeError, KeyError):
      return None


class NumericConverterDictParser(DictParser):
  """Extracts nested dict elements with numerical conversions."""

  def get_nested_field(self, dictionary: dict[str, Any], key: str):
    """Extract nested field with int/float conversion."""

    def convert_field(value):
      for type_ in (int, float):
        with contextlib.suppress(ValueError):
          return type_(value)
      return value

    if result := dictionary.get(key):
      return convert_field(result)

    key = key.split('.')
    try:
      field = functools.reduce(operator.getitem, key, dictionary)
      if isinstance(field, MutableSequence) or field in (True, False):
        return field
      return convert_field(field)
    except KeyError:
      return None


class GarfParserError(exceptions.GarfError):
  """Incorrect data format for parser."""
