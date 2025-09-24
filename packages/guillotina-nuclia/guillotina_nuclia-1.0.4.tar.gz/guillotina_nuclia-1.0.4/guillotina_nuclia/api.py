from guillotina import configure
from guillotina.api.service import Service
from guillotina.component import query_utility
from guillotina.interfaces import IContainer
from guillotina.response import Response
from guillotina_nuclia.interfaces.chat import IChat
from guillotina_nuclia.utility import INucliaUtility


@configure.service(
    context=IChat,
    method="POST",
    permission="nuclia.Predict",
    name="@NucliaPredict",
    summary="Get a response",
    responses={"200": {"description": "Get a response", "schema": {"properties": {}}}},
    requestBody={
        "required": True,
        "content": {
            "application/json": {
                "schema": {
                    "properties": {
                        "question": {
                            "type": "string",
                            "description": "Question",
                            "required": True,
                        },
                    }
                }
            }
        },
    },
)
class PredictChat(Service):
    async def __call__(self):
        nuclia_utility = query_utility(INucliaUtility)
        payload = await self.request.json()
        return await nuclia_utility.predict_chat(
            question=payload["question"], chat=self.context
        )


@configure.service(
    context=IContainer,
    method="POST",
    permission="nuclia.Ask",
    name="@NucliaAsk",
    summary="Get a response",
    responses={"200": {"description": "Get a response", "schema": {"properties": {}}}},
    requestBody={
        "required": True,
        "content": {
            "application/json": {
                "schema": {
                    "properties": {
                        "question": {
                            "type": "string",
                            "description": "Question",
                            "required": True,
                        },
                    }
                }
            }
        },
    },
)
class Ask(Service):
    async def __call__(self):
        nuclia_utility = query_utility(INucliaUtility)
        payload = await self.request.json()
        return await nuclia_utility.ask(question=payload["question"])


@configure.service(
    context=IContainer,
    method="POST",
    permission="nuclia.Ask",
    name="@NucliaAskStream",
    summary="Get a response",
    responses={"200": {"description": "Get a response", "schema": {"properties": {}}}},
    requestBody={
        "required": True,
        "content": {
            "application/json": {
                "schema": {
                    "properties": {
                        "question": {
                            "type": "string",
                            "description": "Question",
                            "required": True,
                        },
                    }
                }
            }
        },
    },
)
class AskStream(Service):
    async def __call__(self):
        nuclia_utility = query_utility(INucliaUtility)
        payload = await self.request.json()
        resp = Response(
            status=200,
            headers={
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Credentials": "true",
                "Access-Control-Expose-Headers": "*",
            },
        )
        resp.content_type = "text/plain"
        await resp.prepare(self.request)
        async for line in nuclia_utility.ask_stream(question=payload["question"]):
            await resp.write(line)
        await resp.write(eof=True)
        return resp


@configure.service(
    context=IContainer,
    method="POST",
    permission="nuclia.Search",
    name="@NucliaSearch",
    summary="Get a response",
    responses={"200": {"description": "Get a response", "schema": {"properties": {}}}},
    requestBody={
        "required": True,
        "content": {
            "application/json": {
                "schema": {
                    "properties": {
                        "question": {
                            "type": "string",
                            "description": "Question",
                            "required": True,
                        },
                    }
                }
            }
        },
    },
)
class Search(Service):
    async def __call__(self):
        nuclia_utility = query_utility(INucliaUtility)
        payload = await self.request.json()
        return await nuclia_utility.search(question=payload["question"])


@configure.service(
    context=IContainer,
    method="POST",
    permission="nuclia.Find",
    name="@NucliaFind",
    summary="Get a response",
    responses={"200": {"description": "Get a response", "schema": {"properties": {}}}},
    requestBody={
        "required": True,
        "content": {
            "application/json": {
                "schema": {
                    "properties": {
                        "question": {
                            "type": "string",
                            "description": "Question",
                            "required": True,
                        },
                    }
                }
            }
        },
    },
)
class Find(Service):
    async def __call__(self):
        nuclia_utility = query_utility(INucliaUtility)
        payload = await self.request.json()
        return await nuclia_utility.find(question=payload["question"])
