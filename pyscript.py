import csv
import sys
import subprocess

def main():
	# Checking if valid argument list
	if len(sys.argv) < 4:
		print "Usage : python pyscript <template file name> <csv file name> <number of documents to be generated>"
		sys.exit()

	# Opening csv file
	csvf 		= open(sys.argv[2], 'rb')
	rd 		= csv.reader(csvf)
	csv_list 	= map(tuple, rd)

	# Getting number of documents to be generater
	doc_num = int(sys.argv[3])

	j = 0

	for i in xrange(doc_num):

		# Creating the tex file which is about to be generated from the template
		file_name = "certificate_" + str(i) + ".tex"
		file_new = open(file_name, "wb")

		# Opening the template file
		template_file = open(sys.argv[1],'r')

		# Copying the template line by line and replacing the parameters
		for line in template_file:
			if line.find('$PARAM$') is -1:
				file_new.write(line)
			else:
				file_new.write(line.replace('$PARAM$', csv_list[i][j]))
				j = j + 1

		j = 0

		template_file.close()
		file_new.close()

		# Generating the pdf from the newly generated latex file
		sys_call = ["pdflatex", file_name]
		subprocess.call(sys_call)

if __name__ == "__main__":
	main()