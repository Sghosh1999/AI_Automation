import streamlit as st
import pandas as import pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

@st.cache
def main():
    def file_selector(folder_path='./climate_dataset'):
        filenames = os.listdir(folder_path)
        selected_filename = st.selectbox("Select A File", filenames)
        return os.path.join(folder_path, selected_filename)

    filename = file_selector()  # Fetching the Dataset
    st.info("You Selected {}".format(filename))

    # Read Dataset
    df = pd.read_csv(filename)
