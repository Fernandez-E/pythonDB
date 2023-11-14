def build_table_query(
        table_name:str
):
    """
    Args:
    table_name:str
    """

    query = f"""
        SELECT *
        FROM {table_name}
    """

    return query

