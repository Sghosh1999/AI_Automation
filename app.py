import streamlit as st
import dataset_analysis
import text_summ
import regresion
import classification
from PIL import Image

def main():
    # Title
    st.title("MLAI: An Integrated Software platform for AI Automation")

    # Sidebar
    activities = ["Home", "Dataset Explorer", "ML Classifiers", "ML Regression","Text Summarizer"]
    choice = st.sidebar.selectbox("Choose Activity", activities)

    if choice == "Home":
        st.header('Empowering companies to jumpstart AI and generate real-world value')
        st.subheader('Use exponential technologies to your advantage and lead your industry with confidence through innovation.')

        
        image = Image.open('images/img0.jpg')
        st.image(image, use_column_width=True, caption='Data Mining')

    if choice == "Dataset Explorer":
        st.subheader("Dataset Explorer")
        dataset_analysis.main()
    
    if choice == "ML Classifiers":
        classification.main()
    if choice == "ML Regression":
        regresion.main()
    if choice == "Text Summarizer":
        text_summ.main()



if __name__ == '__main__':
    main()