from datetime import datetime, timedelta

#안쓸것같아..
class DateManager:
    def __init__(self):
        self.date_form = "%Y%m%d"

    #오늘 날짜 반환
    def get_today_date(self):
        today = datetime.now()
        return today.strftime(self.date_form)
    
    #내일 날짜 반환
    def get_tommorow_date(self):
        tommorow = datetime.now() + timedelta(days=1) # 하루 더하기
        return tommorow.strftime(self.date_form)
    
    #어제 날짜 반환
    def get_yesterday_date(self):
        yesterday = datetime.now() - timedelta(days=1) #하루 빼기
        return yesterday.strftime(self.date_form)
    
