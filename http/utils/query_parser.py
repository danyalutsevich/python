def query_parser(query: str):
    result = {}
    key_value = query.split("&")

    for el in key_value:
        kw = el.split("=")
        result[kw[0]] = kw[1]
    return result
