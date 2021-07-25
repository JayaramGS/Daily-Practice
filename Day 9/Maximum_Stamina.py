No_buildings = int(input())
height = list(map(int, input().split()))
stamina = []

for building in range(No_buildings-1):
    maxi = height[building]
    xor = str(height[building])
    
    for ele in range(building+1, No_buildings):
        if height[ele] > maxi:
            maxi = height[ele]
            xor += '^' + str(height[ele])

    stamina.append(eval(xor))
stamina.append((height[-1]))
print(max(stamina))
