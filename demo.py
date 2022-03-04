import streamlit as st
import random
import time
from random import randrange
from datetime import datetime
import pandas as pd

def main():
    st.set_page_config(layout='wide', page_title='xyzylo')
    hide_streamlit_style = \
        """
            <style>
            MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
        """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)

    df_color = pd.read_csv('./color/image05.csv')

    with st.empty():
        while (True):
            now = datetime.now()
            bgcolor = df_color['color'][int(now.second)%len(df_color)]

            home_page = f"""
				<div style="width:5000px;height: 5000px;background:{bgcolor};position:absolute;left:-100px;right:0px;top:-150px;overflow:hidden;' ">
					<br><br><br>
				</div>
			"""
            st.markdown(home_page, unsafe_allow_html=True)


            while(True):
                if(int(datetime.now().second) % 6 == 0):
                    break
                time.sleep(0.1)


if __name__ == '__main__':
    main()

