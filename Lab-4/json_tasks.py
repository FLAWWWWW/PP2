import json

with open('sample_data.json', 'r') as file:
    data = json.load(file)

print("Interface Status")
print("=" * 80)
print("DN                                             Description            Speed       MTU")
print("-" * 80)

for entry in data["imdata"]:
    attributes = entry["l1PhysIf"]["attributes"]
    dn = attributes["dn"]
    descr = attributes["descr"]
    speed = attributes["speed"]
    mtu = attributes["mtu"]
    print(f"{dn}                 {descr}         {speed}         {mtu}")