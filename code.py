# капча
import random
import time

one = random.randint(1, 3)
two = random.randint(1, 3)
thr = random.randint(1, 3)
four = random.randint(1, 3)

print ("      " * 1000000)

if one == 1:
	print('red')
elif one == 2:
	print('green')
elif one == 3:
	print('yellow')

time.sleep(1)
print ("      " * 1000000)

if two == 1:
	print('red')
elif two == 2:
	print('green')
elif two == 3:
	print('yellow')

time.sleep(1)
print ("      " * 1000000)

if thr == 1:
	print('red')
elif thr == 2:
	print('green')
elif thr == 3:
	print('yellow')

time.sleep(1)
print ("      " * 1000000)

if four == 1:
	print('red')
elif four == 2:
	print('green')
elif four == 3:
	print('yellow')

time.sleep(1)
print ("      " * 1000000)

print('')

print(str(one) + str(two) + str(thr) + str(four))
print('1 = red, 2 = green, 3 = yellow')
print('')
print('Пожалуйста пройдите данную капчу!')

a = int(input('Первый цвет(число): '))
b = int(input('Второй цвет(число): '))
c = int(input('Третий цвет(число): '))
d = int(input('Четвёртый цвет(число): '))

if one == a:
	ai = 1
else:
	ai = 0

if two == b:
	ai2 = 1
else:
	ai2 = 0

if thr == c:
	ai3 = 1
else:
	ai3 = 0

if four == d:
	ai4 = 1
else:
	ai4 = 0

if ai == 1 or ai2 == 1 or ai3 == 1 or ai4 == 1:
	print('Вы прошли проверку на бота!')
if ai == 0 or ai2 == 0 or ai3 == 0 or ai4 == 0:
	print('Вы не прошли проверку на бота!')
	exit()
print('')
print('Добро пожаловать в систему!')
print('Эта была проверка капчи!')
print('')
ex = input('Нажмите пожалуйста на ENTER!')

if ex == "":
	exit()
else:
	while True:
		print('')
		print('Вы не нажали ENTER!')
		ex = input('Нажмите пожалуйста на ENTER!')
		if ex == "":
			print('Ура ты нажал ENTER!')
			exit()
		else:
			print('')
			print('Вы не нажали ENTER!')
