def graficas_data(x_data, y_data)
    # Creamos una figura general para colocar varios subgráficos
    fig = plt.figure(figsize=(20, 10))                   # Definimos el tamaño de la figura
    
    # ----------- Vista 1: Original (elevación 20, azimut 60) -----------
    ax1 = fig.add_subplot(2, 3, 1, projection='3d')      # Primer subplot en una cuadrícula 2x3
    ax1.scatter(x_entrenamiento.iloc[:, 0],             # Coordenada x: primera columna
                x_entrenamiento.iloc[:, 1],             # Coordenada y: segunda columna
                y_entrenamiento,                        # Coordenada z: etiquetas (y)
                color='blue', marker='o')               # Estilo de puntos: azul y circular
    ax1.set_title("Vista Original (elev=20, azim=60)")  # Título del gráfico
    ax1.set_xlabel("x1")                                # Etiqueta eje x
    ax1.set_ylabel("x2")                                # Etiqueta eje y
    ax1.set_zlabel("y")                                 # Etiqueta eje z
    ax1.view_init(elev=20, azim=60)                     # Ángulo de elevación y rotación
    
    # ----------- Vista 2: Desde arriba (plano x1-x2) -----------
    ax2 = fig.add_subplot(2, 3, 2, projection='3d')      # Segundo subplot
    ax2.scatter(x_entrenamiento.iloc[:, 0],
                x_entrenamiento.iloc[:, 1],
                y_entrenamiento,
                color='green', marker='^')              # Estilo: verde y triángulo
    ax2.set_title("Desde Arriba (elev=90, azim=0)")
    ax2.set_xlabel("x1")
    ax2.set_ylabel("x2")
    ax2.set_zlabel("y")
    ax2.view_init(elev=90, azim=0)                      # Vista cenital (desde arriba)
    
    # ----------- Vista 3: Lateral (proyección x2-y) -----------
    ax3 = fig.add_subplot(2, 3, 3, projection='3d')      # Tercer subplot
    ax3.scatter(x_entrenamiento.iloc[:, 0],
                x_entrenamiento.iloc[:, 1],
                y_entrenamiento,
                color='purple', marker='s')             # Estilo: púrpura y cuadrado
    ax3.set_title("Vista Lateral (elev=0, azim=0)")
    ax3.set_xlabel("x1")
    ax3.set_ylabel("x2")
    ax3.set_zlabel("y")
    ax3.view_init(elev=0, azim=0)                       # Cámara horizontal, mirando desde un lado
    
    # ----------- Vista 4: Trasera (rotación de 180°) -----------
    ax4 = fig.add_subplot(2, 3, 4, projection='3d')      # Cuarto subplot
    ax4.scatter(x_entrenamiento.iloc[:, 0],
                x_entrenamiento.iloc[:, 1],
                y_entrenamiento,
                color='orange', marker='x')             # Estilo: naranja y cruces
    ax4.set_title("Vista Trasera (elev=20, azim=180)")
    ax4.set_xlabel("x1")
    ax4.set_ylabel("x2")
    ax4.set_zlabel("y")
    ax4.view_init(elev=20, azim=180)                    # Como la original pero rotada 180°
    
    # ----------- Vista 5: Desde abajo (elevación negativa) -----------
    ax5 = fig.add_subplot(2, 3, 5, projection='3d')      # Quinto subplot
    ax5.scatter(x_entrenamiento.iloc[:, 0],
                x_entrenamiento.iloc[:, 1],
                y_entrenamiento,
                color='red', marker='D')                # Estilo: rojo y rombos
    ax5.set_title("Vista desde Abajo (elev=-60, azim=60)")
    ax5.set_xlabel("x1")
    ax5.set_ylabel("x2")
    ax5.set_zlabel("y")
    ax5.view_init(elev=-60, azim=60)                    # Vista desde debajo del plano
    
    # Ajustamos el espaciado para que no se encimen los gráficos
    plt.tight_layout()
    
    # Mostramos la figura completa
    plt.show()