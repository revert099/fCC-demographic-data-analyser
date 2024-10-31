import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult_data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df.iloc[:, 8].nunique()

    # What is the average age of men?
    men = df.iloc[:, 9] == 'Male'
    average_age_men = men.iloc[:, 0].mean()

    # What is the percentage of people who have a Bachelor's degree?
    bachelors = df.iloc[:, 3] == 'Bachelors'
    percentage_bachelors = bachelors.mean() * 100

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?
    advanced_education = df.iloc[:, 3].isin('Bachelors', 'Masters', 'Doctorate')

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    advanced_over_50k = df[advanced_education & df.iloc[:, 14] == '>50k']
    not_advanced_over_50k = df[~advanced_education & df.iloc[:, 14] == '>50k']

    # percentage with salary >50K
    higher_education_rich = (len(advanced_over_50k) / len(df[advanced_education])) * 100
    lower_education_rich = (len(not_advanced_over_50k) / len(df[~advanced_education])) * 100

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df.iloc[:, 12].min

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df.iloc[: 12].mean() * 100 == '>50k'

    rich_percentage = (len(num_min_workers) / len(min_work_hours)) * 100

    # What country has the highest percentage of people that earn >50K?
    country_stats = df[df.iloc[:, 14] == '>50k'].iloc[:, 13].value_counts() / df.iloc[:, 13].value_counts()
    highest_earning_country = country_stats.idxmax()
    highest_earning_country_percentage = country_stats.max() * 100

    # Identify the most popular occupation for those who earn >50K in India.
    india_high_income = df[(df.iloc[:, 13] == 'India') & (df.iloc[:, 14] == '>50k')]
    top_IN_occupation = india_high_income.iloc[:, 6].value_counts().idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
