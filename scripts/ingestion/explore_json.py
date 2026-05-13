import json

with open("data/raw/incoming/search_results_official.json", "r") as file:
    data = json.load(file)

print("TOP LEVEL TYPE:", type(data))

if isinstance(data, list):
    print("TOP LEVEL LENGTH:", len(data))

    first_item = data[0]
    print("\nFIRST ITEM TYPE:", type(first_item))

    if isinstance(first_item, dict):
        print("FIRST ITEM KEYS:", first_item.keys())

    elif isinstance(first_item, list):
        print("FIRST ITEM LENGTH:", len(first_item))
        print("FIRST INNER ITEM TYPE:", type(first_item[0]))

        if isinstance(first_item[0], dict):
            print("FIRST INNER ITEM KEYS:", first_item[0].keys())

elif isinstance(data, dict):
    print("TOP LEVEL KEYS:", data.keys())
