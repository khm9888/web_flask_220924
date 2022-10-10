from flask import Flask, request, redirect
app = Flask(__name__)


# 1. 플라스크로 메인 화면 생성

# 3. 홈페이지 구현
# index 페이지에서 목차가 나올 수 있게 설정
# html로 이동하여 작성해서 가져올 것

# 3-2. index 형태에 대해서 함수구현 - list or dict에서 가져오는 구조
# 5-6-2. nextId 추가
nextId = 4
index_list = [
    {"id": 1, "title": "html", "body": "html is ..."},
    {"id": 2, "title": "css", "body": "css is ..."},
    {"id": 3, "title": "js", "body": "js is ..."}
]

# 3-3. html에서 li 태그 작성해서, 수정하여 대입
# index_str = ""
# for index_one in index_list:
#     index_str += f"<li><a href=f'read/{index_one['id']}'>{index_one['title']}</a></li>"

# 4-4. 템플릿화하기(겹치는 부분에 대해서 함수처리)
# 6-1-1. id 값을 통해서 해당 데이터의 수정을 적용해야함, 그렇기에 parameter에 id 추가
# 6-1-2. 하지만 id 값을 넣지 않는 경우도 있기에 id에 기본값 None 입력
# 7-1. 삭제기능 추고, contextUI에 추가(따로 페이지 생성 등은 안 함)


def template(index_str, title_body, id=None):
    contextUI = ""
    # print(id)
    if id != None:
        contextUI = f'''
        <li>
            <a href="/update/{id}">update</a>
        </li>
        <li>
            <form action="/delete/{id}" method="POST">
                <input type="submit" value="delete">
            </form>
        </li>
        '''
    page = f"""
    <!DOCTYPE html>
    <html lang="ko">
        <body>
            <h1><a href="/">WEB</a></h1>
            <ol>
                {index_str}
            </ol>
            {title_body}
            <ul>
                <li>
                    <a href="/create/">create</a>
                </li>
                {contextUI}
            </ul>
        </body>
    </html>
    """
    return page

# 4-5. index_str 에 대해서도 함수처리


def get_index_str():
    index_str = ""
    for index_one in index_list:
        index_str += f"<li><a href='/read/{index_one['id']}'>{index_one['title']}</a></li>"
    return index_str


@app.route("/")
def index():
    # 4-5-1. index_str 함수화
    index_str = get_index_str()
    # 3-1. index 형태 제작하고,
    title = "WELCOME"
    body = "Hello,WEB"
    title_body = f"<h2>{title}</h2>{body}"
    page = template(index_str, title_body)
    return page

# 2. 메인페이지로부터 서브페이지(index) 생성 - routing
# 2-1. 구조도 작성

# 2-1-2.read 페이지 작성
# 4. 읽기 기능구현 - read
# 4.1 - index와 유사하여 복사 붙어넣기


@app.route("/read/<int:id>/")  # get 방식으로 값을 가져오기 위한 방법
def read(id):
    # 4-5-1. index_str 함수화
    index_str = get_index_str()
    # 4-2. index_list에서 id를 조회하여 진행
    title = ""
    body = ""
    for index_one in index_list:
        if index_one["id"] == id:  # 자료형을 똑같이 하여 비교하기 위해, route에서 int화 시킴
            title = index_one["title"]
            body = index_one["body"]
            break

# 4-3. title과 body를 넣음
    title_body = f"<h2>{title}</h2>{body}"
    page = template(index_str, title_body, id)
    return page

# 2-1-1.create 페이지 작성
# 5. 쓰기 기능구현 - create
# 5-2. methods에 get, post 추가


@app.route("/create/", methods=["GET", "POST"])
def create():
    # 5-3. request.method 확인
    print(f"request.method {request.method}")
    # 5-4-1. get 방식일 때 추가
    if request.method == "GET":  # 대문자
        # 5-1. form 형태로 추가하고, post 형식으로 값 전달
        content = """
            <form antion="/create/" method="post">
                <p><input type="text" placeholder="title" name ="title"></p>
                <p><textarea placeholder="body" name="body"></textarea></p>
                <p><<input type="submit" value="create"></p>
            </form>
        """
        page = template(get_index_str(), content)
        return page

    elif request.method == "POST":  # 대문자
        global nextId
        # 5-5. form에서 title과 body 가져오는 것
        title = request.form["title"]
        body = request.form["body"]
        # 5-6-1. 새로운 정보 추가
        new_dict = {"title": title, "body": body, "id": nextId}
        index_list.append(new_dict)
        # 5-7-1. 추가가 완료되었으니, read로 이동(추가된 정보의 index로)
        # 5-8 url 끝 단은 / 생략할 것
        url = f"/read/{nextId}"
        nextId += 1
        # 5-7-2.변경된 url로 이동 redirect 함수 적용
        return redirect(url)


# 2-1-3.update 페이지 작성
# 6. 수정 기능구현 - update
# 5-2. methods에 get, post 추가
# 6-2-1. create 문을 수정하여, get/post 방식 가져옴
# 6-2-2. read 문을 통해 id 검색하는 기능 추가
@app.route("/update/<int:id>/", methods=["GET", "POST"])
def update(id):
    # 5-3. request.method 확인
    print(f"request.method {request.method}")
    # 5-4-1. get 방식일 때 추가
    if request.method == "GET":  # 대문자
        # 4-2. index_list에서 id를 조회하여 진행
        title = ""
        body = ""
        for index_one in index_list:
            if index_one["id"] == id:  # 자료형을 똑같이 하여 비교하기 위해, route에서 int화 시킴
                title = index_one["title"]
                body = index_one["body"]
                break
        # 5-1. form 형태로 추가하고, post 형식으로 값 전달
        # 6-2-3. 찾아진 id 값을 토대로 value 적용
        content = f'''
            <form antion="/update/{id}/" method="post">
                <p><input type="text" placeholder="title" name ="title" value="{title}"></p>
                <p><textarea placeholder="body" name="body">{body}</textarea></p>
                <p><<input type="submit" value="update"></p>
            </form>
        '''
        page = template(get_index_str(), content, id)
        return page
    # 5-4-2. post 방식일 때 추가
    elif request.method == "POST":  # 대문자
        # 5-5. form에서 title과 body 가져오는 것
        title = request.form["title"]
        body = request.form["body"]
        for index_one in index_list:
            if index_one["id"] == id:  # 자료형을 똑같이 하여 비교하기 위해, route에서 int화 시킴
                index_one["title"] = title
                index_one["body"] = body
                break
        # 5-6-1. 새로운 정보 추가
        # 5-7-1. 추가가 완료되었으니, read로 이동(추가된 정보의 index로)
        # 5-8 url 끝 단은 / 생략할 것
        url = f"/read/{id}"
        # 5-7-2.변경된 url로 이동 redirect 함수 적용
        return redirect(url)


# 7. 삭제 기능구현 - delete
# 7-2-1. post 방식을 위해 적용
@app.route("/delete/<int:id>/", methods=["POST"])
def delete(id):
    for index_one in index_list:
        if id == index_one["id"]:
            index_list.remove(index_one)
            break
    return redirect("/")


app.run()

# 10. 웹서버 구현
