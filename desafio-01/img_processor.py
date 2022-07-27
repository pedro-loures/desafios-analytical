# Internal Import
import utils as ut

# External import
import numpy as np
import cv2 as cv

def process_img(img, reduce_factor = 7):


  # Process image 1
  image= cv.imread(img)
  original_image = image.copy()
  image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

  image = 255 - image # invert to reduce mean

  # Exponential Filter 2
  image = image * (image/255) * (image/255)
  threshold = image.mean() # Define treshold

  # Resize image do make it lightier
  _height, _width = image.shape 
  _height, _width = int(_height/reduce_factor), int(_width/reduce_factor) 
  image = cv.resize(image, (_width, _height))

  # Local Filter 3
  image = (image < threshold).astype("uint8") * 255


  cv.imwrite(ut.FINAL + "/final.png", image)
  cv.imwrite(ut.FINAL + "/original.png", original_image)
  pass