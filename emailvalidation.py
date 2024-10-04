# Basic email validation

import re
a='jibinaji24@gmail.com1'
if(re.search('^[a-z].*@gmail.com$',a)):
    print("email valid")
else:
    print("ivalid email")