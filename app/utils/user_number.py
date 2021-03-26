from app.authorization.models import Employees

def check_id(gen_func, *args):
    num = gen_func(*args)
    while Employees.objects.filter(id=num).exists():
        num = gen_func(*args)
    return num