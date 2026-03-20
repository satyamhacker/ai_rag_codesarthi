import streamlit as st
import sqlite3
from passlib.hash import pbkdf2_sha256

# --- 1. DATABASE & AUTH UTILITIES ---
def init_db():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS users(username TEXT PRIMARY KEY, password TEXT)')
    conn.commit()
    return conn

def create_user(username, password):
    hashed_pw = pbkdf2_sha256.hash(password)
    try:
        conn = init_db()
        c = conn.cursor()
        c.execute('INSERT INTO users(username,password) VALUES (?,?)', (username, hashed_pw))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False

def login_user(username, password):
    conn = init_db()
    c = conn.cursor()
    c.execute('SELECT password FROM users WHERE username = ?', (username,))
    data = c.fetchone()
    if data and pbkdf2_sha256.verify(password, data[0]):
        return True
    return False

# --- 2. UI COMPONENTS (MODULAR FUNCTIONS) ---

def show_login_page():
    st.subheader("Login Section")
    username = st.text_input("Username", key="login_user")
    password = st.text_input("Password", type='password', key="login_pass")
    
    if st.button("Login"):
        if login_user(username, password):
            st.session_state['logged_in'] = True
            st.session_state['username'] = username
            st.success(f"Welcome back, {username}!")
            st.rerun()
        else:
            st.error("Invalid Username/Password")

def show_signup_page():
    st.subheader("Create New Account")
    new_user = st.text_input("Username", key="signup_user")
    new_password = st.text_input("Password", type='password', key="signup_pass")
    
    if st.button("Signup"):
        if create_user(new_user, new_password):
            st.success("Account created! Please switch to Login.")
        else:
            st.error("Username already exists.")

def show_chat_interface():
    # Sidebar Logout
    st.sidebar.write(f"Logged in as: **{st.session_state['username']}**")
    if st.sidebar.button("Logout"):
        st.session_state['logged_in'] = False
        st.session_state['username'] = None
        st.session_state['messages'] = []
        st.rerun()

    st.write(f"### Welcome to your Private Chat, {st.session_state['username']}")
    
    # Display Chat History
    for message in st.session_state['messages']:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # User Input
    if prompt := st.chat_input("Ask about your documents..."):
        st.session_state['messages'].append({"role": "user", "content": prompt})
        
        # --- RAG Logic Placeholder ---
        # response = qa_chain.invoke({"query": prompt})['result']
        response = f"Hello {st.session_state['username']}, this is a placeholder response."
        
        st.session_state['messages'].append({"role": "assistant", "content": response})
        st.rerun()

# --- 3. MAIN APP CONTROLLER ---

def main():
    st.set_page_config(page_title="RAG Auth System", layout="wide")
    st.title("📚 Private RAG Chatbot")

    # Initialize Session State
    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False
    if 'messages' not in st.session_state:
        st.session_state['messages'] = []
    if 'username' not in st.session_state:
        st.session_state['username'] = None

    # Logic Switcher
    if not st.session_state['logged_in']:
        # Show Auth Sidebar
        menu = ["Login", "SignUp"]
        choice = st.sidebar.selectbox("Auth Menu", menu)
        
        if choice == "Login":
            show_login_page()
        else:
            show_signup_page()
    else:
        # Show the actual Chat App
        show_chat_interface()

if __name__ == '__main__':
    main()