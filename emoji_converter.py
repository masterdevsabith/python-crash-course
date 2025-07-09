def emoji_converter(message):
    emoji_dictionary = {
        ":)": "😀",
        ":(": "😣"
    }

    output = ""
    words = message.split(" ")
    for word in words:
        output += emoji_dictionary.get(word, word) + " "
    return output


print(emoji_converter("hi there :("))
