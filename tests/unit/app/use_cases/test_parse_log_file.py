import pytest
from unittest.mock import mock_open, patch
from src.app.entities.game import Game
from src.app.use_cases.parse_log_file import parse_log_file

@pytest.fixture
def example_log_data():
    raw_string = r''' 
20:37 ------------------------------------------------------------
20:37 InitGame: \sv_floodProtect\1\sv_maxPing\0\sv_minPing\0\sv_maxRate\10000\sv_minRate\0\sv_hostname\Code Miner Server\g_gametype\0\sv_privateClients\2\sv_maxclients\16\sv_allowDownload\0\bot_minplayers\0\dmflags\0\fraglimit\20\timelimit\15\g_maxGameClients\0\capturelimit\8\version\ioq3 1.36 linux-x86_64 Apr 12 2009\protocol\68\mapname\q3dm17\gamename\baseq3\g_needpass\0
20:38 ClientConnect: 2
20:38 ClientUserinfoChanged: 2 n\Isgalamido\t\0\model\uriel/zael\hmodel\uriel/zael\g_redteam\\g_blueteam\\c1\5\c2\5\hc\100\w\0\l\0\tt\0\tl\0
20:38 ClientBegin: 2
20:40 Item: 2 weapon_rocketlauncher
20:40 Item: 2 ammo_rockets
20:42 Item: 2 item_armor_body
20:54 Kill: 1022 2 22: <world> killed Isgalamido by MOD_TRIGGER_HURT
20:59 Item: 2 weapon_rocketlauncher
21:04 Item: 2 ammo_shells
21:07 Kill: 1022 2 22: <world> killed Isgalamido by MOD_TRIGGER_HURT
21:10 ClientDisconnect: 2
21:15 ClientConnect: 2
21:15 ClientUserinfoChanged: 2 n\Isgalamido\t\0\model\uriel/zael\hmodel\uriel/zael\g_redteam\\g_blueteam\\c1\5\c2\5\hc\100\w\0\l\0\tt\0\tl\0
21:17 ClientUserinfoChanged: 2 n\Isgalamido\t\0\model\uriel/zael\hmodel\uriel/zael\g_redteam\\g_blueteam\\c1\5\c2\5\hc\100\w\0\l\0\tt\0\tl\0
21:17 ClientBegin: 2
21:18 Item: 2 weapon_rocketlauncher
21:21 Item: 2 item_armor_body
21:32 Item: 2 item_health_large
21:33 Item: 2 weapon_rocketlauncher
21:34 Item: 2 ammo_rockets
21:42 Kill: 1022 2 22: <world> killed Isgalamido by MOD_TRIGGER_HURT
21:49 Item: 2 weapon_rocketlauncher
21:51 ClientConnect: 3
21:51 ClientUserinfoChanged: 3 n\Dono da Bola\t\0\model\sarge/krusade\hmodel\sarge/krusade\g_redteam\\g_blueteam\\c1\5\c2\5\hc\95\w\0\l\0\tt\0\tl\0
21:53 ClientUserinfoChanged: 3 n\Mocinha\t\0\model\sarge\hmodel\sarge\g_redteam\\g_blueteam\\c1\4\c2\5\hc\95\w\0\l\0\tt\0\tl\0
21:53 ClientBegin: 3
22:04 Item: 2 weapon_rocketlauncher
22:04 Item: 2 ammo_rockets
22:06 Kill: 2 3 7: Isgalamido killed Mocinha by MOD_ROCKET_SPLASH
22:11 Item: 2 item_quad
22:11 ClientDisconnect: 3
22:18 Kill: 2 2 7: Isgalamido killed Isgalamido by MOD_ROCKET_SPLASH
22:26 Item: 2 weapon_rocketlauncher
22:27 Item: 2 ammo_rockets
22:40 Kill: 2 2 7: Isgalamido killed Isgalamido by MOD_ROCKET_SPLASH
22:43 Item: 2 weapon_rocketlauncher
22:45 Item: 2 item_armor_body
23:06 Kill: 1022 2 22: <world> killed Isgalamido by MOD_TRIGGER_HURT
23:09 Item: 2 weapon_rocketlauncher
23:10 Item:'''
    
    # return (
    # r"20:37 InitGame: \sv_floodProtect\1\sv_maxPing\0\sv_minPing\0\sv_maxRate\10000\sv_minRate\0\sv_hostname\Code Miner Server\g_gametype\0\sv_privateClients\2\sv_maxclients\16\sv_allowDownload\0\bot_minplayers\0\dmflags\0\fraglimit\20\timelimit\15\g_maxGameClients\0\capturelimit\8\version\ioq3 1.36 linux-x86_64 Apr 12 2009\protocol\68\mapname\q3dm17\gamename\baseq3\g_needpass\0\\n 20:54 Kill: 1022 2 22: <world> killed Isgalamido by MOD_TRIGGER_HURT\\n 21:07 Kill: 1022 2 22: <world> killed Isgalamido by MOD_TRIGGER_HURT\\n 21:42 Kill: 1022 2 22: <world> killed Isgalamido by MOD_TRIGGER_HURT\\nn 22:06 Kill: 2 3 7: Isgalamido killed Mocinha by MOD_ROCKET_SPLASH\\n 22:18 Kill: 2 2 7: Isgalamido killed Isgalamido by MOD_ROCKET_SPLASH\\n 22:40 Kill: 2 2 7: Isgalamido killed Isgalamido by MOD_ROCKET_SPLASH"
    # )
    return raw_string

    
def test_empty_file():
    with patch('builtins.open', mock_open(read_data="")):
        result = parse_log_file("test.log")
    assert result == []

def test_single_game(example_log_data):
    with patch('builtins.open', mock_open(read_data=example_log_data)):
        result = parse_log_file("test.log")
    expected_result = [
       {'total_kills': 3, 'players': ['Mocinha', 'Isgalamido'], 'kills': {'Isgalamido': -1}}
    ]
    assert result == expected_result

def test_multiple_games(example_log_data):
    log_data = (
        example_log_data + example_log_data
    )
    with patch('builtins.open', mock_open(read_data=log_data)):
        result = parse_log_file("test.log")
    expected_result = [
        {'total_kills': 3, 'players': ['Mocinha', 'Isgalamido'], 'kills': {'Isgalamido': -1}}
    ]
    assert result == expected_result

