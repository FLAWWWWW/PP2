def is_palindrome(word):
    result = word == word[::-1]
    print(f"Is a palindrome : {result}")

is_palindrome("lol")
is_palindrome("kekw")