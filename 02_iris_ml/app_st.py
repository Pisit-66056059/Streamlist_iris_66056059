import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import pickle
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

st.title('Iris Species Classification')
st.write("The Iris dataset was used in R.A. Fisher's classic 1936 paper "
         "The Use of Multiple Measurements in Taxonomic Problems, "
         "and can also be found on the UCI Machine Learning Repository."
         "includes three iris species with 50 samples each as well as some properties about each flower."
         "One flower species is linearly separable from the other two, "
         "but the other two are not linearly separable from each other."
         "The columns in this dataset are: "
         "-Id , SepalLengthCm , SepalWidthCm, PetalLengthCm, PetalWidthCm and species")

iris_file = st.file_uploader('Upload your own iris.csv')

if iris_file is None:
    rf_pickle = open('random_forest_iris.pickle', 'rb')
    map_pickle = open('output_iris.pickle', 'rb')

    rfc = pickle.load(rf_pickle)
    unique_iris_mapping = pickle.load(map_pickle)

    rf_pickle.close()
else:
    iris_df = pd.read_csv(iris_file)
    iris_df = iris_df.dropna()

    output = iris_df['variety']
    features = iris_df[['sepal.length', 'sepal.width', 'petal.length', 'petal.width']]
    features = pd.get_dummies(features)
    output, unique_iris_mapping = pd.factorize(output)

    x_train, x_test, y_train, y_test = train_test_split(
        features, output, test_size=.8)

    rfc = RandomForestClassifier(random_state=15)
    rfc.fit(x_train, y_train)

    y_pred = rfc.predict(x_test)

    score = round(accuracy_score(y_pred, y_test), 2)

    st.write('We trained a Random Forest model on these data,'
             ' it has a score of {}! Use the '
             'inputs below to try out the model.'.format(score))

with st.form('user_inputs'):
    sepal_length = st.number_input(
        'Sepal Length (cm)', min_value=0, value=10)
    sepal_width = st.number_input(
        'Sepal Width (cm)', min_value=0, value=10)
    petal_length = st.number_input(
        'Petal Length (cm)', min_value=0, value=10)
    petal_width = st.number_input(
        'Petal Width (cm)', min_value=0, value=3)
    st.form_submit_button()

new_prediction = rfc.predict([[sepal_length,
                               sepal_width,
                               petal_length,
                               petal_width]])
prediction_species = unique_iris_mapping[new_prediction][0]
st.write('We predict your IRIS is of the {} species'.format(prediction_species))
