![](https://img.shields.io/maintenance/yes/2021)

<img src="https://github.com/DavidKentShirley/FI_Phase1_Project/blob/main/img/%F0%9F%98%BAPet_Store_analysis_using_Yelp_Fusion%F0%9F%98%BA.png?raw=true" width="1000" height="300">

### By David Shirley & Claire Dunne

## Check Out the map!!  [Pet Stores Map](https://sites.google.com/view/just-a-map/home?authuser=1 "Heading link")
## Overview
<img src="https://github.com/DavidKentShirley/FI_Phase1_Project/blob/main/img/NewBusiness.png?raw=true" width="1000" height="600">

## Data Collection
**Which Data?**<br />

**Helpful Data**<br />

* Yelp API: Stores, Parks, Vets.
* Population and household Income.<br />

**Not So Much**
* Explicit ownership
* Price points

It is important to go through the data once you collect it to see which is helpful for answering your question. Once the data has been filtered down to what you need you should do some basic analysis of it to see what factors there are and what you should comapre it to.

<img src="https://github.com/DavidKentShirley/FI_Phase1_Project/blob/main/img/chhart%203.png?raw=true&s=100" width="1000" height="600">

In the above graph we are comparing volume of stores in each area (Queens, Manhattan) in order to see if one are has a lot of pet stores and a low number of vets/dog parks. This will help give us an idea to the data needed. In this case we used Pet Stores and Vets and dropped dog parks since there were more vets in total. The reason we went with vets is because we found that there is a more likley chance of pet owners near vets and more of a variety of pets too.

## EDA Findings<br />



**Which Borough?**<br />
Let's look at ratings and sentiment in each borough to learn more about how shoppers there think about pet stores.<br />

<img src="https://github.com/DavidKentShirley/FI_Phase1_Project/blob/main/img/chart%204.png?raw=true" width="1000" height="600">

This shows the Pet Stores in each borough grouped by overall rating. You can see that a higher percentage of pet store in Queens have a 5 star rating than in Manhatan.<br />
This indicates that there is a gap in the market in Manhattan for what shoppers there perceive as a really good pet store.

## Recommendation #1 <br />
People in Manhattan are less satisfied with the available pet stores than people in Queens. There is a market opportunity there for a really good pet store.
#
**Pet Stores and Vets Correlation** <br />
Is there any Correlation between them?<br />
If you wish to determine the specific zip code in which to locate your business, how can you do that? How can you tell where pet owners are? <br />
Let's look at the correlation between pet stores and vets in each zip code for the two boroughs.

<img src="https://github.com/DavidKentShirley/FI_Phase1_Project/blob/main/img/image%20(2).png?raw=true" width="1000" height="650">

The correlation is much higher in Manhattan (0.79 - strong positive). This means that were you to open a pet store based on the existing number of vets in that zip code, the likelyhood of there being a supporting market for pet store is high.

## Recommendation #2 <br />
There is a much stronger link in Manhattan than in Queens between the number of vets and the number of pet stores in a zip code, perhaps because of car ownership discrepancies. We can use this to determine the zip code in which to locate a new pet store.
#
**Which Zip Code?**<br />
In this piece of analysis, we added the household income and population data for each zipcode. <br />
Bubble size represents household income, and the yellow colors are zips with the highest population. <br />
We also included a linear trendline, which shows the best match for number of pet stores as a function of the number of vets, based on the provided data, which in this case has a correlation coefficient of 0.68 (reduced due to the removal of zip codes with no vets).<br />

<img src="https://github.com/DavidKentShirley/FI_Phase1_Project/blob/main/img/image%20(3).png?raw=true" width="1000" height="650">
A clearly suitable zip code is that with eight vets and three pet stores. A fourth pet store would put it exactly on the trendline. It has a high population, and a high household income. <br />
From the data frame, this zip code is 10021, between Lenox Hill and the Upper East Side. <br />
However, zip codes can be irregular in shape. What if this zip code, while containing only three existing pet stores, has more just outside its boundaries? <br />
This is difficult to tell from numeric data, so instead we used folium to map the specific locations, and see whether this is the case. <br />



# Insert IMG

Since there are no pet stores immediately outside the boundaries of 10021, our expectation of there being sufficient market share for a fourth pet store in 10021 is valid.

# Recommendation #3<br />
The zip code 10021 has a high population, a high average household income, a high instance of vets, and one fewer pet stores than you might expect in Manhattan. We would locate a new pet store in this zip code.
