(Pdb) b 5
Breakpoint 1 at /home/ubuntu/zokie/Week3ZokiEftimov/datastructure.py:5
(Pdb) c
> /home/ubuntu/zokie/Week3ZokiEftimov/datastructure.py(5)<module>()
-> print(results)
(Pdb) len(results)
4
(Pdb) for k1,v1 in results.items():
*** IndentationError: expected an indented block after 'for' statement on line 1
(Pdb) interact
*interactive*
>>> for k1,v1 in results.items():
... print(k1,v1)
Traceback (most recent call last):
  File "/usr/lib/python3.10/code.py", line 63, in runsource
    code = self.compile(source, filename, symbol)
  File "/usr/lib/python3.10/codeop.py", line 153, in __call__
    return _maybe_compile(self.compiler, source, filename, symbol)
  File "/usr/lib/python3.10/codeop.py", line 70, in _maybe_compile
    compiler(source + "\n", filename, symbol)
  File "/usr/lib/python3.10/codeop.py", line 118, in __call__
    codeob = compile(source, filename, symbol, self.flags, True)
  File "<console>", line 2
    print(k1,v1)
    ^
IndentationError: expected an indented block after 'for' statement on line 1
>>> for k1,v1 in results.items():
...     print(k1,v1)
...     print('\n')
... results['152.157.64.5']
Traceback (most recent call last):
  File "/usr/lib/python3.10/code.py", line 63, in runsource
    code = self.compile(source, filename, symbol)
  File "/usr/lib/python3.10/codeop.py", line 153, in __call__
    return _maybe_compile(self.compiler, source, filename, symbol)
  File "/usr/lib/python3.10/codeop.py", line 70, in _maybe_compile
    compiler(source + "\n", filename, symbol)
  File "/usr/lib/python3.10/codeop.py", line 118, in __call__
    codeob = compile(source, filename, symbol, self.flags, True)
  File "<console>", line 4
    results['152.157.64.5']
    ^^^^^^^
SyntaxError: invalid syntax
>>> results['152.157.64.5']['ports']
[{'protocol': 'tcp', 'portid': '22', 'state': 'open', 'reason': 'syn-ack', 'reason_ttl': '49', 'service': {'name': 'ssh', 'method': 'table', 'conf': '3'}, 'cpe': [], 'scripts': []}, {'protocol': 'tcp', 'portid': '80', 'state': 'open', 'reason': 'syn-ack', 'reason_ttl': '49', 'service': {'name': 'http', 'method': 'table', 'conf': '3'}, 'cpe': [], 'scripts': []}, {'protocol': 'tcp', 'portid': '113', 'state': 'closed', 'reason': 'reset', 'reason_ttl': '51', 'service': {'name': 'ident', 'method': 'table', 'conf': '3'}, 'cpe': [], 'scripts': []}, {'protocol': 'tcp', 'portid': '443', 'state': 'open', 'reason': 'syn-ack', 'reason_ttl': '49', 'service': {'name': 'https', 'method': 'table', 'conf': '3'}, 'cpe': [], 'scripts': []}]
>>> for i1 in results['152.157.64.5']['ports']:
...     print(i1)
...     print('\n')
... for i1 in results['152.157.64.5']['ports']:
Traceback (most recent call last):
  File "/usr/lib/python3.10/code.py", line 63, in runsource
    code = self.compile(source, filename, symbol)
  File "/usr/lib/python3.10/codeop.py", line 153, in __call__
    return _maybe_compile(self.compiler, source, filename, symbol)
  File "/usr/lib/python3.10/codeop.py", line 70, in _maybe_compile
    compiler(source + "\n", filename, symbol)
  File "/usr/lib/python3.10/codeop.py", line 118, in __call__
    codeob = compile(source, filename, symbol, self.flags, True)
  File "<console>", line 4
    for i1 in results['152.157.64.5']['ports']:
    ^^^
SyntaxError: invalid syntax
>>> for i1 in results['152.157.64.5']['ports']:
...     print(i1['portid'])
...
(Pdb) results
{'152.157.64.5': {'osmatch': {}, 'ports': [{'protocol': 'tcp', 'portid': '22', 'state': 'open', 'reason': 'syn-ack', 'reason_ttl': '49', 'service': {'name': 'ssh', 'method': 'table', 'conf': '3'}, 'cpe': [], 'scripts': []}, {'protocol': 'tcp', 'portid': '80', 'state': 'open', 'reason': 'syn-ack', 'reason_ttl': '49', 'service': {'name': 'http', 'method': 'table', 'conf': '3'}, 'cpe': [], 'scripts': []}, {'protocol': 'tcp', 'portid': '113', 'state': 'closed', 'reason': 'reset', 'reason_ttl': '51', 'service': {'name': 'ident', 'method': 'table', 'conf': '3'}, 'cpe': [], 'scripts': []}, {'protocol': 'tcp', 'portid': '443', 'state': 'open', 'reason': 'syn-ack', 'reason_ttl': '49', 'service': {'name': 'https', 'method': 'table', 'conf': '3'}, 'cpe': [], 'scripts': []}], 'hostname': [], 'macaddress': None, 'state': {'state': 'up', 'reason': 'syn-ack', 'reason_ttl': '49'}}, 'runtime': {'time': '1680459977', 'timestr': 'Sun Apr  2 11:26:17 2023', 'elapsed': '15.08', 'summary': 'Nmap done at Sun Apr  2 11:26:17 2023; 1 IP address (1 host up) scanned in 15.08 seconds', 'exit': 'success'}, 'stats': {'scanner': 'nmap', 'args': '/usr/bin/nmap -v -oX - -sS 152.157.64.5', 'start': '1680459961', 'startstr': 'Sun Apr  2 11:26:01 2023', 'version': '7.80', 'xmloutputversion': '1.04'}, 'task_results': [{'task': 'Ping Scan', 'time': '1680459962', 'extrainfo': '1 total hosts'}, {'task': 'Parallel DNS resolution of 1 host.', 'time': '1680459972'}, {'task': 'SYN Stealth Scan', 'time': '1680459976', 'extrainfo': '1000 total ports'}]}
