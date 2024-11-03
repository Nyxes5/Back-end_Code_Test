from django.core.cache import cache
from .repositories import get_persons, get_person_by_name
import logging

logger = logging.getLogger('cache')
CACHE_KEY_PERSON = 'person'


def get_or_cache_persons():
    """
    Used for caching and querying the database if it isn't in the cache
    """
    result = cache.get(CACHE_KEY_PERSON, None)
    if not result:
        logger.info('Fetching persons from database and setting cache')
        result = get_persons()
        cache.set(CACHE_KEY_PERSON, result, 60) # Cache time can be set to different value
    return result

def clear_persons_cache():
    """
    Clear the cache
    """
    logger.info('Deleting persons from cache')
    cache.delete(CACHE_KEY_PERSON)

def get_or_cache_person_by_name(name):
    """
    Used for caching and querying the database for a specific person if it isn't in the cache
    """
    result = cache.get(name, None)
    if not result:
        logger.info(f'Fetching person { name } from database and setting cache')
        result = get_person_by_name(name)
        if result:
            cache.set(name, result, 60) # Cache time can be set to different value
    return result