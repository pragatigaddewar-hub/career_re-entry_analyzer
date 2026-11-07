import streamlit as st
import matplotlib.pyplot as plt


st.title("Career Re-entry Analyzer")

st.subheader("Personal & Career Information")

name = st.text_input("Name :")
age = st.number_input("Age :",min_value=1,max_value=100,step=1)
education = st.text_input("Education")
year = st.number_input("Graduation Year :",step=1)
gap = st.number_input("Career Gap :",step=1)
experience = st.radio("Previous Work Experience :",
                      ["Experienced","Fresher"])
job_role = st.selectbox("Target Job Role",
                          ["Data Analytics","Data Scientist","Python Developer"])
location = st.multiselect("Preferred Location",
                          ["Mumbai","Pune","Bengaluru","Hyderabad","Nagpur"])


st.subheader("Skills Assessment")

python = st.slider("Python",min_value=0,max_value=100)
sql = st.slider("SQL",min_value=0,max_value=100)
pandas = st.slider("Pandas",min_value=0,max_value=100)
numpy = st.slider("Numpy",min_value=0,max_value=100)
statistics = st.slider("Statistics",min_value=0,max_value=100)
machine_learning = st.slider("Machine Learning",min_value=0,max_value=100)


skills = {
    "Python"           : python,
    "SQL"              : sql,
    "Pandas"           : pandas,
    "Numpy"            : numpy,
    "Statistics"       : statistics,
    "Machine Learning" : machine_learning
  }
skill_scores = python + sql + pandas + numpy + statistics + machine_learning
strongest_skill = max(skills,key=skills.get)
weakest_skill = min(skills,key=skills.get)

if skill_scores >= 500:
    career_readiness = "High Career Readiness"
elif  skill_scores >= 350:
    career_readiness = "Moderate Career Readiness"
else:
    career_readiness = "Needs Improvement"    


if skill_scores >= 440 and gap >= 10:
    suggestion = "Try For Job Application and Interviews"
elif skill_scores >= 300 and gap >= 10:
  suggestion = "Please Improve Your Skills"

else:
    # if skill score is low, suggest improving skills first
    if skill_scores >= 350:
        suggestion = "Try For Job Application"
    else:
        suggestion = "Please Improve Your Skills"

if gap >= 10:
    career_gap = 'High'
    
elif gap >= 5:
    career_gap = 'Moderate' 

else:
    career_gap = 'Less'  
    
        
submit = st.button("Submit")    
if submit:

    st.write("Basic Information")

    st.write("Name :" ,name)
    if name == "":
        st.warning("Please enter your name.")

    st.write("Age :" ,age)

    st.write("Education :" ,education)
    if education == "":
        st.warning("Please enter your education")

    st.write("Graduation Year :" ,year)
    st.write("Career Gap :" ,gap)
    st.write("Career Gap Status:" ,career_gap)
    st.write("Previous Work Experience :" ,experience)
    st.write("Target Job Role :" ,job_role)
    st.write("Preferred Location :" ,location)
    if not location:
        st.warning("Please select preferred location")

    st.subheader("Skills Assessment")

    st.write("Python           :" ,python)
    st.write("SQL              :" ,sql)
    st.write("Pandas           :" ,pandas)
    st.write("Numpy            :" ,numpy)
    st.write("Statistics       :" ,statistics)
    st.write("Machine Learning :" ,machine_learning)

    st.subheader("Career Analysis")

    col1,col2 = st.columns(2)
    with col1:
        st.metric("Overall Skill Score" ,skill_scores)
    with col2:    
        st.metric("Strongest Skill" ,strongest_skill)
    col3,col4 = st.columns(2)    
    with col3:    
        st.metric("Weakest Skill" ,weakest_skill)
    with col4:    
        st.metric("Career Readiness" ,career_readiness)

    if career_gap == 'High':    
        st.error("You need to work harder...")
        
    elif career_gap == 'Moderate':     
        st.warning("You need to work harder ...")

    else:
        st.success("Keep it up👍")  

    fig, ax = plt.subplots()
    ax.bar(skills.keys(),skills.values())   
    ax.set_title("Skill Assessment")
    ax.set_xlabel("Skill")
    ax.set_ylabel("Score")
    ax.tick_params(axis = 'x',rotation =45)
    st.pyplot(fig)

    st.subheader("Skills Improvement Suggestion")

    st.info(f"Suggestion : {suggestion}")
    st.write("Career Gap Status:" ,career_gap)


    st.subheader("Final Career Recommendation")

    if skill_scores >= 440 and career_gap == 'High':
        st.success(f"You selected {job_role},Your skills are good and career gap is high,you can proceed for job applications and interviews.")
    elif skill_scores >= 440 and career_gap == 'Moderate':
        st.info(f"You selected {job_role},Your skills are good and career gap is moderate,you can proceed for job applications.")
    elif skill_scores >= 440 and career_gap == 'Less':
        st.success(f"You selected {job_role}, your skills are excellent and you have little to no career gap — you're fully ready to apply for jobs and interviews.")    
    else: 
        st.warning(f"You selected {job_role},keep improving your skills and stay consistent with your career preparation.")       


    st.subheader("Skill Improvement Plan")  


    st.warning(f"Your weakest skill is {weakest_skill}. Improve it through regular practice.")
    st.success(f"Your strongest skill is {strongest_skill}. Keep practicing and master this skill to become even better.")
