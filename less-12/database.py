from utilies import random_id, get_user_name


user = {
    "name": get_user_name.get_user_name(),
    "favorite_list": []
}

menu_list = [
    [
        "menu",
        "film by name",
        "sorted list",
        "quit"],
    [
        "all films",
        "back"
    ],
    [
        "by upper to lower rating"
        "by lower to upper rating"
    ],
    [
        "from upper to lower",
        "from lower to upper"
    ]
]

films = [
    {
        "author": "brothers/sisters Wachowski",
        "title": "Matrix",
        "rating": 10000000,
        "id": random_id.get_random_id()
    },
    {
        "author": "C. Nolan",
        "title": "Inception",
        "rating": 10,
        "id": random_id.get_random_id()
    },
    {
        "author": "L. Besson",
        "title": "Taxi",
        "rating": 6,
        "id": random_id.get_random_id()
    },
    {
        "author": "G. Ritchie",
        "title": "Cards money two guns",
        "rating": 9,
        "id": random_id.get_random_id()
    },
    {
        "author": "K. Tarantino",
        "title": "Pulp Fiction",
        "rating": 7,
        "id": random_id.get_random_id()
    },
    {
        "author": "J. Cameron",
        "title": "Terminator 2",
        "rating": 8,
        "id": random_id.get_random_id()
    },
    {
        "author": "P. Buslov",
        "title": "Bumer",
        "rating": 0.1,
        "id": random_id.get_random_id()
    }
]
