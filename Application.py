from tkinter import * 
import matplotlib.pyplot as plt
import networkx as nx 
from networkx.drawing.layout import (
    circular_layout,
    kamada_kawai_layout,
    planar_layout,
    random_layout,
    shell_layout,
    spectral_layout,
    spring_layout,
)
import numpy as np
from tkinter import ttk


fenetre = Tk() 
fenetre.geometry('800x700')
fenetre.title('Graphs')
fenetre.resizable(height = True, width = True)
fenetre.configure(background='#33B8FF')

class Application:
    nbr_sommets = StringVar()
    Matrix = [] 
    M_Entry = [] 
    G = nx.Graph()
    Edgets = []
    btn_BFS = Button()
    btn_Prim = Button()
    btn_Warshall = Button()
    btn_Dijicstra = Button()
    btn_BillmanFord = Button()
    btn_DFS = Button()
    visited = []
    labelS = Label()
    def __init__(self , fenetre):
        self.labelS = Label(fenetre , text="Entrer le nombre de sommet")
        self.labelS.grid(row=0 , column=0)

        entree = Entry(fenetre , textvariable=self.nbr_sommets)
        entree.grid(row=0 , column=1)

        bouton  = Button(fenetre , text="Valider" , command=self.function)
        bouton.grid(row=0 , column=2)
        bouton  = Button(fenetre , text="Graph non Oriente", width='40', padx=3 , pady=2, background='white', command=self.NonOrientedGraph)
        bouton.grid(row=2 , column=0)
        bouton  = Button(fenetre , text="Graph pondere", width='40',padx=3 , pady=2, background='white', command=self.CoutGraph)
        bouton.grid(row=3 , column=0)
        bouton  = Button(fenetre , text="Graph Oriente", width='40',padx=3 , pady=2, background='white' , command=self.OrientedGraph)
        bouton.grid(row=4 , column=0)
        bouton  = Button(fenetre , text="Graph Oriente et pondere",padx=3 , pady=2, background='white', width='40' , command=self.Oriented_CoutGraph)
        bouton.grid(row=5 , column=0)
        bouton  = Button(fenetre , text="Graph Oriente et pondere negativement",padx=3 , pady=2, background='white', width='40' , command=self.negativeCout)
        bouton.grid(row=6 , column=0)
        self.btn_BFS = Button(fenetre , text='Parcour en largeur',padx=3 , pady=2, background='white' , command=self.BFS)
        self.btn_BFS.grid_forget()
        self.btn_DFS = Button(fenetre , text='Parcour en pronfondeur',padx=3 , pady=2, background='white' , command=self.Run_DFS)
        self.btn_DFS.grid_forget()
        self.btn_Prim = Button(fenetre , text='Arbre couvrante Minimale',padx=3 , pady=2, background='white' , command=self.Prim)
        self.btn_Prim.grid_forget()
        self.btn_Warshall = Button(fenetre , text='Est ce que le graphe est connex ??', width='40',padx=3 , pady=2, background='white' , command=self.Warshall)
        self.btn_Warshall.grid_forget()
        self.btn_Dijicstra = Button(fenetre , text='Dijicstra' , width='30' ,command=self.Dijicstra)
        self.btn_Dijicstra.grid_forget()
        self.btn_BillmanFord = Button(fenetre , text='BillmanFord' , width='30' ,command=self.BillmanFord)
        self.btn_BillmanFord.grid_forget()
        self.tree = ttk.Treeview(fenetre , columns= (1,2) , height=5 , show="headings")
        self.tree.grid_forget()
    def function(self):
        nbr_sommmets = int(self.nbr_sommets.get())
        rows = []
        for i in range(nbr_sommmets):
                cols = []
                for j in range(nbr_sommmets):
                    e = Entry(fenetre,justify=CENTER)
                    e.grid(row=i+1, column=j+1, sticky=NSEW)
                    cols.append(e)
                rows.append(cols)
        self.M_Entry = rows
        self.btn_BillmanFord.grid_forget()
        self.btn_Dijicstra.grid_forget()
        self.btn_Warshall.grid_forget()
        self.btn_Prim.grid_forget()
        self.btn_DFS.grid_forget()
        self.btn_BFS.grid_forget()
        for label in fenetre.winfo_children():
            if isinstance(label, Label):
                label.grid_forget()
        self.labelS.grid(row=0 , column=0)
        self.tree.grid_forget()

    def get_Value(self):
        nbr_sommmet = int(self.nbr_sommets.get())
        rows = []
        for i in range(nbr_sommmet):
                cols = []
                for j in range(nbr_sommmet):
                    values_obtained = int(self.M_Entry[i][j].get())
                    cols.append(values_obtained)
                rows.append(cols)
        self.Matrix = rows 
        print(self.Matrix)
    def NonOrientedGraph(self):
        self.get_Value()
        nbr_sommmet = int(self.nbr_sommets.get())
        for i in range(nbr_sommmet):
            self.G.add_node(i)
        for j in range(nbr_sommmet):
            for k in range(nbr_sommmet):
                if (self.Matrix[j][k] == 1):   
                    self.G.add_edge(j,k)
        self.btn_BFS.grid(row=8 , column=2)
        self.btn_DFS.grid(row=8 , column=1)
        nx.draw(self.G , with_labels= True)
        plt.show()
    def CoutGraph(self):
        self.get_Value() 
        pos = nx.circular_layout(self.G)  
        nbr_sommmet = int(self.nbr_sommets.get())
        for i in range(nbr_sommmet):
            self.G.add_node(i)
        for j in range(nbr_sommmet):
            for k in range(nbr_sommmet):
                if (self.Matrix[j][k] != 0):
                    self.G.add_edge(j,k, weight=self.Matrix[j][k])
                    pos[j] = np.array([j , k])
        labels_edges = {}
        labels_edges = {edge:self.G.edges[edge]['weight'] for edge in self.G.edges}
        print(labels_edges) 
        self.btn_Prim.grid(row=8 , column=1)
        self.btn_Dijicstra.grid(row=8, column=2)
        self.btn_BillmanFord.grid(row=8, column=3)
        nx.draw_networkx_edge_labels(self.G, pos , edge_labels=labels_edges , font_color='red')  
        nx.draw(self.G, pos , with_labels= True)
        plt.show()
    def OrientedGraph(self):
        self.get_Value()
        nbr_sommmet = int(self.nbr_sommets.get())
        self.G = nx.DiGraph()
        for i in range(nbr_sommmet):
            self.G.add_node(i)
        for j in range(nbr_sommmet):
            for k in range(nbr_sommmet):
                if (self.Matrix[j][k] == 1): 
                    self.Edgets.append((j,k)) 
                    self.G.add_edges_from(self.Edgets)
        self.btn_Warshall.grid(row=9 , column=2)
        nx.draw_networkx(self.G )
        plt.show()
    def BFS(self):
        visisted = []
        queue = []
        visisted.append(0) # donner le sommet de depart qui est le 0 
        queue.append(0) 
        phrase = 'Votre parcour en largeur est : '
        while queue :
            m=queue.pop(0)
            print(m,"le sommet a bien defiler")
            for n in self.G.neighbors(m):
                if n not in visisted :
                    visisted.append(n)
                    queue.append(n)
        label = Label(fenetre,text=phrase , font=('Arial' , 12) , fg='red')
        label.grid(row=9 , column=1)
        label = Label(fenetre,text=visisted , font=('Arial' , 12) , fg='red')
        label.grid(row=9 , column=2)
    def DFS(self , node):
        self.visited.append(node)
        for neighbor in self.G.neighbors(node):
            if neighbor not in self.visited :
                self.DFS(neighbor)
    def Run_DFS(self):
        node = 0 
        self.DFS(node)
        vis = self.visited 
        label = Label(fenetre,text="Votre parcour en profendeur est : " , font=('Arial' , 12) , fg='red')
        label.grid(row=10 , column=1)
        label = Label(fenetre,text=vis , font=('Arial' , 12) , fg='red')
        label.grid(row=10 , column=2)
        print(self.visited)
    def Prim(self):
        nbr_sommmet = int(self.nbr_sommets.get())
        selected_node = [] 
        selected_node = [0]*nbr_sommmet
        selected_node[0] = True 
        no_edge = 0
        ACM = 0 
        while(no_edge < nbr_sommmet -1):
            minimum = 9999999 
            a=0
            b=0
            for m in range(nbr_sommmet):
                if  selected_node[m]:
                    for n in range(nbr_sommmet):
                        if ( (not selected_node[n]) and self.Matrix[m][n]):
                            if minimum > self.Matrix[m][n]:
                                minimum = self.Matrix[m][n]
                                a=m
                                b=n
            print(str(a) + "-" + str(b) + ":" + str(self.Matrix[a][b]))
            ACM += self.Matrix[a][b]
            selected_node[b] = True
            no_edge += 1
        label = Label(fenetre,text="L'arbre couvrante minimale est : " , font=('Arial',12) , fg='red')
        label.grid(row=9 , column=1)
        label = Label(fenetre,text=ACM , font=('Arial',12) , fg='red')
        label.grid(row=9 , column=2)

    def Warshall(self):
        nbr_sommmet = int(self.nbr_sommets.get())
        for i in range(nbr_sommmet):
            for j in range(nbr_sommmet):
                if( (j , i)  in self.G.edges) and (i != j):
                    for k in range(nbr_sommmet):
                        if ((i,k)  in self.G.edges) and (i!=k):
                            if( (j , k) not in self.G.edges):
                                self.G.add_edge(j,k)
        print(self.G.edges)
        for n in range(nbr_sommmet):
            for m in range(nbr_sommmet):
                if((n,m) in self.G.edges) and ((m,n) in self.G.edges):
                    conx = True 
                else:
                    conx = False
        if(conx):
            label = Label(fenetre , text='Le graph est connex' , font=('Arial' , 12) , fg='red')
            label.grid(row=10 , column=2)
        else:
            label = Label(fenetre , text="Le graph n'est connex",font=('Arial' , 12) , fg='red')
            label.grid(row=10 , column=2)
        nx.draw(self.G , with_labels= True )
        plt.show()
    def Dijicstra(self):
        nbr_sommmet = int(self.nbr_sommets.get())
        L = [1e7] * nbr_sommmet
        for i in range(nbr_sommmet):
            if(self.Matrix[0][i] != 0):
                L[i]= self.Matrix[0][i] 
        L[0] = 0
        resultat = []
        S = [False] * nbr_sommmet
        for u in range(nbr_sommmet):
            u = self.minDistance(L, S)
            S[u] = True
            for v in range(nbr_sommmet):
                if(self.Matrix[u][v] > 0 and
                    S[v] == False and
                    L[v] > L[u] + self.Matrix[u][v]):
                    L[v] = L[u] + self.Matrix[u][v]
        self.tree.grid(row=10 , column=1)
        self.tree.heading(1 , text="Sommet")
        self.tree.heading(2 , text="Distance")
        self.tree.column(1 , width=60)
        self.tree.column(2 , width=60)
        for node in range(nbr_sommmet):
            resultat.append([node , L[node]])
        for row in resultat:
            self.tree.insert('' , END , values=row)
    def minDistance(self, L, S):
        nbr_sommmet = int(self.nbr_sommets.get())
        # initialiser la distance minimale 
        min = 1e7 
        for v in range(nbr_sommmet):
            if L[v] < min and S[v] == False:
                min = L[v]
                min_index = v  
        return min_index   
    def BillmanFord(self):
        resultat = []
        nbr_sommmet = int(self.nbr_sommets.get())
        L = [float("Inf")] * nbr_sommmet 
        L[0] = 0 
        for _ in range(nbr_sommmet - 1): 
            for u, v in self.G.edges:
                if L[u] + self.Matrix[u][v] < L[v]:
                    L[v] = L[u] + self.Matrix[u][v]
        #Verifiant si on a un circuit absorbant
        for u, v in self.G.edges:
            if  L[u] + self.Matrix[u][v] < L[v]:
                print("Graph contains negative weight cycle")
                return
        print("Vertex Distance from Source")
        for i in range(nbr_sommmet):
            print("{0}\t\t{1}".format(i, L[i]))
        self.tree.grid(row=10 , column=1)
        self.tree.heading(1 , text="Sommet")
        self.tree.heading(2 , text="Distance")
        self.tree.column(1 , width=60)
        self.tree.column(2 , width=60)
        for node in range(nbr_sommmet):
            resultat.append([node , L[node]])
        for row in resultat:
            self.tree.insert('' , END , values=row)
    def Oriented_CoutGraph(self):
        self.get_Value()
        self.btn_Dijicstra.grid(row=8, column=2)
        self.btn_BillmanFord.grid(row=8, column=3)
        nbr_sommmet = int(self.nbr_sommets.get())
        G = nx.DiGraph()
        for i in range(nbr_sommmet):
            G.add_node(i)
        for j in range(nbr_sommmet):
            for k in range(nbr_sommmet):
                if self.Matrix[j][k] != 0:
                    G.add_edge(j, k, weight=self.Matrix[j][k])
        pos = nx.circular_layout(G)
        edge_labels = nx.get_edge_attributes(G, 'weight')

        nx.draw(G, pos, with_labels=True, arrows=True)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')
        plt.show()
        self.G = G 
    def negativeCout(self):
        self.get_Value()
        self.btn_BillmanFord.grid(row=8, column=2)
        nbr_sommmet = int(self.nbr_sommets.get())
        G = nx.DiGraph()
        for i in range(nbr_sommmet):
            G.add_node(i)
        for j in range(nbr_sommmet):
            for k in range(nbr_sommmet):
                if self.Matrix[j][k] != 0:
                    G.add_edge(j, k, weight=self.Matrix[j][k])
        pos = nx.circular_layout(G)
        edge_labels = nx.get_edge_attributes(G, 'weight')

        nx.draw(G, pos, with_labels=True, arrows=True)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')
        plt.show()
        self.G = G 


obj = Application(fenetre)
fenetre.mainloop() 