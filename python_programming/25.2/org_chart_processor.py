import json

class OrgChartNode:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, child):
        self.children.append(child)


def build_tree(data, root_name):
    root = OrgChartNode(root_name)
    if root_name in data:
        for child_name in data[root_name]:
            child_node = build_tree(data, child_name)
            root.add_child(child_node)
    return root


def print_tree(node, level=0):
    print('  ' * level + node.name)
    for child in node.children:
        print_tree(child, level + 1)


def main():
    #with open("companies.json", "r") as file:
     #   companies_data = json.load(file)
    companies_data = {
        'CEO': ['CTO', 'CFO', 'CMO'],
        'CTO': ['Dev1', 'Dev2'],
        'CFO': ['Accountant'],
        'CMO': [],
        'Dev1': [],
        'Dev2': ['Intern'],
        'Accountant': [],
        'Intern': []
    }
    root = build_tree(companies_data, 'CEO')
    print_tree(root)


if __name__ == "__main__":
    main()
