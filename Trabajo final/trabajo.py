import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_excel('https://raw.githubusercontent.com/BiancaDiFranco/M-todosOP/main/Trabajo%20final/Rosario%20F.xlsx', engine='openpyxl')

#Total de personas que intencionan votar a cada partido político
LLA = (df["INT DE VOTO X ESPACIO"]=="LIBERTARIOS")
LLA_total = df[LLA].shape[0] 

FdT = (df["INT DE VOTO X ESPACIO"]=="FdT")
FdT_total = df[FdT].shape[0]

JxC = (df["INT DE VOTO X ESPACIO"]=="JxC")
JxC_total = df[JxC].shape[0]

FIT =  (df["INT DE VOTO X ESPACIO"]=="FIT")
FIT_total = df[FIT].shape[0]

PNK =  (df["INT DE VOTO X ESPACIO"]=="PNK")
PNK_total = df[PNK].shape[0]

Otros = (df["INT DE VOTO X ESPACIO"]=="OTROS")
Otros_total = df[Otros].shape[0]

Ninguno_NoSabe = (df["INT DE VOTO X ESPACIO"]=="NINGUNO/NOSABE")
Ninguno_NoSabe_total = df[Ninguno_NoSabe].shape[0]


print(f"Total que piensa votar a La Libertad Avanza: {LLA_total} /n" 
      f"Total que piensa votar al Frente de Todos {FdT_total} /n"
      f"Total que piensa votar a Juntos por el Cambio {JxC_total} /n"
      f"Total que piensa votar al Frente de Izquierda {FIT_total} /n"
      f"Total que piensa votar peronismo no kircherista {PNK_total} /n"
      f"Total que piensa votar a Otros {Otros_total} /n"
      f"Total que no votará a ninguno o todavia no se ha decidido {Ninguno_NoSabe_total}")

#Total de personas que intencionan votar a La Libertad Avanza por rango de edad
filtro1_LLA = (df["INT DE VOTO X ESPACIO"] == "LIBERTARIOS") & (df["EDAD"] == "16 a 25")
LLA_r1 = df[filtro1_LLA].shape[0] 

filtro2_LLA= (df["INT DE VOTO X ESPACIO"] == "LIBERTARIOS") & (df["EDAD"] == "26 a 35")
LLA_r2 = df[filtro2_LLA].shape[0] 

filtro3_LLA= (df["INT DE VOTO X ESPACIO"] == "LIBERTARIOS") & (df["EDAD"] == "36 a 45")
LLA_r3 = df[filtro3_LLA].shape[0]

filtro4_LLA= (df["INT DE VOTO X ESPACIO"] == "LIBERTARIOS") & (df["EDAD"] == "46 a 55")
LLA_r4 = df[filtro4_LLA].shape[0]

filtro5_LLA= (df["INT DE VOTO X ESPACIO"] == "LIBERTARIOS") & (df["EDAD"] == "56 y mas")
LLA_r5 = df[filtro5_LLA].shape[0]

print(f"{LLA_r1} personas de entre 16 y 25 años planean votar a La Libertad Avanza /n"
       f"{LLA_r2} personas de entre 26 a 35 años planean votar a La Libertad Avanza /n"
       f"{LLA_r3} personas de entre 36 a 45 años planean votar a La Libertad Avanza /n"
       f"{LLA_r4} personas de entre 46 a 55 años planean votar a La Libertad Avanza /n"
       f"{LLA_r5} personas de entre 56 y más años planean votar a La Libertad Avanza /n")


#Total de personas que intencionan votar al Frente de Todos por rango de edad
filtro1_FdT = (df["INT DE VOTO X ESPACIO"] == "FdT") & (df["EDAD"] == "16 a 25")
FdT_r1 = df[filtro1_FdT].shape[0] 

filtro2_FdT= (df["INT DE VOTO X ESPACIO"] == "FdT") & (df["EDAD"] == "26 a 35")
FdT_r2 = df[filtro2_FdT].shape[0] 

filtro3_FdT= (df["INT DE VOTO X ESPACIO"] == "FdT") & (df["EDAD"] == "36 a 45")
FdT_r3 = df[filtro3_FdT].shape[0]

filtro4_FdT= (df["INT DE VOTO X ESPACIO"] == "FdT") & (df["EDAD"] == "46 a 55")
FdT_r4 = df[filtro4_FdT].shape[0]

filtro5_FdT= (df["INT DE VOTO X ESPACIO"] == "FdT") & (df["EDAD"] == "56 y mas")
FdT_r5 = df[filtro5_FdT].shape[0]

print(f"{FdT_r1} personas de entre 16 y 25 años planean votar al Frente de Todos /n"
       f"{FdT_r2} personas de entre 26 a 35 años planean votar al Frente de Todos/n"
       f"{FdT_r3} personas de entre 36 a 45 años planean votar al Frente de Todos /n"
       f"{FdT_r4} personas de entre 46 a 55 años planean votar al Frente de Todos /n"
       f"{FdT_r5} personas de entre 56 y más años planean votar al Frente de Todos /n")

#Total de personas que intencionan votar a Juntos por el Cambio por rango de edad
filtro1_JxC = (df["INT DE VOTO X ESPACIO"] == "JxC") & (df["EDAD"] == "16 a 25")
JxC_r1 = df[filtro1_JxC].shape[0] 

filtro2_JxC = (df["INT DE VOTO X ESPACIO"] == "JxC") & (df["EDAD"] == "26 a 35")
JxC_r2 = df[filtro2_JxC].shape[0] 

filtro3_JxC = (df["INT DE VOTO X ESPACIO"] == "JxC") & (df["EDAD"] == "36 a 45")
JxC_r3 = df[filtro3_JxC].shape[0]

filtro4_JxC= (df["INT DE VOTO X ESPACIO"] == "JxC") & (df["EDAD"] == "46 a 55")
JxC_r4 = df[filtro4_JxC].shape[0]

filtro5_JxC= (df["INT DE VOTO X ESPACIO"] == "JxC") & (df["EDAD"] == "56 y mas")
JxC_r5 = df[filtro5_JxC].shape[0]

print(f"{JxC_r1} personas de entre 16 y 25 años planean votar a Juntos por el Cambio /n"
       f"{JxC_r2} personas de entre 26 a 35 años planean votara Juntos por el Cambio /n"
       f"{JxC_r3} personas de entre 36 a 45 años planean votar a Juntos por el Cambio /n"
       f"{JxC_r4} personas de entre 46 a 55 años planean votar a Juntos por el Cambio /n"
       f"{JxC_r5} personas de entre 56 y más años planean votar a Juntos por el Cambio /n")

#Total de personas que intencionan votar al Frente de Izquierda por rango de edad
filtro1_FIT = (df["INT DE VOTO X ESPACIO"] == "FIT") & (df["EDAD"] == "16 a 25")
FIT_r1 = df[filtro1_FIT].shape[0] 

filtro2_FIT = (df["INT DE VOTO X ESPACIO"] == "FIT") & (df["EDAD"] == "26 a 35")
FIT_r2 = df[filtro2_FIT].shape[0] 

filtro3_FIT = (df["INT DE VOTO X ESPACIO"] == "FIT") & (df["EDAD"] == "36 a 45")
FIT_r3 = df[filtro3_FIT].shape[0]

filtro4_FIT= (df["INT DE VOTO X ESPACIO"] == "FIT") & (df["EDAD"] == "46 a 55")
FIT_r4 = df[filtro4_FIT].shape[0]

filtro5_FIT= (df["INT DE VOTO X ESPACIO"] == "FIT") & (df["EDAD"] == "56 y mas")
FIT_r5 = df[filtro5_FIT].shape[0]

print(f"{FIT_r1} personas de entre 16 y 25 años planean votar al Frente de Izquierda /n"
       f"{FIT_r2} personas de entre 26 a 35 años planean votar al Frente de Izquierda /n"
       f"{FIT_r3} personas de entre 36 a 45 años planean votar al Frente de Izquierda /n"
       f"{FIT_r4} personas de entre 46 a 55 años planean votar al Frente de Izquierda /n"
       f"{FIT_r5} personas de entre 56 y más años planean votar al Frente de Izquierda /n")

#Total de personas que intencionan votar al Peronismo No Kircherista por rango de edad
filtro1_PNK = (df["INT DE VOTO X ESPACIO"] == "PNK") & (df["EDAD"] == "16 a 25")
PNK_r1 = df[filtro1_PNK].shape[0] 

filtro2_PNK = (df["INT DE VOTO X ESPACIO"] == "PNK") & (df["EDAD"] == "26 a 35")
PNK_r2 = df[filtro2_PNK].shape[0] 

filtro3_PNK = (df["INT DE VOTO X ESPACIO"] == "PNK") & (df["EDAD"] == "36 a 45")
PNK_r3 = df[filtro3_PNK].shape[0]

filtro4_PNK= (df["INT DE VOTO X ESPACIO"] == "PNK") & (df["EDAD"] == "46 a 55")
PNK_r4 = df[filtro4_PNK].shape[0]

filtro5_PNK= (df["INT DE VOTO X ESPACIO"] == "PNK") & (df["EDAD"] == "56 y mas")
PNK_r5 = df[filtro5_PNK].shape[0]

print(f"{PNK_r1} personas de entre 16 y 25 años planean votar al Peronismo No Kircherista /n"
       f"{PNK_r2} personas de entre 26 a 35 años planean votar al Peronismo No Kircherista /n"
       f"{PNK_r3} personas de entre 36 a 45 años planean votar al Peronismo No Kircherista /n"
       f"{PNK_r4} personas de entre 46 a 55 años planean votar al Peronismo No Kircherista /n"
       f"{PNK_r5} personas de entre 56 y más años planean votar al Peronismo No Kircherista /n")

#Total de personas que intencionan votar a Otros por rango de edad
filtro1_Otros = (df["INT DE VOTO X ESPACIO"] == "OTROS") & (df["EDAD"] == "16 a 25")
Otros_r1 = df[filtro1_Otros].shape[0] 

filtro2_Otros = (df["INT DE VOTO X ESPACIO"] == "OTROS") & (df["EDAD"] == "26 a 35")
Otros_r2 = df[filtro2_Otros].shape[0] 

filtro3_Otros = (df["INT DE VOTO X ESPACIO"] == "OTROS") & (df["EDAD"] == "36 a 45")
Otros_r3 = df[filtro3_Otros].shape[0]

filtro4_Otros= (df["INT DE VOTO X ESPACIO"] == "OTROS") & (df["EDAD"] == "46 a 55")
Otros_r4 = df[filtro4_Otros].shape[0]

filtro5_Otros= (df["INT DE VOTO X ESPACIO"] == "OTROS") & (df["EDAD"] == "56 y mas")
Otros_r5 = df[filtro5_Otros].shape[0]

print(f"{Otros_r1} personas de entre 16 y 25 años planean votar a Otros /n"
       f"{Otros_r2} personas de entre 26 a 35 años planean votar a Otros /n"
       f"{Otros_r3} personas de entre 36 a 45 años planean votar a Otros /n"
       f"{Otros_r4} personas de entre 46 a 55 años planean votar a Otros /n"
       f"{Otros_r5} personas de entre 56 y más años planean votar a Otros /n")

#Total de personas que intencionan no votar a ninguno de los partidos polítiicos mencionados o aún saben a cuál votarán
filtro1_Ninguno_NoSabe = (df["INT DE VOTO X ESPACIO"] == "NINGUNO/NOSABE") & (df["EDAD"] == "16 a 25")
Ninguno_NoSabe_r1 = df[filtro1_Ninguno_NoSabe].shape[0] 

filtro2_Ninguno_NoSabe = (df["INT DE VOTO X ESPACIO"] == "NINGUNO/NOSABE") & (df["EDAD"] == "26 a 35")
Ninguno_NoSabe_r2 = df[filtro2_Ninguno_NoSabe].shape[0] 

filtro3_Ninguno_NoSabe = (df["INT DE VOTO X ESPACIO"] == "NINGUNO/NOSABE") & (df["EDAD"] == "36 a 45")
Ninguno_NoSabe_r3 = df[filtro3_Ninguno_NoSabe].shape[0]

filtro4_Ninguno_NoSabe= (df["INT DE VOTO X ESPACIO"] == "NINGUNO/NOSABE") & (df["EDAD"] == "46 a 55")
Ninguno_NoSabe_r4 = df[filtro4_Ninguno_NoSabe].shape[0]

filtro5_Ninguno_NoSabe= (df["INT DE VOTO X ESPACIO"] == "NINGUNO/NOSABE") & (df["EDAD"] == "56 y mas")
Ninguno_NoSabe_r5 = df[filtro5_Ninguno_NoSabe].shape[0]

print(f"{Ninguno_NoSabe_r1} personas de entre 16 y 25 años planean no votar a ninguno de los partidos polítiicos mencionados o aún saben a cuál votarán /n"
       f"{Ninguno_NoSabe_r2} personas de entre 26 a 35 años planean no votar a ninguno de los partidos polítiicos mencionados o aún saben a cuál votarán /n"
       f"{Ninguno_NoSabe_r3} personas de entre 36 a 45 años planean no votar a ninguno de los partidos polítiicos mencionados o aún saben a cuál votarán /n"
       f"{Ninguno_NoSabe_r4} personas de entre 46 a 55 años planean no votar a ninguno de los partidos polítiicos mencionados o aún saben a cuál votarán /n"
       f"{Ninguno_NoSabe_r5} personas de entre 56 y más años planean no votar a ninguno de los partidos polítiicos mencionados o aún saben a cuál votarán /n")

#Intención de voto de La Libertad Avanza por género

filtroV_LLA = (df["INT DE VOTO X ESPACIO"] == "LIBERTARIOS") & (df["GENERO"] == "Masculino")
LLA_varones = df[filtroV_LLA].shape[0] 

filtroM_LLA = (df["INT DE VOTO X ESPACIO"] == "LIBERTARIOS") & (df["GENERO"] == "Femenino")
LLA_mujeres = df[filtroM_LLA].shape[0] 

filtroO_LLA = (df["INT DE VOTO X ESPACIO"] == "LIBERTARIOS") & (df["GENERO"] == "Otro")
LLA_otros = df[filtroO_LLA].shape[0] 

print (f"{LLA_varones} hombres piensan votar a La Libertad Avanza /n"
       f"{LLA_mujeres} mujeres piensan votar a La Libertad Avanza /n"
       f"{LLA_otros} otros piensan votar a La Libertad Avanza /n")


#Intención de voto del Frente de Todos por género
filtroV_FdT = (df["INT DE VOTO X ESPACIO"] == "FdT") & (df["GENERO"] == "Masculino")
FdT_varones = df[filtroV_FdT].shape[0] 

filtroM_FdT = (df["INT DE VOTO X ESPACIO"] == "FdT") & (df["GENERO"] == "Femenino")
FdT_mujeres = df[filtroM_FdT].shape[0] 

filtroO_FdT = (df["INT DE VOTO X ESPACIO"] == "FdT") & (df["GENERO"] == "Otro")
FdT_otros = df[filtroO_FdT].shape[0] 

print (f"{FdT_varones} hombres piensan votar al Frente de Todos /n"
       f"{FdT_mujeres} mujeres piensan votar al Frente de Todos/n"
       f"{FdT_otros} otros piensan votar al Frente de Todos /n")

#Intención de voto de Juntos por el Cambio por género
filtroV_JxC = (df["INT DE VOTO X ESPACIO"] == "JxC") & (df["GENERO"] == "Masculino")
JxC_varones = df[filtroV_JxC].shape[0] 

filtroM_JxC = (df["INT DE VOTO X ESPACIO"] == "JxC") & (df["GENERO"] == "Femenino")
JxC_mujeres = df[filtroM_JxC].shape[0] 

filtroO_JxC = (df["INT DE VOTO X ESPACIO"] == "JxC") & (df["GENERO"] == "Otro")
JxC_otros = df[filtroO_JxC].shape[0] 

print (f"{JxC_varones} hombres piensan votar a Juntos por el Cambio /n"
       f"{JxC_mujeres} mujeres piensan votar a Juntos por el Cambio /n"
       f"{JxC_otros} otros piensan votar a Juntos por el Cambio /n")

#Intención de voto del Frente de Izquierda por género
filtroV_FIT = (df["INT DE VOTO X ESPACIO"] == "FIT") & (df["GENERO"] == "Masculino")
FIT_varones = df[filtroV_FIT].shape[0] 

filtroM_FIT = (df["INT DE VOTO X ESPACIO"] == "FIT") & (df["GENERO"] == "Femenino")
FIT_mujeres = df[filtroM_FIT].shape[0] 

filtroO_FIT = (df["INT DE VOTO X ESPACIO"] == "FIT") & (df["GENERO"] == "Otro")
FIT_otros = df[filtroO_FIT].shape[0] 

print (f"{FIT_varones} hombres piensan votar al Frente de Izquierda /n"
       f"{FIT_mujeres} mujeres piensan votar al Frente de Izquierda /n"
       f"{FIT_otros} otros piensan votar al Frente de Izquierda /n")

#Intención de voto del Peronismo No Kirchnerista por género
filtroV_PNK = (df["INT DE VOTO X ESPACIO"] == "PNK") & (df["GENERO"] == "Masculino")
PNK_varones = df[filtroV_PNK].shape[0] 

filtroM_PNK = (df["INT DE VOTO X ESPACIO"] == "PNK") & (df["GENERO"] == "Femenino")
PNK_mujeres = df[filtroM_PNK].shape[0] 

filtroO_PNK = (df["INT DE VOTO X ESPACIO"] == "PNK") & (df["GENERO"] == "Otro")
PNK_otros = df[filtroO_PNK].shape[0] 

print (f"{PNK_varones} hombres piensan votar al Peronismo No Kirchnerista /n"
       f"{PNK_mujeres} mujeres piensan votar al Peronismo No Kirchnerista /n"
       f"{PNK_otros} otros piensan votar al Peronismo No Kirchnerista /n")

#Intención de voto de Otros por género
filtroV_Otros = (df["INT DE VOTO X ESPACIO"] == "OTROS") & (df["GENERO"] == "Masculino")
Otros_varones = df[filtroV_Otros].shape[0] 

filtroM_Otros = (df["INT DE VOTO X ESPACIO"] == "OTROS") & (df["GENERO"] == "Femenino")
Otros_mujeres = df[filtroM_Otros].shape[0] 

filtroO_Otros = (df["INT DE VOTO X ESPACIO"] == "OTROS") & (df["GENERO"] == "Otro")
Otros_otros = df[filtroO_Otros].shape[0] 

print(f"{Otros_varones} hombres piensan votar a Otros /n"
       f"{Otros_mujeres} mujeres piensan votar a Otros /n"
       f"{Otros_otros} otros piensan votar a Otros /n")

#Intención de no votar a ninguno de ellos por género
filtroV_Ninguno_NoSabe = (df["INT DE VOTO X ESPACIO"] == "NINGUNO/NOSABE") & (df["GENERO"] == "Masculino")
Ninguno_NoSabe_varones = df[filtroV_Ninguno_NoSabe].shape[0] 

filtroM_Ninguno_NoSabe = (df["INT DE VOTO X ESPACIO"] == "NINGUNO/NOSABE") & (df["GENERO"] == "Femenino")
Ninguno_NoSabe_mujeres = df[filtroM_Ninguno_NoSabe].shape[0] 

filtroO_Ninguno_NoSabe = (df["INT DE VOTO X ESPACIO"] == "NINGUNO/NOSABE") & (df["GENERO"] == "Otro")
Ninguno_NoSabe_otros = df[filtroO_Ninguno_NoSabe].shape[0] 

print(f"{Ninguno_NoSabe_varones} hombres piensan no votar a ninguno de ellos /n"
       f"{Ninguno_NoSabe_mujeres} mujeres piensan no votar a ninguno de ellos /n"
       f"{Ninguno_NoSabe_otros} otros piensan no votar a ninguno de ellos /n")


data = pd.DataFrame({'España' : [826, 943, 942, 901],
                     'Colombia': [668, 781, 791, 813],
                     'México': [488, 553, 563, 537]},
                    index=('Lunes', 'Martes', 'Miercoles', 'Jueves'))
n = len(data.index)
x = np.arange(n)
width = 0.25


#Gráfico de barras
data= pd.DataFrame({"Masculino": [LLA_varones, FdT_varones,JxC_varones,FIT_varones,PNK_varones,Otros_varones, Ninguno_NoSabe_varones],
                     "Femenino" : [LLA_mujeres,FdT_mujeres,JxC_mujeres,FIT_mujeres,PNK_mujeres,Otros_mujeres, Ninguno_NoSabe_mujeres],
                     "Otros": [LLA_otros,FdT_otros,JxC_otros,FIT_otros, PNK_otros,Otros_otros, Ninguno_NoSabe_otros]},
                     index= ("LLA","FdT","JxC","FIT","PNK", "Otros","Ninguno/NS"))
total = data.sum(axis=1)
plt.bar(data.index, data.Masculino + data.Femenino + data.Otros, label= "Masculino")
plt.bar(data.index, data.Femenino + data.Otros, label= "Femenino")
plt.bar(data.index, data.Otros, label= "Otros")
plt.legend(loc='best')
plt.title("Intención de voto por partido político y género")
plt.show()

#Gráfico de torta, rango etario votantes de LLA
votantesLLA = [LLA_r1,LLA_r2,LLA_r3,LLA_r4,LLA_r5]
categorias = ["Entre 16 y 25", "Entre 26 a 35 años", "Entre 36 a 45 años", "Entre 46 a 55 años", "Entre 56 y más años" ]
plt.pie (votantesLLA, labels=categorias,autopct="%0.1f %%") # Este argumento se usa para mostrar el porcentaje de cada sección. El formato "%0.1f %%" indica que se debe mostrar el porcentaje con un solo decimal
plt.axis("equal")
plt.title("Composición etaria de los votantes de La Libertad Avanza")
plt.show()

#Gráfico de torta, rango etario votantes del Fdt
votantesFdT = [FdT_r1,FdT_r2,FdT_r3,FdT_r4,FdT_r5]
categorias = ["Entre 16 y 25", "Entre 26 a 35 años", "Entre 36 a 45 años", "Entre 46 a 55 años", "Entre 56 y más años" ]
plt.pie (votantesFdT, labels=categorias,autopct="%0.1f %%")
plt.axis("equal")
plt.title("Composición etaria de los votantes del Frente de Todos")
plt.show()

#Gráfico de torta, rango etario votantes de JxC
votantesJxC = [JxC_r1,JxC_r2,JxC_r3,JxC_r4,JxC_r5]
categorias = ["Entre 16 y 25", "Entre 26 a 35 años", "Entre 36 a 45 años", "Entre 46 a 55 años", "Entre 56 y más años" ]
plt.pie (votantesJxC, labels=categorias,autopct="%0.1f %%")
plt.axis("equal")
plt.title("Composición etaria de los votantes de Juntos por el Cambio")
plt.show()

#Gráfico de torta, rango etario votantes del FIT
votantesFIT = [FIT_r1,FIT_r2,FIT_r3,FIT_r4,FIT_r5]
categorias = ["Entre 16 y 25", "Entre 26 a 35 años", "Entre 36 a 45 años", "Entre 46 a 55 años", "Entre 56 y más años" ]
plt.pie (votantesFIT, labels=categorias,autopct="%0.1f %%")
plt.axis("equal")
plt.title("Composición etaria de los votantes del FIT")
plt.show()

#Gráfico de torta, rango etario votantes del PNK
votantesPNK = [PNK_r1,PNK_r2,PNK_r3,PNK_r4,PNK_r5]
categorias = ["Entre 16 y 25", "Entre 26 a 35 años", "Entre 36 a 45 años", "Entre 46 a 55 años", "Entre 56 y más años" ]
plt.pie (votantesPNK, labels=categorias,autopct="%0.1f %%")
plt.axis("equal")
plt.title("Composición etaria de los votantes del PNK")
plt.show()

#Gráfico de torta, rango etario votantes de Otros
votantesOtros = [Otros_r1,Otros_r2,Otros_r3,Otros_r4,Otros_r5]
categorias = ["Entre 16 y 25", "Entre 26 a 35 años", "Entre 36 a 45 años", "Entre 46 a 55 años", "Entre 56 y más años" ]
plt.pie (votantesOtros, labels=categorias,autopct="%0.1f %%")
plt.axis("equal")
plt.title("Composición etaria de los votantes de Otros")
plt.show()

#Gráfico de torta, rango etario de quienes no votan a ninguno o aún no se han decidido
votantesNinguno_NoSabe = [Ninguno_NoSabe_r1,Ninguno_NoSabe_r2,Ninguno_NoSabe_r3,Ninguno_NoSabe_r4,Ninguno_NoSabe_r5]
categorias = ["Entre 16 y 25", "Entre 26 a 35 años", "Entre 36 a 45 años", "Entre 46 a 55 años", "Entre 56 y más años" ]
plt.pie (votantesNinguno_NoSabe, labels=categorias,autopct="%0.1f %%")
plt.axis("equal")
plt.title("Composición etaria de quienes no votan a ninguno o aún no se han decidido")
plt.show()