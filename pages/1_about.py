import streamlit as st

def show():
    st.title("About...")
    st.header("the Author")
    author_text = """
    My name is Austin Rose, and I am currently a graduate student at the University of Nebraska- Omaha (UNO) majoring in Data Science. Prior to attending UNO,
    I graduated from the University of Nebraska- Lincoln with a degree in Actuarial Sciences through the College of Business.

    After graduating with my undergrad degree, I began working for a workers' compensation insurance startup in Omaha as a data analyst. From there, I moved to a 
    fully remote role as a business intelligence analyst for a paratransit-scheduling software company based out of Pennsylvania before transitioning into my current role. 
    I currently work for the Kiewit Corporation in their technology group as a data analyst on the IT Financial Management team.
    """
    st.write(author_text)

    st.header("the Project")
    project_text = """
    The application you are looking at serves as the final project for my Tool for Data Analysis course (ECON 8320). The goal of this project is to utilize and demonstrate 
    my knowledge of Python tools that were taught throughout the past semester. Further description for the project details can be found on the "Project Details"(https://econ-8320-final-project-austin-rose.streamlit.app/project_details) page.
    """
    st.write(project_text)

    st.header("What was Learned")
    learn_text = """
    Beyond just exercising what has been learned in both earlier in this course and in prior courses, I have definantly learned a few new tricks in the process of completing this project. 
    To start, I learned a whole new library in Streamlit. This library kind of rules. I makes making simple data dashboard pretty slick. I already have found myself thinking about future projects I could use this library for. 

    I would probably say the second most impactful thing I gained from this project was further exploration of Github. I can see how this could be one of a programmers best friends.
    """
    st.write(learn_text)


def main():
    show()


if __name__ == "__main__":
    main()
