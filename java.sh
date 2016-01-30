#!/bin/bash

# Java version finder v0.1 by Colin Diener
# Last updated 28/1/2016, released under GNU General Public License v3.0

# Output should be something like 8 update 71
CURRENTVERSION=$(curl https://www.java.com/en/download/manual.jsp | grep "Recommended Version" | sed 's/<h4 class=\"sub\">Recommended Version //g' | sed 's/<\/h4>//g' | sed 's/\n//')

# Test to see if the reference file exists
if [ -e current_java_version ] ; then
	RECORDVERSION=$(cat current_java_version)
	if [ "$CURRENTVERSION" != "$RECORDVERSION" ]; then
		# Cool! There's a new version of Java. Let's let someone know
		# This someone needs to be passed into the script, replace $1 for hardcode
		mail -s "New Java!" "$1" <<- EOF
		Hey there!
		This is to let you know that on $(date) we found that java updated!
		Old version:
		$RECORDVERSION 
		New version:
		$CURRENTVERSION
		Feel free to grab it over at https://www.java.com/en/download/manual.jsp
		EOF
		echo "$CURRENTVERSION" > current_java_version
	fi
else
	# It doesn't exist, create one, populate
	touch current_java_version
	echo "$CURRENTVERSION" > current_java_version
fi
