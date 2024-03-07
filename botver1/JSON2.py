import json

second_bd = """
    {
        "pk": 30,
        "id_telegram": "000000000",
        "managers":
        [
            {
                "id": 11,
                "id_manager_name": {
                    "id": 1,
                    "name": "РОО"
                },
                "id_telegram": {
                    "id": 30,
                    "name": "Al AL",
                    "id_telegram": "000000000",
                    "nik_name": "ALEXALEX",
                    "first_name": "Алексей",
                    "last_name": "Попов",
                    "job_title": 25
                },
                "name": "Видеоматериал",
                "number": "17",
                "factors": [
                    29,
                    8
                ]
            }
        ],
        "last_name": "Попов",
        "first_name": "Алексей",
        "name": "ALEXALEX"
    }"""


print(type(second_bd))

data = json.loads(second_bd)
print(type(data))
print(data)

with open('json2.json', 'w') as file:
    json.dump(data, file, indent=3)