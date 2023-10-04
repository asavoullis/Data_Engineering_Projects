# YouTube Ad Campaign Data Engineering Project

## Project Overview

This project aims to execute an end-to-end data engineering process, from data acquisition to building a final dashboard using AWS cloud architecture. The objective is to assist a client or company in understanding how to categorize YouTube videos based on comments and stylistic factors and identify the factors that affect a video's popularity. This information will help the client make informed decisions before investing in a YouTube ad campaign.
This project aims to securely manage, streamline and perform analysis on the structured and semi-structured YouTube videos data based on the video categories and the trending metrics.

## Project Goals

1. Data Ingestion — Build a mechanism to ingest data from different sources (AWS Glue).
2. ETL System — We are getting data in raw format, transforming this data into the proper format (AWS LAMDA).
3. Data lake — We will be getting data from multiple sources so we need a centralized repo to store them (AWS S3).
4. Scalability — As the size of our data increases, we need to make sure our system scales with it.
5. Cloud — We can’t process vast amounts of data on our local computer, so we need to use the cloud. In this case, I will use AWS.
6. Reporting — Build a dashboard to get answers to the questions we asked earlier.

## Services we will be using

1. Amazon S3: Amazon S3 is an object storage service that provides manufacturing scalability, data availability, security and performance. I will use it as a central repository for storing the data I will use.
2. AWS IAM: This is nothing but identity and access management which enables us to manage access to AWS services and resources securely. I will utilize AWS IAM to create roles and users to ensure that all users and services have the correct and necessary permissions to execute tasks and communicate with other AWS services and features securely.
3. QuickSight: Amazon QuickSight is a scalable, serverless, embeddable, machine learning-powered business intelligence (BI) service built for the cloud.
4. AWS Glue: A serverless data integration service that makes it easy to discover, prepare and combine data for analytics, machine learning and application development.I will use it to create a data catalog and perform ETL (Extract, Transform, Load) operations on the YouTube data that I will be using.
5. AWS Lambda: Lambda is a computing service that allows programmers to run code without creating or managing servers. I will leverage Lambda functions to create ETL processes and perform data transformations.
6. AWS Athena: Athena is an interactive query service for S3 in which there is no need to load data, it stays in S3. I will use Athena for querying and analyzing the data.

These AWS services and features will play a crucial role in building a secure, scalable and efficient data engineering pipeline for our YouTube ad campaign data project.

## Dataset Used

This Kaggle dataset contains statistics (CSV files) on daily popular YouTube videos over the course of many months. There are up to 200 trending videos published every day for many locations. The data for each region is in its own file. The video title, channel title, publication time, tags, views, likes and dislikes, description and comment count are among the items included in the data. A category_id field, which differs by area, is also included in the JSON file linked to the region.

**Dataset Link:** [YouTube Trending Videos Dataset](https://www.kaggle.com/datasets/datasnaek/youtube-new)

## Architecture Diagram

![Architecture Diagram](architecture.jpeg)

# YouTube Ad Campaign Data Engineering Project

## Project Overview

This project aims to execute an end-to-end data engineering process, from data acquisition to building a final dashboard using AWS cloud architecture. The objective is to assist a client or company in understanding how to categorize YouTube videos based on comments and stylistic factors and identify the factors that affect a video's popularity. This information will help the client make informed decisions before investing in a YouTube ad campaign.

### Why YouTube?

YouTube is the second most visited website globally, making it a powerful advertising channel.
Understanding the YouTube audience and video trends can provide valuable insights for effective advertising campaigns.

## Project Goals and Success Criteria

1. Collect data from multiple sources.
2. Design and implement an ETL (Extract, Transform, Load) pipeline.
3. Build a scalable data lake using Amazon S3.
4. Utilize AWS cloud services for data processing.
5. Create a dashboard for data visualization and analysis.

## What You Will Learn

In this project, I have gained knowledge and experience in the following areas:

- Building a data lake using Amazon S3.
- Handling semi-structured and structured data.
- Understanding the difference between data lakes and data warehouses.
- Designing and partitioning data tables.
- Utilizing AWS services, including SNS (Simple Notification Service) and IAM (Identity and Access Management).
- Writing SQL queries with Amazon Athena.
- Ingesting data incrementally.
- Schema design for data.
- Creating a dashboard for data visualization.
- Real-time data processing and its importance.
- Challenges of working with big data.

## Author

Charilaos A Savoullis
