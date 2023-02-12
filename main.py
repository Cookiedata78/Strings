# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
#Part 1
scorer_0 = "Gullit"
scorer_1 = "van Basten"
time_1 = 32
time_2 = 54
first_goal = f"{scorer_0} had scored in {time_1}nd minute\n"
second_goal = f"{scorer_1} had scored in {time_2}th minute\n"
scorers = first_goal + second_goal
result = scorers
print(result)
#Part 2 
player = "Marcel van Basten"

first_name = player[0:player.find(" ")]

last_name_len = len(player[player.find(" ")+1:])

name_short = first_name + " van Basten"

chant = first_name + "!"*last_name_len

good_chant = chant[-1] != ""

print(chant)




