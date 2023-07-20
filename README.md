# FileDateSorter
File date sorter

## Tool to update exif dates (with new date in the name of the image)

So, if your file's name is : 2002-11-09 10h14.png the the exif creation date and the os modification datetime will become 2002-11-09 10h14.

## How to use 

1. Create folder
2. Clone repository in it
3. in cmd : *python3 -m venv env && source env/bin-activate*
   > to create and activate python env
5. in cmd : *pip install -r requirements.txt*
   > to install Pillow and piexif
6. in cmd : *python3*
   > open the python shell
   - *from sorter import sort*
   - *sort('/path/from/root/to/folder')*
