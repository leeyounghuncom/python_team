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

# 코드 구현이 필요합니다.
# 5. 회원 인스턴스를 세개 이상 만들고 `members` 라는 빈리스트에 append를 써서 저장해주세요
#테스트 오케이
# input을 이용하여 Member 인스턴스 만드는것을 사용자가 터미널에서 할 수 있게 해주세요.
print("멤버등록")
name = input("이름: ")
username = input("아이디: ")
password = input("패스워드: ")

Mbrs = Member(name=name, username=username, password=password)
members.append(Mbrs)

# 1. members 리스트를 돌면서 회원들의 이름을 모두 프린트 해주세요
for mbr in members:
    print(mbr.name)


# 6. 각각의 회원이 게시글을 세개 이상 작성하는 코드를 만들어주세요.
# (회원이 세명이명 총 9개 이상의 post 인스턴스가 만들어져야 합니다)
# 만들어진 게시글 인스턴스들은 posts 빈리스트에 append를 써서 저장해주세요
#     1. for 문을 돌면서 특정유저가 작성한 게시글의 제목을 모두 프린트 해주세요
#     2. for문을 돌면서 ‘특정 단어’가 content에 포함된 게시글의 제목을 모두 프린트 해주세요

