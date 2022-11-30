from matplotlib import pyplot as plt
import numpy as np
from data import critics
from helpers import critic_polyfeet


def print_plots(film1, film2):
    x = []
    y = []
    for key, value in critics.items():
        for key1, value1 in value.items():
            if key1 in film1:
                x.append(value1)
            elif key1 in film2:
                y.append(value1)

    if len(x) > len(y):
        x = x[:len(y)]
    else:
        y = y[:len(x)]

    fig, ax = plt.subplots(figsize=(15, 5))
    ax.scatter(x, y)
    ax.set_xlabel(f'оценки за {film1}')
    ax.set_ylabel(f'оценки за {film2}')
    plt.show()


def plot_CriticFilmsRatingList(critics, critic_name):
    x = []
    y = []

    for key1, value1 in critics[critic_name].items():
        x.append(key1)
        y.append(value1)

    fig, ax = plt.subplots(figsize=(15, 5))

    ax.scatter(x, y)
    ax.set_xlabel('Фильмы')
    ax.set_ylabel('Рейтинги')
    ax.set_title(critic_name)
    plt.show()


def plot_CriticsCorrelation(critics, critic_name, second_critic_name, title):
    x = []
    y = []

    for key1, value1 in critics[critic_name].items():
        for key2, value2 in critics[second_critic_name].items():
            if key1 == key2:
                x.append(value1)
                y.append(value2)

    fig, ax = plt.subplots(figsize=(15, 5))

    for key1, value1 in critics[critic_name].items():
        for key2, value2 in critics[second_critic_name].items():
            if key1 == key2:
                plt.annotate(key1, (value1, value2))

    ax.scatter(x, y)
    ax.set_xlabel(critic_name)
    ax.set_ylabel(second_critic_name)
    ax.set_title(title)
    critic_polyfeet(x, y)
    plt.show()

