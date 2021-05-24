# 026-Python-原子性-线程安全

官方文档中对于原子操作的说明：
https://docs.python.org/3.5/faq/library.html#what-kinds-of-global-value-mutation-are-thread-safe

For example, the following operations are all atomic (L, L1, L2 are lists, D, D1, D2 are dicts, x, y are objects, i, j are ints):
```python
L.append(x)
L1.extend(L2)
x = L[i]
x = L.pop()
L1[i:j] = L2
L.sort()
x = y
x.field = y
D[x] = y
D1.update(D2)
D.keys()
```
These aren’t:
```python
i = i+1
L.append(L[-1])
L[i] = L[j]
D[x] = D[x] + 1
```
Operations that replace other objects may invoke those other objects’ __del__() method when their reference count reaches zero, and that can affect things. This is especially true for the mass updates to dictionaries and lists. When in doubt, use a mutex!

