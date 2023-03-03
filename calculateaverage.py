#CS175-02
#Peter Parrella
#Calculate Average

def main():
    score_list = get_scores()
    average = sum(score_list)/len(score_list)
    grade_list = get_grades(score_list)
    print_scores(score_list, grade_list, average, grade_list[-1])


def get_scores():
    score_list = []
    for i in range(1, 6):
        score = float(input(f"Enter score {i}: "))
        score_list.append(score)
    return score_list


def get_grades(score_list):
    grade_list = []
    for score in score_list:
        if score >= 90:
            grade_list.append("A")
        elif score >= 80:
            grade_list.append("B")
        elif score >= 70:
            grade_list.append("C")
        elif score >= 60:
            grade_list.append("D")
        else:
            grade_list.append("F")
    average_grade = get_average_grade(grade_list)
    grade_list.append(average_grade)
    return grade_list


def get_average_grade(grade_list):
    average = sum([ord(grade) for grade in grade_list])/len(grade_list)
    if average >= 88:
        return "A"
    elif average >= 76:
        return "B"
    elif average >= 64:
        return "C"
    elif average >= 52:
        return "D"
    else:
        return "F"


def print_scores(score_list, grade_list, average, average_grade):
    print("Score     Numeric Grade   Letter Grade")
    print("---------------------------------------------")
    for i in range(5):
        print(f"score {i+1}:     {score_list[i]:.1f}    {grade_list[i]}")
    print(f"Average score: {average:.1f}  {average_grade}")


def repeat():
    while True:
        repeat = input("Would you like to do another calculation ('yes' or 'no')?: ")
        if repeat == "yes":
            main()
        else:
            break

main()
repeat()
