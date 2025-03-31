#!/usr/bin/env python3

import os
from PIL import Image

# To get the username from environment variable
user = os.getenv('USER')

# The directory which contains all the images.
image_directory = '/home/{}/supplier-data/images'.format(user)

# Parsing through all the images
for image_name in os.listdir(image_directory):

    # Accepting files that has tiff extension and ignoring hidden files
    if not image_name.startswith('.') and 'tif' in image_name:

        # creating absolute path for each image
        image_path = os.path.join(image_directory, image_name)

        # Get th absolute name of image
        #path = os.path.splitext(image_path)[0]

        # Open the image
        im = Image.open(image_path)

        file, ext = os.path.splitext(image_name)

        # Convert the image to RGB, resize and then save it with jpeg format
        im.convert('RGB').resize((600, 400)).save(os.path.join(image_directory, "{}.jpeg".format(file)))