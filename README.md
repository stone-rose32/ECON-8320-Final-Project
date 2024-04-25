# ECON-8320-Final-Project
This project is designed to give you a chance to combine all of the material that we cover during the term, and to show that you can use these tools to collect and clean data, as well as to conduct some rudimentary analysis (other courses will focus much more on the analysis part).

You will create a StreamlitLinks to an external site. dashboard highlighting demographic changes in the US from 2010 to 2023 (all years that are available using the API below).

In this project, you will collect data with the US Census Bureau API from the Current Population Survey (CPS)Links to an external site..
You should collect information about the demographic makeup of cities across the US over time in order to help understand the demographic changes occurring in the US during this period.
Your final data should contain information at the year-month-city level, describing the proportion in the overall population of at least 7 demographic variables of your choosing.
Once you have processed the data, you will build an interactive dashboard using Streamlit, and launch a website from your GitHub using the free deployment process described on the Streamlit website (with the Community Cloud tool).
Your tool should NOT re-collect the data each time it is loaded, but should instead run a collection script once per month through GitHub Actions that will collect and append the most recent month to your dataset, which will be hosted in your repository.
