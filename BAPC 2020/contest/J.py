# Wrong answer
c, e, m = map(int, input().split())

if c == 4:
    surface = (c + e + m) ** 0.5

    if surface == int(surface):
        print(int(surface), int(surface), flush=True)
    else:
        root1 = (-(e / 2) / 2) + ((((e / 2) / 2) ** 2 - m) ** 0.5)
        root2 = (-(e / 2) / 2) - ((((e / 2) / 2) ** 2 - m) ** 0.5)

        try:
            if (root1, root2) == (int(root1), int(root2)):
                print(int(abs(root1)) + 2, int(abs(root2)) + 2, flush=True)
            else:
                print("impossible", flush=True)
        except TypeError:
            print("impossible", flush=True)
else:
    print("impossible", flush=True)