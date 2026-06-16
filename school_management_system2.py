editor = {
    'name': 'Samir',
    'role': 'editor',
}

def permission_check(role):
    def role_selector(func):
        def wrapper(provided_role):
            if provided_role == role:
                return func()
            print( 'access denied' )
        return wrapper
    return role_selector

@permission_check('editor')
def give_assignments():
    return 'given'   

print(give_assignments(editor.get('role'))) 


