def pytest_collection_modifyitems(config, items):
    for item in items.copy():
        if item.cls.__name__.endswith("Base"):
            items.remove(item)
