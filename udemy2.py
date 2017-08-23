# zip code format = 12345-6789
# pattern = r"\d\d\d\d\d-\d\d\d\d"

import re

zipCodeRegex = re.compile(r"(\d\d\d\d\d)-(\d\d\d\d)")

zipMatch = zipCodeRegex.search("My zip code is 12345-67890")

print(zipMatch.group())
print((zipMatch.group(1)))
print(zipMatch.group(2))