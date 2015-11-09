from flask import Flask
from flask import request
from flask import render_template
from flask import jsonify
import json
from time import strftime

app = Flask(__name__)

app.cluster_img_dict = {0:'static/dist/img/cluster_0.jpg',\
                        1:'static/dist/img/cluster_1.jpg',\
                        2:'static/dist/img/cluster_2.jpg',\
                        3:'static/dist/img/cluster_3.jpg',\
                        4:'static/dist/img/cluster_4.jpg',\
                        5:'static/dist/img/cluster_5.jpg'}

# OUR HOME PAGE
#============================================
@app.route('/')
def welcome():
    myname = "Matt"
    return render_template('index.html', data=myname)

@app.route('/technical_summary')
def technical_summary():
    return render_template('technical_summary.html')

@app.route('/cluster_map')
def cluster_map():
    return render_template('cluster_map.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7000, debug=True)