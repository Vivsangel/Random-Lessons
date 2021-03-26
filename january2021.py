#!/usr/bin/env python
# coding: utf-8

# In[1]:


message = "vivensdfadf "


# In[2]:


print(message)


# In[3]:


name = "loveadasf"


# In[4]:


print(name.title())


# In[5]:


name = "viekdf asdfl"
print(name.upper())
print(name.lower())


# In[6]:


first_name = "viek"
second_name ="raina"
full_name =f"{first_name} {second_name}"
print(full_name)


# In[9]:


message =f"Hello,{first_name} {second_name}"


# In[10]:


full_name = "{}{}".format(first_name,last_name)


# In[11]:


print("Language:\nPython\nC\nJavascript")


# In[12]:


print("Language:\n\tPython\n\tC")


# In[13]:


favorite_language ='Pythin '
favorite_language


# In[14]:


favorite_language.rstrip()


# In[15]:


favorite_language


# In[16]:


message = "one of python's strengths is its diverse language"
print(message)


# In[17]:


.1)wer


# In[18]:


2-3


# In[19]:


2++e


# In[20]:


universe_age = 12_32432_23423


# In[21]:


universe_age


# In[22]:


x,y,z = 1,2,3


# In[23]:


x


# In[24]:


y


# In[25]:


MAX_CONNECTIONS = 4004


# In[26]:


MAX_CONNECTIONS


# In[27]:


import this


# In[28]:


#list


# In[29]:


bicycle = ['trek','vive','lkl']


# In[31]:


bicycle


# In[33]:


print(bicycle[0])


# In[34]:


print(bicycle[2])


# In[36]:


print(bicycle[-1])


# In[38]:


print(bicycle(:))


# In[43]:


message = f"My first bicycle was a {bicycle[0].title()}"


# In[44]:


print(message)


# In[45]:


motorcycles = ['honda','yamaha','toyota']
print(motorcycles)


# In[47]:


motorcycles[0] = 'ducati'


# In[48]:


motorcycles


# In[49]:


motorcycles.append('ducati')


# In[50]:


motorcycles


# In[51]:


motorcycles.insert(0,'ducati')


# In[52]:


motorcycles


# In[55]:


del motorcycles[0]


# In[56]:


motorcycles = ['honda','yaradan']


# In[57]:


motorcycles.pop()


# In[58]:


motorcycles.pop()


# In[59]:


motorcycles


# In[60]:


print(f"The last motorcycles was a {last_owned.title()})


# In[61]:


motorcycels.remove('honda')


# In[62]:


cars = ['bsdf','dfdf','dfsdf']


# In[63]:


cars.sort()


# In[64]:


cars


# In[65]:


cars.sort(reverse=True)


# In[66]:


cars


# In[67]:


print("Here is the original list:")


# In[68]:


print(cars)


# In[69]:


print(sorted(cars))


# In[70]:


print("\nHere is the original list:")


# In[71]:


len(cars)


# In[72]:


magicians = ['alice','david','carolina']


# In[73]:


for magician in magicians:
    print(magician)


# In[74]:


magicians = ['ansd','asdf','lfg']
for magician in magicians:
    print(f"{magician.title()},that was a great trick!")


# In[76]:


magicians = ['ansd','asdf','lfg']
for magician in magicians:
    print(f"I can't wait to see your next treat,{magician.title()}.\n")


# In[77]:


for value in range(1,9):
    print(value)


# In[78]:


numbers = list(range(1,6))
print(numbers)


# In[79]:


even_numbers = list(range(2,11,2))


# In[80]:


even_numbers


# In[84]:


squares =[]
for values in range(1,4):
    square = value ** 2
    squares.append(square)
    
print(squares)    


# In[85]:


squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)


# In[86]:


print(square)


# In[87]:


squares = [values**2 for value in range(1,34)]


# In[88]:


squares


# In[89]:


players = ['viv','rain','martina']
print(players[1:3])


# In[90]:


print(players[:])


# In[91]:


print(players[:3])


# In[92]:


print(players[:-4])


# In[93]:


print(players[:-2])


# In[98]:


players = ['charles','martina','michael','florence']

print("Here are thr first three players on my team:")

for player in players[:3]:
    print(player.title())


# In[105]:


my_foods = ['pizza','falafel','carrotcake']
friend_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)
    
   


# In[106]:


print("\nMy friend's favorite foods are:")


# In[107]:


my_foods.append('ice cream')


# In[108]:


my_foods


# In[109]:


#tuple


# In[110]:


dimensions = (234,45)


# In[111]:


print(dimensions[0])


# In[112]:


print(dimensions[1])


# In[113]:


dimensions[1]= wer


# In[114]:


dimensions = (200,34)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)


# In[115]:


print("\nModified dimensions:")


# In[117]:


cars = ['sldf','sdf','vivi','bibf']
for car in cars:
    if car == 'sldf':
        print(car.upper())
    else:
        print(car.lower())


# In[118]:


requested_topping = 'mushrooms'

if requested_topping != 'antichoves':
    print("hod your antichoves")


# In[119]:


answer = 17

if answer != 43:
    print("THAT is the not the correct answer .Please try agaIN!")


# In[120]:


age_1 = 34
age_2 = 44
age_1 == age_2


# In[6]:


available_toppings = ['mushrooms','oilves','green peppers','pepperoni']
requested_toppings = ['mushrooms','french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_toppings}.")
    else:
        print(f"Sorry, we don't have {requested_toppings}.")
        print("\nFinished making your pizza!")


# In[9]:


alien_0 ={'color':'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])


# In[10]:


alien_0 = {'color':'green'}
print(alien_0['color'])


# In[11]:


new_points = alien_0['points']


# In[12]:


print(f"You just earnes {new_points} points")


# In[13]:


alien_0 = {'color':'green','points':5}
prints(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)


# In[17]:


alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = '5'
print(alien_0)


# In[20]:


alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}.")

alien_0['color'] = 'yellow'
print(f"The alien_0 is now {alien_0['color']}.")      


# In[21]:


alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")


# In[26]:


alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")
      
if alien_0['speed'] == 'slow':
      x_increment = 1
elif alien_0['speed'] == 'medium':
      x_increment = 2
else:
      x_increment = 3
alien_0['x_position'] = alien_0['x_position'] + x_increment
      
print(f"New position: {alien_0['x_position']}")      


# In[27]:


alien_0['speed'] ='fast'


# In[28]:


favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}


# In[29]:


langauge = favorite_langauges['sarah'].title()
print(f"Sarah's favorite language is {langauge}.")


# In[30]:


alien_0 = {'color': 'green', 'speed': 'slow'}
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)


# In[31]:


user_0 = {
'username': 'efermi',
'first': 'enrico',
'last': 'fermi',
}
for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")


# In[32]:


for k, v in user_0.items()


# In[35]:


favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}

for name, language in favorite_languages.items():
    
    print(f"{name.title()}'s favorite language is {language.title()}.")


# In[37]:


for name in favorite_languages.keys():
    
    print(name.title())


# In[39]:


friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())


# In[41]:


for name in sorted(favorite_languages.keys()):
     print(f"{name.title()}, thank you for taking the poll.")


# In[44]:


print("The following languages have been mentioned:")
for language in favorite_languages.values():
     print(language.title())


# In[45]:


alien_0 = {'color':'green','points':5}
alien_1 = {'color':'yellow','points':10}
alien_2 = {'color':'red','points':15}

aliens = [alien_0,alien_1,alien_2]

for alien in aliens:
    print(alien)


# In[48]:


aliens = []
for alien_number in range(30):
    new_alien = {'color': 'green','points':5,'speed':'slow'}
    aliens.append(new_alien)
    
for alien in aliens[:5]:
    print(alien)
print(".....")    

print(f"Total number of aliens: {len(aliens)}")


# In[50]:


aliens = []
for alien_number in range(30):
    new_alien = {'color': 'green','points':5,'speed':'slow'}
    aliens.append(new_alien)
    
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    
print(".....")    

print(f"Total number of aliens: {len(aliens)}")


# In[56]:


pizza = {'crust':'thick','toppings': ['mushrooms','extra cheese']}
print(f"You ordered a {pizza['crust']}- crust pizza "
      "with the following toppings:")

for topping in pizza['toppings']:
    print("\t" + topping)


# In[61]:


favorite_languages = {
'jen': ['python', 'ruby'],
'sarah': ['c'],
'edward': ['ruby', 'go'],
'phil': ['python', 'haskell'],}

for name,languages in favorite_languages.items:
        print(f"\n{name.title()}'s favorite languages are:')
    for langauge in langauges:
        print(f"\t{langauge.title()}")  


# In[74]:


users = {
'aeinstein': {
'first': 'albert',
'last': 'einstein',
'location': 'princeton',
},
'mcurie': {
'first': 'marie',
'last': 'curie',
'location': 'paris',
},
}

for username,user_info in users.items():
    
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")               
                   
                   
                   


# In[76]:


message = input("Tell me something, and i will repeat it back to you:")
print(message)


# In[77]:


name = input("Please enter your name: ")
print(f"\nHello, {name}!")


# In[78]:


prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "


# In[79]:


name = input(prompt)


# In[80]:


age = input("How old are you?")


# In[81]:


age = input("How old are you?")


# In[82]:


age>= 18


# In[83]:


age = int(age)
age >=23


# In[84]:


height = input("How tall are you, in inches?")
height = int(height)

if height >= 45:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou be able to ride when you are little older")


# In[86]:


current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1


# In[87]:


active = True
while active:
    message = input(prompt)
    
    if message == 'quit':
        active = False
    else:
        print(message)


# In[88]:


current_number = 0
while current_number <10:
    current_number += 1
    if current_number % 2 == 0:
        continue
        
    print(current_number)    


# In[89]:


x = 1
while x <= 5:
    print(x)
    x += 1


# In[91]:


unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    
    print("fVerifying user: {current_user.title()}")
    confirmed_users.append(current_user)
    
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())    


# In[92]:





# In[ ]:



responses = {}
polling_active = True
while polling_active:
    
    name = input("\nWhat is your name? ")
    response = input("what mountain would you like to scale someday? ")
    
    responses[name]= response
    
    repeat = input("what you like to let another person respond?(yes/no)")
    if repeat == 'no':
        polling_active = False
        
        
print("\n--- Poll Results---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")
    
    
    
    
    
    
    
    


# In[ ]:


def greet_user():
    print("Hello!")
    
greet_user()    


# In[ ]:


from vector_drawing import *
dino_vectors = [(6,4), (3,1), (1,2), (–1,5), (–2,5), (–3,4), (–4,4),
# insert 16 remaining vectors here
]
draw(
Points(*dino_vectors)
)


# In[ ]:


def build_person(first_name,last_name):
    person = {'first':first_name, 'last': last_name}
    return person

musician = build_person('jimi','hendrix')

print(musician)


# In[ ]:


musician


# In[ ]:


def greet_users(names):
    for name in names:
        msg =f"Hello, {name.title()}!"
        print(msg)
        
usernames = ['hannah','ty','margot']
 greet_users(usernames)
        
        


# In[2]:


class Car:
 """A simple attempt to represent a car."""
def __init__(self, make, model, year):
 """Initialize attributes to describe a car."""
self.make = make
self.model = model
self.year = year
self.odometer_reading = 0
def get_descriptive_name(self):
 """Return a neatly formatted descriptive name."""
long_name = f"{self.year} {self.manufacturer} {self.model}"
return long_name.title()
def read_odometer(self):
 """Print a statement showing the car's mileage."""
print(f"This car has {self.odometer_reading} miles on it.")
def update_odometer(self, mileage):
 """
Set the odometer reading to the given value.
Reject the change if it attempts to roll the odometer back.
   """
if mileage >= self.odometer_reading:
self.odometer_reading = mileage
else:
print("You can't roll back an odometer!")
def increment_odometer(self, miles):
"""Add the given amount to the odometer reading."""
self.odometer_reading += miles


# In[6]:


def get_formatted_name(first_name, last_name):
    full_name = f"{first_name}{last_name}"
    return full_name.title()

musician = get_formatted_name('jimi','hendrix')
print('musician')


# In[7]:


def get_formatted_name(first_name,middle_name,last_name):
    full_name = f"{first_name}{middle_name}{last_name}"
    return full_name.title()
musician = get_formatted_name('john','lee','hooker')
print(musician)


# In[10]:


def get_formatted_name(first_name, last_name, middle_name=''):
    
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john','vivek','gisdl;')
print(musician)











# In[11]:


def build_person(first_name,last_name):
    person = {'first': first_name , 'last':last_name}
    return person
musician = build_person('jimi','hendrix')
print(musician)


# In[15]:


def build_person(first_name,last_name, age=None):
    if age:
        person['age'] = age
    return person

musician = build_person('jimi','hendrix', age=23)
print(musician)













# In[16]:


def build_profile(first, last,**user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein', location='princeton' , field= 'physics')
print(user_profile)



# In[1]:


from random import choice
players = ['charles','martina','michael','florence','eli']
first_up = choice(players)
first_up


# In[2]:


first_up


# In[4]:


print("give me two numbers, and i'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\First number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q' :
        break
        
    try:
         answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)























# In[6]:


import json
numbers = [2,4,5,6,7,9]

filename = 'numbers.json'
with open(filename,'w') as f:
    json.dump(numbers,f)


# In[7]:


import json

filename = 'numbers.json'
with open(filename) as f:
    numbers = json.load(f)
    
print(numbers)    


# In[11]:


import json

username = input("what is your name? ")

filename = 'username.json'
with open(filename,'w') as f:
    json.dump(username, f)
    print(f"we'll remenber you whn you come back,{username}!")


# In[12]:


import json

filename = 'username.json'

with open(filename) as f:
    username = json.load(f)
    print(f"welcome back,{username}!")


# In[14]:


def get_formatted_name(first,last):
    full_name= f"{first}{last}"
    return full_name.title()


# In[21]:


from name_function import get_formatted_name

print("Enter 'q' at nay time to quit.")
while True:
    first =input("\nPlease give me a first name: ")
    if first =='q':
        break
    last = input("Please give me a last name: ")
    if last == 'q':
        break
        
    formatted_name = get_formatted_name(first,last)
    print(f"\tNeatly formatted name: {formatted_name}.") 

    
    
    
    


# In[2]:


import numpy as np
import pandas as pd


# In[3]:


url = "https://opendata.socrata.com/api/views/cf4r-dfwe/rows.csv?accessType=DOWNLOAD"


# In[4]:


df = pd.read_csv(url)


# In[5]:


import numpy as np
X = np.arange(0,100)
Y = np.random.randint(0,200, size=X.shape[0])


# In[7]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
plt.plot(X, Y)


# In[8]:


import pandas as pd
df = pd.DataFrame({'x':X, 'y_col':Y})


# In[9]:


plt.plot('x', 'y_col', data=df)


# In[10]:


import seaborn as sns
sns.lineplot(X, Y)
sns.lineplot('x', 'y_col', data=df)


# In[2]:


get_ipython().system('pip install python_marketing_research')


# In[3]:


from python_marketing_research_functions import chapter2


# In[4]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


# In[8]:


x = 5
if x > 2:
        print('x= {}, which is greater than 2'.format(x))
        print('Done!')       


# In[9]:


x = np.array([1,3,4,'a','b'])
print(x)


# In[11]:


a = [3,5,7,5,-34]
x = pd.Series(a)


# In[12]:


x


# In[16]:


store_id = pd.Series([3,4,21,32,54],dtype='category')
store_rev = [543,654,345678,234,789]
store_visits = [45,56,29,45,45]
store_manager = ['ANNIE','Bert','Carla','Dave','Ella']
store_df = pd.DataFrame({'id':store_id,'rev':store_rev,'visits':store_visits,'manager':store_manager})


# In[18]:


store_df


# In[19]:


store_df.corr()


# In[20]:


store_df.describe()


# In[21]:


~np.isnan(x)


# In[22]:


np.mean(x[~np.isnan(x)])


# In[23]:


np.log(np.array([-1.0,1]))


# In[24]:


import pickle
f = open('store_df.pkl','wb')
pickle.dump(store_df,f)
f.close()


# In[25]:


with open('store_df.pkl','wb') as f:
    pickle.dump(store_df,f)


# In[26]:


with open('store_df.pkl', 'rb') as f:
    store_df_reload = pickle.load(f)
store_df_reload    


# In[27]:


store_df.to_csv()


# In[28]:


store_df.to_csv('store_df.csv',index=False)


# In[29]:


store_df_from_csv = pd.read_csv('store_df.csv')


# In[30]:


store_df_from_csv.id = store_df_from_csv.id.astype('category')
store_df_from_csv


# In[ ]:




