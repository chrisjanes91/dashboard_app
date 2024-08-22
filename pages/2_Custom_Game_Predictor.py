import streamlit as st
import numpy as np
import joblib

st.title("Custom Game Predictor")
st.write('Enter a custom set of pre-match averages and view the effect of different scenarios on model predictions. \
Please avoid inputting figures which would be impossible, such as more field goals made than attempted, as this may \
confuse the model\'s interpretation of the figures. The probabilities given are the predicted chances of a home victory.')

scaler = joblib.load('scaler.pkl')
rf_model = joblib.load('rf_model.pkl')
svm_model = joblib.load('svm_model.pkl')
lr_model = joblib.load('lr_model.pkl')

col1, col2, col3 = st.columns(3)

# These columns should accept decimals in tenths

days_between_games_home = col1.number_input("Home Rest Days", min_value=0, value=3, max_value=15)
avg_min_home = col1.number_input("Home Minutes Played", min_value=240, value=240, max_value=490, step=25)
avg_fgm_home = col1.number_input("Home Field Goals Made", min_value=0.0, value=40.0, max_value=250.0, step=0.1)
avg_fga_home = col1.number_input("Home Field Goals Attempted", min_value=0.0, value=80.0, max_value=250.0, step=0.1)
avg_3pm_home = col1.number_input("Home 3-Pointers Made", min_value=0.0, value=15.0, max_value=100.0, step=0.1)
avg_3pa_home = col1.number_input("Home 3-Pointers Attempted", min_value=0.0, value=30.0, max_value=100.0, step=0.1)
avg_ftm_home = col1.number_input("Home Free Throws Made", min_value=0.0, value=18.0, max_value=100.0, step=0.1)
avg_fta_home = col1.number_input("Home Free Throws Attempted", min_value=0.0, value=20.0, max_value=100.0, step=0.1)
avg_oreb_home = col1.number_input("Home Offensive Rebounds", min_value=0.0, value=10.0, max_value=100.0, step=0.1)
avg_dreb_home = col1.number_input("Home Defensive Rebounds", min_value=0.0, value=25.0, max_value=200.0, step=0.1)
avg_treb_home = avg_oreb_home + avg_dreb_home 
avg_ast_home = col1.number_input("Home Assists", min_value=0.0, value=20.0, max_value=100.0, step=0.1)
avg_stl_home = col1.number_input("Home Steals", min_value=0.0, value=10.0, max_value=50.0, step=0.1)
avg_blk_home = col1.number_input("Home Blocks", min_value=0.0, value=10.0, max_value=50.0, step=0.1)
avg_tov_home = col1.number_input("Home Turnovers", min_value=0.0, value=15.0, max_value=100.0, step=0.1)
avg_pf_home = col1.number_input("Home Personal Fouls", min_value=0.0, value=15.0, max_value=62.0, step=0.1)
avg_pts_home = col1.number_input("Home Points", min_value=0.0, value=100.0, max_value=300.0, step=0.1)
avg_plus_minus_home = col1.number_input("Home Plus-Minus", min_value=-250.0, value=10.0, max_value=250.0, step=0.1)
avg_3pm_diff_home = col1.number_input("Home 3-Pointers Differential", min_value=-50.0, value=3.0, max_value=50.0, step=0.1)
avg_ftm_diff_home = col1.number_input("Home Free Throw Differential", min_value=-50.0, value=8.0, max_value=50.0, step=0.1)
avg_reb_diff_home = col1.number_input("Home Rebound Differential", min_value=-50.0, value=5.0, max_value=50.0, step=0.1)
avg_win_home = col1.number_input("Home Win Percentage", min_value=0.0, value=0.5, max_value=1.0, step=0.01)
avg_fg_pct_home = avg_fgm_home / avg_fga_home
avg_3p_pct_home = avg_3pm_home / avg_3pa_home
avg_ft_pct_home = avg_ftm_home / avg_fta_home
avg_true_pct_home = avg_pts_home / (2 * (avg_fga_home + (0.44 * avg_fta_home)))

days_between_games_away = col2.number_input("Away Rest Days", min_value=0, value=3, max_value=10)
avg_min_away = col2.number_input("Away Minutes Played", min_value=240, value=240, max_value=490, step=25)
avg_fgm_away = col2.number_input("Away Field Goals Made", min_value=0.0, value=40.0, max_value=250.0, step=0.1)
avg_fga_away = col2.number_input("Away Field Goals Attempted", min_value=0.0, value=80.0, max_value=250.0, step=0.1)
avg_3pm_away = col2.number_input("Away 3-Pointers Made", min_value=0.0, value=15.0, max_value=100.0, step=0.1)
avg_3pa_away = col2.number_input("Away 3-Pointers Attempted", min_value=0.0, value=30.0, max_value=100.0, step=0.1)
avg_ftm_away = col2.number_input("Away Free Throws Made", min_value=0.0, value=18.0, max_value=100.0, step=0.1)
avg_fta_away = col2.number_input("Away Free Throws Attempted", min_value=0.0, value=20.0, max_value=100.0, step=0.1)
avg_oreb_away = col2.number_input("Away Offensive Rebounds", min_value=0.0, value=10.0, max_value=100.0, step=0.1)
avg_dreb_away = col2.number_input("Away Defensive Rebounds", min_value=0.0, value=25.0, max_value=200.0, step=0.1)
avg_treb_away = avg_oreb_away + avg_dreb_away 
avg_ast_away = col2.number_input("Away Assists", min_value=0.0, value=20.0, max_value=100.0, step=0.1)
avg_stl_away = col2.number_input("Away Steals", min_value=0.0, value=10.0, max_value=50.0, step=0.1)
avg_blk_away = col2.number_input("Away Blocks", min_value=0.0, value=10.0, max_value=50.0, step=0.1)
avg_tov_away = col2.number_input("Away Turnovers", min_value=0.0, value=15.0, max_value=100.0, step=0.1)
avg_pf_away = col2.number_input("Away Personal Fouls", min_value=0.0, value=15.0, max_value=62.0, step=0.1)
avg_pts_away = col2.number_input("Away Points", min_value=0.0, value=100.0, max_value=300.0, step=0.1)
avg_plus_minus_away = col2.number_input("Away Plus-Minus", min_value=-250.0, value=10.0, max_value=250.0, step=0.1)
avg_3pm_diff_away = col2.number_input("Away 3-Pointers Differential", min_value=-50.0, value=3.0, max_value=50.0, step=0.1)
avg_ftm_diff_away = col2.number_input("Away Free Throw Differential", min_value=-50.0, value=8.0, max_value=50.0, step=0.1)
avg_reb_diff_away = col2.number_input("Away Rebound Differential", min_value=-50.0, value=5.0, max_value=50.0, step=0.1)
avg_win_away = col2.number_input("Away Win Percentage", min_value=0.0, value=0.5, max_value=1.0, step=0.01)
avg_fg_pct_away = avg_fgm_away / avg_fga_away
avg_3p_pct_away = avg_3pm_away / avg_3pa_away
avg_ft_pct_away = avg_ftm_away / avg_fta_away
avg_true_pct_away = avg_pts_away / (2 * (avg_fga_away + (0.44 * avg_fta_away)))

input_data = np.array([[days_between_games_home,avg_min_home,avg_fgm_home,avg_fga_home,avg_3pm_home,
                        avg_3pa_home,avg_ftm_home,avg_fta_home,avg_oreb_home,avg_dreb_home,avg_treb_home,
                        avg_ast_home,avg_stl_home,avg_blk_home,avg_tov_home,avg_pf_home,avg_pts_home,
                        avg_plus_minus_home,avg_3pm_diff_home,avg_ftm_diff_home,avg_reb_diff_home,avg_win_home,
                        avg_fg_pct_home,avg_3p_pct_home,avg_ft_pct_home,avg_true_pct_home,
                        days_between_games_away,avg_min_away,avg_fgm_away,avg_fga_away,avg_3pm_away,avg_3pa_away,
                        avg_ftm_away,avg_fta_away,avg_oreb_away,avg_dreb_away,avg_treb_away,avg_ast_away,
                        avg_stl_away,avg_blk_away,avg_tov_away,avg_pf_away,avg_pts_away,avg_plus_minus_away,
                        avg_3pm_diff_away,avg_ftm_diff_away,avg_reb_diff_away,avg_win_away,avg_fg_pct_away,
                        avg_3p_pct_away,avg_ft_pct_away,avg_true_pct_away]])

input_data_scaled = scaler.transform(input_data)

rf_probs = rf_model.predict_proba(input_data_scaled)[0][1]
svm_probs = svm_model.predict_proba(input_data_scaled)[0][1]
lr_probs = lr_model.predict_proba(input_data_scaled)[0][1]

col3.write(f'Logistic Regression Predicts: {round(lr_probs, 2)}')
col3.write(f'SVM Predicts: {round(svm_probs, 2)}')
col3.write(f'Random Forest Predicts: {round(rf_probs, 2)}')
