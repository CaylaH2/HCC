#Getting input from user.
testScore = float(input("Enter test score: "))
classRank = int(input("Enter class rank: "))

#Decision logic
if testScore >= 90:
    if classRank >= 50:
        print("Accept")
    else:
        print("Reject")
else:
    if testScore >= 80:
        if classRank >= 50:
            print("Accept")
        else:
            print("Reject")
    else:
        if testScore >= 70:
            if classRank >= 75:
                print("Accept")
            else:
                print("Reject")
        else:
            print("Reject")