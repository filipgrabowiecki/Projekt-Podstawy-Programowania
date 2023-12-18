import random
import math
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
import csv
from matplotlib.ticker import MultipleLocator, MaxNLocator

def ex_1():
    print("\n","ZADANIE 1","\n")
    onetohundered = []
    for i in range(1, 101):
        onetohundered.append(i)
    fizzandbuzz = []
    for i in onetohundered:
        if i % 3 == 0 and i % 5 == 0:
            fizzandbuzz.append("FizzBuzz")
        elif i % 3 == 0:
            fizzandbuzz.append("Fizz")
        elif i % 5 == 0:
            fizzandbuzz.append("Buzz")
        else:
            fizzandbuzz.append(i)
    print(fizzandbuzz)

def ex_2():
    print("\n","ZADANIE 2","\n")
    n = int(input("Podaj liczbę losowych liczb: "))
    nn = 0
    file_path = "ex2.txt"
    with open(file_path, "w") as file:
        while nn < n:
            random_number = random.randint(1, 100)
            random_number_str = str(random_number)
            file.write(random_number_str)
            file.write("\n")
            nn += 1

def ex_3():
    print("\n", "ZADANIE 3", "\n")
    statistic_numbers = []
    file_path = "ex2.txt"
    with open(file_path, "r") as file:
        lines = file.readlines()
        for line in lines:
            statistic_numbers.append(int(line))
    num_sum = sum(statistic_numbers)
    num_len = len(statistic_numbers)
    avrg = round(num_sum / num_len, 2)
    s_dev = 0
    for number in statistic_numbers:
        s_dev += ((number - avrg) ** 2)
    s_dev = s_dev / num_len
    s_dev = round(math.sqrt(s_dev), 2)
    num_max = max(statistic_numbers)
    num_min = min(statistic_numbers)
    print("\n Średnia: ", avrg, "\n Odchylenie standardowe: ", s_dev, "\n Maksymalna wartość: ", num_max,
          "\n Minimalna wartość: ", num_min,"\n")

def ex_4(n):
    print("\n", "ZADANIE 4", "\n")
    while True:
        if n < 1:
            print("Error")
        else:
            break
    first_val = 0
    second_val = 1
    fib = [first_val, second_val]
    while len(fib) < n:
        new_val = first_val + second_val
        fib.append(new_val)
        first_val = second_val
        second_val = new_val
    return (fib)

def ex_5():
    print("\n", "ZADANIE 5", "\n")
    n = int(input("Ile wyrazów ciągu wygenerować?: "))
    fib = ex_4(n)
    x_values = []
    for i in range(0, len(fib)):
        x_values.append(i)
    y_values = fib
    plt.plot(x_values, y_values)
    plt.title("Ciąg Fibbonacciego")
    plt.show()

def ex_6():
    print("\n", "ZADANIE 6", "\n")
    n = int(input("Podaj liczbę kluczy: "))
    square_dict = {x: x**2 for x in range(1, n + 1)}
    print(square_dict)
    return square_dict

def ex_7():
    print("\n", "ZADANIE 7", "\n")
    square_dict = ex_6()
    sum_of_values = sum(square_dict.values())
    print("Suma wartości słownika to: ", sum_of_values)
def ex_8():
    print("\n", "ZADANIE 8", "\n")
    for i in range(0,10):
        current_time = datetime.now()
        file_name = current_time.strftime("%Y-%m-%d_%h-%M-%S-%f")
        with open(file_name+f"{i}", "wb") as file:
            for n in range(0,100):
                file.write(bytearray(random.randint(0,100)))
def ex_9():
    print("\n", "ZADANIE 9", "\n")
    time_from_start_indx = 0
    pos_x_indx = 1
    pos_y_indx = 2
    pos_z_indx = 3
    vel_x_indx = 4
    vel_y_indx = 5
    vel_z_indx = 6
    flying_data_path = 'reference_trajectory.csv'
    with open(flying_data_path, 'r') as n_flying_data:
        csv_reader = csv.reader(n_flying_data)
        header = next(csv_reader, None)
        flying_data = zip(*csv_reader)
        for current_row_indx, row in enumerate(flying_data):
            if current_row_indx == time_from_start_indx:
                time_from_start = list(row)
            if current_row_indx == pos_x_indx:
                pos_x = list(row)
            if current_row_indx == pos_y_indx:
                pos_y = list(row)
            if current_row_indx == pos_z_indx:
                pos_z = list(row)
            if current_row_indx == vel_x_indx:
                vel_x = list(row)
            if current_row_indx == vel_y_indx:
                vel_y = list(row)
            if current_row_indx == vel_z_indx:
                vel_z = list(row)
    pos_x = [float(x) for x in pos_x]
    pos_y = [float(y) for y in pos_y]
    pos_z = [float(z) for z in pos_z]
    vel_x = [float(x) for x in vel_x]
    vel_y = [float(y) for y in vel_y]
    vel_z = [float(z) for z in vel_z]
    #part1
    fig, axs = plt.subplots(3)
    fig.suptitle("Położenie w osi x, y, z w funkcji czasu")
    axs[0].plot(time_from_start, pos_x, color = "red")
    axs[1].plot(time_from_start, pos_y, color = "green")
    axs[2].plot(time_from_start, pos_z, color = "blue")
    axs[2].set_xlabel("Czas")
    axs[0].set_ylabel("Przesunięcie w osi X")
    axs[1].set_ylabel("Przesunięcie w osi Y")
    axs[2].set_ylabel("Przesunięcie w osi Z")
    axs[0].yaxis.set_major_locator(MultipleLocator(base=70))
    axs[0].xaxis.set_major_locator(MultipleLocator(base=70))
    axs[1].xaxis.set_major_locator(MultipleLocator(base=70))
    axs[2].xaxis.set_major_locator(MultipleLocator(base=70))
    axs[0].yaxis.set_major_locator(MaxNLocator(integer=True, prune="both"))
    axs[0].xaxis.set_major_locator(MaxNLocator(integer=True, prune="both"))
    axs[1].xaxis.set_major_locator(MaxNLocator(integer=True, prune="both"))
    axs[2].xaxis.set_major_locator(MaxNLocator(integer=True, prune="both"))
    plt.show()
    #part2
    avg_pos_x = round(np.mean(pos_x), 4)
    avg_pos_y = round(np.mean(pos_y), 4)
    avg_pos_z = round(np.mean(pos_z), 4)
    print("\n Średnia pozycja w osi X to: ",avg_pos_x,"\n Średnia pozycja w osi Y to: ",avg_pos_y,"\n Średnia pozycja w osi Z to: ",avg_pos_z)
    #part3
    vel_xy = []
    vel_xyz = []
    if len(vel_x) == len(vel_y) == len(vel_z):
        vel_len = len(vel_x)
    for i in range(0,vel_len):
        vel_xy.append(math.sqrt((vel_x[i]**2)+(vel_y[i]**2)))
    for i in range(0, vel_len):
        vel_xyz.append(math.sqrt((vel_xy[i]**2)+(vel_z[i]**2)))
    file_path = "velocity.csv"
    with open(file_path, "w", newline="") as file:
        velocity_writer = csv.writer(file)
        for i in vel_xyz:
            velocity_writer.writerow([i])
def main():
    ex_1()
    ex_2()
    ex_3()
    ex_5()
    ex_6()
    ex_7()
    ex_8()
    ex_9()

if __name__ == '__main__':
    main()
