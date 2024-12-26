import streamlit as st
import pandas as pd

st.set_page_config(page_title="SNK Athletic Meet 2024-25")

# Load data from csv into DataFrame
merged_df = pd.read_csv("combined_2425.csv")

# Streamlit app
st.title("Athletic Meet 2024-25")
st.header("Student Performance App")

# Dropdowns with default selection as None
school_list = sorted(merged_df.School.unique())
select_school = st.selectbox("Select School:", options=school_list, index=None)

if select_school:
    grade_list = sorted(merged_df[merged_df["School"] == select_school].Std.unique())
    select_grade = st.selectbox("Select Grade:", options=grade_list, index=None)
    
    if select_grade:
        section_list = sorted(merged_df[(merged_df["School"] == select_school) & (merged_df["Std"] == select_grade)].Sec.unique())
        select_section = st.selectbox("Select Section:", options=section_list, index=None)
        
        if select_section:
            student_list = sorted(merged_df[(merged_df["School"] == select_school) & 
                                            (merged_df["Std"] == select_grade) & 
                                            (merged_df["Sec"] == select_section)].Name.unique())
            selected_student = st.selectbox("Select Student:", options=student_list, index=None)
            
            if selected_student:
                # Display selected student's data
                selected_student_data = merged_df[merged_df["Name"] == selected_student]
                st.write(f"## {selected_student}'s Performance:")
                st.dataframe(selected_student_data, column_config= {"School": None,"200m(s)": None}, hide_index=True)

                st.write("###### 100m Time: *ss.ms*")
                st.write("###### 200m Time: *ss.ms OR m.ss.ms*")
                st.write("###### If any of your event time is displayed as None, it indicates that your performance time was not recorded due to certain reasons.")
                
                "---"
                # Display top 8 students for events
                st.write("## Top 8 students in each event from your Unit:")
                
                st.write("### 100m Running")
                table1 = merged_df[(merged_df["Unit"] == selected_student_data["Unit"].values[0]) & 
                                   (merged_df["Std"] == select_grade) & (merged_df["School"] == select_school) &
                                   (merged_df["Gender"] == selected_student_data["Gender"].values[0])][["Name","Std","Sec","Unit","Gender","House","100m"]]
                table1 = table1.nsmallest(8, '100m', keep='all').dropna(subset=['100m'])
                st.dataframe(table1, use_container_width=True, hide_index=True)
                
                st.write("### 200m Running")
                table21 = merged_df[(merged_df["Unit"] == selected_student_data["Unit"].values[0]) & 
                                    (merged_df["Std"] == select_grade) & (merged_df["School"] == select_school) &
                                    (merged_df["Gender"] == selected_student_data["Gender"].values[0])][["Name","Std","Sec","Unit","Gender","House","200m","200m(s)"]]
                table21 = table21.nsmallest(8, '200m(s)', keep='all').dropna(subset=['200m(s)'])
                st.dataframe(table21, column_config={"200m(s)": None}, use_container_width=True, hide_index=True)
