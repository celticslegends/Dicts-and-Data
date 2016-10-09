new_england_states = {
    'Maine': 'ME',
    'Vermont': 'VT',
    'Massachusetts': 'MA',
    'Connecticut': 'CT',
    'Rhode Island': 'RI',
    'New Hampshire': 'NH'
}

cities = {
    'MA': 'Boston',
    'NH': 'Manchester',
    'CT': 'Hartford',
    'VT': 'Burlington',
    'ME': 'Portland',
    'RI': 'Providence'
}

cities['MA'] = 'Boston'
cities['NH'] = 'Portsmouth'

print '-' * 10
print "MA Commonwealth has: ", cities['MA']
print "NH Live Free or Die has: ", cities['NH']

print '-' * 10
print "New Hampshire's abbreviation is: ", new_england_states['New Hampshire']
print "Maine's abbreviation is: ", new_england_states['Maine']

print '-' * 10
print "Connecticut has: ", cities[new_england_states['Connecticut']]
print "Rhode Island has: ", cities[new_england_states['Rhode Island']]

print '-' * 10
for state, abbrev in new_england_states.items():
    print "%s abbreviation is %s" % (state, abbrev)

print '-' * 10
for abbrev, city in cities.items():
    print "%s biggest city is %s" % (abbrev, city)

print '-' * 10
for state, abbrev in new_england_states.items():
    print "%s state abbreviated is %s and has %s as it's biggest city." % (
        state, abbrev, cities[abbrev])

print '-' * 10
state = new_england_states.get('Florida')

if not new_england_states:
    print "I'm sorry, but there is no state named Florida in your list."

city = cities.get('FL', 'Does Not Exist')
print "The city for the state 'FL' is: %s" % city
