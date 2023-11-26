

def maskify(cc):
    return "".join(["#" if i < len(cc) - 4 else cc[i] for i in range(len(cc))])

test1 = "4556364607935616" # "############5616"
test2 =  "64607935616" #  "#######5616"
test3 = "1" # "1"
test4 = "" # ""

t1 = maskify(test1)
t2 = maskify(test2)
t3 = maskify(test3)
t4 = maskify(test4)
