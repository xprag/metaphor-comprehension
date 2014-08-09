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
Reference: [Unicode HOWTO](https://docs.python.org/2/howto/unicode.html)
