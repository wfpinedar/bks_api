import requests

def query_google_books(query): 
    url = 'https://www.googleapis.com/books/v1/volumes' 
    params = { 
        'q': query, 
        'maxResults': 1,  # Adjust the number of results as needed 
    } 
 
    response = requests.get(url, params=params) 
    data = response.json() 
 
    books = []
    for item in data.get('items', []): 
        book_info = item.get('volumeInfo', {})
        book = { 
            'title': book_info.get('title', ''), 
            'subtitle': book_info.get('subtitle', ''), 
            'authors': ', '.join(book_info.get('authors', [])), 
            'categories': ', '.join(book_info.get('categories', [])), 
            'editor': book_info.get('publisher', ''), 
            'description': book_info.get('description', ''), 
            'image': book_info.get('imageLinks', {}).get('thumbnail', '')
        } 
        books.append(book) 
 
    return books

def user_is_valid(user: dict):
    if user['username'] == 'Fernando' and user['email'] == 'fercho@gmail.com':
        return True
    else: 
        return False