import tkinter as tk
from tkinter import *
from app.functions import morseCodeDecode

class MainGUI:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.button1 = tk.Button(self.frame, text = 'encode English to Morse', width = 25, command = self.encodeWindow)
        self.button1.pack()
        self.button2 = tk.Button(self.frame, text = 'decode Morse to English', width = 25, command = self.decodeWindow)
        self.button2.pack()
        self.button3 = tk.Button(self.frame, text = 'create new file', width = 25, command = self.writeTofileWindow)
        self.button3.pack()
        self.button4 = tk.Button(self.frame, text = 'close', width = 25, command = self.close_windows)
        self.button4.pack()
        self.frame.pack()

    def encodeWindow(self):
        self.encodeWindow = tk.Toplevel(self.master)
        self.app = encodeGUI(self.encodeWindow)

    def decodeWindow(self):
        self.decodeWindow = tk.Toplevel(self.master)
        self.app = decodeGUI(self.decodeWindow)

    def writeTofileWindow(self):
        self.writeTofileWindow = tk.Toplevel(self.master)
        self.app = writeTofileGUI(self.writeTofileWindow)

    def close_windows(self):
        self.master.destroy()

class encodeGUI:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.var = StringVar()
        self.label = Label(self.master, textvariable=self.var, relief=RAISED )
        self.var.set("Enter the file name you want to encode to Morse")
        self.label.pack()
        self.T = Text(self.master, height=2, width=30)
        self.T.pack()
        self.T.insert(END, "input.txt")
        self.quitButton = tk.Button(self.frame, text = 'OK', width = 25, command = self.mainFunc)
        self.quitButton.pack()
        self.frame.pack()

    def retrieve_input(self):
        input = self.T.get("1.0",'end-1c')
        return input

    def close_windows(self):
        self.master.destroy()

    def mainFunc(self):
            output=''
            file_to_read = self.retrieve_input()
            try:
                    fread = open(file_to_read,"r")

            except:
                    toplevel = Toplevel()
                    label1 = Label(toplevel, text="Error: please enter the correct file name including the file extension", 
                                        height=0)
                    label1.pack()
                    self.close_windows()
                    return

            try:
                for line in fread.readlines():
                        line = line.replace("\n", "")
                        line = line.replace(" ", "")
                        output=output+morseCodeDecode.encodeToMorse(str(line))
                print(output)
                fread.close()
                if(morseCodeDecode.writeTofile(output,"output.txt")==True):
                        toplevel = Toplevel()
                        label1 = Label(toplevel, text="Output successfully written to files", 
                                            height=0)
                        label1.pack()
                        self.close_windows()
                        return

            except Exception as KeyError:
                toplevel = Toplevel()
                label1 = Label(toplevel, text="Error while processing file, please check the text in file and make sure it is in write format", 
                                    height=0)
                label1.pack()

class decodeGUI:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.var = StringVar()
        self.label = Label(self.master, textvariable=self.var, relief=RAISED )
        self.var.set("Enter the file name you want to decode to English")
        self.label.pack()
        self.T = Text(self.master, height=2, width=30)
        self.T.pack()
        self.T.insert(END, "input.txt")
        self.quitButton = tk.Button(self.frame, text = 'OK', width = 25, command = self.mainFunc)
        self.quitButton.pack()
        self.frame.pack()

    def retrieve_input(self):
        input = self.T.get("1.0",'end-1c')
        return input

    def close_windows(self):
        self.master.destroy()

    def mainFunc(self):
            output=''
            file_to_read = self.retrieve_input()
            try:
                    fread = open(file_to_read,"r")

            except:
                    toplevel = Toplevel()
                    label1 = Label(toplevel, text="Error: please enter the correct file name including the file extension", 
                                        height=0)
                    label1.pack()
                    self.close_windows()
                    return 

            try:
                for line in fread.readlines():
                        line = line.replace("\n", "")
                        for word in line.split(' '):
                                word=word+' '
                                output=output+morseCodeDecode.decodeMorse(word)+' '
                print(output)
                fread.close()
                if(morseCodeDecode.writeTofile(output,"output.txt")==True):
                        toplevel = Toplevel()
                        label1 = Label(toplevel, text="Output successfully written to files", 
                                            height=0)
                        label1.pack()
                        self.close_windows()
                        return 

            except Exception as KeyError:
                toplevel = Toplevel()
                label1 = Label(toplevel, text="Error while processing file, please check the text in file and make sure it is in write format", 
                                    height=0)
                label1.pack()


class writeTofileGUI:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.var = StringVar()
        self.label = Label(self.master, textvariable=self.var, relief=RAISED )
        self.var.set("Enter the file name you want to create")
        self.label.pack()
        self.T = Text(self.master, height=2, width=30)
        self.T.pack()
        self.T.insert(END, "input.txt")
        self.var2 = StringVar()
        self.var2.set("Enter string to write to file")
        self.label2 = Label(self.master, textvariable=self.var2, relief=RAISED )
        self.label2.pack()
        self.T2 = Text(self.master, height=2, width=30)
        self.T2.pack()
        self.T2.insert(END, "Sample text")
        self.quitButton = tk.Button(self.frame, text = 'OK', width = 25, command = self.mainFunc)
        self.quitButton.pack()
        self.frame.pack()

    def retrieve_input_file(self):
        input = self.T.get("1.0",'end-1c')
        return input

    def retrieve_input_string(self):
        input = self.T2.get("1.0",'end-1c')
        return input

    def close_windows(self):
        self.master.destroy()

    def mainFunc(self):
        file_name = self.retrieve_input_file()
        string_to_file = self.retrieve_input_string()
        if(morseCodeDecode.writeTofile(string_to_file,str(file_name))==True):
                toplevel = Toplevel()
                label1 = Label(toplevel, text="Output successfully written to files", 
                                    height=0)
                label1.pack()
                self.close_windows()
                return

                
def main(): 
    root = tk.Tk()
    app = MainGUI(root)
    root.mainloop()

if __name__ == '__main__':
    main()