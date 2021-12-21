contacts = {
    "number": 4,
    "students":
    [
        {"name":"sasi", "email":"sasi@example.com"},
        {"name":"vijay", "email":"vijay@example.com"},
        {"name": "arjun", "email": "arjun@example.com"},
        {"name":"vishal", "email": "vishal@example.com"}
    ]
}

for student in contacts["students"]:
    print(student["name"])