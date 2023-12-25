import os


def static(environ):
    path = environ["PATH_INFO"].replace("/", "")
    response = None
    file_path = "./static/" + path + ".html"
    if os.path.exists(file_path):
        with open(file_path, mode="r") as file:
            response = [bytes(file.read().replace("headers", str(environ)), "UTF-8")]
        return response
    else:
        raise FileNotFoundError("File does not exists")
