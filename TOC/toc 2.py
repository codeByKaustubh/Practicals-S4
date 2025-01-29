import re
line = "Horses are taller than dogs"
searchObj = re.search(r'(.*) are (.*?) .*', line,re.M|re.I)
if searchObj:
    print("searchObj.group():", searchObj.group())
    print("searchObj.group():", searchObj.group(1))
    print("searchObj.group():", searchObj.group(2))
else:
    print("Nothing found!")