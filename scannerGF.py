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
notexisturls = ['neverexist','nevercouldexist']
#路由所有URL

@app.route('/webscan_360_cn.html')
def webscan():
    return 'dc5445503925addea4cd3db496a78c66'


@app.route('/', defaults={'path': '/'},methods=['GET', 'POST', 'PUT', 'HEAD', 'DELETE'])
@app.route('/<path:path>',methods=['GET', 'POST', 'PUT', 'HEAD','DELETE'])
def catch_all(path):
	Log.i(path)
	Log.d(str(request.method) + ' ' + str(request.url) +' ' + str(request.get_data()))
	for url in notexisturls:
		if url in path:
			Log.d(path)
			abort(404)
		else:
			pass

	Log.e(path)
	return 'hello my baby!'

	# return str(path) + str(request.get_data()) + str(request.method) + str(request.form)
	# return '111'






if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8099)