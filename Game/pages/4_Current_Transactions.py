import streamlit as st
import pandas as pd


import streamlit as st


def Update():
    st.session_state["variables"]["Clicks"] += 1
    Investments = st.session_state["variables"]["Investments"]

    if (st.session_state["variables"]["Clicks"] % 5 == 0):
        st.session_state["variables"]["Gold"] -= st.session_state["variables"]["Repute"]

    for i in range(len(Investments)):
        Investments[i]["Clicks"] -= 1
        if (Investments[i]["Clicks"] == 0):
            value = Investments[i]["Investment Value"]
            st.session_state["variables"]["Gold"] += value
            st.session_state["variables"]["Investments"].pop(i)
            if (value > 0):
                st.session_state["variables"]["Repute"] += 1
            else:
                st.session_state["variables"]["Repute"] -= 1

    loans = st.session_state["variables"]["Loans"]
    for i in range(len(loans)):
        loans[i]["Clicks"] -= 1
        if (loans[i]["Clicks"] == 0):
            value = loans[i]["Loan Value"]
            st.session_state["variables"]["Gold"] -= value
            st.session_state["variables"]["Loans"].pop(i)
            if (st.session_state["variables"]["Gold"] > 0):
                st.session_state["variables"]["Repute"] += 1
            else:
                st.session_state["variables"]["Repute"] -= 1

    if (st.session_state["variables"]["Gold"] <= 0):
        st.session_state["variables"]["Over"] = True


Update()


st.title("Log Book")
st.write(
    f" Repute: {st.session_state.variables['Repute']}, Gold: {st.session_state.variables['Gold']}")
st.write(f"Clicks : {st.session_state.variables['Clicks']}")


st.write("Loans ")
Loans = st.session_state.variables["Loans"]

values = []
clicks = []

for val in Loans:
    values.append(val["Loan Value"])
    clicks.append(val["Clicks"])

dict = {'Loan Values': values, 'Remaining Clicks': clicks}
df = pd.DataFrame(dict)
st.dataframe(df)


st.write("Investments")
v2 = []
c2 = []

Investments = st.session_state.variables["Investments"]
for val in Investments:
    v2.append(val["Invested Value"])
    c2.append(val["Clicks"])

dict2 = {'Loan Values': v2, 'Remaining Clicks': c2}

st.dataframe(pd.DataFrame(dict2))
