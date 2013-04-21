book1 = {
'title': 'Learning Python',
'likes': 50,
'tags': ['Programming', 'Python']}

book2 = {
'title': 'Thinking in Java',
'likes': 30,
'tags': ['Programming', 'Java']}

db = []
db.append(book1)
db.append(book2)

for book in db:
    print book['title'], ":", book['tags']

x = [book['title'] for book in db if 'Python' in book['tags']]
print x

x = [book['title'] for book in db if book['likes'] < 40 ]
print x

