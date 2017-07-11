import unittest

from spellcheck import SpellChecker

class TestSpellChecker(unittest.TestCase):

    def setUp(self):
        self.spellChecker = SpellChecker()
        self.spellChecker.load_words('spell.words')
		
    def test_spell_checker(self):
        self.assertTrue(self.spellChecker.check_word('zygotic'))
        failed_words = self.spellChecker.check_words('zygotic mistasdas elementary')
        self.assertEquals(1, len(failed_words))
        self.assertEquals('mistasdas', failed_words[0]['word'])
        self.assertEquals(1, failed_words[0]['line'])
        self.assertEquals(9, failed_words[0]['pos'])
        self.assertEquals(0, len(self.spellChecker.check_words('our first correct sentence')))
        # handle case sensitivity
        self.assertEquals(0, len(self.spellChecker.check_words('Our capital sentence')))
        # handle full stop
        self.assertEquals(0, len(self.spellChecker.check_words('Our full stop sentence.')))
        failed_words = self.spellChecker.check_words('zygotic mistasdas spelllleeeing elementary')
        self.assertEquals(2, len(failed_words))
        self.assertEquals('mistasdas', failed_words[0]['word'])
        self.assertEquals(1, failed_words[0]['line'])
        self.assertEquals(9, failed_words[0]['pos'])
        self.assertEquals('spelllleeeing', failed_words[1]['word'])
        self.assertEquals(1, failed_words[1]['line'])
        self.assertEquals(19, failed_words[1]['pos'])
        self.spellChecker.check_document('stuff.txt')
        #self.assertEqual(0, len(self.spellChecker.check_document('spell.words')))
		#self.assertEquals(11, len(self.spellChecker.check_document('stuff.txt')))  
        #self.assertEquals(0, len(self.spellChecker.check_document('stuff.txt')))  
if __name__ == '__main__':
    unittest.main()

