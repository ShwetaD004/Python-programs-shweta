import re
'''str1="Hello my number is 12345678 & friends number is 987654321"
regex='\d+'
match1=re.findall(regex,str1)
print(match) '''

'''str2="Hii I'm a Honest student."
regex='^H\w+'
match2=re.findall(regex,str2)
print(match2)'''

'''str3="Shweta, Shravani, Disha ,Sam"
match3=re.findall("Sam$",str3)
if match3:
  print("Yes, the string ends with 'Sam'")
else:
  print("No match")'''

'''str4="Hello my name is Johnn"
match4=re.findall("Jo.*n",str4)
print(match4)'''

'''str5="This is a balloon"
match5=re.findall("ba.?oon",str5)
print(match5)'''

'''str6="This is a balloon"
match6=re.findall("ba{2}oon",str6)
print(match6)'''

match=re.compile('[a-e]')
print(match.findall("What a pleasant surprise"))

str7 = "The rain in Kolhapur"
match7 = re.findall("\AThe", str7)
print(match7)