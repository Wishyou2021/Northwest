import streamlit as st  
import NORTHWEST 
import NOUTHWEST_map
st.title('NBA數據查詢系統')
st.sidebar.header('選擇球隊及數據')
option = st.sidebar.selectbox( '選擇分組？', ['ATLANTIC', '中央組', 'SOUTHEAST', 'NORTHWEST','太平洋組','西南組'])
if option=='NORTHWEST':
  teams=st.sidebar.selectbox( '選擇球隊？', ['Denver Nuggets', 'Minnesota Timberwolves', 'Oklahoma City Thunder', 'Portland Trail Blazers','Utah Jazz'])
  if teams=='Denver Nuggets':
    NORTHWEST.DenverNuggets()
    NORTHWEST_map.DenverNuggets_map()
  if teams=='Minnesota Timberwolves':
    NORTHWEST.MinnesotaTimberwolves()
    NORTHWEST_map.MinnesotaTimberwolves_map()
  if teams=='Oklahoma City Thunder':
    NORTHWEST.OklahomCityThunder()
    NORTHWEST_map.OklahomCityThunder_map()
  if teams=='Portland Trail Blazers':
    NORTHWEST.PortlandTrailBlazers()
    NORTHWEST_map.PortlandTrailBlazers_map()
  if teams=='Utah Jazz':
    NORTHWEST.UtahJazz()
    NORTHWEST_map.UtahJazz_map()
