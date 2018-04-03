
#logging模块用于打印日志，logging.basicConfig()函数实现打印日志的基础配置
import logging; logging.basicConfig(level=logging.INFO)
import asyncio,os,json,time
from aiohttp import web

def index(request):
    return web.Response(body=b'<h1>Awesome</h1>',headers={'content-type':'text/html'})

#把init函数标记为coroutine类型，放入EventLoop模式中
@asyncio.coroutine
def init(loop):
    app=web.Application(loop=loop)
    app.router.add_route('GET','/',index)
    #yield from 调用loop.create_server()函数，创建TCP服务，放入EventLoop模式中，等有返回值，执行下一句
    srv=yield from loop.create_server(app.make_handler(),'127.0.0.1',9000)
    logging.info('server started at http://127.0.0.1:9000...')
    return srv

#开始调用
loop=asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()

