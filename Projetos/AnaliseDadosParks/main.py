"""
This module is responsible for the overall program flow. It controls how the user interacts with the
program and how the program behaves. It uses the other modules to interact with the user, carry out
processing, and for visualising information.

Note:   any user input/output should be done in the module 'tui'
        any processing should be done in the module 'process'
        any visualisation should be done in the module 'visual'
"""
from process import (
    read_csv,
    save_reviews_park,
    count_reviews,
    save_reviews,
    average_rating_by_year,
    save_average_rating_by_year,
    average_rating_by_all_location,
    save_location_ratings_to_csv,
)
from visual import (
    count_reviews_by_branch,
    plot_pie_chart,
    average_rating_by_branch,
    plot_bar_chart,
    average_rating_by_location,
    plot_top_locations,
    average_rating_by_month,
    plot_monthly_ratings,
)


class DisneyReviewAnalyser:
    def __init__(self):
        # Inicializa a classe e carrega os dados do CSV
        self.data_csv = read_csv()

    def init_msg(self):
        # Exibe a mensagem de inicialização do programa
        msg_init = "Disneyland Review Analyser"
        msg = "-" * len(msg_init)
        print(msg)
        print(msg_init)
        print(msg)

    def view_data(self):
        # Exibe opções para visualizar os dados e processa a escolha do usuário
        print("You have chosen option A - View Data")
        print("Please enter one of the following options:")
        choice_view = input(
            """        [A] View Reviews by Park
        [B] Number of Reviews By Park and Reviewer Location
        [C] Average Score per year by Park
        [D] Average Score per Park by Reviewer Location
        Choose: """
        )
        # Processa a escolha do usuário e executa a ação correspondente
        if choice_view == "A":
            branch = input("Choose a Park: ")
            data_branch = [
                linha for linha in self.data_csv if linha["Branch"] == branch
            ]
            save_reviews_park(data_branch, f"./data_{branch}.csv")

        elif choice_view == "B":
            park = input("Choose park: ")
            location = input("Choose location: ")
            count = count_reviews(self.data_csv, location, park)
            save_reviews(count, location, park, f"./data_{park}_{location}.csv")

        elif choice_view == "C":
            park = input("Choose park: ")
            year = input("Choose year: ")
            average = average_rating_by_year(self.data_csv, park, year)
            save_average_rating_by_year(
                park, year, average, f"./data_{park}_{year}.csv"
            )

        elif choice_view == "D":
            all_ratings = average_rating_by_all_location(self.data_csv)
            save_location_ratings_to_csv(all_ratings, "all_ratings.csv")

    def visualize_data(self):
        # Exibe opções para visualizar os dados e processa a escolha do usuário
        print("You have chosen option B - Visualise Data")
        print("Please enter one of the following options:")
        choice_view = input(
            """        [A] Most Reviewed Parks
        [B] Average Scores
        [C] Park Ranking by Nationality
        [D] Most Popular Month by Park
        Choose: """
        )
        # Processa a escolha do usuário e executa a ação correspondente
        if choice_view == "A":
            reviewed_parks = count_reviews_by_branch(self.data_csv)
            plot_pie_chart(reviewed_parks)

        elif choice_view == "B":
            average_scores = average_rating_by_branch(self.data_csv)
            plot_bar_chart(average_scores)

        elif choice_view == "C":
            park = input("Choose Park: ")
            averages = average_rating_by_location(self.data_csv, park)
            plot_top_locations(averages, park)

        elif choice_view == "D":
            park = input("Choose Park: ")
            average_month = average_rating_by_month(self.data_csv, park)
            plot_monthly_ratings(average_month, park)

    def run(self):
        # Inicia o loop principal do programa
        show_menu = True
        while True:
            if show_menu:
                self.init_msg()
            # Exibe o menu principal e processa a escolha do usuário
            choice = input("[A] View Data\n[B] Visualise Data\n[X] Exit\nChoose: ")

            if choice == "A":
                show_menu = False
                self.view_data()
                continue

            if choice == "B":
                show_menu = False
                self.visualize_data()
                continue

            if choice == "X":
                break


if __name__ == "__main__":
    # Cria uma instância do analisador e executa o programa
    analyser = DisneyReviewAnalyser()
    analyser.run()
