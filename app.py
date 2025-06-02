import streamlit as st

def main():
    st.set_page_config(page_title="=============================", layout="wide")

    st.sidebar.header("Input User Sidebar")

    # Sidebar Inputs
    feature_1 = st.sidebar.slider("Feature 1", min_value=0, max_value=100, value=50)
    feature_2 = st.sidebar.selectbox("Feature 2", ["Option 1", "Option 2"])
    feature_3 = st.sidebar.selectbox("Feature 3", ["Option A", "Option B"])
    feature_4 = st.sidebar.slider("Feature 4", min_value=0, max_value=200, value=100)
    feature_5 = st.sidebar.slider("Feature 5", min_value=0, max_value=300, value=150)
    feature_6 = st.sidebar.selectbox("Feature 6", ["Yes", "No"])
    feature_7 = st.sidebar.selectbox("Feature 7", ["Category 1", "Category 2", "Category 3"])
    feature_8 = st.sidebar.slider("Feature 8", min_value=0, max_value=150, value=75)
    feature_9 = st.sidebar.selectbox("Feature 9", ["True", "False"])

    # Main Section
    st.title("Heart Disease Prediction")

    # Tab Layout
    tab1, tab2 = st.tabs(["Single Prediction", "Multi Prediction"])

    with tab1:
        st.subheader("User Input")
        user_input = {
            "Feature 1": feature_1,
            "Feature 2": feature_2,
            "Feature 3": feature_3,
            "Feature 4": feature_4,
            "Feature 5": feature_5,
            "Feature 6": feature_6,
            "Feature 7": feature_7,
            "Feature 8": feature_8,
            "Feature 9": feature_9,
        }

        st.table([user_input])

        if st.button("Predict"):
            st.success("Prediction Complete")
            st.subheader("Prediction Result")
            # Example Result
            st.markdown(
                "### Prediction: Level X\n" +
                "This is a placeholder for the prediction result.\n" +
                "Please customize the result description based on the model output."
            )

    with tab2:
        st.write("Multi Prediction functionality will be added here.")

if __name__ == "__main__":
    main()
