# surfs_up

## Overview of the analysis:
surfs_up analysis is based on a business plan analysis, in-terms of investment, favorable weather conditions, investors, business success probability of a Surf and Shake shop, serving surfboards and ice cream to locals and tourists. We partners with W. Avy, who is famous for his love fo surfing and we will properly analyze data and run some analytics on a weather data set W. Avy has from the very island where we would like to open our first shop. 

For this analysis W. Avy wants more information about temperature trends before opening the surf shop. Specifically, he wants temperature data for the months of June and December in Oahu, in order to determine if the surf and ice cream shop business is sustainable year-round. 

Analysis code is attached below:

[Surf_Up_Challenge](/SurfsUp_Challenge.ipynb)

![surf](https://user-images.githubusercontent.com/111251560/198156217-afc93560-f16c-45aa-ba94-ea1c323e2cb9.png)

In order to access the data in SQLite database, we used SQLAlchemy to connect and make queries to pull the necessary data for our analysis. Tools used for the analysis are as follows:
- Pandas
- Matplotlib
- SQLite
- Jupyter notebook
- PostgreSQL

**Importing dependencies:**

![SQLAlchemy](https://user-images.githubusercontent.com/111251560/198157093-aab342b4-bb60-42ef-bdab-f88a50026e0d.png)

## Results: 

- ** Precipitation results**
When we pulled the data, we first looked at the the precipitation for a one year timeframe. We reviewed the activity from August 23, 2016 - August 23, 2017. The mean was 0.177279 for 2021 observations, with min and max precipitation value of 0.00 and 6.700000 respectively.

![precipitation](https://user-images.githubusercontent.com/111251560/198177191-3d8d3fc2-e130-4f87-b539-63aab8e060cf.png)

![precipitation_stats](https://user-images.githubusercontent.com/111251560/198177176-cc285f9b-c182-4e45-b80b-9b4fa9e50010.png)

- **June Results** 
In June we had a total count of 1700, mean of 74.944118, min of 64.0 and max of 85.0.

![june_stats](https://user-images.githubusercontent.com/111251560/198178363-63716a8b-211f-437b-bf7b-e90aea73c341.png)

- **December Results**
In December we had a total count of 1517, mean of 71.041529, min of 56.0 and max of 83.0

![december_stats](https://user-images.githubusercontent.com/111251560/198178465-0c108d25-0b5f-4b83-84eb-a9b9ef45239f.png)

Summary:

In short, Oahu is a great place to invest in a surf-and-ice cream shop. The weather is pleasant and moderate year-round. The lows are rarely too low and the highs are rarely too high, most days are clear. By looking at the precipitation and temperature outcomes for the month of June and Dec we could say that Oahu is a great place to invest in this business the precipitation outcomes of Oahu is as follows:

### June Precipitation 
For 2010 to 2016 is as follows:

![june_plot](https://user-images.githubusercontent.com/111251560/198185113-99a2ae2b-2185-4f2f-8791-0796e84c0d67.png)

### December Precipitation
For 2010 to 2016 is as follows:

![dec_plot](https://user-images.githubusercontent.com/111251560/198185186-c0b471d8-6c67-4d3d-95c7-449e1452ab97.png)

### Additional queries:

- **June**

![june_query](https://user-images.githubusercontent.com/111251560/198185344-15eb4c0f-8420-420b-89ff-21153ee182cf.png)

- **December**

![dec_query](https://user-images.githubusercontent.com/111251560/198185370-1d803373-5da6-405a-8ae0-954e247dd4e2.png)
