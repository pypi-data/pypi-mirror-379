import glob
import os
import shutil
import unittest

import geopandas as gpd

from geomltoolkits.downloader import osm as OSMDownloader
from geomltoolkits.downloader import tms as TMSDownloader
from geomltoolkits.regularizer import VectorizeMasks


class TestDownloader(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.zoom = 18
        self.work_dir = "banepa_test"
        self.tms = "https://tiles.openaerialmap.org/62d85d11d8499800053796c1/0/62d85d11d8499800053796c2/{z}/{x}/{y}"
        self.bbox = [
            85.51678033745037,
            27.6313353660439,
            85.52323021107895,
            27.637438390948745,
        ]
        os.makedirs(self.work_dir, exist_ok=True)

    async def test_download_tiles_from_tilejson(self):
        """Test downloading tiles using a TileJSON URL."""
        tilejson_url = "https://titiler.hotosm.org/cog/WebMercatorQuad/tilejson.json?url=https://oin-hotosm-temp.s3.us-east-1.amazonaws.com/62d85d11d8499800053796c1/0/62d85d11d8499800053796c2.tif"

        tilejson_test_dir = os.path.join(self.work_dir, "tilejson_test")
        os.makedirs(tilejson_test_dir, exist_ok=True)

        await TMSDownloader.download_tiles(
            tms=tilejson_url,
            zoom=self.zoom,
            out=tilejson_test_dir,
            bbox=self.bbox,
            georeference=True,
            dump_tile_geometries_as_geojson=True,
            prefix="TileJSON",
            is_tilejson=True,  # This flag tells the downloader to treat the URL as TileJSON
        )

        tif_files = glob.glob(os.path.join(tilejson_test_dir, "chips", "*.tif"))
        self.assertEqual(len(tif_files), 36, "Number of .tif files should be 36")

    async def test_download_bing_tiles(self):
        """Test downloading tiles from Bing tile service."""
        bing_tms = "https://ecn.t{s}.tiles.virtualearth.net/tiles/a{q}.jpeg?g=1"

        bing_test_dir = os.path.join(self.work_dir, "bing_test")
        os.makedirs(bing_test_dir, exist_ok=True)

        await TMSDownloader.download_tiles(
            tms=bing_tms,
            zoom=self.zoom,
            out=bing_test_dir,
            bbox=self.bbox,
            georeference=True,
            dump_tile_geometries_as_geojson=True,
            prefix="Bing",
        )

        tif_files = glob.glob(os.path.join(bing_test_dir, "chips", "*.tif"))
        self.assertGreater(
            len(tif_files), 0, "At least one .tif file should be downloaded"
        )

        tiles_geojson = os.path.join(bing_test_dir, "tiles.geojson")
        self.assertTrue(
            os.path.exists(tiles_geojson),
            "tiles.geojson should be created when dump_tile_geometries_as_geojson=True",
        )

        gdf = gpd.read_file(tiles_geojson)
        self.assertEqual(
            len(gdf),
            len(tif_files),
            "Number of features in tiles.geojson should match number of downloaded tiles",
        )

    async def test_download_esri_tiles(self):
        """Test downloading tiles from ESRI tile service."""
        esri_tms = "https://services.arcgisonline.com/arcgis/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}?blankTile=false"

        esri_test_dir = os.path.join(self.work_dir, "esri_test")
        os.makedirs(esri_test_dir, exist_ok=True)

        await TMSDownloader.download_tiles(
            tms=esri_tms,
            zoom=self.zoom,
            out=esri_test_dir,
            bbox=self.bbox,
            georeference=True,
            dump_tile_geometries_as_geojson=True,
            prefix="ESRI",
            tile_scheme="xyz",
        )

        tif_files = glob.glob(os.path.join(esri_test_dir, "chips", "*.tif"))
        self.assertGreater(
            len(tif_files), 0, "At least one .tif file should be downloaded"
        )

        tiles_geojson = os.path.join(esri_test_dir, "tiles.geojson")
        self.assertTrue(
            os.path.exists(tiles_geojson),
            "tiles.geojson should be created when dump_tile_geometries_as_geojson=True",
        )

        gdf = gpd.read_file(tiles_geojson)
        self.assertEqual(
            len(gdf),
            len(tif_files),
            "Number of features in tiles.geojson should match number of downloaded tiles",
        )

    async def test_download_tiles(self):
        # Download tiles
        await TMSDownloader.download_tiles(
            tms=self.tms,
            zoom=self.zoom,
            out=self.work_dir,
            bbox=self.bbox,
            georeference=True,
            dump_tile_geometries_as_geojson=True,
            prefix="OAM",
        )
        tif_files = glob.glob(os.path.join(self.work_dir, "chips", "*.tif"))
        self.assertEqual(len(tif_files), 36, "Number of .tif files should be 36")

    async def test_download_osm_data(self):
        # Download OSM data for tile boundary
        await self.test_download_tiles()

        tiles_geojson = os.path.join(self.work_dir, "tiles.geojson")
        await OSMDownloader.download_osm_data(
            geojson=tiles_geojson,
            out=os.path.join(self.work_dir, "labels"),
            dump_results=True,
        )
        osm_result_path = os.path.join(self.work_dir, "labels", "osm-result.geojson")
        self.assertTrue(
            os.path.isfile(osm_result_path), "OSM result file should be present"
        )


class TestVectorizeMasks(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory for test outputs
        self.test_dir = "test_vectorize_output"
        os.makedirs(self.test_dir, exist_ok=True)
        # Define the input file and output file paths.
        self.input_tif = os.path.join("data", "sample_predictions.tif")
        self.output_geojson = os.path.join(
            self.test_dir, "sample_predictions_test.geojson"
        )

    def tearDown(self):
        # Cleanup the temporary directory after tests
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)

    def test_vectorize_masks_sample(self):
        # Skip test if input file does not exist.
        if not os.path.exists(self.input_tif):
            self.skipTest(f"Input file {self.input_tif} not found.")

        # Create a VectorizeMasks instance with test settings.
        converter = VectorizeMasks(
            simplify_tolerance=0.2,
            min_area=1.0,
            orthogonalize=True,
            algorithm="potrace",
            tmp_dir=os.getcwd(),
        )

        # Run the conversion.
        converter.convert(self.input_tif, self.output_geojson)

        # Verify that the output file was created.
        self.assertTrue(
            os.path.exists(self.output_geojson),
            f"Output file {self.output_geojson} was not created.",
        )

        # Load the output GeoJSON and check it has features.
        gdf_loaded = gpd.read_file(self.output_geojson)
        self.assertGreater(
            len(gdf_loaded), 0, "Generated GeoJSON contains no features."
        )

    def test_vectorize_masks_rasterio(self):
        # Skip test if input file does not exist.
        if not os.path.exists(self.input_tif):
            self.skipTest(f"Input file {self.input_tif} not found.")

        # Create a VectorizeMasks instance with test settings.
        converter = VectorizeMasks(
            simplify_tolerance=0.2,
            min_area=1.0,
            orthogonalize=True,
            algorithm="rasterio",
            tmp_dir=os.getcwd(),
        )

        # Run the conversion.
        converter.convert(self.input_tif, self.output_geojson)

        # Verify that the output file was created.
        self.assertTrue(
            os.path.exists(self.output_geojson),
            f"Output file {self.output_geojson} was not created.",
        )

        # Load the output GeoJSON and check it has features.
        gdf_loaded = gpd.read_file(self.output_geojson)
        self.assertGreater(
            len(gdf_loaded), 0, "Generated GeoJSON contains no features."
        )


if __name__ == "__main__":
    unittest.main()
