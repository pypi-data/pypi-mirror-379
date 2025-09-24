"""Input Data Manager implementation.

Provides classes and functions for managing input data with geospatial
metadata, projection handling, and validation.
"""

import os
from dataclasses import dataclass, field
from typing import Any, Dict, Optional, Tuple, Union

import geopandas as gpd
import numpy as np
import rasterio
from rasterio.crs import CRS
from rasterio.warp import calculate_default_transform, reproject


@dataclass
class InputDataManager:
    """Manages input data for Laflammscape simulations.

    Features:
    - Geospatial metadata
    - Projection handling
    - Input validation
    - Data preprocessing
    """

    data: Dict[str, np.ndarray] = field(default_factory=dict)
    metadata: Dict[str, Dict[str, Any]] = field(default_factory=dict)
    target_crs: Optional[CRS] = None
    target_resolution: Optional[Tuple[float, float]] = None

    def load_raster(self, name: str, path: str, reproject_to_target: bool = True) -> None:
        """Load raster data from file.

        Args:
            name: Name to assign to the loaded data
            path: Path to raster file
            reproject_to_target: Whether to reproject to target CRS if set

        Raises:
            FileNotFoundError: If the raster file does not exist
            RasterioError: If there's an issue with the raster file
        """
        if not os.path.exists(path):
            raise FileNotFoundError(f"Raster file not found: {path}")

        with rasterio.open(path) as src:
            # Get metadata
            raster_meta = {
                "driver": src.driver,
                "width": src.width,
                "height": src.height,
                "count": src.count,
                "dtype": src.dtypes[0],
                "transform": src.transform.to_gdal(),
                "crs": str(src.crs),
                "bounds": src.bounds,
                "nodata": src.nodata,
                "original_path": path,
            }

            # Handle reprojection if needed
            if reproject_to_target and self.target_crs is not None and src.crs != self.target_crs:
                # Calculate transform for reprojection
                dst_transform, dst_width, dst_height = calculate_default_transform(
                    src.crs,
                    self.target_crs,
                    src.width,
                    src.height,
                    *src.bounds,
                    resolution=self.target_resolution,
                )

                # Update metadata with reprojected info
                raster_meta.update(
                    {
                        "reprojected": True,
                        "original_crs": str(src.crs),
                        "width": dst_width,
                        "height": dst_height,
                        "transform": dst_transform.to_gdal(),
                        "crs": str(self.target_crs),
                    }
                )

                # Create destination array
                dst_array = np.zeros((dst_height, dst_width), dtype=raster_meta["dtype"])

                # Reproject
                reproject(
                    source=rasterio.band(src, 1),
                    destination=dst_array,
                    src_transform=src.transform,
                    src_crs=src.crs,
                    dst_transform=dst_transform,
                    dst_crs=self.target_crs,
                    resampling=rasterio.warp.Resampling.nearest,
                )

                # Store reprojected data
                self.data[name] = dst_array
            else:
                # Store original data
                self.data[name] = src.read(1)

            # Store metadata
            self.metadata[name] = raster_meta

    def load_vector(
        self,
        name: str,
        path: str,
        rasterize: bool = False,
        grid_shape: Optional[Tuple[int, int]] = None,
        transform: Optional[Tuple] = None,
    ) -> None:
        """Load vector data from file.

        Args:
            name: Name to assign to the loaded data
            path: Path to vector file
            rasterize: Whether to rasterize the vector data
            grid_shape: Shape of grid for rasterization (required if rasterize=True)
            transform: Transform for rasterization (required if rasterize=True)

        Raises:
            FileNotFoundError: If the vector file does not exist
            ValueError: If rasterize=True but grid_shape or transform not provided
        """
        if not os.path.exists(path):
            raise FileNotFoundError(f"Vector file not found: {path}")

        # Load vector data with geopandas
        gdf = gpd.read_file(path)

        # Store metadata
        vector_meta = {
            "crs": str(gdf.crs),
            "geometry_type": gdf.geometry.geom_type.mode().iloc[0],
            "count": len(gdf),
            "columns": list(gdf.columns),
            "bounds": gdf.total_bounds.tolist(),
            "original_path": path,
        }

        # Handle reprojection if needed
        if self.target_crs is not None and gdf.crs != self.target_crs:
            gdf = gdf.to_crs(self.target_crs)
            vector_meta.update(
                {
                    "reprojected": True,
                    "original_crs": str(gdf.crs),
                    "crs": str(self.target_crs),
                    "bounds": gdf.total_bounds.tolist(),
                }
            )

        # Handle rasterization if requested
        if rasterize:
            if grid_shape is None or transform is None:
                raise ValueError("Grid shape and transform required for rasterization")

            from rasterio.features import rasterize

            # Create a list of geometry, value pairs
            shapes = [(geom, 1) for geom in gdf.geometry]

            # Rasterize
            raster = rasterize(
                shapes=shapes,
                out_shape=grid_shape,
                transform=transform,
                fill=0,
                dtype=np.uint8,
            )

            # Store rasterized data
            self.data[name] = raster
            vector_meta["rasterized"] = True
        else:
            # Store the GeoDataFrame as a serialized GeoJSON in the data dictionary
            self.data[name] = gdf

        # Store metadata
        self.metadata[name] = vector_meta

    def set_target_crs(
        self,
        crs: Union[str, CRS],
        resolution: Optional[Tuple[float, float]] = None,
    ) -> None:
        """Set target CRS for reprojection.

        Args:
            crs: Target coordinate reference system
            resolution: Target resolution (x_res, y_res) in target CRS units
        """
        if isinstance(crs, str):
            self.target_crs = CRS.from_string(crs)
        else:
            self.target_crs = crs

        self.target_resolution = resolution

    def get_data(self, name: str) -> np.ndarray:
        """Get input data by name.

        Args:
            name: Name of the data to retrieve

        Returns:
            The requested data array

        Raises:
            KeyError: If the requested data doesn't exist
        """
        if name not in self.data:
            raise KeyError(f"Data '{name}' not found")
        return self.data[name]

    def get_metadata(self, name: str) -> Dict[str, Any]:
        """Get metadata for input data by name.

        Args:
            name: Name of the data to retrieve metadata for

        Returns:
            Metadata dictionary for the requested data

        Raises:
            KeyError: If the requested data doesn't exist
        """
        if name not in self.metadata:
            raise KeyError(f"Metadata for '{name}' not found")
        return self.metadata[name]

    def get_extent(self, name: str) -> Tuple[float, float, float, float]:
        """Get spatial extent for input data by name.

        Args:
            name: Name of the data to retrieve extent for

        Returns:
            Tuple of (xmin, ymin, xmax, ymax)

        Raises:
            KeyError: If the requested data doesn't exist
        """
        if name not in self.metadata:
            raise KeyError(f"Metadata for '{name}' not found")

        meta = self.metadata[name]

        # Check if bounds are already stored in metadata
        if "bounds" in meta:
            bounds = meta["bounds"]
            if isinstance(bounds, rasterio.coords.BoundingBox):
                return (bounds.left, bounds.bottom, bounds.right, bounds.top)
            return tuple(bounds)

        # Calculate bounds from transform and shape if not stored
        if "transform" in meta and "width" in meta and "height" in meta:
            from rasterio.transform import Affine

            transform = (
                Affine.from_gdal(*meta["transform"])
                if isinstance(meta["transform"], (list, tuple))
                else meta["transform"]
            )
            width = meta["width"]
            height = meta["height"]

            # Calculate bounds
            left = transform[2]
            top = transform[5]
            right = left + width * transform[0]
            bottom = top + height * transform[4]

            return (left, bottom, right, top)

        raise ValueError(f"Cannot determine extent for '{name}', missing bounds or transform")

    def export_to_raster(self, name: str, output_path: str) -> None:
        """Export data to a raster file.

        Args:
            name: Name of the data to export
            output_path: Path to write the raster file

        Raises:
            KeyError: If the data doesn't exist
            ValueError: If metadata is insufficient for raster export
        """
        if name not in self.data:
            raise KeyError(f"Data '{name}' not found")

        if name not in self.metadata:
            raise KeyError(f"Metadata for '{name}' not found")

        data = self.data[name]
        meta = self.metadata[name]

        # Extract required metadata for raster export
        if "transform" not in meta or "crs" not in meta:
            raise ValueError(f"Insufficient metadata for raster export: {name}")

        # Prepare rasterio metadata
        rasterio_meta = {
            "driver": meta.get("driver", "GTi"),
            "height": data.shape[0],
            "width": data.shape[1],
            "count": 1,
            "dtype": str(data.dtype),
            "crs": meta["crs"],
            "transform": (
                rasterio.transform.Affine.from_gdal(*meta["transform"])
                if isinstance(meta["transform"], (list, tuple))
                else meta["transform"]
            ),
            "nodata": meta.get("nodata", None),
        }

        # Write raster
        with rasterio.open(output_path, "w", **rasterio_meta) as dst:
            dst.write(data, 1)
