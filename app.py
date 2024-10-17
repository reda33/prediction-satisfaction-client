import streamlit as st
import numpy as np
import pickle

# Charger le modèle entraîné (assurez-vous d'enregistrer le modèle après l'entraînement)
model = pickle.load(open('model.pkl', 'rb'))

# Définir la fonction pour obtenir une prédiction
def predict_satisfaction(var3, var15, var36, imp_op_var39_efect_ult1):
    input_features = np.array([[var3, var15, var36, imp_op_var39_efect_ult1]])
    prediction = model.predict(input_features)
    return prediction[0]

# Interface utilisateur
st.title("Prédiction de la Satisfaction Client")

var3 = st.number_input("Entrez la valeur de var3")
var15 = st.number_input("Entrez la valeur de var15")
var36 = st.number_input("Entrez la valeur de var36")
imp_op_var39_efect_ult1 = st.number_input("Entrez la valeur de imp_op_var39_efect_ult1")

if st.button("Prédire"):
    result = predict_satisfaction(var3, var15, var36, imp_op_var39_efect_ult1)
    if result == 1:
        st.success("Le client est insatisfait.")
    else:
        st.success("Le client est satisfait.")

