import requests

base_url = "https://pokeapi.co/api/v2/"

def get_poke_info(name):
  whole_url = f"{base_url}/pokemon/{name}"
  response = requests.get(whole_url)

  if response.status_code == 200:
    data = response.json()
    return data
  else:
    print("data not found")
  

name = "pikachu"
poke_data = get_poke_info(name)

print("Name:",poke_data["name"])
print("Height:",poke_data["height"])
print("Weight:",poke_data["weight"])
abilities = poke_data["abilities"][1]
abi_values = abilities['ability']
#print(abilities['ability'])
print("ability name:",abi_values["name"])
