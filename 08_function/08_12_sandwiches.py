def make_sandwich(*toppings):
    print("/nMaking a sandwich with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_sandwich('lettuce', 'onions', 'tomatos')
make_sandwich('wheat bread', 'extra turkey')