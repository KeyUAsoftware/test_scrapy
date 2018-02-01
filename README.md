# test_scrapy

## Task is:

We want you to develop an app using Python and Scrapy framework to collect some information from https://www.houzz.jp/professionals and answer some questions:

1. How many professionals profiles actually exists and can be discovered and processed?
2. Is it any other ways to review each profile rather then just navigating through the listings?
3. How long it may take to process all profiles using Scrapy engine and store the output to MongoDB?
4. Is it any other ways how you can get professional contact information, i.e email?
5. What will you do if the target website contains some antibot collecting software installed, preventing or making harder to get required info? (DistillNetworks, CloudFlare and etc.)

Objective.

Please process 5.000 of profiles and output the following as JSON array per profile:

1. Area of activity/Category
2. Person contact name
3. Address (separated into street, city, prefecture, postal code fields)
4. Geo coordinates based on location (i.e [Long,Lat])
5. Company name
6. Service cost/price
7. Number of reviews
8. Number of projects done
9. Website
10. Email
11. Profile URL
12. Phone number (E164 format)
13. Pro rating

Scraper should use proxy connection and store each profile into MongDB. Also please create log table in Mongo containg real data while the scraper is running:
1. Start datetime
2. Finish datetime
3. Total time spent
4. Profiles added
5. Profiles total
6. Errors count
7. Retries count

## Answers:

1. 2960 profiles were discovered and processed
2. For current website no, but if website use open API we can send requests where, sometimes we can get information by parsing js scripts
3. For me it takes 6,5 minutes
4. From website of company, if it exists
5. Use proxy, bigger delay between requests.
