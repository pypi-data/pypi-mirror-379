from typed_linq_collections.collections.q_list import QList
from typed_linq_collections.q_iterable import query


def test_querying_built_in_collections() -> None:
    fruits_by_first_character = (query(["apple", "apricot",  "mango", "melon", "peach", "pineapple"])
                                 .group_by(lambda fruit: fruit[0])
                                 .where(lambda group: group.key in {"a", "p"})
                                 .to_list())

    assert fruits_by_first_character == [['apple', 'apricot'], ['peach', 'pineapple']]

def test_querying_with_queryable_collections() -> None:
    fruits_by_first_character = (QList(("apple", "apricot",  "mango", "melon", "peach", "pineapple"))
                                 .group_by(lambda fruit: fruit[0])
                                 .where(lambda group: group.key in {"a", "p"})
                                 .to_list())

    assert fruits_by_first_character == [['apple', 'apricot'], ['peach', 'pineapple']]