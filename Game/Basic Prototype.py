import streamlit as st
import pandas as pd


def Update():
    st.session_state["variables"]["Clicks"] += 1
    Investments = st.session_state["variables"]["Investments"]

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


if "variables" not in st.session_state:
    variables = {
        "Gold": 100,
        "Repute": 5,
        "Goods": 100,
        "Loans": [],
        "Investments": [],
        "Clicks": 0,
        "Debt": 0,
        "Over": False,
        "df": pd.read_csv("ideas.csv")
    }
    st.session_state["variables"] = variables

st.write(
    f" Repute: {st.session_state.variables['Repute']}, Gold: {st.session_state.variables['Gold']}")
st.write(f"Clicks : {st.session_state.variables['Clicks']}")


Update()
