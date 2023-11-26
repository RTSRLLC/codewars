def find_short(s: str) -> int:
    return min(len(i) for i in s.split(" "))

a = find_short("bitcoin take over the world maybe who knows perhaps") # 3)
b = find_short("turns out random test cases are easier than writing out basic ones") # 3)
c = find_short("lets talk about javascript the best language") # 3)
d = find_short("i want to travel the world writing code one day") # 1)
e = find_short("Lets all go on holiday somewhere very cold") # 2)   
f = find_short("Let's travel abroad shall we") # 2)