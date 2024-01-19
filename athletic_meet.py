import streamlit as st
import pandas as pd

st.set_page_config(page_title="SNK Athletic Meet 2023-24")

# Load data from csv into DataFrame
merged_df = pd.read_csv("combined.csv")

# Streamlit app
st.title("Athletic Meet 2023-24")
st.header("Student Performance App")

# Dropdown to select student
school_list = sorted(merged_df.School.unique())
select_school = st.selectbox("Select School:", options=school_list)

grade_list = sorted(merged_df[merged_df["School"] == select_school].Std.unique())
select_grade = st.selectbox("Select Grade:", options=grade_list)

section_list = sorted(merged_df[(merged_df["School"] == select_school) & (merged_df["Std"] == select_grade)].Sec.unique())
select_section = st.selectbox("Select Section:", options=section_list)

student_list = sorted(merged_df[(merged_df["School"] == select_school) & (merged_df["Std"] == select_grade) & (merged_df["Sec"] == select_section)].Name.unique())
selected_student = st.selectbox("Select Student:", options=student_list)

selected_student_data = merged_df[merged_df["Name"] == selected_student]
grade = selected_student_data["Std"].values[0]
school = selected_student_data["School"].values[0]
unit = selected_student_data["Unit"].values[0]
gender = selected_student_data["Gender"].values[0]
house = selected_student_data["House"].values[0]

# Display selected student's information and performance
# st.write(f"## {selected_student}'s Information:")
# st.write("#### School:", school)
# st.write("#### Gender:", gender)
# st.write("#### House:", house)
# "---"
st.write(f"## {selected_student}'s Performance:")
# st.write("### 100m Time:", str(selected_student_data["100m"].values[0]), "*ss.ms*")
# st.write("### 200m Time:", selected_student_data["200m(s)"].values[0], "*ss.ms OR mm.ss.ms*")
# st.write("### Ball Throw Distance:", selected_student_data["Ball Throw"].values[0], "*mt*")

if grade == 1 or grade == 2 :
    st.dataframe(selected_student_data, column_config={"School": None, "School_FK": None, "400m": None, "400m(s)": None, "200m(s)": None}, hide_index=True)
elif grade == 3 or grade == 4:
    st.dataframe(selected_student_data, column_config={"School": None, "School_FK": None, "200m": None, "400m(s)": None, "200m(s)": None}, hide_index=True)

st.write("###### 100m Time: *ss.ms*")
if grade == 1 or grade == 2 :
    st.write("###### 200m Time: *ss.ms OR m.ss.ms*")
elif grade == 3 or grade == 4:
    st.write("###### 400m Time: *m.ss.ms*")
st.write("###### Ball Throw: *mt*")

"---"

# Display top 8 students for each event in the respective unit and grade level
st.write("## Top 8 students in each event of your Unit:")

st.write("### 100m Running")
table1 = merged_df[(merged_df["Unit"] == unit) & (merged_df["Std"] == select_grade) & (merged_df["Gender"] == gender)][["Name","Std","Sec","Unit","Gender","House","100m"]].nsmallest(8, '100m', keep='all').dropna(subset=['100m'])
st.dataframe(table1, use_container_width=True ,hide_index=True)

if grade == 1 or grade == 2 :
    st.write("### 200m Running")
    table2 = merged_df[(merged_df["Unit"] == unit) & (merged_df["Std"] == select_grade) & (merged_df["Gender"] == gender)][["Name","Std","Sec","Unit","Gender","House","200m","200m(s)"]].nsmallest(8, '200m(s)', keep='all').dropna(subset=['200m(s)'])
    st.dataframe(table2, column_config={"200m(s)": None} ,use_container_width=True ,hide_index=True)
elif grade == 3 or grade == 4:
    st.write("### 400m Running")
    table3 = merged_df[(merged_df["Unit"] == unit) & (merged_df["Std"] == select_grade) & (merged_df["Gender"] == gender)][["Name","Std","Sec","Unit","Gender","House","400m","400m(s)"]].nsmallest(8, '400m(s)', keep='all').dropna(subset=['400m(s)'])
    st.dataframe(table3, column_config={"400m(s)": None} ,use_container_width=True ,hide_index=True)

st.write("### Ball Throw")
table4 = merged_df[(merged_df["Unit"] == unit) & (merged_df["Std"] == select_grade) & (merged_df["Gender"] == gender)][["Name","Std","Sec","Unit","Gender","House","Ball Throw"]].nlargest(8, 'Ball Throw', keep="all").dropna(subset=['Ball Throw'])
st.dataframe(table4, use_container_width=True ,hide_index=True)