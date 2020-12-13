import math

ball = (0, 0)
angle = float(input()) # -75 < angle < 75
paddle = (10, 0)

res = (paddle[0] - ball[0]) * math.tan(math.radians(angle)) + ball[1]

print(res, flush=True)