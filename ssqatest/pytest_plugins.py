# pytest_plugins.py

def pytest_collection_modifyitems(items):
    get_all_markers(items, "ecom")
    check_marker_exists_on_each_test(items, "ecom")

def get_all_markers(items, mark_prefix):
    ecom_markers = set()

    for item in items:
        for marker in item.own_markers:
            if marker.name.startswith(mark_prefix):
                ecom_markers.add(marker.name)

    print("Custom markers starting with 'ecom':")
    print(ecom_markers)

def check_marker_exists_on_each_test(items, mark_prefix):

    for item in items:
        for marker in item.own_markers:
            if marker.name.startswith(mark_prefix):
                break
        else:
            breakpoint()
            print(f"None of the markers on this test start with '{mark_prefix}")