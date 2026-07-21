
"""Simulate rate limit"""

request_times = 0
MAX_REQUESTS = 5

def rate_limit( request_function ):
    def wrapper(*args , **kwargs):
        global request_times
        while request_times < MAX_REQUESTS:
            request_times += 1
            request_function(*args , **kwargs)
        print("You have hit the limit...Try Again Later")

    return wrapper


@rate_limit
def ask_random():
    random_word = input("Enter a random word:\n")
    print(f"\nRandom word is: {random_word}")

ask_random()




