#### 1.Write a Python program to clone or copy a list.
  <details> <summary> Result </summary>

  ```js
  original_list = [10, 22, 44, 23, 4]
  new_list = list(original_list)
  print(original_list)
  print(new_list)
  ```
  </details>
  
#### 2.Given a list of ints length 3, change the list with the elements in reverse order, so [1, 2, 3] becomes [3, 2, 1].
<details> <summary> Result </summary>

```js
list = [1,2,3]
list.reverse()
print list
 ```
 
  </details>

#### 2.Given a list within a list with length 3, compute the sum of the elements: lst = [1, 2, [3, 4], 5] sum = 15
<details> <summary> Result </summary>

```js
lst = [1, 2, [3, 4], 5]
s = lst[0] + lst[1] + lst[2][0] + lst[2][1] + lst[3]
print s
 ```
 
  </details>
