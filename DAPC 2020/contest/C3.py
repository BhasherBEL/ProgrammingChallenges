participants, questions = map(int,input().split())

I = questions
response = []

last_time = 0
for participant in range(participants):
    current_time = int(input())
    if response and current_time < last_time:
        I -= 1
    if response and current_time == 0 and I > 0:
        I = 1e6
        break
    response.append(I)
    last_time = current_time
    
if (I == 0 and last_time == 0) or (I == 1 and last_time > 0):
    for rep in response:
        print(rep, flush=True)
else:
    print('ambiguous', flush=True)
    