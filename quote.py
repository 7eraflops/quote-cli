# quote.py
import requests

def get_random_quote():
    """Fetches a random quote from the quotable.io API."""
    try:
        response = requests.get("https://api.quotable.io/random")
        response.raise_for_status()  # Raise an exception for bad status codes
        data = response.json()
        return f"{data['author']}: '{data['content']}'"
    except requests.RequestException as e:
        return f"Error: Could not fetch quote. {e}"

def main():
    """Displays a random inspirational quote."""
    print(get_random_quote())

if __name__ == "__main__":
    main()