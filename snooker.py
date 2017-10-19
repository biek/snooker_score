# 
# snooker score app
# count score
# keep performance data

from sys import argv

player_one = raw_input("Who is player one? ")
player_two = raw_input("Who is player two? ")
active_player = raw_input("Who will begin? ")

(player_one, player_two, active_player) = argv
prompt = '> '

# fresh_table
reds_start = 15
reds_potted = 0
reds_remaining = reds_start - reds_potted

# available break on table
max_break = reds_remaining * 8 + 27 # all_colours from file later on

# active_player = raw_input("Who goes first? Player one? Or player two? ")

print "Okay", active_player, "at this point the maximum break, with", 
reds_remaining, "reds left on the table, is", max_break,"."

table_event = raw_input("So ... what got potted? ")
