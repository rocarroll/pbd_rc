
class SpellChecker(object):

    def __init__(self):
        self.words = []

    def load_file(self, file_name):
        lines = open(file_name).readlines()
        return map(lambda x: x.strip().lower(), lines)

    def load_words(self, file_name):
        self.words = self.load_file(file_name)

    def check_word(self, word):
        return word.strip('.,()/').lower() in self.words

    # index = 0 is set here so that the function can be called for one line and index defaults to 0
    def check_words(self, sentence, index = 0):
        words_to_check = sentence.split(' ')
        caret_position = 0
        failed_words = []
        for word in words_to_check:
            if not self.check_word(word):
                print('Word is misspelt ' + word + ' at line : ' + str(index+1) + ' pos ' + str(caret_position+1))
                failed_words.append({'word':word,'line':index+1,'pos':caret_position+1})
            # update the caret position to be the length of the word plus 1 for the split character.
            caret_position = caret_position + len(word) + 1
        return failed_words 

    def check_document(self, file_name):
        self.sentences = self.load_file(file_name)
        failed_words_in_sentences = []
        for index, sentence in enumerate(self.sentences):
            failed_words_in_sentences.extend(self.check_words(sentence, index))
        return failed_words_in_sentences

