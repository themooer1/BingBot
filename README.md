# BingBot
A simple Bing Rewards automation program written in Python 3 with support for both mobile and desktop searches.

Simply fill in the values at the top of the file with Bing credentials, adjust the search numbers to you liking, 
and watch (or don't) as it searches Bing with randomly generated queries for you.

<h1>Chromedriver</h1>
<strong>Windows Users</strong><br>
<article>Make sure that the chromedriver exe is in your python directory or this will not work.<br>  
<strong>Everyone Else</strong><br>
<article>Install chromedriver through brew on Mac OS, or your package manager on Linux.</article><br>
<h1>Stack Exchange Search</h1>
<article>BingBot can instead of generating random queries, scrape queries from Stack Exchange which are more realistic.  To use this function, go to <strong><a href="https://stackexchange.com">https://stackexchange.com</a></strong>, scroll to the bottom, right click <em>Hot Questions Feed</em>, and paste the link into the <em>StackExchangeFeed</em> variable at the top of the script.  Questions will automatically be pulled from Stack Exchange instead of internally generated.
