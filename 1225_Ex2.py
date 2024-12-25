students = {
    "成婉財": [20, 27, 2],
    "翁雅婷": [73, 77, 84],
    "黃雅姍": [12, 22, 29],
    "黃志輝": [61, 58, 99],
    "郭瑞珊": [75, 76, 85],
    "陳錦華": [54, 63, 51],
    "李豐彬": [73, 55, 51],
    "梁佳正": [80, 97, 53],
}

sorted_students = sorted(students.items(), key=lambda x: sum(x[1]), reverse=True)

print("Sorted Students by Total Scores:")
for name, scores in sorted_students:
    print(f"{name}: Total = {sum(scores)}")
