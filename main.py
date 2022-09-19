"""
Stitch and convert image files to PDF.
baharehd
Sept. 16/22

i guess describe variables and types here
and then describe functions here
"""

from PIL import Image

# TODO: global variables
# image locations,
source_path = 'test_images\\'
output_path = 'test_output\\'

# TODO: inputs
# every user will want to input at least 1 image;
# figure out if i need to add extra options later
image = Image.open(source_path, "r")  # testing one image for now

# TODO: make sure image formats are ok/won't crash the script (create separate script to make functions?)

# TODO: need to figure out how to stitch images so that each image would be a separate page in the pdf

# TODO: save/export final file! Yay!
image.save(output_path, "pdf")
