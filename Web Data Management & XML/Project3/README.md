## A Movie Web Application

####Project Description:


As in Project #2, you will develop this project on the Omega web server and you will test the project on your PC/laptop using the Mozilla Firefox web browser. Login at omega.uta.edu using SSH and do the following:

cd public_html
wget http://lambda.uta.edu/cse5335/project3.tgz
tar xfz project3.tgz
cp project2/.htaccess project2/.htpasswd project3/
cd project3

The project3 directory contains 4 files: OAuth.php, proxy.php, yelp.html, and yelp.js. The library OAuth.php is used for authentication and should not be changed. All the web service requests to yelp.com should go through the proxy.php. See the example in yelp.js. Your project is to edit yelp.html and yelp.js as described in the description of the web application.

For this project, you will use the

Yelp API for Developers v2.0 from Yelp (more specifically, the Search API)
Geocoding from the Google Maps JavaScript API V3
Google Map Markers
To use Google Maps, you need to create a Google Account (if you do not have one) and get an API key. To use the Yelp API, you need to register for an API key from the Yelp API page. After you get the API key, you generate new API v2.0 token/secret from the Yelp API site, you put them in proxy.php, and you test your setup on your web browser by using the URL address:
http://omega.uta.edu/~xyz1234/project3/yelp.html
(use your username instead of xyz1234) and by pushing the Find button. It will display the the top 5 Indian restaurants in Arlington in JSON format.

You need to edit the HTML file yelp.html and the JavaScript file yelp.js. Your HTML web page must have 3 sections:

1. a search text area to put search terms with the button "Find"
2. a Google map of size 600*500 pixels, initially centered at (32.75, -97.13) with zoom level 16
3. a text display area

When you write some search terms in the search text area, say "Indian buffet", it will find the 10 best restaurants in the map area that match the search terms. They may be less than 10 (including zero) sometimes. The map will display the location of these restaurants as map overlay markers with labels from 1 to 10. The text display area will display various information about these restaurants. It will be an ordered list from 1 to 10 that correspond to the best 10 matches. Each list item in the display area will include the following information about the restaurant: the image "image_url", the "name" as a clickable "url" to the Yelp page of this restaurant, the image "rating_img_url" (1-5 stars), and the "snippet_text". When you search for new terms, it will clear the display area and all the map overlay markers, and will create new ones based on the new search.

How do you find the latitude and longitude of a restaurant to put an overlay marker on the map? You need to extract the postal address from the Yelp response and use Geocoding
How do you tell Yelp to search only on the displayed map? You need to "Specify Location by Geographical Bounding Box" on your Yelp search. You get this box from the Google Map.
Note that everything should be done asynchronously and your web page should never be redrawn completely. You need only one XMLHttpRequest object for sending a request to Yelp, since Google Maps is already asynchronous. You should not use JQuery.
