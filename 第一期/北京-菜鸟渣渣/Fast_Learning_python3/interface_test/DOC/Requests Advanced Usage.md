# Requests 高级用法
<!--
![Requests](http://www.python-requests.org/en/master/_static/requests-sidebar.png) -->
![搬砖](https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1521017807024&di=4d43e54309a3dfa0f3c081cce5e5f02a&imgtype=0&src=http%3A%2F%2Fimg5.2345.com%2Fduoteimg%2FzixunImg%2Flocal%2F2017%2F07%2F13%2F14999222088018.jpg)
## 简介说明 : 
Requests是Python中优雅而简单的HTTP库，适用于人类；  
*Requests 支持 Python 2.6—2.7以及3.3—3.7，而且能在 PyPy 下完美运行。*
***
<!--
![Requests Icon](https://farm5.staticflickr.com/4263/35163665790_d182d84f5e_k_d.jpg)
-->
### Session 对象
会话对象允许您跨请求持久化某些参数。它还可以在所有来自会话实例的请求中保存cookie，并使用urllib3的连接池。因此，如果您向同一个主机发出多个请求，那么底层的TCP连接将被重用，这将会显著的提升性能 ;
[会话对象拥有主请求API的所有方法。](http://docs.python-requests.org/zh_CN/latest/api.html)

**在对象中持久化Cookies**
```Python
s = requests.Session()

s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
r = s.get('http://httpbin.org/cookies')

print(r.text)
# '{"cookies": {"sessioncookie": "123456789"}}'
```


>>会话还可以用于向请求方法提供默认数据。这是通过向会话对象的属性提供数据来完成的
```
s = requests.Session()
s.auth = ('user', 'pass')
s.headers.update({'x-test': 'true'})

# both 'x-test' and 'x-test2' are sent
s.get('http://httpbin.org/headers', headers={'x-test2': 'true'})
```
传递给请求方法的任何字典都将与设置的会话级别的值合并。


>>请注意; 即使使用会话，方法级参数也不会在请求之间持久化。这个示例只发送第一个请求的cookie，而不是第二个请:
```
s = requests.Session()

r = s.get('http://httpbin.org/cookies', cookies={'from-my': 'browser'})
print(r.text)
# '{"cookies": {"from-my": "browser"}}'

r = s.get('http://httpbin.org/cookies')
print(r.text)
# '{"cookies": {}}'
```
如果您想在会话中手动添加Cookie，可以使用Cookie工具函数来操作Session.cookies.。  
  

会话也可以用作上下文管理器:
```
with requests.Session() as s:
    s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')

#这将确保即使未处理的异常发生，也会立即关闭该会话。
```
  *从Dict参数中删除一个值。
有时，您需要从dict参数中省略会话级键。要做到这一点，只需在方法级参数中设置该键的值为None。它会自动被省略。  
  example:  {"from-my": "None"}*
  

### 请求(Request)和响应(Response) 对象
无论何时使用requests.get()发起一个请求，此事你正在做两件重要的事情。首先，您正在构造一个请求对象，该对象将被发送到服务器，以请求或查询某些资源。第二，当请求从服务器获得响应时，会生成一个响应对象。响应对象包含服务器返回的所有信息，还包含您最初创建的请求对象。这里有一个简单的请求，可以从维基百科的服务器获取一些非常重要的信息  

```
>>> r = requests.get('http://en.wikipedia.org/wiki/Monty_Python')
```

>> 如果我们想要访问服务器的头信息，我们会这样做:
```
>>> r.headers
{'content-length': '56170', 'x-content-type-options': 'nosniff', 'x-cache':
'HIT from cp1006.eqiad.wmnet, MISS from cp1010.eqiad.wmnet', 'content-encoding':
'gzip', 'age': '3080', 'content-language': 'en', 'vary': 'Accept-Encoding,Cookie',
'server': 'Apache', 'last-modified': 'Wed, 13 Jun 2012 01:33:50 GMT',
'connection': 'close', 'cache-control': 'private, s-maxage=0, max-age=0,
must-revalidate', 'date': 'Thu, 14 Jun 2012 12:59:39 GMT', 'content-type':
'text/html; charset=UTF-8', 'x-cache-lookup': 'HIT from cp1006.eqiad.wmnet:3128,
MISS from cp1010.eqiad.wmnet:80'}
```
*但是，如果我们想要获取我们发送给服务器的头信息，我们只需访问该请求:*
```
>>> r.request.headers
{'Accept-Encoding': 'identity, deflate, compress, gzip',
'Accept': '*/*', 'User-Agent': 'python-requests/1.2.0'}
```
### 请求准备
每当从API调用或会话调用中接收响应对象时，请求属性实际上就是所使用的PreparedRequest。在某些情况下，您可能希望在发送请求之前对body或header(或其他任何东西)做一些额外的工作。简单的方法如下:

```
from requests import Request, Session

s = Session()

req = Request('POST', url, data=data, headers=headers)
prepped = req.prepare()

# do something with prepped.body
prepped.body = 'No, I want exactly this as the body.'

# do something with prepped.headers
del prepped.headers['Content-Type']

resp = s.send(prepped,
    stream=stream,
    verify=verify,
    proxies=proxies,
    cert=cert,
    timeout=timeout
)

print(resp.status_code)
```
>>由于您没有对请求对象执行任何特殊操作，所以您可以立即准备并修改PreparedRequest对象。然后，您将发送到请求的其他参数 requests.* or Session.*.  

>>但是，上面的代码将丢失一些具有请求会话对象的优势。特别是，像cookie这样的会话级状态不会应用到您的请求中。要获得与该状态应用的PreparedRequest，请将调用替换为Request.prepare()，并调用Session.prepare_request()，如下所示:
```
from requests import Request, Session

s = Session()
req = Request('GET',  url, data=data, headers=headers)

prepped = s.prepare_request(req)

# do something with prepped.body
prepped.body = 'Seriously, send exactly these bytes.'

# do something with prepped.headers
prepped.headers['Keep-Dead'] = 'parrot'

resp = s.send(prepped,
    stream=stream,
    verify=verify,
    proxies=proxies,
    cert=cert,
    timeout=timeout
)

print(resp.status_code)
```


### SSL证书验证
验证HTTPS请求的SSL证书，就像web浏览器一样。默认情况下，启用SSL验证，如果无法验证证书，请求将抛出SSLError:
```
>>> requests.get('https://requestb.in')
requests.exceptions.SSLError: hostname 'requestb.in' doesn't match either of '*.herokuapp.com', 'herokuapp.com'
```

您可以使用可信CA的证书通过验证路径到CA_BUNDLE文件或目录。
```
>>> requests.get('https://github.com', verify='/path/to/certfile')
```
or
```
s = requests.Session()
s.verify = '/path/to/certfile'
```

*请注意
如果将验证设置为路径到目录，则该目录必须使用[OpenSSL](http://blog.sina.com.cn/s/blog_4c451e0e010143v3.html)提供的c_rehash实用程序处理。


还可以通过REQUESTS_CA_BUNDLE环境变量指定这个受信任的CAs列表。
如果您将验证设置为False，请求也可以忽略验证SSL证书:
```
>>> requests.get('https://kennethreitz.org', verify=False)
<Response [200]>
```
默认情况下，验证设置为True。选项验证只适用于主机证书。

### 客户端证书
您还可以指定本地证书作为客户端证书，作为单个文件(包含私钥和证书)或两个文件路径的tuple:
```
>>> requests.get('https://kennethreitz.org', cert=('/path/client.cert', '/path/client.key'))
<Response [200]>
```

  or

```
s = requests.Session()
s.cert = '/path/client.cert'
```

如果您指定了错误的路径或无效的证书，您将得到一个SSLError:
```
>>> requests.get('https://kennethreitz.org', cert='/wrong_path/client.pem')
SSLError: [Errno 336265225] _ssl.c:347: error:140B0009:SSL routines:SSL_CTX_use_PrivateKey_file:PEM lib
```

*本地证书的私钥必须是未加密的。目前，请求不支持使用加密密钥。*

### 长连接
在urllib3, keep-alive是100%自动在一个会话!您在会话中的任何请求都将自动重用适当的连接!

Streaming Uploads
请求支持流媒体上传，这允许您发送大的文件而不必将它们读入内存。要传输和上传，只需在body体提供一个类似文件的对象:
```
with open('massive-body', 'rb') as f:
    requests.post('http://some.url/streamed', data=f)
```

>>*Warning
强烈建议您以二进制模式打开文件。这是因为请求可能会尝试为您提供Content-Length的head，如果它执行这个值，那么将被设置为文件中bytes。如果以text mode打开文件，可能会出现错误.*

Chunk-Encoded 请求
请求还支持对传出和传入请求进行块传输编码。要发送一个chunk编码的请求，只需在body体提供一个生成器(或没有长度的任何迭代器):
```
def gen():
    yield 'hi'
    yield 'there'

requests.post('http://some.url/chunked', data=gen())
```
>>对于chunked编码响应，最好使用Response.iter_content()迭代数据。在理想情况下，您将在请求中设置stream=True ，在这种情况下，您可以通过调用iter_content，并使用chunk_size参数来迭代块。如果要设置块的最大大小，可以将chunk_size参数设置为任何整数。

### POST Multiple Multipart-Encoded Files
您可以在一个请求中发送多个文件。例如，假设您希望将图像文件上传到具有多个文件字段“iamges”的HTML表单中

```
<input type="file" name="images" multiple="true" required="true"/>
```
如果要这样做的话,只需将文件设置为元组或列表(form_field_name, file_info)

```
>>> url = 'http://httpbin.org/post'
>>> multiple_files = [
        ('images', ('foo.png', open('foo.png', 'rb'), 'image/png')),
        ('images', ('bar.png', open('bar.png', 'rb'), 'image/png'))]
>>> r = requests.post(url, files=multiple_files)
>>> r.text
{
  ...
  'files': {'images': 'data:image/png;base64,iVBORw ....'}
  'Content-Type': 'multipart/form-data; boundary=3131623adb2043caaeb5538cc7aa0b3a',
  ...
}

```
>>*Warning
强烈建议您以二进制模式打开文件。这是因为请求可能会尝试为您提供Content-Length的head，如果它执行这个值，那么将被设置为文件中bytes。如果以text mode打开文件，可能会出现错误.*

### 自定义的身份验证
请求允许您使用指定您自己的身份验证机制。

任何可调用的，作为对请求方法的auth参数传递的，将有机会在发送请求之前修改请求

身份验证是AuthBase的子类实现。请求中提供了两种常见的身份验证方案实现 ; :HTTPBasicAuth&ensp; HTTPDigestAuth。


假设我们有一个web服务，它只会在X-Pizza标头设置为密码值时才会响应。虽然这不太常用,但是我们仍然可以手工模拟一下;

```
from requests.auth import AuthBase

class PizzaAuth(AuthBase):
    """Attaches HTTP Pizza Authentication to the given Request object."""
    def __init__(self, username):
        # setup any auth-related data here
        self.username = username

    def __call__(self, r):
        # modify and return the request
        r.headers['X-Pizza'] = self.username
        return r
```

我们可以使用我们的Pizza Auth:验证一个要求:

```
>>> requests.get('http://pizzabin.org/admin', auth=PizzaAuth('kenneth'))
<Response [200]>
```

---
---

##  requests.api 源代码
```
request(method, url, params=None, data=None, headers=None, cookies=None, files=None, auth=None, timeout=None, allow_redirects=True, proxies=None, hooks=None, stream=None, verify=None, cert=None, json=None)[源代码见下文]

# Constructs a Request, prepares it and sends it. Returns Response object.
    参数:	
    method -- 指定构造一个request请求对象的方法
    url -- Request请求对象访问的URL.
    params -- (optional)请求发送的查询字符串通常封装为字典或字节。
    data -- (optional)在查询字符串中为请求发送的字典或字节。
    json -- (optional) 在主体中发送的json数据对象。
    headers -- (optional) HTTP报头的字典用以发送请求。
    cookies -- (optional)使用字段或CookieJar对象发送请求。
    files -- (optional)“filename”的字典:用于多部分编码上传的文件类对象。

    auth -- (optional) 可以启用基本/摘要/自定义HTTP Auth。
    timeout (float or tuple) -- (optional)在放弃发送之前等待服务器发送数据的时间，如浮点数或(连接超时，读取超时)元组。
    allow_redirects (bool) -- (optional) 默认设置为True。
    proxies -- (optional) 字典映射协议或协议和主机名到代理的URL。
    stream -- (optional) 是否立即下载响应内容。默认值为False。
    verify -- (optional) 布尔值，通常它控制我们是否验证服务器的TLS证书，或者字符串，在这种情况下，它必须是一个到CA bundle使用的路径。默认值为True。
    cert -- (optional) 如果是字符串，则路径是ssl client 端cert文件(.pem)。如果是Tuple， ('cert'， 'key')。
返回类型:  requests.Response
```


```
class requests.Response
响应对象，其中包含服务器对HTTP请求的响应。
apparent_encoding
由chardet库提供的显示编码。

close()
将连接释放回池。一旦这个方法被调用，底层的原始对象就不能再被访问了。

*Note: 通常不需要显式地调用。*

content
响应的内容，以字节为单位。

cookies = None
服务器返回的cookie

elapsed = None
发送请求和响应到达之间的时间间隔(作为时间增量)。该属性特别度量发送请求的第一个字节和结束解析头之间的时间。因此，它不受消费响应内容或流关键字参数值的影响。

encoding = None
编码在访问r.text时解码.

headers = None
不区分大小写的响应头字典。例如，header ['content-encoding']将返回'content-encoding'响应头的值。

history = None
来自请求历史记录的响应对象列表。任何重定向响应都将在这里结束。这个列表是按最早到最近的请求排序的。
is_permanent_redirect
如果此响应是重定向的永久版本之一，则为真。

is_redirect
如果这个响应是一个正确格式的HTTP重定向，那么它可以被自动处理(通过session .resolve_redirect)。
iter_content(chunk_size=1, decode_unicode=False)    

迭代响应数据。stream=True被设置为请求时，这就避免了将内容立即读取到内存中以获得较大的响应。块大小是它应该读入内存的字节数。这并不一定是返回的每个条目的长度。  

chunk_size必须为int类型或None类型。根据流的值，没有一个值会有不同的功能。stream=True将读取数据，当它到达任何大小的数据块时。如果流=False，数据将作为单个块返回。  

如果decode_unicode是正确的，那么将根据响应对内容进行解码。
iter_lines(chunk_size=512, decode_unicode=None, delimiter=None)

迭代响应数据，一次一行 . stream=True被设置为请求时，这就避免了将内容立即读取到内存中以获得较大的响应。
注解


json(**kwargs)    
返回响应的json编码的内容，如果有的话。 if any.

参数:	**kwargs -- Optional 可选参数,json.loads 加载需要
引发:	ValueError -- 入股响应体不是有效的json格式数据。
links
返回响应的解析头链接, if any.

next
返回在重定向链中的下一个请求的PreparedRequest
ok
如果status_code小于400，则返回True。

此属性检查响应的状态代码是否在400到600之间，以查看是否存在客户端错误或服务器错误。如果状态码在200到400之间，这将返回True。检查响应代码是否为200 OK。

raise_for_status()
抛出HTTPError异常

raw = None
响应的文件样对象表示(用于高级用法)。使用raw需要在请求中设置stream=True。
reason = None
响应HTTP状态的文本原因。, e.g. "Not Found" or "OK".

request = None
这是一个响应的PreparedRequest对象。

status_code = None
响应HTTP状态的整数代码。 e.g. 404 or 200.

text
以unicode形式,返回响应内容。


如果没有响应编码，编码将使用chardet进行猜测。  

响应内容的编码完全基于HTTP报头，遵从RFC 2616协议。您可以利用非http知识来更好地解析编码，那么应该设置r.encoding。在访问此属性之前进行适当的编码。

url = None
Final URL location of Response.
```




```
# -*- coding: utf-8 -*-

"""
requests.api


This module implements the Requests API.

:copyright: (c) 2012 by Kenneth Reitz.
:license: Apache2, see LICENSE for more details.
"""

from . import sessions


def request(method, url, **kwargs):
    """Constructs and sends a :class:`Request <Request>`.

    :param method: method for the new :class:`Request` object.
    :param url: URL for the new :class:`Request` object.
    :param params: (optional) Dictionary or bytes to be sent in the query string for the :class:`Request`.
    :param data: (optional) Dictionary or list of tuples ``[(key, value)]`` (will be form-encoded), bytes, or file-like object to send in the body of the :class:`Request`.
    :param json: (optional) json data to send in the body of the :class:`Request`.
    :param headers: (optional) Dictionary of HTTP Headers to send with the :class:`Request`.
    :param cookies: (optional) Dict or CookieJar object to send with the :class:`Request`.
    :param files: (optional) Dictionary of ``'name': file-like-objects`` (or ``{'name': file-tuple}``) for multipart encoding upload.
        ``file-tuple`` can be a 2-tuple ``('filename', fileobj)``, 3-tuple ``('filename', fileobj, 'content_type')``
        or a 4-tuple ``('filename', fileobj, 'content_type', custom_headers)``, where ``'content-type'`` is a string
        defining the content type of the given file and ``custom_headers`` a dict-like object containing additional headers
        to add for the file.
    :param auth: (optional) Auth tuple to enable Basic/Digest/Custom HTTP Auth.
    :param timeout: (optional) How many seconds to wait for the server to send data
        before giving up, as a float, or a :ref:`(connect timeout, read
        timeout) <timeouts>` tuple.
    :type timeout: float or tuple
    :param allow_redirects: (optional) Boolean. Enable/disable GET/OPTIONS/POST/PUT/PATCH/DELETE/HEAD redirection. Defaults to ``True``.
    :type allow_redirects: bool
    :param proxies: (optional) Dictionary mapping protocol to the URL of the proxy.
    :param verify: (optional) Either a boolean, in which case it controls whether we verify
            the server's TLS certificate, or a string, in which case it must be a path
            to a CA bundle to use. Defaults to ``True``.
    :param stream: (optional) if ``False``, the response content will be immediately downloaded.
    :param cert: (optional) if String, path to ssl client cert file (.pem). If Tuple, ('cert', 'key') pair.
    :return: :class:`Response <Response>` object
    :rtype: requests.Response

    Usage::

      >>> import requests
      >>> req = requests.request('GET', 'http://httpbin.org/get')
      <Response [200]>
    """

    # By using the 'with' statement we are sure the session is closed, thus we
    # avoid leaving sockets open which can trigger a ResourceWarning in some
    # cases, and look like a memory leak in others.
    with sessions.Session() as session:
        return session.request(method=method, url=url, **kwargs)



def get(url, params=None, **kwargs):
    r"""Sends a GET request.

    :param url: URL for the new :class:`Request` object.
    :param params: (optional) Dictionary or bytes to be sent in the query string for the :class:`Request`.
    :param \*\*kwargs: Optional arguments that ``request`` takes.
    :return: :class:`Response <Response>` object
    :rtype: requests.Response
    """

    kwargs.setdefault('allow_redirects', True)
    return request('get', url, params=params, **kwargs)



def options(url, **kwargs):
    r"""Sends an OPTIONS request.

    :param url: URL for the new :class:`Request` object.
    :param \*\*kwargs: Optional arguments that ``request`` takes.
    :return: :class:`Response <Response>` object
    :rtype: requests.Response
    """

    kwargs.setdefault('allow_redirects', True)
    return request('options', url, **kwargs)


def head(url, **kwargs):
    r"""Sends a HEAD request.

    :param url: URL for the new :class:`Request` object.
    :param \*\*kwargs: Optional arguments that ``request`` takes.
    :return: :class:`Response <Response>` object
    :rtype: requests.Response
    """

    kwargs.setdefault('allow_redirects', False)
    return request('head', url, **kwargs)



def post(url, data=None, json=None, **kwargs):
    r"""Sends a POST request.

    :param url: URL for the new :class:`Request` object.
    :param data: (optional) Dictionary (will be form-encoded), bytes, or file-like object to send in the body of the :class:`Request`.
    :param json: (optional) json data to send in the body of the :class:`Request`.
    :param \*\*kwargs: Optional arguments that ``request`` takes.
    :return: :class:`Response <Response>` object
    :rtype: requests.Response
    """

    return request('post', url, data=data, json=json, **kwargs)



def put(url, data=None, **kwargs):
    r"""Sends a PUT request.

    :param url: URL for the new :class:`Request` object.
    :param data: (optional) Dictionary (will be form-encoded), bytes, or file-like object to send in the body of the :class:`Request`.
    :param json: (optional) json data to send in the body of the :class:`Request`.
    :param \*\*kwargs: Optional arguments that ``request`` takes.
    :return: :class:`Response <Response>` object
    :rtype: requests.Response
    """

    return request('put', url, data=data, **kwargs)



def patch(url, data=None, **kwargs):
    r"""Sends a PATCH request.

    :param url: URL for the new :class:`Request` object.
    :param data: (optional) Dictionary (will be form-encoded), bytes, or file-like object to send in the body of the :class:`Request`.
    :param json: (optional) json data to send in the body of the :class:`Request`.
    :param \*\*kwargs: Optional arguments that ``request`` takes.
    :return: :class:`Response <Response>` object
    :rtype: requests.Response
    """

    return request('patch', url, data=data, **kwargs)



def delete(url, **kwargs):
    r"""Sends a DELETE request.

    :param url: URL for the new :class:`Request` object.
    :param \*\*kwargs: Optional arguments that ``request`` takes.
    :return: :class:`Response <Response>` object
    :rtype: requests.Response
    """

    return request('delete', url, **kwargs)

```


一、接口名称：

QQ号码测星运

二、接口描述：

接口地址：http://japi.juhe.cn/qqevaluate/qq  
返回格式：json  
请求方式：get post  
请求示例：http://japi.juhe.cn/qqevaluate/qq?key=您申请的appKey&qq=283340479  
接口备注：根据传入的参数qq号码和您申请的appKey测星运



三、请求参数说明（入参）：
<!--
| Tables        | Are           | Cool  |
| ------------- |:-------------:| -----:|
| col 3 is      | right-aligned | $1600 |
| col 2 is      | centered      |   $12 |
| zebra stripes | are neat      |    $1 |
-->


|名称	 | 必填 |    类型	 |     说明|
|-----|-----|----|-----|
|key|	    是	|   string|	  您申请的appKey|
|qq	|    是	|   string	  |需要测试的QQ号码|




四、 返回参数说明（出参）：
|名称|            类型   |    说明|
|----|----|----|
|error_code |    int	    | 返回状态码  |
|reason	      | string |   返回原因
|result	      | string	| 返回实体内容
|conclusion   |  string|    QQ号码测试结论
|analysis	  | string	| 结论分析



 
五、 JSON返回示例：
```
{
    "error_code": 0,//返回状态码
    "reason": "success",//返回原因
    "result": {//返回实体内容
        "data": {
            "conclusion": "[大吉+官运+财运+才艺]如龙得云，青云直上，智谋奋进，才略奏功",//QQ号码测试结论
            "analysis": "欲望难足希望高，计谋成功财力豪，猜疑嫉妒性自改，如龙乘云势运开。智能超人贯彻大志，富贵无比，不甘寂寞，叱吒风云之大吉数，但容易发生牢骚
及贪心、欲望太多而永不知足，为其缺点。切忌沉迷投机，可免贻误前程。"//结论分析
        }
    }
}
```
六、错误码参考：
服务级别错误代码参照(error_code) :

|错误码|说明 |  
 |------|------ |  
|       |                 |  
|216601|                       请求无结果返回 |  
|216602 |                      无qq参数或者格式不正确 |  
系统级错误码参照 : 
|错误码      |        说明     |
|----|-----|
|10001   |            错误的请求Key|
|10002  |             该key无请求权限|
|10003 |              KEY过期|
|10004|               错误的OPENID|
七、Python代码请求示例：

Appkey参数需要注册申请，才能调用，原接口地址：[https://www.juhe.cn/docs/api/id/166](https://www.juhe.cn/docs/api/id/166)

如果key参数不对，是不会请求成功的！

```
# coding:utf-8
import requests

url = "http://japi.juhe.cn/qqevaluate/qq"

par = {
      "key": "******************",  # appkey需要注册申请
      "qq":  "283340479"
       }

r = requests.get(url, params=par)
print(r.text)  # 打印文本
res = r.json()  # 返回的是json,用r.json解析器转成字典

# 字典取某个字段
conclusion = res["result"]["data"]["conclusion"]
print(conclusion)
analysis = res["result"]["data"]["analysis"]
print(analysis)


```
>>>选读部分 :
八、Java代码请求示例：
```
import java.io.BufferedReader;
import java.io.DataOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.UnsupportedEncodingException;
import java.net.HttpURLConnection;
import java.net.URL;
import java.net.URLEncoder;
import java.util.HashMap;
import java.util.Map;
 
import net.sf.json.JSONObject;
 
/**
*QQ号码测吉凶调用示例代码 － 聚合数据
*在线接口文档：http://www.juhe.cn/docs/166
**/
 
public class JuheDemo {
    public static final String DEF_CHATSET = "UTF-8";
    public static final int DEF_CONN_TIMEOUT = 30000;
    public static final int DEF_READ_TIMEOUT = 30000;
    public static String userAgent =  "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.66 Safari/537.36";
 
    //配置您申请的KEY
    public static final String APPKEY ="*************************";
 
    //1.QQ号码测吉凶 
    public static void getRequest1(){
        String result =null;
        String url ="http://japi.juhe.cn/qqevaluate/qq";//请求接口地址
        Map params = new HashMap();//请求参数
            params.put("key",APPKEY);//您申请的appKey
            params.put("qq","");//需要测试的QQ号码
 
        try {
            result =net(url, params, "GET");
            JSONObject object = JSONObject.fromObject(result);
            if(object.getInt("error_code")==0){
                System.out.println(object.get("result"));
            }else{
                System.out.println(object.get("error_code")+":"+object.get("reason"));
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
 
 
 
    public static void main(String[] args) {
 
    }
 
    /**
     *
     * @param strUrl 请求地址
     * @param params 请求参数
     * @param method 请求方法
     * @return  网络请求字符串
     * @throws Exception
     */
    public static String net(String strUrl, Map params,String method) throws Exception {
        HttpURLConnection conn = null;
        BufferedReader reader = null;
        String rs = null;
        try {
            StringBuffer sb = new StringBuffer();
            if(method==null || method.equals("GET")){
                strUrl = strUrl+"?"+urlencode(params);
            }
            URL url = new URL(strUrl);
            conn = (HttpURLConnection) url.openConnection();
            if(method==null || method.equals("GET")){
                conn.setRequestMethod("GET");
            }else{
                conn.setRequestMethod("POST");
                conn.setDoOutput(true);
            }
            conn.setRequestProperty("User-agent", userAgent);
            conn.setUseCaches(false);
            conn.setConnectTimeout(DEF_CONN_TIMEOUT);
            conn.setReadTimeout(DEF_READ_TIMEOUT);
            conn.setInstanceFollowRedirects(false);
            conn.connect();
            if (params!= null && method.equals("POST")) {
                try {
                    DataOutputStream out = new DataOutputStream(conn.getOutputStream());
                        out.writeBytes(urlencode(params));
                } catch (Exception e) {
                    // TODO: handle exception
                }
            }
            InputStream is = conn.getInputStream();
            reader = new BufferedReader(new InputStreamReader(is, DEF_CHATSET));
            String strRead = null;
            while ((strRead = reader.readLine()) != null) {
                sb.append(strRead);
            }
            rs = sb.toString();
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            if (reader != null) {
                reader.close();
            }
            if (conn != null) {
                conn.disconnect();
            }
        }
        return rs;
    }
 
    //将map型转为请求参数型
    public static String urlencode(Map<String,Object>data) {
        StringBuilder sb = new StringBuilder();
        for (Map.Entry i : data.entrySet()) {
            try {
                sb.append(i.getKey()).append("=").append(URLEncoder.encode(i.getValue()+"","UTF-8")).append("&");
            } catch (UnsupportedEncodingException e) {
                e.printStackTrace();
            }
        }
        return sb.toString();
    }
}
```


![imageICON](https://imgsa.baidu.com/forum/w%3D580/sign=3436a4eb942f07085f052a08d925b865/ac9486ed8a136327d13074979b8fa0ec09fac706.jpg)