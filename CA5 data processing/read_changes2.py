
def read_file(changes_file):
	data = [line.strip() for line in open(changes_file,'r')]
	print(len(data))
	return data

def get_commits (data):
	sep = 72*'-'
	#parse each of the commits and put them into a list of commits	
	# the author with teh spaces at end removed. 
	
	commits = []
	current_commit = None
	index = 0

	while index < len(data):
		try:
			details = data[index+1].split(' | ')
			full_datetime = data[index + 1].split('|')[2]
			weekday = full_datetime.split('(')[1].split(',')[0]
			
			#print details
			
			commit = {'revision':details[0],'author':details[1],'lines':details[3].strip(' ')[0],
				'day':weekday,'datefull':details[2], }
				
			commits.append(commit)
			index = data.index(sep, index+1)
			
		except IndexError:
			break
	return commits
		
def commits_per_day(data):		
	active_days = {}
	index = 0

	while index < len(data):
		# dictionary with days of the week and total number of commits
		# eg active_days = {'mon':53, ' tue': 80}
		try:
			# seperates the full date from file eg '2005-11-27 16:57:44 +0000 (Fri,27 Nov 2015)'
			# pulls out just the day by splitting first on '(' then on ',' to give Mon etc
			full_datetime = data[index + 1].split('|')[2]
			weekday = full_datetime.split('(')[1].split(',')[0]
			
			# check if weekday is already in the dictionary
			if weekday not in active_days:
			# if not, add the weekday and set the number of commits to 1
				active_days[weekday] = 1
				# otherwise, increase the number of commits for this weekday by 1
			else:
				active_days[weekday] = active_days[weekday] + 1
			index = data.index(sep, index + 1)
		except IndexError:
			break
	print active_days
	return active_days


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
	
	
	
if __name__ == '__main__':
	changes_file = 'changes_python.log'
	data = read_file(changes_file)
	commits = get_commits(data)
	print len(commits)
	commits.reverse()
	output_file = 'changes3.csv'
	my_file = open(output_file, 'w')
	my_file.write('Revision,Author, Lines, Date, Date_detail, \n') 
	for commit in commits:
		my_file.write(commit['revision']+','+ commit ['author']+ ','+ commit ['lines']+ ','+commit ['day']+','+ '"'+commit['datefull']+ ' "\n')
	my_file.close()
