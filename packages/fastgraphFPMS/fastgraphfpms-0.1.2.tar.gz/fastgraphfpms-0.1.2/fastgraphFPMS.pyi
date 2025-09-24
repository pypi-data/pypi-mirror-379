"""
Type stubs for fastgraphFPMS - Pour l'autocomplétion IDE
"""

from typing import List, Tuple, Union

class Graph:
    """
    Représente un graphe avec une matrice d'adjacence.
    
    Cette classe permet de créer et manipuler des graphes, et d'exécuter
    divers algorithmes graphiques optimisés.
    """
    
    def __init__(self, matrix: List[List[int]] = None, directed: bool = False) -> None:
        """
        Crée un graphe à partir d'une matrice d'adjacence.
        
        Args:
            matrix: Matrice d'adjacence représentant le graphe
            directed: True pour un graphe dirigé, False pour non dirigé
        """
        ...
    
    def __init__(self, filename: str, directed: bool = False) -> None:
        """
        Crée un graphe à partir d'un fichier.
        
        Args:
            filename: Chemin vers le fichier contenant la matrice
            directed: True pour un graphe dirigé, False pour non dirigé
        """
        ...
    
    def get_num_nodes(self) -> int:
        """Retourne le nombre de nœuds du graphe."""
        ...
    
    def get_is_directed(self) -> bool:
        """Indique si le graphe est dirigé."""
        ...
    
    def add_edge(self, from_node: int, to_node: int, weight: int = 1) -> None:
        """
        Ajoute une arête entre deux nœuds.
        
        Args:
            from_node: Index du nœud source (0-indexé)
            to_node: Index du nœud destination
            weight: Poids de l'arête (défaut: 1)
        """
        ...
    
    def load_from_file(self, filename: str) -> None:
        """Charge un graphe depuis un fichier."""
        ...
    
    def save_to_file(self, filename: str) -> None:
        """Sauvegarde le graphe dans un fichier."""
        ...