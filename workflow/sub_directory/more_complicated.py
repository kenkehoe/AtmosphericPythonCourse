IMPORTED_VARIABLE = 'I love my program'


def more_complicated_function(*args, **kwargs):
    """
    This is a more complicated function with a lot going on. Here we have not specified
    specific arguments or keywords but we can still accept them. We are using these specail
    *args and **kwargs arguments. *args means one or more arguments and **kwargs means
    one or more keyword arguments. Normally we will not process these arguments but will
    instead pass them through to different function that this function calls. It allows us
    to not need to define and manage arguments or keywords and just pass the information
    along to a different function that will accecpt them. This makes little sense right now
    but just know this exists and come back to this some day in the future when this
    concept solves your issue.
    """

    print(f"\n'args' in more_complicated_function() is a {type(args)}")
    print(f"'kwargs' in more_complicated_function() is a {type(kwargs)}\n")

    if len(args) > 0:
        print(f"You supplied {len(args)} arguments to more_complicated_function()")
        for arg in args:
            print(arg)

    if len(kwargs) > 0:
        print(f"\nYou supplied {len(kwargs)} keyword arguments to more_complicated_function()")
        for key, value in kwargs.items():
            print(f"{key}: {value}")
