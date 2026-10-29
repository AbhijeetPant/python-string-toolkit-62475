def count_questions(text):
    count = 0

    for char in text:
        if char == '?':
            count += 1

    return count


text = input("Enter your string : ")
print(count_questions(text))