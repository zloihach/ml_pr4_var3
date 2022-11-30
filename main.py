from recomendations import critics, sim_distance, sim_pearson, top_matches
from graph import print_plots, plot_CriticFilmsRatingList, plot_CriticsCorrelation
from data import critics

#var 8

#task 4
# Изобразить на двух рисунках оценки фильмов
# заданного критика и наиболее похожего,
# заданного критика и наименее похожего.

if __name__ == '__main__':

    print("====================================")
    print("Евклидово")
    print(sim_distance(critics, 'Кот Матроскин', 'Пёс Шарик'))
    print("====================================")
    print("Пирсон")
    print(sim_pearson(critics, 'Кот Матроскин', 'Пёс Шарик'))
    print("====================================")
    print("Метрика схожести по Пирсону DESC")

    print_plots('Ну, погоди!', 'Зима в Простоквашино')
    top_matches(critics, 'Пёс Шарик')
    plot_CriticFilmsRatingList(critics, 'Пёс Шарик')
    plot_CriticsCorrelation(critics, 'Пёс Шарик', 'Галчонок', 'Наиболле похожий')
    plot_CriticsCorrelation(critics, 'Пёс Шарик', 'Тюша Евгеньевич', 'Наименее похожий')
