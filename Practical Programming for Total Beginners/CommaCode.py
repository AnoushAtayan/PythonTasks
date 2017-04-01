spam = ['apples', 'bananas', 'tofu', 'cats']

def listModification(list):
   for i in list:
       if i == list[0]:
           print ("'" + i + ","),
       elif i == list[-1]:
           print ("and " + i + "'"),
       elif i == list[-2]:
           print i,
       else:
           print i+ ", ",


listModification(spam)