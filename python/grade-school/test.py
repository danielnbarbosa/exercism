print '{2: {"James", "Blair", "Paul"}}'

d = dict()
s = set()
s.add("James")
s.add("Blair")
s.add("Paul")
d[2] = s
print d

d[2] = s + s.add("Yup")
print d