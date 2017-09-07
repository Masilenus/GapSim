from __future__ import print_function
import classes

def fill_street(iter):
	s_taken_ls = [0,]
	n = 0
	street = classes.Street(100)
	while n < iter:
		x = n

		car = classes.Car_random()


		if street.get_s_taken() + car.get_length() < street.get_space():
			street.update_s_taken(car.get_length())
			s_taken = street.get_s_taken()
			s_taken_ls.append(s_taken)
			n += 1

		else:
			n = 101
			print("No more street space after %d iterations." % x)

	print(s_taken_ls)
	return s_taken_ls

