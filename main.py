#!/usr/bin/env python

import webapp2

import sys, os
from os.path import dirname
sys.path.append(os.path.dirname(os.path.abspath(__file__))+'/jieba')

import json

import jieba
jieba.tmp_dir = os.path.dirname(os.path.abspath(__file__)) + '/tmp'

class MainHandler(webapp2.RequestHandler):
	def get(self):
		self.response.headers['Content-Type'] = 'application/json'
		self.response.out.write(json.dumps(self.jieba_usage()))

	def post(self):
		self.response.headers['Content-Type'] = 'application/json'
		self.response.out.write(json.dumps(self.jieba_usage()))

	def jieba_usage(self):
		out = {
			'status' : False
		}
		try:
			data = self.request.get("in") or None
			if data <> None:
				out['out'] = []
				for item in jieba.cut(data, cut_all=True):
					out['out'].append( item )
				out['status'] = True
		except Exception, e:
			out['error'] = str(e)
			pass
		return out

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
