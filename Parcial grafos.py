import networkx as nx
import matplotlib.pyplot as plt
def red_social():
    # se crea un grafo vacío
    G = nx.Graph()
    
    # Nodo central osea yo 
    centro = "Yo"
    G.add_node(centro)
    
    # Definir las comunidades y sus integrantes
    familia = ["Mamá", "Papá", "Hermano", "Primo", "Tío", "Prima"]
    barrio = ["Juan", "Jarol", "Jose", "Sofía", "Martin"]
    universidad = ["Diego", "Kevin", "Juan", "Snaider", "Andrés", "Paula"]
    
    # Se añaden nodos al grafo
    G.add_nodes_from(familia)
    G.add_nodes_from(barrio)
    G.add_nodes_from(universidad)
    
    # Se conecta el nodo central con todos los integrantes
    for persona in familia + barrio + universidad:
        G.add_edge(centro, persona)
        
    ## Se crean las conexiones internas dentro de cada comunidad (para que se agrupen visualmente)

    # Conexiones de familia
    conexiones_familia = [("Mamá", "Papá"), ("Mamá", "Hermano"), ("Papá", "Primo"), 
                          ("Hermano", "Primo"), ("Tío", "Prima"), ("Mamá", "Tío")]
    G.add_edges_from(conexiones_familia)
    
    # Conexiones de amigos del barrio
    conexiones_barrio = [("Juan", "Jarol"), ("Jarol", "Jose"), ("Juan", "Martin"), 
                         ("Jose", "Sofía"), ("Sofía", "Martin")]
    G.add_edges_from(conexiones_barrio)
    
    # Conexiones de universidad
    conexiones_universidad = [("Diego", "Kevin"), ("Kevin", "Juan"), ("Juan", "Snaider"),
                              ("Snaider", "Paula"), ("Diego", "Juan"), ("Andrés", "Paula")]
    G.add_edges_from(conexiones_universidad)
    
    # También podemos añadir una conexión entre grupos 
    G.add_edge("Hermano", "Paula")
    G.add_edge("Jose", "Kevin")
    
    # Asignar colores a los nodos dependiendo de su comunidad
    colores = []
    for nodo in G.nodes():
        if nodo == centro:
            colores.append('yellow')      # Centro
        elif nodo in familia:
            colores.append('lightgreen')  # Familia
        elif nodo in barrio:
            colores.append('skyblue')     # Barrio
        elif nodo in universidad:
            colores.append('salmon')      # Universidad
            
    # Configurar el tamaño de la figura
    plt.figure(figsize=(10, 8))
    
    # Generar el layout (spring_layout simula repulsión entre nodos, agrupando los conectados)
    pos = nx.spring_layout(G, k=0.5, seed=42)
    
    # Dibujar los nodos, las aristas y las etiquetas
    nx.draw_networkx_nodes(G, pos, node_color=colores, node_size=2000, edgecolors='black')
    nx.draw_networkx_edges(G, pos, width=1.5, alpha=0.6)
    nx.draw_networkx_labels(G, pos, font_size=10, font_weight="bold", font_family="sans-serif")
    
    # Configuraciones finales del gráfico
    plt.title("Mi Red Social Personal", fontsize=16, fontweight='bold')
    plt.axis('off') # Ocultar los ejes
    
    # Mostrar el gráfico
    plt.show()

# Ejecutar la función
if __name__ == "__main__":
    red_social()