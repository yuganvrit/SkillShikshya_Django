# def validator(func):
#     def wrapper(a,b):
#         if b == 0:
#             return '0 cannot be divider'
#         return func(a,b)
#     return wrapper


# @validator
# def divide(a,b):
#     return a/b


#classwork.

def role_selector(func):

    def wrapper(role):
        if role in ['admin', 'editor', 'user']:
            return func(role)
        print( 'access denied')
    return wrapper


@role_selector
def check_role(role):
    print('Access Granted as ', role)

check_role('hero')
check_role('user')