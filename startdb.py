from __future__ import division
import sys
import os
import sqlite3
import traceback

def conn_to_db(dbname): #Returns sqlite3 connection to dbname, none if error
	try:
		tmp  = open(dbname)		#If we find the database, close the file
		tmp.close()
		conn = sqlite3.connect(dbname) 	#in finally and return a sqlite3 connection
		return conn
	except IOError:			#If not, let's initialze the database with the
		try:				#schema in create_schema.sql
			makeschema = open("makedbschema.sql")
			conn = sqlite3.connect(dbname)
			c = conn.cursor()
			print "Warning: you are about to create a new database with name %s."
			print "Are you sure you want to do this (y/n)?"
			inps = raw_input() #Do you really want to make another db?
			if inps is 'y' or inps is 'yes':
				for l in makeschema:
					c.execute(l) #execute the contents per line. Requires that
								#each CREATE statement is on one line.
				conn.commit()
				#We now have a connection and a cursor to a 
				#freshly schema'd database Fill that sucker up!
				filldb = open("filldb.sql")
				for l in filldb:
					c.execute(l)
		
				conn.commit()
				return conn #Return connection to freshly populated database
			else:
				print "Aborting database creation."
				sys.exit(-5)
				
	except IOError:
		print("Can't create the database schema because files were not found.")
		return
	except sqlite3.OperationalError:
		print("Incorrect SQL statement. Please check files for syntax errors.")
		traceback.print_exc()
		return


			
			


