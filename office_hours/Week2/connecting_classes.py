# Blacksmith and tools
class Tool:
    def __init__(self,name,is_new,cost,metal,durability,strength_needed):
        self.name = name
        self.is_new = is_new
        self.cost = cost # Monetary cost
        self.metal = metal
        self.durability = durability
        self.strength_needed = strength_needed

class Blacksmith:
    def __init__(self,name,strength,health):
        self.name = name
        self.strength = strength
        self.current_health = health
        self.tools = [Tool("tweezers",True,5,"mythril",1000000,10)] # A list of Tools - including a default tool

    # Add a tool to a blacksmith's set
    def add_tool(self,tool):
        self.tools.append(tool) # This adds the passed in Tool to our selection (list) of tools
        return self
    
    # Way to show all the tools
    def show_tools(self):
        for current_tool in self.tools:
            print(current_tool.name)
        return self

    # Method to determine if you can use tool - try doing this as a static method!
    def can_use_tool(self,tool):
        if self.strength < tool.strength_needed:
            return False
        else:
            return True


juan = Blacksmith("Juan",1000000,100)
adrian = Blacksmith("Adrian",70,50)

hammer = Tool("hammer",True,10,"iron",100,10)
pliers = Tool("pliers",True,10,"molybdenum",50,5)
saw = Tool("saw",True,30,"brass",300,75)

# print(juan.can_use_tool(saw))
# print(adrian.can_use_tool(saw))

juan.add_tool(saw)
juan.show_tools()
adrian.add_tool(pliers)

# Another set with Books and Readers
class Book:
    def __init__(self,title,is_fictional,pages,chapters,writer,genre):
        self.title = title
        self.is_fictional = is_fictional
        self.number_of_pages = pages
        self.number_of_chapters = chapters
        self.author = writer
        self.genre = genre

class Reader:
    def __init__(self,name, books = [], pages_read_to = []):
        self.name = name
        self.books_read = books # List of books for the reader to read, if any
        self.pages_read_to = pages_read_to # Starting page numbers for each book, if specified
        # Loop to add default values for starting page numbers - if any are specified
        if len(self.books_read) > 0 and len(pages_read_to) == 0:
            for i in range(len(self.books_read)):
                self.pages_read_to.append(1)
    
    def read_book(self,book_list_index,page_read_to):
        self.pages_read_to[book_list_index] = page_read_to
        return self

    def find_book(self,title):
        # Loop through all the books available to see if it's found - if so, return its index
        for i in range(len(self.books_read)):
            if self.books_read[i].title == title:
                return i
        return -1

lotr = Book("Lord of the Rings",True,500,25,"J.R.R. Tolkien","fantasy")
c_tales = Book("The Canterbury Tales",True,2000,100,"Geoffrey Chaucer","folklore")

rene = Reader("Rene",[lotr,c_tales])

print(rene.pages_read_to)
book_ind = rene.find_book("Lord of the Rings")
if book_ind >= 0:    
    rene.read_book(book_ind,100) # Read LOTR
print(rene.pages_read_to)
rene.read_book(1,50)
print(rene.pages_read_to)



