from django.shortcuts import render
# from django.http import HttpResponse


def index(request):
    question_list = [
        "あなたは子どもですか？",
        "あなたは大人ですか？",
        "あなたは老人ですか",
        "あなたは藤原先生ですか？",
    ]
    context = {
        "question_list": question_list,
        "is polled": True,
        "polled_msg": "投票していただき、本当にありがとうございました。",
        "not_polled_msg": "投票早くしろやこら！！早く、早く、早く、早く、早く、早く、早く、早く",
        "user_name": "たろー",
    }
    return render(request, "main/index.html", context)