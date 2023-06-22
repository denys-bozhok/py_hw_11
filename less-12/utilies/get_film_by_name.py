def get_film_by_name(arr, er):
    is_incorrect = True

    while is_incorrect:

        serch_by_name = input("Enter film name for see info:\n")

        for el in arr:
            if el["title"] == serch_by_name:

                print(f"{len(el['title']) * '*'}\n"
                      f"{el['title'].upper()}\n"
                      f"{len(el['title']) * '*'}\n")

                for key, value in el.items():
                    if serch_by_name == value:
                        continue

                    print(f"{key} : {value}")

                    is_incorrect = False

                return is_incorrect

        print(f"{er}. Please enter film name :\n")

    return
