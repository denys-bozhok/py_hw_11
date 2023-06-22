def get_menu(menu: list) -> list:
    i = 0

    while i < len(menu):
        print(f"{i + 1} {menu[i].upper()}")

        i += 1

    return menu
