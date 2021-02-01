# -*-encoding=utf-8-*-

import cv2

def process_words(words):
    words = words[1:-1]
    words = words.split(',')
    words = list(map(lambda x: x[1:-1], words))
    return words


def judge(n_a, word, number):
    word = list(word)
    tmp = ""
    for alp in word:
        for key, value in n_a.items():
            if alp in value:
                tmp = tmp + key
                break
    if tmp in number:
        return True
    else:
        return False


if __name__ == "__main__":
    number_alphabet = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z'],
    }
    res = []
    phoneNumber = input()
    words = input()
    words = process_words(words)
    for word in words:
        if judge(number_alphabet, word, phoneNumber):
            res.append(word)

    res.sort()
    print("===========================output===========================")
    print(res)
