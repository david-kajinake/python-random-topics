"""Smulate a function call retry"""

retries = 0
MAX_RETRIES = 5
import time

def retry( func ):
    def wrapper( *args, **kwargs ):
        global retries

        while retries < MAX_RETRIES:
            try:
                print("Calling.....")
                result = func( *args , **kwargs )
                return result
            except Exception as e:
                print(f"Error: {e}\nFailed, Retrying.....")
                retries += 1
                time.sleep(2)
        print("Process terminated.")
    return wrapper




@retry
def devide():
    numerator = int(input("Enter a numerator:\n"))
    denominator = int(input("Enter a denominator:\n"))
    answer = numerator / denominator
    return answer


response = devide()
print(response)








