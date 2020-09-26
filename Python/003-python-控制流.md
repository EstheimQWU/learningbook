# 003-python-控制流
## 001条件
```python
if [条件]:
    [行为]
```

```python
if [条件]:
    [行为]
elif [条件]:
    [行为]
else:
    [条件]
```

**input**

input接收的输入是`str`，不能直接用来与`int`作比较。

## 002循环
```python
for item in items:
    [行为]

for item in range(1,5,)
```

```python
while [条件]:
    [行为]
```

`break`用于跳出循环

`continue`用于跳出当次循环

**tips:** 尽量减少`break`与`continue`语句的使用，因为他们会导致代码执行的逻辑分支复杂化，导致出错。大部分情况下， 这两个语句可以通过优化循环逻辑以去除。


