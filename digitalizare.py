import streamlit as st
import openai
import pandas as pd

def main():
    st.title("Asistenți pentru Redactarea Documentelor pentru Fonduri Europene")
    
    # Sidebar for API key input
    st.sidebar.title("Configurare API OpenAI")
    api_key = st.sidebar.text_input("Introdu cheia API OpenAI", type="password")
    
    if api_key:
        openai.api_key = api_key
        st.sidebar.success("Cheia API a fost configurată cu succes.")
    else:
        st.sidebar.warning("Introduceți cheia API OpenAI pentru a continua.")

    st.sidebar.title("Navigare")
    option = st.sidebar.selectbox("Selectează Asistentul", ("Pagina Principală", "Planul de Afaceri", "Proiect Tehnic", "Anexe și Declarații", "Chat GPT-4"))

    if option == "Pagina Principală":
        show_home_page()
    elif option == "Planul de Afaceri":
        if api_key:
            show_business_plan_assistant()
        else:
            st.warning("Vă rugăm să introduceți cheia API OpenAI pentru a utiliza acest asistent.")
    elif option == "Proiect Tehnic":
        if api_key:
            show_technical_project_assistant()
        else:
            st.warning("Vă rugăm să introduceți cheia API OpenAI pentru a utiliza acest asistent.")
    elif option == "Anexe și Declarații":
        if api_key:
            show_annexes_assistant()
        else:
            st.warning("Vă rugăm să introduceți cheia API OpenAI pentru a utiliza acest asistent.")
    elif option == "Chat GPT-4":
        if api_key:
            show_chat_gpt4()
        else:
            st.warning("Vă rugăm să introduceți cheia API OpenAI pentru a utiliza acest asistent.")

def show_home_page():
    st.header("Bine ați venit la Asistenții pentru Redactarea Documentelor pentru Fonduri Europene")
    st.write("""
        Această aplicație vă ajută să redactați documentele necesare pentru accesarea fondurilor europene.
        Alegeți unul dintre asistenții din bara laterală pentru a începe:
        - **Planul de Afaceri:** Ghid complet pentru redactarea unui plan de afaceri.
        - **Proiect Tehnic:** Asistență pentru redactarea specificațiilor tehnice ale proiectului.
        - **Anexe și Declarații:** Ghid pentru completarea anexelor și declarațiilor necesare.
        - **Chat GPT-4:** Interacțiune directă cu modelul GPT-4 pentru asistență personalizată.
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

def show_chat_gpt4():
    st.header("Chat cu GPT-4")

    with st.expander(" ℹ️ Mesaj Informativ ℹ️  "):
        st.write("""
            Vă informăm că acest bot se află într-o fază incipientă de dezvoltare. 
            În acest moment, funcționalitatea este limitată la furnizarea de răspunsuri generale.
        """)

    if "openai_model" not in st.session_state:
        st.session_state["openai_model"] = "gpt-4-1106-preview"

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Afișarea mesajelor anterioare
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Input pentru mesaj nou de la utilizator
    if prompt := st.chat_input("Adăugați mesajul aici."):
        st.session_state.messages.append({"role": "user", "content": f"{prompt}" })
        with st.chat_message("user"):
            st.markdown(prompt)

        # Generarea răspunsului asistentului și afișarea acestuia
        with st.chat_message("assistant"):
            response = generate_response(prompt)
            st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})

def generate_response(prompt):
    response = openai.Completion.create(
        model=st.session_state["openai_model"],
        messages=[
            {"role": "system", "content": "Ești un asistent care ajută la redactarea documentelor pentru fonduri europene."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message["content"]

if __name__ == "__main__":
    main()

