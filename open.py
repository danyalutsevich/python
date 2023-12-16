# with open("test.txt", mode="w") as file:
#     file.write("Host:localhost\r\n")
#     file.write("Connection:close\r\n")
#     file.write("Content-Type:text/css\r\n")
#     file.write("Content-Length:100500\r\n")

file = open("test.txt", mode="r")
content = file.read()
dictionary = {}
for header in content.split("\r")[0].split("\n"):
    splited = header.split(":")
    if len(splited) >= 2:
        dictionary[splited[0]] = splited[1]
print(dictionary)
