#/usr/bin/env python
#-*-coding:utf8-*-

__author__ = 'xdxd'

from flask import Flask
from flask import request
from flask import abort, redirect, url_for
import time
from utils.pencillog import *



#log to file
logging.basicConfig(filename='log.txt',level=logging.INFO)
app = Flask(__name__)
notexisturls = ['neverexist','nevercouldexist']
#路由所有URL

@app.route('/webscan_360_cn.html')
def webscan():
    return 'dc5445503925addea4cd3db496a78c66'

@app.route('baidu-verify-C88E329F6A.txt')
def baiduscan():
	return 'c7701f214f170243f820b45f7cb04258'

@app.route('/', defaults={'path': '/'},methods=['GET', 'POST', 'PUT', 'HEAD', 'DELETE'])
@app.route('/<path:path>',methods=['GET', 'POST', 'PUT', 'HEAD','DELETE'])
def catch_all(path):
	Log.d(path)
	Log.i(str(request.method) + ' ' + str(request.url) +' ' + str(request.get_data()))
	for url in notexisturls:
		if url in path:
			Log.d(path)
			abort(404)
		else:
			pass

	Log.d(path)
	return 'hello my baby!' + str(time.time())

	# return str(path) + str(request.get_data()) + str(request.method) + str(request.form)
	# return '111'






if __name__ == '__main__':
    app.run(host="0.0.0.0",port=80, threaded=True)