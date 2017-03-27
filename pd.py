#!/usr/bin/python2
# coding=UTF-8

####
# Author: Anita Ullrich
####

########################
#INFORMATION FOR THE DATABASE: (pgadminIII)
#Neue Login-Rolle: 'user' mit Passwort: 'p4ssw9rd'
#Tabelle 'special_dates' mit Eigentümer 'user' und
#folgenden Angaben:
# -- Table: public.special_dates
#
# -- DROP TABLE public.special_dates;
#
# CREATE TABLE public.special_dates
# (
#   date date NOT NULL,
#   event character varying NOT NULL, -- what happens on this date????
#   reminder character varying, -- the text that should remind you forr this event
#   CONSTRAINT pk_date_event PRIMARY KEY (date, event)
# )
# WITH (
#   OIDS=FALSE
# );
# ALTER TABLE public.special_dates
#   OWNER TO "user";
# COMMENT ON COLUMN public.special_dates.event IS 'what happens on this date????';
# COMMENT ON COLUMN public.special_dates.reminder IS 'the text that should remind you forr this event';
#
#Dann noch Events hinzufügen.
########################


import datetime

#for PostgreSQL:
import records

#for the time of the last file-change:
import os

import random

def random_color() :
	color = random.randint(50,255)
	return color


def does_file_exist(fln) :
	if not os.path.isfile(fln) :
		file = open(fln, "w")
		file.close()
	return 0

def actual_date() :
	now = datetime.date.today()
	return now

#creates a list of all the events at the actual_date
def date_to_reminder_list(today) :
	db = records.Database('postgres://localhost/pddb?user=user&password=p4ssw9rd')
	reminder_list = db.query("select reminder from special_dates where date = '%s' \
		or date = '0001-%s' or date = '0002-01-%s' or date = '0003-01-01'" %(str(today),str(today)[5:],str(today)[8:]))

	return reminder_list


#write the reminders in a document
#gets reminder_list, filename
def reminder_writer(r_list, fln) :
	file = open(fln, "w")
	#HIER w NICHT r??

	#create a list with all lines, i want to write
	str_list = []
	str_list.append(str(0))
	for item in r_list :
		str_list.append("\n" + item['reminder'])

	file.write("".join(str_list))
	file.close()

#reads the now wanted line, to put this on the statusbar
def readout(fln) :
	file = open(fln, "r")
	message = "Try again tomorrow"
	lines = file.readlines()

	if lines[0] != "0":

		#the current number of the line i want:
		current_nmbr = int(lines[0])
		#create a list of the lines
		if len(lines) > current_nmbr :
			if current_nmbr == len(lines) - 2 :
				message = lines[current_nmbr+1]
			else :
				message = lines[current_nmbr+1]
				message = message[:-1]
				#if the line is not the last one, you need to delete the last
				#sign in that line, because we don't want a \n

	file.close()
	return message

def execute(fln) :
	file = open(fln, "r")
	if file.readline() != "" :
		file.close()
		scds = os.path.getmtime(fln)
		#file is changed today,
		#if seconds are more than today at midnight
		d = datetime.datetime(actual_date().year, actual_date().month, actual_date().day, 0, 0)

		if scds >= d.timestamp() :
			file = open(fln, "r")
			cr_nmbr = int(file.readline())
			lines = file.readlines()

			file.close()

			newfile = open(fln, "w")
			ap_list = []

			#if the number will give the last remainder,
			#we have to set it down to zero again.
			#otherwise we count it up.

			if cr_nmbr == len(lines)-1 :
				cr_nmbr = 0
			else :
				cr_nmbr += 1

			ap_list.append(str(cr_nmbr) + "\n")
			for i in range(0,len(lines)) :
				ap_list.append(lines[i])

			newfile.write("".join(ap_list))
			newfile.close()

		else :
			reminder_writer(date_to_reminder_list(actual_date()), fln)

	#file didn't change today, so it's from yesterday
	else :
		reminder_writer(date_to_reminder_list(actual_date()), fln)

	return readout(fln)

if __name__ == "__main__" :
	does_file_exist("/tmp/pd_tmp.txt")
	r = random_color()
	s = random_color()
	t = random_color()
	print("<span color='" + "#%02X%02X%02X" %(r,s,t) + "'>" + execute("/tmp/pd_tmp.txt") + "</span>")
