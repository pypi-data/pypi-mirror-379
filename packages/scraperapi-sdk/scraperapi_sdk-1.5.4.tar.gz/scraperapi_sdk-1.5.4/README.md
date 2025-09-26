# ScraperAPI Python SDK
## Install 

```
pip install scraperapi-sdk
```


## Usage
```
from scraperapi_sdk import ScraperAPIClient

client = ScraperAPIClient("<API-KEY>")

# regular get request
content = client.get('https://amazon.com/')
# get request with premium
content = client.get('https://amazon.com/', params={'premium': True})

# post request
content = client.post('https://webhook.site/403e44ce-5835-4ce9-a648-188a51d9395d', headers={'Content-Type': 'application/x-www-form-urlencoded'}, data={'field1': 'data1'})

# put request
content = client.put('https://webhook.site/403e44ce-5835-4ce9-a648-188a51d9395d', headers={'Content-Type': 'application/json'}, data={'field1': 'data1'})
```

The `content` variable will contain the scraped page.

If you want to get the `Response` object instead of the content you can use `make_request`.

```
response = client.make_request(url='https://webhook.site/403e44ce-5835-4ce9-a648-188a51d9395d', headers={'Content-Type': 'application/json'}, data={'field1': 'data1'})
# response will be <Response [200]>
```

## Exception

```
from scraperapi_sdk import ScraperAPIClient
from scraperapi_sdk.exceptions import ScraperAPIException

client = ScraperAPIClient(
    api_key=api_key,
)
try:
    result = client.post('https://webhook.site/403e44ce-5835-4ce9-a648-188a51d9395d', headers={'Content-Type': 'application/x-www-form-urlencoded'}, data={'field1': 'data1'})
    _ = result
except ScraperAPIException as e:
    print(e.original_exception)  # you can access the original exception via `.original_exception` property.
```

## scrapyGet

To prepare a URL for scrapy you can use `client.scrapyGet` method.

```python

client.scrapyGet(url,
          headers={"header1": "value1"},
          country_code="us",
          premium=False,
          render=True,
          session_number=2772728518147,
          autoparse=None,
          )
```

All of the parameters except `url` are optional.

Full example:

```python
import scrapy
import os
from pathlib import Path
from scraperapi_sdk import ScraperAPIClient

client = ScraperAPIClient(
    api_key=os.getenv("SCRAPERAPI_API_KEY"),
)
class ExampleSpider(scrapy.Spider):
    name = ""

    async def start(self):
        urls = [
            "https://example.com/",
        ]
        for url in urls:
            yield scrapy.Request(url=client.scrapyGet(url, render=True, ), callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f"example-{page}.html"
        Path(filename).write_bytes(response.body)
        self.log(f"Saved file {filename}")

```
## Structured Data Collection Methods
### Amazon Endpoints
#### Amazon Product Page API

This method will retrieve product data from an Amazon product page and transform it into usable JSON.

```
result = client.amazon.product("<ASIN>")
result = client.amazon.product("<ASIN>", country="us", tld="com")
```

Read more in docs: [Amazon Product Page API](https://docs.scraperapi.com/making-requests/structured-data-collection-method/amazon-product-page-api)

#### Amazon Search API

This method will retrieve products for a specified search term from Amazon search page and transform it into usable JSON.

```
result = client.amazon.search("<QUERY>")
result = client.amazon.search("<QUERY>", country="us", tld="com")
```

Read more in docs: [Amazon Search API](https://docs.scraperapi.com/making-requests/structured-data-collection-method/amazon-search-api)

#### Amazon Offers API
This method will retrieve offers for a specified product from an Amazon offers page and transform it into usable JSON.

```
result = client.amazon.offers("<ASIN>")
result = client.amazon.offers("<ASIN>", country="us", tld="com")
```
Read more in docs: [Amazon Offers API](https://docs.scraperapi.com/making-requests/structured-data-collection-method/amazon-offers-api)


#### Amazon Prices API 

This method will retrieve product prices for the given ASINs and transform it into usable JSON.

```
result = client.amazon.prices(['<ASIN1>'])
result = client.amazon.prices(['<ASIN1>', '<ASIN2>'])
result = client.amazon.prices(['<ASIN1>', '<ASIN2>'], country="us", tld="com")
```
Read more in docs: [Amazon Prices API](https://docs.scraperapi.com/making-requests/structured-data-collection-method/amazon-prices-api)


### Google API
#### Google SERP API
This method will retrieve product data from an Google search result page and transform it into usable JSON.

```
result = client.google.search('free hosting')
result = client.google.search('free hosting', country="us", tld="com")
```
Read more in docs: [Google SERP API](https://docs.scraperapi.com/making-requests/structured-data-collection-method/google-serp-api)
#### Google News API
This method will retrieve news data from an Google news result page and transform it into usable JSON.
```
result = client.google.news('tornado')
result = client.google.news('tornado', country="us", tld="com")
```
Read more in docs: [Google News API](https://docs.scraperapi.com/making-requests/structured-data-collection-method/google-news-api)

#### Google Jobs API

This method will retrieve jobs data from an Google jobs result page and transform it into usable JSON.

```
result = client.google.jobs('Senior Software Developer')
result = client.google.jobs('Senior Software Developer', country="us", tld="com")
```
Read more in docs: [Google Jobs API](https://docs.scraperapi.com/making-requests/structured-data-collection-method/google-jobs-api)

#### Google Shopping API
This method will retrieve shopping data from an Google shopping result page and transform it into usable JSON.
```
result = client.google.shopping('macbook air')
result = client.google.shopping('macbook air', country="us", tld="com")
```

Read more in docs: [Google Shopping API](https://docs.scraperapi.com/making-requests/structured-data-collection-method/google-shopping-api)

### Walmart API
#### Walmart Search API
This method will retrieve product list data from Walmart as a result of a search.
```
result = client.walmart.search('hoodie')
result = client.walmart.search('hoodie', page=2)
```
Read more in docs: [Walmart Search API](https://docs.scraperapi.com/making-requests/structured-data-collection-method/walmart-search-api)

#### Walmart Category API

This method will retrieve Walmart product list for a specified product category.
```
result = client.walmart.category('5438_7712430_8775031_5315201_3279226')
result = client.walmart.category('5438_7712430_8775031_5315201_3279226', page=2)
```
Read more in docs: [Walmart Category API](https://docs.scraperapi.com/making-requests/structured-data-collection-method/walmart-category-api)

#### Walmart Product API
This method will retrieve Walmart product details for one product.
```
result = client.walmart.product('5053452213')
```

Read more in docs: [Walmart Product API](https://docs.scraperapi.com/making-requests/structured-data-collection-method/walmart-product-api)
## Async Scraping

Basic scraping:
```
from scraperapi_sdk import ScraperAPIAsyncClient, ScraperAPIException

client = ScraperAPIAsyncClient(api_key)
request_id = None
# request async scraping
try:
    job = client.create('https://example.com')
    request_id = job.get('id')
except ScraperAPIException as e:
    print(e.original_exception)

# if job was submitted successfully we can request the result of scraping 

if request_id:
    result = client.get(request_id)
```

Read more in docs: [How to use Async Scraping](https://docs.scraperapi.com/making-requests/async-requests-method/how-to-use)

### Webhook Callback
```
from scraperapi_sdk import ScraperAPIAsyncClient, ScraperAPIException

client = ScraperAPIAsyncClient(api_key)
request_id = None
# request async scraping
try:
    job = client.create('https://example.com', webhook_url="https://webhook.site/#!/view/c4facc6e-c028-4d9c-9f58-b14c92a381fe")
    request_id = job.get('id')
except ScraperAPIException as e:
    print(e.original_exception)

# if job was submitted successfully we can request the result of scraping 

if request_id:
    result = client.get(request_id)
```
### Wait for results
You can use wait method which will poll ScraperAPI for result until its ready.

Use `client.wait`

Arguments:
`request_id` (required): ID returned from `client.create` call
`cooldown` (optional, default=5): number of seconds between retries
`max_retries` (optional, default=10): Maximum number of retries 
`raise_for_exceeding_max_retries` (optional, default=False): If True will raise exception when reached max_retries, else returns the response from the API.

```
from scraperapi_sdk import ScraperAPIAsyncClient, ScraperAPIException

client = ScraperAPIAsyncClient(api_key)
request_id = None
# request async scraping
try:
    job = client.create('https://example.com')
    request_id = job.get('id')
except ScraperAPIException as e:
    print(e.original_exception)

# if job was submitted successfully we can request the result of scraping 

if request_id:
    result = client.wait(
        request_id,
        cooldown=5,
        max_retries=10,
        raise_for_exceeding_max_retries=False,
    )
```


### Amazon Async Scraping

#### Amazon Product

Scrape a single Amazon Product asynchronously:

```
from scraperapi_sdk import ScraperAPIAsyncClient, ScraperAPIException

client = ScraperAPIAsyncClient('<api_key>')
request_id = None
try:
    job = client.amazon.product('B0CHVR5K7C')
    request_id = job.get('id')
except ScraperAPIException as e:
    print(e.original_exception)
result = client.get(request_id)
```

Single Product with params:

```
from scraperapi_sdk import ScraperAPIAsyncClient, ScraperAPIException

client = ScraperAPIAsyncClient('<api_key>')
request_id = None
try:
    job = client.amazon.product('B0B5PLT7FZ', api_params=dict(country_code='uk', tld='co.uk'))
    request_id = job.get('id')
except ScraperAPIException as e:
    print(e.original_exception)
result = client.get(request_id)
```

Scrape multiple Amazon Products asynchronously with params:
```
from scraperapi_sdk import ScraperAPIAsyncClient, ScraperAPIException

client = ScraperAPIAsyncClient('<api_key>')
request_id = None
try:
    job = client.amazon.products(['B0B5PLT7FZ', 'B00CL6353A'], api_params=dict(country_code='uk', tld='co.uk'))
    request_id = job.get('id')
except ScraperAPIException as e:
    print(e.original_exception)
result = client.get(request_id)

```
Read more in docs: [Async Amazon Product Scraping](https://docs.scraperapi.com/making-requests/async-structured-data-collection-method/amazon-product-page-api-async)

#### Amazon Search
Search Amazon asynchronously
```
from scraperapi_sdk import ScraperAPIAsyncClient, ScraperAPIException

client = ScraperAPIAsyncClient('<api_key>')
request_id = None
try:
    job = client.amazon.search('usb c microphone')
    request_id = job.get('id')
except ScraperAPIException as e:
    print(e.original_exception)
result = client.get(request_id)
```

Search Amazon asynchronously with `api_params`
```
from scraperapi_sdk import ScraperAPIAsyncClient, ScraperAPIException

client = ScraperAPIAsyncClient('<api_key>')
request_id = None
try:
    job = client.amazon.search('usb c microphone', api_params=dict(country_code='uk', tld='co.uk')
    request_id = job.get('id')
except ScraperAPIException as e:
    print(e.original_exception)
result = client.get(request_id)
```
Read more in docs: [Amazon Review Scraping Async](https://docs.scraperapi.com/making-requests/async-structured-data-collection-method/amazon-search-api-async)
#### Amazon Offers for a Product
Scrape Amazon offers for a single product

```
from scraperapi_sdk import ScraperAPIAsyncClient, ScraperAPIException

client = ScraperAPIAsyncClient('<api_key>')
request_id = None
try:
    job = client.amazon.offers('B0CHVR5K7C')
    request_id = job.get('id')
except ScraperAPIException as e:
    print(e.original_exception)
result = client.get(request_id)

```
Scrape Amazon offers for multiple products
```
from scraperapi_sdk import ScraperAPIAsyncClient, ScraperAPIException

client = ScraperAPIAsyncClient('<api_key>')
request_id = None
try:
    jobs = client.amazon.offers('B0CHVR5K7C')
except ScraperAPIException as e:
    print(e.original_exception)
for job in jobs:
    result = client.get(job.get('id'))
```

#### Amazon Reviews
Scrape Reviews for a single product asynchronously:

```
from scraperapi_sdk import ScraperAPIAsyncClient, ScraperAPIException

client = ScraperAPIAsyncClient('<api_key>')
request_id = None
try:
    job = client.amazon.product('B0B5PLT7FZ'], api_params=dict(country_code='uk', tld='co.uk'))
    request_id = job.get('id')
except ScraperAPIException as e:
    print(e.original_exception)
result = client.get(request_id)
```


Scrape reviews for multiple products asynchronously:

```
from scraperapi_sdk import ScraperAPIAsyncClient, ScraperAPIException

client = ScraperAPIAsyncClient('<api_key>')
try:
    jobs = client.amazon.products(['B0B5PLT7FZ', 'B00CL6353A'], api_params=dict(country_code='uk', tld='co.uk'))
except ScraperAPIException as e:
    print(e.original_exception)
for job in jobs:
    result = client.get(job.get('id'))
```
Read more in docs: [Amazon Review Scraping Async](https://docs.scraperapi.com/making-requests/async-structured-data-collection-method/amazon-review-details-async)

### Google Async Scraping
#### Google Async Search Scraping

```
from scraperapi_sdk import ScraperAPIAsyncClient, ScraperAPIException

client = ScraperAPIAsyncClient('<api_key>')
try:
    jobs = client.google.search('solar eclipse')
except ScraperAPIException as e:
    print(e.original_exception)
for job in jobs:
    result = client.get(job.get('id'))
```


Read more in docs: [Google Search API (Async)](https://docs.scraperapi.com/making-requests/async-structured-data-collection-method/google-search-api-async)

#### Google Async News Scraping

```
from scraperapi_sdk import ScraperAPIAsyncClient, ScraperAPIException

client = ScraperAPIAsyncClient('<api_key>')
try:
    jobs = client.google.news('solar eclipse')
except ScraperAPIException as e:
    print(e.original_exception)
for job in jobs:
    result = client.get(job.get('id'))
```
Read more in docs: [Google News API (Async)](https://docs.scraperapi.com/making-requests/async-structured-data-collection-method/google-news-api-async)

#### Google Async Jobs Scraping
```
from scraperapi_sdk import ScraperAPIAsyncClient, ScraperAPIException

client = ScraperAPIAsyncClient('<api_key>')
try:
    jobs = client.google.jobs('senior software developer')
except ScraperAPIException as e:
    print(e.original_exception)
for job in jobs:
    result = client.get(job.get('id'))
```
Read more in docs: [Google Jobs API (Async)](https://docs.scraperapi.com/making-requests/async-structured-data-collection-method/google-jobs-api-async)

#### Google Async Shopping Scraping
```
from scraperapi_sdk import ScraperAPIAsyncClient, ScraperAPIException

client = ScraperAPIAsyncClient('<api_key>')
try:
    jobs = client.google.shopping('usb c microphone')
except ScraperAPIException as e:
    print(e.original_exception)
for job in jobs:
    result = client.get(job.get('id'))
```
Read more in docs: [Google Shopping API (Async)](https://docs.scraperapi.com/making-requests/async-structured-data-collection-method/google-shopping-api-async)



