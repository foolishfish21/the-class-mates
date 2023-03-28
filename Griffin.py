import requests
import time
import random
input("wanna hear a joke?")
connector=["funny, right?","haha!","now thats good!", "I bet you've never heard that one before!","I'm good at this.", "not bad huh?", "sorry..."]
confirm=["good","perfect","wonderfull","good idea","allright","nice"]
time.sleep (1)
print(confirm[random.randint(0,5)])
time.sleep(2)

while True:
  response =   requests.get('https://icanhazdadjoke.com/',   headers={'Accept': 'application/json'})

  data = response.json()

  joke = data['joke']

  print(joke)
  time.sleep(2)
  print(connector[random.randint(0,7)])
  input("wanna hear another joke")


