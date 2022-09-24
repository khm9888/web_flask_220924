#! C:\Users\admin\AppData\Local\Programs\Python\Python38\python.exe

import cgi
import os

print("content-type: text/html")
print()

files = os.listdir("data")
listStr = ""
for item in files:
    name = item
    listStr += f"<li><a href='index.py?id={name}'>{name}</a></li>"

form = cgi.FieldStorage()
if "id" in form:
    pageId = form["id"].value
    description = open("./data/"+pageId, "r").read()
    update_link = f"<a href='update.py?id={pageId}'>update</a>"
else:
    pageId = "Welcome"
    description = "Hello, web"
    update_link = ""

# print(files)

title = pageId

print(f"""
      <!DOCTYPE html>
<html>

<head>
    <title>
        web1-welcome
    </title>
    <!-- <meta charset="euckr"> -->
    <meta charset="utf-8">
</head>

<body>
    <h1><a href="index.py">WEB</a></h1>
    
    {listStr}

    <a href="create.py">create</a>
    {update_link}
    
    <h2>{title}</h2>
    <p style="margin-top:45px;">{description} </p>

</body>
</html>
""")
