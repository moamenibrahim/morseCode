import sys
from codes import CODE,inverseCODE

class morseCodeDecode(object):

        # parse a morse code string positionInString is the starting point for decoding
        def decodeMorse(code, positionInString = 0):
                letter=''
                if positionInString < len(code):
                        morseLetter = ""
                        for key,char in enumerate(code[positionInString:]):
                                if char == " ":
                                        positionInString = key + positionInString + 1
                                        try:
                                                letter = inverseCODE[morseLetter]
                                        except:
                                                print("Couldn't find that input in morse code list")
                                        return str(letter) + morseCodeDecode.decodeMorse(code, positionInString)
                                else:
                                        morseLetter += char

                else:
                        return ""

        #encode a message in morse code, spaces between words are represented by '/'
        def encodeToMorse(message):
                encodedMessage = ""
                for char in message[:]:
                        encodedMessage += CODE[char.upper()] + " "
                return encodedMessage


        def writeTofile(output_of_morse,fileName):
                try:
                        fwrite = open(fileName,"+w")
                        fwrite.write(output_of_morse)
                        fwrite.close()
                except:
                        return False
                return True

