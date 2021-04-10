import random

# 打招呼
greetings=['你好','hola','hello','hi','Hi','hey!','hey','こんにちは']

# 回复打招呼
random_greeting = random.choice(greetings)

# 对于“你怎么样？”这个问题进行回复
question = ['你怎么样？','How are you?','How are you doing?','あなたはどうですか?']

# “我很好”
responses = ['我很好','OKay','リバーズ']

# 随机选择回答
random_response = random.choice(responses)

#运行
while True:
    userInput = input(">>>")
    if userInput in greetings:
        print(random_greeting)
    elif userInput in question:
        print(random_response)
    # 结束
    elif userInput == '拜拜':
        break
    else:
        print("我没有听懂您说什么")