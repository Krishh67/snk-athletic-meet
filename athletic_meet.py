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
elif grade == 5 or grade == 6 or grade == 7 or grade == 8 or grade == 9 or grade == 10 or grade == 11 or grade == 12:
    st.dataframe(selected_student_data, column_config={"School": None, "School_FK": None, "400m": None, "400m(s)": None, "200m(s)": None, "600m(s)": None, "Ball Throw": None}, hide_index=True)


st.write("###### 100m Time: *ss.ms*")
if grade == 1 or grade == 2 :
    st.write("###### 200m Time: *ss.ms OR m.ss.ms*")
    st.write("###### Ball Throw: *mt*")
elif grade == 3 or grade == 4:
    st.write("###### 400m Time: *m.ss.ms*")
    st.write("###### Ball Throw: *mt*")
elif grade == 5 or grade == 6 or grade == 7 or grade == 8 or grade == 9 or grade == 10 or grade == 11 or grade == 12:
    st.write("###### 200m Time: *ss.ms OR m.ss.ms*")
    st.write("###### 600m Time: *m.ss.ms*")
    st.write("###### Shot Put: *mt*")
    st.write("###### Long Jump: *mt*")


"---"

# Display top 8 students for each event in the respective unit and grade level
st.write("## Top 8 students in each event from your Unit:")

st.write("### 100m Running")
table1 = merged_df[(merged_df["Unit"] == unit) & (merged_df["Std"] == select_grade) & (merged_df["Gender"] == gender)][["Name","Std","Sec","Unit","Gender","House","100m"]].nsmallest(8, '100m', keep='all').dropna(subset=['100m'])
st.dataframe(table1, use_container_width=True ,hide_index=True)

if grade == 1 or grade == 2 :
    st.write("### 200m Running")
    table21 = merged_df[(merged_df["Unit"] == unit) & (merged_df["Std"] == select_grade) & (merged_df["Gender"] == gender)][["Name","Std","Sec","Unit","Gender","House","200m","200m(s)"]].nsmallest(8, '200m(s)', keep='all').dropna(subset=['200m(s)'])
    st.dataframe(table21, column_config={"200m(s)": None} ,use_container_width=True ,hide_index=True)
    st.write("### Ball Throw")
    table41 = merged_df[(merged_df["Unit"] == unit) & (merged_df["Std"] == select_grade) & (merged_df["Gender"] == gender)][["Name","Std","Sec","Unit","Gender","House","Ball Throw"]].nlargest(8, 'Ball Throw', keep="all").dropna(subset=['Ball Throw'])
    st.dataframe(table41, use_container_width=True ,hide_index=True)
elif grade == 3 or grade == 4:
    st.write("### 400m Running")
    table3 = merged_df[(merged_df["Unit"] == unit) & (merged_df["Std"] == select_grade) & (merged_df["Gender"] == gender)][["Name","Std","Sec","Unit","Gender","House","400m","400m(s)"]].nsmallest(8, '400m(s)', keep='all').dropna(subset=['400m(s)'])
    st.dataframe(table3, column_config={"400m(s)": None} ,use_container_width=True ,hide_index=True)
    st.write("### Ball Throw")
    table42 = merged_df[(merged_df["Unit"] == unit) & (merged_df["Std"] == select_grade) & (merged_df["Gender"] == gender)][["Name","Std","Sec","Unit","Gender","House","Ball Throw"]].nlargest(8, 'Ball Throw', keep="all").dropna(subset=['Ball Throw'])
    st.dataframe(table42, use_container_width=True ,hide_index=True)
elif grade == 5 or grade == 6 or grade == 7 or grade == 8 or grade == 9 or grade == 10 or grade == 11 or grade == 12:
    st.write("### 200m Running")
    table22 = merged_df[(merged_df["Unit"] == unit) & (merged_df["Std"] == select_grade) & (merged_df["Gender"] == gender)][["Name","Std","Sec","Unit","Gender","House","200m","200m(s)"]].nsmallest(8, '200m(s)', keep='all').dropna(subset=['200m(s)'])
    st.dataframe(table22, column_config={"200m(s)": None} ,use_container_width=True ,hide_index=True)    
    st.write("### 600m Running")
    table5 = merged_df[(merged_df["Unit"] == unit) & (merged_df["Std"] == select_grade) & (merged_df["Gender"] == gender)][["Name","Std","Sec","Unit","Gender","House","600m","600m(s)"]].nsmallest(8, '600m(s)', keep='all').dropna(subset=['600m(s)'])
    st.dataframe(table5, column_config={"400m(s)": None} ,use_container_width=True ,hide_index=True)
    st.write("### Shot Put")
    table6 = merged_df[(merged_df["Unit"] == unit) & (merged_df["Std"] == select_grade) & (merged_df["Gender"] == gender)][["Name","Std","Sec","Unit","Gender","House","Shot Put"]].nlargest(8, 'Shot Put', keep="all").dropna(subset=['Shot Put'])
    st.dataframe(table6, use_container_width=True ,hide_index=True)
    st.write("### Long Jump")
    table7 = merged_df[(merged_df["Unit"] == unit) & (merged_df["Std"] == select_grade) & (merged_df["Gender"] == gender)][["Name","Std","Sec","Unit","Gender","House","Long Jump"]].nlargest(8, 'Long Jump', keep="all").dropna(subset=['Long Jump'])
    st.dataframe(table7, use_container_width=True ,hide_index=True)