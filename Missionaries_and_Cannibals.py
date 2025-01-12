boat_side = "Right"
machineries_on_right = 3
cannibals_on_right = 3
machineries_on_left = 0
cannibals_on_left = 0

print("M = 0  C = 0 |-------B| M = 3 C = 3")
print("")
while True:
    machineries = int(input("Enter the number of machineries or enter 10 to quit: "))
    if machineries == 10:
        print("You Quit. Game over......")
        break
    cannibals = int(input("Enter the Number of Cannibals: "))

    if boat_side == "Right":
        machineries_on_right = machineries_on_right - machineries
        cannibals_on_right = cannibals_on_right - cannibals

        machineries_on_left += machineries
        cannibals_on_left += cannibals

        print(f"M = {machineries_on_left} C = {cannibals_on_left} |B-------| M = {machineries_on_right} C = {cannibals_on_right} ")
        temp = input("Press (M/C) to take back to Right Side: ")
        if temp == "M" or temp == "m":
            machineries_on_left -= 1
            machineries_on_right += 1
            print(f"M = {machineries_on_left} C = {cannibals_on_left} |B-------| M = {machineries_on_right} C = {cannibals_on_right} ")

        elif temp == "C" or temp == "c":
            cannibals_on_left -= 1
            cannibals_on_right += 1
            print(f"M = {machineries_on_left} C = {cannibals_on_left} |B-------| M = {machineries_on_right} C = {cannibals_on_right} ")

        boat_side = "Left"

    else:
        machineries_on_left = machineries_on_left - machineries
        cannibals_on_left = cannibals_on_left - cannibals

        machineries_on_left += machineries
        cannibals_on_left += cannibals

        print(f"M = {machineries_on_left} C = {cannibals_on_left} |-------B| M = {machineries_on_right} C  = {cannibals_on_right}")
        print("")
        temp = input("Press (M/C) to take back to Left Side: ")
        if temp == "M" or temp == "m":
            machineries_on_right -= 1
            machineries_on_left += 1
            print(f"M = {machineries_on_left} C = {cannibals_on_left} |B-------| M = {machineries_on_right} C = {cannibals_on_right} ")

        elif temp == "C" or temp == "c":
            cannibals_on_right -= 1
            cannibals_on_left += 1
            print(f"M = {machineries_on_left} C = {cannibals_on_left} |B-------| M = {machineries_on_right} C = {cannibals_on_right} ")

        boat_side = "Right"

if (machineries_on_left >= 2) or (machineries_on_right >= 2):
    print("You Loose.....")

if machineries_on_left == 3 and cannibals_on_left == 3:
    print("You Win")
