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
    library = read()
    library.append(book)

    file = open(data_file,"w")
    json.dump(library, file)
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