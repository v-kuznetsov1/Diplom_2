
from faker import Faker
import random
import string


def generate_random_email():  
        domain = "@example.com"  
        username_length = random.randint(5, 10)  
        username = ''.join(random.choice(string.ascii_lowercase) for _ in range(username_length))  
        email = username + domain
        return email



class GenerateUserData:

    def generate_test_data():
        fake = Faker()

        user_data = {
        "email": generate_random_email() ,
        "password": fake.password(length=8, digits=True),
        "name": fake.user_name()
        }
        return user_data
        
        
    fake = Faker()    
    
    
    test_password = fake.password(length=8, digits=True)
    test_username = fake.user_name()

    user_data = {
        "email": generate_random_email(),
        "password": test_password,
        "name": test_username
        }
    
    user_data_without_email = {
        "email": "",
        "password": test_password,
        "name": test_username
        }
    
    user_data_without_password = {
        "email": generate_random_email(),
        "password": "",
        "name": test_username
        }
    
    user_data_without_name = {
        "email": generate_random_email(),
        "password": test_password,
        "name": ""
        }
    
  