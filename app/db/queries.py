teamsInfo = """
select ttm.league_code as "리그명", ttm.teamname_kr as "팀명", ttm.teamname_us as "영어팀명", 
  case
	when ttm.cur_teamname_kr is null and ttm.cur_teamname_us is null
    then 'There''s no current teamname'
    else CONCAT(ttm.cur_teamname_kr, ' / ', ttm.cur_teamname_us) 
  end as "과거팀명"
  from tbl_team_mt01 ttm 
"""

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

players ="""
select tmn.fullname, tmn."position", tmn.teamname,  
  case 
  	when tmn.league_code = 'AL'
  	then 'American League'
  	when tmn.league_code = 'NL'
  	then 'National Leauge'
  end as league_name
  from tbl_mlbplayer_nt01 tmn 
 where tmn.teamcode = %s
"""