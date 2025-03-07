# -*- coding: utf-8 -*-
"""
Created on Fri Mar  7 12:12:00 2025

@author: Miguel Rico
"""

import streamlit as st

def calcular_balance(pulpa_kg, brix_pulpa, nectar_kg, brix_nectar):
    solidos_pulpa = pulpa_kg * (brix_pulpa / 100)
    solidos_nectar = nectar_kg * (brix_nectar / 100)
    azucar_agregar = solidos_nectar - solidos_pulpa
    agua_agregar = nectar_kg - pulpa_kg - azucar_agregar
    return azucar_agregar, agua_agregar

st.title("Cálculo de Balance de Masa para Néctar")

pulpa_kg = st.number_input("Ingrese la cantidad de pulpa en kg:", min_value=0.0, format="%.2f")
brix_pulpa = st.number_input("Ingrese los grados Brix de la pulpa:", min_value=0.0, format="%.2f")
nectar_kg = st.number_input("Ingrese la cantidad de néctar deseada en kg:", min_value=0.0, format="%.2f")
brix_nectar = st.number_input("Ingrese los grados Brix deseados del néctar:", min_value=0.0, format="%.2f")

if st.button("Calcular"):
    if pulpa_kg > 0 and brix_pulpa > 0 and nectar_kg > 0 and brix_nectar > 0:
        azucar_agregar, agua_agregar = calcular_balance(pulpa_kg, brix_pulpa, nectar_kg, brix_nectar)
        st.success(f"Cantidad de azúcar a agregar: {azucar_agregar:.2f} kg")
        st.success(f"Cantidad de agua a agregar: {agua_agregar:.2f} kg")
    else:
        st.error("Por favor, ingrese valores mayores a 0 para todos los campos.")
