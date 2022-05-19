import checkout_solution

x = checkout_solution.checkout("AAAAA")
print("5A " + str(x))
assert checkout_solution.checkout("AAAAA") == 200

x = checkout_solution.checkout("BB")
print("2B " + str(x))
assert checkout_solution.checkout("BB") == 45

x = checkout_solution.checkout("C")
print("C " + str(x))
assert checkout_solution.checkout("C") == 20

x = checkout_solution.checkout("D")
print("D " + str(x))
assert checkout_solution.checkout("D") == 15

x = checkout_solution.checkout("EEB")
print("EEB " + str(x))
assert checkout_solution.checkout("EEB") == 80

x = checkout_solution.checkout("FF")
print("FF " + str(x))
assert checkout_solution.checkout("FF") == 20

x = checkout_solution.checkout("FFF")
print("FFF " + str(x))
assert checkout_solution.checkout("FFF") == 20

x = checkout_solution.checkout("FFFF")
print("FFFF " + str(x))
assert checkout_solution.checkout("FFFF") == 30

x = checkout_solution.checkout("FFFFF")
print("FFFFF " + str(x))
assert checkout_solution.checkout("FFFFF") == 40

x = checkout_solution.checkout("FFFFFF")
print("FFFFF " + str(x))
assert checkout_solution.checkout("FFFFFF") == 40

x = checkout_solution.checkout("G")
print("G" + str(x))
assert checkout_solution.checkout("G") == 20

x = checkout_solution.checkout("H")
print("H " + str(x))
assert checkout_solution.checkout("H") == 10

x = checkout_solution.checkout("HHHHH")
print("HHHHH " + str(x))
assert checkout_solution.checkout("HHHHH") == 45

x = checkout_solution.checkout("HHHHHHHHHH")
print("HHHHHHHHHH " + str(x))
assert checkout_solution.checkout("HHHHHHHHHH") == 80

x = checkout_solution.checkout("I")
print("I " + str(x))
assert checkout_solution.checkout("I") == 35

x = checkout_solution.checkout("J")
print("J " + str(x))
assert checkout_solution.checkout("J") == 60

x = checkout_solution.checkout("K")
print("K " + str(x))
assert checkout_solution.checkout("K") == 70

x = checkout_solution.checkout("KK")
print("KK " + str(x))
assert checkout_solution.checkout("KK") == 150

x = checkout_solution.checkout("L")
print("L " + str(x))
assert checkout_solution.checkout("L") == 90

x = checkout_solution.checkout("M")
print("M " + str(x))
assert checkout_solution.checkout("M") == 15

x = checkout_solution.checkout("N")
print("N " + str(x))
assert checkout_solution.checkout("N") == 40

x = checkout_solution.checkout("O")
print("0 " + str(x))
assert checkout_solution.checkout("O") == 10

x = checkout_solution.checkout("P")
print("P " + str(x))
assert checkout_solution.checkout("P") == 50

x = checkout_solution.checkout("PPPPP")
print("PPPPP " + str(x))
assert checkout_solution.checkout("PPPPP") == 200

x = checkout_solution.checkout("Q")
print("Q " + str(x))
assert checkout_solution.checkout("Q") == 30

x = checkout_solution.checkout("QQQ")
print("QQQ " + str(x))
assert checkout_solution.checkout("QQQ") == 80

x = checkout_solution.checkout("R")
print("R " + str(x))
assert checkout_solution.checkout("R") == 50

x = checkout_solution.checkout("RRRQ")
print("RRRQ " + str(x))
assert checkout_solution.checkout("RRRQ") == 150

x = checkout_solution.checkout("S")
print("S " + str(x))
assert checkout_solution.checkout("S") == 20

x = checkout_solution.checkout("T")
print("T " + str(x))
assert checkout_solution.checkout("T") == 20

x = checkout_solution.checkout("UUU")
print("UUU " + str(x))
assert checkout_solution.checkout("UUU") == 120

x = checkout_solution.checkout("UUUU")
print("UUUU " + str(x))
assert checkout_solution.checkout("UUUU") == 120

x = checkout_solution.checkout("V")
print("V " + str(x))
assert checkout_solution.checkout("V") == 50

x = checkout_solution.checkout("VV")
print("VV " + str(x))
assert checkout_solution.checkout("VV") == 90

x = checkout_solution.checkout("VVV")
print("VVV " + str(x))
assert checkout_solution.checkout("VVV") == 130

x = checkout_solution.checkout("W")
print("W " + str(x))
assert checkout_solution.checkout("W") == 20

x = checkout_solution.checkout("X")
print("X " + str(x))
assert checkout_solution.checkout("X") == 17

x = checkout_solution.checkout("Y")
print("Y " + str(x))
assert checkout_solution.checkout("Y") == 20

x = checkout_solution.checkout("Z")
print("Z " + str(x))
assert checkout_solution.checkout("Z") == 21

x = checkout_solution.checkout("STXXZ")
print("STXXZ " + str(x))
assert checkout_solution.checkout("STXXZ") == 79

x = checkout_solution.checkout("STXYZZ")
print("STXYZZ " + str(x))
assert checkout_solution.checkout("STXYZZ") == 90

x = checkout_solution.checkout("STXYZZZ")
print("STXYZZ " + str(x))
assert checkout_solution.checkout("STXYZZZ") == 107

