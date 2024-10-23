import os
import json
from typing import List, Dict, Any
from app.core.config import settings

class JSONManager:
    def __init__(self):
        pass

    # 오늘 MLB 경기 일정 파일 읽기
    def read_mlb_file(self, day: str) -> List[Dict[str, Any]]:
        mlb_file_path = f"{settings.mlb_file_path}/{day}.json"
        print(f"{day}의 MLB 경기 일정을 가져옵니다.")

        if not os.path.exists(mlb_file_path):
            print(f"MLB file not found: {mlb_file_path}")
            return []

        with open(mlb_file_path, 'r') as file:
            games_list = json.load(file)

        if not games_list:
            print(f"Empty MLB file: {mlb_file_path}")
            return []

        for game in games_list:
            game['TEAM1'] = str(game.get('home_team'))
            game['TEAM2'] = str(game.get('away_team'))
            game['DATE'] = game.get('game_date')

        return games_list

    # 오늘 KBO 경기 일정 파일 읽기
    def read_kbo_file(self, day: str) -> List[Dict[str, Any]]:
        kbo_file_path = f"{settings.kbo_file_path}/{day}.json"
        print(f"{day}의 KBO 경기 일정을 가져옵니다.")

        if not os.path.exists(kbo_file_path):
            print(f"KBO file not found: {kbo_file_path}")
            return []

        with open(kbo_file_path, 'r') as file:
            games_list = json.load(file)

        if not games_list:
            print(f"Empty KBO file: {kbo_file_path}")
            return []

        for game in games_list:
            game['TEAM1'] = str(game.get('home_team'))
            game['TEAM2'] = str(game.get('away_team'))
            game['DATE'] = game.get('game_date')

        return games_list

    # MLB 경기 결과 파일 읽기
    def read_mlb_result_file(self, day: str) -> List[Dict[str, Any]]:
        mlb_result_file_path = f"{settings.mlb_result_file_path}/{day}.json"
        print(f"{day}의 MLB 경기 결과를 가져옵니다.")

        if not os.path.exists(mlb_result_file_path):
            print(f"MLB result file not found: {mlb_result_file_path}")
            return []

        with open(mlb_result_file_path, 'r') as file:
            games_list = json.load(file)

        if not games_list:
            print(f"Empty MLB result file: {mlb_result_file_path}")
            return []

        return games_list

    # KBO 경기 결과 파일 읽기
    def read_kbo_result_file(self, day: str) -> List[Dict[str, Any]]:
        kbo_result_file_path = f"{settings.kbo_result_file_path}/{day}.json"
        print(f"{day}의 KBO 경기 결과를 가져옵니다.")

        if not os.path.exists(kbo_result_file_path):
            print(f"KBO result file not found: {kbo_result_file_path}")
            return []

        with open(kbo_result_file_path, 'r') as file:
            games_list = json.load(file)

        if not games_list:
            print(f"Empty KBO result file: {kbo_result_file_path}")
            return []

        return games_list

    # GPT 예측 결과 파일 읽기 및 중복 제거
    def read_gpt_expect(self) -> List[Dict[str, Any]]:
        gpt_file_path = settings.gpt_expect_file_path
        print("GPT 예상 결과를 가져옵니다.")

        if not os.path.exists(gpt_file_path):
            print(f"GPT file not found: {gpt_file_path}")
            return []

        with open(gpt_file_path, 'r') as file:
            games_list = json.load(file)

        if not games_list:
            print(f"Empty GPT file: {gpt_file_path}")
            return []

        # 중복 제거 로직
        unique_keys = set()
        distinct_list = []

        for game in games_list:
            unique_key = f"{game['TEAM1']}_{game['TEAM2']}_{game['DATE']}"
            if unique_key not in unique_keys:
                unique_keys.add(unique_key)
                distinct_list.append(game)

        return distinct_list
