def solve(heads , legs):
    for rabbits in range(heads + 1):
        chickens = heads - rabbits
        if 2 * chickens + 4 * rabbits == legs:
            print(f"Chickens: {chickens}, Rabbits: {rabbits}")
            return
    print("We don't have an answer(")

solve(35, 94)