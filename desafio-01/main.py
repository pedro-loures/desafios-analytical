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
# -1 create webpage
# -2 set parameter
# -3 upload image
# -4 POST http route with image and parameters
# -5 GET  http route with image binary

# Local import
import static.utils as ut
import static.img_processor as imgp

# External import
from flask import Flask, redirect, url_for, render_template
from flask_cors import CORS
import os


app = Flask(__name__)
CORS(app)

template_dir = os.path.dirname(__file__)
template_dir = os.path.join(template_dir, 'frontend')
app = Flask(__name__, template_folder=template_dir)

@app.route('/') 
def redirect_landing():
    return redirect(url_for('landing'))

@app.route('/landing', methods = ['POST', 'GET'])
def landing():
  return render_template('landing.html')  

# print(template_dir)
# imgp.process_img(ut.CORPUS + '/11.jpg')
if __name__ == '__main__':
  app.run(host="0.0.0.0", debug=True, use_debugger=True, use_reloader=True)
