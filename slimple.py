'''
SLIMple, made by stngo/dream4sy with <3 in Germany!
Makes complex commands simple to use!
only works on windows, because msvcrt and command "clear()"

~ v.0.1.2
'''



import json
from os import system
import msvcrt as mv
import ctypes as cty
import webbrowser
import requests
import zipfile as zf

class clr:
    black = "\u001b[30m"
    red = "\u001b[31m"
    green = "\u001b[32m"
    yellow = "\u001b[33m"
    blue = "\u001b[34m"
    magenta = "\u001b[35m"
    cyan = "\u001b[36m"
    white = "\u001b[37m"

    resc = "\u001b[0m"


class info:
    def name():
        '''
        Get THIS plugin name
        '''
        return "SLIMple"
    def version():
        '''
        Get THIS plugin version
        '''
        return "0.1.2"
    def creator():
        '''
        Get THIS plugin creator
        '''
        return "dream4sy"
    def link(open=False):
        '''
        Get THIS plugin official GitHub link
        '''
        link = "https://github.com/stngo/SLIMple"

        if open:
            webbrowser.open(link)

        return link


def next_line(NUMBER):
    '''
    Prints empty lines, useful for good cmd programs
    '''
    for i in range(NUMBER):
        print()

class os:
    def clear():
        '''
        Clears the Terminal (Only Windows Mechanic)
        '''
        system('cls')
    def one_input():
        '''
        Let the user press only ONE key to continue and/or remember the keypress

        Example:

            Code:
                key = slimple.os.one_input()
                ; print(key)

            Terminal:
                *script waiting for input* | "I press q" | *script continues* | Terminal: q
        '''
        return mv.getch()
    class window:
        '''
        Acess to window features
        '''
        def title(TITLE_OF_WINDOW):
            '''
            Changes the window title on terminal to a custom one.
            '''
            cty.windll.kernel32.SetConsoleTitleW(TITLE_OF_WINDOW)

class var:
    class check:
        def IfInt(VariableToCheck):
            '''
            Checks, if variable is an integer
            '''
            try:
                int(VariableToCheck)
                return True
            except:
                return False

        def IfStr(VariableToCheck):
            '''
            Checks, if variable is an string
            '''
            try:
                str(VariableToCheck)
                return True
            except:
                return False
    def split(VariableToSplit, PREFIX_FOR_SPLIT='|'):
        '''
        Splits an Variable to a list, Example:
        'This/Is/A/Variable/With/Slashes' => '["This", "Is", "A", "Variable", "With", "Slashes"]'
        '''

        return VariableToSplit.split(PREFIX_FOR_SPLIT)
    

    def encrypt(VariableToCrypt, KEY):
        '''
        Encrypts variable with a key between 1 and 255 (remember key to decrypt) for security.
        '''
        data = VariableToCrypt

        data = bytearray(data)
        #print(' \n DEBUG:')
        for index, value in enumerate(data):
            #print(f"index: {index} value: {value}")
            data[index] = value ^ KEY

        #print(' ')
        #print(f' \nDATA:\n{data}\n')
        return data

    def decrypt(VariableToCrypt, KEY):
        '''
        Decrypts a file with a remembered key to read variable.
        '''
        data = VariableToCrypt

        data = bytearray(data)
        #print(' \n DEBUG:')
        for index, value in enumerate(data):
            #print(f"index: {index} value: {value}")
            data[index] = value ^ KEY
        
        #print(' ')
        #print(f' \nDATA:\n{data}\n')
        return data




class file:
    def read(FILENAME):
        '''
        Reads a file

        Example how to use:
            textfile = slimple.file.read('test.txt')

            print(textfile)  # prints out the filecontent
        '''
        return open(FILENAME, 'r').read()
    def read_bytes(FILENAME):
        '''
        Reads a file (reading in bytes)

        Example how to use:
            textfile = slimple.file.read('test.txt')
            
            print(textfile)  # prints out the filecontent
        '''
        return open(FILENAME, 'rb').read()
    def read_json(FILENAME_OF_JSON):
        '''
        Reads a json file

        Example how to use:
            jsonfile = slimple.file.read('test.json')
            
            print(jsonfile['AnJsonEntry'])  # prints out the json entry

        '''
        return json.loads(open(FILENAME_OF_JSON, 'r').read())

    def write(FILENAME, TEXT_TO_WRITE):
        '''
        Write content into a file

        Example how to use:
            content = 'Text To Write'

            slimple.file.write('TestFile.txt', content)
        '''
        open(FILENAME, 'w').write(TEXT_TO_WRITE)
    def write_bytes(FILENAME, TEXT_TO_WRITE):
        '''
        Write content into a file (writing in bytes)

        Example how to use:
            content = 'Text To Write'

            slimple.file.write('TestFile.txt', content)
        '''
        open(FILENAME, 'wb').write(TEXT_TO_WRITE)

    def unzip(ZIPFILE, PATH=''):
        '''
        Unzips a zip

        Example how to use:
            file = 'testfile.zip'
            path = 'test/folder/'

            slimple.file.unzip(file, path)  # Unzips files from zip into path
        '''
        with zf.ZipFile(ZIPFILE) as mz:
            mz.extractall(PATH)
    
    def split(FILENAME, PREFIX_FOR_SPLIT='|'):
        '''
        Splits the File-Content to a list, Example:
        'This/Is/Filecontent/With/Slashes' => '["This", "Is", "Filecontent", "With", "Slashes"]'
        '''
        with open(FILENAME, 'r') as f:
            for line in f.readlines():
                data = line.rstrip()
                method_list = data.split(PREFIX_FOR_SPLIT)
        return method_list



    def encrypt(FILENAME, KEY, NEW_FILENAME='no_new_filename.txt', LOCATION='', PREFIXFILE='', SUFFIXFILE=''):
        '''
        Encrypts a file with a key between 1 and 255 (remember key to decrypt) for security.
        '''
        file = open(FILENAME, "rb")
        data = file.read()
        file.close()

        data = bytearray(data)
        #print(' \n DEBUG:')
        for index, value in enumerate(data):
            #print(f"index: {index} value: {value}")
            data[index] = value ^ KEY

        #print(' ')
        file = open(LOCATION + PREFIXFILE + NEW_FILENAME + SUFFIXFILE, "wb")
        #print(f' \nDATA:\n{data}\n')
        file.write(data)
        file.close()

    def decrypt(FILENAME, KEY, NEW_FILENAME='no_new_filename.txt', LOCATION='', PREFIXFILE='', SUFFIXFILE=''):
        '''
        Decrypts a file with a remembered key to read encrypted file.
        '''
        file = open(FILENAME, "rb")
        data = file.read()
        file.close()

        data = bytearray(data)
        #print(' \n DEBUG:')
        for index, value in enumerate(data):
            #print(f"index: {index} value: {value}")
            data[index] = value ^ KEY
        
        #print(' ')
        file = open(LOCATION + PREFIXFILE + NEW_FILENAME + SUFFIXFILE, "wb")
        #print(f' \nDATA:\n{data}\n')
        file.write(data)
        file.close()

class web:
    '''
    Acess to the web with your program
    '''
    def openLink(link):
        '''
        Opens a link into new tab
        '''
        webbrowser.open(link)
    def getContent(link, redirects=True):
        '''
        Gets Web-Content

        Example:
            Website: *content of json*

            Code:
                link = 'https://test.com/test/this.json/'

                content = slimple.web.getContent(link)

                OUTPUT: *a normal json to read (useful for api's)*

        '''
        this = requests.get(link, allow_redirects=redirects)
        return this.content
