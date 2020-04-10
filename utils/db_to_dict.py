def response_composer(db_data, fields):
	out = dict()
	out['result'] = 'ok'
	out['data'] = dict()
	out['data']['_id'] = str(db_data['_id'])
	for i in fields:
		out['data'][i] = db_data[i]
	return out