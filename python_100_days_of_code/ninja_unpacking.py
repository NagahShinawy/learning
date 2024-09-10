from collections import namedtuple

user = {
    "name": "John",
    "job": "QA",
    "age": 20,
}

print(f'Name is {user["name"]}')
print(f'Job is {user["job"]}')
# print(f'Age is {user["age"]}') # KeyError: 'age'
print(f'Age is {user.get("age")}')
has_age = user.get("age")
age = has_age if has_age else 0
print(f"Age is {age}")
print("#" * 100)
students = [('Alice', 92), ('Bob', 85), ('Charlie', 78), ('David', 95), ('Eva', 66)]
#
# for student in degrees:
#     for name, degree in student:
#         print(name, degree)  # ValueError: too many values to unpack (expected 2)

for name, degree in students:
    print(f"Name is {name}")
    print(f"Degree is {degree}")
    print("#" * 10)

top_teams = ("Real Madrid", "Barca", "Man City")
rm, barca, mancity = top_teams
print(f"{rm},{barca},{mancity}")
print("*" * 100)
books = tech_books = [
    ('The Pragmatic Programmer', 352),
    ('Clean Code: A Handbook of Agile Software Craftsmanship', 464),
    ('The Mythical Man-Month: Essays on Software Engineering', 336),
    ('Introduction to Algorithms', 1312),
    ('Design Patterns: Elements of Reusable Object-Oriented Software', 395),
    ('Code Complete', 960),
    ('You Don’t Know JS', 100),
    ('Hackers and Painters: Big Ideas from the Computer Age', 272),
    ('The Phoenix Project: A Novel About IT, DevOps, and Helping Your Business Win', 432),
    ('Sapiens: A Brief History of Humankind', 498)
]

Book = namedtuple("Book", field_names=["title", "pages"])

for title, pages in books:
    book = Book(title=title, pages=pages)
    print(f"Title: {book.title}")
    print(f"Pages: {book.pages}")
    print("*" * 100)


for book in books:
    title = book[0]
    pages = book[1]
    print(f"Title: {title}")
    print(f"Pages: {pages}")
    print("#" * 100)


# easy with unpacking

dimensions = (5, 8)
print(f"Rows are {dimensions[0]}")
print(f"Col are {dimensions[1]}")
row, col = (5, 8)
print(f"Rows are {row}")
print(f"Col are {col}")

# #########################  ##################################  ##########################
# Result from a database query
employees = [
    (101, "John Doe", "Software Engineer", 60000),
    (102, "Jane Smith", "Data Scientist", 75000),
    (103, "David", "QA engineer", 80000),
]
info = """
ID:     {id}
Name:   {name}
Job:    {job}
Salary: {salary}
"""
for _id, name, job, salary in employees:
    print(info.format(id=_id, name=name, job=job, salary=salary))


def calculate_statistics(data):
    avrg = sum(data) / len(data)
    return min(data), max(data), avrg


minvalue, maxvalue, average = calculate_statistics([30, 40, 60, 10, 12, 77, 53])
print(minvalue, maxvalue, round(average, 2))
