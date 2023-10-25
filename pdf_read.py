from pdfquery import PDFQuery
import re

def check_presence(name, list1):
	for index, item in enumerate(list1):
		if name in item:
			return index
	return None

def check_format(name, list1):
	for index, item in enumerate(list1):
		if re.match(date_pattern, item.strip()):
			return item.strip()
	return None

def get_name_from_list(txt_lst, list1):
	result = ""
	for elm in txt_lst:
		index = check_presence(elm, list1)
		if index != None:
			result = result + ";" + list1[index] 
	return result

def get_from_Box (name1, name2, list1):
	idx1= idx2 = 0
	for index, elm in enumerate(list1):
		if name1 in elm:
			idx1 = index
	for index, elm in enumerate(list1):
		if name2 in elm:
			idx2 = index
	result = ""
	print (idx1)
	print (idx2)
	if idx1 > 0 and idx2 > 0:
		for i in range(idx1, idx2):
			result = result + list1[i]
	return result

ListSpecs = {"SAE","ISO","UNE-EN","DIN","IEC","LIEBERR","EC-","STD","ENS","MSL","STD","JIS","JASO","KES","ASAE","TL","CiA-","GE&ER"}
ListResult = {"Passs","Fail","Measured","Not Applicable"}
ListTestType = {" Durability","Performance","Climatics","IP","External","TestPlan","Electronics","Others","SaltSpray","Humid."}
ListType = {"Panoramic System","Pantagraph System","Tandem System","Single System","Motor","Emotor","ECU,PCA","Wiper arm","Wiper blade","SYS Part","BEPart","Tank","Maure","SerialPart"}


pdf = PDFQuery('Inf_00118_TEST_PLAN_319-9234-20-00E.pdf')
pdf.load()

# Use CSS-like selectors to locate the elements
text_elements = pdf.pq('LTTextBoxHorizontal:contains("Test report")')
text_box_elements = pdf.pq('LTTextBoxHorizontal')
text_box = [t.text for t in text_box_elements]
text_line_elements = pdf.pq('LTTextLineHorizontal')
text_line_cplt = [t.text for t in text_line_elements]
text_line = [item for item in text_line_cplt if item.strip()]
complete_list = text_box + text_line
# Extract the text from the elements
#Extraccion del test Report
text = [t.text for t in text_elements]
print("Test report nr.\n")
TestReportNr = text[1]
print (TestReportNr + '\n')
#Extraccion del HRE
print("HRE nr\n")
index = check_presence("HRE", complete_list)
if index != None:
	HREvalue =  (complete_list[index].strip() + complete_list[index + 1].strip())
else:
    HREvalue = None
print(HREvalue + '\n')
#Extraccion de la fecha
date_pattern = r'\d{2}/\d{2}/\d{4}'
ReportDate = check_format(date_pattern,complete_list)
print(ReportDate + '\n')

#test spec
TestSpec = get_name_from_list(ListSpecs, complete_list)
print(TestSpec + '\n')
#Result
TEstResult = get_name_from_list(ListResult, complete_list)
print(TEstResult + '\n')

#Test type
TestType = get_name_from_list(ListTestType, complete_list)
print(TestType + '\n')

#Type
Type = get_name_from_list(ListType, complete_list)
print(Type + '\n')

#Tested components
print (text_box)
print ("Resultado tested components")
TestedCmp = get_from_Box("TESTED COMPONENTS", "TEST METHOD", text_box)


import glob

folder_path = '/path/to/your/folder'  # Replace with the actual folder path

# Get a list of files with a ".txt" extension in the folder
files = glob.glob(os.path.join(folder_path, '*.txt'))

print("List of .txt files:")
for file in files:
    print(file)
