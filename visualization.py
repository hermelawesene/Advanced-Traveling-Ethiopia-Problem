import networkx as nx
import matplotlib.pyplot as plt

# Define the graph data
connections = {
    "Adigrat": ["Mekelle", "Asmera", "Adwa"],
    "Asmera": ["Adigrat", "Axum"],
    "Adwa": ["Adigrat", "Axum", "Mekelle"],
    "Axum": ["Asmera", "Adwa", "Shire"],
    "Mekelle": ["Sekota", "Adwa", "Alamata", "Adigrat"],
    "Shire": ["Debarke", "Humera", "Axum"],
    "Sekota": ["Mekelle", "Alamata", "Lalibela"],
    "Alamata": ["Woldia", "Sekota", "Mekelle", "Samara"],
    "Debarke": ["Gondar", "Shire"],
    "Humera": ["Kartum", "Gondar", "Shire"],
    "Lalibela": ["DebreTabor", "Woldia", "Sekota"],
    "Woldia": ["Lalibela", "Alamata", "Samara", "Dessie"],
    "Samara": ["Alamata", "Woldia", "FantiRasu", "GabiRasu"],
    "Gondar": ["Humera", "Debarke", "Metema", "Azezo"],
    "Kartum": ["Metema", "Humera"],
    "DebreTabor": ["Lalibela", "BahirDar"],
    "Dessie": ["Woldia", "Kemise"],
    "FantiRasu": ["Samara", "KilbetRasu"],
    "GabiRasu": ["Samara", "Awash"],
    "Metema": ["Gondar", "Azezo", "Kartum"],
    "Azezo": ["Metema", "BahirDar"],
    "BahirDar": ["Azezo", "DebreTabor", "Metekel", "Injibara", "FinoteSelam"],
    "Kemise": ["Dessie", "DebreSina"],
    "KilbetRasu": ["FantiRasu"],
    "Awash": ["GabiRasu", "Matahara", "Chiro"],
    "Metekel": ["BahirDar", "Assosa"],
    "Injibara": ["BahirDar", "FinoteSelam"],
    "FinoteSelam": ["BahirDar", "Injibara", "DebreMarkos"],
    "DebreSina": ["Kemise", "DebreMarkos", "DebreBirhan"],
    "Matahara": ["Awash", "Adama"],
    "Chiro": ["Awash", "DireDewa"],
    "Assosa": ["Metekel", "DembiDollo"],
    "DebreMarkos": ["FinoteSelam", "DebreSina"],
    "DebreBirhan": ["DebreSina", "AddisAbaba"],
    "Adama": ["Matahara", "AddisAbaba", "Batu", "Assella"],
    "DireDewa": ["Chiro", "Harar"],
    "DembiDollo": ["Assosa", "Gambella", "Gimbi"],
    "AddisAbaba": ["DebreBirhan", "Adama", "Ambo"],
    "Batu": ["Adama", "Shashemene", "ButaJira"],
    "Assella": ["Adama", "Assasa"],
    "Harar": ["DireDewa", "Babile"],
    "Gambella": ["DembiDollo", "Gore"],
    "Gimbi": ["DembiDollo", "Nekemete"],
    "Ambo": ["AddisAbaba", "Nekemete", "Wolkite"],
    "ButaJira": ["Batu", "Worabe"],
    "Shashemene": ["Batu", "Hossana", "Hawassa", "Dodolla"],
    "Assasa": ["Assella", "Dodolla"],
    "Babile": ["Harar", "Jigjiga"],
    "Gore": ["Gambella", "Tepi", "Bedelle"],
    "Nekemete": ["Gimbi", "Bedelle", "Ambo"],
    "Wolkite": ["Ambo", "Worabe", "Jimma"],
    "Worabe": ["ButaJira", "Wolkite", "Hossana"],
    "Hossana": ["Worabe", "WolaitaSodo", "Shashemene"],
    "Hawassa": ["Shashemene", "Dilla"],
    "Dodolla": ["Shashemene", "Assasa", "Bale"],
    "Jigjiga": ["Babile", "DegaHabur"],
    "Tepi": ["Gore", "MezanTeferi", "Bonga"],
    "Bedelle": ["Gore", "Nekemete", "Jimma"],
    "Jimma": ["Bedelle", "Wolkite", "Bonga"],
    "WolaitaSodo": ["Hossana", "Dawro", "ArbaMinch"],
    "Dilla": ["Hawassa", "BuleHora"],
    "Bale": ["Dodolla", "Liben", "Goba", "SofOumer"],
    "DegaHabur": ["Jigjiga", "Goba", "KebriDehar"],
    "MizanTeferi": ["Tepi", "Bonga", "Basketo"],
    "Bonga": ["Tepi", "MizanTeferi", "Jimma", "Dawro"],
    "Dawro": ["Bonga", "Basketo", "WolaitaSodo"],
    "ArbaMinch": ["WolaitaSodo", "Basketo", "Konso"],
    "BuleHora": ["Dilla", "Yabello"],
    "Liben": ["Bale"],
    "Goba": ["Bale", "SofOumer", "DegaHabur"],
    "SofOumer": ["Goba", "Bale", "KebriDehar"],
    "KebriDehar": ["DegaHabur", "SofOumer", "Werder", "Gode"],
    "Basketo": ["MizanTeferi", "Dawro", "BenchMaji", "ArbaMinch"],
    "Konso": ["ArbaMinch", "Yabello"],
    "Yabello": ["Konso", "Moyale", "BuleHora"],
    "Gode": ["KebriDehar", "Dollo", "Mokadisho"],
    "Werder": ["KebriDehar"],
    "BenchMaji": ["Basketo", "Juba"],
    "Moyale": ["Yabello", "Nairobi"],
    "Dollo": ["Gode"],
    "Mokadisho": ["Gode"],
    "Juba": ["BenchMaji"],
    "Nairobi": ["Moyale"],
}

# Create the graph
G = nx.Graph()
for city, neighbors in connections.items():
    for neighbor in neighbors:
        G.add_edge(city, neighbor)

# Draw the graph
plt.figure(figsize=(12, 12))
pos = nx.spring_layout(G, seed=42, k=0.5)  # Position nodes for visualization
nx.draw(G, pos, with_labels=True, node_size=2000, node_color="lightblue", font_size=8, edge_color="gray")

plt.title("City Connection Network")
plt.show()
