# Importing packages: streamlit for the frontend, requests to make the api calls
import streamlit as st
import requests
import json

from PIL import Image
import os

@st.cache
def load_image(img):
	im = Image.open(img)
	return im

def main():
    #st.markdown(title_temp,unsafe_allow_html=True)
    our_image = Image.open(os.path.join('dg+az.png'))
    st.image(our_image,width=740)
 
    page = Display()
    service = page.static_elements()
    #apicall = MakeCalls()
    if service == "about":
        st.write(
            "Simple interface to manage devices on Azure IoT HUB"
        )
        st.write(
            
            "**Internal Use Only**"
        )
    else:
        st.write(
            "Select the parameters from the list"
        )


        
class Display:
    def __init__(self):
        st.title("Azure IoT HUB Device Manager")
        st.sidebar.header("Select the Service")
        self.service_options = st.sidebar.selectbox(
            label="",
            options=[
                "About the tool",
                "New Device",
                "Delete Device",
                "Something",
                "Something",
            ],
        )
        self.service = {
            "About the tool": "about",
            "New Device": "New Device",
            "Delete Device": "ner",
            "Something": "sentiment",
            "Something": "summary",
        }

    def static_elements(self):
        return self.service[self.service_options]

    def dynamic_element(self, models_dict: dict):
        """
        This function is used to generate the page for each service.
        :param service: String of the service being selected from the side bar.
        :param models_dict: Dictionary of Model and its information. This is used to render elements of the page.
        :return: model, input_text run_button: Selected model from the drop down, input text by the user and run botton to kick off the process.
        """
        st.header(self.service_options)
        model_name = list()
        model_info = list()
        for i in models_dict.keys():
            model_name.append(models_dict[i]["name"])
            model_info.append(models_dict[i]["info"])
        st.sidebar.header("Model Information")
        for i in range(len(model_name)):
            st.sidebar.subheader(model_name[i])
            st.sidebar.info(model_info[i])
        model: str = st.selectbox("Select the Trained Model", model_name)
        input_text: str = st.text_area("Enter Text here")
        if self.service == "qna":
            query: str = st.text_input("Enter query here.")
        else:
            query: str = "None"
        run_button: bool = st.button("Run")
        return model, input_text, query, run_button

if __name__ == "__main__":
    main()
    
st.sidebar.text(" ")
st.sidebar.text(" ")
st.sidebar.text(" ")
st.sidebar.text(" ")
st.sidebar.text(" ")
st.sidebar.text(" ")
st.sidebar.text(" ")
st.sidebar.text(" ")
st.sidebar.text(" ")
st.sidebar.text(" ")
st.sidebar.text(" ")
st.sidebar.text(" ")
st.sidebar.text(" ")
st.sidebar.text(" ")
st.sidebar.text(" ")
st.sidebar.text(" ")
st.sidebar.text(" ")
st.sidebar.text(" ")
st.sidebar.text(" ")
st.sidebar.text(" ")
st.sidebar.text(" ")
st.sidebar.text(" ")
st.sidebar.text(" ")
st.sidebar.text(" ")
st.sidebar.subheader("About the App")
st.sidebar.text("Datagroup Ulm")
st.sidebar.text("mauroanibal.benetti@datagroup.de")