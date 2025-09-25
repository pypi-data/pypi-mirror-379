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
"""Python Client Library for Harmonize Datasources."""
from typing import Any, Dict, Iterable, List, Optional

import geopandas as gpd
import pandas as pd

from harmonize_ds.manager.datasource_manager import DataSourceManager
from harmonize_ds.sources.base import Source
from harmonize_ds.utils import Utils


class CollectionsView(list):
    """Wrapper for collections with custom repr for Jupyter."""

    def __repr__(self):
        """Represents a text."""
        return f"CollectionsView({list.__repr__(self)})"

    def _repr_html_(self):
        """Represents (Jupyter/IPython)."""
        return Utils.render_html("harmonize_ds.html", collections=self)


class CollectionClient:
    """Represents a specific collection within a data source."""

    def __init__(self, datasource: Source, collection_id: str):
        """Collectionclient init."""
        self._datasource = datasource
        self._collection_id = collection_id
        self._metadata = self._datasource.describe(self._collection_id)

    def describe(self) -> Dict[str, str]:
        """Return the metadata."""
        return self._metadata

    @property
    def title(self) -> Optional[str]:
        """Collection Title."""
        return self._metadata.get("title")

    @property
    def abstract(self) -> Optional[str]:
        """Collection Abstract."""
        return self._metadata.get("abstract")

    def get(
        self,
        filter: Optional[Dict[str, Any]] = None,
        srid: int = 4326,
    ) -> Any:
        """Gets the data from the collection, delegating to the source."""
        return self._datasource.get(self._collection_id, filter=filter, srid=srid)

    def __repr__(self) -> str:
        """Collection representation."""
        return f"<CollectionClient title={self.title}, source_id={self._datasource._source_id }, collection_id={self._collection_id}>"

    def _repr_html_(self):
        """Render collection metadata as HTML in Jupyter Notebook."""
        html = Utils.render_html("metadata.html", metadata=self._metadata)
        return html


class HARMONIZEDS:
    """Harmonize Datasources Class."""

    manager = DataSourceManager()

    @classmethod
    def _list_collections(cls) -> List[str]:
        """Retorn a list of all collections."""
        collections = []
        for datasource in cls.manager.get_datasources():
            collections.extend(datasource.collections)
        return collections

    @classmethod
    def collections(cls) -> CollectionsView:
        """Return collections wrapped in CollectionsView."""
        return CollectionsView(cls._list_collections())

    @classmethod
    def get_collection(cls, id: str, collection_id: str) -> CollectionClient:
        """Return a CollectionClient."""
        datasource = cls.manager.get_datasource_by_id(id)
        if datasource is None:
            raise ValueError(f"Fonte de dados com ID '{id}' não encontrada.")

        return CollectionClient(datasource, collection_id)

    @classmethod
    def describe(cls, id: str, collection_id: str) -> dict:
        """Describe a specific collection."""
        datasource = cls.manager.get_datasource_by_id(id)
        if datasource is None:
            raise ValueError(f"Fonte de dados com ID '{id}' não encontrada.")

        return datasource.describe(collection_id)

    @staticmethod
    def save_feature(
        filename: str,
        gdf: gpd.geodataframe.GeoDataFrame,
        driver: str = "ESRI Shapefile",
    ):
        """Save dataset data to file.

        Args:
            filename (str): The path or filename.
            gdf (geodataframe): geodataframe to save.
            driver (str): Drive (type) of output file.
        """
        gdf.to_file(filename, encoding="utf-8", driver=driver)

    def _repr_html_(self):
        """Display the HarmonizeDS object as HTML."""
        cl_list = self._list_collections()

        cl_list_dict = [{"id": cl.id, "collection": cl.collection} for cl in cl_list]

        html = Utils.render_html("harmonize_ds.html", collections=cl_list_dict)
        return html
