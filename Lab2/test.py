def Greedy_hamsters():

    with open('hamstr.txt') as hamster:
        lines = hamster.readlines()

    my_food = int(lines[0])
    print("My amount of food:")
    print(my_food)

    hamster_amount = int(lines[1])
    print("Amount of hamsters in zoo market:")
    print(hamster_amount)

    hamster_ratio = []
    for element in lines[2:]:
        hamster_ratio.append(list(map(int, element.split())))

    print("Daily rate and greed of hamsters:")
    print(hamster_ratio)

    result = food_count(hamster_ratio)

    while result > my_food:
        greed_hamsters = hamster_ratio[1:]
        min_result = food_count(greed_hamsters)
        min_index = 0

        for a in range(1, hamster_amount):
            if a != hamster_amount - 1:
                greed_hamsters = hamster_ratio[:a] + hamster_ratio[a + 1:]
            else:
                greed_hamsters = hamster_ratio[:a]

            second_result = food_count(greed_hamsters)

            if min_result > second_result:
                min_result = second_result
                min_index = a

        del hamster_ratio[min_index]
        hamster_amount -= 1
        result = min_result

    print("Amount of hamsters that you can feed:")
    print(hamster_amount)


def food_count(hamsters):
    summ = 0
    hamster_amount = hamsters.__len__()
    for b in hamsters:
        hm = b[0] + b[1] * (hamster_amount - 1)
        summ = summ + hm
    return summ

Greedy_hamsters()