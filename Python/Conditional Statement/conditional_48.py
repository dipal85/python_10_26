#48. Write a program to print language choice using match case.

code = input("Code (en/es/fr/de/hi): ").lower()
match code:
    case "en": 
        print("Hello (English)")
    case "es": 
        print("Hola (Spanish)")
    case "fr": 
        print("Bonjour (French)")
    case "de": 
        print("Guten Tag (German)")
    case "hi": 
        print("Namaste (Hindi)")
    case _: 
        print("Unsupported Language")