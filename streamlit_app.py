import streamlit as st
from constant import *
from streamlit_timeline import timeline
import streamlit.components.v1 as components
import plotly.graph_objects as go
import requests
import re
from graph_builder import *


st.set_page_config(page_title="benji.dev", layout="wide",page_icon="👨🏿‍💻")
st.sidebar.code(info["name"])
st.sidebar.image(image="images\\b.jpg",width=300)
st.sidebar.markdown(embed_component['linkedin'],unsafe_allow_html=True)
st.sidebar.markdown(info["Stackoverflow_flair"],unsafe_allow_html=True)

st.subheader('Summary')
st.write(info['bio'])

st.subheader('My journey(Bachelor & Master in CS)')

with st.spinner(text='Building line'):
    with open('timeline.json', 'r') as f:
        data = f.read()
        timeline(data,height=500)


st.subheader('Skills & Tools ⚒️')
def skill_tab():
    rows,cols = len(info['skills'])//skill_col_size,skill_col_size
    skills = iter(info['skills'])
    if len(info['skills'])%skill_col_size!=0:
        rows+=1
    for x in range(rows):
        columns = st.columns(skill_col_size)
        for index_ in range(skill_col_size):
            try:
                columns[index_].button(next(skills))
            except:
                break
with st.spinner(text="Loading section..."):
    skill_tab()


st.subheader('Education 📖')

fig = go.Figure(data=[go.Table(
    header=dict(values=list(info['edu'].columns),
                # fill_color='white',
                align='left',height=65,font_size=20),
    cells=dict(values=info['edu'].transpose().values.tolist(),
            #    fill_color='lavender',
               align='left',height=40,font_size=15))])

fig.update_layout(width=850, height=400)
st.plotly_chart(fig)

st.subheader('Achievements 🥇')
achievement_list = ''.join(['<li>'+item+'</li>' for item in info['achievements']])
st.markdown('<ul>'+achievement_list+'</ul>',unsafe_allow_html=True)


st.subheader('Medium Writer ✍️')
st.markdown("""<a href={}> Click to see the full Profile</a>""".format(info['Medium']),unsafe_allow_html=True)

try:
        page1,page2 = requests.get(info['Medium']), requests.get(info['publication_url'])

        followers = re.findall('(\d+\.\d+[kK]?) Followers',page1.text)[0]
        pub_followers = re.findall('Followers (?:\w+\s+){4}(\d+)',re.sub('\W+',' ', page2.text ))[0]

        cols = st.columns(2)
        cols[0].metric('Followers',followers)
        cols[1].metric('Publication followers',pub_followers)
except:
    pass

with st.expander('Expand to read my latest blog posts'):
    components.html(embed_component['medium'],height=500)


st.subheader('Daily routine as A Develeoper and Content Writer')
st.graphviz_chart(graph)