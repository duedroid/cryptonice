from databases import Database

from core.config import settings


database = Database(settings.DATABASE_URL)