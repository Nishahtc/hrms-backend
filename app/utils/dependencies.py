from fastapi import Query

def pagination_params(limit: int = Query(10, ge=1), skip: int = Query(0, ge=0)):
    return {"limit": limit, "skip": skip}

def search_params(id: int | None = Query(None), name: str | None = Query(None)):
    return {"id": id, "name": name}
