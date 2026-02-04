import json

data = [
{
    "playerID": 1,
    "name": "Pharsa",
    "type": "Mage",
    "attackLevel": 9
  },
  {
    "playerID": 2,
    "name": "Lesley",
    "type": "Marksman",
    "attackLevel": 15
  },
  {
    "playerID": 3,
    "name": "Lancelot",
    "type": "Assassin",
    "attackLevel": 20
  }
]


filepath = 'data.json'

with open(filepath, 'r') as file:
    data = json.load(file)

if 'playerID' in data:
    del data['playerID']

with open(filepath, 'w') as file:
    json.dump(data, file, indent=4)