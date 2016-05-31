# Batch Generate PDFs

This Python script will generate pdf files if it is given a latex template file and csv file consisting of list of items to be entered

### Latex File Template
Items which are required to be replaced need to be written as `$PARAM$`. Let's look at the following file
 
```Latex
\documentclass[12pt]{article}
\setlength\parindent{0pt}
\begin{document}
	This is to certify that\\
	First Name - $PARAM$\\
	Last Name - $PARAM$\\
	has written this document
\end{document}
```

The `$PARAM$` will be replaced by the corresponding entries in the csv file

### CSV File Template
Each row will consist of arguments which will be put in 1 latex document. Therefore, number of rows in the csv file should be equal to the number of documents to be generated.

```
James,Howard,56,Male
Lucy,Smith,45,Female
Mallory,Greg,18,Male
```
In this example, three documents can be created but not more

### Usage
This is the usage script 
`python pyscript <template file name> <csv file name> <number of documents to be generated>`
* First argument : Name of template file. It should be in `.tex` format
* Second argument : Name of the csv file
* Third argument : Number of documents to be generated. It should not be more than the number of rows of the csv file

### Output
PDF files will be generated with the name `certificate_<file number>.pdf`

### Sample Running String
Run the following script to get an understanding
`python pyscript.py sample_files/template.tex sample_files/namelist.csv 4`
