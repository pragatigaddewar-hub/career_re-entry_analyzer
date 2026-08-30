# Career Re-entry Analyzer

A Streamlit web app that helps people returning to work after a career break assess their skills, understand their career gap status, and get personalized guidance on their job readiness.

## Overview

This app collects personal, educational, and career details along with a self-assessment of key technical skills. Based on this, it calculates an overall skill score, evaluates the career gap, and generates tailored suggestions and a final career recommendation.

## Features

- Captures personal and career background: name, age, education, graduation year, career gap, prior experience, target job role, and preferred locations
- Self-assessment sliders for six key skills: Python, SQL, Pandas, Numpy, Statistics, and Machine Learning
- Calculates:
  - Overall skill score and career readiness level
  - Strongest and weakest skill
  - Career gap status (Less / Moderate / High)
  - A personalized suggestion based on skills and career gap
  - A final career recommendation tailored to skill level and gap
- Visualizes skill scores using a bar chart
- Input validation warnings for missing name, education, or location

## How to Run

1. Clone or download this repository.
2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```
3. Run the app:
   ```
   streamlit run career_analyzer.py
   ```
4. Fill in your details and skill levels, then click **Submit** to see your personalized career analysis.

## Tools Used

- **Python**
- **Streamlit** for the web interface
- **Matplotlib** for visualization
