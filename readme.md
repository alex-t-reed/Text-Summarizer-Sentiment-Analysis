# Text Summarizer with Sentiment Analysis Web App

![Demo GIF](./demo.gif)

The Text Summarizer is a web application that leverages natural language processing techniques to create concise and coherent summaries from longer pieces of text. It simplifies the process of information extraction, making it easier for users to digest and comprehend voluminous content such as articles, reports, and documents.Additionally, it includes sentiment analysis for the original text.

This project builds upon previous work in the [NLP-Example Repository](https://github.com/alex-t-reed/NLP-Example), which contains Python scripts for Natural Language Processing (NLP) tasks and text summarization.

- [Text Summarizer with Sentiment Analysis Web App](#text-summarizer-with-sentiment-analysis-web-app)
  - [Features](#features)
  - [Technologies Used](#technologies-used)
  - [Usage](#usage)
  - [Installation](#installation)
  - [Limitations](#limitations)
  - [Feedback](#feedback)

## Features

- User-friendly web interface for text summarization.
- Automatic summarization of input text.
- Option to sample random content from Wikipedia for summarization.
- Sentiment analysis for original and summary text.

## Technologies Used

- Python for backend logic.
- Flask web framework for building the web application.
- NLTK (Natural Language Toolkit) for text processing and summarization.
- Materialize for styling the user interface.
- TextBlob for sentiment analysis.

## Usage

1. **Input Text**: Enter the text you want to summarize into the text area on the main page.

2. **Summarize**: Click the "Summarize" button to generate a summary of the input text.

3. **Sample from Wikipedia**: Optionally, click the "Sample from Wikipedia" button to fetch random Wikipedia text for summarization.

4. **View Summary**: The generated summary will be displayed on the same page along with the original text.

## Installation

To run this application locally, follow these steps:

1. Clone this repository to your local machine.

```bash
git clone https://github.com/alex-t-reed/text-summarizer-sentiment-analysis.git
cd text-summarizer-sentiment-analysis
```
2. Install the required Python packages using pip. It's recommended to use a virtual environment.

```bash
pip install -r requirements.txt
```

3. Start the Flask application.

```bash
python app.py
```

4. Open a web browser and visit http://127.0.0.1:5000 to use the Text Summarizer.

## Limitations

- The quality of the summary depends on the complexity and quality of the input text. It may not always capture nuances and context effectively.
- The summarization model used here is based on word frequency and may not handle very technical or domain-specific content optimally.
- Large volumes of text may result in less coherent summaries.
---
## Feedback

For questions, suggestions, or collaboration opportunities, please don't hesitate to reach out me.
- **Email**: [Alex Reed](mailto:alexreed@ucsb.edu)
- **LinkedIn**: [Alex Reed on LinkedIn](https://www.linkedin.com/in/alextreed)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/alextreed)
