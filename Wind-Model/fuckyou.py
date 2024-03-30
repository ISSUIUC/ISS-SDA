import json

with open("./out.json", "r") as of:
    all_data = of.read()

    data = json.loads(all_data)

    print(json.dumps(data['hours'][0]))