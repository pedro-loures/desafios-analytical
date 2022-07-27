# Internal Import
import utils as ut

# External import
import numpy as np
import cv2 as cv

def process_img(img, reduce_factor = 7):


  # Process image
  image= cv.imread(img)
  original_image = image.copy()
  image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

  image = image * (image/255) * (image/255) #* (image/255)
  

  cv.imwrite(ut.FINAL + "/final.png", image)
  cv.imwrite(ut.FINAL + "/original.png", original_image)
  pass