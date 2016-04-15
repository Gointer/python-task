import datetime


def is_little_endian(A, B, C):
	is_month = False
	is_year = False
	is_day = False

	if 1 <= int(B) <= 12:  # month
		is_month = True

	if 0 <= int(C) <= 999:  # year
		is_day = True

	if 1 <= int(A) <= 31:  # day
		is_year = True

	return_value = is_month and is_year and is_day

	return return_value


def is_big_endian(A, B, C):
	is_month = False
	is_year = False
	is_day = False

	if 1 <= int(B) <= 12:  # month
		is_month = True

	if 1 <= int(C) <= 31:  # day
		is_day = True

	if 0 <= int(A) <= 999:  # year
		is_year = True

	return_value = is_month and is_year and is_day

	return return_value


def is_middle_endian(A, B, C):
	is_month = False
	is_year = False
	is_day = False

	if 1 <= int(B) <= 31:  # day
		is_month = True

	if 0 <= int(C) <= 999:  # year
		is_day = True

	if 1 <= int(A) <= 12:  # month
		is_year = True

	return_value = is_month and is_year and is_day

	return return_value


def get_date(A, B, C):
	date = None

	if is_big_endian(A, B, C):
		date = datetime.date(int(A)+2000, int(B), int(C))	
	elif is_little_endian(A, B, C):
		date = datetime.date(int(C)+2000, int(B), int(A))
	elif is_middle_endian(A, B, C):
		date = datetime.date(int(C)+2000, int(A), int(B))

	date_str = date.strftime("%Y-%m-%d")

	return date_str


if __name__ == "__main__":
	with open('input.txt', 'r') as input_file, open('output.txt', 'w') as output_file:

		for line in input_file:
			A, B, C = line.split('/')

			try:
				date = get_date(A, B, C)
				output_file.write(date + '\n')
			except Exception:
				output_file.write("is illegal \n")

