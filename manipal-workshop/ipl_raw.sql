create table datalake.ipl_raw
(match_id string,
season string,
start_date string,
venue string,
innings string,
ball string,
batting_team string,
bowling_team string,
striker string,
non_striker string,
bowler string,
runs_off_bat string,
extras string,
wides string,
noballs string,
byes string,
legbyes string,
penalty string,
wicket_type string,
player_dismissed string,
other_wicket_type string,
other_player_dismissed string,
cricsheet_id string);

create table datalake.batch_ipl
(match_id string,
season string,
start_date string,
venue string,
innings string,
ball string,
batting_team string,
bowling_team string,
striker string,
non_striker string,
bowler string,
runs_off_bat string,
extras string,
wides string,
noballs string,
byes string,
legbyes string,
penalty string,
wicket_type string,
player_dismissed string,
other_wicket_type string,
other_player_dismissed string,
cricsheet_id string);

create table datamart.team_scores as
select match_id, venue, season,start_date, innings, batting_team, sum(IFNULL(runs_scored,0) + IFNULL(wides,0) + IFNULL(noballs,0)+IFNULL(byes,0)+IFNULL(legbyes,0)+IFNULL(penalty,0)) as total_runs
from 
(SELECT match_id,venue, season,start_date, innings,batting_team, sum(runs_off_bat) as runs_scored, sum(wides) as wides, sum(noballs) as noballs, sum(byes) as byes, sum(legbyes) as legbyes,sum(penalty) as penalty FROM `bubbly-benefit-426415-h5.datamart.batch_ipl`
group by match_id,venue, season,start_date, innings, batting_team
order by match_id desc, season desc, innings asc) as agg_table
group by match_id,venue, season,start_date, innings, batting_team
order by match_id desc, season desc, innings asc;


create table datamart.batsmen_score as select match_id, season, start_date, venue, innings, batting_team,bowling_team, striker, sum(runs_off_bat) total_runs, count(*) total_balls
from datamart.batch_ipl
where wides is null
group by match_id, season, start_date, venue, innings, batting_team,bowling_team, striker;


create table datamart.powerplay_bat as select match_id, season, start_date, venue, innings, batting_team, bowling_team, striker,sum(IFNULL(runs_off_bat,0) + IFNULL(extras,0) + IFNULL(wides,0) + IFNULL(noballs,0) + IFNULL(byes,0) + IFNULL(legbyes,0) + IFNULL(penalty,0)) as total_runs, count(*) no_of_balls
from datamart.batch_ipl
where ball <=6
group by match_id, season, start_date, venue, innings, batting_team, bowling_team, striker
order by match_id desc;

create table datamart.depth_bat as select match_id, season, start_date, venue, innings, batting_team, bowling_team, striker,sum(IFNULL(runs_off_bat,0) + IFNULL(extras,0) + IFNULL(wides,0) + IFNULL(noballs,0) + IFNULL(byes,0) + IFNULL(legbyes,0) + IFNULL(penalty,0)) as total_runs, count(*) no_of_balls
from datamart.batch_ipl
where ball >= 14
group by match_id, season, start_date, venue, innings, batting_team, bowling_team, striker
order by match_id desc;

create table datamart.middle_overs__bat as select match_id, season, start_date, venue, innings, batting_team, bowling_team, striker,sum(IFNULL(runs_off_bat,0) + IFNULL(extras,0) + IFNULL(wides,0) + IFNULL(noballs,0) + IFNULL(byes,0) + IFNULL(legbyes,0) + IFNULL(penalty,0)) as total_runs, count(*) no_of_balls
from datamart.batch_ipl
where ball > 6 and ball < 14
group by match_id, season, start_date, venue, innings, batting_team, bowling_team, striker
order by match_id desc;

create table datamart.bowler_wickets as
select match_id, season, start_date, venue, innings, bowling_team,batting_team, bowler, sum(IFNULL(runs_off_bat,0) + IFNULL(extras,0) + IFNULL(wides,0) + IFNULL(noballs,0) + IFNULL(byes,0) + IFNULL(legbyes,0) + IFNULL(penalty,0)) as total_runs_given, count(wickte_type) as number_of_wickets
from datamart.batch_ipl 
group by match_id, season, start_date, venue, innings, bowling_team,batting_team, bowler;

create table datamart.middle_overs_bowling as select match_id, season, start_date, venue, innings, batting_team, bowling_team, bowler,sum(IFNULL(runs_off_bat,0) + IFNULL(extras,0) + IFNULL(wides,0) + IFNULL(noballs,0) + IFNULL(byes,0) + IFNULL(legbyes,0) + IFNULL(penalty,0)) as total_runs, count(*) no_of_balls
from datamart.batch_ipl
where ball > 6 and ball < 14
group by match_id, season, start_date, venue, innings, batting_team, bowling_team, bowler
order by match_id desc;