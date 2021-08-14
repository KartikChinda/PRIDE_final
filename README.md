# P R I D E ++ 
## Inspiration
Due to Covid-19, the most searched result on Google became how to make mental health better. Just imagine, it took an entire pandemic for us to make the betterment of mental health the most searched topic, while it has stayed **the highest ever searched topic** for people belonging to the LGBTQIA+ community, or the Women in Tech community, or just about any person who is different from the rest. Almost everyone felt attacked when the pandemics restrictions forced us to hide our faces, get constricted into our homes. But people from the LGBTQIA+ community constantly have to hide their identities, get restricted into their "closets" due to the restrictions put on by people. People from minorities have to keep their hands down, maintain their distance from an angry mob. 

But rather than the general support, why should it matter all that much to us, the " majority "? Then again, the age-old quote from 'How To Kill A Mockingbird' comes to my mind: 

> “You never really understand a person until you consider things from his point of view... Until you climb inside of his skin and walk around in it.” 

The same was the case for me until a very close friend of mine came out to me and told me all that she felt, all the dark, scary things she thought of. And well, let's just say, you can read about war all you want, but when you are standing on the battlefield fighting it, it is nothing like what you read. When you see a 16-year-old contemplating suicide just because she has a different orientation than what is the so-called "correct" orientation, you definitely think, **what are you doing to make this world just a bit better**? What is your contribution to give someone who is scared of their identity some peace, and most importantly, other people's experience, telling that someone that hey, it's gonna be okay. Embrace who you are, we have a community here, ready to help you. And we are not the only ones!

**P R I D E ++**, in all its glory, is an attempt to give the aforementioned people peace and make their mental health better. 


## What it does
**P R I D E ++** is a website, or rather, a thought process, that takes up tweets related to whatever is happening around in the world of LGBTQIA+, Women in Tech, and other minority communities, filters out all the bad things that you'd be better off without reading them, and gives to you, the confidence generating, the ecstatic good tweets and experiences of people that releases the much-needed Dopamine in you. Someone is genuinely happy when they see someone else succeed who has faced the same problems that the person is facing. It's the people making other people happy, we are just the medium. *Served with love, and a lot of Pride :D*


## How we built it
This entire project is basically divided into 5 parts: 
1. Extracting data (the top tweets) from various hashtags pertaining to the LGBTQ community, WIT community, coming out stories of different people, and a few more. 

**How this was done**: The tweets are extracted using Twitter's official API, Tweepy. Then using csv reading, the tweets which are collected are hence written into a .csv file. Code was written in such a way that x tweets can get stored in a single go, eliminating the retweets, and storing not just the tweet but the user, the timestamp of the tweet, the followers of the user and any attached link with the tweet.


2. Cleaning the data that we have extracted: The tweets that we usually get from twitter have been written to express someone's opinions. Hence, there are hashtags, @ mentions that are not really feasible to our vision. Along with that, there are a lot of unnecessary characters that need to be removed to get the actual message of the tweet. Hence, the next step was to clean the data and store it in a new data frame, so that we do not tamper with the original data. 

**How this was done**: This is where the 're' standard library and NLP came into use. Functions like regex, stop words etc. were created and used to clean up the raw data and provide tweets with unnecessary data iterms. Basically, whatever we didn't want into the tweet was entered as the first argument of the re.sub function, along with what we will replace it with and where are we performing the function. The cleaned data was then placed into a new dataframe, using Pandas. 


3. The tweets thus extracted and cleaned have all the information related to the hashtag. And hey, there can be no good without evil, can there? This means that there would be tweets that are both in favor of the community, and against it. This is why our next step is to perform a sentiment analysis of the data that we have collected, and segregate the positive tweets from the negative ones. 

**How this was done**: This is a very basic Sentiment analysis, so two functions were defined and performed on the data, which are namely the Subjectivity and the Polarity function. These both come from the TextBlob standard library. In simple words, if any particular sentence has a polarity greater than zero, then it is a positive sentiment. A polarity of zero signified a neutral sentiment and a negative polarity means a negative sentiment. Which is exactly how the analysis is defined and done. 

4. Once the sentiment analysis is done on the Tweets, the next step is to **store the tweets into a csv file** again, which is done easily by storing only the tweets which have their analysis column as positive. Thus, at the end of the sentiment analysis, you get all the tweets related to a hashtag that are positive in nature. 

5.The next step is to **build the website**, which is done using HTML, CSS, JS, React JS and some bootstraps, and creating divs to store the texts of the tweets and displaying them on the screen for nothing but feel good vibes.  

## Challenges we ran into
Nothing truly good ever came easy, right? These are some of the challenges we faced while making the project: 
1. While extracting the tweets from Tweepy, the emojis are converted into the utf-8 code for the emojis, which leads to the tweets having texts instead of emojis. For example, instead of seeing an orange heart, you would see the words 'orange heart'. This was replaced either manually, or the emoji text was removed. 

2. Some of the tweets that are actually positive in nature, are credited as neutral or even negative, due to some words like cancer, destroying etc having negative points. This can be resolved, but since time was limited, the model didn't get trained to a good capacity. 

3. One cannot import and store images from Tweepy directly, so if any tweets had images attached with them, we had to copy up the entire links of the tweet. 

4. This was an *interesting challenge*. As mentioned earlier, the data cleaning process removes the hashtag symbol from the text. Now, if you want to remove the entire hashtag phrase, you would end up with missing phrases in between the tweet, or if you only remove the hashtag symbol, then you would end up with extra phrases at the end :p. 

6.One of the difficulties we faced were that we had to copy the tweets manually into HTML divs. We knew how one can display a csv file as a table in HTML, but we wanted each column to get assigned different divs for some class, and we weren’t able to understand how one can do that. It required something in Ajax, to the best of my knowledge, but we did not have enough time to learn that. 


## Accomplishments that we're proud of
First and foremost? That we took a step for the betterment of the LGBTQIA+ and the other communities. We are proud of the fact that when we looked over all the tweets that spoke against a community that just wants to live in peace, we really felt like change was necessary. And when we saw all the positive tweets, we felt empowered. We felt good, that **change was coming, stronger than ever**. 

And honestly, we are happy to be even a small contribution to bring that change. 

Technically, these are a few of the accomplishments we are proud of: 
1. Neither I nor my teammate has actually made projects that resorted to Machine Learning, so we had to learn the entire thing from scratch. And to not only learn but also implement Sentiment analysis and usage of APIs is something we are very proud of. 

2. Me and my teammate knew how to show an excel file as a HTML document, but we weren't aware of how one could extract a data from a column of a csv file and enter it automatically as divs in HTML, so learning how to do that was something both me and my teammate were amazed at, even though we couldn’t implement it properly. We also learnt a lot of cool stuff like CSS glassbox, and I got to use wordcloud and Canva!

3. This was **one of the best accomplishments** we achieved, and one of the most fun challenges we had to overcome (It definitely wasn't fun when our code was giving errors continuously haha). So, what happened was that while extracting the tweets, we had written the code such that there was a row break between each tweet. For example, the tweets were stored in row 1, 3, 5, 7 and so on while rows 2, 4, 6 and so on were empty. And data cleaning can't be done on empty data, right?  So, it took us a good amount of time to figure out the error and how to rectify it. But as you might know as well, reader, nothing is more satisfying than that code getting compiled without any errors!

4. This is my (Kartik's) first project, so I am pretty happy about it :p. 


## What we learned
While we got better at Website Development using HTML, CSS, Javascript and React, we learned a whole new deal about Machine Learning and Sentiment Analysis using Python, how one can use API's and store information in files, cool effects like Glassbox etc. Most importantly, we learned how to effectively manage time and divide tasks, so that everything gets completed in time.
And it did not hurt to learn about all the amazing, amazing people who are making strides in the LGBTQ+ community, how people are in support of the community, and how the world really might be a better place someday. It is like Captain Raymond Holt says,

> "Every time someone steps up and says who they are, the world becomes a better, more interesting place."


## What's next for P R I D E ++
You name it! If we would sum it up in one word, we would say, **Automation**! The first thing would be to definitely train the model better. Also, why would we just limit ourselves to our website? Why not go over to the mother source of where it all comes from - Twitter? We can easily **make up an automated bot** that takes up all the positive tweets that we have stored and uploads them as a tweet on the Twitter handle we would create for **P R I D E ++** on a daily or even an hourly basis. The next step in automation would definitely be how we can upload the columns from our csv file directly as html divs. 

Other than that, our website could use a lot of work, other than just making people's mental health, we can help them. We can **provide articles and experiences** of other parents for some mom and dad to read whose child just came out of the closet. Similarly, we can provide experiences of other people about how they came out, and provide the young buds the much-needed confidence and self-acceptance that they need. And of course, providing more and more and more stuff that is nothing but a good boost to start the day, nothing but positivity and joy! 

**For other minority communities**, we will be providing them groups where there are more people from different minorities looking for friends, or just someone to hang out with and make people come even closer by organizing outdoor games, bar nights etc. Drives can be held, offline, in different schools that teach students right from an early age that having a different orientation is nothing to be ashamed of, and not only this, also how people from different minorities must be treated as the people from the majority and at the basic blocks of life, we are all just humans, trying to make it to another day!

The website would also need a lot of **SEO optimization**. We will be updating the Schema's of the different articles/tweets that we have or will write in the future. Rankings of the website will be vastly increased, so the website can be accessible to everyone who is just looking for some good news. Collabs will be done by brands, and pages like Upworthy, and celebrities that are openly a part of the LGBTQ+ community. 

As far as revenues are considered (if they will be), two of the direct ways to generate revenue and keep the website alive, apart from donations could be Social media marketing and Google Adsense on a whole. 
