import streamlit as st

# Sidebar with Navigation Links
st.sidebar.title("Navigation")
st.sidebar.markdown("[Resume](https://drive.google.com/file/d/1cM77ga8TZzhngI30XniL03WammTL4PHU/view?usp=sharing)")
st.sidebar.markdown("[GitHub](https://github.com/Madhuganisaikumar)")
st.sidebar.markdown("[THM](https://tryhackme.com/p/yourprofile)")
st.sidebar.markdown("[LinkedIn](https://linkedin.com/in/yourprofile)")

# Main Logo
st.image("https://your-logo-link.com/logo.png", use_column_width=True)

# Main Title
st.title("Welcome to My Portfolio")

# Projects Section (Modal-like expander)
with st.expander("Projects"):
    st.image("https://your-project1-image.com", caption="Zero Trust Blockchain")
    st.image("https://your-project2-image.com", caption="KLCybersac")
    st.image("https://your-project3-image.com", caption="Career Portal")

# Certifications Section (Modal-like expander)
with st.expander("Certifications"):
    st.image("https://your-cert1-image.com", caption="Certified Ethical Hacker")
    st.image("https://your-cert2-image.com", caption="AI Associate")
    st.image("https://your-cert3-image.com", caption="Google Cloud Cybersecurity")
    st.image("https://your-cert4-image.com", caption="Red Hat Developer")
