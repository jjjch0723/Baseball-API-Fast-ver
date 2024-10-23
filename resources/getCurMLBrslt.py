import statsapi
from datetime import datetime, timedelta

# 어제 날짜를 YYYY-MM-DD 형식으로 가져오기
yesterday = (datetime.today() - timedelta(days=1)).strftime('%Y-%m-%d')

def get_yesterday_mlb_results():
    # 어제 날짜로 경기 결과 가져오기
    games = statsapi.schedule(date=yesterday)

    # 결과 저장 리스트
    results = []

    # 각 경기 결과 처리
    for game in games:
        away_team = game['away_id']
        home_team = game['home_id']
        away_score = game['away_score']
        home_score = game['home_score']
        status = game['status']
        
        if status == 'Final':
            if away_score > home_score:
                win_team = away_team
                lose_team = home_team
                win_score = away_score
                lose_score = home_score
            else:
                win_team = home_team
                lose_team = away_team
                win_score = home_score
                lose_score = away_score
        else:
            win_team = ""
            lose_team = ""
            win_score = ""
            lose_score = ""

        result = {
            "DATE": yesterday,
            "WINTEAM": str(win_team),
            "LOSETEAM": str(lose_team),
            "WINSCORE": str(win_score),
            "LOSESCORE": str(lose_score)
        }
        results.append(result)

    return results
