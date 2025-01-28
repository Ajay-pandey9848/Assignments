def my_split(sentence, separator):
    result = []
    current = ""
    for char in sentence:
        if char == separator:
            result.append(current)
            current = ""
        else:
            current += char
    result.append(current)  # Add the last part
    return result

def my_join(lst, separator):
    result = ""
    for i, item in enumerate(lst):
        result += item
        if i < len(lst) - 1:
            result += separator
    return result

def main():
    sentence = input("Please enter sentence:")
    # Use space as default separator for split
    words = my_split(sentence, ' ')
    print(my_join(words, ','))  # Join with comma and print
    for word in words:
        print(word)

if __name__ == "__main__":
    main()
