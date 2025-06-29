import streamlit as st
from streamlit_option_menu import option_menu
from app.utils.agenda_loader import load_agenda_for_day
import io
import contextlib
from pathlib import Path
import json
from app.utils.exercise_generator import generate_exercises
from app.utils.exercise_generator import generate_daywise_exercise_file
import os
generate_daywise_exercise_file()


# Load syllabus
syllabus_path = Path("app/data/syllabus.json")
if syllabus_path.exists():
    with open(syllabus_path, "r") as f:
        syllabus = json.load(f)
else:
    syllabus = {}

# Dummy fallback for generating exercises
def fetch_day_exercises(concepts):
    return [
        f"Write a Python program to demonstrate the concept: **{concept}**"
        for concept in concepts
    ]

# Set layout
st.set_page_config(layout="wide", page_title="Python Tutorial Agent")
st.title("🐍 Python Tutorial Agent")

# Create two columns
left_col, right_col = st.columns([1, 3])

# --- LEFT PANEL ---
with left_col:
    st.markdown("### 📅 Select Day")
    selected_day = st.radio(
        "Choose Day",
        [f"Day {i}" for i in range(1, 31)],
        index=0,
        key="day_selector",
        label_visibility="collapsed"
    )

# Load agenda
agenda = load_agenda_for_day(selected_day)
concepts = agenda.get("concepts", [])

# --- RIGHT MAIN PANEL ---
with right_col:
    st.markdown(f"## 📘 {selected_day} Tutorial")

    selected_tab = option_menu(
        menu_title=None,
        options=[
            "Agenda", "Exercises", "Code Playground",
            "Quiz & Assignments", "Feedback", "Grading", "AI Motivation"
        ],
        icons=[
            "calendar", "bar-chart", "code", "book",
            "chat-left-text", "award", "emoji-smile"
        ],
        orientation="horizontal",
        default_index=0,
    )

    if selected_tab == "Agenda":
        st.markdown(f"### 📝 Topic: `{agenda['topic']}`")
        st.subheader("🎯 Learning Objectives")
        for obj in agenda["objectives"]:
            st.markdown(f"- {obj}")

        st.subheader("🔍 Key Concepts")
        for concept in concepts:
            st.markdown(f"- {concept}")

    # Tab: Exercises
    elif selected_tab == "Exercises":
        st.header(f"🧪 Python Exercises for {selected_day}")
        day_concepts = syllabus.get(selected_day, {}).get("concepts", [])
        exercises = generate_exercises(day_concepts)

        if not exercises:
            st.warning("⚠️ No exercises available for this day.")
        else:
            for idx, exercise in enumerate(exercises, start=1):
                with st.expander(f"{exercise['title']}"):
                    st.markdown(f"**📝 Problem:** {exercise['description']}")
                    st.code("# Use Code Playground to Execute your code.", language="python")

                    # Optional: Show solution toggle
                    # if st.checkbox(f"💡 Show Sample Solution for: {exercise['title']}", key=f"sol_{exercise['title']}"):
                        # st.code(exercise["sample_solution"], language="python")
                    if st.toggle(f"💡 Show Sample Solution for: {exercise['title']}", key=f"sol_{exercise['title']}"):
                        st.code(exercise["sample_solution"], language="python")

    elif selected_tab == "Code Playground":
        st.header("💻 Live Python Code Playground")
        code_input = st.text_area("✍️ Write your Python code here:", height=250, value="""\
# Example: Greet the learner
name = "Abhishek"
print(f"Hello, {name}! Welcome to Python learning.")""")
        if st.button("▶️ Run Code"):
            with st.expander("📤 Output", expanded=True):
                output_buffer = io.StringIO()
                try:
                    with contextlib.redirect_stdout(output_buffer):
                        exec(code_input, {})
                        output = output_buffer.getvalue()
                        st.code(output if output else "✅ Code ran successfully with no output.", language="text")
                except Exception as e:
                    st.error(f"❌ Error during execution:\n{e}")

    elif selected_tab == "Quiz & Assignments":
        st.warning("📋 20 MCQs and 5 code snippets challenge coming here...")

    elif selected_tab == "Feedback":
        st.text_area("✍️ Your feedback about today's learning:")

    elif selected_tab == "Grading":
        st.metric("Grading Result", "In Progress")

    elif selected_tab == "AI Motivation":
        st.markdown("🎉 GPT Motivation: Keep learning! You did great today.")
