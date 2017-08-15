# linkedin-scrapper
python script to help submitting resume; potential machine learning algo to get the right position for user

# Overview
It is harder and harder to find a job for financial engineers/mathematic finance, especially everyone wants to be a quant. 

From my expierence, the key to become a good quant is to strength one's math/computer science/statistc skills. However, even if you have a strong quant background, it is really tricky to find your first job. You need to send hundreds and throusands of resume and it is really time killing. I hope this repo can help the fresh graduated students save some time strenghth their quant backgound, instead of submitting resume like a machine.

# Things in mind
1. figure out how to submit resume automatically through linkedin quick apply
2. scrapping linkedin recruiter email address to send cold emails
3. build a supervised learning algorithm to decide if a position fit a candidate or not

# Step 1. scrapping javascript webpage
Nowadays, a lot of webpage is using java script to pop up data; if we simply open url by urlopen, we will not getting the data fetching by script. One can take a look at this video, it is really helpful to understand:
https://www.youtube.com/watch?v=FSH77vnOGqU

Thus, from my understanding, we need a 'render' to simulate that we are actually loading the webpage. Thus, I created `render.py` so that you guys can start up with.


# Step 2. fetching the right content
1. bs4
2. re
