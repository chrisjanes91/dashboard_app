import streamlit as st
import pandas as pd
from datetime import datetime

df = pd.read_csv('dashboard_stats.csv')
# Extra preprocessing to make the app work and look nicer
df['season'] = df['season'].astype('str')
df['season'] = df['season'].replace({'2019': '2018-19', '2020': '2019-20', '2021': '2020-21', '2022': '2021-22', '2023': '2022-23'})
df['date'] = pd.to_datetime(df['date'])

st.title('Historic Game Data')
st.write('Historic game data from the 2018-19 season through the 2022-23 season. For each game, team averages from up to the past 15 games are shown \
for each team, which served as the inputs for the machine learning models. The pre-match betting odds, prediction probabilities, and actual \
result are also shown. A prediction probability of greater than 0.5 means the home team is favoured to win.')

unique_seasons = df['season'].unique()
selected_season = st.selectbox('Select a season', unique_seasons)
filtered_data = df[df['season'] == selected_season]

filtered_data = filtered_data.copy()
filtered_data['month'] = filtered_data['date'].dt.strftime('%B %Y')  
unique_months = filtered_data['month'].unique()
selected_month = st.selectbox('Select a month', unique_months)
refiltered_data = filtered_data[filtered_data['month'] == selected_month]

refiltered_data = refiltered_data.copy()
refiltered_data['day'] = refiltered_data['date'].dt.strftime('%B %d')
unique_days = refiltered_data['day'].unique()
selected_day = st.selectbox('Select a day', unique_days)
rerefiltered_data = refiltered_data[refiltered_data['day'] == selected_day]


for index, row in rerefiltered_data.iterrows():
    if st.button(row['matchup']):
        data = row.copy()
        row_values = data[['days_between_games_home','avg_min_home', 'avg_fgm_home', 'avg_fga_home', 'avg_3pm_home', 'avg_3pa_home', 'avg_ftm_home', 'avg_fta_home',
                            'avg_oreb_home', 'avg_dreb_home', 'avg_treb_home', 'avg_ast_home', 'avg_stl_home', 'avg_blk_home', 'avg_tov_home', 'avg_pf_home', 'avg_pts_home',
                            'avg_plus_minus_home', 'avg_3pm_diff_home', 'avg_ftm_diff_home', 'avg_reb_diff_home', 'avg_win_home', 'avg_fg_pct_home', 'avg_3p_pct_home',
                            'avg_ft_pct_home', 'avg_true_pct_home',
                            'days_between_games_away','avg_min_away', 'avg_fgm_away', 'avg_fga_away', 'avg_3pm_away', 'avg_3pa_away', 'avg_ftm_away', 'avg_fta_away',
                            'avg_oreb_away', 'avg_dreb_away', 'avg_treb_away', 'avg_ast_away', 'avg_stl_away', 'avg_blk_away', 'avg_tov_away', 'avg_pf_away', 'avg_pts_away',
                            'avg_plus_minus_away', 'avg_3pm_diff_away', 'avg_ftm_diff_away', 'avg_reb_diff_away', 'avg_win_away', 'avg_fg_pct_away', 'avg_3p_pct_away',
                            'avg_ft_pct_away', 'avg_true_pct_away'
                            ]].tolist()
        mid_index = len(row_values) // 2
        first_half = row_values[:mid_index]
        second_half = row_values[mid_index:]
        table_df = pd.DataFrame([first_half, second_half])
        table_df.insert(0, 'Team', ['Home', 'Away'])
        table_df.columns = ['Team', 'Rest Days', 'MIN', 'FGM', 'FGA', '3PM', '3PA', 'FTM', 'FTA', 'OREB', 'DREB', 'TREB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS',
                            'Plus-Minus', '3PT Diff.', 'FTM Diff.', 'REB Diff.', 'Win%', 'FG%', '3P%', 'FT%', 'TS%']
        
        one_dp_cols = ['MIN', 'FGM', 'FGA', '3PM', '3PA', 'FTM', 'FTA', 'OREB', 'DREB', 'TREB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS', 'Plus-Minus', '3PT Diff.',
                        'FTM Diff.', 'REB Diff.']
        two_dp_cols = ['Win%', 'FG%', '3P%', 'FT%', 'TS%']
        table_df[one_dp_cols] = table_df[one_dp_cols].round(1)
        table_df[two_dp_cols] = table_df[two_dp_cols].round(2)
        st.write('### Team Averages (past 15 games)')
        st.dataframe(table_df, hide_index=True)
        
        odds = row[['decimal_home', 'decimal_away', 'predictions_lr', 'predictions_svm', 'predictions_rf']].tolist()
        st.write('### Betting Odds and Model Predictions')
        col1, col2 = st.columns(2)
        col1.write('Home odds: ' + str(odds[0]))
        col1.write('Away odds: ' + str(odds[1]))
        col2.write('Logistic Regression predicts: ' + str(round(odds[2], 2)))
        col2.write('Support Vector Machine predicts: ' + str(round(odds[3], 2)))
        col2.write('Random Forest predicts: ' + str(round(odds[4], 2)))

        result = row[['pts_home', 'pts_away']].tolist()
        st.write('### Result')
        st.write(f'{data['matchup'][0:3]} : {int(result[0])}')
        st.write(f'{data['matchup'][-3:]} : {int(result[1])}')


    






