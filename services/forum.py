from operator import and_
from models.forum import Forum as ForumModel
from schemas.forum import Forum
# Access-Control-Allow-Origin: http://localhost:3000


class ForumService():
    def __init__(self,db) -> None:
        self.db = db

    def get_forum(self):
        result = self.db.query(ForumModel).all()
        return result
    
    def get_forum_by_id(self, id:int):
        result = self.db.query(ForumModel).filter (and_(ForumModel.id == id , ForumModel.status == True)).first()
        return result
    
    def get_forum_by_topic(self, topic:str):
        result = self.db.query(ForumModel).filter(ForumModel.topic == topic).first()
        return result
    
    def create_forum(self, forum:Forum):
        new_forum = ForumModel(
            id= forum.id,
            topic= forum.topic,
            message= forum.message
        )
        self.db.add(new_forum)
        self.db.commit()
        return
    
    def update_forum(self,id:int, data:Forum):
        forum = self.db.query(ForumModel).filter(ForumModel.id == id).first()
        forum.topic = data.topic
        forum.message= data.message
        return
    
    def update_forum_by_topic(self, topic:str, data:Forum):
        forum = self.db.query(ForumModel).filter(ForumModel.topic == topic).first()
        forum.message = data.message
        return
    
  
    def delete_forum(self, id:int):
        self.db.query(ForumModel).filter(ForumModel.id == id).delete()
        self.db.commit()
        return