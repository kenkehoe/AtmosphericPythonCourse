#! /usr/bin/env python3

import re

if True:
    # The basic searh will return an object if found else None.
    string = "The rain in Spain"
    result = re.search("France", string)
    print('result with "France":', result)
    result = re.search("rain", string)
    print('result with "rain":', result)
    print('result.start():', result.start())
    print()

    # Can also find multiple matches. Notice how the search is case sensitive.
    text = 'those THAT tilt that That 8'
    print('re.findall(r"that", text):', re.findall(r"that", text))
    print('re.findall(r"that", text, flags=re.IGNORECASE):',
          re.findall(r"that", text, flags=re.IGNORECASE))
    print()

    # This is finding all instances of upper or lower case "t".
    print('re.findall(r"[tT]",text):', re.findall(r"[tT]", text))
    pattern = re.compile(r"t", flags=re.IGNORECASE)
    print('re.findall(pattern, text):', re.findall(pattern, text))
    print()

    # This finds all characters in a-z or A-Z using excape character notation
    print(re.findall(r"[\w]", text))
    print()

if False:
    # Here we can take the single string and split into a list of strings. Works
    # the same as .split() modifier. The "\s" means single space.
    string = "The rain in Spain"
    print(re.split("\s", string))

    # This will stop after first character that matches and leave the rest as is.
    print(re.split("\s", string, 1))
    print()

if False:
    # We can also repalce a string with another sting.
    string = "The rain in Spain"
    print(re.sub("\s", "_", string))
    print(re.sub("\s", "_", string, 2))
    print(re.sub(" in ", "_IN_", string))
    print()

    # The returned object has methods to provide information about the matched search.
    string = "The rain in Spain"
    # Here we search for a space and "S" followed by one or more word characters.
    x = re.search(r"\bS\w+", string)
    print(x)
    print(x.span())
    print(x.string)
    print(x.group())
    print()

if False:
    text = 'sometext_with_lots_of_STUFF in it'
    search_result = re.match(r"asdfas", text)

    # A match is found. Printing will show a re object.
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
    # We can start to use the power of regular expressions with special characters.
    text = 'someText'

    # The ^ character indicates start
    pattern = r"^someText"
    search_result = re.match(pattern, text)
    print(search_result.group())

    # The $ character indicates end
    pattern = r"someText$"
    search_result = re.match(pattern, text)
    print(search_result.group())

    # Can use both to be very specific where in the string we should match
    pattern = r"^someText$"
    search_result = re.match(pattern, text)
    print(search_result.group())

    # If it does not match will return None
    text = ' someText '
    pattern = r"^someText$"
    search_result = re.match(pattern, text)
    print(search_result)

if False:
    text = 'someTextsomeText'

    # The "." character means match anything including nothing.
    # The character after "." indicates how many to match. In this case "*" means
    # match 0 or more of them.
    pattern = r".*"
    search_result = re.match(pattern, text)
    print(search_result.group())

    # In this case "*" means match 1 or more of them.
    pattern = r".+"
    search_result = re.match(pattern, text)
    print(search_result.group())

    # Now we can add some complexity. Looks for a string starting with "some" text
    # can return string.
    pattern = r"^some.*"
    search_result = re.match(pattern, text)
    print(search_result.group())

    # Match anything upt to "xt" and then end the string. This will search for for first
    # occurence and if found will return with a match.
    pattern = r".*xt+$"
    search_result = re.match(pattern, text)
    print(search_result.group())

    # Here we search the string for "xt". Since there are two we would normally find the
    # first and return. But here it is saying look for 0 or 1 matches at the end of the
    # string. Since the string ends in "xt" this works. The ? is matching nothing which works.
    pattern = r".*xt?"
    search_result = re.match(pattern, text)
    print(search_result.group())

    # This time we find the first instance of "xt" and stop searching so the second
    # someText is not returned.
    pattern = r".*?xt?"
    search_result = re.match(pattern, text)
    print(search_result.group())

if False:
    text = 'abcabcABCCCCCCCabc'

    # We can now say how many times should we find a pattern wiht {}
    # here we look for the instance of "abc" one time.
    pattern1 = r".*abc{1}"
    search_result = re.match(pattern1, text)
    print("pattern1:", search_result)

    # Here we say we need find 1 to five occurances of the C in ABC.
    # Notice how there are more than 5 C's but only 5 are returned.
    pattern2 = r".*ABC{1,5}"
    search_result = re.match(pattern2, text)
    print("pattern2:", search_result)

    # Here we group what we search for with the multiple occuances. Instead of just
    # the one character next to {} find "BC"
    pattern3 = r".*A(BC){1}"
    search_result = re.match(pattern3, text)
    print("pattern3:", search_result)

    # Here we search for 1 or more patterns that match with the "+"
    pattern4 = r".*A(BC)+"
    search_result = re.match(pattern4, text)
    print("pattern4:", search_result)

    # Here we search for "B" or "C", but the search will be a success on first one found.
    pattern5 = r".*A(B|C)"
    search_result = re.match(pattern5, text)
    print("pattern5:", search_result)

    # Here we look for the letters between B to D.
    pattern6 = r".*A[B-D]"
    search_result = re.match(pattern6, text)
    print("pattern6:", search_result)

if False:
    text = 'a more complicated string with 3456 to search.'

    # Search for first word character.
    pattern = r"\w"
    search_result = re.match(pattern, text)
    print(search_result)

    # Search for 0 or more things ending in a word character. Notice how the one or
    # more search is greedy. It returns as much as possible.
    pattern = r".*\w"
    search_result = re.match(pattern, text)
    print(search_result)

    # Here we are searching for 0 or more charactres ending in a digit not a word character.
    # The one or more search is still greedy and returns the full numer in the string.
    pattern = r".*\d"
    search_result = re.match(pattern, text)
    print(search_result)

    # Here we search for 0 or more and ending in space character.
    pattern = r".*\s"
    search_result = re.match(pattern, text)
    print(search_result)

    # Here things start to run together. There are specal characters in the
    # search ".", "*", "+", some real text "with", " " and some excape characters.
    # Escape characters start with "\" to say the next character is not a character to
    # be matched but should be interpreted as what category to search.
    # \d is a digit, \w is a word character, \s is a space character.
    # This says find 0 or more up to a space follwed by "with " followed by
    # a two digits follwed by 1 or more characters.
    pattern = r".*\swith \d\d.+"
    search_result = re.match(pattern, text)
    print(search_result)

if False:
    text = 'abcdeABC123aB'

    # Here we search for two word characters from the beginning
    pattern = r"^\w{2}"
    search_result = re.match(pattern, text)
    print(search_result)

    # This is using ranges of characters [a-z] means all lower case letters
    # [A-Z] means all upper case letters. When the brackets are follwed by "+"
    # means one or more shoud be found. Same for the \d digit and \w word characters.
    # In addion to what is being found, group the results and return individually.
    # To get the groups we call .groups() on the search result. It will return a tuple
    # of matches. If no matches search_result is set to None.
    # The four patterns all match to the same result.
    pattern = r"([a-z]+)([A-Z]+)(\d+)(\w+)$"
#    pattern = r"^([a-z]{1,5})([A-Z]{1,5})(\d{1,5})(\w{1,5})$"
#    pattern = r"([^A-Z]+)([^a-z]+)(\d+)(\w+)$"
#    pattern = r"([^A-Z]+)([A-Z]+)(\d+)(\w+)$"
    search_result = re.match(pattern, text)
    print(search_result.groups())
    print(type(search_result.groups()))
    print()

    # We can use standard Python syntax to unpack the tuple into varibles directly.
    # Just need to make sure the number of variables match the number of groups we
    # expect to find.
    first, second, third, fourth = search_result.groups()
    print(first, second, third, fourth)

if False:
    text = 'abB'
    search_result = re.match(r"([a-z]+)([A-Z])", text)
    print(search_result.groups())
