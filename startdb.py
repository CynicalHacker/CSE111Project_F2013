from __future__ import division
import sys
import os
import sqlite3
import traceback
import hashlib
import myadmin
import myuser

##Module to initialize db connection and authenticate the user.

def login_user():
	print("Enter databse name (blank for default):")
	dbname = raw_input()
	if dbname == "": #if blank, use default name
		dbname = "chemdb" 
	conn = conn_to_db(dbname) #attempt connection
	if conn is None: #DB is missing
		print("Database connection failed. Force creation[y/n]?")
		cont = raw_input
		if cont == "y":
			conn = conn_to_db(dbname, True)
			if conn is None: #Creation failed, probably missing config
				print("Could not create database. Check error messages. Exiting...")
				sys.exit(-5)
			else:
				print("Database creation succesful!")
		else: #do not continue
			print("Exiting...")
			sys.exit(-5)
	#We now have a connection to a database.
	print("Database connection successful!")	
	while(True):
		print("Are you user or admin?")
		user = raw_input()
		if user == "user":
			print("Welcome, user!")
			myuser.main(conn) #Pass control to myuser.py
			sys.exit(0) #If we return from myuser, exit the program
		elif user == "admin":
			print("Please enter the admin password:")
			pwd = raw_input()
			if isAdmin(pwd):
				print("Welcome, Admin!")
				myadmin.main(conn) #Pass control to myadmin.py
				sys.exit(0) #If we return from myadmin, exit program
			else:
				print("Authentication failure!")
		else:
			print("Unrecognized user type!")

def make_default_db():
	return conn_to_db("chemdb", True)

def conn_to_db(dbname, create=False): #Returns sqlite3 connection to dbname, None if error
	try:
		tmp  = open(dbname)		#If we find the database, close the file
		tmp.close()				#and return a sqlite3 connection
		conn = sqlite3.connect(dbname) 
		return conn
	except IOError:			#If not, check to see if we meant to create a db.
		if create is True:	#Continue to make and pop db if we set create flag.
			try: #Try to make db schema
			
				makeschema = open("makedbschema.sql")
				conn = sqlite3.connect(dbname)
				c = conn.cursor()
				
				for l in makeschema:
					c.execute(l) #Pipe statements one line at a time from file
				conn.commit() 	 #and execute them. Must be one SQL per line.
				
			except sqlite3.OperationalError: #bad SQL code!
				print "Warning! SQL Error detected! Please check makebdschema.sql for syntax errors! Stack trace below:"
				traceback.print_exc()
				return None #For safety
			except IOError:
				print("Warning! Population script is missing! Please make sure that makedbschema.sql is present!")
				return None
	
			#At this point in the code, we have a cursor on a db with a schema.

			try: #to populate newly-made DB
				filldb = open("filldb.sql")
				
				for l in filldb:
					c.execute(l)
				conn.commit()
				
				return conn #Return connection to freshly populated database
			except IOError:
				print "Warning! Population script is missing! Please make sure that filldb.sql is present!"
				return None
			except sqlite3.OperationalError:
				print "Warning! SQL Error detected! Please check filldb.sql for syntax errors! Stack trace below:"
				traceback.print_exc()
				return None #For safety
				
		else: #We did not want to make a new database. Return None?
			return None
				
def isAdmin(password):
	#Password is "password". Returns true if it matches
	adminhash = '\xf9\xe0H\xbeL\xd0$\xfc\x14<eR}#\xf2\x88\xfb?\xbb\xcfg\xda\x87tU\x9cl\x07\xcd^\xdd\x1dWtQ\xd1\xb1O\x86K\xf1\xca)\\\xd5\xce\xd8\x92\x95\x84\xca\x14\x98\xbex\xd6\x07\xcc5P\xe7L\xce\xca'
	salt = 'kLi7@alIqDV!2b%."DcNLR$y!yfWkLY11b4l7trkA9j@!r5BDXcm_qDdiQMQd+vq_Ly#M.,ja@,B5g+eUk#FYlW8r8w0ff/Xz%w'
	checker = hashlib.sha512()
	checker.update(password + salt)
	if checker.digest() == adminhash:
		return True	
	else:
		return False
