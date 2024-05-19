import random
import time

activities = ["SyncSwap", "Izumi Finance", "Rhino Bridge", "Owlto Daily", "Rubyscore Daily",
              "Maverick", "Element Market", "Clusters", "SyncFutures", "SuperForm"]

activities_target = int(input("Введите желаемое число активностей: "))
activities_done = []

while activities_target > 0:
    rand = random.choice(activities)
    print(rand)
    activities_target -= 1
    activities_done.append(rand)
    time.sleep(random.uniform(0.5, 1.5))

activity_count = []

for activity in activities:
    count = activities_done.count(activity)
    if count > 0:
        activity_count.append([activity, count])

print("\nКоличество выполненных активностей:")
for activity, count in activity_count:
    print(f"- {activity} сделана {count} раз(а)")