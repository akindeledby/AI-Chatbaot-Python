# Using session_state feature.
# session_state feature os streamlit helps our program/app to keep track or remember data betwqeen interactions.
# With this functionality, we can enable our chat-app to respond back what ever is typed at the prompt.

import streamlit as st

with st.chat_message(name = "assistant"): # This can take either of two roles: user or assistant. We can also use an Emoji of choice with the "avatar" parameter.
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
    
    response = f"Echo: {prompt}"
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistat response to the chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
                                      
