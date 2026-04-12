def greet_user(name):
    return f"Hello, {name}! Welcome to your AI Job Tracker."

if __name__ == "__main__":
    user_name = "Mamid"
    message = greet_user(user_name)
    print(message)