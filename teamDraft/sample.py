#!/usr/bin/env python3

import sys
import os
import pickle

def read_data(matrix_filename):
    fin = open(matrix_filename, "rb")
    data = pickle.load(fin)
    fin.close()
    return data

def main(argv):
    if len(argv) > 1:
        data_file = argv[1]
    else:
        data_file = "data/h.matrix.p"
    
    if not os.path.exists(data_file):
        raise Exception("{} does not exist.".format(data_file))
    
    data = read_data(data_file)
    names, matrix = data
    for attacker in names:
        for defender in names:
            key = (attacker, defender)
            score = matrix[key]
            ### scores are in the range [0, 1000]
            ### 500 is a tie
            ### < 500 means attacker should lose
            ### > 500 means attacker should win
            print("{} vs {} = {}".format(attacker, defender, score))

    return

if __name__ == "__main__":
    main(sys.argv)
    
#
# e.g. ./sample.py data/l.matrix.p
#
