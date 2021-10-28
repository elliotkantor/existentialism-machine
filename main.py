import datetime
import streamlit as st
import time

"# Existentialism Machine"
'### "It updates every second!"'

birthday = st.date_input(
    "Enter your birthday",
    min_value=datetime.datetime(1900, 1, 1),
    max_value=datetime.datetime.now(),
    value=datetime.datetime(2000, 1, 1),
)
birthday = datetime.datetime(birthday.year, birthday.month, birthday.day)
lifespan_years = st.number_input(
    "Enter expected lifespan",
    min_value=60,
    max_value=110,
    value=80,
)
lifespan = datetime.timedelta(days=365.25 * lifespan_years)
a = st.empty()

run = st.radio(label="Running", options=["Off", "On"])
while run == "On":
    today = datetime.datetime.now()
    percent_complete = ((today - birthday) / lifespan) * 100
    a.write(f"# {percent_complete:.8f}% done with your time on Earth!")
    time.sleep(1)
