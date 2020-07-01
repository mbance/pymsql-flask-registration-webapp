"""
	This module contains some test functions that
	can be called to check if a certain component
	is doing what we expect it to do
"""

from config import config
import utils
import components

def test_connect_db( config ):
	db = utils.db_connect( config )
	print(db)
	if db:
		print("Connected to database. Trying to get a document...")
		doc = db.mbanc001.find_one({})
		if doc:
			#print( doc )
			print("PASS: db_connect")
	else:
		print("Error in db_connect. No handle returned.")
	

# run tests...
test_connect_db(config)
