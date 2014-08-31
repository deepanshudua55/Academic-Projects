// Student Name: Sarvesh Sadhoo (100090763)
// Project 2 : A Movie Web Application
//----------------------------------------------------------------------------------------------------------------------------------------    

// This function lists all the movies according to search criteria!

    var json;
    function sendRequest () {
      var xhr = new XMLHttpRequest();
      var query = encodeURI(document.getElementById("form-input").value);
      xhr.open("GET", "proxy.php?method=/3/search/movie&query=" + query);
      xhr.setRequestHeader("Accept","application/json");
      xhr.onreadystatechange = function () {
        if (this.readyState == 4) {
        json = JSON.parse(this.responseText);
        var jsonArray = json.results;
        var tablecontents = "";
        tablecontents = "<table>";
        for(var i=0;i<jsonArray.length;i++){
          tablecontents += "<tr>";
          tablecontents += "<td>" + "&nbsp" +"</td>";
          var id_value = json.results[i].id;
          tablecontents += "<td onclick='javascript:movie_info("+json.results[i].id+")'>" + json.results[i].title + "</td>";
          tablecontents += "<td>" +  "&nbsp&nbsp&nbsp&nbsp" +"</td>";
          tablecontents += "<td>" + json.results[i].release_date + "</td>";
          tablecontents += "</tr>";
          
        }
      tablecontents += "</table>";
      document.getElementById("tablespace").innerHTML = tablecontents;
      }

    };
    xhr.send(null);
    }
//----------------------------------------------------------------------------------------------------------------------------------------   
// This function gest movie info on Tittle, Overvie, Generes & Poster!

   function movie_info(id_value){
    var movie_id = id_value;

    var xhr = new XMLHttpRequest();
    var query = encodeURI(document.getElementById("form-input").value);
    xhr.open("GET", "proxy.php?method=/3/movie/" + movie_id);
    xhr.setRequestHeader("Accept","application/json");
    xhr.onreadystatechange = function () {
       if (this.readyState == 4) {
          var json = JSON.parse(this.responseText);
          var str = JSON.stringify(json,undefined,2);

          var movie_title = json.original_title;
          document.getElementById("title").innerHTML = movie_title;

          var movie_overview = "Overview: ".bold() + json.overview;
          document.getElementById("overview").innerHTML = movie_overview;

          var movie_poster = json.poster_path;
          movie_poster =  "http://image.tmdb.org/t/p/w185" + movie_poster;
          document.getElementById("poster").src = movie_poster;

          var movie_genres = "Genres: ".bold();
          if (json.genres != ""){
            for (item in json.genres){
            movie_genres += (json.genres[item].name) + ", ";
            }
          }else{
            movie_genres = "Genres: ".bold() + "Sorry no genres for this movie! ".fontcolor("red")
          }
          
          movie_genres = movie_genres.substring(0, movie_genres.length-2);
          document.getElementById("genres").innerHTML = movie_genres;
          movie_cast(id_value);
       }
    };
   xhr.send(null);
   }
//----------------------------------------------------------------------------------------------------------------------------------------   
// This function gets the cast of the movie!

function movie_cast(id_value){
    var movie_id = id_value;

    var xhr = new XMLHttpRequest();
    var query = encodeURI(document.getElementById("form-input").value);
    xhr.open("GET", "proxy.php?method=/3/movie/" + movie_id + "/credits");
    xhr.setRequestHeader("Accept","application/json");
    xhr.onreadystatechange = function () {
    if (this.readyState == 4) {
          var json = JSON.parse(this.responseText);
          var str = JSON.stringify(json,undefined,2);
          console.log(json)
          
          var movie_cast = "Cast: ".bold();
          if (json.cast != ""){
            for (i = 0; i <= 4; i++){
            movie_cast += (json.cast[i].name + ", " );
            }
          }
          else{
            movie_cast = "Cast: ".bold() + "Sorry no cast for this movie! ".fontcolor("red")
          }
          movie_cast = movie_cast.substring(0, movie_cast.length-2);
          document.getElementById("cast").innerHTML = movie_cast;
       }
   };
   xhr.send(null);
}

//----------------------------------------------------------------------------------------------------------------------------------------   

