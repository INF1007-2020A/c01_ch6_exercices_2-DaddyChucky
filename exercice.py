#!/usr/bin/env python
# -*- coding: utf-8 -*-


from matplotlib.colors import cnames


def list_to_dict(some_list: list) -> dict:
    # TODO: Transformer la liste en dictionnaire, les éléments de la liste deviennent les clés et leur index deviennent les valeurs
    # for index, elements in enumerate(some_list):
    #     print(index, elements)
    # print(some_list.index())
    return {(index, elements) for index, elements in enumerate(some_list)}


def color_name_to_hex(colors: list) -> list:
    # TODO: Trouver la valeur hex de chaque couleur dans la liste et créer une liste de tupple où le premier élément est le nom de la couleur et le deuxième est la valeur hex
    return [(colors[n], cnames[colors[n]]) for n in range(len(colors))]


def odd_integer_for_loop(end: int) -> list:
    nums = []
    for i in range(end):
        if i % 2 != 0:
            nums.append(i)
    return nums


def odd_integer_list_comprehension(end: int) -> list:
    return [i for i in range(end) if i % 2 != 0]


def loop_traversal(integers: list) -> None:
    print("First list:")
    for index, elements in enumerate(odd_integer_for_loop(13)):
        print(f"Index: {index}, Element: {elements}")

    print("Second list:")
    for index, elements in enumerate(odd_integer_list_comprehension(13)):
        print(f"Index: {index}, Element: {elements}")


def word_dict_for_loop(words) -> dict:
    dico = {}
    for i in range(len(words)):
        dico[words[i][0].upper()] = words[i]
    return dico

def word_dict_comprehension(words) -> dict:
    return {words[letter][0].upper():words[letter] for letter in range(len(words))}


def dictionary_traversal(words: dict) -> None:
    print(words)
    for index, key in enumerate(words):
        print(f"Index: {index}, Key: {key}, Value: {words[key]}")


def main() -> None:
    some_list = ["a", "b", "z", "patate"]
    print(f"La liste suivante {some_list} est transformée en dictionnaire: {list_to_dict(some_list)}")

    colors = ["blue", "red", "green", "yellow", "black", "white"]
    print(f"La valeur hex associée aux couleurs est: {color_name_to_hex(colors)}")

    integer = 13
    integers_for = odd_integer_for_loop(integer)
    print(f"Liste avec boucle for et le nombre 13: {integers_for}")
    integers_comprehension = odd_integer_for_loop(integer)
    print(f"Liste avec list comprehension et le nombre 13: {integers_comprehension}")

    print(f"Les 2 listes sont-elles identiques? {integers_for == integers_comprehension}")
    print(f"Parcours d'une des 2 listes...")
    loop_traversal(integers_for)

    words = ["initialisation", "ajout", "modification", "suppression", "dictionnaire"]
    words_for = word_dict_for_loop(words)
    print(f"Dictionnaire avec la boucle for: {words_for}")
    words_comprehension = word_dict_comprehension(words)
    print(f"Dictionnaire avec le dictionary comprehension: {words_comprehension}")

    print(f"Les 2 dictionnaires sont-ils identiques? {words_for == words_comprehension}")
    print(f"Parcours d'un des 2 dictionnaires...")
    dictionary_traversal(words_comprehension)


if __name__ == '__main__':
    main()
