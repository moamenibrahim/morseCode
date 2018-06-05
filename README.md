# MorseCode Web Api

A program that converts English text to Morse code and vice versa. For example, English text “SOS” should be converted to “•••−−−•••”. Converter is case insensitive, thus “sos” should produce same output “•••−−−•••” as “SOS” does. When converted to English, everything should be uppercased, thus “sos” converted to Morse and back to English should output “SOS”.
For this task, text (Either English or Morse) should be read from a file and output should be written to another. Simple command line interface for usage is enough which asks for input and output files and offers a way to do conversion from either English or Morse.

## Setting up the environment

### You will need

+ [Python 3.6.4](https://www.python.org/downloads/)

### Setting up the python virtual environment

In the project root folder run the following commands.

```bash
virtualenv --python=/path/to/your/python3-binary venv
# this is for mac users, please check your how you activate the virtual environment in your operating system.
. venv/bin/activate
```

## Running the tests

To run the tests please make sure that you activated the virtual environment using. To activate the virtual environment you can run the following command on your bash.

```bash
# In the project root folder
# this is for mac users, please check your how you activate the virtual environment in your operating system.
. venv/bin/activate
./run_morse_api_tests.sh
```

## GUIDE

main.py is for the terminal (command line version)
morseGUI.py is for the Graphical user interface version