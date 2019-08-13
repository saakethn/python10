# WRITE FILE - 

	# If the file is not present, it will create file and write
	# Write - will remove previous data and start writing
	# Write - will take only one string

# 1. write()
# 2. writelines()


with open('sample1.txt','w') as file:
	# file.write('this is first writing operation')  # Creates a file and write the given text

	# file.write(' writing again')
	# file.write('  writing again')  

# If we mention write after write - all data will be written BUT if we comment above after writing and write again previous data will be removed
 	 file.write('removing previous data')

# writelines()

with open('sample.txt','w') as file:
	# file.write('this is first operation')  
	# file.write('raining in hyd')

# if we comment above and write the below one, it will delete previous data
	file.writelines(['this is first writing\n','raining in hyd\n','its python class\n'])


# SAME AS ABOVE FOR APPEND

with open('sample.txt','a') as file:
 	file.writelines(['this is first writing\n','raining in hyd\n','its python class'])
 	