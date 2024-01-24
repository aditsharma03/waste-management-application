import streamlit as st

def render_about_tab():
    st.title("About Waste Management System")

    st.write(
        """
        Welcome to the Waste Management System, a tool designed to promote sustainable living through effective waste segregation and management. Waste management is a crucial aspect of environmental stewardship, and our system aims to empower individuals and communities to make informed decisions about their waste.
""")


    st.subheader("**Why Segregation Matters:**")
    st.write(
        """
        Efficient waste segregation is the first step towards responsible waste management. By categorizing waste into distinct types such as recyclables, organic matter, and non-recyclables, we can significantly reduce environmental impact and contribute to a cleaner, healthier planet.

        **Our Mission:**
        Our mission is to raise awareness about the importance of waste segregation and provide a user-friendly platform for predicting the appropriate disposal category of various items. By integrating technology with eco-conscious practices, we hope to inspire positive change and foster a sustainable mindset.

        """)

    st.subheader("**How to Use the System:**")
    st.write(
            """
        1. Upload an image of the item in question.
        2. Receive instant feedback on the recommended waste disposal category.
        3. Make informed choices to minimize your ecological footprint.

        Join us in our commitment to building a greener future. Together, we can make a difference—one conscious decision at a time.

        Thank you for being a part of the Waste Management System community!
        """
    )


