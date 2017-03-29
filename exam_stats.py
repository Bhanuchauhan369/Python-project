def exam_stats():
    grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

    #print grade element
    def print_grades(grades):
        for grade in grades:
            print(grade)
    #sum of grade elements
    def grades_sum(grades):
        total = 0
        for grade in grades:
            total += grade
        return total
    # average of grades
    def grades_average(grades):
        sum_of_grades = grades_sum(grades)
        average = sum_of_grades / float(len(grades))
        return average

    #variance of grades
    def grades_variance(grades):
        variance = 0
        for g in grades:
            variance += ((grades_average(grades) - g) ** 2)
        return variance / len(grades)
    print(grades_variance(grades))
    variance = grades_variance(grades)

    #standard deviation of grades elements
    def grades_std_deviation(variance):
        return (variance) ** 0.5
        variance = grades_variance(grades)
        print(grades_std_deviation(variance))


    # print all the function results
    print (print_grades(grades))
    print (grades_sum(grades))
    print (grades_average(grades))
    print (grades_variance(grades))
    print (grades_std_deviation(variance))
