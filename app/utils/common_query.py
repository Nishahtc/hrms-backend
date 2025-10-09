

def get_data_by_id(data_list: list, id: int | None = None):
    if id is not None:
        for item in data_list:
            if item.get("id") == id:
                return item
        return {"error": f"Record with id {id} not found"}
    
    return data_list
