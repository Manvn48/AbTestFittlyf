#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import numpy as np
from scipy import stats

# Function to perform AB test
def ab_test(control_visitors, control_conversions, treatment_visitors, treatment_conversions, confidence_level):
    # Calculate z-score and p-value
    z_score = (control_conversions / control_visitors - treatment_conversions / treatment_visitors) / np.sqrt(control_conversions / control_visitors * (1 - control_conversions / control_visitors) / control_visitors + treatment_conversions / treatment_visitors * (1 - treatment_conversions / treatment_visitors) / treatment_visitors)
    p_value = 1 - stats.norm.cdf(z_score)
    alpha = (100 - confidence_level) / 100

    # Compare p-value with alpha
    if p_value < alpha:
        return "Experiment Group is Better"
    elif p_value > (1 - alpha):
        return "Control Group is Better"
    else:
        return "Indeterminate"

# Main function for Streamlit app
def main():
    st.title("AB Test Hypothesis Testing App")
    st.write("This app allows you to perform hypothesis testing for AB testing.")

    # Get user input with labels and styling
    st.sidebar.subheader("Input Parameters")
    control_visitors = st.sidebar.number_input("Control Visitors", min_value=0, value=1000)
    control_conversions = st.sidebar.number_input("Control Conversions", min_value=0, value=200)
    treatment_visitors = st.sidebar.number_input("Treatment Visitors", min_value=0, value=1000)
    treatment_conversions = st.sidebar.number_input("Treatment Conversions", min_value=0, value=230)
    confidence_level = st.sidebar.selectbox("Confidence Level", [90, 95, 99])

    # Perform AB Test
    result = ab_test(control_visitors, control_conversions, treatment_visitors, treatment_conversions, confidence_level)
    
    # Display result with colored text
    st.write("Result of AB Test:", result)
    if result == "Experiment Group is Better":
        st.success(result)
    elif result == "Control Group is Better":
        st.error(result)
    else:
        st.warning(result)

if __name__ == "__main__":
    main()


# In[ ]:




