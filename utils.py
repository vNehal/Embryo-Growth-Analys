
import re
from nltk.stem import SnowballStemmer
from nltk.corpus import stopwords
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer,TfidfTransformer,CountVectorizer
import pickle
import numpy as np
import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier


#évalue la phrase en recupèrant le modele grâce  au fichier feature.pkl
def predictSentiments(req_PDs,req_ASTV,req_POTWALTV):

    model=pickle.load(open("cls_fetal_health.pkl", "rb"))
    
    data = [[ req_PDs, req_ASTV, req_POTWALTV]]

    #indicateur de fiabilité
    x = model.predict(data)[0]

    return (x, round(model.predict_proba(data).max(),3))

     
