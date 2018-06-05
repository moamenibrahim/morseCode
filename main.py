from app.functions import morseCodeDecode

def main():
        while True:        
                choice = input('Enter 1: encode to Morse, 2: decode to English, 3: create a file, 4: quit: ')

                if choice == '1':
                        while True:
                                output=''
                                file_to_read = input('Enter the file name you want to decode to Morse: ')
                                try:
                                        fread = open(file_to_read,"r")
                                except:
                                        print("Error: please enter the correct file name including the file extension")
                                        continue
                                try:
                                        for line in fread.readlines():
                                                line = line.replace("\n", "")
                                                line = line.replace(" ", "")
                                                output=output+morseCodeDecode.encodeToMorse(str(line))
                                        print(output)
                                        fread.close()
                                        if(morseCodeDecode.writeTofile(output,"output.txt")==True):
                                                print("Output successfully written to files")
                                        break
                                except Exception as KeyError:
                                        print("Error while processing file, please check the text in file and make sure it is in write format")

                elif choice == '2':
                        while True:
                                output=''
                                file_to_read = input('Enter the file name you want to encode to Morse: ')
                                try:
                                        fread = open(file_to_read,"r")
                                except:
                                        print("Error: please enter the correct file name including the file extension")
                                        continue
                                try:
                                        for line in fread.readlines():
                                                line = line.replace("\n", "")
                                                for word in line.split(" "):
                                                        word=word+' '
                                                        output=output+morseCodeDecode.decodeMorse(word)+' '
                                        print(output)
                                        fread.close()
                                        if(morseCodeDecode.writeTofile(output,"output.txt")==True):
                                                print("Output successfully written to files")
                                        break
                                except Exception as KeyError:
                                        print("Error while processing file, please check the text in file and make sure it is in write format")
                
                elif choice == '3':
                    file_name=input("Enter file name with extension: ")
                    string_to_file=input("Enter string to write to file: ")
                    if(morseCodeDecode.writeTofile(string_to_file,str(file_name))==True):
                            print("Output successfully written to files")

                elif choice == '4':
                    return False

                else:
                        print('Error: please enter a valid number')

if __name__ == "__main__":
        main()