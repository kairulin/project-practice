import time
import random

def create_employees_id(prefix):
    ate = time.strftime("%Y%m%d")
    number =f'000{random.randint(1,100)}'
    full_number = prefix + ate + number
    return full_number

def make_user_number(prefix):
    from .user_number import check_id
    return check_id(create_employees_id, prefix)

# def make_user_number(prefix):
#     def call_func():
#         from .user_number import check_id
#         return check_id(create_employees_id, prefix)
#     return call_func