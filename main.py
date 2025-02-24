import google.generativeai as genai
import os
import streamlit as st
from streamlit_option_menu import option_menu

# ✅ Load Google Gemini API key from environment variables
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("⚠️ API key not found! Set it as an environment variable before running the script.")
else:
    genai.configure(api_key=api_key)

# ✅ Sidebar navigation menu
with st.sidebar:
    page = option_menu(
        "📖 AI Storytelling Companion",
        ["Home", "Character Builder", "Plot Structuring", "Dialogue Helper", "Editing & Feedback"],
        icons=["house", "person", "book", "chat-dots", "pencil"],
        menu_icon="menu-button-wide",
        default_index=0
    )

st.markdown("<style>body{background-color: #f4f4f4;}</style>", unsafe_allow_html=True)

# ✅ Function to interact with Gemini AI
def generate_response(prompt):
    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"⚠️ An error occurred: {str(e)}"

# ✅ Home Page - Generate Story Ideas
if page == "Home":
    st.title("📜 AI Storytelling Companion")
    st.subheader("🔍 Generate story ideas with AI")
    user_prompt = st.text_area("Enter a story idea:", placeholder="E.g., A young orphan discovers a magical key...")

    if st.button("✨ Generate Plot"):
        if user_prompt:
            with st.spinner("Generating your story idea..."):
                plot = generate_response(f"Generate a plot idea based on: {user_prompt}")
            st.success("✅ Plot generated successfully!")
            st.text_area("📖 Generated Plot:", plot, height=150)
        else:
            st.warning("⚠️ Please enter a story idea first!")

# ✅ Character Builder Page
elif page == "Character Builder":
    st.title("👤 Character Builder")
    char_prompt = st.text_input("Describe your character:", placeholder="E.g., A brave hero with a troubled past...")

    if st.button("🎭 Generate Character"):
        with st.spinner("Creating a unique character..."):
            character = generate_response(f"Generate a unique character profile for: {char_prompt}")
        st.success("✅ Character generated successfully!")
        st.text_area("🎭 Character Profile:", character, height=150)

# ✅ Plot Structuring Page
elif page == "Plot Structuring":
    st.title("📖 Plot Structuring")
    plot_structure = st.selectbox("Choose a structure", ["Three-Act Structure", "Hero’s Journey", "Freytag’s Pyramid"])
    user_story = st.text_area("Enter your story idea:", placeholder="E.g., A detective receives anonymous letters predicting crimes...")

    if st.button("📌 Get Structure"):
        with st.spinner("Structuring your story..."):
            structured_plot = generate_response(f"Suggest a {plot_structure} outline for: {user_story}")
        st.success("✅ Story structure generated!")
        st.text_area("📖 Story Structure:", structured_plot, height=150)

# ✅ Dialogue Helper Page
elif page == "Dialogue Helper":
    st.title("🗨 Dialogue Helper")
    dialogue_prompt = st.text_area("Describe a scene for dialogue generation:", placeholder="E.g., A heated argument between a detective and a suspect...")

    if st.button("🎬 Generate Dialogue"):
        with st.spinner("Generating dialogue..."):
            dialogue = generate_response(f"Generate a dialogue for: {dialogue_prompt}")
        st.success("✅ Dialogue generated!")
        st.text_area("🎬 Generated Dialogue:", dialogue, height=150)

# ✅ Editing & Feedback Page
elif page == "Editing & Feedback":
    st.title("✍️ Editing & Feedback")
    writing_input = st.text_area("Enter your text for feedback:", placeholder="Paste your writing here...")

    if st.button("📝 Get Feedback"):
        with st.spinner("Analyzing your text..."):
            feedback = generate_response(f"Give feedback on this writing: {writing_input}")
        st.success("✅ Feedback generated!")
        st.text_area("📝 Writing Feedback:", feedback, height=150)
