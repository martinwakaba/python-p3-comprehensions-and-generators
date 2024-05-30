#!/usr/bin/env python3

def return_evens(num_list):
    even_nums = []
    for num in num_list:
        if num % 2 == 0:
            even_nums.append(num)
    return even_nums if even_nums else []

def make_exclamation(sentence_list):
    for i in range(len(sentence_list)):
        if len(sentence_list) > 0:
            sentence_list[i] += "!"
    return sentence_list if sentence_list else []