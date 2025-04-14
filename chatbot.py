import streamlit as st
import google.generativeai as genai

st.title("Chatbot de consórcios")

genai.configure(api_key="AIzaSyDFQ6flc6igCzUQFz2AXjsQrlE4w1Q1yFY") # Essa chave é pessoal, teria que ser alterada
model = genai.GenerativeModel("gemini-2.0-flash")

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Olá, sou o seu assistente virtual. Como posso ajudar?"}]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


if prompt:= st.chat_input("Pergunte algo!"):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})
    center = st.container()
    col1, col2, col3 = st.columns([1,1,1])
    with col2:
        with st.spinner("Pensando..."):
            response = model.generate_content((f"Você é um vendedor de consórcios para a Volkswagen, sabendo que atualmente as parcelas estão reduzidas, sem juros de entrada e sem burocracia e a tabela de crédito para parecelas segue a seguinte estrutura: créditos de 50 mil reais, as parcelas são de 405.63 reais, créditos de 60 mil reais, as parcelas são de 486.75 reais, créditos de 80 mil reais, as parcelas são de 649.00 reais, créditos de 90 mil reais, as parcelas são de 730.13 reais, créditos de 120 mil reais, as parcelas são de 973.50 reais, créditos de 140 mil reais, as parcelas são de 1135.75 reais, créditos de 160 mil reais, as parcelas são de 1298.00 reais e créditos de 180 mil reais, as parcelas são de 1460.25 reais. Com isto, responda a seguinte pergunta para um cliente e caso não seja uma informação adicionada neste contexto, ignore a pergunta e responda 'Desculpa, mas não possuo esta informação, entre em contato com nossos vendedores pelo canal (xx)xxxx-xxxx': {str(prompt)}"))
    with st.chat_message("assistant"):
        st.markdown(response.text.replace("$","\$"))
    st.session_state.messages.append({"role": "assistant", "content": response.text.replace("$","\$")})