user = {
    "name": "dhanya",
    "valid": False
}


def authenticated(fn):
    def wrapper(*args, **kwargs):
        if args[0]['valid']: fn( * args, ** kwargs)

    return wrapper


@authenticated
def message_friends(users):
    print('message has been sent')


message_friends(user)
