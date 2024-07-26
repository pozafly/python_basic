# 모듈을 모아둔 것을 package라고 함.
# 파이썬은 패키지로 분할 된 개별적인 모듈로 구성.
# 상대경로 : ..(부모), .(현재 디렉토리)
# __init__.py는 Python 3.3 부터는 없어도 패키지로 인식
#    -> 가져다 쓸 수 있는 모듈을 명시해둔다.
#    -> 단, 하위 호환을 위해 작성 추천

import sub.sub1.module1
import sub.sub2.module2

# 사용
sub.sub1.module1.mod1_test1()  # Path :  /Users/pozafly/Documents/dev/playground/python_basic/0.8 package/sub/sub1/module1.py
sub.sub1.module1.mod1_test2()  # Path :  /Users/pozafly/Documents/dev/playground/python_basic/0.8 package/sub/sub1/module1.py

sub.sub2.module2.mod2_test1()  # Path :  /Users/pozafly/Documents/dev/playground/python_basic/0.8 package/sub/sub2/module2.py
sub.sub2.module2.mod2_test2()  # Path :  /Users/pozafly/Documents/dev/playground/python_basic/0.8 package/sub/sub2/module2.py


# 근데 가져올 때 너무 길다.
from sub.sub1 import module1
from sub.sub2 import module2 as m2  # alias

module1.mod1_test1()
m2.mod2_test1()


# import * (근데 잘 안쓴다. 전부 가져오는 건 비효율 적인 메모리 사용임)
from sub.sub1 import *
from sub.sub2 import *

module1.mod1_test1()
module2.mod2_test1()
# 이렇게 호출이 잘 된다.
# 여기서 import *을 잘 쓸 수 있는 이유는 __init__에 정의된
# __all__ 때문이다. __all__ 안에 모듈 네임이 지정되어 있다.
