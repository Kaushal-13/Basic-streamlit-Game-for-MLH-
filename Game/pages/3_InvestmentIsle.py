import streamlit as st
import pandas as pd
import random


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


selected_value = 30

st.title("Investment Isle")
st.write(
    f" Repute: {st.session_state.variables['Repute']}, Gold: {st.session_state.variables['Gold']}")
st.write(f"Clicks : {st.session_state.variables['Clicks']}")

df = st.session_state["variables"]["df"]

df = df.sample(1)

l = list(df["Investment Idea"])
l2 = list(df["Value"])
l3 = list(df["Story"])

st.write(l3[0])

if (st.button("Invest in this business")):
    a = float(l2[0])
    b = random.random()
    val = True
    if (b > a):
        val = False

    st.session_state.variables['Gold'] -= selected_value
    return_Value = 0
    if (val):
        return_Value = return_Value/(a)
    st.session_state.variables["Investments"].append(
        {
            "Invested Value": selected_value,
            "Investment Value": return_Value,
            "Clicks": 10
        }
    )
