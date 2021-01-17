#!/usr/bin/env python3
# Anmol Kapoor
# SBHacks VII - Memory's Videos

from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
import datetime

MONTHS = "January,February,March,April,May,June,July,August,September,October,November,December".split(",")


class EXIFExtractor:
    def __init__(self, filename):
        self.filename = filename
        self.date_time, self.dt = None, None

    def get_exif(self):
        labeled = {}
        image = Image.open(self.filename)
        image.verify()
        try:
            for (key, val) in image._getexif().items():
                labeled[TAGS.get(key)] = val
        except AttributeError as e:
            print("Error at", self.filename)
            print(e)
            raise ValueError("No Exif Data found for image")
        dt = labeled["DateTimeOriginal"]
        date, time = dt.split(" ")
        self.dt = datetime.datetime.strptime(dt, '%Y:%m:%d %H:%M:%S')
        daytime = "AM"
        hour = int(time.split(":")[0])
        if hour > 12:
            hour -= 12
            morning = "PM"
        time = str(hour) + ":" + ":".join(time.split(":")[1:]) + " " + daytime
        self.date_time = MONTHS[int(date.split(":")[1])-1] + " " + date.split(":")[2] + ", " + date.split(":")[0] + " at " + time
        return image._getexif(), labeled

    def get_geotagging(self, exif):
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

    def get_decimal_from_dms(self, dms, ref):
        degrees = dms[0][0] / dms[0][1]
        minutes = dms[1][0] / dms[1][1] / 60.0
        seconds = dms[2][0] / dms[2][1] / 3600.0

        if ref in ['S', 'W']:
            degrees, minutes, seconds = -degrees, -minutes, -seconds

        return round(degrees + minutes + seconds, 5)

    def get_coordinates(self, geotag_data):
        lati = self.get_decimal_from_dms(geotag_data["GPSLatitude"], geotag_data["GPSLatitudeRef"])
        long = self.get_decimal_from_dms(geotag_data["GPSLongitude"], geotag_data["GPSLongitudeRef"])
        return [lati, long]

    def get_thumbnail(self, save_number):
        img = Image.open(self.filename)

        (width, height) = img.size
        if width > height:
            ratio = 50.0 / width
        else:
            ratio = 50.0 / height

        save_t = str(save_number) + ".png"
        img.thumbnail((round(width * ratio), round(height * ratio)), Image.LANCZOS)
        img.save("./static/thumbnails/" + save_t)
        return [save_t, img.size[0], img.size[1]]

    # def get_coors_n_thumb(self, save_number):
    #     return (self.get_coordinates(self.get_geotagging(self.get_exif()[0])), self.get_thumbnail(save_number), self.filename, self.date_time, self.dt)

if __name__ == "__main__":
    efe = EXIFExtractor("test_files/File_006.jpeg")
    exif_data, labeled_exif_data = efe.get_exif()
    print("GPS Info:")
    print(labeled_exif_data)
    print("\n\n")
    geotags = efe.get_geotagging(exif_data)
    print("Geographical Tagging: ")
    print(geotags)
    coordinates = efe.get_coordinates(geotags)
    print("\n\nCoordinates for Image:", coordinates)
    print(efe.date_time)
