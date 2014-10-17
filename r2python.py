
import sys


def preparePython(pyfile):
	''' Adds a function to the python file to handle calls from R'''
	PythFile = open(pyfile, "a")
	HandleFunction = """\nif __name__ == "__main__":\n\tcommand= sys.argv[1] + "("" + "","".join(sys.argv[2:]) + "")"\n\teval(command)"""
	PythFile.write(HandleFunction)
	
	
	
if __name__ == "__main__":
	if(str(sys.argv[1])[0]=="-"):
		print "indiirect Call"
	else:
		preparePython(sys.argv[1])
		