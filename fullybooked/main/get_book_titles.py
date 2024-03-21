def get_titles_from_file(filename):
    """Retrieve titles from the file."""
    with open(filename, 'r') as file:
        titles = file.readlines()
    return [title.strip() for title in titles]

# Example usage
if __name__ == "__main__":
    titles = get_titles_from_file("book_titles.txt")
    print("Available book titles:")
    for title in titles:
        print(title)

