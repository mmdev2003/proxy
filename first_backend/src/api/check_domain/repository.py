from db import interface as db
from db.models import Domain


async def check_domain(session, public_domain):
    domain = await db.get_row(session, Domain, (Domain.public_domain == public_domain))
    return domain[0]["domain"]
