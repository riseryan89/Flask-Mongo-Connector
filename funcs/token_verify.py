from flask import Blueprint, make_response, jsonify, request
from datetime import datetime
from mongodb import MongoConn
import jwt
import json
from conf import consts as c
from utils import *

token_verify_service = Blueprint("users", __name__, url_prefix="/auth")


'''
Performance Benchmark
Without MongoDB Pool : 70 ~ 120 ms
With MongoDB Pool : 8 ~ 15 ms

Except Fetching Time
'''

@token_verify_service.route("/", methods=["POST"])
def token_verify():
	try:
		body = json.loads(request.data)['token']
		func = json.loads(request.data)['func']
	except KeyError:
		return jsonify(result="failed", data='2 parameters required. [token, func]')
	except Exception as e:
		print(e)
		return jsonify(result="failed", data='parameter Error')

	try:
		# Token Decoding Start
		token = jwt.decode(body, c.JWT, algorithms=['HS256'])
	except jwt.InvalidSignatureError:
		# Token Signature Error
		return jsonify(result="failed", data='invalid signature')
	except jwt.ExpiredSignatureError:
		# Token Signature Error
		return jsonify(result="failed", data='signature expired')
	except Exception as e:
		# Rest Errors Might Occur
		print(e)
		return jsonify(result="failed", data='unable to authenticate')
	if token['exp'] < int(datetime.utcnow().timestamp()):
		# 1 more Token Expired Catch for Security
		return jsonify(result="failed", data='expired')

	try:
		mongo = MongoConn.get_connection()
		if not mongo:
			return jsonify(result="failed", data='DB Connection Failed')
		if func == 'user':
			conn = mongo['accounts']
		else:
			return jsonify(result="failed", data='func parameter error')
	except Exception as e:
		# 모든 에러 프린팅, 추후 로그 확인 후 세분화
		print(e)
		return jsonify(result="failed", data='DB Connection Failed')
	try:
		results = conn.find_one({'pushToken': token['user']['pushToken']})
		if not results:
			return jsonify(result="failed", data='no such a member')
		if func == 'user':
			return jsonify(response_composer(results, ['email', 'SN', 'wSN', 'nick', 'flag', 'state', 'signupDate', 'kycID']))

	except Exception as e:
		print(e)
		return jsonify(result="failed", data='no such a member')