def isValid(string):
    s = []
    output = True
    index = 0
    opens = "([{"
    closes= ")]}"

    while index < len(string) and output:
        sym = string[index]
        if sym in opens:
            s.append(sym)
        else:
            if len(s) == 0:
                output = False
            else:
                top = s.pop()
                if not (opens.index(top) == closes.index(sym)):
                    output = False
        index +=1 
    if output and len(s) == 0:
        return True
    else:
        return False

print(isValid("({{{{}}}))"))