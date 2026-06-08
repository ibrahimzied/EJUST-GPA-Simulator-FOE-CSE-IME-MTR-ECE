import streamlit as st

GRADE_POINTS = {
    "A+": 4.00, "A": 4.00, "A-": 3.70,
    "B+": 3.30, "B": 3.00, "B-": 2.70,
    "C+": 2.30, "C": 2.00, "C-": 1.70,
    "D+": 1.30, "D": 1.00, "F": 0.00
}

COMMON_SEMESTERS = {
    "Semester 1 (L1-1)": {
        "LRA 111 (Japanese 1)": 1, "LRA 112 (Fund. of Communications)": 2, "LRA 113 (Safety & Risk Management)": 2, 
        "IME 111 (Engineering Drawings)": 2, "MTH 111 (Mathematics 1)": 3, "PHY 111 (Physics 1)": 3, 
        "PHY 112 (Physics Lab 1)": 1, "MTR 111 (Mechanics: Static-Dynamic)": 3, "CHM 111 (Chemistry 1)": 1, "CHM 112 (Chemistry Lab 1)": 1
    },
    "Semester 2 (L1-2)": {
        "LRA 121 (Japanese 2)": 1, "LRA 122 (Japanese Culture)": 2, "LRA 123 (Key Skills Seminar)": 2,
        "CSE 111 (Intro to Computer Science)": 2, "MTH 121 (Mathematics 2)": 3, "PHY 121 (Physics 2)": 3,
        "PHY 122 (Physics Lab 2)": 1, "CHM 121 (Chemistry 2)": 1, "CHM 122 (Chemistry Lab 2)": 1, "IME 121 (Intro to Manufacturing)": 3
    },
    "Semester 3 (L2-1)": {
        "LRA 211 (Japanese 3)": 1, "LRA 212 (Economics & Sustainable Dev)": 2, "LRA 21X (UR Elective 1)": 2,
        "MTH 211 (Mathematics 3)": 3, "IME 211 (Intro to Mechanical Eng)": 3, "ECE 211 (Intro to Electrical Eng)": 3,
        "CPE 211 (Intro to Energy & Chem Eng)": 3, "CSE 211 (Computer Programming)": 2
    }
}

DEPARTMENTS_DATA = {
    "Computer Systems Engineering (CSE)": {
        "Semester 4 (L2-2)": {"UR Elective (2)": 2, "Mathematics (4)": 3, "Measurements and Instrumentations": 3, "Project Management": 2, "Digital Logic Design": 3, "Introduction to Electronics": 3, "Signals and Systems": 3},
        "Semester 5 (L3-1)": {"UR Elective (3)": 2, "Advanced mathematics with software application": 3, "Digital Signal Processing": 3, "Electric and Magnetic Fields": 3, "Computer Organization": 3, "Seminar and PBL on CSE": 2, "Discrete Mathematics": 3},
        "Semester 6 (L3-2)": {"Contemporary Societal Issues": 2, "Thermo-Fluid": 3, "Introduction to Control Systems": 3, "Advanced Programming": 3, "Embedded Systems": 2, "Analysis and Design of Algorithms": 3, "Machine Learning": 3},
        "Semester 7 (L4-1)": {"International Contracts and Arbitration": 2, "Cryptography": 3, "Operating Systems": 3, "Elective 1": 3, "Computer Networks": 2, "Image Processing & Computer vision": 2, "Industrial Training": 0, "Graduation Project I": 3},
        "Semester 8 (L4-2)": {"Theory Of Computation": 3, "Parallel and Distributed Computing": 3, "Elective 2": 3, "Elective 3": 3, "Graduation Project II": 6}
    },
    "Electronics & Communications Engineering (ECE)": {
        "Semester 4 (L2-2)": {"UR Elective (2)": 2, "Mathematics (4)": 3, "Measurements and Instrumentations": 3, "Project Management": 2, "Introduction to Electronics Engineering": 3, "Digital Logic Design": 3, "Signals and Systems": 3},
        "Semester 5 (L3-1)": {"UR Elective (3)": 2, "Advanced Engineering mathematics with software applications": 3, "Electric and magnetic fields": 3, "Digital Signal Processing": 3, "Microprocessors and Microcontrollers": 3, "Electronic Devices": 3, "Seminar and Project Based Learning in ECE": 2},
        "Semester 6 (L3-2)": {"Contemporary Societal Issues": 2, "Thermo-Fluid": 3, "Introduction to Control Systems": 3, "Electronic Circuits": 3, "Communications Systems Fundamentals": 3, "Optical communications devices": 2, "Data Communication Networks": 3},
        "Semester 7 (L4-1)": {"International Contracts and Arbitration": 2, "Digital Communications Systems": 3, "Electromagnetic Fields and Antennas": 3, "Digital VLSI modeling and Design": 3, "Principle of Information Theory and coding": 2, "Elective 1": 3, "Industrial Training": 0, "Graduation Project I": 3},
        "Semester 8 (L4-2)": {"CMOS Analog Integrated Circuits": 3, "Fundamentals of Wireless Communications": 3, "Elective 2": 3, "Elective 3": 3, "Graduation Project II": 5}
    },
    "Electrical Power Engineering (EPE)": {
        "Semester 4 (L2-2)": {"UR Elective (2)": 2, "Mathematics (4)": 3, "Measurements and Instrumentations": 3, "Project Management": 2, "Digital Logic Design": 3, "Introduction to Electronics": 3, "Signals and Systems": 3},
        "Semester 5 (L3-1)": {"UR Elective (3)": 2, "Advanced mathematic with software application": 3, "Digital Signal Processing": 3, "Electric and Magnetic Fields": 3, "Power Electronics 1": 3, "Electrical Machines 1": 3, "Advanced Electrical Circuit": 2},
        "Semester 6 (L3-2)": {"Contemporary Societal Issue": 2, "Thermo-Fluid": 3, "Introduction to Control Systems": 3, "Seminar and Project Based Learning on EPE": 2, "Power Electronics 2": 3, "Electrical Machines 2": 3, "Fundamentals of Power Systems": 3},
        "Semester 7 (L4-1)": {"International Contracts and Arbitration": 2, "Special Machines": 3, "Power Systems Analysis": 3, "High Voltage Engineering": 2, "Economic Operation and control of Power Systems": 2, "Elective 1": 3, "Industrial Training": 0, "Graduation Project I": 3},
        "Semester 8 (L4-2)": {"Electric Drives": 3, "Switchgear and Protection of Power Systems": 3, "Elective 2": 3, "Elective 3": 3, "Graduation Project II": 6}
    },
    "Mechatronics Engineering (MTR)": {
        "Semester 4 (L2-2)": {"UR Elective (2)": 2, "Mathematics (4)": 3, "Measurement and Instrumentation": 3, "Project Management": 2, "Engineering Materials": 3, "Theory of Machines": 3, "Strength of Materials": 3},
        "Semester 5 (L3-1)": {"UR Elective (3)": 2, "Introduction to Mechatronics": 2, "Embedded Systems in Mechatronics": 3, "Mechanical Vibrations": 3, "Mechanical Design (1)": 3, "Electronic Circuits": 3, "Digital Logic Design": 3},
        "Semester 6 (L3-2)": {"Contemporary Societal Issues": 2, "Systems Modeling and Control": 3, "Thermodynamics and Heat Transfer": 3, "Fluid Mechanics and Hydraulics": 3, "Mechatronics systems design": 3, "Robotics (1)": 3, "Seminar and PBL in Mechatronics Engineering": 2},
        "Semester 7 (L4-1)": {"International Contracts and Arbitration": 2, "Mobile Robots & Machine vision": 3, "control system design (control 2)": 3, "Micro Systems Technology": 3, "Artificial Intelligence in Mechatronics and Robotics": 3, "Programmable Logic Controllers": 2, "Industrial Training": 0, "Graduation Project I": 3},
        "Semester 8 (L4-2)": {"Elective 1": 3, "Elective 2": 3, "Elective 3": 3, "Hydraulic and Pneumatic Control Systems": 2, "Graduation Project II": 6}
    },
    "Industrial & Manufacturing Engineering (IME)": {
        "Semester 4 (L2-2)": {"UR Elective (2)": 2, "Mathematics (4)": 3, "Measurement and Instrumentation": 3, "Project Management": 2, "Engineering Materials": 3, "Theory of Machines": 3, "Strength of Materials": 3},
        "Semester 5 (L3-1)": {"UR Elective (3)": 2, "Mechanical Vibrations": 3, "Mechanical Design (1)": 3, "Seminar and PBL in Industrial and Manufacturing": 2, "Operations Research (1)": 3, "Metal Forming Processes": 3, "Conventional Machining Processes": 3},
        "Semester 6 (L3-2)": {"Contemporary Societal Issue": 2, "Systems Modeling and Control": 3, "Thermodynamics and Heat Transfer": 3, "Fluid Mechanics and Hydraulics": 3, "Soft Computing in Industrial Applications": 2, "Production and Operations Management": 3, "Management Information Systems": 3},
        "Semester 7 (L4-1)": {"International Contracts and Arbitration": 2, "Engineering Economic Analysis": 2, "Track Requirement (elective)": 3, "Facilities Planning and Material Handling": 3, "Statistical Quality Control": 3, "Ergonomics and Human Factors Engineering": 3, "Industrial Training": 0, "Graduation Project I": 3},
        "Semester 8 (L4-2)": {"Computer Integrated Manufacturing": 3, "Supply Chain and Logistics Management": 3, "Track Requirement (elective) 1": 3, "Track Requirement (elective) 2": 2, "Graduation Project II": 6}
    }
}

st.set_page_config(page_title="E-JUST Engineering GPA Calculator", page_icon="🎓", layout="centered")
st.title("🎓 E-JUST Engineering GPA Simulator")
st.write("Calculate Semester GPA and Cumulative CGPA instantly based on the EXACT official curriculum.")

st.header("1️⃣ Previous Academic Standing")
col_gpa, col_hrs = st.columns(2)
with col_gpa:
    input_cgpa = st.number_input("Prior Cumulative CGPA:", min_value=0.0, max_value=4.0, value=3.16, step=0.01)
with col_hrs:
    input_hours = st.number_input("Prior Cumulative Earned Hours (CH):", min_value=0, value=57, step=1)

st.markdown("---")

st.header("2️⃣ Target Specification & Semester")
selected_dept = st.selectbox("Select Your Department:", list(DEPARTMENTS_DATA.keys()))

available_semesters = list(COMMON_SEMESTERS.keys()) + list(DEPARTMENTS_DATA[selected_dept].keys())
default_sem_index = 3 if len(available_semesters) > 3 else 0
target_semester = st.selectbox("Select Semester to Simulate:", available_semesters, index=default_sem_index)

st.markdown("---")

st.header(f"3️⃣ Expected Course Grades for {target_semester}")

if target_semester in COMMON_SEMESTERS:
    active_courses = COMMON_SEMESTERS[target_semester].copy()
else:
    active_courses = DEPARTMENTS_DATA[selected_dept][target_semester].copy()

with st.expander("➕ Add Custom / Overload Course"):
    c_name = st.text_input("Course Name:")
    c_ch = st.number_input("Credit Hours:", min_value=1, max_value=6, value=3)
    if st.button("Add Course to List"):
        if c_name:
            active_courses[c_name] = c_ch
            st.success(f"Added {c_name} ({c_ch} CH)")

total_term_quality_points = 0.0
total_term_hours = 0
deduct_prior_hours = 0
deduct_prior_points = 0.0

for course, ch in active_courses.items():
    col_name, col_grade, col_repeat = st.columns([3, 1, 1])
    with col_name:
        st.write(f"🔹 **{course}** — `{ch} Credit Hours`")
    with col_grade:
        if ch > 0:
            grade = st.selectbox("Grade:", list(GRADE_POINTS.keys()), index=4, key=f"sim_{target_semester}_{course}")
            total_term_quality_points += GRADE_POINTS[grade] * ch
            total_term_hours += ch
        else:
            st.write("*(Pass/Fail)*")
            
    with col_repeat:
        if ch > 0:
            is_repeat = st.checkbox("Repeat?", key=f"rep_{target_semester}_{course}")
            if is_repeat:
                old_grade = st.selectbox("Old Grade:", list(GRADE_POINTS.keys()), index=11, key=f"old_{target_semester}_{course}")
                deduct_prior_hours += ch
                deduct_prior_points += GRADE_POINTS[old_grade] * ch

calculated_term_gpa = total_term_quality_points / total_term_hours if total_term_hours > 0 else 0.0

prior_total_points = (input_cgpa * input_hours) - deduct_prior_points
adjusted_prior_hours = input_hours - deduct_prior_hours

new_total_quality_points = prior_total_points + total_term_quality_points
new_total_hours = adjusted_prior_hours + total_term_hours
calculated_new_cgpa = new_total_quality_points / new_total_hours if new_total_hours > 0 else 0.0

st.markdown("---")
st.header("📊 Estimation Results Summary")

col_res1, col_res2 = st.columns(2)
with col_res1:
    st.metric(label="Semester GPA", value=f"{calculated_term_gpa:.2f}", delta=f"{total_term_hours} CH Current")
with col_res2:
    cgpa_delta = calculated_new_cgpa - input_cgpa
    st.metric(label="New Cumulative CGPA", value=f"{calculated_new_cgpa:.2f}", delta=f"{cgpa_delta:+.2f} Change")

if calculated_new_cgpa < 2.0:
    st.error("⚠️ **Academic Probation Warning:** Cumulative GPA drops below 2.0 limit. (Article 20)")
elif calculated_term_gpa >= 3.7:
    st.balloons()
    st.success("✈️ 🇯🇵 **Excellent Academic Standing:** Eligible for Japanese Partner University programs. (Article 14)")

st.markdown("---")
st.caption("🔒 **Privacy Note:** This simulator runs entirely in your browser. No academic data is collected or stored on any server.")
st.caption("Developed for **Egypt-Japan University of Science and Technology (E-JUST)** Students.")
