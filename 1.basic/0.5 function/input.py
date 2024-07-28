name = input('Enter Your Name: ')
grade = input('Enter Your Grade: ')
company = input('Enter Your Company name: ')

print(name, grade, company)


# input으로 받아드리는 값은 무조건 str 형이다.
name = input('Enter Your Name: ')
grade = input('Enter Your Grade: ')
company = input('Enter Your Company name: ')

print(type(name), type(grade), type(company))  # <class 'str'> <class 'str'> <class 'str'>


# 형변환 해주어야 함.
first_number = int(input('Enter number: '))
second_number = int(input('Enter number: '))

total = first_number + second_number
print('first_number + second_number: ', total)


# format으로 받기
print(
	'FirstName - {0}, LastName - {1}'.format(
		input('Enter first name: '), input('Enter second name: ')
	)
)


# 예외 처리
try:
	n = int(input('input: '))
	print('Ok. Your number is : ', n)
except ValueError:
	print('This is not a number')


# 올바른 값 입력 완료까지 지속
while True:
	try:
		n = int(input('Enter a number: '))
		break
	except ValueError:
		print('This is not a number')
print('Ok. Your number is : ', n)
