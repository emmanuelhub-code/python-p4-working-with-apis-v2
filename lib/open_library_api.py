import requests
import json

class OpenLibraryAPI:
    BASE_URL = "https://openlibrary.org/search.json"

    def __init__(self):
        pass

    def search_books(self, title, fields=None, limit=5):
        """
        Search books by title.
        Args:
            title (str): The book title to search.
            fields (list, optional): List of fields to include in response. Default ['title','author_name'].
            limit (int, optional): Number of results to return. Default 5.
        Returns:
            list of dicts: Each dict contains requested fields for a book.
        """
        if fields is None:
            fields = ["title", "author_name"]

        search_term_formatted = title.replace(" ", "+")
        fields_formatted = ",".join(fields)

        URL = f"{self.BASE_URL}?title={search_term_formatted}&fields={fields_formatted}&limit={limit}"
        response = requests.get(URL)

        if response.status_code != 200:
            print(f"Error: {response.status_code}")
            return []

        data = response.json()
        return data.get("docs", [])

    def get_first_result(self, title):
        """
        Get first search result for a book title.
        """
        results = self.search_books(title, limit=1)
        if not results:
            return "No results found"
        book = results[0]
        authors = ", ".join(book.get("author_name", ["Unknown author"]))
        return f"Title: {book.get('title', 'Unknown')}\nAuthor(s): {authors}"

# Example usage
if __name__ == "__main__":
    api = OpenLibraryAPI()
    search_term = input("Enter a book title: ")
    result = api.get_first_result(search_term)
    print("\nSearch Result:\n")
    print(result)
