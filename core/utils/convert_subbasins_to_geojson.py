from pathlib import Path
import sys
import geopandas as gpd


def main() -> None:
    if len(sys.argv) < 2:
        raise SystemExit(
            "Usage: python convert_subbasins_to_geojson.py <basin_id>"
        )

    basin_id = sys.argv[1]

    # 👇 this is the key fix
    ROOT_DIR = Path(__file__).resolve().parents[2]

    basin_dir = ROOT_DIR / "resources" / "txpwc" / "basins" / basin_id / "spatial"
    shp_path = basin_dir / "subbasins.shp"
    geojson_path = basin_dir / "subbasins.geojson"

    print(f"Converting subbasins for basin: {basin_id}")
    print(f"Looking for: {shp_path}")

    if not shp_path.exists():
        raise FileNotFoundError(f"Shapefile not found: {shp_path}")

    gdf = gpd.read_file(shp_path)

    if gdf.crs is None:
        raise ValueError("The shapefile has no CRS defined.")

    gdf = gdf.to_crs(epsg=4326)
    
    # Keep only lightweight attributes needed for mapping/interactions
    KEEP_COLUMNS = ["Subbasin", "Elev", "Area"]
    gdf = gdf[KEEP_COLUMNS + ["geometry"]]

    # Simplify geometry to reduce GeoJSON size for web rendering/click interaction.
    # Increase tolerance for lighter/faster maps, decrease it to preserve boundaries more closely.
    gdf["geometry"] = gdf["geometry"].simplify(tolerance=0.001, preserve_topology=True)



    gdf.to_file(geojson_path, driver="GeoJSON")

    print(f"Saved GeoJSON to: {geojson_path}")
    print("Columns:", list(gdf.columns))


if __name__ == "__main__":
    main()