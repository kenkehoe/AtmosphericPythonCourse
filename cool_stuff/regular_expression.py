#! /usr/bin/env python3

import re


if False:
    text = 'sometext_with_lots_of_STUFF in it'

    search_result = re.match(r"asdfas", text)

    # Note what happens when no match is found. Returns None.
    print('\nsearch_result:', search_result)

    # This time a match is found. Printing will show a re object.
    search_result = re.match(r"sometext_with_", text)
    print('\nsearch_result:', search_result)

    if True:
        # Using .group() will print the matching text. Notice how the searh
        # text will work as long as the start of the string matches. If the
        # start does not it will not match.
        print('\nsearch_result.group():', search_result.group())

    # We can use this knowledge to handle when a match is not found and 
    # correclty handle what to do next.
    else:
        if search_result is not None:
            print('\nif: Found a match.', search_result)
        else:
            print('\nif: Did not find a match:', search_result)

        # Or we can use a try/excpet to catch the specific error.
        try:
            print('\ntry:', search_result.group())
        except AttributeError:
            print('\ntry: Did not find a match.')

if False:
    # We can start to use the power of regular expressions with specail
    # characters.
    text = 'someText'

    pattern = r"^someText"
    search_result = re.match(pattern, text)
    print(search_result.group())

    pattern = r"someText$"
    search_result = re.match(pattern, text)
    print(search_result.group())

    pattern = r"^someText$"
    search_result = re.match(pattern, text)
    print(search_result.group())

if False:
    text = 'someTextsomeText'

    pattern = r".*"
    search_result = re.match(pattern, text)
    print(search_result.group())

    pattern = r".+"
    search_result = re.match(pattern, text)
    print(search_result.group())

    pattern = r"^some.*"
    search_result = re.match(pattern, text)
    print(search_result.group())

    pattern = r".*xt+$"
    search_result = re.match(pattern, text)
    print(search_result.group())

    pattern = r".*xt?"
    search_result = re.match(pattern, text)
    print(search_result.group())


if False:
    text = 'abcabcABCCCCCCCabc'

    pattern = r".*abc{1}"
    search_result = re.match(pattern, text)
    print(search_result)

    pattern = r".*ABC{1,5}"
    search_result = re.match(pattern, text)
    print(search_result)

    pattern = r".*A(BC){1}"
    search_result = re.match(pattern, text)
    print(search_result)

    pattern = r".*A(BC)+"
    search_result = re.match(pattern, text)
    print(search_result)

    pattern = r".*A(B|C)"
    search_result = re.match(pattern, text)
    print(search_result)

    pattern = r".*A[BC]"
    search_result = re.match(pattern, text)
    print(search_result)

if False:
    text = 'a more complicated string with 3456 to search.'

    pattern = r"\w"
    search_result = re.match(pattern, text)
    print(search_result)

    pattern = r".*\w"
    search_result = re.match(pattern, text)
    print(search_result)

    pattern = r".*\d"
    search_result = re.match(pattern, text)
    print(search_result)

    pattern = r".*\s"
    search_result = re.match(pattern, text)
    print(search_result)

    pattern = r".*\swith \d\d.+"
    search_result = re.match(pattern, text)
    print(search_result)

if True:
    text = 'abcdeABC123aB'

    pattern = r"^\w{2}"
    search_result = re.match(pattern, text)
    print(search_result)

    pattern = r"([a-z]+)([A-Z]+)(\d+)(\w+)$"
#    pattern = r"^([a-z]{1,5})([A-Z]{1,5})(\d{1,5})(\w{1,5})$"
#    pattern = r"([^A-Z]+)([^a-z]+)(\d+)(\w+)$"
#    pattern = r"([^A-Z]+)([A-Z]+)(\d+)(\w+)$"
    search_result = re.match(pattern, text)
    print(search_result.groups())
    print(type(search_result.groups()))
    first, second, third, fourth = search_result.groups()
    print(first, second, third, fourth)

if False:
    text = 'abB'
    search_result = re.match(r"([a-z]+)([A-Z])", text)
    print(search_result.groups())














