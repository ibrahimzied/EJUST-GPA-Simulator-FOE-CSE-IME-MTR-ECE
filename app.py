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
        "Semester 7 (L4-1)": {"International Contracts and Arbitration": 2, "Cryptography": 3, "Operating Systems": 3, "Elective
