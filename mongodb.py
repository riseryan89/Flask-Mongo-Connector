from pymongo import MongoClient
from conf import consts as c
## 몽고DB 커넥션 포인트 Singleton Design

class MongoConn(object):
	# Underscored Variable 외부 접근 금지
	__db = None

	@classmethod
	def get_connection(cls):
		if cls.__db is None:
			# 몽고 DB 커넥션 에러시 ReTry 10회 실시
			retry = 10
			while retry > 0:
				try:
					client = MongoClient(c.DB_TEST,
					                     maxPoolSize=50,
					                     waitQueueMultiple=10
					                     )
					db = client['brace']
					cls.__db = db
					break
				except Exception as e:
					print(e)
					retry -= 1
					if retry == 0:
						return False
		return cls.__db


