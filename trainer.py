import numpy
import json


def constructData():
    X = []
    y = []
    with open('state-action.txt', 'r') as f:
        for line in f:
            data_point = line.rstrip('\n').split('#')
            state = json.loads(data_point[0])
            action = int(data_point[1])
            X.append(state)
            y.append(action)
    return X, y

def main():
    X, y = constructData()
    print y



if __name__ == '__main__':
    main()
