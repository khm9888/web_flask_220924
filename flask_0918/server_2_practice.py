from flask import Flask

app = Flask(__name__)


# 1. 플라스크로 메인 화면 생성

# 3. 홈페이지 구현
# index 페이지에서 목차가 나올 수 있게 설정
# html로 이동하여 작성해서 가져올 것

# 3-2. index 형태에 대해서 함수구현 - list or dict에서 가져오는 구조

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


def template(index_str, title_body):
    page = f"""
    <!DOCTYPE html>
    <html lang="ko">
        <body>
            <h1><a href="/">WEB</a></h1>
            <ol>
                {index_str}
            </ol>
            {title_body}
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


@app.route("/read/<int:id>")  # get 방식으로 값을 가져오기 위한 방법
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
    page = template(index_str, title_body)
    return page

# 2-1-1.create 페이지 작성


@app.route("/create/")
def create():
    return "Create"


# 2-1-3.update 페이지 작성
@app.route("/update/")
def update():
    return "update"


# 5. 쓰기 기능구현 - create
# 6. 수정 기능구현 - update
# 7. 삭제 기능구현 - delete


app.run(debug=True)

# 10. 웹서버 구현
