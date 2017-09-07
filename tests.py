from __future__ import print_function
from random import choice
import classes


def fill_street(iter):
	s_taken_ls = [0,]
	n_cars_ls = []
	n = 0
	street = classes.Street(100)
	n_cars_ls.append(street.get_n_cars())

	while n < iter:
		x = n

		car = classes.Car_random()


		if street.get_s_taken() + car.get_length() < street.get_space():
			street.update_s_taken(car.get_length())
			s_taken_ls.append(street.get_s_taken())
			street.update_n_cars(1)
			n_cars_ls.append(street.get_n_cars())

			n += 1

		else:
			n = 101
			print("No more street space after %d iterations." % x)

	print(s_taken_ls, n_cars_ls)
	return [s_taken_ls, n_cars_ls]



def random50_street(iter):
	s_taken_ls = [50,]
	n_cars_ls = []
	n = 0
	street = classes.Street(100)
	street.update_n_cars(10)
	street.update_s_taken(50)
	n_cars_ls.append(street.get_n_cars())

	while n < iter:
		x = n

		car = classes.Car_random()

		if choice('ab') is 'b':
			if street.get_s_taken() + car.get_length() < street.get_space():
				street.update_s_taken(car.get_length())
				s_taken_ls.append(street.get_s_taken())
				street.update_n_cars(1)
				n_cars_ls.append(street.get_n_cars())

				n += 1

			else:
				n = 101
				print("No more street space after %d iterations." % x)

		else:
			street.update_s_taken(-1*car.get_length())
			s_taken_ls.append(street.get_s_taken())
			street.update_n_cars(-1)
			n_cars_ls.append(street.get_n_cars())

			n += 1


	#print(s_taken_ls, n_cars_ls)
	return [s_taken_ls, n_cars_ls]

