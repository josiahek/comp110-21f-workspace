"""Quiz0 Practice."""
#example 1
a: str = "qwerty"
b: str = "3.14"
c: str = a[0] + a[len(b)]
a = "hehe"
print(c + b)

print(a)
print(b)
print(c)

#example 2
a: str = "a"
b: str = "a" + "c"
print(a)
print(b)
print(b + a)
b = b + "b"
a = a + b[len(a) + 1]
print(a)
print(b)
print(a[1])