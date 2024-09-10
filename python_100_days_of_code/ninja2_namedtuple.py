from collections import namedtuple
import json


users = ("john", "teamlead")
print(f"'{users[0].capitalize()}' is the '{users[1].capitalize()}'")

User = namedtuple("User", ["fullname", "role", "age", "location"])

john = User(location="Cairo", fullname="John Smith Eric", role="Teamlead", age=25)

print(john)  # User(name='John', role='Teamlead', age=25, location='Cairo')
print(type(john))   # <class '__main__.User'>
info = """
fullname is '{fullname}'
Location is '{location}'
Age is      '{age}'
Role        '{role}'
"""
print(info.format(fullname=john.fullname, location=john.location, age=john.age, role=john.role))

print("#" * 100)

Profile = namedtuple("Profile", ["id", "email", "username", "gender", "phone"])

profiles = [
    {"id": 101, "email": "adam@test.eg", "username": "adam", "gender": "male", "phone": "0100000000"},
    {"id": 102, "email": "john@test.eg", "username": "john", "gender": "male", "phone": "01011111111"},
    {"id": 103, "email": "celin@test.eg", "username": "celin", "gender": "female", "phone": "0102222222"},
]
info = """
ID is         '{id}'
Email is      '{email}'
Username is   '{username}'
Gender        '{gender}'
Phone        '{phone}'
"""

for profile in profiles:
    prf = Profile(**profile)
    print(info.format(id=prf.id, email=prf.email, username=prf.username, gender=prf.gender, phone=prf.phone))
    print("#" * 50)


Point = namedtuple("Point", field_names=["X", "Y"])

point = Point(X=10, Y=20)

print(f"X is {point.X}")
print(f"Y is {point.Y}")


class Config:
    HOST = "0.0.0.0"
    DB_NAME = "postgresql"
    DB_USER = "postgres"
    DB_PASSWORD = "postgres"
    DB_PORT = 5432

    def __str__(self):
        return f"{self.__class__.__name__}(host={self.HOST})"


print(Config())

Config = namedtuple("Config", field_names=["host", "db_name", "db_user", "db_password", "db_port"])
server = Config(host="1.1.1.1", db_user="postgres", db_name="postgresql", db_password="test", db_port=5432)
print(f"Host is [{server.host}]")
print(f"DB name is [{server.db_name}]")
print(f"DB user is [{server.db_user}]")
print(f"DB Port is [{server.db_port}]")
print("*" * 100)
api_response = '{"temperature": 72, "humidity": 50, "description": "clear sky"}'

Weather = namedtuple("Weather", ["temperature", "humidity", "description"])

weather = Weather(**json.loads(api_response))
print(f"Temperature is [{weather.temperature}]")
print(f"Humidity is [{weather.humidity}]")
print(f"Description is [{weather.description}]")