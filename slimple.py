'''
SLIMple, made by stngo/dream4sy with <3 in Germany!
Makes complex commands simple to use!
~ v.0.3.2
'''

import json
from os import system
import ctypes as cty
import webbrowser
import requests
import zipfile as zf
from cryptography.fernet import Fernet
from easy_getch import getch
import platform

class clr:
    '''
    Access to Colors in Terminal
    '''
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
    '''
    Get infos about this plugin
    '''
    def name():
        '''
        Get THIS plugin name
        '''
        return "SLIMple"
    def version():
        '''
        Get THIS plugin version
        '''
        return "0.3.2"
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
    '''
    Access to OS commands
    '''
    def clear():
        '''
        Clears the Terminal
        '''

        syst=platform.system()

        if syst == 'Windows':
            system('cls')
        else: system('clear')
    def check_os():
        '''
        Returning the name of the operation system
        '''
        return platform.system()
    def getch():
        '''
        Let the user press only ONE key to continue and/or remember the keypress

        Example:

            Code:
                key = slimple.os.getch()
                ; print(key)

            Terminal:
                *script waiting for input* | "I press q" | *script continues* | Terminal: q [NOT BYTE]
        '''
        return getch()
    class window:
        '''
        Access to window features
        '''
        def title(TITLE_OF_WINDOW):
            '''
            Changes the window title on terminal to a custom one.
            '''
            cty.windll.kernel32.SetConsoleTitleW(TITLE_OF_WINDOW)

class var:
    '''
    Access to Variable commands
    '''
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

    class crypt:
        '''
        Access to en- and decryption on Variables!
        '''
        class default:
            '''
            Use default en- and decryption. (a key, 1 up to 255)

            How to use:

            Template command:
                slimple.var.crypt.default(KEY, VARIABLE, DECODE=False).encrypt() -> encrpyted variable as output (decoded or not)
            '''

            def __init__(self, KEY=int, VARIABLE='', DECODE=False):
                self.key = KEY
                self.var = VARIABLE
                self.dec = DECODE

            def encrypt(self):
                '''
                Encrypts variable (remember key to decrypt). Useful for security.

                [BYTEARRAY NOT WORK, ONLY INT AND STR]
                '''
                maindata = self.var
                maindata = bytes(maindata, 'utf-8')

                data = bytearray(maindata)
                #print(' \n DEBUG:')
                for index, value in enumerate(data):
                    #print(f"index: {index} value: {value}")
                    data[index] = int(value) ^ int(self.key)

                #print(' ')
                #print(f' \nDATA:\n{data}\n')

                if self.dec:
                    return data.decode('utf-8')
                else:
                    return data

            def decrypt(self):
                '''
                Decrypts a file with a remembered key to read variable.

                [NEEDS BYTEARRAY -> not decoded encrypted variable]
                '''
                maindata = self.var
                #maindata = bytes(maindata, 'utf-8')

                data = bytearray(maindata)
                #print(' \n DEBUG:')
                for index, value in enumerate(data):
                    #print(f"index: {index} value: {value}")
                    data[index] = int(value) ^ int(self.key)

                #print(' ')
                #print(f' \nDATA:\n{data}\n')
                if self.dec:
                    return data.decode('utf-8')
                else:
                    return data

        class Fernet:
            '''
            More security encryption using a longer and harder key!

            How to use:

            Template command:
             slimple.var.crypt.Fernet(FERNET_KEY, VARIABLE).encrypt() -> encrpyted variable as output
              [VARIABLE MUST BE BYTES, OR IT WILL NOT WORK]
            Generate key:  key = slimple.file.crypt.Fernet()._generate()
            '''

            def __init__(self, FERNET_KEY=None, VARIABLE=None):
                self.key = FERNET_KEY
                self.var = VARIABLE

                self.error_notset = "Error: No variable and/or key set!"

            def _generate(x=None):
                '''
                Generates Fernet Key
                '''
                return Fernet.generate_key()
            def encrypt(self):
                if self.key == None or self.var == None:
                    return self.error_notset
                var = Fernet(self.key).encrypt(self.var)
                return var
            def decrypt(self):
                if self.key == None or self.var == None:
                    return self.error_notset
                var = Fernet(self.key).decrypt(self.var)
                return var





class file:
    '''
    Access to file commands
    '''
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



    class crypt:
        '''
        Access to en- and decryption on Variables!
        '''
        class default:
            '''
            Use default en- and decryption. (a key, 1 up to 255)

            How to use:

            Template command:
                slimple.var.crypt.default(KEY, VARIABLE, DECODE=False).encrypt() -> encrpyted variable as output (decoded or not)
            '''

            def __init__(self, KEY=int, FILE='', DECODE=False):
                self.key = KEY
                self.file = FILE
                self.dec = DECODE

            def encrypt(self):
                '''
                Encrypts file (remember key to decrypt). Useful for security.
                '''
                file = open(self.file, "rb")
                data = file.read()
                file.close()

                data = bytearray(data)
                #print(' \n DEBUG:')
                for index, value in enumerate(data):
                    #print(f"index: {index} value: {value}")
                    data[index] = int(value) ^ int(self.key)

                #print(' ')
                #print(f' \nDATA:\n{data}\n')

                if self.dec:
                    open(self.file, 'wb').write(data.decode('utf-8'))
                else:
                    open(self.file, 'wb').write(data)

            def decrypt(self):
                '''
                Decrypts a file with a remembered key to read variable.

                [NEEDS BYTEARRAY -> not decoded encrypted file]
                '''
                file = open(self.file, "rb")
                data = file.read()
                file.close()
                #maindata = bytes(maindata, 'utf-8')

                data = bytearray(data)
                #print(' \n DEBUG:')
                for index, value in enumerate(data):
                    #print(f"index: {index} value: {value}")
                    data[index] = int(value) ^ int(self.key)

                #print(' ')
                #print(f' \nDATA:\n{data}\n')
                if self.dec:
                    open(self.file, 'wb').write(data.decode('utf-8'))
                else:
                    open(self.file, 'wb').write(data)

        class Fernet:
            '''
            More security encryption using a longer and harder key!

            How to use:

            Template command:
             slimple.file.crypt.Fernet(FERNET_KEY, VARIABLE).encrypt() -> encrpyted file [replaced]
            Generate key:  key = slimple.file.crypt.Fernet()._generate()
            '''

            def __init__(self, FERNET_KEY=None, FILE=None):
                self.key = FERNET_KEY
                self.file = FILE

                self.error_notset = "Error: No file and/or key set!"

            def _generate(x=None):
                '''
                Generates Fernet Key
                '''
                return Fernet.generate_key()
            def encrypt(self):
                if self.key == None or self.file == None:
                    return self.error_notset

                filedata = open(self.file, 'rb').read()
                data = Fernet(self.key).encrypt(filedata)

                open(self.file, 'wb').write(data)

            def decrypt(self):
                if self.key == None or self.file == None:
                    return self.error_notset

                filedata = open(self.file, 'rb').read()
                data = Fernet(self.key).decrypt(filedata)

                open(self.file, 'wb').write(data)

class web:
    '''
    Access to the web with your program
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
