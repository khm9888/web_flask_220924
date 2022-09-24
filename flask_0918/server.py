from flask import Flask, request, redirect

app = Flask(__name__)

nextID = 4
topics = [
    {"id": 1, "title": "html", "body": "html is ..."},
    {"id": 2, "title": "css", "body": "css is ..."},
    {"id": 3, "title": "javascript", "body": "javascript is ..."}
]


def template(liTags, content, id=None):
    contextUI = ""

    delete_html = f"""
        <li>
            <form action="/delete/{id}/" method="POST">
                <input type="submit" value="delete">
            </form>
        </li>   
    """
    if id != None:
        contextUI = f'''
            <li><a href="/update/{id}/">update</a></li>
            {delete_html}
        '''
    html_text = f'''
    <!DOCTYPE html>

    <html lang="ko">
    <body>
        <h1><a href="/">WEB</a></h1>
        <ol>
            {liTags}
        </ol>
        {content}
        <ul>
            <li><a href="/create/">create</a></li>
            {contextUI}
        </ul>
    </body>
    </html>
    '''
    return html_text


def getContents():
    liTags = ''
    for topic in topics:
        liTags += f"<li><a href='/read/{topic['id']}'>{topic['title']}</a></li>"
    return liTags


@app.route("/")
def index():
    content = """<h2>web</h2>
    <p>
        Hello,web
    </p>"""
    return template(getContents(), content)


# @app.route("/create/", methods=["get", "post"])
@app.route("/create/", methods=["get", "post"])
def create():
    # <form action="/create/" method="post">
    print(f"request.method:{request.method}")
    if request.method == "GET":
        content = """ 
        <form action="/create/" method="post">
            <p><input name = "title" type="text" placeholder="title"></p>   
            <p><textarea name = "body" placeholder="body"></textarea></p>   
            <p><input type="submit" value="create"></p>
        </form>   
        """
        return template(getContents(), content)
    elif request.method == "POST":
        global nextID
        title = request.form["title"]
        body = request.form["body"]
        # nextID로 안 만들어서 에러날 수 있음
        newtopic = {"id": nextID, "title": title, "body": body}
        topics.append(newtopic)
        url = f"/read/{nextID}"
        print(url)
        nextID += 1
        return redirect(url)


@app.route("/update/<int:id>/", methods=["get", "post"])
def update(id):
    # <form action="/update/" method="post">
    print(f"request.method:{request.method}")
    if request.method == "GET":
        title = ""
        body = ""
        for topic in topics:
            if id == topic["id"]:
                title = topic["title"]
                body = topic["body"]
                break

        content = f""" 
        <form action="/update/{id}/" method="post">
            <p><input name = "title" type="text" placeholder="title" value="{title}"></p>   
            <p><textarea name = "body" placeholder="body">{body}</textarea></p>   
            <p><input type="submit" value="update"></p>
        </form>   
        """
        return template(getContents(), content)
    elif request.method == "POST":
        title = request.form["title"]
        body = request.form["body"]

        for topic in topics:
            if id == topic["id"]:
                topic["title"] = title
                topic["body"] = body
                break
        # nextID로 안 만들어서 에러날 수 있음
        url = f"/read/{id}"
        print(url)
        return redirect(url)


@app.route("/read/<int:id>")
def read(id):
    title = ""
    body = ""
    for topic in topics:
        if id == topic["id"]:
            title = topic["title"]
            body = topic["body"]
            break
    content = f"""<h2>{title}</h2>
    <p>
        {body}
    </p>"""

    return template(getContents(), content, id)


@app.route("/delete/<int:id>/", methods=["post"])
def delete(id):
    for topic in topics:
        if id == topic["id"]:
            topics.remove(topic)
            break
    return redirect("/")


app.run(debug=True)  # debuging mode on! #실제로 적용할 때 debugger mode (x)
