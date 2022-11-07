from add import add_func
from sub import sub_func
from mul import mul_func
from div import div_func

## 함수

## 전역
num1, num2, res = 100, 200, 0

## 메인
res = add_func(num1, num2)
print(num1, '+', num2, '=', res)

res = sub_func(num1, num2)
print(num1, '-', num2, '=', res)