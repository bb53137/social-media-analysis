from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lower, regexp_extract, count, desc, date_format
import matplotlib.pyplot as plt
import time  
from datetime import datetime  

start_time = time.time()
print(f"Script started at: {datetime.now()}") 


spark = SparkSession.builder.appName("Sentiment140CloudAnalysis").getOrCreate()

data_path = "gs://macro-nuance-210216/enlarged_sentiment140.csv"  
print("Loading Sentiment140 dataset from Google Cloud Storage...")
df = spark.read.csv(data_path, header=False, inferSchema=True)
print(f"Dataset loaded at: {datetime.now()}")

print("Preview of dataset:")
df.show(5)

df = df.selectExpr("_c0 as sentiment", "_c2 as created_at", "_c3 as text")

df = df.withColumn("sentiment", col("sentiment").cast("string"))

print("Dataset schema:")
df.printSchema()

print("Analyzing hashtags...")
hashtags = df.withColumn("hashtag", regexp_extract(lower(col("text")), r"#(\w+)", 1))
top_hashtags = (
    hashtags.groupBy("hashtag")
    .agg(count("*").alias("count"))
    .filter(col("hashtag") != "") 
    .orderBy(desc("count"))
    .limit(10)
)

print("Analyzing sentiment distribution...")
sentiment_count = df.groupBy("sentiment").count()

print("Analyzing activity over time...")
df = df.withColumn("hour", date_format(col("created_at"), "HH"))
activity_by_hour = df.groupBy("hour").count().orderBy("hour")

output_dir = "gs://macro-nuance-210216/output_proyect/" 
print("Saving results to Google Cloud Storage...")

top_hashtags.write.mode("overwrite").csv(output_dir + "top_hashtags.csv", header=True)
sentiment_count.write.mode("overwrite").csv(output_dir + "sentiment_count.csv", header=True)
activity_by_hour.write.mode("overwrite").csv(output_dir + "activity_by_hour.csv", header=True)
print(f"Results saved at: {datetime.now()}")
print("Generating visualizations...")

top_hashtags_pd = top_hashtags.toPandas()
sentiment_pd = sentiment_count.toPandas()
activity_pd = activity_by_hour.toPandas()

plt.figure(figsize=(8, 5))
plt.bar(top_hashtags_pd['hashtag'], top_hashtags_pd['count'])
plt.title("Top 10 Hashtags")
plt.xlabel("Hashtag")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("/tmp/top_hashtags.png") 

plt.figure(figsize=(8, 5))
plt.bar(sentiment_pd['sentiment'], sentiment_pd['count'], color=['green', 'gray', 'red'])
plt.title("Sentiment Distribution")
plt.xlabel("Sentiment")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("/tmp/sentiment_distribution.png")

plt.figure(figsize=(8, 5))
plt.plot(activity_pd['hour'], activity_pd['count'], marker='o')
plt.title("Tweet Activity by Hour")
plt.xlabel("Hour of the Day")
plt.ylabel("Tweet Count")
plt.grid()
plt.tight_layout()
plt.savefig("/tmp/activity_by_hour.png")

import os
os.system("gsutil cp /tmp/top_hashtags.png gs://macro-nuance-210216/output/")
os.system("gsutil cp /tmp/sentiment_distribution.png gs://macro-nuance-210216/output/")
os.system("gsutil cp /tmp/activity_by_hour.png gs://macro-nuance-210216/output/")

print("Visualizations uploaded to Google Cloud Storage.")

end_time = time.time()
print(f"Script ended at: {datetime.now()}")  
print(f"Total Execution Time: {end_time - start_time} seconds") 
