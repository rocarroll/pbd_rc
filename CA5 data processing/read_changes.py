#########################################################
# B8IT105 Programming for Big Data						#
# Assignment 5 - Analysis on a 5000 line dataset		#
# Submitted by:											#
# Roisin Carroll (10361457)								#
#########################################################





import pandas as pd

def read_file(changes_file):
	# assigns the file 'changes_file' to the variable 'data' which is passed into the functions below
	# use strip to trim the lines and take out spaces. Data cut from 5255 to 422
	data = [line.strip() for line in open(changes_file,'r')]
	print(len(data))
	return data

def get_commits (data):
	# list of dictionaries with commit details. 
	# file is seperated by 72 '-'
	sep = 72*'-'				
	commits = []				
	current_commit = None
	index = 0

	while index < len(data):
		try:
			# seperate out each commit and put them in a list of commits. Seperate on '|'
			details = data[index+1].split(' | ')
			# seperate out full date from data
			full_datetime = data[index + 1].split('|')[2]
			# split the date and pull out the day. Keep the original full date. 
			weekday = full_datetime.split('(')[1].split(',')[0]
			# add the commit details to a dictionary. 
			commit = {'revision':details[0],'author':details[1],'lines':details[3].strip(' ')[0],
				'day':weekday,'datefull':details[2], }
			# add the dictionary to the list and return the list	
			commits.append(commit)
			index = data.index(sep, index+1)
			
		except IndexError:
			break
	return commits
		
def commits_per_day(data):	
	# dictionary with days of the week and total number of commits
	# eg active_days = {'mon':53, ' tue': 80}
	active_days = {}
	index = 0
	sep = 72*'-'
	
	while index < len(data):
		try:
			# seperates the full date from file eg '2005-11-27 16:57:44 +0000 (Fri,27 Nov 2015)'
			# pulls out just the day by splitting first on '(' then on ',' to give Mon etc
			details = data[index+1].split(' | ')
			full_datetime = data[index + 1].split('|')[2]
			weekday = full_datetime.split('(')[1].split(',')[0]
			
			# check if weekday is already in the dictionary
			if weekday not in active_days:
			# if not, add the weekday and set the number of commits to 1
				active_days[weekday] = 1
				# otherwise, increase the number of commits for this weekday by 1
			else:
				active_days[weekday] = active_days[weekday] + 1
			index = data.index(sep,index + 1)
		except IndexError:
			break
	print active_days
	return active_days


def get_authors(data):
	# dictionary with authors name as key and the total number of commits they've done as value
	# eg. authors = {'Thomas': 191, 'Vincent': 26}
	authors = {}
	index = 0
	sep = 72*'-'
	while index < len(data):
		try:
			# parse each of the authors and put them into a dictionary with the number of commits they've done
			# get the author name with spaces at end removed
			details = data[index+1].split( '|')
			author = details[1].strip()
			# check if author is already in the dictionary
			if author not in authors:
				authors[author]=1
				# if not, add the author and set the number of commits to 1
			else:
				# otherwise, increment the number of commits for this author
				authors[author] = authors[author]+1
			index = data.index(sep,index+1)
	
		except IndexError:
			break
	print authors
	return authors

def get_modifications(data):
	# dictionary of the number of modifications made. A is for Additions, D for deletions, M for modifications
	sep = 72*'-'
	modifications = {}
	index = 0
	while index < len(data):
		try:
			# go to the third line and split on '/' to get the A/M/D
			mod = data[index+3].split('/')[0]
			if mod not in modifications:
				modifications[mod]=1
			# add A/M or D to the dictionary and increment by 1 each time it appears
			else:
				modifications[mod] = modifications[mod]+1
			index = data.index(sep,index+1)
			
		except IndexError:
			break
	print modifications
	return modifications
	


	
#####################################################################################
## tried to get commits per hour but having problems

#def commits_per_hour(data)
#active_hours = {}
#index = 0

#while index < len(data):
	# dictionary with the hour as the key and number of commits as the values
	# eg active_hours = {'1':22, '2': 23}
	#	full_datetime = data[index + 1].split('|')[2]
	#	hours = full_datetime.split(' ')[2].split(':')[0]
	
	#	if hours not in active_hours:
	#		active_hours[hours] = 1
	#	else:
	#		active_hours[hours] = active_hours[hours]+1
		#	index = data.index(sep, index + 1)
	#except IndexError:
	#	break
#print active_hours
#######################################################################################



def output_CSV(s, filename):
	# function to convert a series or list of dicts to a dataframe and output to CSV
	df = pd.DataFrame(s)
	df.to_csv(filename)

if __name__ == '__main__' :
	# open the original file and read it in. Assign it to data and get the commits details.
	changes_file = 'changes_python.log'
	data = read_file(changes_file)
	commits = get_commits(data)
	print len(commits)
	
	# write out a CSV file with the commit details of Author Revision, Lines, Day and Full Date
	commits.reverse()
	output_file = 'changes3.csv'
	my_file = open(output_file, 'w')
	my_file.write('Revision,Author, Lines, Day, Date, \n') 
	for commit in commits:
		my_file.write(commit['revision']+','+ commit ['author']+ ','+ commit ['lines']+ ','+commit ['day']+','+ '"'+commit['datefull']+ ' "\n')
	my_file.close()
	

	
	 # output commits_per_day to a CSV file
	active_days = commits_per_day(data)
	s = pd.Series(active_days)
	output_CSV(s, 'active_days.csv')
	
	 # output author totals to a CSV file
	author_totals = get_authors(data)
	s = pd.Series(author_totals)
	output_CSV(s, 'author_totals.csv')
	
	# output modification totals to a CSV file
	modification_totals = get_modifications(data)
	s = pd.Series(modification_totals)
	output_CSV(s, 'modifications_totals.csv')
	
	
	
#read_file(changes_file)
#get_commits(data)
#commits_per_day(data)
#get_authors(data)
#get_modifications(data)

