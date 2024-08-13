print ("chào mừng ...")
question_and_answer = [
    ("python là ngôn ngữ lập trình?:", "đúng")
    ("trái đất ình vuông?:", "sai")
    ("năm 2024 là năm nhuận?:" , "đúng")
    ("con bò biết bay?:", "sai")
]

score = 0

for question, correct_answer in question_and_answer:
    print(question)
    user_answer = input("câu trả lời của bạn là (đúng/sai):").lower()

    if user_answer == correct_answer:
        print("Chính xác!")
        score +=1
    else :
        print("chưa chính xác")
print(f"\Bạn đã trả lời đúng {score} câu.")
print("cảm ơn bạn đã tham gia trò chơi")
