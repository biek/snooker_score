# some questions (food for thought for later on):

# write interface in choice based text adventure style
"stretched out before you, you see the lofty green fields with x reds remaining"
"or x colours, when all reds have gone"
"to the North is the baulk area, while down South a chance for a x break lies await"
"who moved things around?" <- player selection
"where did the action take place?" <- for fun and stats
"was it a long trip" <- for fun and stats
"what moved first?" <- red or colour
"did it leave?" <- yes, no
"was it supposed to?" <- yes, no

# when things go as planned:
who's turn is it?
what was potted?
answers: (nothing, red, colour or white)

what was expected to be potted?
answers: (red (beginning of break), colour or 'same')

# in case of foul:
- if what was potted was unexpected: what happened?
answers: (red instead of colour, colour instead of red, white)

- if nothing was potted: was the correct object ball hit?
answers: (yes, no)
- if no: what was hit?
answers: (nothing, red, yellow, green, brown, blue, pink, black)

- how did the turn end?
answers: (missed pot, safety, foul)

- app waits for input, and 'expects' values
so ... what happened?
[ red ][ ylw ][ grn ][ brn ]
[ blu ][ pnk ][ blc ][ wht ]

# example scenario
player 1 is at the table
white hits red, pots it

# imput from user:
player_one
player_two
break_off
active_player # = break_off at fresh table
next event
