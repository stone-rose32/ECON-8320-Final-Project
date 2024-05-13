import streamlit as st
import requests

# Create a function to get the data from the URL
def get_data(url):
  response = requests.get(url)
  return response.text

def main():
    # Create a section for the project code
    st.title("Project Code")
    pc_intro_text = """
    This tab's purpose is to show the code used in this project. Ultimately, there are aspects
      of the project's code I know can be improved upon which I touched on in the "About" page. 
      Alas, at some point, the project meets the required criteria, and it becomes time to 
      move on. As Leonadro Da Vinci said, "Art is never finished, only abandoned."

    Welp, consider this abandoned for the time being. The source code can be found
      on the Github repository linked below. Feel free to suggest any edits!

    [Link to Github Repository](https://github.com/stone-rose32/ECON-8320-Final-Project/tree/main)
    """
    st.write(pc_intro_text)
    
    # Create tabs for the different sections of the project code
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["Initial Data Extraction", "Streamlit Application Core", "About Page", "GetCensusData Class", "Data and Visual Page", "Project Code Page"])
    # Load the code from the respective URLs
    with tab1:
        app_data_url = 'https://raw.githubusercontent.com/stone-rose32/ECON-8320-Final-Project/main/app_data.py'
        data_code = get_data(app_data_url)
        st.header('Initial Data Extraction Code')
        st.code(data_code, language='python')
    with tab2:
        app_data_url = 'https://raw.githubusercontent.com/stone-rose32/ECON-8320-Final-Project/main/home.py'
        data_code = get_data(app_data_url)
        st.header('Streamlit Application Core Code')
        st.code(data_code, language='python')
    with tab3:
        app_data_url = 'https://raw.githubusercontent.com/stone-rose32/ECON-8320-Final-Project/main/pages/1_about.py'
        data_code = get_data(app_data_url)
        st.header('About Page Code')
        st.code(data_code, language='python')
    with tab4:
        app_data_url = 'https://raw.githubusercontent.com/stone-rose32/ECON-8320-Final-Project/main/GetCensusData.py'
        data_code = get_data(app_data_url)
        st.header('GetCensusData Class Code')
        st.code(data_code, language='python')
    with tab5:
        app_data_url = 'https://raw.githubusercontent.com/stone-rose32/ECON-8320-Final-Project/main/pages/3_data_and_visuals.py'
        data_code = get_data(app_data_url)
        st.header('Data and Visual Page Code')
        st.code(data_code, language='python')
    with tab6:
        app_data_url = 'https://raw.githubusercontent.com/stone-rose32/ECON-8320-Final-Project/main/pages/4_project_code.py'
        data_code = get_data(app_data_url)
        st.header('Project Code Page Code')
        st.code(data_code, language='python')

# Run the main function
if __name__ == "__main__":
    main()
