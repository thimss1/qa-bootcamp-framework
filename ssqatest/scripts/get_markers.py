import os

def find_pytest_markers(starting_with):
    markers = set()
    for root, dirs, files in os.walk('../tests'):
        for file in files:
            if file.endswith('.py'):
                with open(os.path.join(root, file), 'r') as f:
                    lines = f.readlines()
                    for line in lines:
                        if '@pytest.mark.' in line:
                            marker = line.split('@pytest.mark.')[1].split('(')[0].split()[0]
                            if marker.startswith(starting_with):
                                markers.add(marker)
    return markers

if __name__ == '__main__':
    starting_with = 'ecom'
    markers = find_pytest_markers(starting_with)
    print(f"Custom markers starting with '{starting_with}':")
    for marker in markers:
        print(marker)
