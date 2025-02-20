from fastapi import Response, Cookie, status, Header, APIRouter
from datetime import datetime, UTC
from typing import Annotated

from schema.post import PostIn
from views.post import PostOut

router = APIRouter(prefix='/posts')

fake_db = [
    {"title": "Criando uma aplicação com Djamgp", "date": datetime.now(UTC), "published": True},
    {"title": "Internacionalizando um app FastAPI", "date": datetime.now(UTC), "published": False},
    {"title": "Criando uma aplicação com Flask", "date": datetime.now(UTC), "published": True},
    {"title": "Internacionalizando um app Starlett", "date": datetime.now(UTC), "published": True}
    ]



@router.post('/', status_code=status.HTTP_201_CREATED, response_model=PostOut)
def create_post(post: PostIn):
    fake_db.append(post.model_dump())
    return post

@router.get('/', response_model=list[PostOut])
def read_posts(response: Response, published: bool, limit: int, skip: int = 0, ads_id: Annotated[str | None, Cookie()] = None,
user_agent: Annotated[str | None, Header()] = None):

    response.set_cookie(key='user', value='felipe' )
    print(f"Cookie: {ads_id}")
    print(f"User-agent: {user_agent}")
    return [post for post in fake_db[skip : skip + limit] if post['published'] is published]

@router.get('/{framework}', response_model=PostOut)
def read_framework_posts(framework: str):
    return {"posts": [{"title": f"Criando uma aplicação com {framework}", "date": datetime.now(UTC)},
                      {"title": f"Internacionalizando um app {framework}", "date": datetime.now(UTC)}
    ]}