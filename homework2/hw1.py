"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
from typing import List
from math import inf


def get_longest_diverse_words(file_path: str) -> List[str]:
    """
    Find 10 longest words consisting from largest amount of unique symbols
    :param file_path: name and path of text file
    :return: list of the longest words
    """
    dict_length = {}
    with open(file_path, encoding='unicode_escape', errors="ignore") as fi:
        for line in fi:
            line_list = line.split()
            for word in line_list:
                if dict_length.get(len(set(word))) is None:
                    dict_length[len(set(word))] = [word]
                else:
                    dict_length[len(set(word))].append(word)
    list_key_sorted = sorted(dict_length, reverse=True)
    list_resulted = []
    for key in list_key_sorted:
        while dict_length[key] and len(list_resulted) < 10:
            list_resulted.append(dict_length[key].pop(0))
        else:
            continue
    return list_resulted


def get_rarest_char(file_path: str) -> str:
    """
    Find the rarest symbol for document, take first symbol if the same value
    :param file_path: name and path of text file
    :return: the rarest symbols in text
    """
    dict_symbols = {}
    with open(file_path, encoding='unicode_escape', errors="ignore") as fi:
        for line in fi:
            line_list = line.split()
            for word in line_list:
                for symbol in word:
                    if symbol not in dict_symbols.keys():
                        dict_symbols[symbol] = 1
                    else:
                        dict_symbols[symbol] += 1
    min_value = inf
    min_key = ""
    for keys in dict_symbols.keys():
        if dict_symbols[keys] < min_value:
            min_value = dict_symbols[keys]
            min_key = keys
    return min_key


def count_punctuation_chars(file_path: str) -> int:
    """
    counting amount of punctuation chars in text file
    use ascii punctuation chars from 33 to 48
    :param file_path: name and path of text file
    :return: number of symbols in text
    """
    symbol_counter = 0
    with open(file_path, encoding='unicode_escape', errors="ignore") as fi:
        for line in fi:
            line_list = line.split()
            for word in line_list:
                for symbol in word:
                    if 33 <= ord(symbol) <= 48:
                        symbol_counter += 1
    return symbol_counter


def count_non_ascii_chars(file_path: str) -> int:
    """
    count every non ascii char in text file
    :param file_path: name and path of text file
    :return: number of  non ascii symbols in text
    """
    symbol_counter = 0
    with open(file_path, encoding='unicode_escape', errors="ignore") as fi:
        for line in fi:
            line_list = line.split()
            for word in line_list:
                for symbol in word:
                    if not 0 <= ord(symbol) <= 127:
                        symbol_counter += 1
    return symbol_counter


def get_most_common_non_ascii_char(file_path: str) -> str:
    """
    find most common non ascii char in text file
    :param file_path: name and path of text file
    :return: symbol
    """
    nonascii_dict = {}
    with open(file_path, encoding='unicode_escape', errors="ignore") as fi:
        for line in fi:
            line_list = line.split()
            for word in line_list:
                for symbol in word:
                    if not 0 <= ord(symbol) <= 127:
                        if symbol not in nonascii_dict.keys():
                            nonascii_dict[symbol] = 1
                        else:
                            nonascii_dict[symbol] += 1
    max_value = -inf
    max_key = ""
    for key in nonascii_dict.keys():
        if nonascii_dict[key] > max_value:
            max_value = nonascii_dict[key]
            max_key = key
    return max_key

