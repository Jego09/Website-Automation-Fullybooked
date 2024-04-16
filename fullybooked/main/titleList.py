import random

book_titles = [
"The Night Circus", "To Kill a Mockingbird", "1984", "The Great Gatsby", "Harry Potter and the Philosopher's Stone", "The Catcher in the Rye", "Pride and Prejudice", "The Hobbit", "The Da Vinci Code", "The Hunger Games", "The Lord of the Rings", "The Alchemist", "Gone with the Wind", "The Chronicles of Narnia", "The Fault in Our Stars","Moby-Dick", "Brave New World", "The Picture of Dorian Gray", "The Road", "One Hundred Years of Solitude", "The Kite Runner", "Frankenstein", "The Girl with the Dragon Tattoo", "The Bell Jar", "The Secret History", "The Goldfinch", "The Help", "Wuthering Heights", "The Handmaid's Tale", "The Book Thief","The Brothers Karamazov", "The Count of Monte Cristo", "Beloved", "The Name of the Wind", "The Underground Railroad", "Sapiens: A Brief History of Humankind", "Norwegian Wood", "Educated", "The Nightingale", "The Martian", "The Stand", "The God of Small Things", "Never Let Me Go", "The Thorn Birds", "Life of Pi","Crime and Punishment", "Anna Karenina", "The Picture of Dorian Gray", "The Road", "The Brief Wondrous Life of Oscar Wao", "Americanah", "Atonement", "The Grapes of Wrath", "The Wind-Up Bird Chronicle", "The Secret Garden", "The Color Purple", "The Old Man and the Sea", "East of Eden", "The Poisonwood Bible", "White Teeth"
]

def generate_random_title():
    """Generate a random book title."""
    return random.choice(book_titles)
