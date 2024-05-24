import csv
import matplotlib.pyplot as plt
from collections import defaultdict
import calendar


def read_csv():
    dir = "./disneyland_reviews.csv"
    data = []
    with open(dir, "r", newline="", encoding="utf-8") as file:
        file_csv = csv.DictReader(file)
        for row in file_csv:
            data.append(row)
    return data


def show_by_branch(data, branch):
    for row in data:
        if row["Branch"] == branch:
            print("Review_ID:", row["Review_ID"])
            print("Rating:", row["Rating"])
            print("Year_Month:", row["Year_Month"])
            print("Reviewer_Location:", row["Reviewer_Location"])
            print("Branch:", row["Branch"])
            print()


def save_csv_branch(data, file_name):
    with open(file_name, "w", newline="", encoding="utf-8") as file:
        columns = data[0].keys() if data else []
        escritor_csv = csv.DictWriter(file, fieldnames=columns)
        escritor_csv.writeheader()
        escritor_csv.writerows(data)


def count_reviews(data, location, park):
    contador = 0
    for linha in data:
        if linha["Branch"] == park and linha["Reviewer_Location"] == location:
            contador += 1
    print(f"The park {park} received {contador} reviews from {location}.")
    return contador


def save_reviews(count, location, park, name_file):
    with open(name_file, "w", newline="", encoding="utf-8") as file:
        escritor_csv = csv.writer(file)
        escritor_csv.writerow(["Branch", "Reviewer_Location", "Review_Count"])
        escritor_csv.writerow([park, location, count])


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


def save_average_rating_by_year(park, year, average_rating, filename):
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Branch", "Year", "Average Rating"])
        writer.writerow([park, year, average_rating])


def count_reviews_by_branch(data):
    counts = {}
    for row in data:
        branch = row["Branch"]
        counts[branch] = counts.get(branch, 0) + 1
    return counts


def plot_pie_chart(counts):
    labels = counts.keys()
    values = counts.values()

    plt.figure(figsize=(8, 6))
    plt.pie(values, labels=labels, autopct="%1.1f%%", startangle=140)
    # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.axis("equal")
    plt.title("Number of Reviews per Park")
    plt.show()


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


def save_location_ratings_to_csv(location_ratings, file_name):
    with open(file_name, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Branch", "Reviewer_Location", "Average_Rating"])
        for park, location_averages in location_ratings.items():
            for location, average_rating in location_averages.items():
                writer.writerow([park, location, average_rating])


CSV = read_csv()

all = average_rating_by_all_location(CSV)
save_location_ratings_to_csv(all, 'all.csv')

# rating = average_rating_by_branch(CSV)
# plot_bar_chart(rating)
# print(rating)

# averages = average_rating_by_location(CSV, "Disneyland_HongKong")
# plot_top_locations(averages, "Disneyland_HongKong")


# cnt = count_reviews_by_branch(CSV)
# plot_pie_chart(cnt)

# # print(average_rating_by_year(CSV, "Disneyland_HongKong", 2019))
# # count_reviews(CSV, "Philippines", 'Disneyland_HongKong')
