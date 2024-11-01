from django.core.cache import cache
from .repositories import get_persons
import logging

logger = logging.getLogger('cache')
CACHE_KEY_PERSON = 'person'


def get_or_cache_persons():
    """
    Used for caching and querying the database if it isn't in the cache
    """
    result = cache.get(CACHE_KEY_PERSON, None)
    if not result:
        logger.info('Fetching persons from database and setting cache') # This is for development purposes only
        result = get_persons()
        cache.set(CACHE_KEY_PERSON, result, 60)
    return result

def clear_persons_cache():
    """
    Clear the cache
    """
    logger.info('Deleting persons from cache') # This is for development purposes only
    cache.delete(CACHE_KEY_PERSON)