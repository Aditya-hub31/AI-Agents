import streamlit as st

# Set page title
st.title("Utility-Based Agent")

# Define utility values
utilities = {
    "Study": 8,
    "Netflix": 3,
    "Walk": 5,
    "Sleep": 6
}

st.write("### Select the activities you are considering:")

# Create checkboxes for each option
user_choices = []
for activity in utilities.keys():
    if st.checkbox(activity):
        user_choices.append(activity)

# Button to make decision
if st.button("Decide Best Option"):
    if not user_choices:
        st.warning("Please select at least one option.")
    else:
        # Choose the activity with the highest utility
        best_choice = max(user_choices, key=lambda x: utilities[x])
        st.success(f"✅ Based on utility scores, you should: **{best_choice}** (Score: {utilities[best_choice]})")

        st.write("### Utility Scores of Selected Options:")
        for choice in user_choices:
            st.write(f"- {choice}: {utilities[choice]}")
