from pypika import Query, Table, Field
import constants

def get_foundation_query():
	table = get_table()
	fields = get_fields()
	query = Query.from_(table).select(*fields)
	return query


def get_foundation_query_sql():
	return get_foundation_query().get_sql()


def get_table():
	return Table(TABLE_NAME)


def get_fields():
	all_fields = [Field(constants.META_INSTANCE_ID), Field(constants.DEVICE_ID), Field(constants.START_TIME),
				 Field(constants.IMAGE_TYPE), Field(constants.COMMENTS), Field(constants.GPS_LATITUDE), 
				 Field(constants.GPS_LONGITUDE), Field(constants.GPS_ALTITUDE), Field(constants.GPS_ACCURACY),
				  Field(constants.END_TIME)]

	return all_fields


def get_fields_list():
	return [c.get_sql() for c in get_fields()]