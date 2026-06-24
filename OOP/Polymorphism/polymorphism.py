class Message:
    def send_message(self):
        return f"Message sent!"
    
class Mail(Message):
    def send_message(self):
        return f"Mail Sent!"
    
class Sms(Message):
    def send_message(self):
        return f"Sms Sent!"
    
class Whatsapp(Message):
    def send_message(self):
        return f"Whatsapp Sent!"
    
list = [Mail(), Sms(), Whatsapp()]
for l in list:
    print(l.send_message())



# create a class name as employee and demonstrate a perfect use case of instance, class and static method

class Employee:
    company = "Vrit"
    salary = 1000

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def info(self):
        return f"{self.name} is {self.age} years who is a {self.gender}"
    
    @classmethod
    def company_intro(cls):
        return f"Works in {cls.company}"
    
    @staticmethod
    def isValidSalary(salary):
        return salary>2000

print(Employee("Ram", 21, "Male").info())
print(Employee("Ram", 21, "Male").company_intro())
print(Employee("Ram", 21, "Male").isValidSalary(1000))



# abstraction classwork--------------------------------------------------------------------------
# create a class of dbengine and create some 
# sub classes like postgresqldbserver, mysqldbserver which inherit 
# above abs class
# create some abs methods which validates the host_name, username, password of that db server
# another abstract methods for orm conversion to raw sql
from abc import ABC, abstractmethod


class DBEngine(ABC):
    def __init__(self, host_name, username, password):
        self.host_name = host_name
        self.username = username
        self.password = password

    @abstractmethod
    def validate_host(self):
        pass

    @abstractmethod
    def validate_username(self):
        pass

    @abstractmethod
    def validate_password(self):
        pass

    @abstractmethod
    def orm_to_sql(self, table_name, **kwargs):
        pass


class PostgreSQLDBServer(DBEngine):

    def validate_host(self):
        return self.host_name.endswith(".com")

    def validate_username(self):
        return len(self.username) >= 5

    def validate_password(self):
        return len(self.password) >= 8

    def orm_to_sql(self, table_name, **kwargs):
        columns = ", ".join(kwargs.keys())
        values = ", ".join([f"'{v}'" for v in kwargs.values()])
        return f"INSERT INTO {table_name} ({columns}) VALUES ({values});"


class MySQLDBServer(DBEngine):

    def validate_host(self):
        return "." in self.host_name

    def validate_username(self):
        return self.username.isalnum()

    def validate_password(self):
        return (
            len(self.password) >= 6
            and any(char.isdigit() for char in self.password)
        )

    def orm_to_sql(self, table_name, **kwargs):
        columns = ", ".join(kwargs.keys())
        values = ", ".join([f"'{v}'" for v in kwargs.values()])
        return f"INSERT INTO `{table_name}` ({columns}) VALUES ({values});"


# PostgreSQL Example
pg = PostgreSQLDBServer(
    host_name="postgres.example.com",
    username="sahil123",
    password="secret123"
)

print(pg.validate_host())
print(pg.validate_username())
print(pg.validate_password())
print(pg.orm_to_sql("users", name="Sahil", age=22))


# MySQL Example
mysql = MySQLDBServer(
    host_name="mysql.local",
    username="admin123",
    password="pass123"
)

print(mysql.validate_host())
print(mysql.validate_username())
print(mysql.validate_password())
print(mysql.orm_to_sql("employees", name="John", salary=50000))