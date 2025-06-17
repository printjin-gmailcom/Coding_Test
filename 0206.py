# lambda 함수는 여러줄의 코드를 포함할 수 없다.

# 파이썬에서 global  키워드를 사용하면 함수 내부에서 전역 변수를 수정할 수 있다.

# 파이썬에서 if 문 내부에서는 break 문을 사용할 수 없다.

# sorted()와 sort()의 차이점은 sorted()는 새로운 정렬된 리스트를 반환하고, sort()는 원본 리스트를 정렬한다.

print(range(5, 11, 2))

x = (1,2,3)
x[1] = 10
print(x)
# 위 코드는 튜플은 불변(immutable) 자료형이므로, 요소를 변경할 수 없다는 오류가 발생한다.

my_list = [10, 20, 30, 40]
print(my_list[::-1])  # [20, 30]
# 위 코드는 my_list[::-1]은 리스트를 역순으로 슬라이싱하는 방법이므로, [40, 30, 20, 10]이 출력된다.

my_dict = {"a":1, "b":2, "c":3}
value = my_dict.get("d", 0)
my_dict["b"] = 5
print(my_dict, value)
# 위 코드는 my_dict.get("d", 0)에서 "d" 키가 없으므로 기본값 0이 반환되고, my_dict["b"] = 5로 "b"의 값을 5로 변경한다.

user_input = list(map(int, input().split()))
user_input.sort()
a = user_input[0] + user_input[1]
b = user_input[2]
if a < b:
    print("a is less than b")
elif a == b:
    print("a is equal to b")
elif a > b:
    print("a is greater than b")    

a = input()
b = input()
if a in b:
    print(len(b) - len(a))
else:
    print(-1)