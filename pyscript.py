import csv
import sys
import subprocess

def main():
	# Checking if valid argument list
	if len(sys.argv) < 4:
		print "Usage : python pyscript <template file name> <csv file name> <number of documents to be generated>"
		sys.exit()

	# Checking if given template is a tex file or not
	if sys.argv[1][-4:] != '.tex':
		print "Invalid template file!"
		sys.exit()

	# Checking is given database is a csv file or not
	elif sys.argv[2][-4:] != '.csv':
		print "Invalid csv file!"
		sys.exit()

	# Opening csv file
	csvf 		= open(sys.argv[2], 'rb')
	rd 		= csv.reader(csvf)
	csv_list 	= map(tuple, rd)

	# Getting number of documents to be generator
	doc_num = int(sys.argv[3])

	for i in xrange(doc_num):

		# Creating the tex file which is about to be generated from the template
		file_name 	= sys.argv[1][0:-4] + "_" + str(i+1)
		file_name_tex 	= file_name + ".tex"
		file_new 	= open(file_name_tex, "wb")

		# Opening the template file
		template_file = open(sys.argv[1],'r')

		# Parameter index in the csv file
		j = 0

		# Copying the template line by line and replacing the parameters
		for line in template_file:
			if line.find('$PARAM$') is -1:
				file_new.write(line)

			else:
				file_new.write(line.replace('$PARAM$', csv_list[i][j]))
				j = j + 1

		template_file.close()
		file_new.close()

		# Generating the pdf from the newly generated latex file
		sys_call1 = ["pdflatex", file_name]
		sys_call2 = ["rm", file_name + ".log", file_name + ".aux"]
		
		subprocess.call(sys_call1)
		subprocess.call(sys_call2)

if __name__ == "__main__":
	main()
