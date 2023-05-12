# Documentation

## Pipeline overview

An e-commerce company requires that users sign up for a membership on the website in order to purchase a product from the platform.

The purpose of this pipeline is to process those membership applications submitted by users on an **hourly interval**.

## Components

The pipeline consists of the following components:

1. Data Ingestion
   1. Applications are batched into ******\*\*******varying******\*\******* number of datasets and dropped into a folder on an **hourly basis**.
2. Data Cleaning
   1. Split **\*\*\*\***name**\*\*\*\*** into first_name, last_name
   2. Format birthday field into **YYYYMMDD**
   3. Remove any rows which do not have a **name** field (to consolidate, put into separate folder as unsuccessful applications
3. Data validity checks: If any of this doesnt pass, the entry is considered an **unsuccessful application**
   1. Application number is **8 digits**
   2. Applicant is **over 18 years old** as of 1 jan 2022
   3. Applicant has a **valid email**
4. Membership ID Generation: <last*name>*<hash(YYYYMMDD)>
5. Data output:
   1. Successful applications in one folder
   2. Unsuccessful applications dropped into a **separate folder**

## Schedule

The pipeline will run every hour, at the beginning of the hour using the **cron** scheduler.
This is done through crontab scheduler by following these steps:

1. Open crontab editor by running command 'crontab -e'
2. Add new line to crontab file to include the scheduling of the bash script to run hourly

```jsx
0 * * * * /bin/bash/ /path/to/bash/process_memberships.sh
```

3. Save and exit the crontab editor. The new cron job will take effect immediately.
