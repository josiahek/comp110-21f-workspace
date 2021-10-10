"""demonstrations of dictionary capabilities."""


# declaring the type of a dictionary
schools: dict[str, int]

# initialize to an empty dictionary
schools = dict()

# set a key-value pairing in the dictionary
schools["UNC"] = 19400
schools["Duke"] = 6717
schools["NCSU"] = 26150

# print a ductuibary literal representation
print(schools)

# access a value by its key -- "lookup"
print(f"UNC has {schools['UNC']} students")

# remove a key-value pair from a dictionary
# by its key
schools.pop("Duke")

# test for the existence of a key
is_duke_present: bool = "Duke" in schools
print(f"Duke is present: {is_duke_present}")

# update / reassign a key-value pair
schools["UNC"] = 20000
schools["NCSU"] += 200


# demonstration of dictionary literals

# empty dictionary literal
schools = {}  # same as dict()
print(schools)


# alternatively, initialize key-value pairs
schools = {"UNC": 19400, "Duke": 6717, "NCSU": 26150}
print(schools)

# what happens when a key does not exist?
# print(schools["UNCC"])

for key in schools:
    print((f"Key: {key} -> Value: {schools[key]}"))