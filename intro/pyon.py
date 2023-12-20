import json

def create_json():
    file = open("data.json", mode="w")

    file.write(
        """
        {
            "field":"value",
            "array":[1,2,3],
            "float":2.23,
            "null":null,
            "true":true,
            "false":false,
            "obj":{
                "field":"value"
            }
        }
    """
    )

def print_json():
    with open("data.json") as file:
        pyon = json.load(file)
        print(pyon)


print_json()