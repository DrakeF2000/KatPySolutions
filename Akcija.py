def calc_cost(books:list):
    books.sort(reverse=True)
    total_price = 0
    for i in range(len(books)):
        if i % 3 != 2:
            total_price += books[i]
    print(books)
    return total_price

book_count = int(input())
data = []
for i in range(book_count):
    data.append(int(input()))
print(calc_cost(data))