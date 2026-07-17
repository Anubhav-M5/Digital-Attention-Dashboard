# 📊 Personal Digital Attention Economy Dashboard

This project is an **end-to-end data analytics application** built to help me understand my online habits. It takes messy, unorganized platform history logs and turns them into **clean charts** and **clear metrics**.

---

### 🎯 Why I Built This & The Core Goal
The internet is designed to capture our attention and keep us scrolling. I wanted to **audit my own habits** to see if I actually use platforms productively or if I just get pulled into entertainment loops. 

To prove this mathematically, I calculated a **Pearson Correlation Coefficient** comparing what I intentionally typed into the search bar versus what I actually ended up watching. My score came out to **0.41**, showing a **solid, moderate connection**—meaning my learning goals do drive my choices, even if algorithmic recommendations win sometimes.

---

### 🛠️ Tools Used
* **Code & App Development:** Python, VS Code, and Jupyter Notebooks
* **Data Processing:** Pandas and NumPy
* **Visuals & Charts:** Plotly Express
* **Web Dashboard UI:** Streamlit 

---

### 🔒 Privacy Notice: Why Some Files Are Missing
> ⚠️ **A quick note on data privacy:** Because this project uses my actual personal history, I have intentionally blocked the raw data folder (`history/`) and the individual user logs (`.csv` files) from being publicly visible on GitHub using a `.gitignore` file. 

The code itself is completely modular and ready to use. If you want to test this dashboard out for yourself, you can easily plug in your own data by following the steps below.

---

### 🚀 How to Run this Project Locally

#### 1. Setup Your Folder
Make sure your local directory contains these core files:
```text
├── app.py                             # The interactive web dashboard app
├── data_cleaning_and_exploration.ipynb   # The script that processes data
└── requirements.txt                   # List of needed Python packages
2. Add Your Personal Data
Request and download your account logs in JSON format via Google Takeout.

Create a folder named history/ in your project and drop your watch-history.json and search-history.json files right inside it.

3. Run the Processing Script
Open and run all cells in data_cleaning_and_exploration.ipynb. This will filter out background noise, organize your text into clean categories, and automatically generate the needed cleaned_youtube_watches.csv and cleaned_youtube_searches.csv summary tables.

4. Spin Up Your Dashboard
Open your computer terminal in this project folder, install the requirements, and run the Streamlit application command:

Bash
pip install -r requirements.txt
streamlit run app.py
📈 Major Highlights of the Code
Noise Removal: Built a system to filter out tracking junk, community posts, dead links, and ad impressions so only actual content remains.

Smart Content Categorization: Programmed a text matching engine to scan keywords and automatically sort individual titles into custom groups like Data Science, Education, or Entertainment.

Intent-to-Action Vector: Calculated a timeline showing the time of day my productivity drops or spikes.
