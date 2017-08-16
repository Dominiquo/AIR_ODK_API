def respondTableData(query_data):
	# Query return protocol from "SHOW columns FROM tablename;" source
	# https://dev.mysql.com/doc/refman/5.7/en/show-columns.html
	FIELD = 'Field'
	TYPE = 'Type'
	NULL = 'NULL'
	KEY = 'Key'
	DEFAULT = 'Default'
	EXTRA = 'Extra'

	response_dict = {FIELD: [], TYPE: [], NULL: [], KEY: [],
							DEFAULT: [], EXTRA: []}
	try:
		for field, dType, isNull, key, default, extra in query_data:
			response_dict[FIELD].append(field)
			response_dict[TYPE].append(dType)
			response_dict[NULL].append(isNull)
			response_dict[KEY].append(key)
			response_dict[DEFAULT].append(default)
			response_dict[EXTRA].append(extra)

		return response_dict
			
	except Exception as e:
		print e
		# TODO: pass up exception to return non 200 response
		return None


def respondSelectColumns(response_data, column_names):
	try:
		columns = column_names.split(',')
		response_dict = {c_name:[] for c_name in columns}

		if len(response_data) == 0:
			return response_dict

		for res in response_data:
			for i, col in enumerate(columns):
				response_dict[col].append(res[i])

		return response_dict
	except Exception as e:
		print e
		# TODO: pass up exception to return non 200 response
		return None


		