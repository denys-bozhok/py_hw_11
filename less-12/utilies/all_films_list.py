def shaw_all_films(arr: list):
    i = 0

    for el in arr:
        for key, value in el.items():

            if key == "title":
                i += 1
                print(f"{i}) {value}".upper())

