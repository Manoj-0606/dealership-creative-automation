# Dealership Creative Automation Tool

## Project Overview

This project is a web-based tool designed to automate the generation of dealership marketing creatives by combining background images, dealership panels, and optional logos.

The tool allows users to quickly generate multiple creatives with minimal manual effort, fulfilling the requirements of bulk processing and intelligent automation.

---

## Features

* **Brand Selection**

  * Choose from multiple brands (Tata, Kia, Volkswagen)

* **Dealership Selection (Bulk Support)**

  * Select one or multiple dealerships dynamically based on the chosen brand

* **Background Image Upload**

  * Upload JPG/PNG images without distortion

* **Logo Toggle**

  * Option to include or exclude logo in creatives

* **Automated Creative Generation**

  * Combines:

    * Background image
    * Dealership panel
    * Logo (optional)

* **Bulk Processing**

  * Generates creatives for multiple dealerships in one click

* **Output Display**

  * Preview generated creatives directly in the UI

* **Download Option**

  * Download all creatives as a ZIP file

---

## AI / Automation Logic Implemented

The system includes intelligent automation features:

* **Auto-scaling of Logo**

  * Dynamically adjusts logo size based on image dimensions

* **Panel Positioning**

  * Automatically places dealership panels at the bottom with proper alignment

* **Batch Processing**

  * Efficiently processes multiple dealerships using looping logic

---

## Tech Stack

* Python
* Streamlit (Web UI)
* Pillow (Image Processing)
* OS & Zipfile (File handling)

---

## Project Structure

```
dealership-creative-automation/
│
├── app.py
├── main.py
├── requirements.txt
|---database.sql
├── core/
│   └── image_engine.py
│
├── assets/
│   ├── Logos/
│   ├── Dealership-panels/
│   ├── Sample-input-images/
│   └── Expected-output-examples/
│
└── output/
```

---

## Setup Instructions

1. Clone or download the project

2. Install dependencies:

```
pip install -r requirements.txt
```

3. Run the application:

```
streamlit run app.py
```

4. Open the browser at:

```
http://localhost:8501
```

---

## How to Use

1. Select a **Brand**
2. Select one or more **Dealerships**
3. Upload a **Background Image**
4. Toggle **Include Logo** (optional)
5. Click **Generate Creatives**
6. Preview outputs and download ZIP

---

## Output Formats

* Generated creatives are saved as JPG images
* Bulk download available as ZIP file

---

##  Notes

* The system ensures proper alignment and avoids image distortion
* Designed for scalability and bulk processing
* Easy to extend with additional brands and dealerships

---

##  Author

Manoj

---
