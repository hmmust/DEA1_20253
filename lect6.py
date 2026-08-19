students = [
    {"name":"Diaa","age":21},
    {"name":"Mahmoud","age":20},
    {"name":"Hashem","age":22},
]
students = list(sorted(students, key=lambda s: s['name'] ))
print(students)