# push test by jmc

import json
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Line,Station,Recent,User,Schedule,Data

@csrf_exempt
def keyboard(request):
    response_json={}
    response_json["type"]="buttons"
    response_json["buttons"]=["시작하기"]
    return HttpResponse(json.dumps(response_json,ensure_ascii=False), content_type=u"application/json; charset=utf-8")

@csrf_exempt
def message(request):
    value=json.loads(request.body.decode("utf-8"))
    key=value['user_key']
    text=value['type']
    content=value["content"]
    response_json={}
    
        
    response_json={
        "message":{
            "text": content+" 선택하셨습니다."
        },
        "keyboard":{
            "type": "buttons",
            "buttons":[
                
                "최근 역1-1",
                "최근 역2-1",
                "최근 역2-1",
                "최근 역3-1",
                "최근 역4-1",
                "여기에 없음-1"

                ]
        }
    }
    
    # response_json["message"]={"text": content+" 선택하셨습니다."}
    # response_json["keyboard"]={{"type":"buttons"},{"buttons":["최근 역1","최근 역2","최근 역3","최근 역4","여기에 없음"]}}
    return HttpResponse(json.dumps(response_json,ensure_ascii=False), content_type=u"application/json; charset=utf-8")

@csrf_exempt    
def reg_friend(request):
    value=json.loads(request.body.decode("utf-8"))
    key=value['user_key']#유저 키 등록
    new_user=User(user_key=key)
    new_user.save()
    return HttpResponse("")

@csrf_exempt
def del_friend(request,user_key):
    #유저 키 삭제
    try: 
        del_user=User.objects.get(user_key=user_key)
        del_user.exist_user=0
        del_user.save()
    finally:
        return HttpResponse("")


@csrf_exempt
def room(request,user_key):
    #채팅방 나감
    
    return HttpResponse("")