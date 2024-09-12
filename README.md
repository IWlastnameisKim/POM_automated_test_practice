POM 구조로 테스트 자동화 스크립트를 업로드 하는 곳입니다.

* 기본 구성은 아래와 같이 했어요

- Conftest.py
- Common
  ㄴ TestBase.py
- Pages
  ㄴ Homepage.py
  ㄴ Loginpage.py
- tests
  ㄴ test_테스트스크립트_1
  ㄴ test_테스트스크립트_2
  ㄴ test_테스트스크립트_3
  ㄴ test_테스트스크립트_4
  .
  .
  .
  .


  * Conftest.py 는 셀레니움 및 pandas 등 전체적으로 사용 해야 하는 모듈을 셋팅 해요
  * TestBase.py 는 자주 사용하는 함수나 엘레멘트의 위치를 모아놓고, 테스트 스크립트에 상속해서 재사용할 수 있게 해요
  * Pages 디렉토리 내의 .py 들은 각 페이지에서 고유하게 가지고 있지만 재사용 해야하는 엘레멘트의 위치나 함수를 모아놓고 있어요. 테스트 스크립트 내 객체를 생성하여 재사용 하도록 하고 있어요.
  * Chormedriver 는 conftest.py에서 install하여 사용하도록 하고 있어요
  * pip install 을 통해 설치가 필요한 것들이 있어요! (ex : selenium , pandas , pytest, pytest-dependency 등)
