#! /usr/bin/env python3

from collections import OrderedDict, defaultdict, deque, Counter, namedtuple
from datetime import datetime, timedelta


# An ordered dictionary will keep the order of insertion when
# called in a loop. A regular dictionary may or may not follow
# the order of insertion.
if True:
    norm_dict = dict()
    norm_dict['a'] = 1
    norm_dict['b'] = 2
    norm_dict['c'] = 3
    norm_dict['d'] = 4

    ord_dict = OrderedDict()
    ord_dict['one'] = 1
    ord_dict['two'] = 2
    ord_dict['three'] = 3
    ord_dict['four'] = 4

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
    ice_cream = defaultdict(lambda: 'Vanilla')
    ice_cream['Sarah'] = 'Chunky Monkey'
    ice_cream['Abdul'] = 'Butter Pecan'

    print('ice_cream.keys():', ice_cream.keys())
    print('ice_cream["Sarah"]:', ice_cream['Sarah'])
    print('ice_cream["Joe"]:', ice_cream['Joe'])

# Using a default dictionary with the int as the default
# will start at 0. Using increment notation will add a number
# to the default of 0 or the value if one is set. This allows
# using a dictionary as a counter of items.
if False:
    from collections import defaultdict
    food_list = 'spam spam spam spam spam spam eggs spam'.split()
    food_count = defaultdict(int)  # default value of int is 0
    for food in food_list:
        food_count[food] += 1  # increment element's value by 1

    print(food_count)

# Using a default dictionary with a list of tuples allows adding a
# city to a state without needing to define all states initially.
if False:
    from collections import defaultdict
    city_list = [('TX', 'Austin'), ('TX', 'Houston'), ('NY', 'Albany'),
                 ('NY', 'Syracuse'), ('NY', 'Buffalo'), ('NY', 'Rochester'),
                 ('TX', 'Dallas'), ('CA', 'Sacramento'), ('CA', 'Palo Alto'),
                 ('GA', 'Atlanta')]

    cities_by_state = defaultdict(list)
    for state, city in city_list:
        cities_by_state[state].append(city)

    for state, cities in cities_by_state.items():
        print(state, ', '.join(cities))

# deques are much faster at prepending than lists. They also allow faster
# removal of first or lase elements.
if False:
    num = 200000
    list_a = list()
    deque_b = deque()

    start_datetime = datetime.now()
    for ii in range(num):
        list_a.insert(0, ii)
    diff = datetime(1970, 1, 1, 0, 0, 0)+timedelta(seconds=(
        datetime.now()-start_datetime).seconds)
    print('list elapsed time for {} values: '.format(num) +
          diff.strftime("%H:%M:%S"), '\n')
    del list_a

    start_datetime = datetime.now()
    for ii in range(num):
        deque_b.appendleft(ii)
    diff = datetime(1970, 1, 1, 0, 0, 0)+timedelta(seconds=(
        datetime.now()-start_datetime).seconds)
    print('deque elapsed time for {} values: '.format(num) +
          diff.strftime("%H:%M:%S"), '\n')


# A tuple stores information by index number. A named tuple stores information
# by a name for each piece of information.
if False:

    # Create the new named tuple with the named keys.
    Person = namedtuple('Person', 'name age gender')

    bob = Person(name='Bob', age=30, gender='male')
    print('\nRepresentation:', bob)

    jane = Person(name='Jane', age=29, gender='female')
    print('\nField by name:', jane.name)

    print('\nFields by name:')
    for p in [bob, jane]:
        print('{} is a {} year old {}'.format(p.name, p.age, p.gender))

# A counter will automatically count the number of occurances of each letter.
if False:
    c = Counter('abcdaabzyyzz')

    for letter in c:
        print('{} : {}'.format(letter, c[letter]))
