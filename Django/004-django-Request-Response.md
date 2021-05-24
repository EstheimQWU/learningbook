# 004-django-Request-Response
## 001HttpRequest objects
### Attributes
`HttpRequest.scheme`

`HttpRequest.body`

`HttpRequest.path`

`HttpRequest.path_info`

`HttpRequest.method`

`HttpRequest.encoding`

`HttpRequest.content_params`

`HttpRequest.GET`

`HttpRequest.POST`

`HttpRequest.COOKIES`

`HttpRequest.FILES`

`HttpRequest.META`

`HttpRequest.headers`这是一个类似字典对象，通过访问这个对象可以获取头部报文。
```python
>>> request.headers['User-Agent']
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6)
```
```html
{{ request.headers.user_agent }}
```
### Attributes set by middleware

`HttpRequest.current_app`

`HttpRequest.urlconf`

`HttpRequest.exception_reporter_filter`

`HttpRequest.exception_reporter_class`

### Attributes set by application code

`HttpRequest.session`
A readable and writable, dictionary-like object that represents the current session.

`HttpRequest.site`

`HttpRequest.user`

### Methods
`HttpRequest.get_host()`

`HttpRequest.get_port()`

`HttpRequest.get_full_path()`

`HttpRequest.get_full_path_info()`

`HttpRequest.build_absolute_uri(location=None)`

`HttpRequest.get_signed_cookie(key, default=RAISE_ERROR, salt='', max_age=None)`

`HttpRequest.is_secure()`
Returns True if the request is secure; that is, if it was made with HTTPS.

`HttpRequest.accepts(mime_type)`

`HttpRequest.read(size=None)`

`HttpRequest.readline()`

`HttpRequest.readlines()`

`HttpRequest.__iter__()`

## 002QueryDict objects
The QueryDicts at request.POST and request.GET will be immutable when accessed in a normal request/response cycle. To get a mutable version you need to use QueryDict.copy().

### Methods



## 003HttpResponse objects
In contrast to HttpRequest objects, which are created automatically by Django, HttpResponse objects are your responsibility. Each view you write is responsible for instantiating, populating, and returning an HttpResponse.

The HttpResponse class lives in the django.http module.

通过使用HTTPRESPONSE对象可以设置返回的内容。

## 004JsonResponse objects
### Attributes
`HttpResponse.content`

`HttpResponse.charset`

`HttpResponse.status_code`

`HttpResponse.reason_phrase`

`HttpResponse.streaming`

`HttpResponse.closed`

### Methods

https://docs.djangoproject.com/en/3.1/ref/request-response/#id3


## 005JsonResponse objects
`class JsonResponse(data, encoder=DjangoJSONEncoder, safe=True, json_dumps_params=None, **kwargs)`

An HttpResponse subclass that helps to create a JSON-encoded response. It inherits most behavior from its superclass with a couple differences:

这是一个可以协助创建JSON格式响应报文的HttpResponse子类，但是有一些不同之处。

Its default Content-Type header is set to application/json.

Content-Type报文头属性默认设置为application/json

The first parameter, data, should be a dict instance. If the safe parameter is set to False (see below) it can be any JSON-serializable object.

第一个参数data，需要一个dict实例。

The encoder, which defaults to django.core.serializers.json.DjangoJSONEncoder, will be used to serialize the data. See JSON serialization for more details about this serializer.

The safe boolean parameter defaults to True. If it’s set to False, any object can be passed for serialization (otherwise only dict instances are allowed). If safe  is True and a non-dict object is passed as the first argument, a TypeError will be raised.

The json_dumps_params parameter is a dictionary of keyword arguments to pass to the json.dumps() call used to generate the response.

## 006StreamingHttpResponse objects

## 007FileResponse objects
