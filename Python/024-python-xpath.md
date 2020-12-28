# 024-python-xpath
## xpath的基本概念
xpath中的内容分为3种类型：
1. 节点（node）
2. 基本值（Atomic value）
3. 项目（item）

节点与节点之间的关系：
1. Parent
2. Children
3. Sibling
4. Ancestor
5. Descendant

xpath有七种基本的类型：元素、属性、文本、命名空间、处理指令、注释以及文档（根）节点。

## 选取节点
| 表达式 | 描述 |
| ---- | ---- |
| nodename | 选取此节点的所有子节点。 |
| / | 从根节点选取。 |
| // | 从匹配选择的当前节点选择文档中的节点，而不考虑它们的位置。 |
| .	| 选取当前节点。 |
| .. | 选取当前节点的父节点。 |
| @ | 选取属性。 |

## 谓语
谓语用来查找某个特定的节点或者包含某个指定的值的节点。
谓语属于方括号。

| 路径表达式 | 结果 |
| ---- | ---- |
| `/bookstore/book[1]` | 选取属于 bookstore 子元素的第一个 book 元素。|
| `/bookstore/book[last()]`	| 选取属于 bookstore 子元素的最后一个 book 元素。 |
| `/bookstore/book[last()-1]` | 选取属于 bookstore 子元素的倒数第二个 book 元素。 |
| `/bookstore/book[position()<3]` | 选取最前面的两个属于 bookstore 元素的子元素的 book 元素。 |
| `//title[@lang]` | 选取所有拥有名为 lang 的属性的 title 元素。 |
| `//title[@lang='eng']` | 选取所有 title 元素，且这些元素拥有值为 eng 的 lang 属性。 |
| `/bookstore/book[price>35.00]` | 选取 bookstore 元素的所有 book 元素，且其中的 price 元素的值须大于 35.00。 |
| `/bookstore/book[price>35.00]//title`	| 选取 bookstore 元素中的 book 元素的所有 title 元素，且其中的 price 元素的值须大于 35.00。 |

## 选取未知节点
xpath通配符可以用来选取未知的XML。

| 表达式 | 描述 |
| ---- | ---- |
| * | 匹配任何元素节点。 |
| @* | 匹配任何属性节点。 |
| node() | 匹配任何类型的节点。 |


## XPATH轴（Axes）
轴可定义相对于当前节点的节点集。

| 轴名称 | 描述 |
| ---- | ---- |
| ancestor | 选取当前节点的所有先辈（父、祖父等）。 |
| ancestor-or-self | 选取当前节点的所有先辈（父、祖父等）以及当前节点本身。 |
| attribute | 选取当前节点的所有属性。 |
| child	| 选取当前节点的所有子元素。 |
| descendant | 选取当前节点的所有后代元素（子、孙等）。 |
| descendant-or-self | 选取当前节点的所有后代元素（子、孙等）以及当前节点本身。 |
| following | 选取文档中当前节点的结束标签之后的所有节点。 |
| following-sibling | 选取当前节点之后的所有兄弟节点。 |
| namespace | 选取当前节点的所有命名空间节点。 |
| parent | 选取当前节点的父节点。 |
| preceding | 选取文档中当前节点的开始标签之前的所有节点。 |
| preceding-sibling | 选取当前节点之前的所有同级节点。 |
| self | 选取当前节点。 |

## xpath运算符
XPath 表达式可返回节点集、字符串、逻辑值以及数字。
XPath 运算符
下面列出了可用在 XPath 表达式中的运算符：

| 运算符 | 描述 | 实例 | 返回值 |
| ---- | ---- | ---- | ---- |
| 计算两个节点集 | //book | //cd | 返回所有拥有 book 和 cd 元素的节点集 |
| `+`	| 加法 | `6 + 4` | 10 |
| `-`	| 减法 | `6 - 4` | 2 |
| `*`	| 乘法 | `6 * 4` | 24 |
| `div`	| 除法 | `8 div 4` | 2 |
| `=`	| 等于 | `price=9.80` |	如果 price 是 9.80，则返回 true。如果 price 是 9.90，则返回 false。 |
| `!=` | 不等于 | `price!=9.80` | 如果 price 是 9.90，则返回 true。如果 price 是 9.80，则返回 false。 |
| `<` 小于 | `price<9.80` | 如果 price 是 9.00，则返回 true。如果 price 是 9.90，则返回 false。 |
| `<=` | 小于或等于 | `price<=9.80` | 如果 price 是 9.00，则返回 true。如果 price 是 9.90，则返回 false。 |
| `>` | 大于 | `price>9.80` | 如果 price 是 9.90，则返回 true。如果 price 是 9.80，则返回 false。|
| `>=` | 大于或等于 | `price>=9.80` | 如果 price 是 9.90，则返回 true。如果 price 是 9.70，则返回 false。 |
| or | 或 | `price=9.80 or price=9.70` | 如果 price 是 9.80，则返回 true。如果 price 是 9.50，则返回 false。 |
| and | 与 | `price>9.00 and price<9.90` | 如果 price 是 9.80，则返回 true。如果 price 是 8.50，则返回 false。 |
| mod | 计算除法的余数 | `5 mod 2` | 1 |
