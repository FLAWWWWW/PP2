def reverse_sentence(text):
    words = text.split()
    index = -1
    reversed = ""
    i = 0
    while i < len(words):
        reversed += words[index]
        reversed += " "
        index = index - 1
        i += 1
    return reversed

print(reverse_sentence('We are ready'))