is_logged_in = False

def login_required( requested_function ):
    def check_auth_status( *args , **kwargs ):
        if is_logged_in:
            print("Permission granted")
            requested_function( *args , **kwargs)
            print("Session ended")
        else:
            print("Permission denied. You must login")
    return check_auth_status


@login_required
def self_introduction(name):
    print(f"Hello My name is {name}...Nice to meet you")

self_introduction("Peter Okoye")