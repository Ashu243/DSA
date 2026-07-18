people = [3,2,2,1]
limit = 3

def boats_save_people(people, limit):
        j = len(people)-1
        i = 0
        count = 0
        people.sort()

        while i<=j:
            sum = people[i]+people[j]
            if sum > limit:
                j-= 1
            elif sum <= limit:
                i += 1
                j-= 1
            count+= 1
        return count
print(boats_save_people(people, limit))