import os
import pickle
from sklearn.naive_bayes import GaussianNB

# define the class encodings and reverse encodings
classes = {0: "Class_0", 1: "Class_1", 2: "Class_2"}
r_classes = {y: x for x, y in classes.items()}

# function to process data and return it in correct format
def process_data(data):
    processed = [
        {
             "alchohol": d.alchohol,
             "malic_acid":d.malic_acid,
             "ash": d.ash,
             "alcalinity": d.alcalinity,
             "magnesium": d.magnesium,
             "total_phenols": d.total_phenols,
             "flavanoids": d.flavanoids,
             "nonflav_phenols": d.nonflav_phenols,
             "proanthocyanins": d.proanthocyanins,
             "color": d.color,
             "hue": d.hue,
             "od280": d.od280,
             "proline": d.proline,
        }
        for d in data
    ]

    return processed
