import pickle
import pandas as pd


def load_data():
    X_train = pd.read_pickle("../data/processed/X_train.pkl")
    X_test = pd.read_pickle("../data/processed/X_test.pkl")
    y_train = pd.read_pickle("../data/processed/y_train.pkl")
    y_test = pd.read_pickle("../data/processed/y_test.pkl")
    return X_train, X_test, y_train, y_test

def load_scaler():
    with open("../models/scaler.pkl", "rb") as f:
        scaler = pickle.load(f)
    return scaler
