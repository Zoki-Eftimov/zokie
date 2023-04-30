#!/usr/bin/python3

#Zoran Eftimov
#prof. Ski Kacoroski
#SEC444 - Automation/Configuration & Management
#4-29-2023

# Description: This script loops through all sections and prints out statements.
# Versioning
# Zoki 4 - 29 - 23: initial version v.01

# Globals
RESULTS = {'152.157.64.5': {'osmatch': {}, 'ports': [{'protocol': 'tcp', 'portid': '22', 'state': 'open', 'reason': 'syn-ack', 'reason_ttl': '49', 'service': {'name': 'ssh', 'method': 'table', 'conf': '3'}, 'cpe': [], 'scripts': []}, {'protocol': 'tcp', 'portid': '80', 'state': 'open', 'reason': 'syn-ack', 'reason_ttl': '49', 'service': {'name': 'http', 'method': 'table', 'conf': '3'}, 'cpe': [], 'scripts': []}, {'protocol': 'tcp', 'portid': '113', 'state': 'closed', 'reason': 'reset', 'reason_ttl': '51', 'service': {'name': 'ident', 'method': 'table', 'conf': '3'}, 'cpe': [], 'scripts': []}, {'protocol': 'tcp', 'portid': '443', 'state': 'open', 'reason': 'syn-ack', 'reason_ttl': '49', 'service': {'name': 'https', 'method': 'table', 'conf': '3'}, 'cpe': [], 'scripts': []}], 'hostname': [], 'macaddress': None, 'state': {'state': 'up', 'reason': 'syn-ack', 'reason_ttl': '49'}}, 'runtime': {'time': '1680459977', 'timestr': 'Sun Apr  2 11:26:17 2023', 'elapsed': '15.08', 'summary': 'Nmap done at Sun Apr  2 11:26:17 2023; 1 IP address (1 host up) scanned in 15.08 seconds', 'exit': 'success'}, 'stats': {'scanner': 'nmap', 'args': '/usr/bin/nmap -v -oX - -sS 152.157.64.5', 'start': '1680459961', 'startstr': 'Sun Apr  2 11:26:01 2023', 'version': '7.80', 'xmloutputversion': '1.04'}, 'task_results': [{'task': 'Ping Scan', 'time': '1680459962', 'extrainfo': '1 total hosts'}, {'task': 'Parallel DNS resolution of 1 host.', 'time': '1680459972'}, {'task': 'SYN Stealth Scan', 'time': '1680459976', 'extrainfo': '1000 total ports'}]}

# Functions
def main():
    "Loop through all the sections"
    for i in range(1,9):
        cmd = 'section' + str(i)+ '()'
        eval(cmd)
        print('\n')

def section1():
    print('*** Section 1 ***')
#   print("### Should print '3'") Changed the '>' with '<' so it prints 3.
    a1 = 1
    a2 = 5
    if a1 < a2:
        print('3')
    else:
        print('4')

def section2():
	print('*** Section 2 ***')
#	print("### Should print 'cat'") I changed (a2[1]) to (a2[0]), so it prints cat, that's the index of cat.
	a2 = ['cat', 'dog', 'bird']
	print(a2[0])

def section3():
    print('*** Section 3 ***')
#   print("### Should print 'Cutie my cat loves her cat door'") - added "cut,"cat" in the line mystring.replace.
    mystring = "Cutie my cat loves her cut door"
    mystring = mystring.replace('cut','cat')
    print(mystring)


def section4():
    print('*** Section 4 ***')
#   The different order is because Dictionaries in Python are unordered
#   Some of the items in mypets were out of order and I switched the order, so it prints correctly, the keys and values were also swapped, so that was corrected as well.
    mypets = {'Mido':'cat', 'Timber':'dog', 'Whiskers':'mouse', 'Tweety':'bird'}
    for k,v in mypets.items():
        print(k + ' is my ' + v)

def section5():
    print('*** Section 5 ***')
#   The base case in the recursive is returning 0, replaced it return 1; the return x should multiply instead of add.
    def fact(x):
        if x == 1:
            return 1
        else:
            return x * fact(x - 1)
    res = fact(5)
    print(res)

def section6():
    global RESULTS
    print('*** Section 6***')
#   Added global RESULTS, so it reads the data from RESULTS, then added the extrainfo key in the third item of task_results list to get the ports scanned info.
    print('Ports scanned: '+ RESULTS['task_results'][2]['extrainfo'])


def section7():
    global RESULTS
    print('*** Section 7 ***')
#   global RESULTS added again + the code was trying to print the wrong item from the dictionary, task results changed with runtime and elapsed.
    print('Elapsed time: '+ RESULTS['runtime']['elapsed'])

def section8():
    global RESULTS
    print('*** Section 8 ***')
# There was a mistake in the loop statement. First, I fixed the loop statement, so it correctly defines the variable port to be used inside the loop and eliminates the error, then I added service name to be dictionary for each port in the 'ports'.
    for port in RESULTS['152.157.64.5']['ports']:
        service_name = port['service']['name']
        print('Service ' + service_name + ' on port ' + port['portid'])


# Run main() if script called directly
if __name__ == "__main__":
        main()

