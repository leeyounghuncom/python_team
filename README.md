# python_team
**용어 설명**

- 클래스 : 클래스는 인스턴스의 설계도나 템플릿입니다. 객체의 속성(어트리뷰트)과 행위(메소드)를 정의하는 틀입니다. 예를 들어, 자동차 클래스는 자동차의 속성(색상, 모델 등)과 행위(가속, 정지 등)를 정의합니다.
- 인스턴스 : 클래스의 정의를 기반으로 실제로 생성된 객체를 인스턴스라고 합니다
- 메소드 : 클래스 함수라고도 합니다. 클래스 내에서 지정된 함수입니다. 자동차 클래스의 "가속"이나 "정지"와 같은 작업이 메소드의 예시입니다.
- 어트리뷰트 : 클래스 변수라고도 합니다. 클래스 내에서 변수를 지정할때 사용합니다.  자동차 클래스에서 "색상"이나 "모델"과 같은 특징이 어트리뷰트의 예시입니다.

**아직 용어가 익숙하지 않으신 분들은 클래스 부분 복습이 필요할 수 있습니다**

**과제 내용:**

1. **`Member`** 클래스와 **`Post`** 클래스를 정의하세요.
2. **`Member`** 클래스에는 다음과 같은 속성을 가지고 있어야 합니다.
    - 회원 이름 (**`name`**)
    - 회원 아이디 (**`username`**)
    - 회원 비밀번호 (**`password`**)
3. **`Member`** 클래스에는 다음과 같은 메소드를 가지고 있어야 합니다.
    - 회원 정보를 print해주는 `display` (회원이름과 아이디만 보여주고 비밀번호는 보여줘서는 안됩니다!)
4. **`Post`** 클래스에는 다음과 같은 속성을 가지고 있어야 합니다.
    - 게시물 제목 (**`title`**)
    - 게시물 내용 (**`content`**)
    - 작성자 (**`author`**) : 회원의 `username` 이 저장되어야 함!
5. 회원 인스턴스를 세개 이상 만들고 `members` 라는 빈리스트에 append를 써서 저장해주세요
    1. members 리스트를 돌면서 회원들의 이름을 모두 프린트 해주세요
6. 각각의 회원이 게시글을 세개 이상 작성하는 코드를 만들어주세요.(회원이 세명이명 총 9개 이상의 post 인스턴스가 만들어져야 합니다). 만들어진 게시글 인스턴스들은 posts 빈리스트에 append를 써서 저장해주세요
    1. for 문을 돌면서 특정유저가 작성한 게시글의 제목을 모두 프린트 해주세요
    2. for문을 돌면서 ‘특정 단어’가 content에 포함된 게시글의 제목을 모두 프린트 해주세요

**참고 자료:**

- <과제 3번 코드 스니펫>
    
    ```python
    # ----- 코드 정의 ------
    class Member:
        # TODO : 코드 구현이 필요합니다.
    
        def display(self):
            # TODO : 코드 구현이 필요합니다.
            pass
    
    class Post:
        # TODO : 코드 구현이 필요합니다.
        pass
    
    # ----- 코드 실행 ------
    members = []
    posts = []
    
    # TODO : 코드 구현이 필요합니다.
    
    ```
    

**추가 도전 과제:**

1. input을 이용하여 Member 인스턴스 만드는것을 사용자가 터미널에서 할 수 있게 해주세요.
2. post도 터미널에서 생성할 수 있게 해주세요.
3. (심화)비밀번호 해싱이 무엇인지 공부한 후 hashlib 라이브러리를 써서 회원 비밀번호를 해시화하여 저장하게 해주세요.

**평가**

- 클래스와 인스턴스 개념을 설명할 수 있는가?
- 메소드와 어트리뷰트(속성)을 설명할 수 있는가?
- 클래스를 정의할 수 있는가?
- 인스턴스를 생성할 수 있는가?