from django.db import models
from django.utils import timezone

# Create your models here.
class Line(models.Model):
    # 라인 모델
    # -각 열들
    # name: 1호선, 경춘선 등으로 저장함
    
    name=models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
    
class Station(models.Model):
    # 역 모델
    # -외래 키
    # line: 몇호선의 역인가 구분
    
    # -각 열들
    # name: 역이름
    
    line=models.ForeignKey(Line)
    name=models.CharField(max_length=20)
    
    def __str__(self):
        return self.line.name+' '+self.name
        
class Schedule(models.Model
    # 열차 시간표 모델
    # -외래 키
    # station: 어느 열차의 시간표인지 구분
    
    # -각 열들
    # time: 열차 시간
    # weather: 날씨
    # interval: 앞 차와의 간격
    
    time=models.DateTimeField()
    station=models.ForeignKey(Station,null=True)
    weather=models.CharField(max_length=20)
    interval=models.IntegerField()
    
    def __str__(self):
        return str(self.time)

class User(models.Model):
    #유저 모델
    # -각 열들
    # user_key: 유저 키 저장
    # stacked_data: 해당 유저가 얼마나 많은 데이터를 입력했는지 보는 숫자
    # exist_user: 친구추가된 상태이면 1, 차단한 상태이면 0
    # status: 대화 진행도를 체크하기 위한 상태변수
    
    user_key=models.CharField(max_length=50)
    stacked_data=models.IntegerField(default=0)
    exist_user=models.BooleanField(default=1)
    status=models.IntegerField(default=0)
    
    def __str__(self):
        return self.user_key
    
class Recent(models.Model):
    #최근 조회 역 모델
    # -외래 키
    # user: 어떤 유저의 최근 역 정보 정보인지 저장
    # station: 어떤 역인지 저장한다
    
    # -각 열들
    # number: 얼마나 많이 조회했는지 저장

    user=models.ForeignKey(User)
    number=models.IntegerField(default=1)
    station=models.ForeignKey(Station,null=True)
    
    def __str__(self):
        return self.station.name
    
class Data(models.Model):
    # 데이터 모델
    # -외래키
    # user: 어떤 유저가 데이터를 남겼는가
    # schedule: 어느 시간표에 데이터를 남겼는가
    
    # -각 열들
    # time: 데이터가 생성된 시간 및 날짜
    # sit: 입,착석 여부 입석일 경우 1, 착석일 경우 2가 저장된다
    # detail: 열차가 얼마나 빽빽한지 알기 위한 키다 sit 열 처럼 아래 DETAIL_IN_DATA_CHOICES 튜플 쌍에 있는 첫 번째 정수 값으로 구분할 수 있다.
    
    schedule=models.ForeignKey(Schedule)
    user=models.ForeignKey(User)
    time=models.DateTimeField(auto_now_add=True)
    
    SIT_IN_DATA_CHOICES = (
        (1, '입석'),
        (2, '착석')
    )
    DETAIL_IN_DATA_CHOICES=(
        (1,'콩나물 시루다'),
        (2,'자리는 없다'),
        (3,'자리가 남아 있다')
        )
    sit=models.IntegerField(choices=SIT_IN_DATA_CHOICES)
    detail=models.IntegerField(choices=DETAIL_IN_DATA_CHOICES)
    
    def __str__(self):
        return str(self.time)+' '+str(self.schedule.station)
        
    # ~년월일시간 ~역 ~호선으로 나오게 된다
    