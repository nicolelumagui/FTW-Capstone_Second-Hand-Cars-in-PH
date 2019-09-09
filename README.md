![Introduction](https://github.com/nicolelumagui/FTW-Capstone_Second-Hand-Cars-in-PH/blob/master/Images/Team%20Money%20Capstone%20190810-01.png)

<br>

# About
**Second-Hand Cars in the PH: A Buyer's Guide** is a capstone project presented for [FTW Foundation](https://www.ftwfoundation.org) Data Science Program that predicts the prices of second-hand/used cars in the Philippines. This is created by Elyse Go, Nicole Lumagui, Bernadette Misa and Jero Santos, and sponsored by [Carlove](https://www.carlove.ph/).

<br>

### See our model in action here: http://nicolelumagui.pythonanywhere.com/
*(This site will be disabled on Monday 25 November 2019)*

<br>

# Introduction
**Traffic. Congestion. Carmaggedon.**
Metro Manila is one of the densest cities. What is one of the government’s way of solving this? The TRAIN Law. Specifically, Auto Tax Reform.
Modeled after Singapore, TRAIN Law is put in place to limit “new” cars on the road. Because of this, people are discouraged to buy brand new cars to help alleviate traffic. And because of this, a window of opportunity opens: **an increase in market activity for second-hand cars**.

Buying used cars has many advantages:
  <ol>
    <li>More savings</li>
    <li>Cheaper insurance cost</li>
    <li>Slower depreciation</li>
    <li>Extended warranty</li>
    <li>Good for the environment</li>
  </ol>
  
But there are also risks:
<ol>
  <li>Unknown reliability or treatment</li>
  <li>More frequent maintenance</li>
  <li>Hard to find an exact match of what you want</li>
  <li>Untouched warranty</li>
  <li>Lemon Car / Overpriced Car</li>
</ol>
  
<br>

### *How can we help consumers in their journey of buying a second-hand car?*
## By empowering them with information derived from Machine Learning!

<br>

# Process Overview
1. Scraped data from the websites Carmudi, Philkotse, Priceprice Auto and AutoSearch Manila
1. Joined the scraped data sets and cleaned the data
1. Used K-Nearest Neighbors to impute for mileage 
1. Exploratory Data Analysis
1. Tried Decision Trees to get the first glance on feature importance
1. Used Random Forest Regressor then XGBoost to predict the price of second-hand cars
1. Created Web App using Django and applying the pickled Random Forest Regressor model on backend

<br>

# Dataset
<p>
The data used for this project are car listings scraped from <a href="https://www.carmudi.com.ph/">Carmudi</a> and <a href="https://philkotse.com">Philkotse</a>. While, the retail price of the cars are scraped from <a href="https://ph.priceprice.com/cars/">Priceprice Auto</a> and <a href="http://www.autosearchmanila.com/">AutoSearch Manila</a>.
</p>

## Features:
<ul>
  <li>
    Age of car
  </li>
  <li>
    Retail Price of Car
  </li>
  <li>
    Mileage of Car in km
  </li>
  <li>
    Car Brand/Make - 
    <i>Toyota, Honda, Hyundai, Ford, etc...</i>
  </li>
  <li>
    Car Model - 
    <i>Civic, Adventure, Ranger, Vios, etc...</i>
  </li>
  <li>
    Car Body Type - 
    <i>Saloon/Sedan, Hatchbak/Wagon, SUV, MPV/AUV, etc...</i>
  </li>
  <li>
    Fuel Type of Car - 
    <i>Diesel, Gasoline, Electric</i>
  </li>
  <li>
    Transmission Type of Car - 
    <i>Automanual, Automatic, CVT, Manual, Shiftable Automatic</i>
  </li>
  <li>
    Car's Color
  </li>
  <li>
    Seller Type - 
    <i>Individual/Private Owner or Dealer</i>
  </li>
  <li>
    Seller's Location/City
  </li>
  <li>
    Age of Post/Listing in Days
  </li>
</ul>

<br>

# Results / Output
## Machine Learning Model
**Model** | **Cross-Val Score** 
------------ | -------------
**XGBoost** | 79.63%
**Random Forest Regressor** | 80%

### Graph of the results of Random Forest Regressor model
![Graph of the Results of Random Forest Regressor model](https://github.com/nicolelumagui/FTW-Capstone_Second-Hand-Cars-in-PH/blob/master/Images/Team%20Money%20Capstone%20190810-25.png)

### Feature Importance
![Feature Importance based on Random Forest Regressor model](https://github.com/nicolelumagui/FTW-Capstone_Second-Hand-Cars-in-PH/blob/master/Images/Team%20Money%20Capstone%20190810-37.png)

<br>

## Web App Prototype
![A Look on the Web App Prototype](https://github.com/nicolelumagui/FTW-Capstone_Second-Hand-Cars-in-PH/blob/master/Images/Team%20Money%20Capstone%20190810-39.png)

<br>

# Recommendations
<ul>
  <li>Add more data from other marketplaces and banks, and compile a dataset with balanced distribution of car brands and models.</li>
  <li>Improve user interface of web app.</li>
  <li>More fine tuning of the model.</li>
  <li>Add more features, such as number of doors.</li>
</ul>

<br>

# References
<ul>
  <li>https://www2.bc.edu/thomas-chemmanur/phdfincorp/MF891%20papers/Ackerlof%201970.pdf</li>
  <li>https://www.business-standard.com/article/news-cd/5-reasons-why-you-should-buy-a-used-car-116051000836_1.html</li>
  <li>https://www.investopedia.com/articles/pf/07/neworusedcar.asp</li>
  <li>https://www.carmudi.com.ph/journal/pros-and-cons-of-buying-a-used-or-new-car/</li>
</ul>

<br>

# Contact Us
<ul>
  <li>
    Elyse Go (<a href="http://github.com/fur-elyse">@fur-elyse</a>)<br>
    <a href="mailto:elysekatrina.go@ftwfoundation.org">elysekatrina.go@ftwfoundation.org</a>
  </li>
  <li>
    Nicole Lumagui (<a href="http://github.com/nicolelumagui">@nicolelumagui</a>)<br>
    <a href="mailto:nicole.lumagui@ftwfoundation.org">nicole.lumagui@ftwfoundation.org</a>
  </li>
  <li>
    Bernadette Misa (<a href="http://github.com/bernablues">@bernablues</a>)<br>
    <a href="mailto:bernadette@ftwfoundation.org">bernadette@ftwfoundation.org</a>
  </li>
  <li>
    Jero Santos (<a href="http://github.com/jerosantos">@jerosantos</a>)<br>
    <a href="mailto:jero@ftwfoundation.org">jero@ftwfoundation.org</a>
  </li>
</ul>

<br>

# Special Thanks
<ul>
  <li>
    <a href="https://www.ftwfoundation.org">FTW Foundation community</a>
  </li>
  <li>
    <a href="https://www.carlove.ph/">Carlove</a>
  </li>
</ul>
