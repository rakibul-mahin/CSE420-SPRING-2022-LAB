def starts_with_num(text):
    if text[0] in "0123456789":
        return True
    else:
        return False

def starts_with_www(text):
    if text[:4] == "www.":
        return True
    else:
        return False

def find_mail_company(text):
    temp = text.split('@')
    company = ''

    if 'g.bracu.ac.bd' in temp[1]:
        return 'g.bracu.ac.bd'

    for i in temp[1]:
        if i == '.':
            return company
        else:
            company += i

def find_domain(text):
    temp = text.split('.')
    domain = ''
    for i in temp[-1]:
        domain += i

    return domain

def checker(text, pos):
    if starts_with_num(text):
        pass

    elif starts_with_www(text) and find_domain(text) in web_domain and '@' not in text and text[-1] != '.':
        print('Web,',pos+1)

    elif '@' in text and not starts_with_www(text) and find_mail_company(text) in mail_company and find_domain(text) in mail_domain and text[-1] != '.':
        print('Mail,',pos+1)

mail_company = 'gmail yahoo hotmail protonmail edumail g.bracu.ac.bd'.split()
mail_domain = 'com net g.bracu.ac.bd bd'.split()
web_domain = 'com org gov net edu biz bd uk us au'.split()

n = int(input("Please Enter a number: "))
user_input = []

[user_input.append(input("Please Enter a Text: ").lower()) for _ in range(n)]

[checker(j, i) for i, j in enumerate(user_input)]