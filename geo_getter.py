#!/usr/bin/env python3
# Anmol Kapoor
# SBHacks VII - Memory's Videos

from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
from pprint import pprint

def get_exif(filename):
    labeled = {}
    image = Image.open(filename)
    image.verify()
    for (key, val) in image._getexif().items():
        labeled[TAGS.get(key)] = val
    return image._getexif(), labeled

def get_geotagging(exif):
    if not exif:
        raise ValueError("No EXIF metadata found")

    geotagging = {}
    for (idx, tag) in TAGS.items():
        if tag == "GPSInfo":
            if idx not in exif:
                raise ValueError("No EXIF geotagging found")
            for (key, val) in GPSTAGS.items():
                if key in exif[idx]:
                    geotagging[val] = exif[idx][key]

    return geotagging

def get_decimal_from_dms(dms, ref):
    degrees = dms[0][0] / dms[0][1]
    minutes = dms[1][0] / dms[1][1] / 60.0
    seconds = dms[2][0] / dms[2][1] / 3600.0

    if ref in ['S', 'W']:
        degrees, minutes, seconds = -degrees, -minutes, -seconds

    return round(degrees + minutes + seconds, 5)

def get_coordinates(geotag_data):
    lati = get_decimal_from_dms(geotag_data["GPSLatitude"], geotag_data["GPSLatitudeRef"])
    long = get_decimal_from_dms(geotag_data["GPSLongitude"], geotag_data["GPSLongitudeRef"])
    return (lati, long)

def get_thumbnail(filename):
    img = Image.open(filename)

    (width, height) = img.size
    if width > height:
        ratio = 50.0 / width
    else:
        ratio = 50.0 / height

    img.thumbnail((round(width * ratio), rount(height * ratio), Image.LANCZOS))
    return img

exif_data, labeled_exif_data = get_exif("test_files/File_006.jpeg")
print("GPS Info:")
pprint(labeled_exif_data["GPSInfo"])
print("\n\n")
geotags = get_geotagging(exif_data)
print("Geographical Tagging: ")
pprint(geotags)
coordinates = get_coordinates(geotags)
print("\n\nCoordinates for Image:", coordinates)
