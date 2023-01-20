from curses import A_ALTCHARSET
from re import A
from multiwidth import __version__
import multiwidth
import os

from multiwidth.multiwidth import get_letter_locations

def test_version():
    assert __version__ == '0.1.3'

def test_split():
    in_data = 'Hello world'
    out_data = ['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
    
    assert multiwidth.split(in_data) == out_data

def test_process_line():
    in_data = 'foo bar baz'
    out_data = ['foo', 'bar', 'baz']
    
    word_locations = multiwidth.get_letter_locations(in_data)
    widths = [word_locations[i+1]-word_locations[i] for i in range(0, len(word_locations)-1)]
    assert multiwidth.process_line(in_data, widths) == out_data

def test_process_line_extra_spaces():
    in_data = 'foo    bar    baz'
    out_data = ['foo', 'bar', 'baz']

    word_locations = multiwidth.get_letter_locations(in_data)
    widths = [word_locations[i+1]-word_locations[i] for i in range(0, len(word_locations)-1)]
    assert multiwidth.process_line(in_data, widths) == out_data

def test_loads():
    
    in_data = '''
foo    bar    baz   
hello  world  foobar
a      b      c     '''
    out_data = [['hello', 'world', 'foobar'],['a', 'b', 'c']]

    assert multiwidth.loads(in_data) == out_data

def test_loads_json():
    
    in_data = '''
foo    bar    baz   
hello  world  foobar
a      b      c     '''
    out_data = [{'foo':'hello', 'bar':'world', 'baz':'foobar'},{'foo':'a', 'bar':'b', 'baz':'c'}]

    assert multiwidth.loads(in_data, header=True, output_json=True) == out_data

def test_loads_json_error():
    
    in_data = '''
foo    bar    baz   
hello  world  foobar
a      b      c     '''
    out_data = [{'foo':'hello', 'bar':'world', 'baz':'foobar'},{'foo':'a', 'bar':'b', 'baz':'c'}]

    try:
        multiwidth.loads(in_data, header=False, output_json=True)
    except:
        assert True

def test_load():
    
    test_dir = os.path.dirname(os.path.abspath(__file__))
    with open(f'{test_dir}/data/input.txt', 'r', encoding='utf-8') as in_data:

        out_data = [
            [
                '3c3c15c25c3e',
                'frontend',
                '"./start-frontend.sh"',
                '10 seconds ago',
                'Up 8 seconds',
                '0.0.0.0:9000->9000/tcp',
                'velocimodel_frontend_1'
            ],
            [
                'c39392bb88cd',
                'model-manager',
                '"./start-model-manag…"',
                '10 seconds ago',
                'Up 7 seconds',
                '127.0.0.1:9003->9003/tcp',
                'velocimodel_model-manager_1'
            ],
            [
                'ef3acf42bfa4',
                'asset-manager',
                '"./start-asset-manag…"',
                '10 seconds ago',
                'Up 7 seconds',
                '127.0.0.1:9002->9002/tcp',
                'velocimodel_asset-manager_1'
            ],
            [
                '17b161dfa33d',
                'auth-manager',
                '"./start-auth-manage…"',
                '10 seconds ago',
                'Up 7 seconds',
                '127.0.0.1:9005->9005/tcp',
                'velocimodel_auth-manager_1'
            ],
            [
                '79af01ae46a3',
                'api-server',
                '"./start-api-server.…"',
                '11 seconds ago',
                'Up 9 seconds',
                '127.0.0.1:9004->9004/tcp',
                'velocimodel_api-server_1'
            ],
            [
                '00f3cc52f026',
                'service-manager',
                '"./start-service-man…"',
                '11 seconds ago',
                'Up 10 seconds',
                '127.0.0.1:9001->9001/tcp',
                'velocimodel_service-manager_1'
            ],
            [
                'd187007ae065',
                'ceresdb',
                '"./ceresdb"',
                '12 seconds ago',
                'Up 11 seconds',
                '127.0.0.1:7437->7437/tcp',
                'velocimodel_ceresdb_1'
            ]
        ]
        assert multiwidth.load(in_data) == out_data

def test_dumps():
    in_data = [
        [
            '3c3c15c25c3e',
            'frontend',
            '"./start-frontend.sh"',
            '10 seconds ago',
            'Up 8 seconds',
            '0.0.0.0:9000->9000/tcp',
            'velocimodel_frontend_1'
        ],
        [
            'c39392bb88cd',
            'model-manager',
            '"./start-model-manag…"',
            '10 seconds ago',
            'Up 7 seconds',
            '127.0.0.1:9003->9003/tcp',
            'velocimodel_model-manager_1'
        ],
        [
            'ef3acf42bfa4',
            'asset-manager',
            '"./start-asset-manag…"',
            '10 seconds ago',
            'Up 7 seconds',
            '127.0.0.1:9002->9002/tcp',
            'velocimodel_asset-manager_1'
        ],
        [
            '17b161dfa33d',
            'auth-manager',
            '"./start-auth-manage…"',
            '10 seconds ago',
            'Up 7 seconds',
            '127.0.0.1:9005->9005/tcp',
            'velocimodel_auth-manager_1'
        ],
        [
            '79af01ae46a3',
            'api-server',
            '"./start-api-server.…"',
            '11 seconds ago',
            'Up 9 seconds',
            '127.0.0.1:9004->9004/tcp',
            'velocimodel_api-server_1'
        ],
        [
            '00f3cc52f026',
            'service-manager',
            '"./start-service-man…"',
            '11 seconds ago',
            'Up 10 seconds',
            '127.0.0.1:9001->9001/tcp',
            'velocimodel_service-manager_1'
        ],
        [
            'd187007ae065',
            'ceresdb',
            '"./ceresdb"',
            '12 seconds ago',
            'Up 11 seconds',
            '127.0.0.1:7437->7437/tcp',
            'velocimodel_ceresdb_1'
        ]
    ]

    out_data = '''3c3c15c25c3e   frontend          "./start-frontend.sh"    10 seconds ago   Up 8 seconds    0.0.0.0:9000->9000/tcp     velocimodel_frontend_1
c39392bb88cd   model-manager     "./start-model-manag…"   10 seconds ago   Up 7 seconds    127.0.0.1:9003->9003/tcp   velocimodel_model-manager_1
ef3acf42bfa4   asset-manager     "./start-asset-manag…"   10 seconds ago   Up 7 seconds    127.0.0.1:9002->9002/tcp   velocimodel_asset-manager_1
17b161dfa33d   auth-manager      "./start-auth-manage…"   10 seconds ago   Up 7 seconds    127.0.0.1:9005->9005/tcp   velocimodel_auth-manager_1
79af01ae46a3   api-server        "./start-api-server.…"   11 seconds ago   Up 9 seconds    127.0.0.1:9004->9004/tcp   velocimodel_api-server_1
00f3cc52f026   service-manager   "./start-service-man…"   11 seconds ago   Up 10 seconds   127.0.0.1:9001->9001/tcp   velocimodel_service-manager_1
d187007ae065   ceresdb           "./ceresdb"              12 seconds ago   Up 11 seconds   127.0.0.1:7437->7437/tcp   velocimodel_ceresdb_1
'''

    assert multiwidth.dumps(in_data, cell_suffix='   ') == out_data

def test_dumps_header():
    in_data = [
        [
            '3c3c15c25c3e',
            'frontend',
            '"./start-frontend.sh"',
            '10 seconds ago',
            'Up 8 seconds',
            '0.0.0.0:9000->9000/tcp',
            'velocimodel_frontend_1'
        ],
        [
            'c39392bb88cd',
            'model-manager',
            '"./start-model-manag…"',
            '10 seconds ago',
            'Up 7 seconds',
            '127.0.0.1:9003->9003/tcp',
            'velocimodel_model-manager_1'
        ],
        [
            'ef3acf42bfa4',
            'asset-manager',
            '"./start-asset-manag…"',
            '10 seconds ago',
            'Up 7 seconds',
            '127.0.0.1:9002->9002/tcp',
            'velocimodel_asset-manager_1'
        ],
        [
            '17b161dfa33d',
            'auth-manager',
            '"./start-auth-manage…"',
            '10 seconds ago',
            'Up 7 seconds',
            '127.0.0.1:9005->9005/tcp',
            'velocimodel_auth-manager_1'
        ],
        [
            '79af01ae46a3',
            'api-server',
            '"./start-api-server.…"',
            '11 seconds ago',
            'Up 9 seconds',
            '127.0.0.1:9004->9004/tcp',
            'velocimodel_api-server_1'
        ],
        [
            '00f3cc52f026',
            'service-manager',
            '"./start-service-man…"',
            '11 seconds ago',
            'Up 10 seconds',
            '127.0.0.1:9001->9001/tcp',
            'velocimodel_service-manager_1'
        ],
        [
            'd187007ae065',
            'ceresdb',
            '"./ceresdb"',
            '12 seconds ago',
            'Up 11 seconds',
            '127.0.0.1:7437->7437/tcp',
            'velocimodel_ceresdb_1'
        ]
    ]

    out_data = '''CONTAINER ID   IMAGE             COMMAND                  CREATED          STATUS          PORTS                      NAMES
3c3c15c25c3e   frontend          "./start-frontend.sh"    10 seconds ago   Up 8 seconds    0.0.0.0:9000->9000/tcp     velocimodel_frontend_1
c39392bb88cd   model-manager     "./start-model-manag…"   10 seconds ago   Up 7 seconds    127.0.0.1:9003->9003/tcp   velocimodel_model-manager_1
ef3acf42bfa4   asset-manager     "./start-asset-manag…"   10 seconds ago   Up 7 seconds    127.0.0.1:9002->9002/tcp   velocimodel_asset-manager_1
17b161dfa33d   auth-manager      "./start-auth-manage…"   10 seconds ago   Up 7 seconds    127.0.0.1:9005->9005/tcp   velocimodel_auth-manager_1
79af01ae46a3   api-server        "./start-api-server.…"   11 seconds ago   Up 9 seconds    127.0.0.1:9004->9004/tcp   velocimodel_api-server_1
00f3cc52f026   service-manager   "./start-service-man…"   11 seconds ago   Up 10 seconds   127.0.0.1:9001->9001/tcp   velocimodel_service-manager_1
d187007ae065   ceresdb           "./ceresdb"              12 seconds ago   Up 11 seconds   127.0.0.1:7437->7437/tcp   velocimodel_ceresdb_1
'''
    assert multiwidth.dumps(in_data, cell_suffix='   ', headers=["CONTAINER ID", 'IMAGE', 'COMMAND', 'CREATED', 'STATUS', 'PORTS', 'NAMES']) == out_data

def test_dumps_json():
    in_data = [
        {
            'CONTAINER ID': '3c3c15c25c3e',
            'IMAGE': 'frontend',
            'COMMAND': '"./start-frontend.sh"',
            'CREATED': '10 seconds ago',
            'STATUS': 'Up 8 seconds',
            'PORTS': '0.0.0.0:9000->9000/tcp',
            'NAMES': 'velocimodel_frontend_1'
        },
        {
            'CONTAINER ID': 'c39392bb88cd',
            'IMAGE': 'model-manager',
            'COMMAND': '"./start-model-manag…"',
            'CREATED': '10 seconds ago',
            'STATUS': 'Up 7 seconds',
            'PORTS': '127.0.0.1:9003->9003/tcp',
            'NAMES': 'velocimodel_model-manager_1'
        },
        {
            'CONTAINER ID': 'ef3acf42bfa4',
            'IMAGE': 'asset-manager',
            'COMMAND': '"./start-asset-manag…"',
            'CREATED': '10 seconds ago',
            'STATUS': 'Up 7 seconds',
            'PORTS': '127.0.0.1:9002->9002/tcp',
            'NAMES': 'velocimodel_asset-manager_1'
        },
        {
            'CONTAINER ID': '17b161dfa33d',
            'IMAGE': 'auth-manager',
            'COMMAND': '"./start-auth-manage…"',
            'CREATED': '10 seconds ago',
            'STATUS': 'Up 7 seconds',
            'PORTS': '127.0.0.1:9005->9005/tcp',
            'NAMES': 'velocimodel_auth-manager_1'
        },
        {
            'CONTAINER ID': '79af01ae46a3',
            'IMAGE': 'api-server',
            'COMMAND': '"./start-api-server.…"',
            'CREATED': '11 seconds ago',
            'STATUS': 'Up 9 seconds',
            'PORTS': '127.0.0.1:9004->9004/tcp',
            'NAMES': 'velocimodel_api-server_1'
        },
        {
            'CONTAINER ID': '00f3cc52f026',
            'IMAGE': 'service-manager',
            'COMMAND': '"./start-service-man…"',
            'CREATED': '11 seconds ago',
            'STATUS': 'Up 10 seconds',
            'PORTS': '127.0.0.1:9001->9001/tcp',
            'NAMES': 'velocimodel_service-manager_1'
        },
        {
            'CONTAINER ID': 'd187007ae065',
            'IMAGE': 'ceresdb',
            'COMMAND': '"./ceresdb"',
            'CREATED': '12 seconds ago',
            'STATUS': 'Up 11 seconds',
            'PORTS': '127.0.0.1:7437->7437/tcp',
            'NAMES': 'velocimodel_ceresdb_1'
        }
    ]

    out_data = '''CONTAINER ID   IMAGE             COMMAND                  CREATED          STATUS          PORTS                      NAMES
3c3c15c25c3e   frontend          "./start-frontend.sh"    10 seconds ago   Up 8 seconds    0.0.0.0:9000->9000/tcp     velocimodel_frontend_1
c39392bb88cd   model-manager     "./start-model-manag…"   10 seconds ago   Up 7 seconds    127.0.0.1:9003->9003/tcp   velocimodel_model-manager_1
ef3acf42bfa4   asset-manager     "./start-asset-manag…"   10 seconds ago   Up 7 seconds    127.0.0.1:9002->9002/tcp   velocimodel_asset-manager_1
17b161dfa33d   auth-manager      "./start-auth-manage…"   10 seconds ago   Up 7 seconds    127.0.0.1:9005->9005/tcp   velocimodel_auth-manager_1
79af01ae46a3   api-server        "./start-api-server.…"   11 seconds ago   Up 9 seconds    127.0.0.1:9004->9004/tcp   velocimodel_api-server_1
00f3cc52f026   service-manager   "./start-service-man…"   11 seconds ago   Up 10 seconds   127.0.0.1:9001->9001/tcp   velocimodel_service-manager_1
d187007ae065   ceresdb           "./ceresdb"              12 seconds ago   Up 11 seconds   127.0.0.1:7437->7437/tcp   velocimodel_ceresdb_1
'''
    assert multiwidth.dumps(in_data, cell_suffix='   ') == out_data

def test_get_letter_locations():
    in_data = '''CONTAINER ID   IMAGE             COMMAND                  CREATED          STATUS          PORTS                      NAMES
3c3c15c25c3e   frontend          "./start-frontend.sh"    10 seconds ago   Up 8 seconds    0.0.0.0:9000->9000/tcp     velocimodel_frontend_1'''
    out_data = [0, 15, 33, 58, 75, 91, 118, 141]

    assert multiwidth.get_letter_locations(in_data) == out_data

def test_dump():
    test_dir = os.path.dirname(os.path.abspath(__file__))
    with open(f'{test_dir}/data/output.txt', 'w', encoding='utf-8') as out_file:
        
        in_data = [
            [
                '3c3c15c25c3e',
                'frontend',
                '"./start-frontend.sh"',
                '10 seconds ago',
                'Up 8 seconds',
                '0.0.0.0:9000->9000/tcp',
                'velocimodel_frontend_1'
            ],
            [
                'c39392bb88cd',
                'model-manager',
                '"./start-model-manag…"',
                '10 seconds ago',
                'Up 7 seconds',
                '127.0.0.1:9003->9003/tcp',
                'velocimodel_model-manager_1'
            ],
            [
                'ef3acf42bfa4',
                'asset-manager',
                '"./start-asset-manag…"',
                '10 seconds ago',
                'Up 7 seconds',
                '127.0.0.1:9002->9002/tcp',
                'velocimodel_asset-manager_1'
            ],
            [
                '17b161dfa33d',
                'auth-manager',
                '"./start-auth-manage…"',
                '10 seconds ago',
                'Up 7 seconds',
                '127.0.0.1:9005->9005/tcp',
                'velocimodel_auth-manager_1'
            ],
            [
                '79af01ae46a3',
                'api-server',
                '"./start-api-server.…"',
                '11 seconds ago',
                'Up 9 seconds',
                '127.0.0.1:9004->9004/tcp',
                'velocimodel_api-server_1'
            ],
            [
                '00f3cc52f026',
                'service-manager',
                '"./start-service-man…"',
                '11 seconds ago',
                'Up 10 seconds',
                '127.0.0.1:9001->9001/tcp',
                'velocimodel_service-manager_1'
            ],
            [
                'd187007ae065',
                'ceresdb',
                '"./ceresdb"',
                '12 seconds ago',
                'Up 11 seconds',
                '127.0.0.1:7437->7437/tcp',
                'velocimodel_ceresdb_1'
            ]
        ]
        out_data = '''CONTAINER ID   IMAGE             COMMAND                  CREATED          STATUS          PORTS                      NAMES
3c3c15c25c3e   frontend          "./start-frontend.sh"    10 seconds ago   Up 8 seconds    0.0.0.0:9000->9000/tcp     velocimodel_frontend_1
c39392bb88cd   model-manager     "./start-model-manag…"   10 seconds ago   Up 7 seconds    127.0.0.1:9003->9003/tcp   velocimodel_model-manager_1
ef3acf42bfa4   asset-manager     "./start-asset-manag…"   10 seconds ago   Up 7 seconds    127.0.0.1:9002->9002/tcp   velocimodel_asset-manager_1
17b161dfa33d   auth-manager      "./start-auth-manage…"   10 seconds ago   Up 7 seconds    127.0.0.1:9005->9005/tcp   velocimodel_auth-manager_1
79af01ae46a3   api-server        "./start-api-server.…"   11 seconds ago   Up 9 seconds    127.0.0.1:9004->9004/tcp   velocimodel_api-server_1
00f3cc52f026   service-manager   "./start-service-man…"   11 seconds ago   Up 10 seconds   127.0.0.1:9001->9001/tcp   velocimodel_service-manager_1
d187007ae065   ceresdb           "./ceresdb"              12 seconds ago   Up 11 seconds   127.0.0.1:7437->7437/tcp   velocimodel_ceresdb_1
'''

        multiwidth.dump(in_data, out_file, cell_suffix='   ', headers=["CONTAINER ID", 'IMAGE', 'COMMAND', 'CREATED', 'STATUS', 'PORTS', 'NAMES'])

    with open(f'{test_dir}/data/output.txt', 'r', encoding='utf-8') as in_file:
        contents = in_file.read()
        
    assert contents == out_data
