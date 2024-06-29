#예제 코드 복붙 이렇게 해서 작업 시작 해보자
# 3. (심화)비밀번호 해싱이 무엇인지 공부한 후 hashlib 라이브러리를 써서 회원 비밀번호를 해시화하여 저장하게 해주세요.
import hashlib

# ----- 코드 정의 ------
# 1. Member 클래스와 Post 클래스를 정의하세요.
class Member:
    # 코드 구현이 필요합니다.
    # Member 클래스에는 다음과 같은 속성을 가지고 있어야 합니다.
    #     - 회원 이름 (**`name`**)
    #     - 회원 아이디 (**`username`**)
    #     - 회원 비밀번호 (**`password`**)
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = hashlib.sha256(b"password").hexdigest() # b는 (normally bytes) using the
        #https://docs.python.org/ko/3/library/hashlib.html

    # 3. **`Member`** 클래스에는 다음과 같은 메소드를 가지고 있어야 합니다.
    #     - 회원 정보를 print해주는 `display` (회원이름과 아이디만 보여주고 비밀번호는 보여줘서는 안됩니다!)
    def display(self):
        # 코드 구현이 필요합니다.
        return f"Name: {self.name}, Username: {self.username}"


class Post:
    # 코드 구현이 필요합니다.
    # Post 클래스에는 다음과 같은 속성을 가지고 있어야 합니다.
    #     - 게시물 제목 (**`title`**)
    #     - 게시물 내용 (**`content`**)
    #     - 작성자 (**`author`**) : 회원의 `username` 이 저장되어야 함!
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

# ----- 코드 실행 ------
# (회원이 세명이명 총 9개 이상의 post 인스턴스가 만들어져야 합니다)
# 회원 3명에 콘텐츠 3개 등록 되는 구현...
members = []
posts = []

# 5. 회원 인스턴스를 세개 이상 만들고 `members` 라는 빈리스트에 append를 써서 저장해주세요
# input을 이용하여 Member 인스턴스 만드는것을 사용자가 터미널에서 할 수 있게 해주세요.
for _ in range(3):
    name = input("이름: ")
    username = input("아이디: ")
    password = input("패스워드: ")

    Mbrs = Member(name=name, username=username, password=password)
    members.append(Mbrs)

# 1. members 리스트를 돌면서 회원들의 이름을 모두 프린트 해주세요
for mbr in members:
    print(mbr.name)

# 6. 각각의 회원이 게시글을 세개 이상 작성하는 코드를 만들어주세요.
# post도 터미널에서 생성할 수 있게 해주세요.
for mbr in members:
    title = input("제목: ")
    content = input("내용: ")

    # 만들어진 게시글 인스턴스들은 posts 빈리스트에 append를 써서 저장해주세요
    Posts = Post(title=title, content=content, author=mbr.name)
    posts.append(Posts)

# 1. for 문을 돌면서 특정유저가 작성한 게시글의 제목을 모두 프린트 해주세요
se_user = input("유저의 아이디: ")
for post in posts:
    if se_user == post.author:
        print(post.title)

# 2. for문을 돌면서 ‘특정 단어’가 content에 포함된 게시글의 제목을 모두 프린트 해주세요
se_word = input("특정 단어: ")
for post in posts:
    if se_word in post.content:
        print(post.title)

