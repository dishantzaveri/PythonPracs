def hanoi(disks,sorc,aux,dest):
    if disks==1:
        print(f"Move Disk {disks} from {sorc} to {dest}.")
        return
    hanoi(disks-1,sorc,dest,aux)
    print(f"Move Disk {disks} from {sorc} to {dest}.")
    hanoi(disks-1,aux,sorc,dest)
disks = int(input("Enter Number of Disks: "))
hanoi(disks,"A","B","C")
