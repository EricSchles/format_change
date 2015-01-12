class Reformatter:
	def __init__(self,template,to_format):
		self.template = template
		self.to_format = to_format

	def process_formatting(self):
		form = []
		metrics = {
			"number_of_characters":0,
			"captialized_words":[],
			"numbers_present_on_line":False,
			"tab_after_word":[],
			"aligned":""
			}
		with open(self.template,"r") as f:
			#metrics are passed for each line.