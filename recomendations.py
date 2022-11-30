import math
import matplotlib.pyplot as plt
from data import critics

def sim_pearson(critics, first_critic_name, second_critic_name):
    first_crit_dict = critics[first_critic_name]
    second_crit_dict = critics[second_critic_name]

    X = []
    Y = []

    for key, value in first_crit_dict.items():
        for key1, value1 in second_crit_dict.items():
            if key == key1:
                X.append(value)
                Y.append(value1)
            else:
                pass

    sumXY = 0
    sumX = 0
    sumY = 0
    quadratic_sumX = 0
    quadratic_sumY = 0

    for i in range(len(X)):
        sumXY += X[i] * Y[i]
        sumX += X[i]
        sumY += Y[i]
        quadratic_sumX += X[i] ** 2
        quadratic_sumY += Y[i] ** 2

    # If division by zero else return 0
    if len(X) != 0:
        P = (sumXY - (sumX * sumY / len(X))) / math.sqrt(
            (quadratic_sumX - (sumX ** 2) / len(X)) * (quadratic_sumY - (sumY ** 2) / len(X)))
        return P
    else:
        return 0

def sim_distance(critics, first_critic_name, second_critic_name):
    first_crit_dict = critics[first_critic_name]
    second_crit_dict = critics[second_critic_name]
    c_1_i = []
    c_2_i = []
    for key, value in first_crit_dict.items():
        for key1, value1 in second_crit_dict.items():
            if key == key1:
                c_1_i.append(value)
                c_2_i.append(value1)
            else:
                pass

    quadratic_sum = 0
    for i in range(len(c_1_i)):
        quadratic_sum += (c_1_i[i] - c_2_i[i]) ** 2
    P = 1 / (1 + math.sqrt(quadratic_sum))
    # print(P)
    return P


def top_matches(critics, critic_name):
    critics_coefs = {}
    for key in critics.keys():
        if critic_name != key:
            critics_coefs[key] = sim_pearson(critics, critic_name, key)
    critics_coefs = dict(sorted(critics_coefs.items(), key=lambda item: item[1]))
    critics_coefs = dict(critics_coefs.items().__reversed__())
    print(critics_coefs)
