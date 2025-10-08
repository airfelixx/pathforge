import xml.etree.ElementTree as ET

def parse_osm(file_path: str):
    tree = ET.parse(file_path)
    root = tree.getroot()

    nodes = {}
    for node in root.findall('node'):
        node_id = int(node.attrib['id'])
        lat = float(node.attrib['lat'])
        lon = float(node.attrib['lon'])
        nodes[node_id] = (lat, lon)


    edges = []
    for way in root.findall('way'):
        nds = [int(nd.attrib['ref']) for nd in way.findall('nd')]
        for i in range(len(nds)-1):
            edges.append((nds[i], nds[i+1]))

    return nodes, edges

nodes, edges = parse_osm("../maps_ignore/basic_city_graph.osm")
print(nodes)
print(edges)
