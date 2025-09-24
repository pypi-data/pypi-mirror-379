from .peError import *
seed = 0
chars= ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
        'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
ywcyze = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
        'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
        '`','~','!',"@",'"',"'","#",'$','%',"^",'&','*','(',")","_","-",'+','=',':',';',"<",",",".",">","?","/",
        "{","}","[","]","|","\\","1","3","4","5","2","6","7","8",'9','0',"€"]#Commonly_used_English_characters

def get_seed():
    global seed
    for i in range(100):
        seed ^= id(object())
        seed = (seed << 13) | (seed >> 17)
    return seed % 2 ** 32
state = get_seed()

def xorshift():
    global state
    state ^= state << 13
    state ^= state >> 17
    state ^= state << 5
    state &= 0xFFFFffff
    return state
def randdev(min:float = 0.0, max:float = 1.0):
    if min == 0.0 and max == 1.0:
        return xorshift() / 2 ** 32
    else:
        return min + (max - min) % (xorshift() / 2 ** 32)
    
def randint(min:int = 0, max:int = 10):
    if min > max:
        min,max = max,min
    range_size = max - min + 1
    return min + xorshift() % range_size

def randchar():
    min = 0
    max = 51
    if min > max:
        min,max = max,min
    range_size = max - min + 1
    m = min + xorshift() % range_size
    return chars[m]

def randstr(length : int = 9):
    a = []
    if length <= 1:
        raise InvalidLengthError("Please provide a right length.")
    for i in range(length):
        min = 0
        max = len(chars) - 1
        s = ""
        range_size = max - min + 1
        m = min + xorshift() % range_size
        if min > max:
            min,max = max,min
        if m > len(chars) or m < 0:
            m = m + xorshift() % range_size
        a.append(chars[m])
    for i in range(len(a)):
        s = s + a[i]
    return s

def random(length : int = 9):
    a = []
    if length <= 0:
        raise InvalidLengthError("Please provide a right length.")
    for i in range(length):
        min = 0
        max = len(ywcyze) - 1
        s = ""
        range_size = max - min + 1
        m = min + xorshift() % range_size
        if min > max:
            min,max = max,min
        if m > len(ywcyze) or m < 0:
            m = m + xorshift() % range_size
        a.append(ywcyze[m])
    for i in range(len(a)):
        s = s + a[i]
    return s