import movie
import fresh_tomatoes

# Instantiating variables of the class Movie
toy_story = movie.Movie(
    "Toy Story",
    "A cowboy doll is profoundly threatened and jealous"
    " when a new spaceman figure supplants him as top toy in a boy's room.",
    "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
    "https://www.youtube.com/watch?v=KYz2wyBy3kc"
    )

toy_story_2 = movie.Movie(
    "Toy Story 2",
    "When Woody is stolen by a toy collector, Buzz and his friends vow to"
    "rescue him, but Woody finds the idea of immortality in a museum"
    " tempting.",
    "http://www.impawards.com/1999/posters/toy_story_two_xlg.jpg",
    "https://www.youtube.com/watch?v=Lu0sotERXhI"
    )

toy_story_3 = movie.Movie(
    "Toy Story 3",
    "The toys are mistakenly delivered to a day-care center instead of"
    " the attic right before Andy leaves for college, and it's up to Woody to"
    " convince the other toys that they weren't abandoned and to return home.",
    "http://www.impawards.com/2010/posters/toy_story_three_ver10.jpg",
    "https://www.youtube.com/watch?v=JcpWXaA2qeg"
    )

star_wars_4 = movie.Movie(
    "Star Wars: Episode IV - A New Hope",
    "Luke Skywalker joins forces with a Jedi Knight, a cocky pilot,"
    " a Wookiee, and two droids to save the galaxy from the Empire's"
    " world-destroying battle-station, while also attempting to rescue "
    "Princess Leia from the evil Darth Vader.",
    "https://images-na.ssl-images-amazon.com/images/I/51tYqdoRx4L.jpg",
    "https://www.youtube.com/watch?v=9gvqpFbRKtQ"
    )

star_wars_5 = movie.Movie(
    "Star Wars: Episode V - The Empire Strikes Back",
    "After the rebels are overpowered by the Empire on their newly"
    " established "
    "base, Luke Skywalker begins Jedi training with Master Yoda. His friends"
    " accept"
    " shelter from a questionable ally as Darth Vader hunts them in a plan"
    " to capture Luke.",
    "http://a.dilcdn.com/bl/wp-content/uploads/sites/6/2015/07/ESBWind.jpg",
    "https://www.youtube.com/watch?v=96v4XraJEPI"
    )

star_wars_6 = movie.Movie(
    "Star Wars: Episode VI - Return of the Jedi",
    "After a daring mission to rescue Han Solo from Jabba the Hutt, the rebels"
    " dispatch to Endor to destroy a more powerful Death Star. Meanwhile, Luke"
    " struggles to help Vader back from the dark side without falling into the"
    " Emperor's trap.",
    "https://images-na.ssl-images-amazon.com/images/I/51UdiBUkerL._SY450_.jpg",
    "https://www.youtube.com/watch?v=5UfA_aKBGMc"
    )

# Adding each movie into a list
movie_list = [
    toy_story,
    toy_story_2,
    toy_story_3,
    star_wars_4,
    star_wars_5,
    star_wars_6
    ]

# Using the prepared code to render the generated website from list
fresh_tomatoes.open_movies_page(movie_list)
