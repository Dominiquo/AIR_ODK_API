import pandas as pd
import constants


def make_json_compatible(data_dict):
	df = pd.DataFrame(data_dict)
	df = df.reset_index()
	df[constants.END_TIME] = df[constants.END_TIME].apply(str)
	df[constants.START_TIME] = df[constants.START_TIME].apply(str)
	df[constants.GPS_LATITUDE] = df[constants.GPS_LATITUDE].apply(float)
	df[constants.GPS_LONGITUDE] = df[constants.GPS_LONGITUDE].apply(float)
	df[constants.GPS_ALTITUDE] = df[constants.GPS_ALTITUDE].apply(float)
	df[constants.GPS_ACCURACY] = df[constants.GPS_ACCURACY].apply(float)
	
	return df.to_dict()
