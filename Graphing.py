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


def graph_data(file_name, ):
    file = open(file_name + ".txt")
    print(file_name)
    x_axis = []
    y_axis = []
    lines = file.readlines()
    for i in lines:
        x_axis.append(float(i.split('\t')[0])*(1/(4*600)))
        y_axis.append(float(i.split('\t')[1]))
   
    plt.plot(x_axis,y_axis,'o')
    
    x_axis = np.array(x_axis)
    y_axis = np.array(y_axis)
    
    m_error = slope_error(x_axis, y_axis)
    #plt.errorbar(x_axis, y_axis,xerr = x_error)
    
    res= st.linregress(x_axis,y_axis)
    m= res.slope
    b= res.intercept
    R = res.rvalue**2
    
    
    print(m)
    print(m_error)
    print(b)
    
    plt.plot(x_axis, m*x_axis + b)
    
    printM = "{:.3f}".format(m)
    printB = "{:.3f}".format(b)
    printR = "{:.3f}".format(R)
    
    plt.text(0.0028, 0.13, "y = "+str(printM) + "$x$ + "+str(printB), style='normal', bbox={'facecolor': 'cyan', 'alpha': 0.5, 'pad': 10})
    plt.text(0.0028, 0.23, "R$^2$ = "+str(printR), style='normal', bbox={'facecolor': 'orange', 'alpha': 0.5, 'pad': 10})
    
    plt.grid()


def main():
    graph_data("600")
    
  
if __name__ == '__main__':
    main()

