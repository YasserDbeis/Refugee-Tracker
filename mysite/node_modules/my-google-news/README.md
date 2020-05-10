Node.js - my-google-news
=====================


A module to search and scrape from **`google news`**. This is not sponsored, supported, or affiliated with Google Inc.

Installation
------------

    npm install --save my-google-news
    
API Example
-------

```js
var myGoogleNews = require('my-google-news');

myGoogleNews.resultsPerPage = 25; // max 100

var nextCounter = 0;
var googleQuery="trump"; //search Query

myGoogleNews(googleQuery, function (err, res){
  if (err) console.error(err)
  res.links.forEach(function(item){
    console.log(item.title + ' - ' + item.href)
    console.log(item.description + "\n")
  });
 
  //number of pages if you want more than one page
  /*if (nextCounter < 4) {
    nextCounter += 1
    if (res.next) res.next()
  }*/
});
```

Example Result
-------
```json
[
  {
    "title": "Trump Touts First 100 Days Record, Slams the Press in Campaign ...",
    "link": "http://www.nbcnews.com/storyline/president-trumps-first-100-days/trump-touts-first-100-days-record-slams-press-campaign-style-n752916",
    "description": "",
    "href": "http://www.nbcnews.com/storyline/president-trumps-first-100-days/trump-touts-first-100-days-record-slams-press-campaign-style-n752916"
  },
  {
    "title": "In Dueling Events, Samantha Bee and Hasan Minhaj Target Trump ...",
    "link": "https://www.nytimes.com/2017/04/30/arts/television/whcd-samantha-bee-hasan-minhaj-trump-fox-news-and-cnn.html",
    "description": "",
    "href": "https://www.nytimes.com/2017/04/30/arts/television/whcd-samantha-bee-hasan-minhaj-trump-fox-news-and-cnn.html"
  }
]
```
full result here : http://www.jsoneditoronline.org/?id=0340890093b40a3b27cbaa5af65a56cd

API TEST
-------
After testing we can do ~~**` 4 requests per minute `**~~ **`unlimited requests `** **`with max 100 results per request`** without being blocked by google captcha.

License
-------

Licensed under MIT. See `LICENSE` for more details.

Copyright (c) Hakim Mliki

Fill free to give **`a star ♥  `** and **`follow me ♥`** for more updates and news ;)
