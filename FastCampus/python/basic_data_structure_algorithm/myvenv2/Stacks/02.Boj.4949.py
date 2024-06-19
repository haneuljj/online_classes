# 세계는 균형이 잘 잡혀있어야 한다. 양과 음, 빛과 어둠 그리고 왼쪽 괄호와 오른쪽 괄호처럼 말이다.
# 정민이의 임무는 어떤 문자열이 주어졌을 때, 괄호들의 균형이 잘 맞춰져 있는지 판단하는 프로그램을 짜는 것이다.
# 문자열에 포함되는 괄호는 소괄호("()") 와 대괄호("[]")로 2종류이고, 문자열이 균형을 이루는 조건은 아래와 같다.

# 모든 왼쪽 소괄호("(")는 오른쪽 소괄호(")")와만 짝을 이뤄야 한다.
# 모든 왼쪽 대괄호("[")는 오른쪽 대괄호("]")와만 짝을 이뤄야 한다.
# 모든 오른쪽 괄호들은 자신과 짝을 이룰 수 있는 왼쪽 괄호가 존재한다.
# 모든 괄호들의 짝은 1:1 매칭만 가능하다. 즉, 괄호 하나가 둘 이상의 괄호와 짝지어지지 않는다.
# 짝을 이루는 두 괄호가 있을 때, 그 사이에 있는 문자열도 균형이 잡혀야 한다.
# 정민이를 도와 문자열이 주어졌을 때 균형잡힌 문자열인지 아닌지를 판단해보자.

# 각 문자열은 마지막 글자를 제외하고 영문 알파벳, 공백, 소괄호("( )"), 대괄호("[ ]")로 이루어져 있으며, 
# 온점(".")으로 끝나고, 길이는 100글자보다 작거나 같다.
# 입력의 종료조건으로 맨 마지막에 온점 하나(".")가 들어온다.

input_string = input()
stack = []
is_balanced = True

for s in input_string:
    if s == "(" or s == "[":
        stack.append(s)

    if s == ")" and len(stack) > 0 and stack[-1] == "(":
        stack.pop(-1)
    if s == ")" and len(stack) == 0:
        is_balanced = False

    if s == "]" and len(stack) > 0 and stack[-1] == "[":
        stack.pop(-1)
    if s == "]" and len(stack) == 0:
        is_balanced = False

if(len(stack)) == 0 and is_balanced == True:
    print("yes")
else:
    print("no")


# 풀이
while True:
    s = input()
    if s == ".":
        break

    stack2 = []
    balanced = True

    for i in range(len(s)):
        # 왼쪽 괄호는 스택에 추가
        if s[i] == '(' or s[i] == '[':
            stack2.append(s[i])

        # 오른쪽 괄호를 만났을 경우
        if s[i] == ')':
            # stack이 비어있으면 안됨
            if len(stack2) == 0:
                balanced = False
                break

            # 스택의 마지막 값이 매칭되는 괄호가 아니면 안됨
            last = stack2.pop(-1)
            if last != '(':
                balanced = False
                break 

        if s[i] == ']':
            if len(stack2) == 0:
                balanced = False
                break

            last = stack2.pop(-1)
            if last != '[':
                balanced = False
                break 

    # 스택이 비어있지 않으면 안됨
    if len(stack2) != 0:
        balanced = False

    if balanced:
        print("yes")
    else:
        print("no")

            