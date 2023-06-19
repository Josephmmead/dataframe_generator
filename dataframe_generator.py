from pyspark.sql import SparkSession
import pandas as pd
import numpy as np


file_path = '.\\test_file.csv'


def get_dataset(size):
    df = pd.DataFrame()
    dates = pd.date_range('2020-01-01', '2022-12-31')

    df['size'] = np.random.choice(['big', 'medium', 'small'], size)
    df['age'] = np.random.randint(1, 50, size)
    df['team'] = np.random.choice(['red', 'blue', 'yellow', 'green'], size)
    df['win'] = np.random.choice(['yes', 'no'], size)
    df['date'] = np.random.choice(dates, size)
    df['prob'] = np.random.uniform(0, 1, size)
    df['size1'] = np.random.choice(['big', 'medium', 'small'], size)
    df['age1'] = np.random.randint(1, 50, size)
    df['team1'] = np.random.choice(['red', 'blue', 'yellow', 'green'], size)
    df['win1'] = np.random.choice(['yes', 'no'], size)
    df['date1'] = np.random.choice(dates, size)
    df['prob1'] = np.random.uniform(0, 1, size)
    df['size2'] = np.random.choice(['big', 'medium', 'small'], size)
    df['age2'] = np.random.randint(1, 50, size)
    df['team2'] = np.random.choice(['red', 'blue', 'yellow', 'green'], size)
    df['win2'] = np.random.choice(['yes', 'no'], size)
    df['date2'] = np.random.choice(dates, size)
    df['prob2'] = np.random.uniform(0, 1, size)
    df['size3'] = np.random.choice(['big', 'medium', 'small'], size)
    df['age3'] = np.random.randint(1, 50, size)
    df['team3'] = np.random.choice(['red', 'blue', 'yellow', 'green'], size)
    df['win3'] = np.random.choice(['yes', 'no'], size)
    df['date3'] = np.random.choice(dates, size)
    df['prob3'] = np.random.uniform(0, 1, size)
    df['size4'] = np.random.choice(['big', 'medium', 'small'], size)
    df['age4'] = np.random.randint(1, 50, size)
    df['team4'] = np.random.choice(['red', 'blue', 'yellow', 'green'], size)
    df['win4'] = np.random.choice(['yes', 'no'], size)
    df['date4'] = np.random.choice(dates, size)
    df['prob4'] = np.random.uniform(0, 1, size)
    df['size5'] = np.random.choice(['big', 'medium', 'small'], size)
    df['age5'] = np.random.randint(1, 50, size)
    df['team5'] = np.random.choice(['red', 'blue', 'yellow', 'green'], size)
    df['win5'] = np.random.choice(['yes', 'no'], size)
    df['date5'] = np.random.choice(dates, size)
    df['prob5'] = np.random.uniform(0, 1, size)
    return df


if __name__ == "__main__":
    spark = SparkSession.builder.getOrCreate()

    amount_of_columns = 1000

    for i in range(1):
        df = get_dataset(amount_of_columns)
        print('finished')
        print(df)

    spark_df = spark.createDataFrame(df)
    spark_df.show()


