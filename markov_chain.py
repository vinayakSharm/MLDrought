import csv
import numpy as np

with open('train_timeseries/train_timeseries.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    last = 0
    A = np.zeros([6,6])
    transitions = 0
    for row in csv_reader:
        if line_count == 0:
            pass
            line_count += 1
        else:
            if(len(row[-1]) > 0):
                next_ = int(round(float(row[-1])))
                A[last][next_] += 1
                last = next_
                transitions += 1

            line_count += 1
    print(np.round(A/A.sum(axis=1,keepdims=True),2))