text = input()
result = [text[0]]

for i in range(1, len(text)):
    if text[i] != text[i - 1]:
        result.append(text[i])

print("".join(result))
