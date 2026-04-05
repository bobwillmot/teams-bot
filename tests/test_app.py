import unittest

from aiohttp.test_utils import TestClient, TestServer

from app import app


class MessagesEndpointSmokeTest(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.server = TestServer(app)
        await self.server.start_server()
        self.client = TestClient(self.server)
        await self.client.start_server()

    async def asyncTearDown(self):
        await self.client.close()
        await self.server.close()

    async def test_messages_endpoint_rejects_get(self):
        response = await self.client.get("/api/messages")

        self.assertEqual(response.status, 405)
        self.assertEqual(response.headers.get("Allow"), "POST")


if __name__ == "__main__":
    unittest.main()