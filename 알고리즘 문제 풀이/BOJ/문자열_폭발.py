import sys
input = sys.stdin.readline

# 문자열이 폭발 문자열을 포함하고 있을 때
# 모든 폭발 문자열이 폭발함
# 남은 문자열을 순서대로 이어붙어야함
# 새로 생긴 문자열도 폭발 문자열이 있을 수 있다
# 폭발은 폭발 문자열이 없을 때까지 계속된다

# 남은 문자열이 없다면 FRULA 를 출력한다

# 문자열 길이 1 ~ 1,000,000
# 폭발 문자열 길이 1 ~ 36

# 두 문자열은 모두 알파벨 소문자, 대문자, 숫자로만 이루어져 있다

stack = list(input().rstrip())[::-1]
bomb = input().rstrip()
length_of_bomb = len(bomb)
# 스택에 문자열을 넣고 차례대로 꺼낸다.
# bomb의 첫 문자와 일치하는 문자가 있다면 있다고 플래그
# 첫 문자와 일치하는 순간부터 꺼내서 bomb과 동일한지 검증 후
# bomb 과 일치한다면 스택에 다시 넣지 않는다

remain_string = []
temp_string = []
is_exist = 0

while stack:
    # print("working is exist : ", is_exist)
    # print(remain_string)
    w = stack.pop()
    if w == bomb[0]:
        # print("find 0")
        is_exist += 1
        temp_string.append(w)
        
        i = 1
        while stack and i < length_of_bomb:
            next = stack.pop()
            temp_string.append(next)
            i += 1
            # if next == bomb[i]:
            #     temp_string.append(next)
        # print(''.join(temp_string))
        if bomb == ''.join(temp_string):
            # print("find bomb")
            temp_string = []
            is_exist -= 1
            # print(is_exist)
            if is_exist:
                # print("is_exist")
                while True:
                    a = remain_string.pop()
                    # print(a)
                    stack.append(a)
                    if a == bomb[0]:
                        is_exist -= 1
                        break
            continue
        else:
            while temp_string:
                stack.append(temp_string.pop())
            stack.pop()
        # remain_string += temp_string
                    
    remain_string.append(w)

if remain_string:
    print(''.join(remain_string))   
else:
    print("FRULA")