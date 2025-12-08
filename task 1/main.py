#Мазалевская Вариант 4
print(f"start code...")
books=[
    {
        "title":"Спеши любить",
        "author":"Николас Спаркс",
        "year":1999
    },
    {
        "title":"А зори здесь тихие",
        "author":"Борис Васильев",
        "year":1969 
    },
    {
         "title":"Убийство в Восточном экспрессе",
        "author":"Агата Кристи",
        "year":1934
    },
    {
         "title":"Оно",
        "author":"Стивен Кинг",
        "year":1986
    },
    {
         "title":"Внутри убийцы",
        "author":"Майк Омер",
        "year":2018
    }
]
for i, inf in enumerate(books,1):
    print(f"---------------Книга {i}---------------")
    print(f"Название: {inf["title"]}, Автор: {inf["author"]}")
    print(f"----------------{inf["year"]}----------------")
    print("\n")
print(f"end code...")