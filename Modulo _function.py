t = int(input())
for i in range(t):
    N = int(input())
    total_games = N//30
    remaining_time = N % 30
    print(total_games, remaining_time)