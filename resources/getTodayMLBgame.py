import statsapi
from datetime import datetime, timedelta

# 한국 시간 기준으로 현재 날짜 가져오기
now_kst = datetime.now() + timedelta(hours=14)
today_kst = now_kst.strftime('%Y-%m-%d')

def get_today_mlb_schedule():
    # 오늘 날짜의 경기 일정 가져오기
    games = statsapi.schedule(start_date=today_kst, end_date=today_kst)

    # 경기 일정 리스트로 반환
    games_list = []
    if games:
        for game in games:
            games_list.append({
                "away_team": game['away_id'],
                "home_team": game['home_id'],
                "game_date": game['game_date']
            })
    return games_list