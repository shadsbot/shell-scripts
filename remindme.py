#!/usr/bin/env python

# Requires: Python (duh), PyMsgBox, sox, xmpppy, simplexml

import os
import sys
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import datetime as dt
from pymsgbox import *

# Load configurations
server_smtp= 'smtp.gmail.com'
server_port= 587
email= ""
email_pass= ""
triggered= False


reminder = sys.argv[2]

smtpserver = smtplib.SMTP(server_smtp,server_port)

#######################

# Handle time manipulation to get the seconds
def getSeconds( itime ):
	stopme = 0
	# b = datetime.then()
	# c = (b-a).total_seconds()
	# return c
	a = dt.datetime.now()
	b = "Something went wrong!"
	if "TOMORROW" in itime.upper():
		b = a
		b += dt.timedelta(days = 1)
		stopme = 1
	elif itime.upper() in ("MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY","SUNDAY","MON","TUE","WED","THU","FRI","SAT","SUN"):
		# Remember - Monday: 0, Sunday: 6
		b = a
		stopme = 1
		mod = 0
		if itime.upper() in ("MONDAY","MON"):
			mod = 0
		elif itime.upper() in ("TUESDAY","TUE"):
			mod = 1
		elif itime.upper() in ("WEDNESDAY","WED"):
			mod = 2
		elif itime.upper() in ("THURSDAY", "THU"):
			mod = 3
		elif itime.upper() in ("FRIDAY", "FRI"):
			mod = 4
		elif itime.upper() in ("SATURDAY", "SAT"):
			mod = 5
		elif itime.upper() in ("SUNDAY", "SUN"):
			mod = 6

		while (b.weekday() != mod):
			b += dt.timedelta(days = 1)
		
	elif itime.upper() in "NOW":
		return 1
	if stopme == 0:	
		if "S" in itime.upper() or "SECONDS" in itime.upper():
			b = int(itime[:itime.upper().index('S')])
			return b
		if ("M" in itime.upper() or "MINUTES" in itime.upper() or "MINUTE" in itime.upper()) and not "PM" in itime.upper() and not "AM" in itime.upper() and not "H" in itime.upper():
			b = int(itime[:itime.upper().index('M')])*60
			return b
		if "H" in itime.upper() or "HOUR" in itime.upper() or "HOURS" in itime.upper() and not "M" in itime.upper():
			b = int(itime[:itime.upper().index('H')])*60*60
			return b
		if "H" in itime.upper() and ("M" in itime.upper() and not "A" in itime.upper() and not "P" in itime.upper()):
			h = int(itime[:itime.upper().index('H')])
			mm = itime[:itime.upper().index('M')]
			m = int(mm[m.upper().index("H")+1:])
			h = h*60*60
			m = m*60
			return h+m
		if len(itime) < 8:
			if len(itime) >= 6:
				b = dt.datetime.strptime(itime, '%I:%M%p')
				b = b.replace(year = dt.datetime.now().year)
				b = b.replace(month = dt.datetime.now().month)
				b = b.replace(day = dt.datetime.now().day)
			if len(itime) == 5:
				b = dt.datetime.strptime(itime, '%H:%M')
				b = b.replace(year = dt.datetime.now().year)
				b = b.replace(month = dt.datetime.now().month)
				b = b.replace(day = dt.datetime.now().day)
	c = (b-a).total_seconds()
	# So seconds
	return c
# Wait it out
def procedure(protime):
	if protime > 0:
		time.sleep(protime)
	else:
		playTone()
		alert(text="Erm... The time needs to be in the future... Spitting out your reminder now:\n\n" + sys.argv[2], title='Reminder!', button='OK, sorry!')
		sys.exit(1)

def signin():
	# You may need to go to accounts.google.com/DisplayUnlockCaptcha the first time
	smtpserver.starttls()
	smtpserver.ehlo()
	try:
		smtpserver.login(email,email_pass)
	except:
		playTone()
		print("[!] Something went wrong - did you set up email correctly?")
def signal(type, to):
	if type.upper() == "EMAIL":
		signin()
		msg = MIMEMultipart()
		msg['From'] = gmail
		msg['To'] = to
		msg['Subject'] = "Remindme: "+reminder[:10]+"..."
		msg.attach(MIMEText(reminder))
		msg.attach(MIMEText("\n\nSent (with love) from RemindMe"))
		try:
			smtpserver.sendmail(email,to,msg.as_string())
		except ValueError:
			alert(text="[!!] FATAL ERROR: COULDN'T SEND EMAIL",title="ERROR",button="OK")
		smtpserver.close()
	else:
		pass # planned feature?
def playTone():
	"Middle C is 523 Hz"
	os.system('play --no-show-progress --null --channels 1 synth .1 sine 523')
	os.system('play --no-show-progress --null --channels 1 synth .1 sine 423')
	# play(.1,523)

# Main stuff is here
try:
	sys.argv[3]
except:
	# No email/XMPP
	return c
# Wait it out
def procedure(protime):
	if protime > 0:
		time.sleep(protime)
	else:
		playTone()
		alert(text="Erm... The time needs to be in the future... Spitting out your reminder now:\n\n" + sys.argv[2], title='Reminder!', button='OK, sorry!')
		sys.exit(1)

def signin():
	# You may need to go to accounts.google.com/DisplayUnlockCaptcha the first time
	smtpserver.starttls()
	smtpserver.ehlo()
	try:
		smtpserver.login(email,email_pass)
	except:
		playTone()
		print("[!] Something went wrong - did you set up email correctly?")
def signal(type, to):
	if type.upper() == "EMAIL":
		signin()
		msg = MIMEMultipart()
		msg['From'] = gmail
		msg['To'] = to
		msg['Subject'] = "Remindme: "+reminder[:10]+"..."
		msg.attach(MIMEText(reminder))
		msg.attach(MIMEText("\n\nSent (with love) from RemindMe"))
		try:
			smtpserver.sendmail(email,to,msg.as_string())
		except ValueError:
			alert(text="[!!] FATAL ERROR: COULDN'T SEND EMAIL",title="ERROR",button="OK")
		smtpserver.close()
	else:
		pass # planned feature?
def playTone():
	"Middle C is 523 Hz"
	os.system('play --no-show-progress --null --channels 1 synth .1 sine 523')
	os.system('play --no-show-progress --null --channels 1 synth .1 sine 423')
	# play(.1,523)

# Main stuff is here
try:
	sys.argv[3]
except:
	# No email/XMPP
	procedure(getSeconds(sys.argv[1]))
	playTone()
	alert(text=reminder,title='Reminder!',button='OK')
else:
	#Email or XMPP
	if not triggered:
		print('''[!] Please note: 
		Email was kind of a challenge for me to program, so 
		there's a very good chance that I messed something up.
		Please please please test the configuration for errors 
		before using it! I don't want you to not get something 
		important because of this...

		This message will only appear once.
		''')
		#with open(sys.path.append(os.path.dirname(os.path.expanduser(configfile))),'r') as file:
		#	data = file.readlines()
		#data[5] = "triggered = True"
		#with open(sys.path.append(os.path.dirname(os.path.expanduser(configfile))),'w') as file:
		#	file.writelines(data)
	procedure(getSeconds(sys.argv[1]))
	signal(sys.argv[3],sys.argv[4])

sys.exit(0)
