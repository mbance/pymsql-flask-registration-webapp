#!/usr/bin/env python3

# import modules from Python standard library
import cgi
import cgitb
cgitb.enable()

# import custom modules
from config import config
import utils
import components

# connect to database
db = utils.db_connect( config )

# tell the browser we are outputting HTML
print("Content-Type: text/html\n")

# get the form data
form = cgi.FieldStorage()

# check that register form was submitted
if 'btn_register' in form:
	result = components.register( db, form )
	msg = result['msg']
else:
	msg = ""

# output the form as HTML
print( utils.render_html( config['HTML'] + 'register.html', data=[msg] ) )
