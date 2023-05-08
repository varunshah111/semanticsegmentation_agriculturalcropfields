#%%
'''
import numpy as np
from shapely.geometry import Polygon, Point, box
import geopandas as gpd
import os
import rasterio
from geopandas import GeoDataFrame



def Random_Points_In_Polygon(poly, num_points):
    min_x, min_y, max_x, max_y = poly.bounds.values[0]
    points = []
    while len(points) < num_points:
        random_point = Point(
            [np.random.uniform(min_x, max_x), np.random.uniform(min_y, max_y)]
        )
        if any(random_point.within(poly.geometry)):
            points.append(random_point)

    return points


# create square polygons around each point
def create_square(point, size):
    x, y = point.x, point.y
    square = Polygon(
        [
            (x - size * 0.5, y - size * 0.5),
            (x + size * 0.5, y - size * 0.5),
            (x + size * 0.5, y + size * 0.5),
            (x - size * 0.5, y + size * 0.5),
        ]
    )
    return square


# apply create_square function to each point and create geoDataFrame with crs of polygon
def create_square_gdf(points, size, polygon):
    squares = [create_square(point, size) for point in points]
    squares_gdf = gpd.GeoDataFrame(squares, columns=["geometry"])
    squares_gdf.crs = polygon.crs
    return squares_gdf


# try reading shapfile using geopandas except read file with rasterio from input file path, then get bounds and create polygon from bounds
def read_a_file(geo_path):
    try:
        polygon = gpd.read_file(geo_path)
    except:
        with rasterio.open(geo_path) as src:
            bounds = src.bounds
            geom = box(*bounds)
            polygon = gpd.GeoDataFrame(geometry=[geom], crs=src.crs.to_string())
    return polygon


# iterate through features of squares_gdf and write each feature to a new geojson file
def write_to_geojson(squares_gdf, geo_path, name_postfix):
    for i, row in squares_gdf.iterrows():
        square = squares_gdf.loc[[i]]
        filename = os.path.join(
            os.path.dirname(geo_path), f"{i:06d}_grid_{name_postfix}" + ".geojson"
        )
        square.to_file(
            filename,
            driver="GeoJSON",
        )
        square.to_file(
            os.path.join(
                os.path.dirname(geo_path), f"{i:06d}_poly_{name_postfix}" + ".geojson"
            ),
            driver="GeoJSON",
        )


# read in shapefile create random points inside of it and create square polygons around each point of a given size return geodataframe of squares with crs of polygon
def random_box(geo_path, num_points, size, name_postfix, crs="EPSG:3395"):
    """
    Writes a geojson file for random squares of a given size in a given crs
    within polygon or raster bounds in geo_path
    geo_path: path to shapefile or raster
    num_points: number of random boxes to create
    size: size of square in linear unit of crs
    name_postfix: name_postfix of data - appended to filename
    crs: crs of output with linear unit for use in size
    returns: geodataframe of squares with crs of polygon
    """
    polygon = read_a_file(geo_path).to_crs(crs)
    points = Random_Points_In_Polygon(polygon.geometry, num_points)
    squares_gdf = create_square_gdf(points, size, polygon)
    write_to_geojson(squares_gdf, geo_path, name_postfix)
    return squares_gdf

'''
#%%
'''
# create random points within polygon
def Random_Points_In_Polygon(poly, num_points):
    min_x, min_y, max_x, max_y = poly.bounds.values[0]
    points = []
    while len(points) < num_points:
        random_point = Point(
            [np.random.uniform(min_x, max_x), np.random.uniform(min_y, max_y)]
        )
        if any(random_point.within(poly.geometry)):
            points.append(random_point)

    return points


# create square polygons around each point
def create_square(point, size):
    x, y = point.x, point.y
    square = Polygon(
        [
            (x - size * 0.5, y - size * 0.5),
            (x + size * 0.5, y - size * 0.5),
            (x + size * 0.5, y + size * 0.5),
            (x - size * 0.5, y + size * 0.5),
        ]
    )
    return square


# apply create_square function to each point and create geoDataFrame with crs of polygon
def create_square_gdf(points, size, polygon):
    squares = [create_square(point, size) for point in points]
    squares_gdf = gpd.GeoDataFrame(squares, columns=["geometry"])
    squares_gdf.crs = polygon.crs
    return squares_gdf


# try reading shapfile using geopandas except read file with rasterio from input file path, then get bounds and create polygon from bounds
def read_a_file(geo_path):
    try:
        polygon = gpd.read_file(geo_path)
    except:
        with rasterio.open(geo_path) as src:
            bounds = src.bounds
            geom = box(*bounds)
            polygon = gpd.GeoDataFrame(geometry=[geom], crs=src.crs.to_string())
    return polygon


# create a poly and grid geojson file for each input
def write_poly_grid(out_shape, out_dir, name_prefix, name_postfix):
    # write multi-box to geojson
    filename = os.path.join(
        out_dir,
        f"{name_prefix}_grid_{name_postfix}" + ".geojson",
    )
    out_shape.to_file(
        filename,
        driver="GeoJSON",
    )

    # write ploy to geojson
    out_shape.to_file(
        os.path.join(
            out_dir,
            f"{name_prefix}_poly_{name_postfix}" + ".geojson",
        ),
        driver="GeoJSON",
    )


# iterate through features of squares_gdf and write each feature to a new geojson file
def write_to_geojson(squares_gdf, geo_path, out_dir, name_prefix, name_postfix):
    # if name_prefix is variable then write each square to a separate file

    # out path
    if out_dir is None:
        out_dir = os.path.dirname(geo_path)

    # write multi-box to geojson
    if name_prefix is not None:
        write_poly_grid(squares_gdf, out_dir, name_prefix, name_postfix)

    # write each square to a separate file
    else:
        for i, row in squares_gdf.iterrows():
            # get square from squares_gdf
            square = squares_gdf.loc[[i]]

            # use index as name_prefix if name_prefix is None
            name_prefix = f"{i:06d}"

            # write single grids to geojsons
            write_poly_grid(square, out_dir, name_prefix, name_postfix)


# read in shapefile create random points inside of it and create square polygons around each point of a given size return geodataframe of squares with crs of polygon
def random_box(
    geo_path,
    num_points,
    size,
    out_dir=None,
    name_prefix=None,
    name_postfix=None,
    crs="EPSG:3395",
):
    """
    Writes a geojson file for random squares of a given size in a given crs
    within polygon or raster bounds in geo_path
    geo_path: path to shapefile or raster
    num_points: number of random boxes to create
    size: size of square in linear unit of crs
    out_dir: directory to write geojson files
    name_prefix: name_prefix of data - prepended to filename. If is None, assumes each square is a separate file, if not None, writes all squares to a single file
    name_postfix: name_postfix of data - appended to filename
    crs: crs of output with linear unit for use in size
    returns: geodataframe of squares with crs of polygon
    """
    polygon = read_a_file(geo_path).to_crs(crs)
    points = Random_Points_In_Polygon(polygon.geometry, num_points)
    squares_gdf = create_square_gdf(points, size, polygon)
    write_to_geojson(squares_gdf, geo_path, out_dir, name_prefix, name_postfix)
    return squares_gdf

'''
#%%

from randombox import random_box
#%%
import os
os.getcwd()

#%%

'''
OR_PATH = os.getcwd()
os.chdir("/home/ubuntu/randombox/data")

box_dir = os.getcwd()
sep = os.path.sep
os.chdir(OR_PATH)
'''

#%%

OR_PATH = os.getcwd()
os.chdir("/home/ubuntu/Geography/Capstone")

DATA_DIR = os.getcwd() + os.path.sep + 'Data' + os.path.sep
sep = os.path.sep
os.chdir(OR_PATH)

#%%
QUARTERLY = DATA_DIR + 'Quarterly_Chunks' + sep

#%%
shapefiles = DATA_DIR + 'shapefiles' + sep


#%%
image = QUARTERLY + 'S2_SR_2021_Q01-0000016384-0000000000.tif'

#%%
geo_path = image
num_points = 5
size = 1000

#squares_grid = random_box(geo_path, num_points, size, name_postfix="2020", crs="EPSG:3395")
squares_gdf  = random_box(geo_path, num_points, size, name_postfix="2020", crs="EPSG:3395")


#%%
squares_gdf.to_file(shapefiles + "squares3.geojson", driver="GeoJSON")


#%%
'''
num_points = 10
size = 0.1
squares_gdf = random_box(geo_path, num_points, size)
squares_gdf.to_file("folder/squares.geojson", driver="GeoJSON")
'''