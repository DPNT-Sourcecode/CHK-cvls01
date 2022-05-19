import checkout_solution

x = checkout_solution.checkout("AAAAA")
print("5A " + str(x))
assert checkout_solution.checkout("AAAAA") == 200

x = checkout_solution.checkout("BB")
print("2B " + str(x))
assert checkout_solution.checkout("BB") == 40