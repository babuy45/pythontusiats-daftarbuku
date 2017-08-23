#social security number format: 111-11-1111

#def ssn(num):
    #if len(num) != 11:
     #   return False
    #for a in range(0,3):
      #  if num[a].isdecimal() is False:
     #       return False
    #if num[3] != "-":
     #   return False
    #for b in range(4, 6):
      #  if num[b].isdecimal() is False:
     #       return False
    #if num[6] != "-":
     #   return False
    #for c in range(7, 11):
   #     if num[c].isdecimal() is False:
  #          return False
 #   return True

#print(ssn("123-45-6789"))

#regular Eexpression with the RE Module

import re
ssnRegex = re.compile(r"\d\d\d-\d\d-\d\d\d\d")
#ssnMatch = ssnRegex.search("The two ssn's you're looking for are 557-12-8176 and 321-54-9876")

print(ssnRegex.findall("The two ssn's you're looking for are 557-12-8176 and 321-54-9876"))
