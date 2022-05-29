final = {
    'others': [],
    'keywords': [],
    'identifier': [],
    'math_operator': [],
    'logical_operator': [],
    'numerical_constant': [],
}

used = []

possible_keywords = 'int float if else for while return String double char boolean'.split()
possible_others = ["'",'"',"(",")","{","}","[","]",";",",",]
possible_math_operator = '+ - * / % ='.split()
possible_logical_operator = '&& || != == > >= < <='.split()

def find_symbols(pos_symbol, text, type):
    for i in pos_symbol:
        if i in text and i not in final[type]:
            final[type].append(i)
            used.append(i)

def find_num(txt, type):
    num = ''
    for i in txt:
        if i in '0123456789.':
            num += i
        
    if len(num) > 0 and num not in final[type]:
        final[type].append(num)
        return num

def find_identifier(txt, used, type):
    identifier = ''
    for i in txt:
        if i in '_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
            identifier += i
        else:
            identifier += ' '

    identifier = identifier.split()
    
    for i in identifier:
        if i not in used and i not in final[type]:
            final[type].append(i)
            used.append(i)

def output_creator(title, type, file):
    if type == 'others':
        print(f'{title}: ', end='', file=file)
        for i, j in enumerate(final[type]):
            if i == len(final[type])-1:
                print(j, file=file)
            else:
                print(j, end='', file=file)
    else:
        print(f'{title}: ', end='', file=file)
        for i, j in enumerate(final[type]):
            if i == len(final[type])-1:
                print(j, file=file)
            else:
                print(j, end=',', file=file)

def find_string_var(text, used, type):
    var = ''
    for i, j in enumerate(text):
        if j == '"' or j == "'":
            new_text = text[i+1:-1]
            for k in new_text:
                if k == '"' or k == "'":
                    break
                else:
                    var += k
    if var not in type and var not in used:
        final[type].append(var)
        used.append(var)

with open('input1.txt', 'r') as rf:
    data = [i for i in rf.read().splitlines()]
    for i in data:
        find_string_var(i, used, 'others')
        find_symbols(possible_others, i, 'others')
        find_symbols(possible_keywords, i, 'keywords')
        find_symbols(possible_math_operator, i, 'math_operator')
        find_symbols(possible_logical_operator, i, 'logical_operator')
        find_num(i, 'numerical_constant')
        find_identifier(i, used, 'identifier')

    with open('output1.txt', 'w') as wf:
        output_creator('Keywords', 'keywords', wf)
        output_creator('Identifiers', 'identifier', wf)
        output_creator('Math Operators', 'math_operator', wf)
        output_creator('Logical Operators', 'logical_operator', wf)
        output_creator('Numerical Constants', 'numerical_constant', wf)
        output_creator('Others', 'others', wf)