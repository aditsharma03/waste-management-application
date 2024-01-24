import streamlit as st

def render_status_tab():
    st.title("System Status")

    # Dummy data for demonstration
#    dustbin_1_fill = 0
#    dustbin_2_fill = 0
#    dustbin_3_fill = 0

    # Create a two-column layout
    col1, col2 = st.columns(2)


    # Display sliders in the second column
    with col2:
        col21, col22 = col2.columns(2)
        with col22:
            st.subheader("Fill Levels")
            dustbin_1_fill = st.slider("Dustbin 1 Fill (%)", 0, 100, 30, key="dustbin_1_slider")
            dustbin_2_fill = st.slider("Dustbin 2 Fill (%)", 0, 100, 60, key="dustbin_2_slider")
            dustbin_3_fill = st.slider("Dustbin 3 Fill (%)", 0, 100, 80, key="dustbin_3_slider")


    # Display bars for dustbins above sliders
    with col1:
        #st.subheader("Dustbin Status")
        # Bar for Dustbin 1 with label
        st.text("Organic Waste")
        st.progress(dustbin_1_fill / 100.0)
        if dustbin_1_fill > 90:
            st.warning("Dustbin 1 is almost full. Please empty!")

        # Bar for Dustbin 2 with label
        st.text("Recyclables")
        st.progress(dustbin_2_fill / 100.0)
        if dustbin_2_fill > 90:
            st.warning("Dustbin 2 is almost full. Please empty!")

        # Bar for Dustbin 3 with label
        st.text("Non-Recyclables")
        st.progress(dustbin_3_fill / 100.0)
        if dustbin_3_fill > 90:
            st.warning("Dustbin 3 is almost full. Please empty!")

if __name__ == "__main__":
    render_status_tab()

