def get_data_by_id(data_list: list, id: int):
    for item in data_list:
        if item.get("id") == id:
            return item
    return None







