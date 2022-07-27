# Author: Pedro Loures Alzamora
# Description: Removes white background from digitalizations

# General
# TODO list
# -1 benchmark

# remove white
# TODO list
# -1 OK Read Document 
# -2 OK Apply exponential filter
# -3 OK Scan image using the image mean as a threshold
# -4 TODO Apply local filter
# -5 TODO Convolute image
# -6 TODO Get min rectangle
# -7 TODO expand/reduce min rectangle (with/whithout padding)
# -EXTRA minimum quadrange to correct perspective
# -EXTRA separete documents 


# create page
# TODO list 
# -1 create webpage
# -2 set parameter
# -3 upload image
# -4 POST http route with image and parameters
# -5 GET  http route with image binary

import utils as ut
import img_processor as imgp

imgp.process_img(ut.CORPUS + '/11.jpg')