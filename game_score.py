#1. input collection
player_name = input("enter player's name:")
games_played=int(input("enter number of games played:"))
total_score=int(input("enter the total score achived:"))
average_score=total_score/games_played
#2. output
print("\nplayer stats:")
print("player:",player_name)
print("games played:",games_played)
print("total score:",total_score)
print("average score:",average_score)
