class testclass2(object):
	
	
	def __init__(self, value):
		print "Class 2 initiated."
		self.value = value
	
	def __iter__(self):
		
		class iterclass:
			
			
			def __init__(self, value):
				print "Iterator object within testclass2 is initiated."
				self.value = value
			
			def next(self):
				if self.value <= 20:
					print "Iterator object processing the next() function."
					self.value += 1
					return self.value
				raise StopIteration()
		
		return iterclass(self.value) 

a = testclass2(10)
for i in a:
	print i
