#
# This file is part of Python Client Library for the Harmonize Datasources.
# Copyright (C) 2022 INPE.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/gpl-3.0.html>.
#
"""Python Client Library for the Harmonize DataSources."""
import importlib.resources as resources
import re
from typing import Any, Dict, Optional, Tuple, Union

import httpx
import jinja2
from jsonschema import RefResolver, validate

templateLoader = jinja2.FileSystemLoader(
    searchpath=str(resources.files(__package__) / "templates")
)
templateEnv = jinja2.Environment(loader=templateLoader)


class Utils:
    """Utilities class for interacting with Harmonize DS."""

    @staticmethod
    def _get(
        url: str,
        access_token: Optional[str] = None,
        params: Optional[Dict[str, Any]] = None,
    ) -> Union[Dict[str, Any], Tuple[str, bytes]]:
        """
        Perform an HTTP GET request and return the result as a JSON document or file content.

        :param url: The URL to query; must be a valid LCCS-WS endpoint.
        :param access_token: (Optional) Access token for authentication.
        :param params: (Optional) Query parameters as a dictionary.
        :return: JSON response as a dictionary or a tuple with file name and binary content.
        :raises ValueError: If the response body does not contain valid JSON or is not of an expected content type.
        """
        headers = {"x-api-key": access_token} if access_token else {}

        with httpx.Client(timeout=100.0) as client:
            response = client.get(url, params=params, headers=headers)
            response.raise_for_status()

            content_type = response.headers.get("content-type", "")

            if content_type == "application/octet-stream":
                content_disposition = response.headers.get("content-disposition", "")
                try:
                    file_name = re.findall(r'filename="?(.*?)"?$', content_disposition)[
                        0
                    ]
                except IndexError as exc:
                    raise ValueError(
                        "Error extracting file name from Content-Disposition header."
                    )
                return file_name, response.content

            if content_type not in (
                "application/json",
                "application/geo+json",
                "application/xml",
                "text/xml; charset=utf-8",
                "application/json;charset=UTF-8",
            ):
                raise ValueError(
                    f"HTTP response is not JSON or XML: Content-Type: {content_type}"
                )

        return response.text

    @staticmethod
    def _post(
        url: str,
        access_token: Optional[str] = None,
        data: Optional[Dict[str, Any]] = None,
        json: Optional[Dict[str, Any]] = None,
        files: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """
        Perform an HTTP POST request.

        :param url: The URL to query.
        :param access_token: (Optional) Access token for authentication.
        :param data: (Optional) Data to send in the body of the request.
        :param json: (Optional) JSON to send in the body of the request.
        :param files: (Optional) Files to send in the body of the request.
        :return: JSON response as a dictionary.
        """
        headers = {"x-api-key": access_token} if access_token else {}

        with httpx.Client(timeout=100.0) as client:
            response = client.post(
                url, headers=headers, data=data, json=json, files=files
            )
            response.raise_for_status()

        return response.json()

    @staticmethod
    def _put(
        url: str,
        access_token: Optional[str] = None,
        data: Optional[Dict[str, Any]] = None,
        json: Optional[Dict[str, Any]] = None,
        files: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """
        Perform an HTTP PUT request.

        :param url: The URL to query.
        :param access_token: (Optional) Access token for authentication.
        :param data: (Optional) Data to send in the body of the request.
        :param json: (Optional) JSON to send in the body of the request.
        :param files: (Optional) Files to send in the body of the request.
        :return: JSON response as a dictionary.
        """
        headers = {"x-api-key": access_token} if access_token else {}

        with httpx.Client(timeout=100.0) as client:
            response = client.put(
                url, headers=headers, data=data, json=json, files=files
            )
            response.raise_for_status()

        return response.json()

    @staticmethod
    def _delete(
        url: str,
        access_token: Optional[str] = None,
        params: Optional[Dict[str, Any]] = None,
    ) -> httpx.Response:
        """
        Perform an HTTP DELETE request.

        :param url: The URL to query.
        :param access_token: (Optional) Access token for authentication.
        :param params: (Optional) Query parameters as a dictionary.
        :return: JSON response as a dictionary.
        """
        headers = {"x-api-key": access_token} if access_token else {}

        with httpx.Client(timeout=100.0) as client:
            response = client.delete(url, params=params, headers=headers)
            response.raise_for_status()

        return response

    @staticmethod
    def render_html(template_name, **kwargs):
        """Render Jinja2 HTML template."""
        template = templateEnv.get_template(template_name)
        return template.render(**kwargs)
