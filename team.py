#예제 코드 복붙 이렇게 해서 작업 시작 해보자

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
        self.password = password

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
members = []
posts = []

# TODO : 코드 구현이 필요합니다.
