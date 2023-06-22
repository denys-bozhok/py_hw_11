def gritting(name: str) -> str:
    string = f"Hallo, {name} in our filmsGallery!".upper()

    def greeting_decor():
        decor_string = (len(string) + 4) * '~'
        return decor_string

    result = f"{greeting_decor()}\n" \
             f"* {string} *\n" \
             f"{greeting_decor()}"

    return result
