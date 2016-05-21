#!/usr/bin/python

import sqlite3

#take in story id and return string of all lines for that story
def getPhoto(photo_id):
	conn = sqlite3.connect("hello.db", check_same_thread=False)
	c = conn.cursor()
	c.execute('SELECT photo FROM photos WHERE photo_id = ?;', (str(photo_id)))
	photo = c.fetchall()
	print photo
	story = []
	for i in photo:
		#print i
		story += [ i[0] ]
	conn.close()
	return  story
#testing - DONE
# print "testing getStory"
# print getPhoto(1) #returns all the lines
# print getStory(2) #return nothing :)

conn = sqlite3.connect('hello.db')

print "Opened database successfully";

conn.execute('''CREATE TABLE PHOTOS
       (ID INT PRIMARY KEY     NOT NULL,
       PHOTO          BLOB    NOT NULL);''')

print "Table created successfully";

conn.close()
