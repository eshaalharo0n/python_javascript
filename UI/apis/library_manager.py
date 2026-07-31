import json
data_file = "library.json"
def read():
    file = open(data_file, "r")
    library = json.load(file)
    file.close()
    
    return library
def read_by_id(id):
    library = read()
    library_result = None
    for book in library:
        if book["id"] == id:
            library_result = book
            break
    
    return library_result
def add(book):
    books = read()
    book["availability"] ="yes"
    if len(books) == 0:
        book["id"] = 1
    else:
        max_id = books[0]["id"]
        for s in books:
            if int(s["id"]) > int(max_id):
                max_id = s["id"]
        book["id"] = max_id + 1
    books.append(book)    
    

    file = open(data_file,"w")
    json.dump(books, file)
    file.close()
def update(book_id, book):
    library = read()
    
    for bk in library:
        if bk["id"] == book_id:
            bk["book_name"] = book["book_name"]
            bk["author"] = book["author"]
            bk["category"] = book["category"]
            bk["availability"] = book["availability"]
            break
    
    file = open(data_file,"w")
    json.dump(library, file)
    file.close() 
def delete(book_id):
    library = read()
    
    for bk in library:
        if bk["id"] == book_id:
            library.remove(bk)
            break
        
    file = open(data_file,"w")
    json.dump(library, file)
    file.close()     