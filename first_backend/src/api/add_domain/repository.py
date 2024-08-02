from db import interface as db
from db.models import Domain


async def add_domain(session, domain_data):
    return await db.set_row(session, Domain, domain_data)
