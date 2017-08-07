import unittest

from read_changes import read_file, get_commits, commits_per_day, get_authors, get_modifications

class TestCommits(unittest.TestCase):

    def setUp(self):
        #runs at the very start, reads in the file so all other tests can use it
        self.data = read_file('changes_python.log')

    def test_number_of_lines(self):
        self.assertEqual(5255, len(self.data))

    def test_number_of_commits(self):
        commits = get_commits(self.data)
        self.assertEqual(422, len(commits))

    def test_first_commit(self):
        commits = get_commits(self.data)
        self.assertEqual('Thomas', commits[0]['author'])
        self.assertEqual('r1551925', commits[0]['revision'])
        
    def test_author_totals(self):
        author_totals = get_authors(self.data)
        self.assertEqual(10, len(author_totals))
        self.assertEqual(191, author_totals['Thomas'])
        
    def test_number_of_active_days(self):
        active_days = commits_per_day(self.data)
        self.assertEqual(5, len(active_days))
        self.assertEqual(95, active_days['Fri'])

    def test_number_of_authors(self):
        authors = get_authors(self.data)
        self.assertEqual(10, len(authors))
       
	def test_number_of_modifications(self):
		mod = get_modifications(self.data)
		self.assertEqual(422, len(mod))
		self.asserEqual(48,mod['A'])
        

  
        
if __name__ == '__main__':
	unittest.main()