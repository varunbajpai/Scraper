#Requirements:
	python 3.5 or higher
	#pip libraries: if not present use, pip install library_name
		requests
		html.parser
		sys
		ast
	#Configuration Files: These Files contain list Used during Programme execution
		bad_data : Data such as \n or \t that need not be scraped
		stopwords: Tags such as script and style The data within which is not relevant
		specialwords: Tags such as b,h1 where data length is < 10 but are relevant to information
		In case of additional information to any of these tags, include tags in files as described

#NAVIGATE TO WORKING DIRECTORY AND RUN USING COMMAND LINE ARGUMENTS:
	Windows:python main.py ~url
		Example: python main.py https://distill.pub/2017/feature-visualization/
	Linux:  python3 main.py ~url
		Example: python3 main.py https://distill.pub/2017/feature-visualization/

NOTE: Output File Is opened in append mode everytime, So if sending a new request data for that url will be appended to the existing file
For seperate files for separate URL either delete the files or moove to other location
