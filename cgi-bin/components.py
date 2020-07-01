#!/usr/bin/env python3

""" 
	This module provides a set of reuseable functions
	which provide the main app functionality.
	We could even go a stage further and separate
	database interactions from logic...
"""

# import modules from Python standard library
from bson.objectid import ObjectId

def register( db, form ):
	""" Registers a new user by inserting an account
	    in the accounts collection

	Params:
		db: 	handle to a database
		form: 	FieldStorage object
	
	Returns:
		Dict 
	"""
	# registration status false by default
	status = False
	try:
		# get the studentId from the form
		studentId = form['studentId'].value
		# get the user from the form
		user = form['user'].value
		# get the forename from the form
		fname = form['fname'].value
		# get the surname from the form
		lname = form['lname'].value
		#get student registration data from form
		registered = form['registered'].value

	except KeyError:
		# a field must be missing from the form data
		response = "Please complete all fields."

	else:
		# check if the student has already been registered
		result = db.mbanc001.find_one( { '$or': [
			{ 'registered' : registered }
		]} )

		# if so, print message to say the student has registered
		if result:
			if registered = True:
				response = "Student has already registered."

		# otherwise go ahead and register the student
		else:
			query = {
				"user": user,
				"registered" : True
			}
			# make sure name fields aren't empty
			# if they are, give them empty string values
			if 'fname' in form:
				fname = form['fname'].value
			else:
				first = ""
			if 'lname' in form:
				lname = form['lname'].value
			else:
				last = ""
			# append name to query
			query["send"] = { "studentId" : studentId, "user" : user, "fname" : fname, "lname" : lname, registered : bool }
			# insert the account in the database
			doc = db.accounts.insert( query )
			if doc:
				status = True
				response = "Student has been registered successfully!"
			else:
				response = "Problem registering student. Please refresh the page to try again."
	# return something useful...
	return {'status': status, 'msg': response}
