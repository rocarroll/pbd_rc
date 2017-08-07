
####################################################################################
#                           Active Days
####################################################################################

# load in the active days CSV file and set col headings
mydata <- read.csv('active_days.csv', header = TRUE, col.names = c("Day","NbrCommits"))
fix(mydata)

#create vectors for the days and the number of commits
days <- mydata$Day
commits <- mydata$NbrCommits

# give the bar chart file a name
png(file = 'barchart_active_days.png')

# plot the bar chart
barplot(commits,names.arg = days,xlab = "Weekday",ylab = "Number of Commits",col = "blue",
        main = "Active Days",border = "red")

# save the file
dev.off()

####################################################################################
#                           Author Totals
####################################################################################

# load in the author totals CSV file and set col headings
mydata <- read.csv('author_totals.csv', header = TRUE, col.names = c("Author","NbrCommits"))
fix(mydata)

#create vectors for the authors and the number of commits
authors <- mydata$Author
authors <- gsub('/OU=Domain Control Validated/CN=svn.company.net','System', authors)
commits <- mydata$NbrCommits

# give the bar chart file a name
png(file = 'barchart_author_commits.png')

# plot the bar chart
barplot(commits,names.arg = authors,xlab = "Author",ylab = "Number of Commits",las=2, col = "blue",
        main = "Commits by Author",border = "red")

# save the file
dev.off()


####################################################################################
#                           Types of commits
####################################################################################

# load in the modifications totals CSV file and set col headings
mydata <- read.csv('modifications_totals.csv', header = TRUE, col.names = c("Type of Commit","NbrCommits"))
fix(mydata)

# give the bar chart file a name
png(file = 'barchart_modifications.png')

#create vectors for the type and the number of commits
type <- mydata$Type
commits <- mydata$NbrCommits

# plot the bar chart
barplot(commits,names.arg = type, xlab = "Type of Modifications",ylab = "Number of Commits",col = "blue",
        main= "types of commits: A =Addition, D = Deletion, M = Modification")

# save the file
dev.off()

