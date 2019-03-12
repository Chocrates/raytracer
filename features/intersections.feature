Feature: Intersection data structure tests
	Scenario: An intersection encapsulates t and object
		Given s sphere()
		When i intersection(3.5,s)
		Then i.t = 3.5
			And i.shape = s

	Scenario: Aggregating intersections
		Given s sphere()
			And i1 intersection(1,s)
			And i2 intersection(2,s)
		When xs intersections(i1,i2)
		Then xs.count = 2
			And xs[0].t = 1
			And xs[1].t = 2

