import streamlit as st
import streamlit.components.v1 as components
from janusbot_helper import *
from PIL import Image

#from janusbot_helper_usegroq import *

# st.title("SQL AI")

#initialize chat histroy

if "messages" not in st.session_state:
    st.session_state.messages=[]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

html_code = """ 

<body>
        <div class="App">
            <div class="Content">
                <div class="companyLogo">
                    <img src="https://raw.githubusercontent.com/avipnvhawkeye/test-avipnv/main/images/pgd_logo.png">
                </div>
                <div class="chatBoxTitleBox">
                    <img src="https://raw.githubusercontent.com/avipnvhawkeye/test-avipnv/main/images/sql_ai_logo.png"><span class="chatBotLogo">SQL AI</span>
                    <h1>Welcome to SQL Code Assistant</h1>
                    <h3>Your AI-powered copilot for SQL</h3>
                </div>
            </div>
        </div>
    </body>

"""
st.markdown(html_code, unsafe_allow_html=True)
   


sqlAiStyle = """ <style> 

    body,
    textarea {
        font-family: 'Calibri', sans-serif;
        background: #fff;
    }

    .App {
        text-align: center;
        font-family: Arial, Helvetica, sans-serif;
        font-size: 1em;
        font-weight: normal;
    }

    button,
    [type='button'],
    [type='reset'],
    [type='submit'] {
        -webkit-appearance: button;
        background-color: transparent;
        background-image: none;
        border: 0;
    }

    .Content {
        width: 100%;
        display: table;
    }

    .questionArea {}

    .answerWindow {}

    .Sidebar {
        min-height: 96vh;
        width: 15%;
        display: flex;
        flex-direction: column;
        color: #666;
        float: left;
        background-color: #eee;
        padding: 20px;
        font-size: 12px;
        position: relative;
    }

    .Sidebar h2 {
        font-size: 22px;
        display: inline;
    }

    .Sidebar span {
        font-size: 12px;
        display: inline;
    }

    .sideList {
        padding: 1rem;
        margin-top: 0.375rem;
    }

    .sideList li {
        list-style: none;
    }

    .sideList li a {
        display: flex;
        padding-top: 0.5rem;
        padding-bottom: 0.5rem;
        padding-left: 0.75rem;
        padding-right: 0.75rem;
        column-gap: 0.75rem;
        align-items: center;
        border-radius: 0.5rem;
        font-size: 0.875rem;
        line-height: 1.25rem;
        text-decoration: none;
        color: rgb(51 65 85);
    }

    .sideList li a:hover {
        background-color: #F3F4F6;
    }

    .collapseBtn {
        position: absolute;
        right: 10px;
        bottom: 10px;
    }

    .collapseBtn svg {
        bottom: -6px;
        position: relative;
    }


    .companyLogo {
        width: 100%;
        text-align: left;
        padding: 10px 0px 10px 20px;
        margin-bottom: 50px;
        border-bottom: 1px solid #ccc;
    }

    .chatBoxTitleBox {
        margin: 0 auto;
    }

    h1 {
        color: #2c69ba;
        margin: 10px 0px 0px 0px;
        padding: 0;
    }

    h3 {
        color: #000;
        margin: 10px 0px 20px 0px;
        padding: 0;
    }

    .chatBoxTitleBox img {
        padding: 0px 0px 0px 0px;
    }

    .chatBotLogo {
        display: inline-block;
        vertical-align: top;
        padding: 8px;
    }

    .registration {
        padding: 10px;
        text-decoration: none;
        font-size: 15px;
        color: rgb(51 65 85);
    }

    .containerHead {
        background: #bad6fa;
        color: #000;
        font-size: 16px;
        font-weight: bold;
        padding: 8px 0px 8px 20px;
        text-align: left;
    }

    .container {
        width: 60%;
        margin: 0 auto;
        padding: 30px;
        background: #f4f4f4;
    }

    .containerChatAssistance {
        background: #fff;
        padding-left: 0;
        padding-right: 0;
        width: 63.5%;
    }

    .botChat {
        display: inline-block;
    }

    .botChat p {

        font-size: 14px;
        color: #000;
        padding: 0px 0px 0px 40px;
    }

    .chatInpt {
        padding: 1rem;
        padding-bottom: 3rem;
        border-radius: 0.5rem;
        border: 1px solid #999;
        line-height: 1.25rem;
        background-color: #F3F4F6;
        text-align: left;
        border-top-right-radius: 0;
        border-top-left-radius: 0;
    }

    .botIcon {
        width: 30px;
    }

    .botTxt {
        display: inline-block;
        vertical-align: top;
        padding: 5px;
        font-weight: bold;
        font-size: 14px;
    }

    .nobg {
        background-color: none !important;
        background: none;
    }

    .bgwhite {
        background-color: #fff !important;
        background: #fff;
    }

    .textareaInpt {
        padding: 1rem;
        padding-bottom: 3rem;
        border-radius: 0.5rem;
        border-color: #999;
        width: 100%;
        line-height: 1.25rem;
        background-color: #F3F4F6;
    }

    .actionBarHolder {
        position: relative;
        width: 100%;
        margin: 0 auto;
        top: -40px;
    }

    .userActions {
        width: 98%;
        display: inline-block;
    }

    .userActions button {
        display: inline-flex;
        justify-content: center;
        align-items: center;
        border-radius: 0.5rem;
        color: #6B7280;
    }

    .userActions button:hover {
        color: #2563EB;
    }

    .attachIcon {
        float: left;
    }

    .sendIcon {
        float: right;
    }

    .sendIcon:hover {
        cursor: pointer;
    }

    .appview-container {
        background: #fff;
    }

    .block-container {
        width: 100%;
        max-width: 100%;
    }

    textarea[data-testid=stChatInputTextArea] {
        padding: 1rem;
        padding-bottom: 3rem;
        border-radius: 0.5rem;
        border-color: #999;
        width: 100%;
        line-height: 1.25rem;
        background-color: #F3F4F6;
        color: #000;
    }

    .stChatMessage {
        padding: 1rem;
        padding-bottom: 3rem;
        border-radius: 0.5rem;
        border-color: #999;
        width: 100%;
        line-height: 1.25rem;
        background-color: #F3F4F6;
        color: #000;
    }

    .stMarkdown {
        color: #000;
    }

    [data-testid="stChatMessageContent"] {
        
    }

    [data-testid="stMarkdownContainer"] {
        

    }

    [data-testid="stMarkdownContainer"] p{
        padding-top: 40px;
    }

    .st-emotion-cache-vj1c9o {
        background: #fff;
    }

    [data-testid="chatAvatarIcon-user"] svg {
        
    }

    [data-testid="chatAvatarIcon-user"]::after{
        content: "USER";
        padding-left: 75px;
        font-weight: bold;
    }

    [data-testid="chatAvatarIcon-user"] {
        background:url('https://raw.githubusercontent.com/avipnvhawkeye/test-avipnv/main/images/user_chat.png') no-repeat;
        border-radius: 0;
        background-size: contain;
    }

    [data-testid="chatAvatarIcon-assistant"] svg {
        display:none;
    }

    [data-testid="chatAvatarIcon-assistant"]::after{
        content: "SQLAI";
        padding-left: 100px;
        font-weight: bold;
    }

    [data-testid="chatAvatarIcon-assistant"]{
        background:url('https://raw.githubusercontent.com/avipnvhawkeye/test-avipnv/main/images/ai_chat.png') no-repeat;
        border-radius: 0;
        background-size: contain;
    }

</style> """
st.markdown(sqlAiStyle, unsafe_allow_html=True)

#react to user input

if prompt := st.chat_input("Please write your question here"):
    
    # Dispaly user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    #add user messgae to chat history
    st.session_state.messages.append({"role":"user","content":prompt})

    #response =f"Echo: {prompt}"
    response =query_response(prompt)

    #Display assistant response in chat message container

    with st.chat_message("assistant"):
        st.markdown(response)

    #Add response to chat history

    st.session_state.messages.append({"role":"assistant","content":response})
    
