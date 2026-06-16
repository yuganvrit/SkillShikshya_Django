# # Simulate a "logged in" user — in a real app this might come from a session/token
# current_user = {"name": "Alice", "role": "editor"}

# def require_role(required_role):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             if current_user["role"] != required_role:
#                 print(f"Access denied: '{current_user['role']}' role cannot access this. Requires '{required_role}'.")
#                 return None
#             return func(*args, **kwargs)
#         return wrapper
#     return decorator


# @require_role("admin")
# def delete_user(username):
#     print(f"User '{username}' has been deleted.")

# @require_role("editor")
# def edit_post(post_id):
#     print(f"Post {post_id} has been edited.")


# delete_user("bob")   # current_user is "editor" -> denied
# edit_post(42)         # current_user is "editor" -> allowed


# Simulated "logged in" user — in a real app this would come from a session/database
current_user = {"name": "Alice", "role": "editor"}


def require_role(required_role):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if current_user["role"] == required_role:
                return func(*args, **kwargs)
            else:
                print("Access Denied")
        return wrapper
    return decorator


@require_role("admin")
def delete_user(username):
    print(f"User '{username}' has been deleted.")


@require_role("editor")
def edit_post(post_id):
    print(f"Post {post_id} has been edited.")


@require_role("user")
def view_profile():
    print("Viewing profile...")


# --- Testing ---
delete_user("bob")     # current_user role is "editor" -> Access Denied
edit_post(42)           # current_user role is "editor" -> allowed
view_profile()          # current_user role is "editor" -> Access Denied