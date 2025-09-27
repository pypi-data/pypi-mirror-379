# TTAgent

Утилита для создания чат бота на базе SSE протокола.
Переподключается при сетевых сбоях или временного отключения сервера.
Для работы с АПИ, в т.ч. ответных постов, используется клиентская библиотека `ttclient`
(устанавливается как зависимость).


## INSTALL

Достаточно установить библиотеку ttagent

```
$ pip install ttagent
```


## CODE

Create `agent.py`

```python
from ttagent import Action, Post, TTAgent


class MyAgent(TTAgent):
    async def on_post(self, post: Post) -> None:
        ''' Вызывается, когда боту приходит пост '''
        post.user_id            # int, who send post
        post.user_unique_name   # str, who send post
        post.chat_id    # int, in what chat
        post.post_no    # int, post number
        post.team_id    # int | None, if chat from team
        post.text       # str, post text
        post.text_parsed    # list[dict], parsed post text
        post.attachments    # list[str], guids of attached files
        post.reply_no       # int, if post has reply to other post (number)
        post.reply_text     # str, if post has reply to other post (text)
        post.file_name      # str, if post is file filename here
        post.file_guid      # str, if post is file guid here

        # Отправляем ответ
        await self.client.send_post(post.chat_id, 'answer')

    async def on_action(self, action: Action) -> None:
        ''' Вызывается когда пользователь кликает по ссылке-экшену '''
        action.action   # str, action name
        action.params   # dict, params of action
        action.user_id          # int, who send post
        action.user_unique_name   # str, who send post
        action.chat_id    # int, in what chat
        action.post_no    # int, post number
        action.team_id    # int | None, if chat from team

    async def on_startup(self) -> None:
        '''
            Вызывается до подключения к потоку.
            Можно запустить веб-сервер или подключиться к БД.
        '''
        self.log.debug('Called on_startup handler')

    async def on_shutdown(self) -> None:
        '''
            Вызывается при завершении работы сервера.
            Можно корректно завершить работу с внешними ресурсами.
        '''
        self.log.debug('Called on_shutdown handler')

    async def on_connect(self) -> None:
        '''
            Открыто подключение к потоку, но сообщения еще не принимаются.
            Можно инициализировать/проверить ресурсы,
            которые могли отключиться за время простоя.
        '''
        self.log.debug('Called on_connect handler (retry: %s)', self._retry_counter)

    async def on_retry(self) -> None:
        '''
            Попытка переподключения к потоку, вызывается сразу после
            возникновения сбоя.
            Можно отправить уведомления в системы мониторинга.
        '''
        self.log.debug('Called on_retry handler (retry: %s)', self._retry_counter)
```


## RUN

`SECRET` given when bot created

`DOMAIN` of server hostname

```
SECRET=<...> API_HOST=<hostname> ttagent example.agent:MyAgent
```

Запуск с uvx простого агента.

Нужно создать файл окружения `cfg.env`

```
export DOMAIN=example.com
export SECRET=1ni...ph7
export PYTHONPATH=.
```

Запускаем

```
uvx --env-file cfg.env ttagent agent:MyAgent
```
