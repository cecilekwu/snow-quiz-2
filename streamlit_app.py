import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
from PIL import Image

image = Image.open('Summit banner.png')

# Function to display header image
def display_header_image():
    st.image(image, use_column_width=True)

# Intro page
def intro_page():
    display_header_image()
    st.title("Welcome to the Personality Quiz")
    st.write("This quiz will help determine your personality based on your preferences.")
    if st.button("Start Quiz"):
        st.session_state.current_question_index = 1
        st.experimental_rerun()

# Question pages
def question_page(question, options):
    display_header_image()
    st.title("Personality Quiz")
    st.header("Question:")
    st.write(question)
    selected_option = st.radio("Choose one:", options)
    if st.button("Next"):
        st.session_state[f"answer_{st.session_state.current_question_index}"] = selected_option
        st.session_state.current_question_index += 1
        st.experimental_rerun()

# Results page
def result_page():
    display_header_image()
    st.title("Personality Quiz - Results")
    st.write("Thank you for completing the quiz!")

    # Get answers
    answers = [st.session_state.get(f"answer_{i}") for i in range(1, 5)]

    # Determine personality
    personality = determine_personality(answers)

    # Display personality type
    st.write("Your personality type is:", personality)

    # Display personality description and image
    personality_descriptions = {
        "Type 1": {
            "description": "You are an introverted and calm individual. You enjoy spending time alone, reading books, and relaxing at the beach.",
            "image": "https://cdn.cookielaw.org/logos/cb85e692-4053-4d0a-8dda-d24b5daa8b06/da03e0fe-832b-44c4-8eb4-08e1f224aa22/SNO-SnowflakeLogo_blue.png"
        },
        "Type 2": {
            "description": "You are an introverted and imaginative person. You love spending time alone, reading books, and exploring the mountains.",
            "image": "https://cdn.cookielaw.org/logos/cb85e692-4053-4d0a-8dda-d24b5daa8b06/da03e0fe-832b-44c4-8eb4-08e1f224aa22/SNO-SnowflakeLogo_blue.png"
        },
        "Type 3": {
            "description": "You are an outgoing and adventurous person. You enjoy outdoor activities like hiking and spending time at the beach.",
            "image": "https://cdn.cookielaw.org/logos/cb85e692-4053-4d0a-8dda-d24b5daa8b06/da03e0fe-832b-44c4-8eb4-08e1f224aa22/SNO-SnowflakeLogo_blue.png"
        },
        "Type 4": {
            "description": "You are an outgoing and adventurous individual. You love outdoor activities like hiking and exploring the mountains.",
            "image": "https://cdn.cookielaw.org/logos/cb85e692-4053-4d0a-8dda-d24b5daa8b06/da03e0fe-832b-44c4-8eb4-08e1f224aa22/SNO-SnowflakeLogo_blue.png"
        }
    }

    st.write("Description:")
    if personality in personality_descriptions:
        st.write(personality_descriptions[personality]["description"])
        st.image(personality_descriptions[personality]["image"])
    else:
        st.write("No description available for this personality type.")

# Determine personality based on answers
def determine_personality(answers):
    # Define personality types and their corresponding answer combinations
    personality_types = {
        ("Spring", "Blue", "Reading", "Beach"): "Type 1",
        ("Spring", "Blue", "Reading", "Mountains"): "Type 2",
        ("Spring", "Blue", "Hiking", "Beach"): "Type 3",
        ("Spring", "Blue", "Hiking", "Mountains"): "Type 4",
        # Add more combinations as needed
    }

    # Check if the answers match any of the predefined combinations
    for combination, personality in personality_types.items():
        if all(answer in combination for answer in answers):
            return personality

    return "Unknown"

# Initialize current_question_index if not already initialized
if 'current_question_index' not in st.session_state:
    st.session_state.current_question_index = 0

# Main function
def main():
    if st.session_state.current_question_index == 0:
        intro_page()
    elif st.session_state.current_question_index < 5:
        questions = [
            "Which season do you prefer?",
            "What is your favorite color?",
            "Choose a hobby:",
            "What is your ideal vacation destination?"
        ]
        options = [
            ("Spring", "Fall"),
            ("Blue", "Red"),
            ("Reading", "Hiking"),
            ("Beach", "Mountains")
        ]
        question = questions[st.session_state.current_question_index - 1]
        option = options[st.session_state.current_question_index - 1]
        question_page(question, option)
    else:
        result_page()

if __name__ == "__main__":
    main()
