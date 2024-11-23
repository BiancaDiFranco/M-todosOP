import pandas as pd

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