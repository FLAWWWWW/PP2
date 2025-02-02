def unique_list(lst):
    unique = []
    for item in lst:
        if item not in unique:
            unique.append(item)
    print(f"Unique elements: {unique}")

unique_list([1, 2, 3, 2, 4, 5, 1])