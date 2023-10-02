def argument_function(argument, value1=None, value2=False):
    """
    This is a library funciton that accepts arguments and keywords and will typically do
    something. In this case not much, more of an example

    Parameters
    ----------
    argument : str
        This is documentation telling you what the argument should be when passed in and
        how it will be used in the function. We have defined it will be a string with the
        " : str" part after "argument". It's not a hard and fast rule that the value must
        be a string, it's more of a statement. Depending on how the rest of the function
        is codeded a non-string may/maynot work. There are ways to force the type but it is
        not implemented here.
    value1 : str, list or None
        This is a keyword. Notice it can be three different types, string, list or None.
    value2 : bool
        This is a second keyword. It is a boolean. You typicall do not want to set
        a keyword to a mutable object in the function declaration. It will work just fine
        but goes against good programing practices. In this case a boolean is an imutable
        object so this is a good place to set the default of False. Notice below even if
        you do not set the keyword in you call to this function value2 will still have
        a value set, and it will be False.


    Returns
    -------
    Returns a tuple with first value set to a string set to "Have a great day".
    We can return anything but if we return more than one thing we need to expect
    to set more than one varible. If more than one thing is returned it will return a tuple
    and we can set multiple varibles to the return.

    Example
    -------
    result, value1, value2 = argument_function('What is for breakfast?', 'spam and eggs', value2=True)

    """

    print(f"\nYou passed '{argument}' into argument_function()")

    print(f"value1 is set to '{value1}' in argument_function()")

    print(f"value2 is set to '{value2}' in argument_function()\n")

    return "Have a great day", value1, value2


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

    print()
    print(f"args in more_complicated_function() is a {type(args)}")
    print(f"kwargs in more_complicated_function() is a {type(kwargs)}")
    print()

    if len(args) > 0:
        print(f"You supplied {len(args)} arguments to more_complicated_function()")
        for arg in args:
            print(arg)

    if len(kwargs) > 0:
        print(f"You supplied {len(kwargs)} keyword arguments to more_complicated_function()")
        for key, value in kwargs.items():
            print(f"{key}: {value}")
