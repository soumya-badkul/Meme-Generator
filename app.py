from flask import Flask, render_template, request, jsonify
import os
from flask_jsglue import JSGlue
from meme import *
from trending123 import *
from trendingcat import *

jsglue = JSGlue()


app = Flask(__name__)
jsglue.init_app(app)


APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def index():
    return render_template('memedev.html')

@app.route('/memegenerator', methods=['POST'])
def memegenerator():

    #image
    target = os.path.join(APP_ROOT, 'static/inputs')
    target1 = os.path.join(APP_ROOT, 'static/results')
    for upload in request.files.getlist("File1"):
        filename = upload.filename
    destination1 = "/".join([target1, filename])
    destination = "/".join([target, filename])
    upload.save(destination)
    
    #lines
    toplines = request.form['top-text']
    bottomlines = request.form['Bottom-text']
    print(toplines)


    meme(destination, destination1, toplines, bottomlines)

    return jsonify({'filename' : filename})


@app.route('/memegenerator123', methods=['POST'])
def memegenerator123():

    target1 = os.path.join(APP_ROOT, 'static/results')
    target = os.path.join(APP_ROOT, 'static/inputs')
    destination1 = "/".join([target1, '123.jpg'])
    destination = "/".join([target, '123.jpg'])
    
    #lines
    leftlines = request.form['left-text']
    middlelines = request.form['middle-text']
    rightlines = request.form['right-text']
    

    trending123(destination, destination1, leftlines, middlelines, rightlines)

    return jsonify({'filename' : '123.jpg'})

@app.route('/memegeneratorcat', methods=['POST'])
def memegeneratorcat():

    target1 = os.path.join(APP_ROOT, 'static/results')
    target = os.path.join(APP_ROOT, 'static/inputs')
    destination1 = "/".join([target1, 'cat.jpg'])
    destination = "/".join([target, 'cat.jpg'])
    
    #lines
    leftlines = request.form['left-text']
    rightlines = request.form['right-text']
    

    trendingcat(destination, destination1, leftlines, rightlines)

    return jsonify({'filename' : 'cat.jpg'})

@app.route('/memegeneratoryesno', methods=['POST'])
def memegeneratoryesno():

    target1 = os.path.join(APP_ROOT, 'static/results')
    target = os.path.join(APP_ROOT, 'static/inputs')
    destination1 = "/".join([target1, 'yesno.jfif'])
    destination = "/".join([target, 'yesno.jfif'])
    
    #lines
    top = request.form['top-text']
    bottom = request.form['bottom-text']
    
    print(top)
    print(bottom)

    trendingyesno(destination, destination1, top, bottom)

    return jsonify({'filename' : 'yesno.jfif'})


if __name__ == '__main__':
	app.run(debug=True)