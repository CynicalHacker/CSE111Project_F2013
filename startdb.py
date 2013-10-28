from __future__ import division
import sys
import os
import sqlite3
import traceback

def conn_to_db(dbname): #Returns sqlite3 connection to dbname
	try:
		tmp  = open(dbname)		#If we find the database, close the file
		tmp.close()
		conn = sqlite3.connect(dbname) 	#in finally and return a sqlite3 connection
		return conn
	except IOError:			#If not, let's initialze the database with the
		try:				#schema in create_schema.sql
			line = open("makedbschema.sql")
			conn = sqlite3.connect(dbname)
			c = conn.cursor()
			for l in line:
				c.execute(l) #execute the contents line by line. Requires that
							#each CREATE statement is on one line.
			conn.commit()
			return conn
		except IOError:
			print("Damn. Can't create the database schema because dbschema.sql was not found.")
			return
		except sqlite3.OperationalError:
			print("Incorrect SQL statement. Please check dbschema.sql for syntax errors.")
			traceback.print_exc()
			return
