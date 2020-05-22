class City:
	name = ""
	country = ""
	elevation = 0 
	population = 0

# create a new instance of the City class and
# define each attribute
city1 = City()
city1.name = "Cusco"
city1.country = "Peru"
city1.elevation = 3399
city1.population = 358052

# create a new instance of the City class and
# define each attribute
city2 = City()
city2.name = "Sofia"
city2.country = "Bulgaria"
city2.elevation = 2290
city2.population = 1241675

# create a new instance of the City class and
# define each attribute
city3 = City()
city3.name = "Seoul"
city3.country = "South Korea"
city3.elevation = 38
city3.population = 9733509

def maxelevationcity(minpopulation):
	returncity = City()
	if city1.population >= minpopulation:
		returncity = city1
	if city2.population >= minpopulation:
		if city2.elevation > returncity.elevation:
			returncity = city2
	if city3.population >= minpopulation:
		if city3.elevation > returncity.elevation:
			returncity = city3
	if returncity.name:
		return "{}, {}".format(returncity.name, returncity.country)
	else:
		return ""
		
# zunächst wird wird city1 geprüft ob minpop. Falls ja wird city2 geprüft. Wenn city2 auch minpop erfüllt. Wenn ja wird die Höhe der bisherigen returncity mit city2 Höhe verglichen. Ist city2 höher, wird city2 returncity. wenn nicht bleibt es city1. Dann das ganze mit city3.
print(maxelevationcity(100000)) # Should print "Cusco, Peru"
print(maxelevationcity(1000000)) # Should print "Sofia, Bulgaria"
print(maxelevationcity(10000000)) # Should print ""