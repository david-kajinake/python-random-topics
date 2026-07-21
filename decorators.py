
"""Simulate rate limit"""

request_times = 0
MAX_REQUESTS = 5

def rate_limit( request_function ):

    def wrapper( *args , **kwargs ):
        global request_times
        if request_times < MAX_REQUESTS:
            request_times += 1
            print(f"Requet {request_times} Accepted")
            request_function(*args , **kwargs)
        else:
            print("429 Too Many Requests")
        
    return wrapper

@rate_limit
def greet(name):
    print(f"Hello {name}..How are you doing")

greet("Alice")
greet("George")
greet("Amanda")
greet("Ericick")
greet("Tonny")
greet("Anita")
greet("Laur")
greet("Diana")
