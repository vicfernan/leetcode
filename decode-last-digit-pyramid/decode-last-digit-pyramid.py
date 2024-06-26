def last_numbers_pyramid(number):
	result = []
	current = 1
	line = 1

	while current <= number:
		start = current
		end = start + line - 1
		result.append(end)
		current = end + 1
		line += 1

	return result



def decode(message_file):
	decoded_words = []
	unshorted_final_list = []
	shorted_final_list = []

	with open(message_file, 'r') as file:
		lines = file.readlines()
		expected_numbers = last_numbers_pyramid(len(lines))
		for line in lines:
			parts = line.strip().split()
			number = int(parts[0])
			if int(parts[0]) in expected_numbers:
				unshorted_final_list.append(parts)
		shorted_final_list = sorted(unshorted_final_list, key=lambda x: int(x[0]))
		decoded_message = [item[1] for item in shorted_final_list]
	decoded_message = ' '.join([item[1] for item in shorted_final_list])
	
	return decoded_message

# Assuming the file 'encoded_message.txt' exists in the current directory
decoded_message = decode('coding_qual_input.txt')
print(decoded_message)

