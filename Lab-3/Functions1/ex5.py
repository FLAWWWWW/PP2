from itertools import permutations

def print_permutations(s):
    perms = []
    for p in permutations(s):
        perm = ""
        for char in p:
            perm += char
        perms.append(perm)
    print("Permutations:", perms)

print_permutations("abc")