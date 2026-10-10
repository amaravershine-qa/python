def matchCase():
    status = int(input("Enter a status code:"))
    match status:
        case 200:
            return "Success"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:
            return "Unknown Status Code"
result = matchCase()
print(result)
