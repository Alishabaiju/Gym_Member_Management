import streamlit as st
from memberView import GymMemberManager

member_instance = GymMemberManager()

tab1,tab2=st.tabs(["Add Member","View Member"])
with tab1:
    st.title("Add New Member")
    name = st.text_input("Enter member name")
    place = st.text_input("Enter the place")
    plan = st.selectbox("Select the plan details",["1 month","2 months","3 months","6 months","1 year"])
    mobile = st.text_input("Enter the phone number")
    fee = st.text_input("Enter the fees")
    joining_date = st.date_input("Enter the joining date")
    if st.button("Submit"):
        member_instance.post(name=name,place=place,plan=plan,mobile=mobile,fee=fee,joining_date=joining_date)
        st.success("Member added successfully..")

with tab2:
    st.title("View members details")
    record = member_instance.get()
    print(record)
    if record:
        st.table(record)

        