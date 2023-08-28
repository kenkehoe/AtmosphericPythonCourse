#! /usr/bin/env python3

# First notice we are importing the fuctions from the "collections" class.
# We need to do this to gain access to the functions. They are not part of
# the default name space.
from collections import OrderedDict, defaultdict, deque, Counter, namedtuple
from datetime import datetime, timedelta


# An ordered dictionary will keep the order of insertion when
# called in a loop. A regular dictionary may or may not follow
# the order of insertion.
if True:
    norm_dict = dict()
    norm_dict["a"] = 1
    norm_dict["b"] = 2
    norm_dict["c"] = 3
    norm_dict["d"] = 4

    ord_dict = OrderedDict()
    ord_dict["one"] = 1
    ord_dict["two"] = 2
    ord_dict["three"] = 3
    ord_dict["four"] = 4

    for key, value in norm_dict.items():
        print(key, value)

    for key, value in ord_dict.items():
        print(key, value)

# A default dictionary will allow setting a default value for any
# new entry. This includes when the key does not exist. So when
# the dictionary is called without a key it is added to the dictionary
# with the default value as the value.
if False:

    # Create the default dictionary and use lambda to set the default
    # value to use if created with no value.
    ice_cream = defaultdict(lambda: "Vanilla")
    ice_cream["Sarah"] = "Chunky Monkey"
    ice_cream["Abdul"] = "Butter Pecan"

    print("ice_cream.keys():", ice_cream.keys())
    print('ice_cream["Sarah"]:', ice_cream["Sarah"])
    print('ice_cream["Joe"]:', ice_cream["Joe"])

# Using a default dictionary with the int as the default
# will start at 0. Using increment notation will add a number
# to the default of 0 or the value if one is set. This allows
# using a dictionary as a counter of items.
if False:
    from collections import defaultdict

    food_list = "spam spam spam spam spam spam eggs spam".split()
    food_count = defaultdict(int)  # default value of int is 0
    print('food_count:', food_count)
    for food in food_list:
        food_count[food] += 1  # increment element's value by 1

    print(food_count)

# Using a default dictionary with a list of tuples allows adding a
# city to a state without needing to define all states initially.
if False:
    from collections import defaultdict

    city_list = [
        ("TX", "Austin"),
        ("TX", "Houston"),
        ("NY", "Albany"),
        ("NY", "Syracuse"),
        ("NY", "Buffalo"),
        ("NY", "Rochester"),
        ("TX", "Dallas"),
        ("CA", "Sacramento"),
        ("CA", "Palo Alto"),
        ("GA", "Atlanta"),
    ]

    cities_by_state = defaultdict(list)
    print('cities_by_state:', cities_by_state)
    for state, city in city_list:
        # The .append() method is adding the city name to the end
        # of the list stored in a dictionary with the state name as the key.
        cities_by_state[state].append(city)

    for state, cities in cities_by_state.items():
        print(state, ", ".join(cities))

# deques are much faster at prepending than lists. They also allow faster
# removal of first element. They are helpful when adding and removing to
# both front and end of a list of items.
if False:
    num = 200000
    list_a = list()
    deque_b = deque()

    start_datetime = datetime.now()
    for ii in range(num):
        list_a.insert(0, ii)

    diff = datetime(1970, 1, 1, 0, 0, 0) + timedelta(
        seconds=(datetime.now() - start_datetime).seconds)
    print("list elapsed time for prepending {} values: ".format(num) +
          diff.strftime("%H:%M:%S"), "\n")

    start_datetime = datetime.now()
    for ii in range(num):
        deque_b.appendleft(ii)

    diff = datetime(1970, 1, 1, 0, 0, 0) + timedelta(
        seconds=(datetime.now() - start_datetime).seconds)
    print("deque elapsed time for prepending {} values: ".format(num) +
          diff.strftime("%H:%M:%S"), "\n")

    start_datetime = datetime.now()
    while len(list_a) > 0:
        list_a.pop(0)

    diff = datetime(1970, 1, 1, 0, 0, 0) + timedelta(
        seconds=(datetime.now() - start_datetime).seconds)
    print("list elapsed time for poping first element of {} values: ".format(num) +
          diff.strftime("%H:%M:%S"), "\n")

    start_datetime = datetime.now()
    while len(deque_b) > 0:
        deque_b.popleft()

    diff = datetime(1970, 1, 1, 0, 0, 0) + timedelta(
        seconds=(datetime.now() - start_datetime).seconds)
    print("deque elapsed time for poping first element of {} values: ".format(num) +
          diff.strftime("%H:%M:%S"), "\n")

# A tuple stores information by index number. A named tuple stores information
# by a name for each piece of information.
if False:

    # Create the new named tuple with the named keys.
    Person = namedtuple("Person", "name age gender")

    bob = Person(name="Bob", age=30, gender="male")
    print("\nRepresentation:", bob)

    jane = Person(name="Jane", age=29, gender="female")
    print("\nField by name:", jane.name)

    print("\nFields by name:")
    for p in [bob, jane]:
        print("{} is a {} year old {}".format(p.name, p.age, p.gender))

# A counter is a container that keeps track of how many times values are added.
# The standard use is with letters.
if False:
    # There are three ways to initialize a counter object
    list_counter = Counter(['a', 'b', 'c', 'a', 'b', 'b'])
    dict_counter = Counter({'a':2, 'b':3, 'c':1})
    keyword_couner = Counter(a=2, b=3, c=1)

    # Can creaet an empty counter and then update with a second call.
    # This looks a little strange with the input being a single string,
    # but the update expects a list object. If a string is entered it
    # will automatically convert to a list. When Python converts a single
    # sting to a list all the charactrs are separated into individual
    # elements. Go ahead and try print(list('abcabb')).
    empty_counter = Counter()
    empty_counter.update('abcabb')

    for counter_element in [list_counter, dict_counter, keyword_couner, empty_counter]:
        print(counter_element)

    # As new data is added the couner is updated.
    empty_counter.update(['a', 'd'])
    print('\nUpdated counter:', empty_counter)

if False:
    # But we can also use the counter on full words.

    # Start off with a sentence.
    my_str = "This this this is really really good."
    print('myStr:', my_str)
    # Next split the single string of a sentence into a list of words
    # by splitting at white spaces. The .split() method assumes whitespace
    # if no delimiter is provided.
    my_list = my_str.split()
    print('my_str:', my_str)

    # Now use the list of words as input into the Counter. It will
    # return a dictionary with the words as keys and values as number
    # of times that word is counted. Notice how the count is case sensitive.
    my_dict = Counter(my_list)
    print('myDict:', my_dict)

    # To remove case sensitive counter just lower the calse of all characters
    # befor entering into the Counter()
    my_lower_case_list = [ii.lower() for ii in my_list]
    my_lower_case_dict = Counter(my_lower_case_list)
    print('my_lower_case_dict:', my_lower_case_dict)

if False:
    # A counter will also work with numbers other objects.
    my_numbers = [0, 1, 2, 3, 4, 4, 4, 55, 67, 67, 10242425242552]
    number_dict = Counter(my_numbers)
    print('number_dict:', number_dict)

    # To just see the n number of most common use the .most_common() method.
    # Notice how the type is different. It is no longer a dictionary but a
    # list of tuples. This is important when you want to extract the values
    # and use them. They will be extracted with different syntax.
    print('number_dict.most_common(2):', number_dict.most_common(2))

    # convert to a regular dictionary
    number_dict_most_common_as_dict = dict(number_dict.most_common(2))
    print('number_dict_most_common_as_dict:', number_dict_most_common_as_dict)

    # Here is a list of the more common patterns used with Counters()
    total = sum(number_dict.values())  # total of all counts
    print('total:', total)
    # list unique elements or "keys" if that is easier to understand
    number_dict_list = list(number_dict)
    print('number_dict_list:', number_dict_list)

    # Reset all counts, or essentially just make number_dict set to None
    number_dict = number_dict.clear()
    print('number_dict:', number_dict)

if False:
    # Counters have the ability to perform mathematical operations from within
    # the Counter object.
    c = Counter(Tom=3, Jerry=1)
    d = Counter(Tom=1, Jerry=2, Scooby=4)

    c_plud_d = c + d  # add two counters together:  c[x] + d[x]
    c_minus_d = c - d  # subtract (keeping only positive counts)
    c_intersect_d = c & d  # intersection:  min(c[x], d[x]) 
    c_union_d = c | d  # union:  max(c[x], d[x])

    print('c_plud_d:', c_plud_d)
    print('c_minus_d:', c_minus_d)
    print('c_intersect_d:', c_intersect_d)
    print('c_union_d:', c_union_d)
