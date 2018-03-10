Requirements:
	python 3.5 or higher
	pip libraries: If not present use, pip install library_name
		requests
		html.parser
		sys
		ast
	Configuration Files: These Files contain list Used during Programme execution
		bad_data : Data such as \n or \t that need not be scraped
		Stopwords: Tags such as script and style The data within which is not relevant
		Specialwords: Tags such as b,h1 where data length is < 10 but are relevant to information
		In case of additional information to any of these tags, include tags in files as described

Navigate to working Directory and Run using command Line arguments:
	Windows:python main.py ~url
		Example: python main.py https://distill.pub/2017/feature-visualization/
	Linux:  python3 main.py ~url
		Example: python3 main.py https://distill.pub/2017/feature-visualization/

NOTE: Output File Is opened in append mode everytime, Hence New request will be appended in the output file
