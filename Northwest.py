import streamlit as st  
import SOUTHEAST 
st.title('NBA數據查詢系統')
st.sidebar.header('選擇球隊及數據')
option = st.sidebar.selectbox( '選擇分組？', ['ATLANTIC', '中央組', 'SOUTHEAST', 'NORTHWEST','太平洋組','西南組'])
if option=='NORTHWEST':
  teams=st.sidebar.selectbox( '選擇球隊？', ['Atlanta Hawks', 'Charlotte Hornets', 'Miami Heat', 'Orlando Magic','Washington Wizards'])
  if teams=='Atlanta Hawks':
    NORTHWEST.AtlantaHawks()
  if teams=='Charlotte Hornets':
    NORTHWEST.CharlotteHornets()
  if teams=='Miami Heat':
    NORTHWEST.MiamiHeat()
  if teams=='Orlando Magic':
    NORTHWEST.OrlandoMagic()
  if teams=='Washington Wizards':
    NORTHWEST.WashingtonWizards()
