
import math

x = 1.79
fun_1 = math.cos(math.exp(x)) + (math.log(1 + x))**2
fun_2 = math.sqrt(math.exp(math.cos(x))) + math.sin(math.pi*x)**2
fun_3 = math.sqrt(1/x) + math.cos(x**2)

x = 1.79
y = (fun_1 + fun_2 + fun_3)**math.sin(x)

print('Ответ:', y)