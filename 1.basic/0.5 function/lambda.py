# 람다
# 메모리 절약, 가독성, 코드 간결
# 함수는 객체 생성 -> 리소스(메모리) 할당
# 람다는 즉시 실행 함수(Heap 초기화) -> 메모리 초기화
# 남발 시 가독성 오히려 감소


def mul_func(x, y):
	return x * y


lambda_mul_func = lambda x, y: x * y
print(lambda_mul_func(50, 50))  # 2500


def func_final(x, y, func):
	print(x * y * func(100, 100))


func_final(10, 20, lambda x, y: x * y)  # 2000000
