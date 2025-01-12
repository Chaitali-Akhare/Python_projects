import webbrowser
from urllib import request, error
from bs4 import BeautifulSoup


def open_and_fetch_visible_content(url):
    try:
        # Attempt to open the URL in the default web browser
        webbrowser.open(url)

        # Fetch the content of the webpage
        with request.urlopen(url) as response:
            html_content = response.read().decode('utf-8')

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')

        # Extract and return the visible text content
        visible_text = soup.get_text(separator='\n', strip=True)
        return visible_text

    except error.HTTPError as e:
        # Handle HTTP errors (e.g., 404 Not Found, 500 Internal Server Error)
        return f"HTTP Error: {e.code} - {e.reason}"

    except error.URLError as e:
        # Handle URL errors (e.g., network unreachable, connection timeout)
        return f"URL Error: {e.reason}"

    except Exception as e:
        # Handle any other unexpected exceptions
        return f"An unexpected error occurred: {e}"


# Example usage
url = input("Enter the URL: ")
webpage_content = open_and_fetch_visible_content(url)
print(webpage_content)
