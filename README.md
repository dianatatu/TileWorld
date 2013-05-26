Random notes

```python
{'H': 4,
 'W': 4,
 'cells': [[{'agents': [],
             'color': 'green',
             'h': -2,
             'tiles': [],
             'x': 0,
             'y': 0},
            {'agents': [],
             'color': 'none',
             'h': 0,
             'tiles': [],
             'x': 0,
             'y': 1},
            {'agents': [],
             'color': 'none',
             'h': 0,
             'tiles': [],
             'x': 0,
             'y': 2},
            {'agents': [('agent1', 0, 3, 'green')],
             'color': 'none',
             'h': 0,
             'tiles': [],
             'x': 0,
             'y': 3}],
           [{'agents': [],
             'color': 'none',
             'h': 0,
             'tiles': [],
             'x': 1,
             'y': 0},
            {'agents': [],
             'color': 'none',
             'h': 1,
             'tiles': [],
             'x': 1,
             'y': 1},
            {'agents': [],
             'color': 'blue',
             'h': -2,
             'tiles': [],
             'x': 1,
             'y': 2},
            {'agents': [],
             'color': 'none',
             'h': 0,
             'tiles': ['green'],
             'x': 1,
             'y': 3}],
           [{'agents': [],
             'color': 'none',
             'h': 0,
             'tiles': ['green'],
             'x': 2,
             'y': 0},
            {'agents': [],
             'color': 'none',
             'h': 1,
             'tiles': [],
             'x': 2,
             'y': 1},
            {'agents': [],
             'color': 'none',
             'h': 1,
             'tiles': [],
             'x': 2,
             'y': 2},
            {'agents': [],
             'color': 'none',
             'h': 0,
             'tiles': ['blue', 'blue'],
             'x': 2,
             'y': 3}],
           [{'agents': [('agent0', 3, 0, 'blue')],
             'color': 'none',
             'h': 0,
             'tiles': [],
             'x': 3,
             'y': 0},
            {'agents': [],
             'color': 'none',
             'h': 0,
             'tiles': [],
             'x': 3,
             'y': 1},
            {'agents': [],
             'color': 'none',
             'h': 0,
             'tiles': [],
             'x': 3,
             'y': 2},
            {'agents': [],
             'color': 'none',
             'h': 0,
             'tiles': [],
             'x': 3,
             'y': 3}]]}

```


```python
[1369592878] agent0: Requesting entire state
[1369592878] agent1: Requesting entire state
--------------------------------
[T = 1369592878]
--------------------------------
-2    	 0 		 0 		 0,0 		
 0 		 # 		-2		 0* 		
 0* 		 # 		 # 		 0** 		
 0,0 		 0 		 0 		 0 		
--------------------------------
[environment] {'from': 'agent0', 'type': 'request_entire_state'}
[1369592878] agent0: I have the entire state!
[1369592878] agent0: Sending proposal to agent1: {'proposal': {'initiator': 'agent0', 'color': 'blue', 'tile': (2, 3), 'hole': (1, 2), 'reward': 11, 'id': UUID('0f6906fa-8c92-4900-a728-9be61b52d78d')}, 'type': 'proposal'}
[1369592878] agent0: Requesting action: {'y': 1, 'x': 3, 'type': 'go_to'}
[1369592878] agent1: Received proposal UUID('0f6906fa-8c92-4900-a728-9be61b52d78d') from 'agent0'
[1369592878] agent1: I have no knowledge about the grid. Postponing proposal.
--------------------------------
[T = 1369592879]
--------------------------------
-2		 0 		 0 		 0,0 		
 0 		 # 		-2		 0* 		
 0* 		 # 		 # 		 0** 		
 0,0 		 0 		 0 		 0 		
--------------------------------
[environment] {'from': 'agent1', 'type': 'request_entire_state'}
[1369592879] agent1: I have the entire state!
[1369592879] agent1: Sending proposal to agent0: {'proposal': {'initiator': 'agent1', 'color': 'green', 'tile': (2, 0), 'hole': (0, 0), 'reward': 11, 'id': UUID('3b3a8933-2f04-4ded-abf8-f79e395164c5')}, 'type': 'proposal'}
[1369592879] agent0: Received proposal UUID('3b3a8933-2f04-4ded-abf8-f79e395164c5') from 'agent1'
[1369592879] agent0: Investigating ...
[1369592879] agent1: Accept proposal UUID('0f6906fa-8c92-4900-a728-9be61b52d78d') from 'agent0'. Actual reward = 11-8 = 3
[1369592879] agent1: Requesting action: {'y': 3, 'x': 1, 'type': 'go_to'}
[1369592879] agent0: Accept proposal UUID('3b3a8933-2f04-4ded-abf8-f79e395164c5') from 'agent1'. Actual reward = 11-10 = 1
[1369592879] agent0: :) 'agent1' accepted proposal {'initiator': 'agent0', 'color': 'blue', 'tile': (2, 3), 'hole': (1, 2), 'reward': 11, 'id': UUID('0f6906fa-8c92-4900-a728-9be61b52d78d')}
[1369592879] agent1: :) 'agent0' accepted proposal {'initiator': 'agent1', 'color': 'green', 'tile': (2, 0), 'hole': (0, 0), 'reward': 11, 'id': UUID('3b3a8933-2f04-4ded-abf8-f79e395164c5')}
[1369592879] agent1: Shake hands on UUID('0f6906fa-8c92-4900-a728-9be61b52d78d') with 'agent0' for 11 points.
[1369592879] agent0: Shake hands on UUID('3b3a8933-2f04-4ded-abf8-f79e395164c5') with 'agent1' for 11 points.
--------------------------------
[T = 1369592880]
--------------------------------
-2		 0 		 0 		 0,0 		
 0 		 # 		-2		 0* 		
 0* 		 # 		 # 		 0** 		
 0,0 		 0 		 0 		 0 		
--------------------------------
[environment] {'action': {'y': 1, 'x': 3, 'type': 'go_to'}, 'from': 'agent0', 'type': 'request_action'}
[1369592880] agent0: Requesting action: {'y': 2, 'x': 3, 'type': 'go_to'}
--------------------------------
[T = 1369592881]
--------------------------------
-2		 0 		 0 		 0,0 		
 0 		 # 		-2		 0* 		
 0* 		 # 		 # 		 0** 		
 0 		 0,0 		 0 		 0 		
--------------------------------
[environment] {'action': {'y': 3, 'x': 1, 'type': 'go_to'}, 'from': 'agent1', 'type': 'request_action'}
[1369592881] agent1: Requesting action: {'y': 3, 'x': 1, 'type': 'pick', 'color': 'green'}
--------------------------------
[T = 1369592882]
--------------------------------
-2		 0 		 0 		 0 		
 0 		 # 		-2		 0*,0 		
 0* 		 # 		 # 		 0** 		
 0 		 0,0 		 0 		 0 		
--------------------------------
[environment] {'to': 'agent1', 'type': 'transfer_points', 'value': 11, 'from': 'agent0'}
[1369592882] agent0: I transferred 11 points to 'agent1'
--------------------------------
[T = 1369592883]
--------------------------------
-2		 0 		 0 		 0 		
 0 		 # 		-2		 0*,11 		
 0* 		 # 		 # 		 0** 		
 0 		 0,-11 		 0 		 0 		
--------------------------------
[environment] {'to': 'agent0', 'type': 'transfer_points', 'value': 11, 'from': 'agent1'}
[1369592883] agent1: I transferred 11 points to 'agent0'
--------------------------------
[T = 1369592884]
--------------------------------
-2		 0 		 0 		 0 		
 0 		 # 		-2		 0*,0 		
 0* 		 # 		 # 		 0** 		
 0 		 0,0 		 0 		 0 		
--------------------------------
[environment] {'action': {'y': 2, 'x': 3, 'type': 'go_to'}, 'from': 'agent0', 'type': 'request_action'}
[1369592884] agent0: Requesting action: {'y': 3, 'x': 3, 'type': 'go_to'}
--------------------------------
[T = 1369592885]
--------------------------------
-2		 0 		 0 		 0 		
 0 		 # 		-2		 0*,0 		
 0* 		 # 		 # 		 0** 		
 0 		 0 		 0,0 		 0 		
--------------------------------
[environment] {'action': {'y': 3, 'x': 1, 'type': 'pick', 'color': 'green'}, 'from': 'agent1', 'type': 'request_action'}
[1369592885] agent1: Requesting action: {'y': 3, 'x': 0, 'type': 'go_to'}
--------------------------------
[T = 1369592886]
--------------------------------
-2		 0 		 0 		 0 		
 0 		 # 		-2		 0,0*  		
 0* 		 # 		 # 		 0** 		
 0 		 0 		 0,0 		 0 		
--------------------------------
[environment] {'action': {'y': 3, 'x': 3, 'type': 'go_to'}, 'from': 'agent0', 'type': 'request_action'}
[1369592886] agent0: Requesting action: {'y': 3, 'x': 2, 'type': 'go_to'}
--------------------------------
[T = 1369592887]
--------------------------------
-2		 0 		 0 		 0 		
 0 		 # 		-2		 0,0*  		
 0* 		 # 		 # 		 0** 		
 0 		 0 		 0 		 0,0 		
--------------------------------
[environment] {'action': {'y': 3, 'x': 0, 'type': 'go_to'}, 'from': 'agent1', 'type': 'request_action'}
[1369592887] agent1: Requesting action: {'y': 2, 'x': 0, 'type': 'go_to'}
--------------------------------
[T = 1369592888]
--------------------------------
-2		 0 		 0 		 0,0*  		
 0 		 # 		-2		 0 		
 0* 		 # 		 # 		 0** 		
 0 		 0 		 0 		 0,0 		
--------------------------------
[environment] {'action': {'y': 3, 'x': 2, 'type': 'go_to'}, 'from': 'agent0', 'type': 'request_action'}
[1369592888] agent0: Requesting action: {'y': 3, 'x': 2, 'type': 'pick', 'color': 'blue'}
--------------------------------
[T = 1369592889]
--------------------------------
-2		 0 		 0 		 0,0*  		
 0 		 # 		-2		 0 		
 0* 		 # 		 # 		 0**,0 		
 0 		 0 		 0 		 0 		
--------------------------------
[environment] {'action': {'y': 2, 'x': 0, 'type': 'go_to'}, 'from': 'agent1', 'type': 'request_action'}
[1369592889] agent1: Requesting action: {'y': 1, 'x': 0, 'type': 'go_to'}
--------------------------------
[T = 1369592890]
--------------------------------
-2		 0 		 0,0*  		 0 		
 0 		 # 		-2		 0 		
 0* 		 # 		 # 		 0**,0 		
 0 		 0 		 0 		 0 		
--------------------------------
[environment] {'action': {'y': 3, 'x': 2, 'type': 'pick', 'color': 'blue'}, 'from': 'agent0', 'type': 'request_action'}
[1369592890] agent0: Requesting action: {'y': 3, 'x': 1, 'type': 'go_to'}
--------------------------------
[T = 1369592891]
--------------------------------
-2		 0 		 0,0*  		 0 		
 0 		 # 		-2		 0 		
 0* 		 # 		 # 		 0*,0*  		
 0 		 0 		 0 		 0 		
--------------------------------
[environment] {'action': {'y': 1, 'x': 0, 'type': 'go_to'}, 'from': 'agent1', 'type': 'request_action'}
[1369592891] agent1: Requesting action: {'y': 0, 'x': 0, 'type': 'drop', 'color': 'green'}
--------------------------------
[T = 1369592892]
--------------------------------
-2		 0,0*  		 0 		 0 		
 0 		 # 		-2		 0 		
 0* 		 # 		 # 		 0*,0*  		
 0 		 0 		 0 		 0 		
--------------------------------
[environment] {'action': {'y': 3, 'x': 1, 'type': 'go_to'}, 'from': 'agent0', 'type': 'request_action'}
[1369592892] agent0: Requesting action: {'y': 2, 'x': 1, 'type': 'drop', 'color': 'blue'}
--------------------------------
[T = 1369592893]
--------------------------------
-2		 0,0*  		 0 		 0 		
 0 		 # 		-2		 0,0*  		
 0* 		 # 		 # 		 0* 		
 0 		 0 		 0 		 0 		
--------------------------------
[environment] {'action': {'y': 0, 'x': 0, 'points': 10, 'type': 'drop', 'color': 'green'}, 'from': 'agent1', 'type': 'request_action'}
[1369592893] agent1: My new plan: {'tile': (2, 3), 'color': 'blue', 'hole': (1, 2), 'id': UUID('3ca07c6f-d337-413b-8057-ce7f5f64e867'), 'actions': [{'y': 2, 'x': 0, 'type': 'go_to'}, {'y': 3, 'x': 0, 'type': 'go_to'}, {'y': 3, 'x': 1, 'type': 'go_to'}, {'y': 3, 'x': 2, 'type': 'go_to'}, {'y': 3, 'x': 2, 'type': 'pick', 'color': 'blue'}, {'y': 3, 'x': 1, 'type': 'go_to'}, {'y': 2, 'x': 1, 'type': 'drop', 'color': 'blue'}]}
[1369592893] agent1: Requesting action: {'y': 2, 'x': 0, 'type': 'go_to'}
--------------------------------
[T = 1369592894]
--------------------------------
-1		 0,10 		 0 		 0 		
 0 		 # 		-2		 0,0*  		
 0* 		 # 		 # 		 0* 		
 0 		 0 		 0 		 0 		
--------------------------------
[environment] {'action': {'y': 2, 'x': 1, 'points': 10, 'type': 'drop', 'color': 'blue'}, 'from': 'agent0', 'type': 'request_action'}
[1369592894] agent0: My new plan: {'tile': (2, 0), 'color': 'green', 'hole': (0, 0), 'id': UUID('95fb9f30-56f3-48e3-80f8-18537fefecb7'), 'actions': [{'y': 3, 'x': 2, 'type': 'go_to'}, {'y': 3, 'x': 3, 'type': 'go_to'}, {'y': 2, 'x': 3, 'type': 'go_to'}, {'y': 1, 'x': 3, 'type': 'go_to'}, {'y': 0, 'x': 3, 'type': 'go_to'}, {'y': 0, 'x': 2, 'type': 'go_to'}, {'y': 0, 'x': 2, 'type': 'pick', 'color': 'green'}, {'y': 0, 'x': 1, 'type': 'go_to'}, {'y': 0, 'x': 0, 'type': 'drop', 'color': 'green'}]}
[1369592894] agent0: Requesting action: {'y': 3, 'x': 2, 'type': 'go_to'}
--------------------------------
[T = 1369592895]
--------------------------------
-1		 0,10 		 0 		 0 		
 0 		 # 		-1		 0,10 		
 0* 		 # 		 # 		 0* 		
 0 		 0 		 0 		 0 		
--------------------------------
[environment] {'action': {'y': 2, 'x': 0, 'type': 'go_to'}, 'from': 'agent1', 'type': 'request_action'}
[1369592895] agent1: Requesting action: {'y': 3, 'x': 0, 'type': 'go_to'}
--------------------------------
[T = 1369592896]
--------------------------------
-1		 0 		 0,10 		 0 		
 0 		 # 		-1		 0,10 		
 0* 		 # 		 # 		 0* 		
 0 		 0 		 0 		 0 		
--------------------------------
[environment] {'action': {'y': 3, 'x': 2, 'type': 'go_to'}, 'from': 'agent0', 'type': 'request_action'}
[1369592896] agent0: Requesting action: {'y': 3, 'x': 3, 'type': 'go_to'}
--------------------------------
[T = 1369592897]
--------------------------------
-1		 0 		 0,10 		 0 		
 0 		 # 		-1		 0 		
 0* 		 # 		 # 		 0*,10 		
 0 		 0 		 0 		 0 		
--------------------------------
[environment] {'action': {'y': 3, 'x': 0, 'type': 'go_to'}, 'from': 'agent1', 'type': 'request_action'}
[1369592897] agent1: Requesting action: {'y': 3, 'x': 1, 'type': 'go_to'}
--------------------------------
[T = 1369592898]
--------------------------------
-1		 0 		 0 		 0,10 		
 0 		 # 		-1		 0 		
 0* 		 # 		 # 		 0*,10 		
 0 		 0 		 0 		 0 		
--------------------------------
[environment] {'action': {'y': 3, 'x': 3, 'type': 'go_to'}, 'from': 'agent0', 'type': 'request_action'}
[1369592898] agent0: Requesting action: {'y': 2, 'x': 3, 'type': 'go_to'}
--------------------------------
[T = 1369592899]
--------------------------------
-1		 0 		 0 		 0,10 		
 0 		 # 		-1		 0 		
 0* 		 # 		 # 		 0* 		
 0 		 0 		 0 		 0,10 		
--------------------------------
[environment] {'action': {'y': 3, 'x': 1, 'type': 'go_to'}, 'from': 'agent1', 'type': 'request_action'}
[1369592899] agent1: Requesting action: {'y': 3, 'x': 2, 'type': 'go_to'}
--------------------------------
[T = 1369592900]
--------------------------------
-1		 0 		 0 		 0 		
 0 		 # 		-1		 0,10 		
 0* 		 # 		 # 		 0* 		
 0 		 0 		 0 		 0,10 		
--------------------------------
[environment] {'action': {'y': 2, 'x': 3, 'type': 'go_to'}, 'from': 'agent0', 'type': 'request_action'}
[1369592900] agent0: Requesting action: {'y': 1, 'x': 3, 'type': 'go_to'}
--------------------------------
[T = 1369592901]
--------------------------------
-1		 0 		 0 		 0 		
 0 		 # 		-1		 0,10 		
 0* 		 # 		 # 		 0* 		
 0 		 0 		 0,10 		 0 		
--------------------------------
[environment] {'action': {'y': 3, 'x': 2, 'type': 'go_to'}, 'from': 'agent1', 'type': 'request_action'}
[1369592901] agent1: Requesting action: {'y': 3, 'x': 2, 'type': 'pick', 'color': 'blue'}
--------------------------------
[T = 1369592902]
--------------------------------
-1		 0 		 0 		 0 		
 0 		 # 		-1		 0 		
 0* 		 # 		 # 		 0*,10 		
 0 		 0 		 0,10 		 0 		
--------------------------------
[environment] {'action': {'y': 1, 'x': 3, 'type': 'go_to'}, 'from': 'agent0', 'type': 'request_action'}
[1369592902] agent0: Requesting action: {'y': 0, 'x': 3, 'type': 'go_to'}
--------------------------------
[T = 1369592903]
--------------------------------
-1		 0 		 0 		 0 		
 0 		 # 		-1		 0 		
 0* 		 # 		 # 		 0*,10 		
 0 		 0,10 		 0 		 0 		
--------------------------------
[environment] {'action': {'y': 3, 'x': 2, 'type': 'pick', 'color': 'blue'}, 'from': 'agent1', 'type': 'request_action'}
[1369592903] agent1: Requesting action: {'y': 3, 'x': 1, 'type': 'go_to'}
--------------------------------
[T = 1369592904]
--------------------------------
-1		 0 		 0 		 0 		
 0 		 # 		-1		 0 		
 0* 		 # 		 # 		 0,10*  		
 0 		 0,10 		 0 		 0 		
--------------------------------
[environment] {'action': {'y': 0, 'x': 3, 'type': 'go_to'}, 'from': 'agent0', 'type': 'request_action'}
[1369592904] agent0: Requesting action: {'y': 0, 'x': 2, 'type': 'go_to'}
--------------------------------
[T = 1369592905]
--------------------------------
-1		 0 		 0 		 0 		
 0 		 # 		-1		 0 		
 0* 		 # 		 # 		 0,10*  		
 0,10 		 0 		 0 		 0 		
--------------------------------
[environment] {'action': {'y': 3, 'x': 1, 'type': 'go_to'}, 'from': 'agent1', 'type': 'request_action'}
[1369592905] agent1: Requesting action: {'y': 2, 'x': 1, 'type': 'drop', 'color': 'blue'}
--------------------------------
[T = 1369592906]
--------------------------------
-1		 0 		 0 		 0 		
 0 		 # 		-1		 0,10*  		
 0* 		 # 		 # 		 0 		
 0,10 		 0 		 0 		 0 		
--------------------------------
[environment] {'action': {'y': 0, 'x': 2, 'type': 'go_to'}, 'from': 'agent0', 'type': 'request_action'}
[1369592906] agent0: Requesting action: {'y': 0, 'x': 2, 'type': 'pick', 'color': 'green'}
--------------------------------
[T = 1369592907]
--------------------------------
-1		 0 		 0 		 0 		
 0 		 # 		-1		 0,10*  		
 0*,10 		 # 		 # 		 0 		
 0 		 0 		 0 		 0 		
--------------------------------
[environment] {'action': {'y': 2, 'x': 1, 'points': 50, 'type': 'drop', 'color': 'blue'}, 'from': 'agent1', 'type': 'request_action'}
--------------------------------
[T = 1369592908]
--------------------------------
-1		 0 		 0 		 0 		
 0 		 # 		 0		 0,10 		
 0*,60 		 # 		 # 		 0 		
 0 		 0 		 0 		 0 		
--------------------------------
[environment] {'action': {'y': 0, 'x': 2, 'type': 'pick', 'color': 'green'}, 'from': 'agent0', 'type': 'request_action'}
[1369592908] agent0: Requesting action: {'y': 0, 'x': 1, 'type': 'go_to'}
--------------------------------
[T = 1369592909]
--------------------------------
-1		 0 		 0 		 0 		
 0 		 # 		 0		 0,10 		
 0,60*  		 # 		 # 		 0 		
 0 		 0 		 0 		 0 		
--------------------------------
[environment] {'action': {'y': 0, 'x': 1, 'type': 'go_to'}, 'from': 'agent0', 'type': 'request_action'}
[1369592909] agent0: Requesting action: {'y': 0, 'x': 0, 'type': 'drop', 'color': 'green'}
--------------------------------
[T = 1369592910]
--------------------------------
-1		 0 		 0 		 0 		
 0,60*  		 # 		 0		 0,10 		
 0 		 # 		 # 		 0 		
 0 		 0 		 0 		 0 		
--------------------------------
[environment] {'action': {'y': 0, 'x': 0, 'points': 50, 'type': 'drop', 'color': 'green'}, 'from': 'agent0', 'type': 'request_action'}
--------------------------------
[T = 1369592911]
--------------------------------
 0		 0 		 0 		 0 		
 0,60 		 # 		 0		 0,60 		
 0 		 # 		 # 		 0 		
 0 		 0 		 0 		 0 		
--------------------------------

```
