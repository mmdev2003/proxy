import aiohttp
import requests


class RequestException(Exception):
    def __init__(self, status):
        self.status = status

    def __str__(self):
        if self.status == 500:
            return 'Server error'

        if self.status == 400:
            return 'Bad request'


class Client:
    def __init__(self, base_url):
        self.base_url = base_url

    async def async_get(
            self,
            url,
            cookies=None,
            headers=None,
            body=None
    ):
        response_data = {}
        async with aiohttp.ClientSession() as session:

            async with session.get(url, json=body, cookies=cookies, headers=headers) as res:

                if res.status == 500:
                    raise RequestException(500)

                if res.status == 400:
                    raise RequestException(400)

                try:
                    content = await res.read()
                    response_data["content"] = list(content)
                except Exception as e:
                    print(e)

                try:
                    response_data["cookies"] = dict(res.cookies)
                except:
                    pass

                try:
                    response_data["body"] = await res.json()
                except:
                    pass

                try:
                    response_data["headers"] = dict(res.headers)
                except:
                    pass

                return response_data

    async def async_post(
            self,
            url,
            body=None
    ):
        async with aiohttp.ClientSession() as session:

            async with session.post(url, json=body) as resp:

                if resp.status == 500:
                    raise RequestException(500)

                if resp.status == 400:
                    raise RequestException(400)
                return await resp.json()

    async def redirect_to_get(self, body):
        url = f'http://{self.base_url}/api/redirect/get'
        return await self.async_post(url, body=body)

    async def redirect_to_second_backend(self, body):
        url = f'http://{self.base_url}/api/capture'
        return await self.async_post(url, body=body)

    async def request_original_domain(self, path, body, headers, cookies):
        url = f'{self.base_url}{path}'
        return await self.async_get(url, cookies=cookies, headers=headers, body=body)
