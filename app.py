# With this idea/feature of session_state, we can develop a similar chatbot like Chat-GPT, but will not echo back the user prompt as done in "streamlit-echo.py". 
# We will install "openai" library: "pip3 install openai" and then import it into our app

import openai
import streamlit as st

st.title("ChatBot Assistant")

openai.api_key = st.secrets["OPENAI_API_KEY"]

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

with st.chat_message(name = "assistant", avatar = ""): # This can take either of two roles: user or assistant. We can also use an Emoji of choice with the "avatar" parameter.
    st.write("Hello")

# Initialize chat history. The messages is an empty list when the browser first loads.
if "messages" not in st.session_state:
    st.session_state.messages = []

# The essance/idea behind this is to create a dictionary of the user and the assistant: - user: content(our prompt), assistant: content(the response)
# Display chat history from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# React to user input
if prompt := st.chat_input("What's up?"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})


    with st.chat_message("assistance"):
        message_placeholder = st.empty()
        full_response = ""
        for response in open.ChatComplete.create(
            model = st.session_state["openai_model"],
            messages = [
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream = True,
        ):
            full_response += response.choices[0].delta.get("content", "")
            message_placeholder.markdown(full_response + "| ")
        message_placeholder.markdown(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response})

