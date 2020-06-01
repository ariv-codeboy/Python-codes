To_morse = {'A':'.-', 
            'B':'-...', 
            'C':'-.-.', 
            'D':'-..', 
            'E':'.', 
            'F':'..-.', 
            'G':'--.', 
            'H':'....', 
            'I':'..', 
            'J':'.---',
            'K':'-.-', 
            'L':'.-..',
            'M':'--',
            'N':'-.', 
            'O':'---',
            'P':'.--.',
            'Q':'--.-', 
            'R':'.-.', 
            'S':'...', 
            'T':'-', 
            'U':'..-', 
            'V':'...-', 
            'W':'.--', 
            'X':'-..-', 
            'Y':'-.--', 
            'Z':'--..', 
            '1':'.----', 
            '2':'..---', 
            '3':'...--', 
            '4':'....-', 
            '5':'.....', 
            '6':'-....', 
            '7':'--...', 
            '8':'---..', 
            '9':'----.', 
            '0':'-----', 
            ',':'--..--', 
            '.':'.-.-.-', 
            '?':'..--..', 
            '/':'-..-.', 
            '-':'-....-', 
            '(':'-.--.', 
            ')':'-.--.-',
            ' ':'  '
            } 

From_morse={'.-':'A',
            '-...':'B',
            '-.-.':'C',
            '-..':'D',
            '.':'E',
            '..-.':'F',
            '--.':'G',
            '....':'H',
            '..':'I',
            '.---':'J',
            '-.-':'K',
            '.-..':'L',
            '--':'M',
            '-.':'N',
            '---':'O',
            '.--.':'P',
            '--.-':'Q',
            '.-.':'R',
            '...':'S',
            '-':'T',
            '..-':'U',
            '...-':'V',
            '.--':'W',
            '-..-':'X',
            '-.--':'Y',
            '--..':'Z',
            '.----':'1',
            '..---':'2',
            '...--':'3',
            '....-':'4',
            '.....':'5',
            '-....':'6',
            '--...':'7',
            '---..':'8',
            '----.':'9',
            '-----':'0',
            '--..--':',',
            '.-.-.-':'.',
            '..--..':'?',
            '-..-.':'/',
            '-....-':'-',
            '-.--.':'(',
            '-.--.-':')',
            ' ':'  ',
            }   


msg=input("Enter your msg here: ").upper()
encrypt=""
for i in msg:
    encrypt=encrypt+To_morse.get(i)+" "
print(encrypt)

msg=input("Enter your morse code here: ").split(" ")
decrypt=""
for i in msg:
    decrypt=decrypt+From_morse.get(i)+" "
print(decrypt)