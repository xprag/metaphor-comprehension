### TODO List
1. Update the experiment setting adding the following fields: Sex, Age, ...
2. Change the colour of solution into feedback routine (maybe it should be possible to do it into python code).

### Issues fixed
1. ####conditionsFile
To generate a proper "condition file" you need to use excel and save the file in the following formats "xslx" or "cvs".
If you use another text editor it will not work.

2. ####Unicode HOWTO
If you need to set an accented character you should generate the unicode string of length 1 that contains the corresponding code point.
For example by using the python console you should type the following command:
```
>>> u'è'
u'\xe8'
```

3. ##### The missing word
How should I display the missing word:
- 
```
'P1: ' + $premise1.replace('...', $TW) +
'\n\n' +
'P2: ' + $premise2.replace('...', $TW) +
'\n_______________________________\n\n' +
'C: ' + $conclusion
```

Reference: [Unicode HOWTO](https://docs.python.org/2/howto/unicode.html)
