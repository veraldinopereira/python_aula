"""
This module is responsible for processing the data.  It will largely contain functions that will recieve the overall dataset and 
perfrom necessary processes in order to provide the desired result in the desired format.
It is likely that most sections will require functions to be placed in this module.
"""

import csv
import json
from collections import defaultdict


def read_csv():
    # Função para ler o arquivo CSV e retornar os dados como uma lista de dicionários
    dir = "./disneyland_reviews.csv"
    dir = "./disneyland_reviews.csv"
    data = []
    with open(dir, "r", newline="", encoding="utf-8") as file:
        file_csv = csv.DictReader(file)
        for row in file_csv:
            data.append(row)
    return data


# Função para salvar os dados de um parque como CSV, TXT e JSON
def save_reviews_park(data, file_name):
    # Save as csv
    with open(file_name, "w", newline="", encoding="utf-8") as file:
        columns = data[0].keys() if data else []
        writer_csv = csv.DictWriter(file, fieldnames=columns)
        writer_csv.writeheader()
        writer_csv.writerows(data)

    # Save as txt
    txt_file_name = file_name.replace(".csv", ".txt")
    with open(txt_file_name, "w", encoding="utf-8") as file:
        for row in data:
            file.write(
                ", ".join(f"{key}: {value}" for key, value in row.items()) + "\n"
            )

    # Save as json
    json_file_name = file_name.replace(".csv", ".json")
    with open(json_file_name, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


# Função para contar o número de avaliações para um determinado local e parque
def count_reviews(data, location, park):
    count = 0
    for row in data:
        if row["Branch"] == park and row["Reviewer_Location"] == location:
            count += 1
    print(f"The park {park} received {count} reviews from {location}.")
    return count


# Função para salvar o número de avaliações para um determinado local e parque como CSV, TXT e JSON
def save_reviews(count, location, park, name_file):
    # Save as csv
    with open(name_file, "w", newline="", encoding="utf-8") as file:
        writer_csv = csv.writer(file)
        writer_csv.writerow(["Branch", "Reviewer_Location", "Review_Count"])
        writer_csv.writerow([park, location, count])

    # Save as txt
    txt_file_name = name_file.replace(".csv", ".txt")
    with open(txt_file_name, "w", encoding="utf-8") as file:
        file.write(
            f"Branch: {park}, Reviewer_Location: {location}, Review_Count: {count}\n"
        )

    # Save as json
    json_file_name = name_file.replace(".csv", ".json")
    with open(json_file_name, "w", encoding="utf-8") as file:
        json.dump(
            {"Branch": park, "Reviewer_Location": location, "Review_Count": count},
            file,
            ensure_ascii=False,
            indent=4,
        )


# Função para calcular a avaliação média de um parque em um determinado ano
def average_rating_by_year(data, park, year):
    total_rating = 0
    count = 0
    for review in data:
        if review["Branch"] == park and review["Year_Month"].startswith(str(year)):
            total_rating += int(review["Rating"])
            count += 1
    if count == 0:
        return None
    return total_rating / count


# Função para salvar a avaliação média de um parque em um determinado ano como CSV, TXT e JSON
def save_average_rating_by_year(park, year, average_rating, filename):
    # Save as csv
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Branch", "Year", "Average Rating"])
        writer.writerow([park, year, average_rating])

    # Save as txt
    txt_file_name = filename.replace(".csv", ".txt")
    with open(txt_file_name, "w", encoding="utf-8") as file:
        file.write(f"Branch: {park}, Year: {year}, Average Rating: {average_rating}\n")

    # Save as json
    json_file_name = filename.replace(".csv", ".json")
    with open(json_file_name, "w", encoding="utf-8") as file:
        json.dump(
            {"Branch": park, "Year": year, "Average Rating": average_rating},
            file,
            ensure_ascii=False,
            indent=4,
        )


# Função para calcular a avaliação média de todos os locais para cada parque
def average_rating_by_all_location(data):
    park_location_ratings = defaultdict(lambda: defaultdict(list))

    for row in data:
        park = row["Branch"]
        location = row["Reviewer_Location"]
        rating = int(row["Rating"])
        park_location_ratings[park][location].append(rating)

    overall_location_averages = {}
    for park, location_ratings in park_location_ratings.items():
        park_location_averages = {}
        for location, ratings in location_ratings.items():
            average_rating = sum(ratings) / len(ratings)
            park_location_averages[location] = average_rating
        overall_location_averages[park] = park_location_averages

    return overall_location_averages


# Função para salvar as avaliações médias de todos os locais para cada parque como CSV, TXT e JSON
def save_location_ratings_to_csv(location_ratings, file_name):
    # Save as csv
    with open(file_name, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Branch", "Reviewer_Location", "Average_Rating"])
        for park, location_averages in location_ratings.items():
            for location, average_rating in location_averages.items():
                writer.writerow([park, location, average_rating])

    # Save as txt
    txt_file_name = file_name.replace(".csv", ".txt")
    with open(txt_file_name, "w", encoding="utf-8") as file:
        for park, location_averages in location_ratings.items():
            for location, average_rating in location_averages.items():
                file.write(
                    f"Branch: {park}, Reviewer_Location: {location}, Average_Rating: {average_rating}\n"
                )

    # Save as json
    json_file_name = file_name.replace(".csv", ".json")
    with open(json_file_name, "w", encoding="utf-8") as file:
        json.dump(location_ratings, file, ensure_ascii=False, indent=4)
        