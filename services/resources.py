# from sqlalchemy import Session
# from models import Resources
# from schemas import ResourceCreate

# class ResourcesService():
#     def __init__(self,db)-> None:
#         self.db = db

#     def create_resource(db: Session, resource: ResourceCreate, resoruce_id:int):
#         db_resource = Resources(**resource.dict(), resource_id=resoruce_id)
#         db.add(db_resource)
#         db.commit()
#         db.refresh(db_resource)
#         return db_resource

#     def get_resource_by_id(db: Session, id:int):
#         db_resource = db.query(Resources).filter(Resources.id == id).first()
#         return db_resource

#     def get_resources(db: Session):
#         db_resources = db.query(Resources).all()
#         return db_resources

#     def update_resource(db: Session, resource: Resources, id:int):
#         db_resource = db.query(Resources).filter(Resources.id == id).first()
#         db_resource.update(resource.dict())
#         db.commit()
#         db.refresh(db_resource)
#         return db_resource