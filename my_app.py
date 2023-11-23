
import streamlit as st
import pandas as pd
import numpy as np

def main():
    st.write("""# Simple streamlit app""")
    ser1 = pd.Series(list('abcedfghijklmnopqrstuvwxyz'))
    ser2 = pd.Series(np.arange(26))
    df = pd.DataFrame({"alpha":ser1, "num":ser2}).reset_index()
    st.dataframe(df)
    st.write("""### Line Chart on Alpha Column """)
    st.line_chart(df.alpha)
    st.write("""### Line Chart on Num Column """)
    st.line_chart(df.num)

if __name__ == '__main__':
    main()
