import re
def encodedstring(estring):
    splitstring=re.split('0+',estring)
    return {"first_name":splitstring[0],
            "last_name": splitstring[1],
            "id":splitstring[2]
            }
    
print(encodedstring("John000Doe000123"))    
print(encodedstring("Steven0Smith00000000000125"))    