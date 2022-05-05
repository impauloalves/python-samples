# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries

# Create dict
person = {
    'first_name': 'Paulo',
    'last_name': 'Alves',
    'age': 27
}

# Use constructor
#person2 = dict(first_name='Paulo', last_name='Alves', age=27)

# Get value
print(person['first_name'])
print(person.get('last_name'))

# Add key/value
person['phone'] = '555-555-5555'

# Get dict keys
print(person.keys())

# Get dict items
print(person.items())

# Copy dict
person2 = person.copy()
person2['city'] = 'Boston'

# Remove item
del(person['age'])
person.pop('phone')

# Clear
person.clear()

# Get length
print(len(person2))

# List of dict
people = [
    {
        'name': 'Paulo',
        'age': 27
    },
    {
        'name': 'Alves',
        'age': 26
    }
]

print(people[1]['name'])
