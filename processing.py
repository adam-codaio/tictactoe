import numpy
import json


def identifyMove(prev_state, state):
    for i in xrange(len(prev_state)):
        if prev_state[i] != state[i]:
            return i


def main():
    with open('state-action.txt', 'w') as outfile:
        with open('seed_data.txt', 'r') as infile:
            prev_state = []
            counter = 0
            for line in infile:
                counter += 1
                data_point = line.rstrip('\n').split('#')
                state = json.loads(data_point[0])
                result = float(data_point[1])
                if len(prev_state) and state != [0.0] * 9:
                    action = identifyMove(prev_state, state)
                    outfile.write(json.dumps(prev_state))
                    outfile.write('#')
                    outfile.write(json.dumps(action))
                    outfile.write('\n')
                prev_state = state
                if not counter % 1000:
                    print "Process %d lines so far." % counter


if __name__ == '__main__':
    main()
