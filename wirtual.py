import requests
import json
from win11toast import toast
import time
import sys, os

n = int(sys.argv[1])

def run_message(floor):
     toast(f'Wirtual got to floor {floor}!!!', 
           image='C:/Users/48503/Desktop/TYMSON/Wirtual/wicked.jpg',
           button={'activationType': 'protocol', 'arguments': 'https://www.twitch.tv/wirtual', 'content': 'Open the stream'},
           app_id='Wirtual cooking 0_0')
     
def which_floor():
      url = 'https://files.deepdip2.com/user.json'
      page = requests.get(url)
      text = json.loads(page.text)
      floor = int(text["currentFloor"])
      return floor

def blockPrint():
    sys.stdout = open(os.devnull, 'w')

def enablePrint():
    sys.stdout = sys.__stdout__


try:
      prev_floor = None
      while True:
            floor = which_floor()
            if floor != prev_floor:
                  print(f'Currently on floor {floor}...')
            prev_floor = floor

            if floor >= n:
                  blockPrint()
                  run_message(floor)
                  enablePrint()
                  while True:
                        floor = which_floor()

                        if floor < n:
                              print(f'Reached floor {prev_floor} and fell down to floor {floor}.')
                              break

                        if floor != prev_floor:
                              print(f'Currently on floor {floor}...')

                        prev_floor = floor
                        time.sleep(30)
                  prev_floor = floor
            time.sleep(30)
except KeyboardInterrupt:
      print("Session closed")
