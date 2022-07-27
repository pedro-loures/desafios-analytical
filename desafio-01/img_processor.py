# Internal Import
import utils as ut

# External import
import numpy as np
import cv2 as cv
import warnings


# TODO apply filter in border
def _filter_disturbance(image, filter_size, filter_sensibility):
  assert filter_size < 100, "filter_size must be a percentage smaller than 100"

  # process image
  _img_black = (image == 0).astype(int)
  _t_img_black = _img_black.T
  _width, _height = image.shape 

  # process parameters
  _filter = int(min(_width, _height) * filter_size/100)
  _line_sensibility = _filter/5
  _half = int(_filter/2)
  _sensibility = int((filter_sensibility/100) * (_filter*_filter))

  # apply filter in image
  for _y, _row in enumerate(_img_black):
    for _x, _value in enumerate(_row):
      if _value == 1: 
        _soma = 0
        _y_overflow = _y-_half < 0 or _y+_half+1 >= _width
        _x_overflow = _x-_half < 0 or _x + _half >= _height
        if _y_overflow or _x_overflow: continue
        _soma = _img_black[_y-_half:_y+_half+1,_x-_half:_x+_half+1].sum()
        
        _liney = _img_black[_y][_x-_half:_x+_half+1].sum() > _line_sensibility    # if more than half the size
        _linex = _t_img_black[_x][_y-_half:_y+_half+1].sum() > _line_sensibility  #  is black is a line
        _condition = _soma < _sensibility  and not _linex and not _liney
        if _condition: image[_y][_x] = 255 # makes it white
  return image


def process_img(img, reduce_factor = 7,
                filter_size=10,filter_sensibility=15, 
                convolution_factor=20
                ):


  # Process image 1
  _image= cv.imread(img)
  _original_image = _image.copy()
  _image = cv.cvtColor(_image, cv.COLOR_BGR2GRAY)

  _image = 255 - _image # invert to reduce mean

  # Exponential Filter 2
  _image = _image * (_image/255) * (_image/255)
  _threshold = _image.mean() # Define treshold

  # Resize image do make it lightier
  _height, _width = _image.shape 
  _height, _width = int(_height/reduce_factor), int(_width/reduce_factor) 
  _image = cv.resize(_image, (_width, _height))

  # Local Filter 3
  _image = (_image < _threshold).astype("uint8") * 255

  # Local Filter 4
  _image = _filter_disturbance(_image, filter_size=filter_size, filter_sensibility=filter_sensibility)

  # Checks as apply minimum convolution factor division
  _input_convolution_factor = convolution_factor
  if int(min(_image.shape)/convolution_factor) < 10: 
    while(True):
      convolution_factor = convolution_factor - 1
      if int(min(_image.shape)/convolution_factor) > 10:
        warnings.warn("input convolution_factor["+str(_input_convolution_factor)+"] too small, using "+ str(convolution_factor) + " instead.")
        break

  # Convolute image
  s_height, s_columns = _image.shape
  conv_height, conv_columns = int(s_height/convolution_factor), int(s_columns/convolution_factor)
  _convolution = cv.resize(_image, (conv_columns, conv_height ))
  _clean_convolution = _convolution.copy()



  cv.imwrite(ut.FINAL + "/final.png", _image)
  cv.imwrite(ut.TMP + "/convolution.png", _convolution)
  cv.imwrite(ut.FINAL + "/original.png", _original_image)
  pass