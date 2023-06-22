def get_sorted_list(films: list):
    arr_length = len(films)

    def swap(arr: list, first_el, second_el):

        first_el_copy = arr[first_el]
        arr[first_el] = arr[second_el]
        arr[second_el] = first_el_copy

        return arr

    for film_i in range(arr_length):
        for film_el in range(arr_length):
            if films[film_el]["rating"] < films[film_i]["rating"]:
                arr = swap(films, film_i, film_el)

    result = swap(films, film_i, film_el)

    return result
