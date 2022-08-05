import json

from Book_store.django_Redis import RedisService


class BookRedis:
    @classmethod
    def _save(cls, user: str, book_dict: dict):
        RedisService.set(str(user), json.dumps(book_dict))

    @classmethod
    def extract(cls, user):
        user = str(user)
        if not RedisService.get(user):
            return {}
        return json.loads(RedisService.get(user))

    @classmethod
    def update(cls, user: str, book_dict: dict):
        """
        saving Note data into redis
        key = user_id
        value = {note_1:{'id':1,'title':'note title',...},note_2:{'id':2,'title':'note title',...}}
        """
        existing_data = cls.extract(user)
        existing_data.update({book_dict['id']: book_dict})
        cls._save(user=user, book_dict=existing_data)
