from fastapi import status, APIRouter, Depends
from src.schemas.post import PostIn, PostUpdateIn
from src.views.post import PostOut
from src.services.post import PostService
from src.security import login_required

router = APIRouter(prefix='/posts', dependencies=[Depends(login_required)])

service = PostService()


@router.get('/', response_model=list[PostOut])
async def read_posts(published: bool, limit: int, skip: int = 0):
    # query = posts.select()
    # return await database.fetch_all(query)
    return await service.read_all(published=published, limit=limit, skip=skip)


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=PostOut)
async def create_post(post: PostIn):
    return {**post.model_dump(), 'id': await service.create(post)}


@router.get("/{id}")
async def read_post(id: int):
    # query = posts.select().where(posts.c.id == id)
    # return await database.fetch_one(query)
    return await service.read(id)


@router.patch("/{id}", response_model=PostOut)
async def update_post(id: int, post: PostUpdateIn):
    return await service.update(id=id, post=post)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT, response_model=None)
async def delete_post(id: int):
    await service.delete(id)
