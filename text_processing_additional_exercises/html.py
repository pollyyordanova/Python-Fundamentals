title = input()
content = input()

print(f"<h1>\n    {title}\n</h1>")
print(f"<article>\n    {content}\n</article>")

while True:
    comment = input()
    if comment == "end of comments":
        break
    print(f"<div>\n    {comment}\n</div>")
