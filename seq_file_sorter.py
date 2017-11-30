#!/usr/bin/env python 

# Navigate to file in teriminal 
# type: chmod u+x py_file_sorter.py
# set the open with to Terminal
import os
import re
import sys

# changes current working directory to location of file
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# creates the ab1 and seq directories
if not os.path.exists('ab1'):
	os.makedirs('ab1')

if not os.path.exists('seq'):
	os.makedirs('seq')


# regex for quintara (.*)(_\d{4}-\d{2}-\d{2}_[a-hA-H]\d*)(.(ab1|seq))
# removes the leading junk added on by ELIM or Quintara to sequence files and moves to useful folders.
try:
	for filename in os.listdir("."):
		if '.ab1' in filename or '.seq' in filename:  # not sure if I need this, I will have to check
			
			# for this regx(ELIM):
			# ([A-Z]+_[0-9]+-[0-9]+_)(.*)(_[A-H]{1}[0-9]{2}(.ab1|seq))
			# |-group1------|--group2---------|-g3|-g4
			#									   |g5
			# JL_470815-501_US_NDT80_pUC-Seq-F_A12.ab1
			if re.search('([A-Z]+_[0-9]+-[0-9]+_)(.*)([-|_][A-Z]+[0-9]+)(.(ab1|seq))',filename):
				parsed_name = re.search('([A-Z]+_[0-9]+-[0-9]+_)(.*)([-|_][A-Z]+[0-9]+)(.(ab1|seq))',filename).group(2,4,5) # group returns a tuple based on items in regex ()
				os.rename(filename, parsed_name[2]+'/'+''.join(parsed_name[:2]))
			# Quintara
			# (.*)(_\d{4}-\d{2}-\d{2}_[a-hA-H]\d*)(.(ab1|seq))
			# |-g1---|--g2----------|g3-
			#						 |g4
			# H1_JL62_2017-01-20_E06.ab1

			elif re.search('(.*)(_\d{4}-\d{2}-\d{2}_[a-hA-H]\d*)(.(ab1|seq))',filename):
				parsed_name = re.search('(.*)(_\d{4}-\d{2}-\d{2}_[a-hA-H]\d*)(.(ab1|seq))', filename).group(1,3,4)
				os.rename(filename,parsed_name[2]+'/'+''.join(parsed_name[:2]))

			else:
				print('File type could not be identified, script is currently setup to parse file names from Quintara and ELIM as of 1/20/2017')
				break
				
	print("Files sorted, enjoy!")
except:
	print("There was an error, probably because the files were not formated as expected. Only ELIM and Quintara formats as of Jan 2017 are accepted")
	# I know this is not true error handling
	# this mainly gets past when prefix_len is None and you can't parse the name
	# I think this will mostly happen if the script runs twice.
	pass

def yes_or_no(question):
	if sys.version_info < (3,0):
		reply = raw_input( question +' (y/n): ').lower().strip()
	else:
		reply = input( question +' (y/n): ').lower().strip()
	if reply[0] == 'y':
		return True
	if reply[0] == 'n':
		return False
	else:
		return yes_or_no("please enter y/n only")

move_file = yes_or_no("Should I move myself to the Desktop?")

file_name = os.path.basename(__file__)
current_location = os.path.dirname(os.path.realpath(__file__))

if move_file is True:
	os.rename(current_location+'/'+file_name, os.path.expanduser("~/Desktop/")+file_name)	
	

