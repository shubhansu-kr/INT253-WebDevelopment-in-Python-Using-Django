You are building a Movie Library System where users can browse and filter movies without using a database (no models). Instead, the system relies on a hardcoded list of movies stored in the application.
Requirements:
1.Implement a view function to display a list of movies using a hardcoded dataset.
2.Allow users to filter movies by genre using a URL pattern like:


/movies/action/
3. Allow users to filter movies by both genre and release year using a URL pattern like:

/movies/action/2020/
4 Implement template inheritance, where:
base.html includes a header and navigation menu
movies.html extends base.html and displays the list of movies with filtering logic applied in Django Template Language (DTL)


 Ensure the filtering is case-insensitive (e.g., "Action", "action", "ACTION" should return the same results).
 If no movies match the filter, display a "No movies found" message.