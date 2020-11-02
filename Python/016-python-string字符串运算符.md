# 016-python-string字符串运算符
1. 字符串连接符 `+`
```python
"hello" + "!"
>>>'hello!'
```
2. 重复输出字符串
```python
"hello" * 2
>>>'hellohello'
```
3. 通过索引获得字符串字符
```python
"hello"[0]
>>>'h'
```
4. 截取字符串的一部分
```python
"hello"[1:4]
>>>'ell'
```
5. 成员运算符，包含给定的字符返回`True`
```python
"h" in "hello"
>>>True
```
6. 成员运算符，不包含给定的字符时返回`True`
```python
"m" not in "hello"
>>>True
```
7. r/R还原所有的转义字符串。
```python
r'hello\n\n'
>>>'hello\n\n'
```
8. 格式化字符串
```python
string = "my name is s%" % ('estheim')
```