import numpy as np #Para manejo de listas
import scipy.stats as st #Creacion de linea de tendencia
import matplotlib.pyplot as plt #Herramientas para graficar

def slope_error(x,y):

    #promedio de las listas (para calcular error)
    x_av = np.average(x)
    y_av = np.average(y) 

    #Cada miembro de la lista menos el promedio.
    xi_x = x - x_av
    yi_y = y - y_av

    #Multiplicacion de las listas creadas anteriormenta
    xy = xi_x*yi_y
    xx = xi_x**2
    yy = yi_y**2

    #Suma de las listas creadas
    Sxy = np.sum(xy)
    Sxx = np.sum(xx)
    Syy = np.sum(yy)
    
    #Beta 1 es igual al valor de la pendiente
    Beta_1 = Sxy/Sxx
    #Beta 0 es igual al valor de b (interseccion con el eje y)
    Beta_0 = x_av - Beta_1*y_av

    #sigma cuadrado. Se divide entre la cantidad de elementos de una lista de datos menos 2
    sigma_2 = (Syy-Beta_1*Sxy)/(len(x)-2)

    #Error total de la pendiente.
    V_Beta1 = sigma_2/Sxx
    
    return V_Beta1


def graph_data(file_name):
    file = open(file_name + ".txt")
    print(file_name)
    x_axis = []
    R0_axis = []
    R1_axis = []
    R2_axis = []
    R3_axis = []
    R4_axis = []
    lines = file.readlines()
    lines.pop(0)
    for i in lines:
        x_axis.append(float(i.split('\t')[0]))
        R0_axis.append(float(i.split('\t')[1]))
        R1_axis.append(float(i.split('\t')[2]))
        R2_axis.append(float(i.split('\t')[3]))
        R3_axis.append(float(i.split('\t')[4]))
        R4_axis.append(float(i.split('\t')[5]))
   
    plt.plot(x_axis,R0_axis)
    plt.plot(x_axis,R1_axis)
    plt.plot(x_axis,R2_axis)
    plt.plot(x_axis,R3_axis)
    plt.plot(x_axis,R4_axis)
    
    plt.xlabel("b / °")
    plt.ylabel("R/(1/s)")

   # plt.text(0.0028, 0.13, "y = "+str(printM) + "$x$ + "+str(printB), style='normal', bbox={'facecolor': 'cyan', 'alpha': 0.5, 'pad': 10})
   # plt.text(0.0028, 0.23, "R$^2$ = "+str(printR), style='normal', bbox={'facecolor': 'orange', 'alpha': 0.5, 'pad': 10})
    
    plt.grid()

def get_bigger_in_range(file_name, a, b):
    max_ = 0
    it = 0
    file = open(file_name + ".txt")
    
    x_axis = []
    R0_axis = []
    R1_axis = []
    R2_axis = []
    R3_axis = []
    R4_axis = []
    
    lines = file.readlines()
    lines.pop(0)
    for i in lines:
        x_axis.append(float(i.split('\t')[0]))
        R0_axis.append(float(i.split('\t')[1]))
        R1_axis.append(float(i.split('\t')[2]))
        R2_axis.append(float(i.split('\t')[3]))
        R3_axis.append(float(i.split('\t')[4]))
        R4_axis.append(float(i.split('\t')[5]))
    data_R = [x_axis, R0_axis, R1_axis, R2_axis, R3_axis, R4_axis]
         
    start = x_axis.index(a)
    finish = x_axis.index(b)
    
    for x in data_R:
        for j in range (start, finish): 
            if(x[j]>=max_):
                max_ = x[j]
                it = j
        print (str(j) + " " +str(x_axis[it])+" "+str(max_))
def main():
    graph_data("datan")
    get_bigger_in_range("datan", 6,7)
    
  
if __name__ == '__main__':
    main()

