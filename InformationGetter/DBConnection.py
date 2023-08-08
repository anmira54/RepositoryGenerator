import pyodbc
import Constants.Environment as environment

connection_string = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={environment.server};DATABASE={environment.database};UID={environment.username};PWD={environment.password}"
connection = pyodbc.connect(connection_string) 