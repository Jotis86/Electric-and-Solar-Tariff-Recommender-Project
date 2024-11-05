# ⚡🔋 Electric and Solar Tariff Recommender 🔋⚡

![An electric bulb and several piles of coins](streamlit_app/image.jpg "You can save money choosing the best tariff")

➡️ Try it here : [Electric and Solar Tariff Recommender](https://electric-tariff-recommender.streamlit.app/) ⬅️

## 📋 Objective
The goal of this project is to provide personalized recommendations for solar panel installations in homes, helping users to save on their electricity bills and contribute to a more sustainable world. 🌍✨

## 🛠️ Functionality
This application allows users to input their electricity consumption data and receive recommendations on the number of solar panels they should install. It also compares different solar tariffs to find the most economical option. 💡🔋

## 🧰 Tools Used
- **Python** 🐍
- **Streamlit** 📊
- **Pandas** 🐼
- **BeautifulSoup** 🌐
- **Selenium** 🕵️‍♂️
- **Matplotlib** 📈

## 🛠️ Development Process
1. **Topic Selection**: We started by looking for an interesting topic and formulating some hypotheses related to solar energy and electricity consumption.
2. **Data Source Investigation**: We investigated various data sources available for our chosen topic, focusing on electricity consumption and solar tariffs.
3. **Project Management**: We created a Kanban board using Trello for project management purposes, allowing us to track our progress and collaborate effectively.
4. **GitHub Repository Setup**: We set up a GitHub repository and practiced working collaboratively on the repository.
5. **Data Collection**:
    - We performed web scraping from the websites of several electric companies using BeautifulSoup and Selenium.
    - We inspected the website’s structure and wrote scripts to scrape the required data, resulting in 9 datasets from 4 companies.
6. **Data Wrangling**:
    - We examined the data and understood every field before proceeding with data cleaning and manipulation.
    - We developed a plan for cleaning and transforming the data.
    - We created a dataset for each company and cleaned the data to make it suitable for analysis.
7. **Exploratory Data Analysis (EDA)**:
    - We performed basic EDA to gain insights and validate or disprove our initial hypotheses.
    - We used visualizations to better understand the data and identify patterns.
8. **Model Development**:
    - We developed a model to recommend the number of solar panels based on user input.
    - We implemented a comparison tool to find the most economical solar tariff.
9. **User Interface**:
    - We built an interactive user interface using Streamlit, allowing users to input their data and receive recommendations.
10. **Finalization**:
    - We finalized all cleaning, transformation, and analysis tasks.
    - We refined our code according to best practices.
    - We prepared a visually appealing presentation to effectively communicate our insights and conclusions.

## 📊 Results
The application provides users with:
- The recommended number of solar panels to install.
- A comparison of different solar tariffs.
- The estimated savings from installing solar panels.

## 📈 Summary Report
The summary report includes:
- A comparison of solar tariffs.
- Visualizations to support the analysis and conclusions.

## 🗂️ Trello Board
We used Trello for project management, allowing us to track our progress and collaborate effectively. Our Trello board included tasks for data collection, data wrangling, model development, and user interface design.
![Trello](/images/Trello.png "Trello Board for project management")


## 🗂️ Project Structure
  - **app_logic/**
  - **data/**
  - **data_cleaning/**
  - **data_extraction/**
  - **data_visualization/**
  - **images/**
  - **project_presentation/**
  - **streamlit_app/**
  - **summary_report/**
  - .gitignore
  - recomendador_tarifas.pdf
  - requirements.txt
  - README.md

## 🌐 Streamlit App
The Streamlit app has the following structure:
- **Introduction**: Overview of the project and its objectives.
- **Objectives**: Detailed objectives of the project.
- **Methodology**: Explanation of the methodology used in the project.
- **Visualizations**: Visual representations of the data and analysis.
- **Electric Tariff Recommender**: Tool to recommend the best electric tariffs.
- **Solar Panel Tariff Recommender**: Tool to recommend the best solar panel tariffs.

![Aplication menu](/images/menu.jpg "Side menu of the app") ![Graphic](/images/visualizacion.jpg "Visualization of the data") ![Tariffs](/images/tarifas.jpg "Users write their data to obtain a recomendation")


## 🎥 Project Presentation
A pdf presentation of the project is available [here](https://github.com/datasilvia/data-wrangling-project/blob/main/recomendador_tarifas.pdf).
The online version of the presentation is also available [here](https://www.canva.com/design/DAGVK1T4r0Q/1RBA97MLAYG6vvedLw5uRA/edit).

##  📊 Data Sources

- **Naturgy**: [Naturgy](https://www.naturgy.es/hogar)
- **Octopus**: [Octopus](https://octopusenergy.es/precios)
- **Repsol**: [Repsol](https://www.repsol.es/particulares/)
- **Xenera**: [Xenera](https://xenera.com/)
- **Horas de sol por provincia**: [Horas de sol por provincia](https://greenlifesolutions.es/blog/horas-de-sol-anuales-por-comunidad-autonoma/)
- **Salida y puesta del sol**: [salida y puesta del sol](https://astronomia.ign.es/hora-salidas-y-puestas-de-sol)

## 👥 Project Members

| Name           | Role                | Special Characteristic       | GitHub Profile                          |
|----------------|---------------------|------------------------------|-----------------------------------------|
| Silvia Alonso  | Data Analyst        | Expert in data wrangling     | [Silvia Alonso](https://github.com/datasilvia) |
| Juan Duran     | Data Analyst        | Skilled in web scraping      | [Juan Duran](https://github.com/Jotis86)       |
| Ana Pineda     | Data Analyst        | Spanish Excel Champion       | [Ana Pineda](https://github.com/asdianita)       |


## 🤝 Collaborations and Suggestions
We welcome collaborations and suggestions! Feel free to open an issue or submit a pull request. 

![A Vaquiña](/images/cow.png "This friendly cow is from Xenera, one of the companies we studied, from Galicia, the land of Juan, our master data scrapper and app deployer.")
![Octocat](/images/octocat.jpg "Octocat likes to save money and help the environment with the best electricity rate and solar panels")