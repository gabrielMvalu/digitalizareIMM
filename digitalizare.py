from openai import OpenAI
import streamlit as st

with st.expander(" ℹ️ Mesaj Informativ ℹ️  "):
    st.write("""
        Vă informăm că aceast bot se află într-o fază incipientă de dezvoltare. 
        În acest moment, funcționalitatea este limitată la furnizarea de răspunsuri generale.
    """)

with st.sidebar:
    openai_api_key = st.text_input("Acces Key", key="chatbot_api_key", type="password")
    
if not openai_api_key:
    st.info("Vă rugăm să introduceți cheia de acces în bara laterală.")
else:
    # Inițializarea clientului OpenAI cu cheia API introdusă
    client = OpenAI(api_key=openai_api_key)

    # Inițializarea stării sesiunii pentru model și mesaje
    if "openai_model" not in st.session_state:
        st.session_state["openai_model"] = "gpt-4o"

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Afișarea mesajelor anterioare
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Input pentru mesaj nou de la utilizator
    if prompt := st.chat_input("Adaugati mesajul aici."):
        st.session_state.messages.append({"role": "user", "content": f"{prompt}" })
        with st.chat_message("user"):
            st.markdown(prompt)

        # Generarea răspunsului asistentului și afișarea acestuia
        with st.chat_message("assistant"):
            stream = client.chat.completions.create(
                model=st.session_state["openai_model"],
                messages=[
                    {"role": m["role"], "content": m["content"]}
                    for m in st.session_state.messages
                ],
                stream=True,
            )
            response = st.write_stream(stream)
        st.session_state.messages.append({"role": "assistant", "content": response})
