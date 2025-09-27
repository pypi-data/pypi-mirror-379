import asyncio

import uvicorn
from fastapi import FastAPI

from ttagent import Action, Post, TTAgent

app = FastAPI()


@app.get('/')
def read_root() -> dict[str, str]:
    return {'Hello': 'World'}


class MyAgent(TTAgent):
    async def on_startup(self) -> None:
        ''' Run webserver '''
        config = uvicorn.Config(app)
        loop = asyncio.get_running_loop()
        loop.create_task(uvicorn.Server(config=config).serve())

    async def post_handler(self, post: Post) -> None:
        self.log.info('Get post %s', str(post))

    async def action_handler(self, action: Action) -> None:
        self.log.info('Get action %s', str(action))


agent = MyAgent()
