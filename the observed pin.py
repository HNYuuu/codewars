import itertools

pin = {
    '0': ['8', '0'],
    '1': ['1', '2', '4'],
    '2': ['1', '2', '3', '5'],
    '3': ['2', '3', '6'],
    '4': ['1', '4', '5', '7'],
    '5': ['2', '4', '5', '6', '8'],
    '6': ['3', '5', '6', '9'],
    '7': ['4', '7', '8'],
    '8': ['5', '7', '8', '9', '0'],
    '9': ['6', '8', '9']
}

def get_pins(observed):
    result = ['']
    for i in range(len(observed)):
        result = process(observed[i], result)
    return result

def process(num, result):
    y = pin.get(num)
    x = result
    temp2 = []
    temp3 = ''
    temp = list(itertools.product(x, y))
    for i in temp:
        for o in i:
            temp3 += o
        temp2.append(temp3)
        temp3 = ''
    return temp2

if __name__ == '__main__':
    print(get_pins('11'))
