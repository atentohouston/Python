var = "ABCDEF"
print(var[:2])	# Up to index 2
# AB
print(var[2:])	# Ignore everything up to index 2
# CDEF
print(var[2:4])	# Everything between index 2 and 4 ("2" is counted)
# CD
print(var[-2:])	# Up to negative index 2 (last two characters)
# EF