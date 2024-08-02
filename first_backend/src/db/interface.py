from sqlalchemy import insert, select, update, delete

from utils.logger import logger


async def update_row(session, table, filter_condition, update_data):
    try:
        query = update(table).where(filter_condition).values(update_data)
        await session.execute(query)
        await session.commit()
    except Exception as e:
        logger.error('Row update', extra=e)
        raise e


async def get_row(session, table, filter_condition=None):
    try:
        query = select(table)
        if filter_condition is not None:
            query = query.where(filter_condition)
        result = await session.execute(query)
        result = result.scalars().all()
        result_dicts = [{column.name: getattr(row, column.name) for column in table.__table__.columns if
                         column.name not in ['create_time', 'update_time']} for row in result]
        return result_dicts
    except Exception as e:
        logger.error('Row get', extra=e)
        return []


async def delete_row(session, table, filter_condition):
    try:
        query = delete(table).where(filter_condition)
        await session.execute(query)
        await session.commit()
    except Exception as e:
        logger.error('Row delete', extra=e)


async def set_row(session, table, set_data):
    try:
        query = insert(table).values(set_data)
        result = await session.execute(query)
        await session.commit()
        return result.inserted_primary_key[0]
    except Exception as e:
        logger.error('Row set', extra=e)
        raise e
