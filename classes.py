class Bottle:
	def __init__(self,volume,material):
		self.volume = volume
		self.material = material
		
	def fill_bootle(self):
		"""Füllt die Flache bis sie voll ist"""
		start = 0.0
		while start < self.volume:
			print("#")
			start += 0.2
	
	def __str__(self):
		return "Die Flasche ist aus {} und fasst {} Liter".format(self.material,self.volume)

help(Bottle)
wasserflasche = Bottle(1.0, "Glas")
#print(wasserflasche)