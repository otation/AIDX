Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> list=[]
>>> list.append(1)
>>> list.append(2)
>>> list.append(6)
>>> list.append(3)
>>> list
[1, 2, 6, 3]
>>> print(list)
[1, 2, 6, 3]
>>> pwd
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    pwd
NameError: name 'pwd' is not defined. Did you forget to import 'pwd'?
>>> clear
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    clear
NameError: name 'clear' is not defined
>>> ls
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    ls
NameError: name 'ls' is not defined
>>> list[0]
1
>>> list[3]
3
>>> list[2]
6
