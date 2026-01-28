import streamlit as st
import pandas as pd

st.title("Student Management System")

# ---------- Section 1: Add Student ----------
st.header("Add Student")
students=[]
roll = st.text_input("Roll Number")
name = st.text_input("Student Name")
age = st.number_input("Age", min_value=1, step=1)

if st.button("Add Student"):
    st.students.append({
            "Roll No": roll,
            "Name": name,
            "Age": age
        })
    st.success("Student added successfully 🎉")

# ---------- Section 2: Display Table ----------
st.header("Student List")

if st.session_state.students:
    df = pd.DataFrame(st.session_state.students)
    st.table(df)

    # ---------- Section 3: Delete Student ----------
    st.header("Delete Student")

    roll_numbers = [student["Roll No"] for student in st.session_state.students]
    selected_roll = st.selectbox("Select Roll Number to delete", roll_numbers)

    if st.button("Delete"):
        st.session_state.students = [
            student for student in st.session_state.students
            if student["Roll No"] != selected_roll
        ]
        st.success("Student deleted successfully ❌")
else:
    st.info("No students added yet.")
