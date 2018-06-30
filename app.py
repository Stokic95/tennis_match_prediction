import pandas as pd


def load_data(_paths):

    print("Loading data..")

    _data = []

    for _path in _paths:
        print("Loading \"" + str(_path) + "\"")
        _data.append(pd.read_csv(_path))

    print("Data loaded.")

    return _data

if __name__ == '__main__':
    paths = [
        "data/atp_matches_2000.csv",
        "data/atp_matches_2001.csv",
        "data/atp_matches_2002.csv",
        "data/atp_matches_2003.csv",
        "data/atp_matches_2004.csv",
        "data/atp_matches_2005.csv",
        "data/atp_matches_2006.csv",
        "data/atp_matches_2007.csv",
        "data/atp_matches_2008.csv",
        "data/atp_matches_2009.csv",
        "data/atp_matches_2010.csv",
        "data/atp_matches_2011.csv",
        "data/atp_matches_2012.csv",
        "data/atp_matches_2013.csv",
        "data/atp_matches_2014.csv",
        "data/atp_matches_2015.csv",
        "data/atp_matches_2016.csv",
        "data/atp_matches_2017.csv",
        "data/atp_matches_2018.csv"
    ]

    data = load_data(paths)

    print(len(data))
