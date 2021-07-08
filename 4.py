import re
a = 'qwrtypsdfghjklzxcvbnm'
b = 'aeiou'
match = re.findall(r'(?<=['+a+'])(['+b+']{2,})(?=['+a+'])',input(),flags = re.I)
if match:
    for i in match:
        print(i)
else:
    print -1