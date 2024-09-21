# codeing = utf-8
import random

items = ['八股文', 'composition-novel','composition - (music app)', '英语面试准备', 'IELTS - (code English)', 'IELTS-Friends', 'IELTS - (TED or Others)']
weights = [12, 3, 6, 3, 3, 2, 5]
random_choice = random.choices(items, weights=weights, k=1)[0]
print(random_choice)