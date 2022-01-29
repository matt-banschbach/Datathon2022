import pandas as pd
from matplotlib import pyplot as plt


def initial():
    """
    Complete the setup necessary for analysis
    """
    my_data = pd.read_csv("cleaned_data.csv")
    return my_data


def debt_to_income_acceptance(in_data):
    my_categories = {}
    for cat in in_data["debt_to_income_ratio"]:
        if cat in my_categories:
            my_categories[cat] += 1
        else:
            my_categories[cat] = 1


    dual = pd.DataFrame(in_data, columns=['debt_to_income_ratio', 'accepted'])

    dual_dict = {}

    for row in range(len(dual["debt_to_income_ratio"])):
        cat = dual["debt_to_income_ratio"][row]
        if cat in dual_dict:
            dual_dict[cat] += dual["accepted"][row]
        else:
            dual_dict[cat] = 1

    for key in dual_dict:
        dual_dict[key] /= my_categories[key]

    plt.bar(dual_dict.keys(), dual_dict.values(), color='g')
    plt.title("Acceptance Ratio by Debt to Income Ratio")
    plt.show()


def race_acceptance(in_data):

    race_accept = pd.DataFrame(in_data, columns=['race', 'accepted'])
    rejections_proportion = {}
    race_totals = {}
    for race in race_accept["race"]:
        if race in rejections_proportion:
            race_totals[race] += 1
        else:
            rejections_proportion[race] = 0
            race_totals[race] = 1

    for row in range(len(race_accept)):
        race = race_accept['race'][row]
        rejections_proportion[race] += race_accept['accepted'][row]
    for race in rejections_proportion:
        rejections_proportion[race] /= race_totals[race]

    plt.bar(rejections_proportion.keys(), rejections_proportion.values())
    plt.title("Acceptance Proportion by Race")
    plt.show()


def hispanic_acceptance(in_data):

    eth_accept = pd.DataFrame(in_data, columns=['ethnicity', 'accepted'])
    acceptance_proportion = {}
    ethnic_totals = {}
    for eth in data["ethnicity"]:
        if eth in acceptance_proportion:
            ethnic_totals[eth] += 1
        else:
            acceptance_proportion[eth] = 0
            ethnic_totals[eth] = 1

    for row in range(len(eth_accept)):
        race = eth_accept['ethnicity'][row]
        acceptance_proportion[race] += eth_accept['accepted'][row]
    for race in acceptance_proportion:
        acceptance_proportion[race] /= ethnic_totals[race]

    plt.bar(acceptance_proportion.keys(), acceptance_proportion.values())
    plt.title("Acceptance Proportion by Ethnicity")
    plt.show()



data = initial()
#debt_to_income_acceptance(data)
#race_acceptance(data)
#hispanic_acceptance(data)
