import streamlit as st
from tabs.about import render_about_tab
from tabs.prediction import render_prediction_tab
from tabs.status import render_status_tab


st.set_page_config(page_title="Waste Management System", page_icon=":recycle:")
tabs = {  "Status": render_status_tab, "Prediction": render_prediction_tab, "About": render_about_tab}

selected_tab = st.sidebar.selectbox("Select Tab", list(tabs.keys()))
tabs[selected_tab]()

