import pandas as pd
import numpy as np
from scipy.interpolate import RectBivariateSpline
from pathlib import Path


class GVLookup:
    def __init__(self, path: str = None):
        """Initialize with CSV file containing GV lookup table."""

        if path is None:
            this_file_dir = Path(__file__).parent
            csv_path = this_file_dir / "assets" / "RC_2020.csv"
        else:
            csv_path = Path(path)
        self.df = pd.read_csv(csv_path, index_col=0)
        self.lats = self.df.index.astype(float).values
        self.lons = self.df.columns.astype(float).values
        self.values = self.df.values.astype(float)

        # Note: RectBivariateSpline requires strictly increasing coordinates
        self.interpolator = RectBivariateSpline(
            self.lats[::-1],  # Reverse for ascending order
            self.lons,
            self.values[::-1],  # Reverse to match lats
            s=0,
        )

    def get_gv(self, lat, lon):
        """
        Get GV value for given lat/lon coordinates.

        Args:
            lat: Latitude (-90 to 90)
            lon: Longitude (-180 to 180)

        Returns:
            Interpolated GV value
        """
        lat = np.clip(lat, -90, 90)
        lon = np.clip(lon, -180, 180)

        return round(float(self.interpolator(lat, lon)[0, 0]), 2)
