# Cycl.co

Matthew Sarni, November 2015

## Overview

View at cycl.co

The central concept of bike sharing programs is to provide
free or affordable access to bicycles for short-distance trips in an urban area
as an alternative to motorised public transport or private vehicles, thereby
reducing traffic congestion, noise, and air pollution.

Beginning in 2013, the Bay Area Bike Share has experienced continued growth
and has meticulously kept track of its data.

![alt text](https://github.com/mattsarn/cycl.co/blob/master/webapp/static/dist/img/clustered.png "Clusters")

Focusing on 2014 and San Francisco proper, this project aims
to create personalities for bike trips in an effort to analyze and
better understand bike share use.

The model is built to cluster bike share bicycle trips by a number of determined features. 
Data is just a story waiting to be told, and the aim of this project is to provide some insight
for cities and metropolitan areas looking to adopt a similar program. It is supposed to help
them understand who is using the bicycles and why.

##Future Steps
I'd like to add an interactive map in the future, with visualizations by cluster and a time series
analysis. A demand prediction program has been used for cities like Chicago to help solve
the balancing problem, but I may include my own just for some extra practice.

##Packages Used
* Pandas
* Seaborn
* NumPy
* scikit-learn