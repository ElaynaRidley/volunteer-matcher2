def readFile(filename):
	'''
		Read contents of file whose name is filename, and return it.
		Return empty string on error.
	'''
	try:
		f = open(filename,'r')
		text = f.read()
		f.close()
		return text
	except:
		print('Error in readfile:  filename='+filename)
		return ''

def getDatabase():
     lines = readFile("database.txt").split("\n")
     
     global orgs
     orgs = []              # list of all organizations.  this is a list of tuples
     current_name = ""   # the name of the current organization we are reading in
     current_list = []   # the current organization's list of activities
     
     for line in lines:
     	if line.startswith("name:"):
     		if len(current_name) > 0:
     			orgs.append([current_name, current_list])
     		current_name = line[5:]
     		current_list = []
     	elif len(line) > 0:
     		current_list.append(line)
     
     orgs.append([current_name, current_list])

def help():
        print("Commands:\n---------------------")
        print("    stop -- end this program")
        print("    list -- list all the organizations")
        print("    find X -- find all organizations with a partial name X")
        print("    list sorted -- list all the organizations' names in sorted order")
        print('    find activity x -- find all organizations with an activity that partially matches x')
        print('    describe x -- list all activities of organization x')
              

def list(do_sorted=False):
        if do_sorted==False:
                for i in range(len(orgs)):
                        print(str(i+1)+'. '+str(orgs[i][0]))
        if do_sorted==True:
                newlist = []
                for i in range(len(orgs)):
                        newlist.append(str(orgs[i][0]))
                for i in range(len(newlist)-1):
                        for j in range(i + 1, len(newlist)):
                                if newlist[i] > newlist[j]:
                                        temp = newlist[i]
                                        newlist[i] = newlist[j]
                                        newlist[j] = temp
                for i in range(len(newlist)):
                        print(str(i+1)+'. '+str(newlist[i]))


def find(partial_org_name):
        pass

def find_activity(activity):
        pass

def describe(org_name):
        pass

def main():
        while True:
                command = input('Enter Command: ')
                if command == 'stop':
                        break
                elif command == 'help':
                        help()
                elif command == 'list':
                        list()
                elif command == 'list sorted':
                        list(True)
                elif command.startswith('find'):
                        find(command[5:])
                elif command.startswith('find activity'):
                        find_activity(activity)
                elif command.startswith('describe'):
                        describe(org_name)
                else:
                        print('Unknown command! Try help')
                


#  this is the beginning of the main code
getDatabase()
main()
