#!/usr/bin/env python3
'''task web.
'''
import redis
import requests
from functools import wraps
from typing import Callable


redis_store = redis.Redis()
'''redis store.
'''


def data_cacher(method: Callable) -> Callable:
    '''Callable data.
    '''
    @wraps(method)
    def invoker(url) -> str:
        '''The invoker.
        '''
        redis_store.incr(f'count:{url}')
        result = redis_store.get(f'result:{url}')
        if result:
            return result.decode('utf-8')
        result = method(url)
        redis_store.set(f'count:{url}', 0)
        redis_store.setex(f'result:{url}', 10, result)
        return result
    return invoker


@data_cacher
def get_page(url: str) -> str:
    '''get page
    '''
    return requests.get(url).text
