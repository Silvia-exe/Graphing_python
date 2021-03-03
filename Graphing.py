import numpy as np #Para manejo de listas
import scipy.stats as st #Creacion de linea de tendencia
import matplotlib.pyplot as plt #Herramientas para graficar

K_calc = 0.78*(10**-3)
K_calib = 0.67*(10**-3)
r = 0.04
I = np.array([1.7447,1.742,1.728,1.709,1.6444,1.64,1.5764,1.5702,1.4832,1.4585,1.432]) #Lista que guarda los valores de s
U = np.array([300.61,290.88,280.51,270.14,260.71,250.41,240.2,230.08,220.1,210.31,200.51]) #Lista que guarda los valores de \delta t

I_plot = I**2
U_plot = 2*U/((r**2)*(K_calib**2))
#promedio de las listas (para calcular error)
I_plot_av = np.average(I_plot)
U_plot_av = np.average(U_plot) 

#Cada miembro de la lista menos el promedio. x es el tiempo, y la distancia recorrida (2s)
xi_x = I_plot - I_plot_av
yi_y = U_plot - U_plot_av

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
Beta_0 = I_plot_av - Beta_1*U_plot_av

#sigma cuadrado. Se divide entre la cantidad de elementos de una lista de datos menos 2
sigma_2 = (Syy-Beta_1*Sxy)/(len(I)-2)

#Error total de la pendiente.
V_Beta1 = sigma_2/Sxx

#Graficar tiempo contra distancia recorrida (2s)
plt.plot(I_plot,U_plot,'o')

#Linea de tendencia. Nos regresa valores de la pendiente, interseccion y R
res= st.linregress(I_plot,U_plot)
m= res.slope
b= res.intercept
R = res.rvalue**2
#Graficar linea de tendencia
plt.plot(I_plot,m*I_plot+b)

#Valores usados para generar leyendas. Se redondean a 2 decimales por estetica.
printM = "{:.2f}".format(m/(10**11))
printB = "{:.2f}".format(b/(10**11))
printR = "{:.2f}".format(R)

#Edicion de la grafica. Se agregan leyendas, cuadricula, etiquetas de ejes y titulo
plt.text(2.6,6.4*10**11, "y = "+str(printM)+"x 10$^{11}x$ + "+str(printB) + "x 10$^{11}$", style='normal', bbox={'facecolor': 'cyan', 'alpha': 0.5, 'pad': 10})
plt.text(2.6,5.8*10**11, "R$^2$ = "+str(printR), style='normal', bbox={'facecolor': 'orange', 'alpha': 0.5, 'pad': 10})
plt.grid()
plt.xlabel("I$^2$")
plt.ylabel("2U/r$^2$k$^2$")
plt.title("Corriente vs Relacion de energia potencial")

#Se imprime la pendiente sin redondear para agregar en el reporte
print(m)

