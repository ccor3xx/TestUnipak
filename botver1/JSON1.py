import json

first_bd = """{
        "id": 1,
        "date_release": "28.06.2023",
        "id_overrun_pieces": {
            "id": 5,
            "name": "Шт -"
        },
        "id_overrun_kg": {
            "id": 6,
            "name": "---"
        },
        "id_work_item": {
            "id": 2,
            "id_GN": {
                "id": 3,
                "name": "GN2220C/B",
                "number": 3
            },
            "id_factory_change": {
                "id": 3,
                "name": "Смена В"
            },
            "id_factory_type_change": {
                "id": 2,
                "name": "Дневная"
            },
            "responsible_person_material": "Борисова Надежда Вячеславовна",
            "responsible_person_item": "Борисова Надежда Вячеславовна",
            "comment_item": "Материал - выработка всего материала,",
            "comment_material": "Качество - факт. толщина ленты ниже номинальной (по факту:___), 0,69-0,71; шаг т/к 12; факт 11-12 мм",
            "personal": "Борисова Надежда Вячеславовна",
            "job_title": {
                "id": 29,
                "title": "Начальник смены"
            },
            "id_item": {
                "id": 7,
                "name": "Т313 Д",
                "create_date": "2023-06-28",
                "vendor_code": 63511
            },
            "id_material": {
                "id": 23,
                "name": "ПС505*0,7",
                "create_date": "2023-06-28"
            },
            "date_release": "28.06.2023",
            "item_plan_count": "0",
            "item_fact_count": "0",
            "material_plan_kg": "0",
            "material_fact_kg": "0",
            "material_plan_based_on_fact_kg": "0",
            "date_create": "2023-06-29"
        },
        "date_create": "2023-06-29",
        "deviation_item_count": "0",
        "deviation_material_kg": "0",
        "deviation_material_kg_percent": "0"
    }
"""
print(type(first_bd))

data = json.loads(first_bd)
print(type(data))
print(data)

with open('json1.json', 'w') as file:
    json.dump(data, file, indent=3)
