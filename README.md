# Sentiment140 Analysis with PySpark and Google Cloud

## Overview

This project performs sentiment analysis, hashtag extraction, and activity trend analysis on an **enlarged Sentiment140 dataset** using **PySpark**. It processes the data and generates visualizations, while storing outputs on **Google Cloud Storage (GCS)**.
The main objective is to demonstrate how a cloud-based infrastructure can efficiently handle large datasets and generate actionable insights.

---

## Key Features

- **Hashtag Analysis**: Finds the top 10 most frequent hashtags.
- **Sentiment Distribution**: Calculates counts for positive, neutral, and negative sentiments.
- **Tweet Activity Over Time**: Analyzes hourly tweet activity trends.
- **Visualizations**: Graphical charts for clear insights.
- **Google Cloud Integration**: Reads data from and saves results to Google Cloud Storage.

---

## Dataset
The extended Sentiment140 dataset contains information about tweets categorized by sentiment (positive, neutral, negative).

Source: Sentiment140
Size: Over 1 GB.
Format: CSV.
Relevant Fields:
-sentiment: Sentiment label.
-created_at: Date and time the tweet was created.
-text: Tweet content.
Note: The **Enlarged Sentiment140 Dataset** is too large to upload to GitHub (over 1 GB). It is stored in Google Cloud Storage and can be downloaded from this link:  

[**Download the Enlarged Sentiment140 Dataset**](https://console.cloud.google.com/storage/browser/macro-nuance-210216/enlarged_sentiment140.csv)

---


## Project Structure

The project is organized as follows:

social-media-analysis/
│
├── data/                            # Placeholder for the input dataset
│   
│
├── output/
│   ├── activity_by_hour/            # Output directory for tweet activity trends
│   │   ├── output_proyect_activity_by_hour.csv_SUCCESS
│   │   └── output_proyect_activity_by_hour.csv_part-00000
│   ├── sentiment_count/             # Output directory for sentiment distribution
│   │   ├── output_proyect_sentiment_count.csv_SUCCESS
│   │   └── output_proyect_sentiment_count.csv_part-00000
│   └── top_hashtags/                # Output directory for top hashtags
│       ├── output_proyect_top_hashtags.csv_SUCCESS
│       └── output_proyect_top_hashtags.csv_part-00000
│
├── social_media_analysis.py         # Main script for running analysis
├── .gitignore                       # Git ignore file to exclude unnecessary files
└── README.md                        # Documentation for the project



## Setup Instructions

### Prerequisites

1. **Python 3.x** installed
2. **PySpark** for data processing
3. **Google Cloud SDK** installed and configured
4. Access to Google Cloud Storage (GCS)
5. **Matplotlib** library for visualizations

---

### Steps to Run the Project

1. **Clone the Repository**
   Open a terminal and run:
   ```bash
   git clone https://github.com/bb53137/social-media-analysis.git
   cd social-media-analysis

2. **Install Dependencies**
   Install the required libraries using `pip`:
   ```bash
   pip install pyspark matplotlib google-cloud-storage

3. **Update Google Cloud Paths**
   Replace the file paths in the code.py file with your Google Cloud Storage bucket paths:
   ```bash
   data_path = "gs://macro-nuance-210216/enlarged_sentiment140.csv"
   output_dir = "gs://macro-nuance-210216/output_proyect/"
   
4. **Run the Code**
   Execute the script:
   ```bash
   python social_media_analysis.py

### Outputs

The script generates the following outputs:

1. **CSV Files** (stored in GCS `output_proyect` folder):
   - `top_hashtags.csv`: Contains the top 10 most frequent hashtags.
   - `sentiment_count.csv`: Sentiment counts.
   - `activity_by_hour.csv`: Tweet activity trends by hour.

2. **Visualizations**:
   - **Top 10 Hashtags**
   - **Sentiment Distribution**
   - **Tweet Activity Over Time**
## Access Output Files

You can download the output files directly from Google Cloud Storage:

- [Top Hashtags CSV](https://console.cloud.google.com/storage/browser/macro-nuance-210216/output_proyect/top_hashtags.csv/)
- [Sentiment Count CSV](https://console.cloud.google.com/storage/browser/macro-nuance-210216/output_proyect/sentiment_count.csv/)
- [Activity by Hour CSV](https://console.cloud.google.com/storage/browser/macro-nuance-210216/output_proyect/activity_by_hour.csv/)

  
## Visualizations

Here are the links to the visualization images:

- [Top Hashtags Visualization](https://console.cloud.google.com/storage/browser/macro-nuance-210216/output_proyect/top_hashtags.png)
- [Sentiment Distribution Visualization](https://console.cloud.google.com/storage/browser/macro-nuance-210216/output_proyect/sentiment_distribution.png)
- [Tweet Activity Visualization](https://console.cloud.google.com/storage/browser/macro-nuance-210216/output_proyect/activity_by_hour.png)

## Advanced Features
Utilized regular expressions in PySpark to extract hashtags.
Generated visualizations using Matplotlib and automatically uploaded them to GCS.
Optimized PySpark transformations with efficient chaining.

## Conclusions
This project demonstrates how to handle large-scale data in the cloud using PySpark and Google Cloud.
The visualizations provide key insights into user behavior on Twitter.
-Lessons learned:
GCS integration simplifies large-scale data management.
PySpark is effective for distributed analysis but requires proper tuning for optimal performance.

-Future work:

Implement real-time analysis using Spark Streaming.
Explore additional datasets for comparative analysis.

### References
- [Sentiment140 Dataset](http://help.sentiment140.com/for-students/)  
  Official page for the Sentiment140 dataset, including details on how to use it.

- [PySpark Documentation](https://spark.apache.org/docs/latest/api/python/)  
  Official documentation for PySpark, describing its functionalities and available APIs.

- [Google Cloud SDK Documentation](https://cloud.google.com/sdk/docs/)  
  Official guide for Google Cloud SDK, including installation, configuration, and usage instructions.
Sentiment140
Página oficial de Sentiment140, que incluye información sobre el dataset y cómo utilizarlo.
PySpark Documentation
Documentación oficial de PySpark, que describe todas las funcionalidades y APIs disponibles.
Google Cloud SDK
Guía oficial de Google Cloud SDK, incluyendo cómo instalarlo, configurarlo y usarlo para interactuar con Google Cloud.
   
