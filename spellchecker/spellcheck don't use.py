## spellchecker

words = open("spell.words").readlines()

words = map(lambda x: x.strip(), words)
print len(words)
print words[0]
print words[len(words)-1]

print ('zygotic' in words)
print ('misdasdas' in words)

def load_words(file_name):
	words = open(file_name).readlines()
	words = map(lambda x: x.strip(), words)
	return words

def check_word(words,word):
	return word in words
	
def check_words(words,senteance):
	words_to_check = senteance.split(' ')
	failed_words = []
	for word in words_to_check:
		if not check_word(words,word):
			print ("Word is misspelt : " + word)
			failed_words.append(word)
	return failed_words
	
print load_words("spell.words") [0]

print check_word(words, 'zygotic')
print check_word(words, 'mistasdas')
print (check_words(words,'zygotic mistasdas elementary'))
