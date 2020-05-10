def getFirstChar(str):
    pos = 1
    c = ''
    while str != None and len(str) > 0:
        c = str[0]
        if c in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
            # qwertyuiopasdfghjklzxcvbnm QWERTYUIOPASDFGHJKLZXCVBNM
            return c, pos
        else:
            pos += 1
            str = str[1:]

def getLastChar(str):
    pos = 1
    c = ''
    while str != None and len(str) > 0:
        c = str[len(str) - 1]
        if c in 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM':
            return c, pos
        else:
            pos += 1
            str = str[:-1]

def isPalindrome(str):
    # print(str)
    if len(str) <= 1:
        return True
    else:
        f = getFirstChar(str)
        if f == None:
            return True
        else:
            first, firstpos = f
        l = getLastChar(str)
        if l == None:
            return True
        else:
            last, lastpos = l
        # print(first, firstpos, last, lastpos, '<', str, '>', '<', str[firstpos:-lastpos], '>')
        if first.lower() == last.lower():
            return isPalindrome(str[firstpos:-lastpos])
        else:
            return False


# print(isPalindrome('; '))

# print(isPalindrome(''))
# print(isPalindrome('x'))
# print(isPalindrome('xx'))
# print(isPalindrome('xy'))
# print(isPalindrome('kayak'))
# print(isPalindrome('aibohphobia'))
# print(isPalindrome('Live not on evil'))

print(isPalindrome('kayak'))
# print(getLastChar('hph'))
print(isPalindrome('aibohphobia'))
print(isPalindrome('Live not on evil'))
print(isPalindrome('Reviled did I live, said I, as evil I did deliver'))
print(isPalindrome('Go hang a salami; I’m a lasagna hog.'))
print(isPalindrome('Able was I ere I saw Elba'))
print(isPalindrome('Kanakanak'))
print(isPalindrome('Wassamassaw'))
# print(isPalindrome('Kanakanak – a town in Alaska'))
# print(isPalindrome('Wassamassaw – a town in South Dakota'))