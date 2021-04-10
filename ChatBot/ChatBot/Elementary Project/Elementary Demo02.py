from nltk import word_tokenize
import random

# 精确对答
greeting = ['你好','hola','hello','hi','Hi','hey!','hey','こんにちは']
random_greeting = random.choice(greeting)
question = ['周末','break','holiday','vacation','weekend']
responses = ['我打算好好休息','It was nice! I went to Paris',"Sadly, I just stayed at home"]
random_response = random.choice(responses)

#运行
while True:
    userInput = input(">>>")
    # 清理一下输入，看看都有哪些词
    cleaned_input = word_tokenize(userInput)
    # 比较一下关键词，确定他属于哪个问题
    if not set(cleaned_input).isdisjoint(greeting):
        print(random_greeting)
    elif not set(cleaned_input).isdisjoint(question):
        print(random_response)
    elif userInput == '拜拜':
        break
    else:
        print("很抱歉，我不明白您说什么")