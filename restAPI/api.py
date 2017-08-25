from flask import Flask
from flask_restful import Resource, Api
from flask_restful import reqparse
from flask.ext.mysql import MySQL
from tools import utils, accessDB, handleTyping
import constants
import pandas as pd



mysql = MySQL()
app = Flask(__name__)

credentials = accessDB.get_credentials()

app.config['MYSQL_DATABASE_USER'] = credentials[accessDB.USER]
app.config['MYSQL_DATABASE_PASSWORD'] = credentials[accessDB.PASSWORD]
app.config['MYSQL_DATABASE_DB'] = credentials[accessDB.DATABASE]
app.config['MYSQL_DATABASE_HOST'] = credentials[accessDB.HOST]

mysql.init_app(app)
api = Api(app)


class GetTableInfo(Resource):
    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('tablename', type=str, help='name of table you would like information on')
            args = parser.parse_args()

            _tablename = args['tablename']
            query = "SHOW columns FROM %s;" % _tablename 
            data = execute_query(query)
            return utils.respondTableData(data)

        except Exception as e:
            return {'error': str(e)}


class SelectColumnsWhere(Resource):
	def post(self):
		try:
			parser = reqparse.RequestParser()
			parser.add_argument('columnNames', required=True, type=str, help='comma separated list of column names for table')
			parser.add_argument('tablename', required=True, type=str, help='name of table you would like information on')
			parser.add_argument('whereStatement', type=str, help="single string columnname=value")
			args = parser.parse_args()

			_column_names = args['columnNames']
			_tablename = args['tablename']
			_whereStatement = args['whereStatement']

			if _whereStatement:
				query = "SELECT %s FROM %s WHERE %s;" % (_column_names, _tablename, _whereStatement)
			else:
				query = "SELECT %s FROM %s;" % (_column_names, _tablename)

			data = execute_query(query)
			columns = _column_names.split(',')

			return utils.respondSelectColumns(data, columns)


		except Exception as e:
			return {'error': str(e)}


class DashboardData(Resource):
	def post(self):
		try:
			parser = reqparse.RequestParser()
			parser.add_argument('blank', type=str, help='place holder for later filtering')
			args = parser.parse_args()

			_holder_arg = args['blank']

			query = constants.get_foundation_query_sql()
			data = execute_query(query)
			column_names = constants.get_fields_list()

			data_dict = utils.respondSelectColumns(data, column_names)
			

			return handleTyping.make_json_compatible(data_dict)

		except Exception as e:
			return {'error': str(e)}




def execute_query(query):
	conn = mysql.connect()
	cursor = conn.cursor()
	cursor.execute(query)
	data = cursor.fetchall()
	cursor.close()
	conn.close()
	return data



api.add_resource(GetTableInfo, '/GetTableInfo')
api.add_resource(SelectColumnsWhere, '/SelectColumnsWhere')
api.add_resource(DashboardData, '/DashboardData')

if __name__ == '__main__':
    app.run(debug=True)
