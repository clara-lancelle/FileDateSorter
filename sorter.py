from datetime import datetime
import os
import re

import piexif

def sort(folder_name):
    for root, _, files in os.walk(folder_name):
        for file in files:
            if re.match(r"[\d]{4}-[\d]{2}-[\d]{2}", file):
                fullPath = os.path.abspath(os.path.join(root, file))
                file_date = re.search("[\d]{4}-[\d]{2}-[\d]{2}", file)
                file_date_array = re.split('-', file_date.group(0))
                file_hour = re.search("[\d]{2}h[\d]{2}", file)
                if file_hour:
                    file_hour_array = re.split('h', file_hour.group(0))
                else :
                    file_hour_array = [0,0]
                new_date = datetime(int(file_date_array[0]), int(file_date_array[1]), int(file_date_array[2]), int(file_hour_array[0]), int(file_hour_array[1]), 0).strftime("%Y:%m:%d %H:%M:%S")
                new_epoch = datetime(int(file_date_array[0]), int(file_date_array[1]), int(file_date_array[2]), int(file_hour_array[0]), int(file_hour_array[1]), 0).strftime("%s")
                exif_dict = piexif.load(fullPath)
                #Update DateTimeOriginal
                exif_dict['Exif'][piexif.ExifIFD.DateTimeOriginal] = new_date
                #Update DateTimeDigitized               
                exif_dict['Exif'][piexif.ExifIFD.DateTimeDigitized] = new_date
                #Update DateTime
                exif_dict['0th'][piexif.ImageIFD.DateTime] = new_date
                exif_bytes = piexif.dump(exif_dict)
                piexif.insert(exif_bytes, fullPath)            
                # update modification time
                os.utime(fullPath, (int(new_epoch),int(new_epoch)))
                print('done!')
