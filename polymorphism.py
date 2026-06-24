# # ##classwork
# # #class show a polymorphic in naturee of send_message throuogh different classes like mail sms whatsapp and manymore


# # class Message:
# #     def send_message(self):
# #         pass

# # class Whatsapp(Message):
# #     def send_message(self):
# #         print('Sending message through whatsapp')

# # class Facebook(Message):
# #     def send_message(self):
# #         print("Message is sendiing via Facebook")

# # class Twitter(Message):
# #     def send_message(self):
# #         print("Message is sended via Twitter")


# # services = [Whatsapp(), Facebook(), Twitter()]

# # # Polymorphism
# # for service in services:
# #     service.send_message()



# ##create a class named as employee and demonstrate a perfect use case of instance, class and static method
# class Employee:
#     total_employee = 50

#     def __init__(self, name, id, age, position):
#         self.name = name
#         self.id = id
#         self.age = age
#         self.position = position

#     def message(self):
#         return f'Hello my name is {self.name}. I am a senior level developer in {self.position}.'

#     @classmethod
#     def employee_count(cls):
#         return cls.total_employee

#     @staticmethod
#     def id_number(id):
#         return f'Employee Id : {id}'
    
#     @staticmethod
#     def age_emp(age):
#        return age>27


# Ram = Employee("Ram", 1, 23, "Python Django")

# print(Ram.message())
# print(Ram.employee_count())
# print(Ram.id_number(1))
# print(Ram.age_emp(Ram.age))


# from abc import ABC, abstractmethod

# class PaymentMethod(ABC):
#     def __init__(self, name):
#         self.name = name

#     @abstractmethod
#     def transaction_log(self):
#         print("Transaction has been started")


# class Esewa(PaymentMethod):
#     def transaction_log(self):
#         super().transaction_log()
#         print("Transaction is completed")


# pay_to_tea = Esewa("esewa")
# pay_to_tea.transaction_log()


##create a abstract class of databaseengine and create some subclasses like PostgresqlDBServer,MysqlServer which inherite above abstract class.
##create some abstract methods which validate the host_name,username,password of that db server


from abc import ABC, abstractmethod


class DatabaseEngine(ABC):
    def __init__(self, host_name, username, password):
        self.host_name = host_name
        self.username = username
        self.password = password

    @abstractmethod
    def validate_host_name(self):
        pass

    @abstractmethod
    def validate_username(self):
        pass

    @abstractmethod
    def validate_password(self):
        pass


class PostgresqlDBServer(DatabaseEngine):

    def validate_host_name(self):
        if self.host_name.endswith(".com"):
            return "PostgreSQL Hostname is valid"
        return "Invalid PostgreSQL hostname"

    def validate_username(self):
        if len(self.username) >= 5:
            return "PostgreSQL Username is valid"
        return "Username must contain at least 5 characters"

    def validate_password(self):
        if len(self.password) >= 8:
            return "PostgreSQL Password is valid"
        return "Password must contain at least 8 characters"


class MysqlServer(DatabaseEngine):

    def validate_host_name(self):
        if "." in self.host_name:
            return "MySQL Hostname is valid"
        return "Invalid MySQL hostname"

    def validate_username(self):
        if self.username.isalnum():
            return "MySQL Username is valid"
        return "Username should contain only letters and numbers"

    def validate_password(self):
        if len(self.password) >= 6:
            return "MySQL Password is valid"
        return "Password must contain at least 6 characters"


# PostgreSQL Server
postgres = PostgresqlDBServer(
    "postgres.example.com",
    "admin123",
    "securepass"
)

print(postgres.validate_host_name())
print(postgres.validate_username())
print(postgres.validate_password())



# MySQL Server
mysql = MysqlServer(
    "mysql.local",
    "user01",
    "pass123"
)

print(mysql.validate_host_name())
print(mysql.validate_username())
print(mysql.validate_password())
