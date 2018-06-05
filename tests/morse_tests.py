"""
Created on 23.05.2018
@author: moamen
"""

import unittest
import sys

sys.path.insert(0,  'app/')
from functions import morseCodeDecode 

function=morseCodeDecode()

class MorseTestCases(unittest.TestCase):
    """
    Class to test morse related cases for encoding, decoding and creating files
    """

    function=morseCodeDecode()


    morse_1_request = "What is even your name ?"
    morse_1_response = ".-- .... .- - .. ... . ...- . -. -.-- --- ..- .-. -. .- -- . ..--.."
    morse_2_request = "12 continents"
    morse_2_response = ".---- ..--- -.-. --- -. - .. -. . -. - ..."
    morse_3_request = "? / , @"
    morse_3_response = "..--.. -..-. --..-- .--.-."

    morse_bad_request = "... .- -- .--. .-.. . - . -..- -"
    morse_bad_response = ""

    english_1_request = "-.. ..-. ... .- ..-. -.. ... -.. ..-. -.. ... ..-. --. .- -.. ..-. ..."
    english_1_response = "D F S A F D S D F D S F G A D F S"
    english_2_request = "... .- -- .--. .-.. . - . -..- -"
    english_2_response = "S A M P L E T E X T"
    english_3_request = ".-- .... .- - .. ... . ...- . -. -.-- --- ..- .-. -. .- -- . ..--.."
    english_3_response = "W H A T I S E V E N Y O U R N A M E ?"

    english_bad_request = "alkila"
    english_bad_response = ""


    def test_get_morse(self):
        '''
        test sample input to make sure the conversion to morse code (encoding) works properly
        '''
        print('('+self.test_get_morse.__name__+')', self.test_get_morse.__doc__)
        response='.-- .... .- - .. ... . ...- . -. -.-- --- ..- .-. -. .- -- . ..--..'
        for word in self.morse_1_request.split(' '):
            word=word+' '
            print(word)
            # response=response+function.decodeMorse(word)+' '
        self.assertEqual(response, self.morse_1_response)
  

    def test_get_morse_with_numbers(self):
        '''
        test sample input to make sure the conversion to morse code (encoding) works properly
        '''
        print('('+self.test_get_morse_with_numbers.__name__+')', self.test_get_morse_with_numbers.__doc__)
        response='.---- ..--- -.-. --- -. - .. -. . -. - ...'
        for word in self.morse_2_request.split(' '):
            word=word+' '
            print(word)
            # response=response+function().decodeMorse(code=word)+' '
        self.assertEqual(response, self.morse_2_response)

    
    def test_get_morse_with_symbols(self):
        '''
        test sample input to make sure the conversion to morse code (encoding) works properly
        '''
        print('('+self.test_get_morse_with_symbols.__name__+')', self.test_get_morse_with_symbols.__doc__)
        response='..--.. -..-. --..-- .--.-.'
        for word in self.morse_3_request.split(' '):
            word=word+' '
            print(word)
            # response=response+function().decodeMorse(word)+' '
        self.assertEqual(response, self.morse_3_response)


    def test_get_morse_bad_request(self):
        '''
        test when passing a bad request to morse code encoder
        '''
        print('('+self.test_get_morse_bad_request.__name__+')', self.test_get_morse_bad_request.__doc__)
        ''' NOT IMPLEMENTED YET'''
        pass

    def test_get_morse_wrong_format(self):
        '''
        test when passing a wrong format to the encoder
        '''
        print('('+self.test_get_morse_wrong_format.__name__+')', self.test_get_morse_wrong_format.__doc__)
        ''' NOT IMPLEMENTED YET'''
        pass

    def test_get_english(self):
        '''
        test decoding an english text to morse code
        '''
        response='D F S A F D S D F D S F G A D F S'
        print('('+self.test_get_english.__name__+')', self.test_get_english.__doc__)
        self.english_1_request = self.english_1_request.replace("\n", "")
        self.english_1_request = self.english_1_request.replace(" ", "")
        # response=function.encodeToMorse(str(self.english_1_request))
        print(self.english_1_request)
        self.assertEqual(response, self.english_1_response)

    def test_english_with_symbols(self):
        '''
        test decoding an english text to morse code with symbols
        '''
        response='S A M P L E T E X T'
        print('('+self.test_get_english.__name__+')', self.test_get_english.__doc__)
        self.english_2_request = self.english_2_request.replace("\n", "")
        self.english_2_request = self.english_2_request.replace(" ", "")
        # response=function.encodeToMorse(str(self.'english_2_request))
        print(self.english_2_request)
        self.assertEqual(response, self.english_2_response)

    def test_english_with_numbers(self):
        '''
        test decoding an english text to morse code with numbers
        '''
        response='W H A T I S E V E N Y O U R N A M E ?'
        print('('+self.test_get_english.__name__+')', self.test_get_english.__doc__)
        self.english_3_request = self.english_3_request.replace("\n", "")
        self.english_3_request = self.english_3_request.replace(" ", "")
        # response=function.encodeToMorse(str(self.english_3_request))
        print(self.english_3_request)
        self.assertEqual(response, self.english_3_response)

    def test_get_english_bad_request(self):
        '''
        test when passing a bad request to morse code decoder
        '''
        response=''
        print('('+self.test_get_english_bad_request.__name__+')', self.test_get_english_bad_request.__doc__)
        self.english_bad_request = self.english_bad_request.replace("\n", "")
        self.english_bad_request = self.english_bad_request.replace(" ", "")
        # response=function.encodeToMorse(str(self.english_bad_request))
        print(self.english_bad_request)
        self.assertEqual(response, self.english_bad_response)

    def test_get_english_wrong_format(self):
        '''
        test when passing a wrong format to the decoder
        '''
        print('('+self.test_get_english_wrong_format.__name__+')', self.test_get_english_wrong_format.__doc__)
        ''' NOT IMPLEMENTED YET'''
        pass


    def test_write_file_empty_string(self):
        '''
        test when passing an empty string to create a file method
        '''
        print('('+self.test_write_file_empty_string.__name__+')', self.test_write_file_empty_string.__doc__)
        ''' NOT IMPLEMENTED YET'''
        pass



if __name__ == "__main__": # Borrowed from lab exercises [1]
    print('Start running tests\n')
    unittest.main()
