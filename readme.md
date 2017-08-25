# ODK AI Research Lab API


## Introduction

This API was developed for querying and serving data from ODK's databases to bypass ODK aggregate exporting latency. Currently, ODK Aggregate allows for users to view their form data from the ODK Aggregate dashboard, but in order to manipulate this data further or display live in ways that aren't currently available through Aggregate, it must be exported. When databases become larger, exporting the entire database into a CSV file isn't the most efficient process especially when internet bandwidth may hinder this process. 


### Dependencies
Built in Python 2.7

- flask
- flask_restful
- pandas
- pypika

### Installation

Clone the repository and create your necessary constants and credentials file to connect to your database. Currently work in progress to make this process more streamlined with less personal code contribution to make functional.

### Launch

Once the proper DB credentials are stored, the command the launch the database is simply
 ```
 Python RestAPI/api.py
 ```
 
 The RESTFUL services will no be available on the specified hostname. This was developed with localhost usage. I will investigate necessary code to configure the launch domain. 
 
 ### Usage
 
 Let's consider the usage when launching on local host. Currently functionality allows us to get table information, select columns from a table and populate the mCrops dashboard. 
 
 #### Get Table Information
 
Used to query the DB to get more information on a given table to posislby make a more refined query later. This is very extremely general use.
 
Send a post request to `localhost:8000/GetTableInfo` with param `tablename=NAME_OF_TABLE`. This will return a json object with columns as Table column names and information about that columns via https://dev.mysql.com/doc/refman/5.7/en/show-columns.html. 

#### Select Columns Where

Another extremely general API call to directly access the database. You must know the structure of your database to properly make these calls as there isn't much room for error correction.

Send a post request to `localhost:8000/SelectColumnsWhere` with params `columnNames=NAME,OF,ALL,COLUMNS`, `tablename=NAME_OF_TABLE`, and `whereStatement=COLUMNS=CONDITIONAL`. If the `whereStatement` is not included, the API will return the entire table. Again, this is extremely general and I plan to update this to handle where statements better.

#### DashboardData

More specific call for our uses. This needs to be updated when we get more information on photos from ODK (https://forum.opendatakit.org/t/dynamically-display-odk-data-on-a-website-using-mysql/9412). There also needs to be added infastructure to handle specific calls that may include joining tables and filtering results. `pypika` is helpful with constructing these statements as you can see in  `table_data.py`. 


### TODOs

As of right now, I didn't have too much involvement with the APIs current use cases. This means that the API is extremely general and mostly provides a template for developing onwards. I am familiar with `pandas` so I use the `pandas` structure as a way of jsonifying data and on the other side of the request, `pandas` can also be used to reconstruct and restructure the data for more complex function application. 

I plan on mocking the api to test response typing because the jsonify method used by `flask_restful` doesn't seem to have all of the capabilities of other jsonify functions. Along with this, I want to try to expand the SQL statement function generating library. I have yet to fully utilize `pypika` because of the early generalization, but I think it would be extremely beneficial to continue with this library to have a more wholistic language for creating safe queries. 


Send a 
 
