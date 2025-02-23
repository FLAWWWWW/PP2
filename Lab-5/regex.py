import re

# Task 1
'''
txt = "The a aa ab abb acbbb cab"

print(re.findall("ab*", txt))
'''

# Task 2
'''
txt = "The aa ab abb abbb abbbb"
pattern = r"ab{2,3}"

print(re.findall(pattern, txt))
'''

# Task 3
'''
txt = "THE a_b aa_bb aabb A_B"
pattern = r"[a-z]+[_]+[a-z]"

print(re.findall(pattern, txt))
'''

# Task 4
'''
txt = "THE a_b aa_bb aabb A_B A_b AC_b"
pattern = r"[A-Z]{1}+[_]+[a-z]"

print(re.findall(pattern, txt))
'''

# Task 5
'''
txt = "THE  acccb acc ab nanan" # acccb acc ab it is like one string
pattern = r"a.+b"

print(re.findall(pattern, txt))
'''

# Task 6
'''
txt = "THE, acccb. acc ab nanan"
pattern = r"[. ,]" # рассматривает каждый символ как отдельный символ

print(re.sub(pattern, ':', txt))
'''

# Task 7
'''
txt = "snake_case"
pattern = r"([a-zA-Z])_([a-zA-Z])"

def camel(match):
    return match.group(1) + match.group(2).upper()

print(re.sub(pattern, camel, txt))
'''

# Task 8
'''
txt = "HelloMyNameIsFlaw"
pattern = r"[A-Z][^A-Z]*" # [^A-Z]* - находит все большие буквы после которых идут любые другие символы

result = re.findall(pattern, txt)

print(result)
'''

# Task 9
'''
txt = "HelloMyNameIsFlaw"
pattern = r"([A-Z])"

result = re.sub(pattern, r' \1', txt).strip() # \1 сохраняет найденную большую букву. ' ' добавляет пробел перед. strip() убирает пробел с начала

print(result)
'''

# Task 10
'''
txt = "camelCase"
pattern = r"([a-z])([A-Z])"

def snake(match):
    return match.group(1) + "_" + match.group(2).lower()

print(re.sub(pattern, snake, txt))
'''