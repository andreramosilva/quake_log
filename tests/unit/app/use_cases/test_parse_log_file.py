import pytest
from unittest.mock import mock_open, patch
from src.app.entities.game import Game
from src.app.use_cases.parse_log_file import parse_log_file

@pytest.fixture
def example_log_data():
    return (
        ''' 0:00 ------------------------------------------------------------
            0:00 InitGame: \sv_floodProtect\1\sv_maxPing\0\sv_minPing\0\sv_maxRate\10000\sv_minRate\0\sv_hostname\Code Miner Server\g_gametype\0\sv_privateClients\2\sv_maxclients\16\sv_allowDownload\0\dmflags\0\fraglimit\20\timelimit\15\g_maxGameClients\0\capturelimit\8\version\ioq3 1.36 linux-x86_64 Apr 12 2009\protocol\68\mapname\q3dm17\gamename\baseq3\g_needpass\0
            15:00 Exit: Timelimit hit.
            20:34 ClientConnect: 2
            20:34 ClientUserinfoChanged: 2 n\Isgalamido\t\0\model\xian/default\hmodel\xian/default\g_redteam\\g_blueteam\\c1\4\c2\5\hc\100\w\0\l\0\tt\0\tl\0
            20:37 ClientUserinfoChanged: 2 n\Isgalamido\t\0\model\uriel/zael\hmodel\uriel/zael\g_redteam\\g_blueteam\\c1\5\c2\5\hc\100\w\0\l\0\tt\0\tl\0
            20:37 ClientBegin: 2
            20:37 ShutdownGame:
            20:37 ------------------------------------------------------------
            20:37 ------------------------------------------------------------'''
    )

    
def test_empty_file():
    with patch('builtins.open', mock_open(read_data="")):
        result = parse_log_file("test.log")
    assert result == []

def test_single_game(example_log_data):
    with patch('builtins.open', mock_open(read_data=example_log_data)):
        result = parse_log_file("test.log")
    expected_result = [
       {
        "kills": {},
        "players": [],
        "total_kills": 0
        },
    ]
    assert result == expected_result

def test_multiple_games(example_log_data):
    log_data = (
        example_log_data +
        ''' 0:00 ------------------------------------------------------------
            0:00 InitGame: \sv_floodProtect\1\sv_maxPing\0\sv_minPing\0\sv_maxRate\10000\sv_minRate\0\sv_hostname\Code Miner Server\g_gametype\0\sv_privateClients\2\sv_maxclients\16\sv_allowDownload\0\dmflags\0\fraglimit\20\timelimit\15\g_maxGameClients\0\capturelimit\8\version\ioq3 1.36 linux-x86_64 Apr 12 2009\protocol\68\mapname\q3dm17\gamename\baseq3\g_needpass\0
            15:00 Exit: Timelimit hit.
            20:34 ClientConnect: 2
            20:34 ClientUserinfoChanged: 2 n\Isgalamido\t\0\model\xian/default\hmodel\xian/default\g_redteam\\g_blueteam\\c1\4\c2\5\hc\100\w\0\l\0\tt\0\tl\0
            20:37 ClientUserinfoChanged: 2 n\Isgalamido\t\0\model\uriel/zael\hmodel\uriel/zael\g_redteam\\g_blueteam\\c1\5\c2\5\hc\100\w\0\l\0\tt\0\tl\0
            20:37 ClientBegin: 2
            20:37 ShutdownGame:
            20:37 ------------------------------------------------------------
            20:37 ------------------------------------------------------------'''
    )
    with patch('builtins.open', mock_open(read_data=log_data)):
        result = parse_log_file("test.log")
    expected_result = [
        {
            "kills": {},
            "players": [],
            "total_kills": 0
            },
        {
            "kills": {},
            "players": [],
            "total_kills": 0
            },
    ]
    assert result == expected_result

