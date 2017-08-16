import json

CREDENTIALS_PATH = 'credentials.p'
USER = 'MYSQL_DATABASE_USER'
PASSWORD  = 'MYSQL_DATABASE_PASSWORD'
DATABASE = 'MYSQL_DATABASE_DB'
HOST = 'MYSQL_DATABASE_HOST'

def get_credentials(credentials_path=CREDENTIALS_PATH):
	return load_data(credentials_path)

def load_data(data_path):
	with open(data_path, 'r') as infile:
		data = json.load(infile)
	return data

def dump_data(data_path, obj):
	with open(data_path, 'w') as outfile:
		json.dump(obj, outfile)
	return True