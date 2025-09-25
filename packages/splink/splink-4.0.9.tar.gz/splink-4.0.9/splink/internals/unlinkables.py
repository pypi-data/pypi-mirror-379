from __future__ import annotations

from typing import TYPE_CHECKING, Any

from splink.internals.pipeline import CTEPipeline

# https://stackoverflow.com/questions/39740632/python-type-hinting-without-cyclic-imports
if TYPE_CHECKING:
    from splink.internals.linker import Linker


def unlinkables_data(linker: Linker) -> list[dict[str, Any]]:
    """Generate data displaying the proportion of records that are "unlinkable"
    for a given splink score threshold and model parameters. These are records that,
    even when compared with themselves, do not contain enough information to confirm
    a match.

    Args:
        linker (Splink): A Splink data linker
    """

    self_link_df = linker._self_link()

    pipeline = CTEPipeline()

    sql = f"""
        select
        round(match_weight, 2) as match_weight,
        round(match_probability, 5) as match_probability
        from {self_link_df.physical_name}
    """

    pipeline.enqueue_sql(sql, "__splink__df_round_self_link")

    sql = """
        select
        max(match_weight) as match_weight,
        match_probability,
        count(*) / cast( sum(count(*)) over () as float) as prop
        from __splink__df_round_self_link
        group by match_probability
        order by match_probability
    """

    pipeline.enqueue_sql(sql, "__splink__df_unlinkables_proportions")

    sql = """
        select *,
        sum(prop) over(order by match_probability) as cum_prop
        from __splink__df_unlinkables_proportions
        where match_probability < 1
    """
    pipeline.enqueue_sql(sql, "__splink__df_unlinkables_proportions_cumulative")
    data = linker._db_api.sql_pipeline_to_splink_dataframe(pipeline, use_cache=False)

    unlinkables_dict = data.as_record_dict()
    data.drop_table_from_database_and_remove_from_cache()
    return unlinkables_dict
