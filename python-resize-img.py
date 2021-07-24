import os, sys
from PIL import Image

import re
def list_files_re(rootpath, filename_re=None, folder_re=None ):
    '''
    rootpath : root path to lookup files
    filename_re : regular expression to search for filename
    folder_re : regular expression to search for folder

    return : a list of filepaths
    '''


    list_files = []
    for folder, _, files in os.walk(rootpath):
        for file in files:
            if filename_re == None:
                filename_re = '.*'
            if folder_re == None:
                folder_re = '.*'

            if ((re.search(filename_re, file) != None) & (re.search(folder_re, folder) != None)):
                list_files.append(os.path.join(folder, file))

    return list_files




size = 128, 128
folder_path = '/Users/isara/Downloads/images'
outfolder_path = '/Users/isara/Downloads/images_resized'
os.makedirs(outfolder_path, exist_ok=True)

list_img_path = list_files_re(folder_path, '.JPG')
for infile in list_img_path:
    outfile = os.path.join(outfolder_path, os.path.basename(infile) )

    im = Image.open(infile)
    im.thumbnail(size, Image.ANTIALIAS)
    im.save(outfile)
