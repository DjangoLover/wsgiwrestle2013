wsgiwrestle2013
===============

get("/games")

TODO: Should actually return more info about the game - a Game object
{
    'tic-tac-toe': 'Tic Tac Toe',
    'pinnocle': "Pinnocle", 
    'blokus': "Blockus(tm)",
    'chess': "Chess",
    'checkers': "Checkers"
}


get("/games/tic-tac-toe")

{
    'game': 'Tic Tac Toe',
    'link': 'tic-tac-toe',
    'current players': 42,
    'active games': [
        {
            'id': 'game12',
            'players': ['jeff', 'player2'],
            'spectating': [],
            'status': 'in progress'
        },
        {
            'id': 'game54',
            'players': ['wayne', 'player2'],
            'spectating': ['jeff', 'player3', 'PeeWee Herman'],
            'status': 'new game'
        },
        {
            'id': 'game45',
            'players': ['jeff', 'player2'],
            'spectating': ['player3', 'PeeWee Herman'],
            'status': 'end game'
        },
        {
            'id': 'game13',
            'players': ['jeff', 'wayne'],
            'spectating': ['PeeWee Herman'],
            'status': 'in progress'
        }
    ],
    'waiting games':[
        {
            'id': 'game42'
            'players': ['wayne'],
            'status': 'waiting',
            'players needed': 1,
            'seats available': 1
        },
        {
            'id': 'game17'
            'players': ['jeff'],
            'status': 'waiting',
            'players needed': 1,
            'seats available': 1
        }
    ]
}

post('/games/tic-tac-toe/start') # assuming valid cookie info

    {
        'id': 'game72',
        'players': ['wayne'],
        'status': 'waiting',
        'players needed': 1,
        'seats available': 1
    }


get('/games/tic-tac-toe/game72')
    
    {
        'id': 'game72',
        'players': ['wayne', 'jeff'],
        'status': 'in progress',
        'spectating': [],
        'current turn': 'wayne',
        'board': [[null, null, null],
                  [null, null, null],
                  [null, null, null]],
        'teams': {'X': ['wayne'],
                  'O': ['jeff']
        }
    }


post('/games/tic-tac-toe/game72', data={'move', [0, 2]})

    {
        'id': 'game72',
        'players': ['wayne', 'jeff'],
        'status': 'in progress',
        'spectating': [],
        'current turn': 'jeff',
        'board': [[null, null, null],
                  [null, null, null],
                  ['X',  null, null]],
        'teams': {'X': ['wayne'],
                  'O': ['jeff']
        }
    }


post('/games/tic-tac-toe/game72', data={'move': [0, 1]})

    {
        'id': 'game72',
        'error': 'Not your turn',
        'players': ['wayne', 'jeff'],
        'status': 'in progress',
        'spectating': [],
        'current turn': 'jeff',
        'board': [[null, null, null],
                  [null, null, null],
                  ['X',  null, null]],
        'teams': {'X': ['wayne'],
                  'O': ['jeff']
        }
    }


get('/games/tic-tac-toe/game72')
    
    {
        'id': 'game72',
        'players': ['wayne', 'jeff'],
        'status': 'in progress',
        'spectating': [],
        'current turn': 'wayne',
        'board': [[null, null, null],
                  [null, 'O',  null],
                  ['X',  null, null]],
        'teams': {'X': ['wayne'],
                  'O': ['jeff']
        }
    }

and so on...

post('/games/tic-tac-toe/game72', data={'move': [0, 1]})
    {
        'id': 'game72',
        'players': ['wayne', 'jeff'],
        'status': 'end game',
        'winning team': null,
        'spectating': [],
        'current turn': 'wayne',
        'board': [['X',  'O',  'X' ],
                  ['O',  'O',  'X' ],
                  ['X',  'X',  'O' ]],
        'teams': {'X': ['wayne'],
                  'O': ['jeff']
        }
    }


post('/games/tic-tac-toe/reset/game72')
    
    {
        'id': 'game72',
        'players': ['wayne', 'jeff'],
        'status': 'ready',
        'spectating': [],
        'current turn': 'wayne',
        'board': [[null, null, null],
                  [null, null, null],
                  [null, null, null]],
        'teams': {'X': ['wayne'],
                  'O': ['jeff']
        }
    }
