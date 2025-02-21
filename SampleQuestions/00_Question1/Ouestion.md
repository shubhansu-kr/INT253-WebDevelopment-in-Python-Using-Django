# Sample Question 1 : Library Management

Developing a Django-based book library system where users can browse and filter books by author and publication year. However, the system does not use a database (no models) and instead relies on a hardcoded list of books stored in the application.

Requirements:
1. Implement a view function to display a list of books using a hardcoded dataset.
2. Allow users to filter books by author using a URL pattern like:
	/library/<author>/

3. Allow users to filter books by both author and year using a URL pattern like:
	/library/<author>/<year>/

4. Implement template inheritance where:
base.html includes a header and navigation menu.
library.html extends base.html and displays the list of books with filtering logic applied in Django Template Language (DTL).

5. Ensure the filtering is case-insensitive

6. If no books match the filter, display a "No books found" message
