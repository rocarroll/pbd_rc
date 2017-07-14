changes_file = 'changes_python.log'
	
data = [line.strip() for line in open(changes_file,'r')]

print(len(data))

sep = 72*'-'
	#parse each of the commits and put them into a list of commits	
	# the author with teh spaces at end removed. 
	
commits = []
current_commit = None
index = 0

while index < len(data):
	try:
		details = data[index+1].split(' | ')
		#print details
		commit = {'revision':details[0],'author':details[1],
			'date':details[2]}
		commits.append(commit)
		index = data.index(sep, index+1)
		
	except IndexError:
		break
print len(commits)

commits.revers()
output_file = 'changes.csv'
my_file = open(output_file, 'w')
my_file.write('Revision,Author,Date \n') 
for commit in commits:
	my_file.write(commit['revision']+','+ commit ['author']+',"'+commit['date'] + '"\n')
my_file.close()
