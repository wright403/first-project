import random 
Destinations = ['las vegas', 'New york city','Marine corps bootcamp', 'california']

restaurants = [' longhorn steakhouse', 'texas roadhouse', 'chow hall', 'bahama breeze']

transportations = ['rental car', 'train', 'bus']

entertainments = ['concert', 'skydiving', 'night club', 'lasertag']

def welcome():
    print('welcome to the day trip generator!')
welcome()

def randomizer(list):
    result = random.choice(list)
    user_input = input(f'for your trip we have selected {result}. Enter 1 to confirm and 2 to see a new option. ')
    hasConfirmed = False
    while hasConfirmed == False:         # False = False is a True statement just like True = True is
        if user_input == "1":
            hasConfirmed = True
            return result
        elif user_input == "2":
            result = random.choice(list)
            user_input = input(f'for your trip we have selected {result}. Enter 1 to confirm and 2 to see a new option. ')    

destResult = randomizer(Destinations)   # build 3 more of these, one for each list. After build a string using concatination to describe the trip to the user.
restResult = randomizer(restaurants)
transResult = randomizer(transportations)
enterResult = randomizer(entertainments)


def the_destination(destination):
    if destination == 'las vegas':
        print('thank you for choosing las vegas! thats a great choice. lets move on')
    elif destination == 'New york city':
        print('thank you for choosing new york city! lets move on')
    elif destination == 'Marine corps bootcamp':
        print('this is the worst decision you could have made. sorry lets move on')
    elif destination == 'california':
        print('thank you for choosing california! lets move on')

the_destination(destResult)


def the_restaurant(restaurant):
    if restaurant == 'longhorn steakhouse':
        print('thats a great choice! lets move on')
    elif restaurant == 'texas roadhouse':
        print('thats a great choice! lets move on')
    elif restaurant == 'chow hall':
        print('thats a great choice! lets move on')
    elif restaurant == 'bahama breeze':
        print('thats a great choice! lets move on')

the_restaurant(restResult)

def the_transportation(transportation):
    if transportation == 'rental car':
        print('We have a chevy corvette waiting for you')
    elif transportation == 'train':
        print('we have several train stations across the city')
    elif transportation == 'bus':
        print('not my first choice but we have tons of buses across the city')

the_transportation(transResult)

def the_entertainment(entertainment):
    if entertainment == 'concert':
        print('we have an eminem concert going on')
    elif entertainment == 'skydiving':
        print('you are brave')
    elif entertainment == 'nightclub':
        print('we have several nightclubs around the city')
    elif entertainment == 'lasertag':
        print('our personal favorite! we have two locations in the city')

the_entertainment(enterResult)

def trip():
    print('congratulations! your trip is complete now lets confirm you got everything you wanted')
trip()

def tripp(firstdestination):
    print('the trip we have generated for you is:')
    print(f'your destination is {firstdestination}')
tripp(destResult)

def vaca(secdestination):
    print(f'your restaurant is {secdestination}')
vaca(restResult)

def free(thirddestination):
    print(f' your transportation is {thirddestination}')
free(transResult)

def mytrip(fourthdestination):
    print(f'your entertainment is {fourthdestination}')
mytrip(enterResult)

def finaltrip():
    my_input = input("would you like to finalize your trip? enter y or n")
    myconfirm = False
    if my_input == 'y':
        print(f'your dreams will soon be realized! you are going to {destResult} you will eat at {restResult} you will be picked up by {transResult} you will be entertained by {enterResult}')
        myconfirm == True
    elif my_input == 'n':
        print('what seems to be the problem I did everything you asked')
finaltrip()        



            










