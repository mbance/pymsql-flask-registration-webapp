#!/usr/bin/env python3

# import modules from Python Standard library
import cgi
import cgitb
cgitb.enable()

# import custom modules
from config import config
import utils
import components

# connect to a database
db = utils.db_connect( config )

# tell browser to expect HTML 
print("Content-Type: text/html\n")

# get any data sent with the GET or POST request
# this may be required by multiple components
sent_data = cgi.FieldStorage()

# -------- START OF FUNCTIONAL COMPONENTS ----------->>>

# ---------- HANDLE REGISTRATION FORM SUBMISSIONS ----------

# check if login form was submitted
if 'btn_register' in sent_data:
	# it was, so call the login function
	result = components.register(db, sent_data)
	msg = result['msg']
else:
	# message displayed in register form will be empty
	msg = ""

#render html document containing form
print( utils.render_html( config['HTML'] + 'register.html', data=[msg] ) )

# ---------- HANDLE REGISTRATION FORM SUBMISSIONS ERRORS -----------

# check if registered already
if 'btn_register' in sent_data:
	# student is already registered?
	result = components.register(db, sent_data['registered'].value = True)
	msg = "Student is already registered."

# --------- /END OF COMPONENTS --------
