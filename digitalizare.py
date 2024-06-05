import streamlit as st
import openai
import pandas as pd

# Set up the OpenAI API key
openai.api_key = st.secrets["openai_api_key"]

def main():
    st.title("Asistenți pentru Redactarea Documentelor pentru Fonduri Europene")
    
    # Sidebar for API key input
    with st.sidebar:
        st.header("Configurare API OpenAI")
        api_key = st.text_input("Introdu cheia API OpenAI", type="password")
        if api_key:
            st.write("Cheia API a fost configurată.")
            openai.api_key = api_key
            st.secrets["openai_api_key"] = api_key

    st.sidebar.title("Navigare")
    option = st.sidebar.selectbox("Selectează Asistentul", ("Pagina Principală", "Planul de Afaceri", "Proiect Tehnic", "Anexe și Declarații"))

    if option == "Pagina Principală":
        show_home_page()
    elif option == "Planul de Afaceri":
        show_business_plan_assistant()
    elif option == "Proiect Tehnic":
        show_technical_project_assistant()
    elif option == "Anexe și Declarații":
        show_annexes_assistant()

def show_home_page():
    st.header("Bine ați venit la Asistenții pentru Redactarea Documentelor pentru Fonduri Europene")
    st.write("""
        Această aplicație vă ajută să redactați documentele necesare pentru accesarea fondurilor europene.
        Alegeți unul dintre asistenții din bara laterală pentru a începe:
        - **Planul de Afaceri:** Ghid complet pentru redactarea unui plan de afaceri.
        - **Proiect Tehnic:** Asistență pentru redactarea specificațiilor tehnice ale proiectului.
        - **Anexe și Declarații:** Ghid pentru completarea anexelor și declarațiilor necesare.
    """)

def show_business_plan_assistant():
    st.header("Asistent pentru Planul de Afaceri")
    business_name = st.text_input("Numele Afacerii")
    business_description = st.text_area("Descrierea Afacerii")
    market_analysis = st.text_area("Analiza Pieței")
    marketing_strategy = st.text_area("Strategia de Marketing")
    financial_plan = st.text_area("Planul Financiar")
    if st.button("Generează Planul de Afaceri"):
        st.write("Planul de Afaceri pentru ", business_name)
        st.write("Descriere: ", business_description)
        st.write("Analiza Pieței: ", market_analysis)
        st.write("Strategia de Marketing: ", marketing_strategy)
        st.write("Planul Financiar: ", financial_plan)

def show_technical_project_assistant():
    st.header("Asistent pentru Proiectul Tehnic")
    # Adaugă funcționalitățile necesare pentru acest asistent

def show_annexes_assistant():
    st.header("Asistenți pentru Anexe și Declarații")
    # Adaugă funcționalitățile necesare pentru acest asistent

if __name__ == "__main__":
    main()
