# Internal Import
import utils as ut

# External import
import numpy as np
import cv2 as cv
import warnings


def _get_min_square(Matrix, padding = 1):
  assert (Matrix != 255).sum() > 1, "image is blank"

  _height, _width = Matrix.shape
  _found0 = False

  for _y, _row in enumerate(Matrix):
    if _y < padding or _y + 1> _height - padding:
      continue
    for _x, _value in enumerate(_row):
      if _x < padding or _x + 1 > _width - padding:
        continue
      # print(_value)
      if _value < 255:
        # print('ok')
        if not _found0:
          _xtop, _xleft, _xbottom, _xright = _x, _x, _x, _x
          _ytop, _yleft, _ybottom, _yright = _y-1, _y, _y, _y
          _found0 = True   
        elif _x + 2 > _xright: # make a 
          _xright = _x + 1# if (_x+2 > _width) else _x + 1
          
          _yright = _y
        elif _x <= _xleft : # to the left of _xright
          _xleft = _x - 1
          _yleft = _y
        
        _xbottom = _x
        _ybottom = _y+1

  # _xtop, _yleft, _xbottom, _yright  >> intersections 
  return [_xleft, _ytop, _xleft, _ybottom, _xright, _ybottom, _xright, _ytop], [_xtop, _yleft, _xbottom, _yright]


def _get_min_quadrilateral(Matrix):
  # [xtop, yleft, xbottom, yright] >> intersection 

  [xleft, ytop, xleft, ybottom, xright, ybottom, xright, ytop], [xtop, yleft, xbottom, yright] = _get_min_square(Matrix)

  # line1, line2, line3, line4 >> condition from lines 
  return xleft, ytop, xleft, ybottom, xright, ybottom, xright, ytop


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

def _convert_points(points, shape1, shape2):
  _width1, _height1 = shape1
  _width2, _height2 = shape2

  image_points = np.array([0, 0, 0, 1, 1, 1, 1, 0])
  image_points = image_points.reshape((-1, 1, 2))
  image_points = (points + image_points) * np.array([_width1/_width2 , _height1/_height2])
  image_points = image_points - 1 
  image_points[image_points < 0] = 0
  
  return image_points

# if side overlaps with document expand square, else reduces it
def _reduce_side(var, image, threshold, slice, expand_direction=1):
  begin, end = slice
  _overlap = (image[var][begin:end].mean() > threshold) 
  _expand = 1 if _overlap else - 1 # makes it moere legible
  _expand = _expand * expand_direction # direction of expansion (negative or positive)
  
  # expand/reduce while initial condition is mantained 
  while(True):    
    _expand_overload = var + _expand < 0 or var + _expand >= image.shape[0]
    if (image[var][begin:end].mean() > threshold) != _overlap or _expand_overload : break
    var = var + _expand
  return var

def _reduce_square(square, image, padding = 5, scan_threshold = 1):
  
  # apply padding
  if padding == 0:
    _img_cpy = image.copy()
  else:
    _img_cpy = image[padding:-padding].T
    _img_cpy = _img_cpy[padding:-padding].T
  _pad_height, _pad_width = _img_cpy.shape
    
  # correct min square for padding
  left, top = square[0][0].astype(int)
  right, bottom = square[2][0].astype(int)
  
  left = 0 if left < padding else left - padding
  top = 0 if top < padding else top - padding
  bottom = _pad_height-1 if bottom >= _pad_height else bottom - padding
  right = _pad_width-1 if right >= _pad_width else right - padding

  # correct do 0 >> white, 1 >> black
  _img_black = (_img_cpy == 0).astype(int)
  _thr = _img_black.mean() * scan_threshold * _img_black.std()

  # if side overlaps with document expand square, else reduces it
  top = _reduce_side(top, _img_black, _thr, (left, right), expand_direction=-1)
  left = _reduce_side(left, _img_black.T, _thr, (top, bottom), expand_direction=-1)
  bottom = _reduce_side(bottom, _img_black, _thr, (left, right), expand_direction=1)
  right = _reduce_side(right, _img_black.T, _thr, (top, bottom), expand_direction=1)

  new_square = np.array([left, top, left, bottom, right, bottom, right, top])
  new_square = new_square.reshape((-1, 1, 2))
  # return square
  return new_square + padding

def process_img(img, reduce_factor = 7,
                filter_size=10,filter_sensibility=15, 
                convolution_factor=20, padding=15,
                scan_threshold = .5
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
  _sheight, _swidth = _image.shape
  _conv_height, _conv_width = int(_sheight/convolution_factor), int(_swidth/convolution_factor)
  _convolution = cv.resize(_image, (_conv_width, _conv_height ))

  # quatrant minimum square
  _points = _get_min_quadrilateral(_convolution)
  _points = np.array(_points)
  _points = _points.reshape((-1, 1, 2))
  # convert points size
  _image_points = _convert_points(_points, (_swidth, _sheight),(_conv_width, _conv_height))
  
  # Image minimum square 
  _image_points = _reduce_square(_image_points, _image, padding = padding, scan_threshold=scan_threshold)
  _image_points = _reduce_square(_image_points, _image, padding = 0, scan_threshold=scan_threshold)
  # Convert points size  
  _orig_h, _orig_w, _= _original_image.shape
  _original_points = _convert_points(_image_points, (_orig_w, _orig_h), (_width, _height))
  
  # Write rectangle
  rectangle_img = _original_image.copy()
  cv.polylines(rectangle_img, [_original_points.astype(int)], True, 100, 1)  

  # cut image
  _left, _top = _original_points[0][0].astype(int)
  _right, _bottom = _original_points[2][0].astype(int) 
  final_image = _original_image[_top:_bottom, _left:_right]

  # save image
  cv.imwrite(ut.TMP + "/rectangle.png", rectangle_img)
  cv.imwrite(ut.FINAL + "/final.png", final_image)
  pass