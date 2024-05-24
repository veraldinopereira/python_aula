"""
This module is responsible for visualising the data using Matplotlib.
Any visualisations should be generated via functions in this module.
"""

import calendar
import matplotlib.pyplot as plt
from collections import defaultdict


# Função para contar o número de avaliações por parque
def count_reviews_by_branch(data):
    counts = {}
    for row in data:
        branch = row["Branch"]
        counts[branch] = counts.get(branch, 0) + 1
    return counts


# Função para traçar um gráfico de pizza mostrando o número de avaliações por parque
def plot_pie_chart(counts):
    labels = counts.keys()
    values = counts.values()

    plt.figure(figsize=(8, 6))
    plt.pie(values, labels=labels, autopct="%1.1f%%", startangle=140)
    # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.axis("equal")
    plt.title("Number of Reviews per Park")
    plt.show()


# Função para calcular a média das avaliações por parque
def average_rating_by_branch(data):
    averages = {}
    counts = {}

    for row in data:
        branch = row["Branch"]
        rating = int(row["Rating"])

        if branch in averages:
            averages[branch] += rating
            counts[branch] += 1
        else:
            averages[branch] = rating
            counts[branch] = 1

    for branch in averages:
        averages[branch] /= counts[branch]

    return averages


# Função para traçar um gráfico de barras mostrando a média das avaliações por parque
def plot_bar_chart(averages):
    branches = list(averages.keys())
    ratings = list(averages.values())

    plt.figure(figsize=(10, 6))
    plt.bar(range(len(branches)), ratings, align="center", alpha=0.8)
    plt.xticks(range(len(branches)), branches, rotation=45, ha="right")
    plt.ylabel("Average Score")
    plt.title("Average Review Score by Park")
    plt.tight_layout()
    plt.show()


# Função para calcular a média das avaliações por localização para um determinado parque
def average_rating_by_location(data, park):
    location_ratings = defaultdict(list)

    for row in data:
        if row["Branch"] == park:
            location = row["Reviewer_Location"]
            rating = int(row["Rating"])
            location_ratings[location].append(rating)

    location_averages = {
        loc: sum(ratings) / len(ratings) for loc, ratings in location_ratings.items()
    }
    return location_averages


# Função para traçar um gráfico de barras mostrando as principais localizações por média de avaliação para um parque específico
def plot_top_locations(averages, park):
    # Ordenar as localizações pela média das avaliações
    sorted_averages = sorted(averages.items(), key=lambda x: x[1], reverse=True)[:10]
    locations = [loc for loc, _ in sorted_averages]
    ratings = [avg for _, avg in sorted_averages]

    # Criar o gráfico de barras
    plt.figure(figsize=(12, 8))
    plt.bar(locations, ratings, alpha=0.8)
    plt.xticks(rotation=45, ha="right")
    plt.ylabel("Average Score")
    plt.xlabel("Location")
    plt.title(f"Top 10 Places by Average Score for {park}")
    plt.tight_layout()
    plt.show()


# Função para calcular a média das avaliações por mês para um parque específico
def average_rating_by_month(data, park):
    month_ratings = defaultdict(list)

    for row in data:
        if row["Branch"] == park:
            year_month = row["Year_Month"]
            # Verificar se a string está no formato esperado
            if "-" in year_month:
                year, month_number = map(int, year_month.split("-"))
                # Obter o nome do mês
                month_name = calendar.month_name[month_number]
                rating = int(row["Rating"])
                month_ratings[month_name].append(rating)

    # Calcular a média das avaliações para cada mês
    month_averages = {}
    for month_name, ratings in month_ratings.items():
        average_rating = sum(ratings) / len(ratings)
        month_averages[month_name] = average_rating

    # Ordenar os meses em ordem cronológica
    sorted_months = sorted(
        month_averages.items(), key=lambda x: list(calendar.month_name).index(x[0])
    )
    sorted_month_averages = {month: rating for month, rating in sorted_months}

    return sorted_month_averages


# Função para traçar um gráfico de barras mostrando a média das avaliações por mês para um parque específico
def plot_monthly_ratings(averages, park):
    months = sorted(
        averages.keys(), key=lambda x: list(calendar.month_name).index(x)
    )  # Ordenar os meses
    ratings = [averages[month] for month in months]

    # Criar o gráfico de barras
    plt.figure(figsize=(10, 6))
    plt.bar(months, ratings, alpha=0.8)
    plt.xlabel("Month")
    plt.ylabel("Average Rating")
    plt.title(f"Average Rating per Month for the Park {park}")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()
