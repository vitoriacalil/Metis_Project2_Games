# Metis Project 2 - Predicting Video Games Sale

Below is a list with explanation of all files in this repo.

## 1st file:
*sgames.py*
Scrapy spider used to scrap data from vgchartz.com

## 2nd file:
*DataAcqui.ipynb*
In this notebook, I cleaned previously scraped data, and merged a dataset that I downloaded from Kaggle.
Some CSV file were created, and they will be used for future modeling.

## 3rd file:
*first_model(scrapy).ipynb*
In this notebook I started experimenting linear regression only with the data that I had scraped from vgchartz. At this point my results were not satisfactory, and I noticed that I would need more data to incorporate my model.

## 4th file:
*second_model(original).ipynb*
Here I merged scraped data with data from Kaggle data set.
My results were significantly better, and much of it was caused by the 'rank position' feature.

## 5th file:
*third_model(all_quart).ipynb*
After analyzing my dataset and my problem, I noticed that I would have to come up with new features to improve my model.
Having some domain knowledge and after analyzing Lasso coefficients, I engineered some features, most were about the Game Publisher, which plays a huge effect on the model.
All the work affected my model positively, and I could see better R2 scores.

## 6th file:
*fourth_model(above_median).ipynb*
Here I used the same methods and features as the previous model, I only eliminated games that were published by smaller publishers - by smaller I mean, Publishers that has produced less than the median number of games that is published by a company.
Although my results were not as good as in the previous model, this modelling makes more sense because my 'client' has more interest in games produced by big companies.

## 7th file:
*fifth_model(fourth_w_bias).ipynb*
In this last notebook I changed some categories of features, and this was based on my domain knowledge. The main objective of this transformations was to make the modeling scenario closer to the real scenario.

## 8th file:
*Predicting_Games_Sale.pdf*
Slides presented
