import random

book_titles = [
    "The Bible",
    "Quotations from Chairman Mao Tse-tung",
    "Harry Potter and the Philosopher's Stone",
    #"The Lord of the Rings", Error Fetching
    "The Alchemist",
    "The Da Vinci Code",
    "The Catcher in the Rye",
    "The Adventures of Sherlock Holmes",
    "The Very Hungry Caterpillar",
    "Dream of the Red Chamber",
    "And Then There Were None",
    "The Hobbit",
    "Harry Potter and the Chamber of Secrets",
    "Harry Potter and the Prisoner of Azkaban",
    "Harry Potter and the Goblet of Fire",
    "Harry Potter and the Order of the Phoenix",
    "Harry Potter and the Half-Blood Prince",
    "Harry Potter and the Deathly Hallows",
    "The Lion, the Witch and the Wardrobe",
    "The Adventures of Huckleberry Finn",
    "The Adventures of Pinocchio"
]

def generate_random_title():
    """Generate a random book title."""
    return random.choice(book_titles)

def store_title(filename, title):
    """Store the title in a file."""
    with open(filename, 'a') as file:
        file.write(title + '\n')