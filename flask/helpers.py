

#prints objects neatly on html- just for testing
def pretty_print_objects(objectArray):
	newString = ""
	for item in objectArray:
		newString += "<li>"
		newString += str(item)
		newString += '\n\n'
		newString += '</i><br></br>'
	return newString	

