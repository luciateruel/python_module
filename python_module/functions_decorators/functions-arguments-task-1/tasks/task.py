from typing import Dict, Any, Callable, Iterable

DataType = Iterable[Dict[str, Any]]
ModifierFunc = Callable[[DataType], DataType]


def query(data: DataType, selector: ModifierFunc,
          *filters: ModifierFunc) -> DataType:
    """
    Query data with column selection and filters

    :param data: List of dictionaries with columns and values
    :param selector: result of `select` function call
    :param filters: Any number of results of `field_filter` function calls
    :return: Filtered data
    """
    # primero aplicar selector
    result = selector(data)

    # luego aplicar cada filtro en orden
    for f in filters:
        result = f(result)

    return result


def select(*columns: str) -> ModifierFunc:
    """Return function that selects only specific columns from dataset
    :param columns: Column names to keep
    :return: Function that filters dictionaries by these columns"""
    def selector(data: DataType) -> DataType:
        # Para cada fila, devolver solo las keys que están en columns
        return [{k: row[k] for k in columns} for row in data]

    return selector



def field_filter(column: str, *values: Any) -> ModifierFunc:
    """Return function that filters specific column to be one of `values`"""

    def filtered_func(data):
        return [row for row in data if row[column] in values]

    return filtered_func



def test_query():
    friends = [
        {'name': 'Sam', 'gender': 'male', 'sport': 'Basketball'}
    ]
    value = query(
        friends,
        select(*('name', 'gender', 'sport')),
        field_filter(*('sport', *('Basketball', 'volleyball'))),
        field_filter(*('gender', *('male',))),
    )
    assert [{'gender': 'male', 'name': 'Sam', 'sport': 'Basketball'}] == value


if __name__ == "__main__":
    test_query()
friends = [
    {'name': 'Sam', 'gender': 'male', 'sport': 'Basketball'},
    {'name': 'Emily', 'gender': 'female', 'sport': 'Volleyball'},
]

result = query(
    friends,
    select('name', 'gender', 'sport'),
    field_filter('sport', *('Basketball', 'Volleyball')),
    field_filter('gender', *('male',)),
)
