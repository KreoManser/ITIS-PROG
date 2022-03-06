from matplotlib import pyplot as plt


def distance(key_first: tuple, key_second: tuple):
	"""

	:param key_first: Координаты 1-го дома
	:param key_second: Координаты 2-го дома
	:return: bool: Проверка на расстояние 1 км
	"""
	if (((key_first[0] - key_second[0]) ** 2 + (key_first[1] - key_second[1]) ** 2) ** 0.5) < 0.5:
		return True
	return False


def distance2(key_first: tuple, key_second: tuple):
	"""

	:param key_first: Координаты 1-го дома
	:param key_second: Координаты 2-го дома
	:return: bool: Проверка на расстояние 500 метров
	"""
	if (((key_first[0] - key_second[0]) ** 2 + (key_first[1] - key_second[1]) ** 2) ** 0.5) > 1:
		return True
	return False


def read_data(path):
	"""
	Чтение файла и сохранение в словаре вида: ключ адрес, значения это кортеж (координата Х, коордианата Y, площадь)
	Пример: {'пр-кт Фатыха Амирхана д 91Б': (5.73063, 11.8712, 2095.0), ... }
	Args:
		path (str): путь к файлу
	Returns:
		dict: ключ адрес, значение (x, y, площадь)
	"""
	database = {}
	with open(path) as file:
		for line in file:
			address, x, y, s = line.strip().split('\t')
			database[address] = float(x), float(y), int(s)
			# data = line.split('\t')
			# database[data[0]] = tuple(map(float, data[1:]))
	return database


def task1(database: dict):
	"""
	Задача 1
	Args:
		database (dict): изначальный датасет словарь, ключ адрес, значение (x, y, площадь)
		помимо database могут быть любые другие аргументы
	Returns:
		list: координаты дома (x, y)
	"""
	key_list = list(database.keys())
	size = len(database)
	top_address = {}
	for key1 in range(size):
		top_address[key_list[key1]] = 0
		for key2 in range(size):
			if distance(database[key_list[key1]], database[key_list[key2]]):
				top_address[key_list[key1]] += 1  # сколько домов в округе(радиусе)
	top_house = max(top_address.keys(), key=lambda x: top_address[x])
	print(f'Task1: {[database[top_house][0], database[top_house][1]]}')
	return [database[top_house][0], database[top_house][1]]


def task2(database: dict):
	"""
	Задача 2
	Args:
		database (dict): изначальный датасет словарь, ключ адрес, значение (x, y, площадь)
		помимо database могут быть любые другие аргументы
	Returns:
		list: координаты домов [(x1,y1), (x2,y2) ... (xn,yn)]
	"""
	key_list = list(database.keys())
	size = len(database)
	top_address = {}
	for key1 in range(size):
		top_address[key_list[key1]] = 0
		for key2 in range(size):
			if distance(database[key_list[key1]], database[key_list[key2]]):
				top_address[key_list[key1]] += 1  # сколько домов в округе(радиусе)
	top_house = max(top_address.keys(), key=lambda x: top_address[x])
	start = dict(list(sorted(top_address.items(), key=lambda x: x[1], reverse=True)))
	key_start = list(start.keys())
	top_10 = [top_house]
	# print(top_house, f'------ {top_address[top_house]} ------', database[top_house])
	for key1 in key_start[1:]:
		if all(distance2(database[key1], database[checked]) for checked in top_10):
			top_10.append(key1)
			if len(top_10) >= 10:
				break

	answer = []
	for i in top_10:
		answer.append((database[i][0], database[i][1]))
	print(f'Task2: {answer}')
	return answer


def task3(database: dict):
	"""
	Задача 3
	Args:
		database (dict): изначальный датасет словарь, ключ адрес, значение (x, y, площадь)
		помимо database могут быть любые другие аргументы
	Returns:
		list: координаты домов [(x1,y1), (x2,y2) ... (xn,yn)]
	"""
	key_list = list(database.keys())
	size = len(database)
	top_address = {}
	for key1 in range(size):
		top_address[key_list[key1]] = 0
		for key2 in range(size):
			if distance(database[key_list[key1]], database[key_list[key2]]):
				top_address[key_list[key1]] += round(database[key_list[key2]][2]*0.7/18)  # расчет жильцов
	top_house = max(top_address.keys(), key=lambda x: top_address[x])
	start = dict(list(sorted(top_address.items(), key=lambda x: x[1], reverse=True)))
	key_start = list(start.keys())
	top_15 = [top_house]

	for key1 in key_start[1:]:
		if all(distance2(database[key1], database[checked]) for checked in top_15):
			top_15.append(key1)
			if len(top_15) >= 15:
				break

	answer = []
	for i in top_15:
		answer.append((database[i][0], database[i][1]))
	print(f'Task3: {answer}')
	return answer


def plot(database, best_coords):
	"""
	НЕ МЕНЯТЬ КОД!
	Отрисовка точек 2D
	Args:
		database (dict): изначальный датасет словарь, ключ адрес, значение (x, y, площадь)
		best_coords (list): для задачи 1 это (x, y), для задачи 2-3 это [(x1,y1), (x2,y2) ... (xn,yn)]
	"""
	plt.close()
	fig, ax = plt.subplots(figsize=(8, 8))
	plt.plot([coord[0] for coord in database.values()],
			[coord[1] for coord in database.values()], '.', ms=5, color='k', alpha=0.5)
	if isinstance(best_coords[0], tuple):
		for x, y in best_coords:
			circle = plt.Circle((x, y), 0.5, color='r', fill=False, zorder=2)
			ax.add_patch(circle)
		plt.plot([coord[0] for coord in best_coords],
				[coord[1] for coord in best_coords], '.', ms=15, color='r')
	elif isinstance(best_coords[0], float):
		x, y = best_coords
		circle = plt.Circle((x, y), 0.5, color='r', fill=False, zorder=2)
		ax.add_patch(circle)
		plt.plot(*best_coords, '.', ms=15, color='r')
	else:
		raise ValueError("Проверь, что подаёшь список кортежей или кортеж из двух координат")
	plt.show()


def homework():
	path = "buildings.txt"  # у меня не работает без txt(проблема в маке)
	database = read_data(path)

	best_task1 = task1(database)
	plot(database, best_task1)

	top10_task2 = task2(database)
	plot(database, top10_task2)

	top15_task2 = task3(database)
	plot(database, top15_task2)


if __name__ == '__main__':
	homework()
	# print(read_data("buildings.txt"))
