
def main():

    person = {
        "name": "John Doe",
        "age": 30,
        "city": "New York"
    }

    for key in person:
        value = person[key]
        print(key + ":", value)

    for key, value in person.items():
        print(key + ":", value)
        
main()