# create a mapping of state to abbreviation
states = [
    'Madhya Pradesh': 'MP',
    'Maharashtra': 'MH',
    'Uttar Pradesh': 'UP',
    'Kerla': 'KL',     
    'Orissa': 'OR'
]

  
# create a basic set of states and some cities in them
cities = [
       'UP': 'Agra',
       'OR': 'Bhuwneshwar',
       'MH': 'Mumbai'
]

  
# add some more cities
cities['KL'] = 'Thrissur'
cities['MP'] = 'Bhopal'

# print out some cities
print '- ' * 10
print "KL State has: ", cities['KL']
print "MP State has: ", cities['MP']

  
# print some states
print '- ' * 10
print "Orissa's abbreviation is: ", states['Orissa']
  
print "Maharashtra's's abbreviation is: ", states['Maharashtra']

  
# do it by using the state then cities dict
print '- ' * 10
print "Orissa has: ", cities[states['Orissa']]
print "Maharashtra has: ", cities[states['Maharashtra']]

  
# print every state abbreviation
print '- ' * 10
for state, abbrev in states.items():
     print "%s is abbreviated %s" % (state, abbrev)

  
# print every city in state
print '- ' * 10
for abbrev, city in cities.items():
       print "%s has the city %s" % (abbrev, city)

  
# now do both at the same time
print '- ' * 10
for state, abbrev in states.items():
     print "%s state is abbreviated %s and has city %s" % (
           state, abbrev, cities[abbrev])

print '- ' * 10
# safely get an abbreviation by state that might not be there
state = states.get('Indore', None)

  
if not state:
   print "Sorry, no Indore."

   # get a city with a default value
city = cities.get('IN', 'Does Not Exist')
print "The city for the state 'IN' is: %s" % city