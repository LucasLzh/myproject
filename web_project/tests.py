from functools import wraps

def decorator_name(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        if not can_run:
            return "function will not run"
        return func(*args, **kwargs)
    return decorated


@decorator_name
def func():
    return ("function is running")


can_run = True
print(func())

can_run = False
print(func())


