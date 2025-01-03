# **Sentiment140 Analysis with PySpark and Google Cloud**

## **Overview**

This project performs sentiment analysis, hashtag extraction, and activity trend analysis on an **enlarged Sentiment140 dataset** using **PySpark**. It processes the data and generates visualizations, while storing outputs on **Google Cloud Storage (GCS)**.

The main objective is to demonstrate how a cloud-based infrastructure can efficiently handle large datasets and generate actionable insights.

### **Why Big Data and Cloud?**
- **Big Data**: The dataset exceeds 1 GB, making it impractical for local processing. PySpark allows parallel processing of large datasets efficiently.
- **Cloud**: Google Cloud provides scalable infrastructure and storage for managing and analyzing data at scale.
  
---

## **Key Features**

- **Hashtag Analysis**: Finds the top 10 most frequent hashtags.
- **Sentiment Distribution**: Calculates counts for positive, neutral, and negative sentiments.
- **Tweet Activity Over Time**: Analyzes hourly tweet activity trends.
- **Visualizations**: Graphical charts for clear insights.
- **Google Cloud Integration**: Reads data from and saves results to Google Cloud Storage.

---

## **Dataset**
The extended Sentiment140 dataset contains information about tweets categorized by sentiment (positive, neutral, negative).

-**Source**: Sentiment140
- **Size**: Over 1 GB.
- **Format**: CSV.
- **Relevant Fields**:
  - `sentiment`: Sentiment label (positive, neutral, or negative).
  - `created_at`: Date and time the tweet was created.
  - `text`: The tweet's content.
>**Note**: The **Enlarged Sentiment140 Dataset** is too large to upload to GitHub (over 1 GB).
> It is stored in Google Cloud Storage and can be downloaded from this link:  
>[**Download the Enlarged Sentiment140 Dataset**](https://console.cloud.google.com/storage/browser/macro-nuance-210216/enlarged_sentiment140.csv)

---


## **Project Structure**

The project is organized as follows:

social-media-analysis/
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



## **Setup Instructions**

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

### **Outputs**

The script generates the following outputs:

1. **CSV Files** (stored in GCS `output_proyect` folder):
   - `top_hashtags.csv`: Contains the top 10 most frequent hashtags.
   - `sentiment_count.csv`: Sentiment counts.
   - `activity_by_hour.csv`: Tweet activity trends by hour.

2. **Visualizations**:
   - **Top 10 Hashtags**
   - **Sentiment Distribution**
   - **Tweet Activity Over Time**
  


## **Performance Evaluation**

### **Configurations Tested**

| Configuration           | Dataset Size | Nodes | vCPUs per Node | Execution Time |
|--------------------------|--------------|-------|----------------|----------------|
| Local Machine            | 1 GB         | 1     | 4              | ~15 minutes    |
| Google Cloud (Small)     | 1 GB         | 1     | 4              | ~5 minutes     |
| Google Cloud (Medium)    | 1 GB         | 3     | 4              | ~2 minutes     |

---

### **Observations**

1. **Scalability**: Adding nodes improves performance significantly.
2. **Cost Efficiency**: A small cluster is sufficient for moderate datasets, while larger clusters are better for Big Data.

---

### **How to Reproduce Performance Evaluation**

#### Local Environment:
1. Run the script on your local machine.
2. Use the existing `time` module implementation in your script to measure execution time.

#### Google Cloud Dataproc:
1. Create a Dataproc cluster.
2. Upload the dataset to Google Cloud Storage.
3. Submit the PySpark job using:
   ```bash
   gcloud dataproc jobs submit pyspark gs://<bucket-name>/social_media_analysis.py \
    --cluster=<cluster-name> \
    --region=<region>


## Access Output Files

You can download the output files directly from Google Cloud Storage:

- [Top Hashtags CSV](https://console.cloud.google.com/storage/browser/macro-nuance-210216/output_proyect/top_hashtags.csv/)
- [Sentiment Count CSV](https://console.cloud.google.com/storage/browser/macro-nuance-210216/output_proyect/sentiment_count.csv/)
- [Activity by Hour CSV](https://console.cloud.google.com/storage/browser/macro-nuance-210216/output_proyect/activity_by_hour.csv/)

  
## **Visualizations**

Here are the links to the visualization images:

- [Top Hashtags Visualization](https://console.cloud.google.com/storage/browser/macro-nuance-210216/output_proyect/top_hashtags.png)
- [Sentiment Distribution Visualization](https://console.cloud.google.com/storage/browser/macro-nuance-210216/output_proyect/sentiment_distribution.png)
- [Tweet Activity Visualization](https://console.cloud.google.com/storage/browser/macro-nuance-210216/output_proyect/activity_by_hour.png)

## **Code Explanation**

The main script `social_media_analysis.py` performs the following steps:

1. **Data Loading**:
   - Reads the dataset from Google Cloud Storage into a Spark DataFrame.

2. **Hashtag Analysis**:
   - Extracts hashtags using regular expressions.
   - Groups hashtags and counts their occurrences.
   - Saves the top 10 most frequent hashtags to GCS.

3. **Sentiment Distribution**:
   - Groups tweets by sentiment (positive, neutral, negative) and calculates counts.
   - Saves the sentiment distribution to GCS.

4. **Hourly Activity Trends**:
   - Extracts the hour from the `created_at` column.
   - Groups tweets by hour and calculates tweet counts.
   - Saves hourly activity trends to GCS.

5. **Visualizations**:
   - Generates visualizations for hashtags, sentiment distribution, and hourly trends using Matplotlib.
   - Uploads the images to GCS for easy access.


## **Advanced Features**
Utilized regular expressions in PySpark to extract hashtags.
Generated visualizations using Matplotlib and automatically uploaded them to GCS.
Optimized PySpark transformations with efficient chaining.

## **Conclusions**
This project demonstrates how to handle large-scale data in the cloud using PySpark and Google Cloud.
The visualizations provide key insights into user behavior on Twitter.

**Lessons learned**:
GCS integration simplifies large-scale data management.
PySpark is effective for distributed analysis but requires proper tuning for optimal performance.

**Future work**:
 Implement real-time analysis using Spark Streaming.
Explore additional datasets for comparative analysis.

### **References**
- [Sentiment140 Dataset](http://help.sentiment140.com/for-students/)  
  Official page for the Sentiment140 dataset, including details on how to use it.

- [PySpark Documentation](https://spark.apache.org/docs/latest/api/python/)  
  Official documentation for PySpark, describing its functionalities and available APIs.

- [Google Cloud SDK Documentation](https://cloud.google.com/sdk/docs/)  
  Official guide for Google Cloud SDK, including installation, configuration, and usage instructions.

   
