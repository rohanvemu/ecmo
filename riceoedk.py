import pandas as pd  # read csv, df manipulation
import streamlit as st  #
import os
from streamlit_gsheets import GSheetsConnection

# Create a connection object.
# Create a connection object.
spreadsheet_url = st.secrets["store"]["url"]
    
st.set_page_config(
    page_title="ECMO",
    page_icon=":hospital:",
    layout="wide",
)

# Page Title
st.markdown('<h1 style="color:red;"> Ultrasound-Guided Continuous Coagulation Monitoring for ECMO</h1>', unsafe_allow_html=True)


# Project Overview Section
st.header("Project Overview")
st.markdown("""
Welcome to our project! We are working on a way to <span style="color:red">**non-invasively and continuously**</span> monitor coagulation status for critically ill patients on ECMO. 
 
  We believe that we can devise a method to allow better control over hemodynamic stability and vastly improve patient outcomes! 

  We are excited to invite engineering students to join us, keep reading to learn more!
""", unsafe_allow_html=True)

# st.markdown("""
# This is a line with **bold text**.  
# This line is <span style="color:green">green</span> and **bold**.  
# This is another line.<br><br>Here’s a new paragraph.
# """, unsafe_allow_html=True)

# Media Section
# Media Section
st.header("Project Background")

st.markdown("Extracorporeal membranous oxygenation (ECMO) provides cardiac and respiratory support for critically ill patients refractory to conventional management. The circuit is extremely complex with a lot of moving parts!")

# Create two columns
col1, col2 = st.columns(2)

# Place images in the columns
with col1:
    st.image("Images/patient.png", caption="Patient on ECMO", use_column_width=True)

with col2:
    st.image("Images/schematic_2.png", caption="ECMO Circuit Schematic", use_column_width=True)


st.header("It's a Balancing Act")

st.markdown("Coagulation monitoring is key in ensuring the success of ECMO for a patient; however, it comes with a few drawbacks. Multiple coagulation panels are taken in discrete measurements every 4-12 hours and such repeated blood draws can cause further complications in critically ill patients. Since the measurements are discrete, there is potential risk of missing an immediate change in a patient coagulation status. Finally, interfacing non-biologic ECMO polyvinyl cannulas with critically ill patients with already varying levels of hemodynamic stability can create a very risky, pro-thrombotic state.")


# Create empty columns to center the image
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.image("Images/juggle.png", caption="Factors to Juggle", width=700)

st.header("What Are We Addressing with Our Design")
st.markdown("""
There is a highlighted need to engineer a solution that can:
1. Reduce the number of blood draws needed
2. Continuously monitor coagulation status
3. Perform such data collection non-invasively and autonomously and display results on a mobile device.
""")

#Project Updates
st.header("Progression of Our Design")
st.write("Here are some of our milestones, so you can understand where we are with the design, and what role you as engineers will play in advancing our work!")
st.text("Update 1: Working Model")
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.image("Images/schematic_1.png", caption="Our Working Schematic", width=700)

st.text("Update 2: Initial Data Collection")
col1, col2 = st.columns(2)

# Place images in the columns
with col1:
    st.image("Images/aPTT.png", caption="aPTT w/ Thrombin Addition", use_column_width=True)

with col2:
    st.image("Images/FGN.png", caption="Fibrinogen w/ Thrombin Addition", use_column_width=True)
             

st.header("Advancing our Design with Engineers")
st.markdown("One of our main goals will be integrating the Clarius ultrasound probe which will provide extensive amounts of data on blood flow (e.g., RF data, B-mode images, elastography) that can serve as a proxy for clot formation. The Clarius ultrasound probe is specifically preferred due to its portability, ease of visualizing clot formation in the circuit, and ability to integrate its data with other potential design elements (i.e., Raspberry Pi, ML algorithms, LCD displays).")
col1, col2 = st.columns(2)

# Place images in the columns
with col1:
    st.image("Images/clarius.png", caption="Clarius Probe", width=300)

with col2:
    st.image("Images/sampledata.png", caption="Sample Data from Probe", use_column_width=True)
             
st.markdown("""
Our final design goals are as such:
<ol>
<li><strong style="color:red;">Create a device and casing that houses the ultrasound unit, circuitry, and additional sensors, integrates seamlessly with current ECMO circuit, and graphically displays the clotting metrics over time</strong></li>
<li><strong style="color:red;">Characterize the data coming from the Clarius ultrasound probe and software suite</strong></li>
<li><strong style="color:red;">Develop software and circuitry to process and analyze data, thus establishing specific metrics indicative of clot formation</strong></li>
<li><strong style="color:red;">Develop mobile app system to alert providers when metrics of clot formation exceed certain thresholds. (optional, time pending)</strong></li>
</ol>
""", unsafe_allow_html=True)

# Join the Team Section
st.header("Join the Team")
st.write("Interested in joining? Fill out the form below!")
name = st.text_input("Your Name")
email = st.text_input("Your Email")
message = st.text_area("Questions for Us")

if st.button("Submit"):
    if name and email and message:
        save_to_csv(name, email, message)
        st.write(f"Thank you for your interest, {name}! We will get in touch with you soon.")
    else:
        st.write("Please fill out all the fields.")
        
# Contact Information
data = {
    "Project Role": ["Principal Investigator", "Trauma Research Fellow", "Medical Student"],
    "Name": ["Howard Pryor, MD", "Shannon Larabee, MD", "Rohan Vemu, MSE"],
    "Email Address": ["hipryori@texaschildrens.org", "sxlarabe@texaschildrens.org", "rohan.vemu@bcm.edu"]
}

df = pd.DataFrame(data)

st.header("Contact Information")
st.write("For more information, reach out to us here:.")
st.dataframe(df.set_index(df.columns[0]))

# Social Media Integration (Simple Links)
st.header("Want to Learn More and Connect?")
st.write("[Our Lab](https://www.texaschildrens.org/find-a-provider/howard-irwin-pryor-ii-md) | [Helpful Links](https://github.com/rohanvemu/ecmo)")
