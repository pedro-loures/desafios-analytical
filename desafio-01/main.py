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
# -4 OK Apply local filter
# -5 OK Convolute image
# -6 OK Get min rectangle
# -7 OK expand/reduce min rectangle (with/whithout padding)
# -EXTRA minimum quadrange to correct perspective
# -EXTRA separete documents 


# create page
# TODO list 
# -1 OK create webpage
# -2 OK set parameter
# -3 OK upload image
# -4 POST http route with image and parameters
# -5 GET  http route with image binary

# Local import
from re import TEMPLATE
import static.utils as ut
import static.img_processor as imgp

# External import
from flask import Flask, flash, request, redirect, url_for, render_template, jsonify
from werkzeug.utils import secure_filename
from flask_cors import CORS
import os


app = Flask(__name__)
CORS(app)

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

UPLOAD_FOLDER = os.path.dirname(__file__)
UPLOAD_FOLDER = os.path.dirname('tmp')
TEMPLATE_FOLDER = os.path.dirname(__file__)
TEMPLATE_FOLDER = os.path.join(TEMPLATE_FOLDER, 'frontend')
app = Flask(__name__, template_folder=TEMPLATE_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/') 
def redirect_landing():
    return redirect(url_for('landing'))

@app.route('/landing', methods = ['POST', 'GET'])
def landing():
  if request.method == 'GET':
    return render_template('landing.html') 

# def upload_file():
#   if request.method == 'POST':
#     print('HERE!')
#     # check if the post request has the file part
#     if 'file' not in request.files:
#       flash('No file part')
#       return redirect(request.url)
#     file = request.files['file']
#     # if user does not select file, browser also
#     # submit an empty part without filename
#     if file.filename == '':
#       flash('No selected file')
#       return redirect(request.url)
#     if file and allowed_file(file.filename):
#       filename = secure_filename(file.filename)
#       file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

#       return redirect(url_for('uploaded_file',
#                               filename=filename))
#     return render_template('landing.html') 

@app.route('/process_image', methods = ['POST', 'GET'])
def process_image():
  if request.method == 'GET':
    req = request.args
    req = req.to_dict()
    img = ut.CORPUS + '/' + str(req['image_number']) + '.jpg'
    params = list(req.values())[:6]
    scan_threshold = float(params.pop(-1))
    reduce_factor,filter_size,filter_sensibility,convolution_factor, padding = [int(p) for p in params]
    params = [reduce_factor,filter_size,filter_sensibility,convolution_factor, padding, scan_threshold]
    
    print("parametros:",params)
    binary = imgp.process_img(img, *params)
    
    return binary
  else:
    return 'POST'

# print(TEMPLATE_FOLDER)
imgp.process_img(ut.CORPUS + '/6.jpg')
if __name__ == '__main__':
  app.run(host="0.0.0.0", debug=True, use_debugger=True, use_reloader=True)
