import streamlit as st

# Create a function to show the about page
def show():
    st.title("About...")
    # Create a section for the author
    st.header("the Author")
    author_text = """
    My name is Austin Rose, and I am currently a graduate student at the University of Nebraska- Omaha (UNO) majoring in Data Science. Prior to attending UNO, I graduated from the University of Nebraska- Lincoln with a degree in Actuarial Sciences through the College of Business.

    After graduating with my undergrad degree, I began working for a workers' compensation insurance startup in Omaha as a data analyst. From there, I moved to a fully remote role as a business intelligence analyst for a paratransit-scheduling software company based out of Pennsylvania before transitioning into my     current role. I currently work for the Kiewit Corporation in their technology group as a data analyst on the IT Financial Management team.
    """
    st.write(author_text)

    # Create a section for the project
    st.header("the Project")
    project_text = """
    The application you are looking at serves as the final project for my Tool for Data Analysis course (ECON 8320). The goal of this project is to utilize and demonstrate my knowledge of Python tools that were taught throughout the past semester. Further description for the project details can be found on the GitHub repository (https://github.com/stone-rose32/ECON-8320-Final-Project).
    """
    st.write(project_text)

# Create a main function to run the about page
def main():
    show()


# Run the main function
if __name__ == "__main__":
    main()
