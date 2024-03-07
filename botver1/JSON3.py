import json

third_bd = """
   {
        "factor":
            [
                {
                    "id": 29,
                    "name": "Работа в рамках СПЭП",
                    "number": "0"
                },
                {
                    "id": 8,
                    "name": "Видео инцидента",
                    "number": "7"

                }
            ]
    } """


print(type(third_bd))

data = json.loads(third_bd)
print(type(data))
print(data)

with open('json3.json', 'w') as file:
    json.dump(data, file, indent=3)