# -----------------------------------------------
# Python Data Types
# -----------------------------------------------

# 1) type() — check an object's type
# Use type(obj) to see the data type.
example_values = [42, 3.14, 1+2j, "hello", True, [1,2], (1,2), range(3),
                  {"a":1}, {1,2}, frozenset({1,2}), b"bytes", bytearray(2), memoryview(b"ab"), None]
for v in example_values:
    print(v, "->", type(v))

# 2) Numbers: int, float, complex
# int: whole numbers, unlimited size; float: decimal; complex: a + bj
i = 12345678901234567890
f = 3.14159
c = 2 + 3j
print("int:", i)
print("float:", f)
print("complex:", c, "real:", c.real, "imag:", c.imag)

# Conversions
print("int(3.9):", int(3.9))        # truncates toward zero
print("float(7):", float(7))        # 7.0
print("complex(5):", complex(5))    # (5+0j)

# 3) Strings (str): text, immutable, sequence of Unicode
s = "Python"
print("s:", s, "| len:", len(s), "| s[0]:", s, "| s[1:4]:", s[1:4])
print("upper():", s.upper())
name, age = "Mahir", 20
print(f"{name} is {age} years old.")  # f-string formatting

# 4) Booleans (bool): True/False; truthiness of values
is_adult = age >= 18
print("is_adult:", is_adult)
print("True == 1:", True == 1, "False == 0:", False == 0)
print("bool(0):", bool(0), "bool(5):", bool(5), "bool(''):", bool(""))

# 5) Sequences: list (mutable), tuple (immutable), range (integer sequence)
lst = [10, 20, 30]
lst.append(40)
print("list:", lst, "first:", lst[0], "len:", len(lst))

tup = (10, 20, 30)
print("tuple:", tup, "first:", tup[0], "len:", len(tup))


# 6) Mapping: dict (key -> value)
person = {"name": "mahir", "age": 20}
person["city"] = "Pune"                  # add/update
print("dict:", person)
print("get existing:", person.get("name"))
print("get missing with default:", person.get("email", "N/A"))
print("keys:", list(person.keys()))
print("values:", list(person.values()))
print("items:", list(person.items()))

# 7) Sets: set (mutable unique collection), frozenset (immutable)
colors = {"red", "green", "blue", "red"}  # duplicates removed
print("set:", colors, "'red' in set?", "red" in colors)
colors.add("yellow")
print("after add:", colors)
fset = frozenset(["a", "b", "a"])
print("frozenset:", fset)

# 8) Binary types: bytes (immutable), bytearray (mutable), memoryview (no-copy view)
b = b"hi"
print("bytes:", b, "first byte:", b[0])
ba = bytearray(b"hi")
ba[10] = ord("o")  # change 'i' -> 'o'
print("bytearray:", ba, "as bytes:", bytes(ba))
mv = memoryview(b"abc")
print("memoryview first byte:", mv)

# 9) NoneType: None represents “no value”; compare with 'is'
result = None
print("result is None:", result is None)

# 10) Common conversions (casting)
print("str(123):", str(123))
print("int('45'):", int("45"))
print("float('3.14'):", float("3.14"))
print("bool('non-empty'):", bool("non-empty"))
print("list('abc'):", list("abc"))
print("tuple([1,2,3]):", tuple([1, 2, 3]))
print("set([1,1,2]):", set([1, 1, 2]))


# Quick rules :
# - Use int/float/complex for numbers; convert with int(), float(), complex().
# - str is immutable; use slicing and methods; f-strings for formatting.
# - bool is True/False; many values have truthiness (0, '', None -> False).
# - list is ordered and mutable; good for changing collections.
# - tuple is ordered and immutable; good for fixed data and dict keys.
# - range is efficient for loops.
# - dict maps keys to values; keys must be hashable (e.g., str, int, tuple).
# - set stores unique items; fast membership tests; frozenset is immutable.
# - bytes/bytearray/memoryview for binary data.