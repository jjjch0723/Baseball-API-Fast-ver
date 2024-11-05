# 전체 팀정보
teamsInfo = """
select ttm.league_code as "리그명", ttm.teamname_kr as "팀명", ttm.teamname_us as "영어팀명", 
  case
	when ttm.cur_teamname_kr is null and ttm.cur_teamname_us is null
    then 'There''s no current teamname'
    else CONCAT(ttm.cur_teamname_kr, ' / ', ttm.cur_teamname_us) 
  end as "과거팀명"
  from tbl_team_mt01 ttm 
"""

# 특정 팀정보
teamInfo = """
select ttm.league_code as "리그명", ttm.teamname_kr as "팀명", ttm.teamname_us as "영어팀명",
  case
	when ttm.cur_teamname_kr is null and ttm.cur_teamname_us is null
    then 'There''s no current teamname'
    else CONCAT(ttm.cur_teamname_kr, ' / ', ttm.cur_teamname_us) 
  end as "과거팀명"
  from tbl_team_mt01 ttm 
 where ttm.team_code = %s
"""

# 팀 로스터 정보
players ="""
select 
  case 
  	when tmn.league_code = 'AL'
  	then 'American League'
  	when tmn.league_code = 'NL'
  	then 'National Leauge'
   end as league_name, tmn.teamname, tmn.fullname, tmn."position", tmn.teamcode
  from tbl_mlbplayer_nt01 tmn 
 where tmn.teamcode = %s
 order by "position" 
"""

#포지션별 선수 모음
position ="""
select
  case 
  	when tmn.league_code = 'AL'
  	then 'American League'
  	when tmn.league_code = 'NL'
  	then 'National Leauge'
  end as league_name, tmn."position", tmn.fullname, tmn.teamname, tmn.teamcode
  from tbl_mlbplayer_nt01 tmn 
 where tmn."position" = %s
 order by tmn.teamcode
"""
