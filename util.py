'''
make some utility functions to keep jupyter notebook clean and easy to  digest 
'''

import pandas as pd

# 01_Intro: to merge and clean the gdp and satisfaction dataset 
def prepare_country_stats(oecd_bli, gdp_per_capita):
    '''
    To clean and merge oecd(avg. satisfaction data with gdp per capital database)
    Input: 
        oecd_bil = pd dataframe downloaded from OECD website
        gdp_per_capita = pd dataframe downloaded from  world bank 
    Output:
        full_country_stats = pd dataframe with two variables GDP and life_satisfaction
    '''
    oecd_bli = oecd_bli[oecd_bli["INEQUALITY"]=="TOT"]
    oecd_bli = oecd_bli.pivot(index="Country", columns="Indicator", values="Value")
    gdp_per_capita.rename(columns={"2015": "GDP per capita"}, inplace=True)
    gdp_per_capita.set_index("Country", inplace=True)
    full_country_stats = pd.merge(left=oecd_bli, right=gdp_per_capita,
                                  left_index=True, right_index=True)
    full_country_stats.sort_values(by="GDP per capita", inplace=True)
    remove_indices = [0, 1, 6, 8, 33, 34, 35]
    keep_indices = list(set(range(36)) - set(remove_indices))
    return full_country_stats[["GDP per capita", 'Life satisfaction']].iloc[keep_indices]



# for 02_Linear_regression_housing_data, fetching data

def download_housing_data():

    import os
    import tarfile
    import urllib.request

    DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml2/master/"
    HOUSING_PATH = os.path.join("datasets", "housing")
    HOUSING_URL = DOWNLOAD_ROOT + "datasets/housing/housing.tgz"

    def fetch_housing_data(housing_url=HOUSING_URL, housing_path=HOUSING_PATH):
        if not os.path.isdir(housing_path):
            os.makedirs(housing_path)
        tgz_path = os.path.join(housing_path, "housing.tgz")
        urllib.request.urlretrieve(housing_url, tgz_path)
        housing_tgz = tarfile.open(tgz_path)
        housing_tgz.extractall(path=housing_path)
        housing_tgz.close()
        print("California Housing data downloaded")

    return fetch_housing_data()

# for 02, loading the housing data

def get_housing_data():
    import os
    import tarfile
    import urllib.request

    DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml2/master/"
    HOUSING_PATH = os.path.join("datasets", "housing")
    HOUSING_URL = DOWNLOAD_ROOT + "datasets/housing/housing.tgz"

    def load_housing_data(housing_path=HOUSING_PATH):
        csv_path = os.path.join(housing_path, "housing.csv")
        return pd.read_csv(csv_path)

    return load_housing_data()