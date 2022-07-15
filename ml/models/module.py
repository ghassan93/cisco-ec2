import pickle
import re
import pandas as pd
import requests
from urllib.parse import urlencode
api_key = "AIzaSyAwgy1LdO_Xl_fM_ED-ETL9IQyUNzEZqnM"



# loadig the model:
dictionary = pickle.load((open('ml/models/dictionary.sav', 'rb')))
tf_idf_1 = pickle.load(open('ml/models/tfidf.sav', 'rb'))
similarity_object = pickle.load(open('ml/models/similarity_object.sav', 'rb'))


def tokenize(txt):
    tokens = re.split('\W', txt)
    return tokens


def System_one(i):
    query_text_u = [i]
    df2 = pd.DataFrame({'Customers': query_text_u})
    df2['customer_tokenized'] = df2['Customers'].apply(
        lambda x: tokenize(str(x).lower()))
    query_doc_bow_u = dictionary.doc2bow(df2['customer_tokenized'][0])
    query_doc_tf_idf_u = tf_idf_1[query_doc_bow_u]
    similarity_scores_u = similarity_object[query_doc_tf_idf_u]
    list_similarity_u = similarity_scores_u.tolist()
    list_similarity_u.sort(reverse=True)
    short_list_sorted = list_similarity_u[:3]
    return short_list_sorted, similarity_scores_u


def Google_Names(i):
    Cname = i
    base_endpoint_places = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json"
    params = {
        "key": api_key,
        "input": Cname,
        "inputtype": "textquery",
        "fields": "name",
        "locationbias": "point:45.1,-95.05",

    }
    params_encoded = urlencode(params)
    places_endpoint = f"{base_endpoint_places}?{params_encoded}"
    r = requests.get(places_endpoint)
    jason_dic = r.json()
    query_text_api = jason_dic['candidates'][0]['name']
    return query_text_api

def System_two(z):
    query_text_u = [z]
    df2 = pd.DataFrame({'Customers': query_text_u})
    df2['customer_tokenized'] = df2['Customers'].apply(
        lambda x: tokenize(str(x).lower()))
    query_doc_bow_u = dictionary.doc2bow(df2['customer_tokenized'][0])
    query_doc_tf_idf_u = tf_idf_1[query_doc_bow_u]
    similarity_scores_u = similarity_object[query_doc_tf_idf_u]
    list_similarity_u = similarity_scores_u.tolist()
    list_similarity_u.sort(reverse=True)
    short_list_sorted = list_similarity_u[:3]
    return short_list_sorted, similarity_scores_u


def System_three(tokens):
    query_text_u = [tokens]
    df2 = pd.DataFrame({'Customers': query_text_u})
    df2['customer_tokenized'] = df2['Customers'].apply(
        lambda x: tokenize(str(x).lower()))
    query_doc_bow_u = dictionary.doc2bow(df2['customer_tokenized'][0])
    query_doc_tf_idf_u = tf_idf_1[query_doc_bow_u]
    similarity_scores_u = similarity_object[query_doc_tf_idf_u]
    list_similarity_u = similarity_scores_u.tolist()
    list_similarity_u.sort(reverse=True)
    short_list_sorted = list_similarity_u[:4]
    return short_list_sorted, similarity_scores_u
