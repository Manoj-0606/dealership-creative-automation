import streamlit as st
import os
from PIL import Image
import zipfile

from core.image_engine import ImageEngine

st.set_page_config(page_title="Dealership Creative Tool", layout="wide")

st.title("Dealership Creative Automation Tool")

engine = ImageEngine()

# -------------------------------
# Brand Selection
# -------------------------------
brand = st.selectbox(
    "Select Brand",
    ["Tata", "Kia", "Volkswagen"]
)

# -------------------------------
# Dealership Mapping
# -------------------------------
dealers = {
    "Tata": ["Tata Motors Bangalore", "Tata Motors Delhi"],
    "Kia": ["Kia Indiranagar", "Kia Whitefield"],
    "Volkswagen": ["VW Apple Auto", "VW KUN", "VW Lally"]
}

selected_dealers = st.multiselect(
    "Select Dealership(s)",
    dealers[brand]
)

# -------------------------------
# Upload Image
# -------------------------------
uploaded_file = st.file_uploader(
    "Upload Background Image",
    type=["jpg", "jpeg", "png"]
)

# -------------------------------
# Logo Option
# -------------------------------
use_logo = st.checkbox("Include Logo", value=True)

# -------------------------------
# Generate Button
# -------------------------------
if st.button("Generate Creatives"):

    if uploaded_file is None:
        st.error("Please upload an image")
    elif len(selected_dealers) == 0:
        st.error("Please select at least one dealership")
    else:
        # Save uploaded image temporarily
        temp_path = "temp.jpg"
        with open(temp_path, "wb") as f:
            f.write(uploaded_file.read())

        logo = engine.load_logo() if use_logo else None
        panels = engine.load_panels()

        outputs = []

        # Generate creatives for selected dealerships
        for i, dealer in enumerate(selected_dealers):
            panel = panels[i % len(panels)] if panels else None

            output_img = engine.process_image(temp_path, logo, panel)

            output_path = f"{dealer.replace(' ', '_')}.jpg"
            output_img.save(output_path)
            outputs.append(output_path)

        st.success("Creatives Generated Successfully")

        # -------------------------------
        # Display Outputs
        # -------------------------------
        for img_path in outputs:
            st.image(img_path, caption=img_path, use_container_width=True)

        # -------------------------------
        # Create ZIP for download
        # -------------------------------
        zip_path = "creatives.zip"
        with zipfile.ZipFile(zip_path, "w") as zipf:
            for file in outputs:
                zipf.write(file)

        with open(zip_path, "rb") as f:
            st.download_button(
                label="Download All Creatives (ZIP)",
                data=f,
                file_name="creatives.zip",
                mime="application/zip"
            )