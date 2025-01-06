#Find the subsrting from the given string
import re
def find_substring(name, target):
    occurance = len(re.findall(target, name))
    if occurance > 0:
        return occurance, target
    else:
        return None, None

name = "kajasahithkajakhankaja"
target = "kaja"
print(find_substring(name, target))