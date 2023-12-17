import streamlit as st
from random import sample


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


st.title("Loan Land")
st.write(
    f" Repute: {st.session_state.variables['Repute']}, Gold: {st.session_state.variables['Gold']}")


st.write(f"Clicks : {st.session_state.variables['Clicks']}")
repute = st.session_state.variables['Repute']

interest_rate = int(40/(repute + 1))
gold = st.session_state.variables['Gold']
max_value = gold + gold*(repute/100)
max_value = int(max_value)
l = []

with open('loan_texts.txt', 'r') as file:
    lines = file.readlines()  # Read all lines into a list
    for line in lines:
        l.append(str(line))

display = sample(l, 1)
st.write(display[0])

selected_value = st.slider(
    "Select a value", min_value=0, max_value=max_value, value=50, step=1)

st.write(f"Selected value: {selected_value}")
Loan_Value = selected_value + int(selected_value*(interest_rate/100))
st.write(
    f"You shall have to pay a value of : {Loan_Value} within 30 clicks")

if (st.button("Take Loan")):

    st.session_state.variables['Gold'] += selected_value
    st.session_state.variables["Loans"].append({
        "Loan Value": Loan_Value,
        "Clicks": 30
    })
    st.session_state.variables["Debt"] += Loan_Value

Update()
