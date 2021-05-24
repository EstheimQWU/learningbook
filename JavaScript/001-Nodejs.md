# 001-Nodejs
## 模块化
hello.js
```javascript
'use strict':
var s = 'hello'
function gereet () {
    console.log(s + '.')
}

module.export = greet;
```
引用`hello.js`模块
```javascript
'use strict'

var greet = require('./hello')
var s = 'name'
greet(s)
```

