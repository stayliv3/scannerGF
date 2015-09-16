#/usr/bin/env python
#-*-coding:utf8-*-

__author__ = 'xdxd'

from flask import Flask
from flask import request
from flask import abort, redirect, url_for

from utils.pencillog import *



#log to file
logging.basicConfig(filename='log.txt',level=logging.DEBUG)
app = Flask(__name__)

#路由所有URL
@app.route('/', defaults={'path': ''},methods=['GET', 'POST', 'PUT', 'HEAD', 'DELETE'])
@app.route('/<path:path>',methods=['GET', 'POST', 'PUT', 'HEAD','DELETE'])
def catch_all(path):
	Log.d(str(request.method) + ' ' + str(request.url) +' ' + str(request.get_data()))

	if 'nevercouldexist' in path:
		abort(404)


	return 'hello my baby!'

	# return str(path) + str(request.get_data()) + str(request.method) + str(request.form)
	# return '111'






if __name__ == '__main__':
    app.run(host="0.0.0.0",port=80)