# Packages//////////////////////////////////////////////////////////////////////////////////////////////
from PIL import Image
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import streamlit as st
# //////////////////////////////////////////////////////////////////////////////////////////////////////

# Streamlit Design Settings/////////////////////////////////////////////////////////////////////////////
st.set_page_config(layout="wide")

def Title(label):
    st.markdown(f'<link href="https://fonts.googleapis.com/css?family=Sigmar One" rel="stylesheet">\
    	<p style="color:#BF1E2D; font-size:30px; text-align:center; font-family:Sigmar One; font-weight:bold">{label}</p>', unsafe_allow_html=True)
    
def InputLabel(label):
    st.markdown(f'<p style="color:#D56828; font-size:15px; font-family:Source Sans Pro; font-weight:bold">{label}</p>', unsafe_allow_html=True)
    
st.markdown("""
    <style>
    p{
	    padding: 0px;
	    font-size: 17px;
	    font-family: 'Source Sans Pro';
	}

    div.stButton > button:first-child {
        box-shadow: 3px 4px 0px 0px #6B2D00;
		background-color: #D56828;
		border-radius: 18px;
		border: 1px solid #D56828;
		display: inline-block;
		cursor: pointer;
		color: #FFFFFF;
		padding: 7px 25px;
		text-decoration: none;
		text-shadow: 0px 1px 0px #6B2D00;
		width: 100%;
    }
    div.stButton > button:hover {
        background-color: #E69F6C;
    }
    div.stButton > button:active {
    	background-color: #FFFFFF;
        position:relative;
		top:3px;
    }
            
    div.stDownloadButton > button:first-child {
        box-shadow: 3px 4px 0px 0px #6B2D00;
		background-color: #D56828;
		border-radius: 18px;
		border: 1px solid #D56828;
		display: inline-block;
		cursor: pointer;
		color: #FFFFFF;
		padding: 7px 25px;
		text-decoration: none;
		text-shadow: 0px 1px 0px #6B2D00;
		width: 100%;
    }
    div.stDownloadButton > button:hover {
        background-color: #E69F6C;
    }
    div.stDownloadButton > button:active {
    	background-color: #FFFFFF;
        position:relative;
		top:3px;
    }
    </style>
""", unsafe_allow_html=True)
# //////////////////////////////////////////////////////////////////////////////////////////////////////

# Changeable Information////////////////////////////////////////////////////////////////////////////////
year = "2025"
# //////////////////////////////////////////////////////////////////////////////////////////////////////

# Results Page//////////////////////////////////////////////////////////////////////////////////////////
col1, col2, col3 = st.columns([5, 2, 5])
with col2:
    st.image(Image.open("ITURO.png"))
     
st.divider()
Title("🏆 ALGOLAB " + year + " SONUÇLARI 🏆")

# Input Competitor Data~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
sample_data = False

# Number of Competitors=================================================================================
if sample_data:
    num_competitors = 6
else:
    InputLabel("Lütfen yarışmacı sayısını giriniz:")
    num_competitors = st.number_input("-", min_value=5, step=1, label_visibility="collapsed")
# ======================================================================================================

# Table Title List======================================================================================
df_title_list = ["Yarışmacı", "P1 - Puan", "P1 - Kod Boyutu",\
                              "P2 - Puan", "P2 - Kod Boyutu",\
                              "P3 - Puan", "P3 - Kod Boyutu",\
                              "P4 - Puan", "P4 - Kod Boyutu",\
                              "P5 - Puan", "P5 - Kod Boyutu"]
# ======================================================================================================

# Table Column Configuration============================================================================
column_config_dict = {"Yarışmacı" : st.column_config.Column(required=True)}
for col_index in range(10):
    if col_index % 2 == 0:
        competitor_index = int(col_index / 2) + 1
        column_config_dict["P" + str(competitor_index) + " - Puan"] = st.column_config.NumberColumn(required=True, min_value=0)
    else:
        competitor_index = int((col_index - 1) / 2) + 1
        column_config_dict["P" + str(competitor_index) + " - Kod Boyutu"] = st.column_config.NumberColumn(required=True, min_value=0)
# ======================================================================================================

# Competitor Data Table=================================================================================
if sample_data:
    competitor_data = np.array([["Emir", 100, 46, 100, 97, 100, 121, 100, 163, 100, 204],
				                ["Emre", 100, 52, 80, 112, 80, 136, 60, 205, 0, 0],
				                ["Batuhan", 100, 67, 100, 115, 80, 125, 80, 198, 80, 226],
				                ["Samed", 100, 75, 80, 134, 80, 162, 80, 216, 80, 271],
				                ["Selin", 100, 53, 100, 96, 100, 122, 100, 151, 80, 183],
				                ["Cansu", 100, 35, 100, 89, 100, 97, 100, 143, 100, 176]])
else:
    InputLabel("Lütfen yarışmacıların her soruya ilişkin bilgilerini giriniz:")
    competitor_data = np.hstack((np.array(["Yarışmacı"] * num_competitors).reshape(num_competitors, 1), np.zeros((num_competitors, 10), dtype=int)))
df_competitor_data = pd.DataFrame(competitor_data, columns=df_title_list)
df_competitor_data.index = map(str, range(1, num_competitors + 1))
df_competitor_data.index.name = "#"
competitor_data = np.array(st.data_editor(df_competitor_data, use_container_width=True, column_config=column_config_dict, disabled=["#"]))
C = competitor_data[:, 0].reshape(-1, 1)
S = competitor_data[:, 1:].astype(float)
# ======================================================================================================
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Final Result List~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if st.button("Sonuçları Göster"):
    # Mapping Code Size=================================================================================
    mapped_min = 100
    mapped_max = 0
    for col_index in [1, 3, 5, 7, 9]:
        code_size_list = S[:, col_index]
        if sum(code_size_list == 0) == num_competitors:
            S[:, col_index] = np.zeros((num_competitors,))
        elif len(set(code_size_list)) == 1:
            S[:, col_index] = mapped_min * np.ones((num_competitors,))
        elif sum(code_size_list > 0) == 1:
            existing_code_index = np.where(code_size_list > 0)[0][0]
            S[:, col_index] = np.zeros((num_competitors,))
            S[existing_code_index, col_index] = mapped_min
        else:
            min_size = min(code_size_list[code_size_list > 0])
            max_size = max(code_size_list[code_size_list > 0])
            for competitor_index in range(num_competitors):
                code_size = S[competitor_index, col_index]
                if code_size > 0:
                    S[competitor_index, col_index] = round(mapped_min + (float(code_size - min_size) / float(max_size - min_size) * (mapped_max - mapped_min)), 2)
    # ==================================================================================================
                            
    # Calculate Total Scores============================================================================
    T = np.zeros((num_competitors, 1), dtype=float)
    for competitor_index in range(num_competitors):
        competitor_scores = S[competitor_index, :]
        T[competitor_index] = round(0.20 * (0.65 * competitor_scores[0] + 0.35 * competitor_scores[1]) +\
                                    0.35 * (0.65 * competitor_scores[2] + 0.35 * competitor_scores[3]) +\
                                    0.45 * (0.65 * competitor_scores[4] + 0.35 * competitor_scores[5]) +\
                                    0 * (0.65 * competitor_scores[6] + 0.35 * competitor_scores[7]) +\
                                    0 * (0.65 * competitor_scores[8] + 0.35 * competitor_scores[9]), 2)
    R = np.hstack((C, T))
    R_sorted = R[(-R[:, 1]).argsort()]
    # ==================================================================================================

    # Show Final Results================================================================================
    color_list = [["#ADE9FF"] * 3 + ["#F5F5F5"] * (num_competitors - 3)]
    order_list = ["🥇","🥈","🥉"] + list(range(4, num_competitors + 1))
    final_table = np.hstack((np.array(order_list).reshape(-1, 1), R_sorted))
    go_fig = go.Figure(data=[go.Table(
        header=dict(values=["<b>#</b>","<b>Competitor</b>","<b>Total Score</b>"],
                    font=dict(color="white", size=20, family="Source Sans Pro"),
                    fill_color="#2C3E50",
                    line_color="#000000",
                    align="center"),
        cells=dict(values=np.transpose(final_table),
                    font=dict(color="black", size=18, family="Source Sans Pro"),
                    fill_color=color_list,
                    line_color="#000000",
                    height=30,
                    align="center")
    )])
    top_margin = 80
    h = min(len(final_table[:, 0]), 20) * 30 + 50 + top_margin
    go_fig.update_layout(height=h, width=1000, margin=dict(r=0, l=0, t=top_margin, b=0))
    st.write(go_fig)
    # ==================================================================================================
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# //////////////////////////////////////////////////////////////////////////////////////////////////////
