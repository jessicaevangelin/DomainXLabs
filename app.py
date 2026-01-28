import streamlit as st
import pandas as pd
st.title("Student Management System")
st.write("Add, view, and delete student details")
if "students" not in st.session_state:
    st.session_state.students = []

# ---------- Section 1: Add Student ----------
st.subheader("Section 1: Add Student")
roll = st.text_input("Enter Roll Number")
name = st.text_input("Enter Student Name")
age = st.number_input("Enter Age", min_value=1)
if st.button("Add Student"):
    if roll and name:
        st.session_state.students.append({
            "Roll No": roll,
            "Name": name,
            "Age": age
        })
        st.success("Student added successfully")
    else:
        st.warning("Please fill all details")
# ---------- Section 2: Student Table ----------
st.subheader("Section 2: Student Details")
if st.session_state.students:
    df = pd.DataFrame(st.session_state.students)
    st.table(df)
    # ---------- Section 3: Delete Student ----------
    st.subheader("Section 3: Delete Student")
    roll_numbers = [student["Roll No"] for student in st.session_state.students]
    selected_roll = st.selectbox("Select Roll Number to delete", roll_numbers)
    if st.button("Delete Student"):
        st.session_state.students = [
            student for student in st.session_state.students
            if student["Roll No"] != selected_roll
        ]
        st.success("Student deleted successfully")
else:
    st.info("No students added yet")
