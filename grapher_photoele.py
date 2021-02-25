
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st

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
    y_axis = []
    lines = file.readlines()
    for i in lines:
        y_axis.append(float(i.split('\t')[0]))
        x_axis.append(float(i.split('\t')[1]))
   
    e = 1.6*10**-19
    for i in range(len(x_axis)):
        y_axis[i] = y_axis[i]* e
        x_axis[i] = x_axis[i]*10**12
    plt.plot(x_axis,y_axis,'o')
    
    x_axis = np.array(x_axis)
    y_axis = np.array(y_axis)
    
    m_error = slope_error(x_axis, y_axis)
    x_error = len(x_axis)*[(0.02*10**15)]
    x_error = np.array(x_error)
    plt.errorbar(x_axis, y_axis,xerr = x_error)
    
    res= st.linregress(x_axis,y_axis)
    m= res.slope
    b= res.intercept
    R = res.rvalue**2
    
    plt.title(file_name)
    plt.xlabel("f [Hz]")
    plt.ylabel ("V x e [Nm]")
    plt.plot(x_axis,m*x_axis+b)
    
    print(m)
    print(m_error)
    print(b)
    printM = "{:.3f}".format(m*10**34)
    printB = "{:.3f}".format(b*10**19)
    printR = "{:.3f}".format(R)
    
    plt.text(6.5*10**14, 1*e, "y = "+str(printM) +"x$10^{-34}$ "+"$x$ + "+str(printB)+"x$10^{-19}$", style='normal', bbox={'facecolor': 'cyan', 'alpha': 0.5, 'pad': 10})
    plt.text(6.5*10**14, 0.8*e, "R$^2$ = "+str(printR), style='normal', bbox={'facecolor': 'orange', 'alpha': 0.5, 'pad': 10})
    
    plt.grid()


def main():
    graph_data("Scnd_order")
    
  
if __name__ == '__main__':
    main()