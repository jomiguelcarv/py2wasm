# bsp_test.py
import numpy as np
import networkx as nx
from shapely.geometry import Polygon, LineString
from shapely.ops import split, unary_union
from shapely import affinity
from scipy.cluster.hierarchy import linkage, fcluster

def run_tests():
    results = []
    
    # NumPy test
    a = np.array([1,2,3,4])
    results.append(f"NumPy OK mean={a.mean()}")

    # NetworkX test
    G = nx.Graph()
    G.add_edge("A","B")
    G.add_edge("B","C")
    results.append(f"NetworkX OK nodes={len(G.nodes)}")
    
    # Shapely union test
    poly1 = Polygon([(0,0),(2,0),(2,2),(0,2)])
    poly2 = Polygon([(1,1),(3,1),(3,3),(1,3)])
    u = unary_union([poly1, poly2])
    results.append(f"Union OK area={round(u.area,2)}")
    
    # Shapely split test
    poly = Polygon([(0,0),(4,0),(4,4),(0,4)])
    line = LineString([(2,-1),(2,5)])
    pieces = split(poly,line).geoms
    results.append(f"Split OK pieces={len(pieces)}")
    
    # Shapely transform test
    rot = affinity.rotate(poly, 45)
    results.append(f"Rotate OK area={round(rot.area,2)}")
    
    return "\n".join(results)


def respond_to_js(msg: str) -> str:
    """Respond to JS messages."""
    if msg == "hello":
        return "world"
    elif msg == "run_bsp":
        # Optionally run the tests from JS
        return run_tests()
    else:
        return f"Python received: {msg}"