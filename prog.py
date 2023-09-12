##Manoj Baddela##Assignment2#determine if the input string is valid#
import re
def isValid(s: str) -> bool:
    if (s == ''):
        return True
    elif not ((s.count('(') - s.count(')')) == 0 and (s.count('[') - s.count(']')) == 0 and (s.count('{') - s.count('}')) == 0):
        return False
    else:
        _result = [re.search(pattern, s)
                   for pattern in ['\((.)*\)', '\[(.)*\]', '\{(.)*\}']]
        _result = ['' if _result[i] is None else _result[i].group()[1:-1]
                   for i in range(len(_result))]
        return isValid(_result[0]) and isValid(_result[1]) and isValid(_result[2])
if __name__ == '__main__':
    #TestCase
    #True
    print("Manoj Baddela  Test Cases")
    print(isValid('[]'))
    print(isValid('{[]}'))
    #False
    print(isValid('([]){'))
    print(isValid('(]'))
    print(isValid('([)]'))
    print(isValid('({()}{[}])'))
