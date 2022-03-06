from Penguin import *
"""
Content.py is where we actually handle our raw data for manipulation
can handle any data type but is by default unordered.
"""
def update(content, key, value):
	content[key] = value
	
class content_import():
	def content():
		content = {
			"data1" : {"subgroup1": 2},
			"data2" : {"subgroup1": "2"},
			"data3" : {"subgroup1": {"erik": 1}
			}
		}
		return content
		
content = content_import.content()
#update(content, "122", {2:3})

test = Parser.file_reader('write.txt')
print(test)

n()

Parser.file_writer('write.txt', test, str(content), 'w')
print(test)
