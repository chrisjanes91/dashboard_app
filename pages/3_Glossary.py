import streamlit as st

st.title('Glossary of Terms')

st.markdown("""
- **MIN**: Total minutes played by team.
- **FGM**: Total field goals made by team.
- **FGA**: Total field goals attempted by team.
- **3PM**: Total 3-pointers made by team.
- **3PA**: Total 3-pointers attempted by team.
- **FTM**: Total freee throws made by team.
- **FTA**: Total free throws attempted by team.
- **OREB**: Total offensive rebounds by team.
- **DREB**: Total defensive rebounds by team.
- **TREB**: Total rebounds by team.
- **AST**: Total assists by team.
- **STL**: Total steals by team.
- **BLK**: Total blocks by team.
- **TOV**: Total turnovers by team.
- **PF**: Total personal fouls by team.
- **PTS**: Total points by team.
- **Plus-Minus**: Total plus-minus by team. PLus-minus estimates the number of points per 100 possessions that a player contributed above a league-average player.
- **3PT Diff.**: Difference in total 3-pointers made by each team.
- **FTM Diff.**: Difference in total free throws made by each team..
- **REB Diff.**: Difference in total rebounds by each team..
- **Win%**: Percentage of games won.
- **FG%**: Percentage of field goals made.
- **3P%**: Percentage of 3-pointers made.
- **FT%**: Percentage of free throws made.
- **TS%**: Shooting metric to capture the different values of 3-point shots, 2-point shots, and free thows. \
Given by: PTS / (2 $\\times$ (FGA + (0.44 $\\times$ FTA)))
""")