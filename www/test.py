import asyncio
import orm
import sys
from models import User, Blog, Comment

@asyncio.coroutine
def test(loop):
    yield from orm.create_pool(loop=loop, user='www-data', password='www-data', db='awesome')
    
    u = User(name='Test123', email='test123@example.com', passwd='test123', image='about:blank')
    
    yield from u.save()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test(loop))
    loop.close()
    if loop.is_closed():
        sys.exit(0)