import re
a=re.search(r"([a-zA-Z0-9])\1+",input())
if a:
    print (a.group(1))
else:
    print -1     