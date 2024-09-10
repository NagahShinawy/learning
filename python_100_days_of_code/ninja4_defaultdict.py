from black.trans import defaultdict

tech_books = [
    ('The Pragmatic Programmer', 100),
    ('Clean Code: A Handbook of Agile Software Craftsmanship', 200),
    ('The Mythical Man-Month: Essays on Software Engineering', 100),
    ('Introduction to Algorithms', 50),
    ('Design Patterns: Elements of Reusable Object-Oriented Software', 50),
    ('Code Complete', 100),
    ('You Don’t Know JS', 200),
    ('Hackers and Painters: Big Ideas from the Computer Age', 300),
]

# Avoids Key Errors: You don't need to check if a key exists before accessing or modifying it.
grouping_books = {}
for title, price in tech_books:
    if not grouping_books.get(price):
        grouping_books[price] = []
    grouping_books[price].append(title)


print(grouping_books)

print("#" * 100)
grouping_books = defaultdict(list)

for title, price in tech_books:
    grouping_books[price].append(title)

print(grouping_books)


tech = "python python js go python go html css react react vue react js django flask odoo flask"

words = tech.split()

words_count = defaultdict(int)

for word in words:
    words_count[word] += 1


print(words_count)

# ##########################################

employees = [
    ("David", "QA"),
    ("John", "BE"),
    ("Smith", "FE"),
    ("Adam", "QA"),
    ("Eva", "BE"),
    ("Bob", "FE"),
    ("Loen", "FE"),
]

emps_grouping = defaultdict(list)

for name, job in employees:
    emps_grouping[job].append(name)


print(emps_grouping)
