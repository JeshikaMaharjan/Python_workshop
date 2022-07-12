# Decorator
#A decorator takes in a function, adds some functionality and returns it.
def login_required(func):
    def do_authentication():
        print('Authenticate the user')
        func()
    return do_authentication


@login_required
def view_facebook():
    print('You are viewing facebook')


view_facebook()


@login_required
def view_settings():
    pass