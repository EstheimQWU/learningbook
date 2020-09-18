# -*- coding: UTF-8 -*-
import random

if __name__ == "__main__":
    len = [1, 2, 3, 4, 5]
    len.append(6)
    print(random.choice(len))
    report = {"A1": 20, "A2": 50, "A3": 90}
    print(report["A2"])
    for i in report:
        if i == "A1":
            print(report[i])
        elif i == "A2":
            print(report[i])
        else:
            print(report[i])
    