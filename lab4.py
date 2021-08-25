class Book:
    def __init__(self, author, title, book_id):
        self.author = author
        self.title = title
        self.book_id = book_id

    def __str__(self):
        return 'Book({}, {}, {})'.format(self.author, self.title, self.book_id)

    def __repr__(self):

        return 'Book({}, {}, {})'.format(self.author, self.title, self.book_id)

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author and self.book_id == other.book_id

class Description(Book):
    def __init__(self, description, desc_id):
        self.desc_id = desc_id
        self.description = description
    
    def __str__(self):
        return 'Desc({}, {})'.format(self.desc_id, self.description)
    
    def __repr__(self):
        return 'Desc({}, {})'.format(self.desc_id, self.description)
    
    def __eq__(self, other):
        return self.desc_id == other.desc_id and self.description == other.description
        

newBook = Book('Simon', 'Start With What', 123)
newDesc = Description('gfgfgf',123)
if newBook.book_id == newDesc.desc_id:
    print(newBook, "\n", newDesc)
else:
    print("Error! Please check your book and description id")
    
def romanize(number):
    n2rMap = {1000:'M', 900:'CM', 500:'D', 400:'CD', 100:'C', 90:'XC', 50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'}
    roman = ""
    for key in n2rMap.keys():
      count = int(number / key)
      roman += n2rMap[key] * count
      number -= key * count
    return roman
