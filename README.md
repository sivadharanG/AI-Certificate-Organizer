# AI Certificate Organizer

## Overview

AI Certificate Organizer is a Python-based application that helps users organize and analyze certificates automatically. The system extracts text from certificate images and PDFs, identifies skills, categorizes them into domains, generates LinkedIn captions, creates resume summaries, and provides career recommendations using Gemini AI.

## Features

* Upload certificate images and PDFs
* OCR-based text extraction using Tesseract
* Automatic skill detection
* Domain-wise skill categorization
* Interactive dashboard and analytics
* AI-generated LinkedIn captions
* Resume summary generation
* Career recommendations
* AI Readiness Score calculation

## Technologies Used

* Python
* Streamlit
* Tesseract OCR
* PDFPlumber
* Pandas
* Matplotlib
* Google Gemini AI

## Installation

1. Clone the repository

```bash
git clone https://github.com/sivadharanG/AI-Certificate-Organizer.git
```

2. Navigate to the project folder

```bash
cd AI-Certificate-Organizer
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Create a `.env` file

```env
GEMINI_API_KEY=your_api_key
```

5. Run the application

```bash
streamlit run app.py
```

## Project Workflow

1. Upload certificates
2. Extract text using OCR
3. Detect skills automatically
4. Analyze domains and skill frequency
5. Generate LinkedIn captions
6. Create resume summaries
7. Recommend career paths

## Future Improvements

* Certificate authenticity verification
* Skill gap analysis
* Resume generation
* Certificate database storage
* Advanced AI-based career roadmap suggestions

## Author

Sivadharan G

B.Sc Artificial Intelligence & Machine Learning

VLB Janakiammal College of Arts and Science
