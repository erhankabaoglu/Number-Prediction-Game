from random import randint
from random import shuffle


def calculateAllPermute(n=4):
    permute = []
    for i in range(10 ** (n - 1), 10 ** n):
        if len(set(parseNumber(i))) < n:
            continue
        permute.append(i)

    dct = {permute[i]: 0 for i in range(len(permute))}
    keys = list(dct.keys())
    shuffle(keys)
    dct = {keys[i]: dct[keys[i]] for i in range(len(keys))}
    return dct


def calculateOccurrence(predicted, dct, poz, neg):
    p_number = parseNumber(predicted)

    for keys in dct.keys():
        p_keys = parseNumber(keys)
        if ensure(p_keys, p_number, poz, neg):
            dct[keys] += 1
        else:
            dct[keys] -= 1


def parseNumber(number):
    temp = str(number)
    x = [i for i in temp]
    return x


def ensure(key, predicted, poz, neg):
    poz_one = 0
    for i, j in zip(key, predicted):
        if i == j:
            poz_one += 1

    matches = set(key) & set(predicted)
    neg_one = len(matches) - poz_one
    if poz_one == poz and neg_one == neg:
        return 1
    return 0


def calculateScore(number, predicted):
    poz_one = 0
    p_number = parseNumber(number)
    p_predicted = parseNumber(predicted)
    for i, j in zip(p_number, p_predicted):
        if i == j:
            poz_one += 1
    matches = set(p_number) & set(p_predicted)
    neg_one = len(matches) - poz_one
    return poz_one, neg_one


def selectNumber(dct):
    dct = {k: v for k, v in sorted(dct.items(), key=lambda item: item[1], reverse=True)}
    next_ = next(iter(dct.keys()))
    dct.pop(next_)
    return next_, dct


def start(n=4):
    count = 0
    number = 9628
    dct = calculateAllPermute()
    while True:
        predicted = randint(10 ** (n - 1), 10 ** n)
        if len(set(parseNumber(predicted))) == n:
            break

    while True:
        count += 1
        if number == predicted:
            return
        poz, neg = calculateScore(number, predicted)
        calculateOccurrence(predicted, dct, poz, neg)
        predicted, dct = selectNumber(dct)
