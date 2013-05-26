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
[1369593160] agent0: Requesting entire state
[1369593160] agent1: Requesting entire state
--------------------------------
[T = 1369593160]
--------------------------------
-2 	 0 		 0 		 0,0 		
 0 		 # 		-2		 0* 		
 0* 		 # 		 # 		 0** 		
 0,0 		 0 		 0 		 0 		
--------------------------------
[environment] {'from': 'agent0', 'type': 'request_entire_state'}
[1369593160] agent0: {'grid': {'H': 4, 'cells': [[{'tiles': [], 'color': 'green', 'h': -2, 'agents': [], 'y': 0, 'x': 0}, {'tiles': [], 'color': 'none', 'h': 0, 'agents': [], 'y': 1, 'x': 0}, {'tiles': [], 'color': 'none', 'h': 0, 'agents': [], 'y': 2, 'x': 0}, {'tiles': [], 'color': 'none', 'h': 0, 'agents': [('agent1', 0, 3, 'green')], 'y': 3, 'x': 0}], [{'tiles': [], 'color': 'none', 'h': 0, 'agents': [], 'y': 0, 'x': 1}, {'tiles': [], 'color': 'none', 'h': 1, 'agents': [], 'y': 1, 'x': 1}, {'tiles': [], 'color': 'blue', 'h': -2, 'agents': [], 'y': 2, 'x': 1}, {'tiles': ['green'], 'color': 'none', 'h': 0, 'agents': [], 'y': 3, 'x': 1}], [{'tiles': ['green'], 'color': 'none', 'h': 0, 'agents': [], 'y': 0, 'x': 2}, {'tiles': [], 'color': 'none', 'h': 1, 'agents': [], 'y': 1, 'x': 2}, {'tiles': [], 'color': 'none', 'h': 1, 'agents': [], 'y': 2, 'x': 2}, {'tiles': ['blue', 'blue'], 'color': 'none', 'h': 0, 'agents': [], 'y': 3, 'x': 2}], [{'tiles': [], 'color': 'none', 'h': 0, 'agents': [('agent0', 3, 0, 'blue')], 'y': 0, 'x': 3}, {'tiles': [], 'color': 'none', 'h': 0, 'agents': [], 'y': 1, 'x': 3}, {'tiles': [], 'color': 'none', 'h': 0, 'agents': [], 'y': 2, 'x': 3}, {'tiles': [], 'color': 'none', 'h': 0, 'agents': [], 'y': 3, 'x': 3}]], 'W': 4}, 'type': 'response_entire_state'}
[1369593160] agent0: I have the entire state!
[1369593160] agent0: Sending proposal to agent1: {'proposal': {'initiator': 'agent0', 'color': 'blue', 'tile': (2, 3), 'hole': (1, 2), 'reward': 11, 'id': UUID('63c11ad0-60d0-4f33-85da-a3c1c9688b59')}, 'type': 'proposal'}
[1369593160] agent0: Requesting action: {'y': 1, 'x': 3, 'type': 'go_to'}
[1369593160] agent1: {'from': 'agent0', 'proposal': {'initiator': 'agent0', 'color': 'blue', 'tile': (2, 3), 'hole': (1, 2), 'reward': 11, 'id': UUID('63c11ad0-60d0-4f33-85da-a3c1c9688b59')}, 'type': 'proposal'}
[1369593160] agent1: Received proposal UUID('63c11ad0-60d0-4f33-85da-a3c1c9688b59') from 'agent0'
[1369593160] agent1: I have no knowledge about the grid. Postponing proposal.
--------------------------------
[T = 1369593161]
--------------------------------
-2		 0 		 0 		 0,0 		
 0 		 # 		-2		 0* 		
 0* 		 # 		 # 		 0** 		
 0,0 		 0 		 0 		 0 		
--------------------------------
[environment] {'from': 'agent1', 'type': 'request_entire_state'}
[1369593161] agent1: {'grid': {'H': 4, 'cells': [[{'tiles': [], 'color': 'green', 'h': -2, 'agents': [], 'y': 0, 'x': 0}, {'tiles': [], 'color': 'none', 'h': 0, 'agents': [], 'y': 1, 'x': 0}, {'tiles': [], 'color': 'none', 'h': 0, 'agents': [], 'y': 2, 'x': 0}, {'tiles': [], 'color': 'none', 'h': 0, 'agents': [('agent1', 0, 3, 'green')], 'y': 3, 'x': 0}], [{'tiles': [], 'color': 'none', 'h': 0, 'agents': [], 'y': 0, 'x': 1}, {'tiles': [], 'color': 'none', 'h': 1, 'agents': [], 'y': 1, 'x': 1}, {'tiles': [], 'color': 'blue', 'h': -2, 'agents': [], 'y': 2, 'x': 1}, {'tiles': ['green'], 'color': 'none', 'h': 0, 'agents': [], 'y': 3, 'x': 1}], [{'tiles': ['green'], 'color': 'none', 'h': 0, 'agents': [], 'y': 0, 'x': 2}, {'tiles': [], 'color': 'none', 'h': 1, 'agents': [], 'y': 1, 'x': 2}, {'tiles': [], 'color': 'none', 'h': 1, 'agents': [], 'y': 2, 'x': 2}, {'tiles': ['blue', 'blue'], 'color': 'none', 'h': 0, 'agents': [], 'y': 3, 'x': 2}], [{'tiles': [], 'color': 'none', 'h': 0, 'agents': [('agent0', 3, 0, 'blue')], 'y': 0, 'x': 3}, {'tiles': [], 'color': 'none', 'h': 0, 'agents': [], 'y': 1, 'x': 3}, {'tiles': [], 'color': 'none', 'h': 0, 'agents': [], 'y': 2, 'x': 3}, {'tiles': [], 'color': 'none', 'h': 0, 'agents': [], 'y': 3, 'x': 3}]], 'W': 4}, 'type': 'response_entire_state'}
[1369593161] agent1: I have the entire state!
[1369593161] agent1: Sending proposal to agent0: {'proposal': {'initiator': 'agent1', 'color': 'green', 'tile': (2, 0), 'hole': (0, 0), 'reward': 11, 'id': UUID('9ba20f5f-5a4c-4e77-924a-984583ead17b')}, 'type': 'proposal'}
[1369593161] agent0: {'from': 'agent1', 'proposal': {'initiator': 'agent1', 'color': 'green', 'tile': (2, 0), 'hole': (0, 0), 'reward': 11, 'id': UUID('9ba20f5f-5a4c-4e77-924a-984583ead17b')}, 'type': 'proposal'}
[1369593161] agent0: Received proposal UUID('9ba20f5f-5a4c-4e77-924a-984583ead17b') from 'agent1'
[1369593161] agent0: Investigating ...
[1369593161] agent1: Accept proposal UUID('63c11ad0-60d0-4f33-85da-a3c1c9688b59') from 'agent0'. Actual reward = 11-8 = 3
[1369593161] agent1: Requesting action: {'y': 3, 'x': 1, 'type': 'go_to'}
[1369593161] agent0: Accept proposal UUID('9ba20f5f-5a4c-4e77-924a-984583ead17b') from 'agent1'. Actual reward = 11-10 = 1
[1369593161] agent0: {'from': 'agent1', 'proposal': {'initiator': 'agent0', 'color': 'blue', 'tile': (2, 3), 'hole': (1, 2), 'reward': 11, 'id': UUID('63c11ad0-60d0-4f33-85da-a3c1c9688b59')}, 'type': 'accept_proposal'}
[1369593161] agent1: {'from': 'agent0', 'proposal': {'initiator': 'agent1', 'color': 'green', 'tile': (2, 0), 'hole': (0, 0), 'reward': 11, 'id': UUID('9ba20f5f-5a4c-4e77-924a-984583ead17b')}, 'type': 'accept_proposal'}
[1369593161] agent0: :) 'agent1' accepted proposal {'initiator': 'agent0', 'color': 'blue', 'tile': (2, 3), 'hole': (1, 2), 'reward': 11, 'id': UUID('63c11ad0-60d0-4f33-85da-a3c1c9688b59')}
[1369593161] agent1: :) 'agent0' accepted proposal {'initiator': 'agent1', 'color': 'green', 'tile': (2, 0), 'hole': (0, 0), 'reward': 11, 'id': UUID('9ba20f5f-5a4c-4e77-924a-984583ead17b')}
[1369593161] agent1: {'from': 'agent0', 'proposal': {'from': 'agent1', 'proposal': {'initiator': 'agent0', 'color': 'blue', 'tile': (2, 3), 'hole': (1, 2), 'reward': 11, 'id': UUID('63c11ad0-60d0-4f33-85da-a3c1c9688b59')}, 'type': 'accept_proposal'}, 'type': 'shake_hands'}
[1369593161] agent0: {'from': 'agent1', 'proposal': {'from': 'agent0', 'proposal': {'initiator': 'agent1', 'color': 'green', 'tile': (2, 0), 'hole': (0, 0), 'reward': 11, 'id': UUID('9ba20f5f-5a4c-4e77-924a-984583ead17b')}, 'type': 'accept_proposal'}, 'type': 'shake_hands'}
[1369593161] agent1: Shake hands on UUID('63c11ad0-60d0-4f33-85da-a3c1c9688b59') with 'agent0' for 11 points.
[1369593161] agent0: Shake hands on UUID('9ba20f5f-5a4c-4e77-924a-984583ead17b') with 'agent1' for 11 points.
--------------------------------
[T = 1369593162]
--------------------------------
-2		 0 		 0 		 0,0 		
 0 		 # 		-2		 0* 		
 0* 		 # 		 # 		 0** 		
 0,0 		 0 		 0 		 0 		
--------------------------------
[environment] {'action': {'y': 1, 'x': 3, 'type': 'go_to'}, 'from': 'agent0', 'type': 'request_action'}
[1369593162] agent0: {'action': {'y': 1, 'x': 3, 'type': 'go_to'}, 'status': 'OK', 'type': 'response_action'}
[1369593162] agent0: Requesting action: {'y': 2, 'x': 3, 'type': 'go_to'}
--------------------------------
[T = 1369593163]
--------------------------------
-2		 0 		 0 		 0,0 		
 0 		 # 		-2		 0* 		
 0* 		 # 		 # 		 0** 		
 0 		 0,0 		 0 		 0 		
--------------------------------
[environment] {'action': {'y': 3, 'x': 1, 'type': 'go_to'}, 'from': 'agent1', 'type': 'request_action'}
[1369593163] agent1: {'action': {'y': 3, 'x': 1, 'type': 'go_to'}, 'status': 'OK', 'type': 'response_action'}
[1369593163] agent1: Requesting action: {'y': 3, 'x': 1, 'type': 'pick', 'color': 'green'}
--------------------------------
[T = 1369593164]
--------------------------------
-2		 0 		 0 		 0 		
 0 		 # 		-2		 0*,0 		
 0* 		 # 		 # 		 0** 		
 0 		 0,0 		 0 		 0 		
--------------------------------
[environment] {'to': 'agent1', 'type': 'transfer_points', 'value': 11, 'from': 'agent0'}
[1369593164] agent0: {'status': 'OK', 'from': 'agent0', 'type': 'response_transfer_points', 'value': 11, 'to': 'agent1'}
[1369593164] agent0: I transferred 11 points to 'agent1'
--------------------------------
[T = 1369593165]
--------------------------------
-2		 0 		 0 		 0 		
 0 		 # 		-2		 0*,11 		
 0* 		 # 		 # 		 0** 		
 0 		 0,-11 		 0 		 0 		
--------------------------------
[environment] {'to': 'agent0', 'type': 'transfer_points', 'value': 11, 'from': 'agent1'}
[1369593165] agent1: {'status': 'OK', 'from': 'agent1', 'type': 'response_transfer_points', 'value': 11, 'to': 'agent0'}
[1369593165] agent1: I transferred 11 points to 'agent0'
--------------------------------
[T = 1369593166]
--------------------------------
-2		 0 		 0 		 0 		
 0 		 # 		-2		 0*,0 		
 0* 		 # 		 # 		 0** 		
 0 		 0,0 		 0 		 0 		
--------------------------------
[environment] {'action': {'y': 2, 'x': 3, 'type': 'go_to'}, 'from': 'agent0', 'type': 'request_action'}
[1369593166] agent0: {'action': {'y': 2, 'x': 3, 'type': 'go_to'}, 'status': 'OK', 'type': 'response_action'}
[1369593166] agent0: Requesting action: {'y': 3, 'x': 3, 'type': 'go_to'}
--------------------------------
[T = 1369593167]
--------------------------------
-2		 0 		 0 		 0 		
 0 		 # 		-2		 0*,0 		
 0* 		 # 		 # 		 0** 		
 0 		 0 		 0,0 		 0 		
--------------------------------
[environment] {'action': {'y': 3, 'x': 1, 'type': 'pick', 'color': 'green'}, 'from': 'agent1', 'type': 'request_action'}
[1369593167] agent1: {'action': {'y': 3, 'x': 1, 'type': 'pick', 'color': 'green'}, 'status': 'OK', 'type': 'response_action'}
[1369593167] agent1: Requesting action: {'y': 3, 'x': 0, 'type': 'go_to'}
--------------------------------
[T = 1369593168]
--------------------------------
-2		 0 		 0 		 0 		
 0 		 # 		-2		 0,0*  		
 0* 		 # 		 # 		 0** 		
 0 		 0 		 0,0 		 0 		
--------------------------------
[environment] {'action': {'y': 3, 'x': 3, 'type': 'go_to'}, 'from': 'agent0', 'type': 'request_action'}
[1369593168] agent0: {'action': {'y': 3, 'x': 3, 'type': 'go_to'}, 'status': 'OK', 'type': 'response_action'}
[1369593168] agent0: Requesting action: {'y': 3, 'x': 2, 'type': 'go_to'}
--------------------------------
[T = 1369593169]
--------------------------------
-2		 0 		 0 		 0 		
 0 		 # 		-2		 0,0*  		
 0* 		 # 		 # 		 0** 		
 0 		 0 		 0 		 0,0 		
--------------------------------
[environment] {'action': {'y': 3, 'x': 0, 'type': 'go_to'}, 'from': 'agent1', 'type': 'request_action'}
[1369593169] agent1: {'action': {'y': 3, 'x': 0, 'type': 'go_to'}, 'status': 'OK', 'type': 'response_action'}
[1369593169] agent1: Requesting action: {'y': 2, 'x': 0, 'type': 'go_to'}
--------------------------------
[T = 1369593170]
--------------------------------
-2		 0 		 0 		 0,0*  		
 0 		 # 		-2		 0 		
 0* 		 # 		 # 		 0** 		
 0 		 0 		 0 		 0,0 		
--------------------------------
[environment] {'action': {'y': 3, 'x': 2, 'type': 'go_to'}, 'from': 'agent0', 'type': 'request_action'}
[1369593170] agent0: {'action': {'y': 3, 'x': 2, 'type': 'go_to'}, 'status': 'OK', 'type': 'response_action'}
[1369593170] agent0: Requesting action: {'y': 3, 'x': 2, 'type': 'pick', 'color': 'blue'}
--------------------------------
[T = 1369593171]
--------------------------------
-2		 0 		 0 		 0,0*  		
 0 		 # 		-2		 0 		
 0* 		 # 		 # 		 0**,0 		
 0 		 0 		 0 		 0 		
--------------------------------
[environment] {'action': {'y': 2, 'x': 0, 'type': 'go_to'}, 'from': 'agent1', 'type': 'request_action'}
[1369593171] agent1: {'action': {'y': 2, 'x': 0, 'type': 'go_to'}, 'status': 'OK', 'type': 'response_action'}
[1369593171] agent1: Requesting action: {'y': 1, 'x': 0, 'type': 'go_to'}
--------------------------------
[T = 1369593172]
--------------------------------
-2		 0 		 0,0*  		 0 		
 0 		 # 		-2		 0 		
 0* 		 # 		 # 		 0**,0 		
 0 		 0 		 0 		 0 		
--------------------------------
[environment] {'action': {'y': 3, 'x': 2, 'type': 'pick', 'color': 'blue'}, 'from': 'agent0', 'type': 'request_action'}
[1369593172] agent0: {'action': {'y': 3, 'x': 2, 'type': 'pick', 'color': 'blue'}, 'status': 'OK', 'type': 'response_action'}
[1369593172] agent0: Requesting action: {'y': 3, 'x': 1, 'type': 'go_to'}
--------------------------------
[T = 1369593173]
--------------------------------
-2		 0 		 0,0*  		 0 		
 0 		 # 		-2		 0 		
 0* 		 # 		 # 		 0*,0*  		
 0 		 0 		 0 		 0 		
--------------------------------
[environment] {'action': {'y': 1, 'x': 0, 'type': 'go_to'}, 'from': 'agent1', 'type': 'request_action'}
[1369593173] agent1: {'action': {'y': 1, 'x': 0, 'type': 'go_to'}, 'status': 'OK', 'type': 'response_action'}
[1369593173] agent1: Requesting action: {'y': 0, 'x': 0, 'type': 'drop', 'color': 'green'}
--------------------------------
[T = 1369593174]
--------------------------------
-2		 0,0*  		 0 		 0 		
 0 		 # 		-2		 0 		
 0* 		 # 		 # 		 0*,0*  		
 0 		 0 		 0 		 0 		
--------------------------------
[environment] {'action': {'y': 3, 'x': 1, 'type': 'go_to'}, 'from': 'agent0', 'type': 'request_action'}
[1369593174] agent0: {'action': {'y': 3, 'x': 1, 'type': 'go_to'}, 'status': 'OK', 'type': 'response_action'}
[1369593174] agent0: Requesting action: {'y': 2, 'x': 1, 'type': 'drop', 'color': 'blue'}
--------------------------------
[T = 1369593175]
--------------------------------
-2		 0,0*  		 0 		 0 		
 0 		 # 		-2		 0,0*  		
 0* 		 # 		 # 		 0* 		
 0 		 0 		 0 		 0 		
--------------------------------
[environment] {'action': {'y': 0, 'x': 0, 'points': 10, 'type': 'drop', 'color': 'green'}, 'from': 'agent1', 'type': 'request_action'}
[1369593175] agent1: {'action': {'y': 0, 'x': 0, 'points': 10, 'type': 'drop', 'color': 'green'}, 'status': 'OK', 'type': 'response_action'}
[1369593175] agent1: My new plan: {'tile': (2, 3), 'color': 'blue', 'hole': (1, 2), 'id': UUID('06f93879-2ae0-4a94-bf38-079dae7a6ad0'), 'actions': [{'y': 2, 'x': 0, 'type': 'go_to'}, {'y': 3, 'x': 0, 'type': 'go_to'}, {'y': 3, 'x': 1, 'type': 'go_to'}, {'y': 3, 'x': 2, 'type': 'go_to'}, {'y': 3, 'x': 2, 'type': 'pick', 'color': 'blue'}, {'y': 3, 'x': 1, 'type': 'go_to'}, {'y': 2, 'x': 1, 'type': 'drop', 'color': 'blue'}]}
[1369593175] agent1: Requesting action: {'y': 2, 'x': 0, 'type': 'go_to'}
--------------------------------
[T = 1369593176]
--------------------------------
-1		 0,10 		 0 		 0 		
 0 		 # 		-2		 0,0*  		
 0* 		 # 		 # 		 0* 		
 0 		 0 		 0 		 0 		
--------------------------------
[environment] {'action': {'y': 2, 'x': 1, 'points': 10, 'type': 'drop', 'color': 'blue'}, 'from': 'agent0', 'type': 'request_action'}
[1369593176] agent0: {'action': {'y': 2, 'x': 1, 'points': 10, 'type': 'drop', 'color': 'blue'}, 'status': 'OK', 'type': 'response_action'}
[1369593176] agent0: My new plan: {'tile': (2, 0), 'color': 'green', 'hole': (0, 0), 'id': UUID('0805fd46-7697-4e42-a7e7-3ea08b873840'), 'actions': [{'y': 3, 'x': 2, 'type': 'go_to'}, {'y': 3, 'x': 3, 'type': 'go_to'}, {'y': 2, 'x': 3, 'type': 'go_to'}, {'y': 1, 'x': 3, 'type': 'go_to'}, {'y': 0, 'x': 3, 'type': 'go_to'}, {'y': 0, 'x': 2, 'type': 'go_to'}, {'y': 0, 'x': 2, 'type': 'pick', 'color': 'green'}, {'y': 0, 'x': 1, 'type': 'go_to'}, {'y': 0, 'x': 0, 'type': 'drop', 'color': 'green'}]}
[1369593176] agent0: Requesting action: {'y': 3, 'x': 2, 'type': 'go_to'}
--------------------------------
[T = 1369593177]
--------------------------------
-1		 0,10 		 0 		 0 		
 0 		 # 		-1		 0,10 		
 0* 		 # 		 # 		 0* 		
 0 		 0 		 0 		 0 		
--------------------------------
[environment] {'action': {'y': 2, 'x': 0, 'type': 'go_to'}, 'from': 'agent1', 'type': 'request_action'}
[1369593177] agent1: {'action': {'y': 2, 'x': 0, 'type': 'go_to'}, 'status': 'OK', 'type': 'response_action'}
[1369593177] agent1: Requesting action: {'y': 3, 'x': 0, 'type': 'go_to'}
--------------------------------
[T = 1369593178]
--------------------------------
-1		 0 		 0,10 		 0 		
 0 		 # 		-1		 0,10 		
 0* 		 # 		 # 		 0* 		
 0 		 0 		 0 		 0 		
--------------------------------
[environment] {'action': {'y': 3, 'x': 2, 'type': 'go_to'}, 'from': 'agent0', 'type': 'request_action'}
[1369593178] agent0: {'action': {'y': 3, 'x': 2, 'type': 'go_to'}, 'status': 'OK', 'type': 'response_action'}
[1369593178] agent0: Requesting action: {'y': 3, 'x': 3, 'type': 'go_to'}
--------------------------------
[T = 1369593179]
--------------------------------
-1		 0 		 0,10 		 0 		
 0 		 # 		-1		 0 		
 0* 		 # 		 # 		 0*,10 		
 0 		 0 		 0 		 0 		
--------------------------------
[environment] {'action': {'y': 3, 'x': 0, 'type': 'go_to'}, 'from': 'agent1', 'type': 'request_action'}
[1369593179] agent1: {'action': {'y': 3, 'x': 0, 'type': 'go_to'}, 'status': 'OK', 'type': 'response_action'}
[1369593179] agent1: Requesting action: {'y': 3, 'x': 1, 'type': 'go_to'}
--------------------------------
[T = 1369593180]
--------------------------------
-1		 0 		 0 		 0,10 		
 0 		 # 		-1		 0 		
 0* 		 # 		 # 		 0*,10 		
 0 		 0 		 0 		 0 		
--------------------------------
[environment] {'action': {'y': 3, 'x': 3, 'type': 'go_to'}, 'from': 'agent0', 'type': 'request_action'}
[1369593180] agent0: {'action': {'y': 3, 'x': 3, 'type': 'go_to'}, 'status': 'OK', 'type': 'response_action'}
[1369593180] agent0: Requesting action: {'y': 2, 'x': 3, 'type': 'go_to'}
--------------------------------
[T = 1369593181]
--------------------------------
-1		 0 		 0 		 0,10 		
 0 		 # 		-1		 0 		
 0* 		 # 		 # 		 0* 		
 0 		 0 		 0 		 0,10 		
--------------------------------
[environment] {'action': {'y': 3, 'x': 1, 'type': 'go_to'}, 'from': 'agent1', 'type': 'request_action'}
[1369593181] agent1: {'action': {'y': 3, 'x': 1, 'type': 'go_to'}, 'status': 'OK', 'type': 'response_action'}
[1369593181] agent1: Requesting action: {'y': 3, 'x': 2, 'type': 'go_to'}
--------------------------------
[T = 1369593182]
--------------------------------
-1		 0 		 0 		 0 		
 0 		 # 		-1		 0,10 		
 0* 		 # 		 # 		 0* 		
 0 		 0 		 0 		 0,10 		
--------------------------------
[environment] {'action': {'y': 2, 'x': 3, 'type': 'go_to'}, 'from': 'agent0', 'type': 'request_action'}
[1369593182] agent0: {'action': {'y': 2, 'x': 3, 'type': 'go_to'}, 'status': 'OK', 'type': 'response_action'}
[1369593182] agent0: Requesting action: {'y': 1, 'x': 3, 'type': 'go_to'}
--------------------------------
[T = 1369593183]
--------------------------------
-1		 0 		 0 		 0 		
 0 		 # 		-1		 0,10 		
 0* 		 # 		 # 		 0* 		
 0 		 0 		 0,10 		 0 		
--------------------------------
[environment] {'action': {'y': 3, 'x': 2, 'type': 'go_to'}, 'from': 'agent1', 'type': 'request_action'}
[1369593183] agent1: {'action': {'y': 3, 'x': 2, 'type': 'go_to'}, 'status': 'OK', 'type': 'response_action'}
[1369593183] agent1: Requesting action: {'y': 3, 'x': 2, 'type': 'pick', 'color': 'blue'}
--------------------------------
[T = 1369593184]
--------------------------------
-1		 0 		 0 		 0 		
 0 		 # 		-1		 0 		
 0* 		 # 		 # 		 0*,10 		
 0 		 0 		 0,10 		 0 		
--------------------------------
[environment] {'action': {'y': 1, 'x': 3, 'type': 'go_to'}, 'from': 'agent0', 'type': 'request_action'}
[1369593184] agent0: {'action': {'y': 1, 'x': 3, 'type': 'go_to'}, 'status': 'OK', 'type': 'response_action'}
[1369593184] agent0: Requesting action: {'y': 0, 'x': 3, 'type': 'go_to'}
--------------------------------
[T = 1369593185]
--------------------------------
-1		 0 		 0 		 0 		
 0 		 # 		-1		 0 		
 0* 		 # 		 # 		 0*,10 		
 0 		 0,10 		 0 		 0 		
--------------------------------
[environment] {'action': {'y': 3, 'x': 2, 'type': 'pick', 'color': 'blue'}, 'from': 'agent1', 'type': 'request_action'}
[1369593185] agent1: {'action': {'y': 3, 'x': 2, 'type': 'pick', 'color': 'blue'}, 'status': 'OK', 'type': 'response_action'}
[1369593185] agent1: Requesting action: {'y': 3, 'x': 1, 'type': 'go_to'}
--------------------------------
[T = 1369593186]
--------------------------------
-1		 0 		 0 		 0 		
 0 		 # 		-1		 0 		
 0* 		 # 		 # 		 0,10*  		
 0 		 0,10 		 0 		 0 		
--------------------------------
[environment] {'action': {'y': 0, 'x': 3, 'type': 'go_to'}, 'from': 'agent0', 'type': 'request_action'}
[1369593186] agent0: {'action': {'y': 0, 'x': 3, 'type': 'go_to'}, 'status': 'OK', 'type': 'response_action'}
[1369593186] agent0: Requesting action: {'y': 0, 'x': 2, 'type': 'go_to'}
--------------------------------
[T = 1369593187]
--------------------------------
-1		 0 		 0 		 0 		
 0 		 # 		-1		 0 		
 0* 		 # 		 # 		 0,10*  		
 0,10 		 0 		 0 		 0 		
--------------------------------
[environment] {'action': {'y': 3, 'x': 1, 'type': 'go_to'}, 'from': 'agent1', 'type': 'request_action'}
[1369593187] agent1: {'action': {'y': 3, 'x': 1, 'type': 'go_to'}, 'status': 'OK', 'type': 'response_action'}
[1369593187] agent1: Requesting action: {'y': 2, 'x': 1, 'type': 'drop', 'color': 'blue'}
--------------------------------
[T = 1369593188]
--------------------------------
-1		 0 		 0 		 0 		
 0 		 # 		-1		 0,10*  		
 0* 		 # 		 # 		 0 		
 0,10 		 0 		 0 		 0 		
--------------------------------
[environment] {'action': {'y': 0, 'x': 2, 'type': 'go_to'}, 'from': 'agent0', 'type': 'request_action'}
[1369593188] agent0: {'action': {'y': 0, 'x': 2, 'type': 'go_to'}, 'status': 'OK', 'type': 'response_action'}
[1369593188] agent0: Requesting action: {'y': 0, 'x': 2, 'type': 'pick', 'color': 'green'}
--------------------------------
[T = 1369593189]
--------------------------------
-1		 0 		 0 		 0 		
 0 		 # 		-1		 0,10*  		
 0*,10 		 # 		 # 		 0 		
 0 		 0 		 0 		 0 		
--------------------------------
[environment] {'action': {'y': 2, 'x': 1, 'points': 50, 'type': 'drop', 'color': 'blue'}, 'from': 'agent1', 'type': 'request_action'}
[1369593189] agent1: {'action': {'y': 2, 'x': 1, 'points': 50, 'type': 'drop', 'color': 'blue'}, 'status': 'OK', 'type': 'response_action'}
--------------------------------
[T = 1369593190]
--------------------------------
-1		 0 		 0 		 0 		
 0 		 # 		 0		 0,10 		
 0*,60 		 # 		 # 		 0 		
 0 		 0 		 0 		 0 		
--------------------------------
[environment] {'action': {'y': 0, 'x': 2, 'type': 'pick', 'color': 'green'}, 'from': 'agent0', 'type': 'request_action'}
[1369593190] agent0: {'action': {'y': 0, 'x': 2, 'type': 'pick', 'color': 'green'}, 'status': 'OK', 'type': 'response_action'}
[1369593190] agent0: Requesting action: {'y': 0, 'x': 1, 'type': 'go_to'}

```
