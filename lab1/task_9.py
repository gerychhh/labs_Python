ip = input("Enter your ip: ")

p1 = ip.find(".")
p2 = ip.find(".", p1 + 1)
p3 = ip.find(".", p2 + 1)

if p1 == -1 or p2 == -1 or p3 == -1:
    print("Bad ip")
else:
    part1 = ip[:p1]
    part2 = ip[p1+1:p2]
    part3 = ip[p2+1:p3]
    part4 = ip[p3+1:]

    n1 = int(part1)
    n2 = int(part2)
    n3 = int(part3)
    n4 = int(part4)

    if (0 <= n1 <= 255 and
            0 <= n2 <= 255 and
            0 <= n3 <= 255 and
            0 <= n4 <= 255):
        print("Good ip")
    else:
        print("Bad ip")
