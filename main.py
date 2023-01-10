from encodingData import charData

def decode(url):
    for key, value in charData.items():
        url = url.replace(key, value)
    return url

def encode(url):
    for key, value in charData.items():
        url = url.replace(value, key)
    return url
    

if __name__ == "__main__":
    running = True

    print("Welcome to the URL Decoder!")
    while running:
        print("Do you want to encode or decode a URL? (e/d) / any other key to quit")
        choice = input()
        if choice == "E" or choice == "e":
            print("Please enter the URL you want to encode:")
            url = input()
            print("The encoded URL is: " + encode(url) + "\n")
        elif choice == "D" or choice == "d":

            print("Please enter the URL you want to decode:")
            url = input()
            print("The decoded URL is: " + decode(url) + "\n")

        else:
            running = False

