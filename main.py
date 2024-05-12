import tkinter as tk
import numpy as np

root = tk.Tk()
root.title("Рассчёт коэффициента сверхсжимаемости газа")
root.geometry("800x500")
root.resizable(False, False)
photo = tk.PhotoImage(file="favicon.png")
root.iconphoto(False, photo)
#Делаем вес каждой колонки = 1
for i in range(12):
    root.columnconfigure(index=i, weight=1)

tk.Label(root, text="Исходные данные").grid(row=0, column=0, columnspan=6, stick='ew')
tk.Label(root, text="Результат расчёта").grid(row=0, column=6, columnspan=6, stick='ew')


tk.Label(root, text="Компонент").grid(row=1, column=1, columnspan=2)
tk.Label(root, text="Мольная доля").grid(row=1, column=3, columnspan=2)

tk.Label(root, text="C1").grid(row=2, column=1, columnspan=2)
C1 = tk.Entry(root)
C1.grid(row=2, column=3, columnspan=2)

tk.Label(root, text="C2").grid(row=3, column=1, columnspan=2)
C2 = tk.Entry(root)
C2.grid(row=3, column=3, columnspan=2)

tk.Label(root, text="C3").grid(row=4, column=1, columnspan=2)
C3 = tk.Entry(root)
C3.grid(row=4, column=3, columnspan=2)

tk.Label(root, text="NC4").grid(row=5, column=1, columnspan=2)
NC4 = tk.Entry(root)
NC4.grid(row=5, column=3, columnspan=2)

tk.Label(root, text="NC5").grid(row=6, column=1, columnspan=2)
NC5 = tk.Entry(root)
NC5.grid(row=6, column=3, columnspan=2)

tk.Label(root, text="C6").grid(row=7, column=1, columnspan=2)
C6 = tk.Entry(root)
C6.grid(row=7, column=3, columnspan=2)

tk.Label(root, text="N2").grid(row=8, column=1, columnspan=2)
N2 = tk.Entry(root)
N2.grid(row=8, column=3, columnspan=2)

tk.Label(root, text="CO2").grid(row=9, column=1, columnspan=2)
C02 = tk.Entry(root)
C02.grid(row=9, column=3, columnspan=2)

tk.Label(root, text="H2S").grid(row=10, column=1, columnspan=2)
H2S = tk.Entry(root)
H2S.grid(row=10, column=3, columnspan=2)

tk.Label(root, text="Пластовое давление").grid(row=11, column=1, columnspan=2)
PP = tk.Entry(root)
PP.grid(row=11, column=3, columnspan=2)

tk.Label(root, text="Пластовая температура").grid(row=12, column=1, columnspan=2)
PT = tk.Entry(root)
PT.grid(row=12, column=3, columnspan=2)

tk.Button(root, text='Рассчитать', command=lambda:calcZ()).grid(row=13, column=2, columnspan=2, sticky='ew')

tk.Label(root, text="По СРК").grid(row=4, column=7, columnspan=2)
tk.Entry(root).grid(row=4, column=9, columnspan=2)
tk.Label(root, text="По П-Р.").grid(row=5, column=7, columnspan=2)
tk.Entry(root).grid(row=5, column=9, columnspan=2)
tk.Label(root, text="По Гуревичу-Платонову").grid(row=6, column=7, columnspan=2)
tk.Entry(root).grid(row=6, column=9, columnspan=2)

# Разделить массив на подмамассивы(сделать матрицу)
def split_array(array, num):
    new_array = [array[i:i + num] for i in range(0, len(array), num)]
    return new_array

def calcZ():
    # Исходные данные
    xj = [
            float(C1.get()), float(C2.get()), float(C3.get()),
            float(NC4.get()), float(NC5.get()), float(C6.get()),
            float(N2.get()), float(C02.get()), float(H2S.get())
        ]
    xk = xj

    R = 8.314

    Tпл = float(PT.get())

    Pпл =  float(PP.get())

    Tcj = [190.45, 305.32, 369.83, 425.12, 469.7, 512.8, 126.2, 304.19, 373.53]

    Vcj = [0.0000986, 0.0001455, 0.0002, 0.000255, 0.000313, 0.000335]

    Vck = [0.0000986, 0.0001455, 0.0002, 0.000255, 0.000313, 0.000335]

    Pcj = [45.99 * 100000, 48.72 * 100000, 42.48 * 100000, 37.96 * 100000, 33.7 * 100000, 33.3 * 100000, 34.6 * 100000,
           73.82 * 100000, 89.63 * 100000]

    w = [0.012, 0.1, 0.152, 0.2, 0.252, 0.25, 0.0377, 0.228, 0.0942]



    # ------------------------------------------------------------------------------------

    # Расчёт aj для П-Р
    aj1 = []
    for j in range(9):
        aj1.append(0.45724 * (R ** 2) * (Tcj[j] ** 2) / Pcj[j])

    # ------------------------------------------------------------------------------------
        # Расчёт aj для СРК
    aj2 = []
    for j in range(9):
        aj2.append(0.42748 * (R ** 2) * (Tcj[j] ** 2) / Pcj[j])

    # ------------------------------------------------------------------------------------

    # Расчёт bj ДЛЯ П-Р
    bj1 = []
    for j in range(9):
        bj1.append(0.0778 * (R) * (Tcj[j]) / Pcj[j])

    # ------------------------------------------------------------------------------------
        # Расчёт bj ДЛЯ СРК
    bj2 = []
    for j in range(9):
        bj2.append(0.08664 * (R) * (Tcj[j]) / Pcj[j])

    # ------------------------------------------------------------------------------------

    # Расчёт kj ДЛЯ П-Р
    kj1 = []
    for j in range(9):
        kj1.append(0.37464 + 1.54226 * w[j] - 0.26992 * (w[j] ** 2))

    # ------------------------------------------------------------------------------------
        # Расчёт kj ДЛЯ СРК
    kj2 = []
    for j in range(9):
        kj2.append(0.48 + 1.574 * w[j] - 0.176 * (w[j] ** 2))

    # ------------------------------------------------------------------------------------

    # Расчёт alpha_j ДЛЯ П-Р
    alpha_j1 = []
    for j in range(9):
        alpha_j1.append(aj1[j] * ((1 + kj1[j] * (1 - ((Tпл / Tcj[j]) ** 0.5))) ** 2))

    alpha_k1 = alpha_j1

    # ------------------------------------------------------------------------------------

    # Расчёт alpha_j ДЛЯ СРК
    alpha_j2 = []
    for j in range(9):
        alpha_j2.append(aj2[j] * ((1 + kj2[j] * (1 - ((Tпл / Tcj[j]) ** 0.5))) ** 2))

    alpha_k2 = alpha_j2

    # ------------------------------------------------------------------------------------

    # Расчёт delta для углеводородных компонентов
    delta_test = []

    delta = []

    for j in range(6):
        for k in range(6):
            delta_test.append(1 - (((2 * ((Vcj[j] ** (1 / 6)) * (Vck[k] ** (1 / 6)))) / (
                        (Vcj[j] ** (1 / 3)) + (Vck[k] ** (1 / 3)))) ** (1.2)))

    delta_test = np.array(split_array(delta_test, 6))

    delta.append(np.block([delta_test[0], np.array([0.025, 0.105, 0.07])]))
    delta.append(np.block([delta_test[1], np.array([0.01, 0.13, 0.085])]))
    delta.append(np.block([delta_test[2], np.array([0.09, 0.125, 0.08])]))
    delta.append(np.block([delta_test[3], np.array([0.095, 0.115, 0.075])]))
    delta.append(np.block([delta_test[4], np.array([0.1, 0.115, 0.07])]))
    delta.append(np.block([delta_test[5], np.array([0.11, 0.115, 0.07])]))
    delta.append(np.array([0.025, 0.01, 0.09, 0.095, 0.1, 0.11, 0, 0, 0.13]))
    delta.append(np.array([0.105, 0.13, 0.125, 0.115, 0.115, 0.115, 0, 0, 0.135]))
    delta.append(np.array([0.07, 0.085, 0.08, 0.075, 0.07, 0.07, 0.13, 0.135, 0]))
    # ------------------------------------------------------------------------------------
    

    # Расчёт alpha_jk для П-Р
    alpha_jk1 = []

    for j in range(9):
        for k in range(9):
            alpha_jk1.append(((alpha_j1[j] * alpha_k1[k]) ** 0.5) * (1 - delta[j][k]))

    alpha_jk1 = split_array(alpha_jk1, 9)

    # ------------------------------------------------------------------------------------

    # Расчёт alpha_jk для СРК
    alpha_jk2 = []

    for j in range(9):
        for k in range(9):
            alpha_jk2.append(((alpha_j2[j] * alpha_k2[k]) ** 0.5) * (1 - delta[j][k]))

    alpha_jk2 = split_array(alpha_jk2, 9)

    # ------------------------------------------------------------------------------------

    # Расчёт alpha_m и betta_m для П-Р
    xjxk = (np.outer(xj, xk))

    alpha_m1 = np.sum(np.dot(xjxk, alpha_jk1))

    betta_m1 = np.sum(np.dot(xj, bj1))

    # ------------------------------------------------------------------------------------
    # Расчёт alpha_m и betta_m для СРК
    alpha_m2 = np.sum(np.dot(xjxk, alpha_jk2))

    betta_m2 = np.sum(np.dot(xj, bj2))

    # ------------------------------------------------------------------------------------

    # Расчёт A и B для П-Р
    A1 = (alpha_m1 * Pпл) / ((R ** 2) * (Tпл ** 2))

    B1 = (betta_m1 * Pпл) / ((R) * (Tпл))

    # ------------------------------------------------------------------------------------

    # Расчёт A и B для СРК
    A2 = (alpha_m2 * Pпл) / ((R ** 2) * (Tпл ** 2))

    B2 = (betta_m2 * Pпл) / ((R) * (Tпл))

    # ------------------------------------------------------------------------------------

    # Расчёт z для П-Р
    coeff1 = [1, -(1 - B1), (A1 - 2 * B1 - 3 * (B1 ** 2)), -(A1 * B1 - ((B1 ** 2) - (B1 ** 3)))]

    z1 = max(np.roots(coeff1))

    print("z ПО П-Р = ", z1)
    # ------------------------------------------------------------------------------------

    # Расчёт z для П-Р
    coeff2 = [1, -(1), (A1 - 1 * B1 - 1 * (B1 ** 2)), -(A1 * B1)]

    z2 = max(np.roots(coeff2))

    print("z ПО СРК = ", z2)
    print(alpha_m1)

root.mainloop()
