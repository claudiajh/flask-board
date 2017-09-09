from app.models.DocumentModel import DocumentModel
from app.models.UserModel import UserModel


def getDocumentUserQuery():
    return DocumentModel.query. \
        with_entities(DocumentModel.id,
                      DocumentModel.title,
                      DocumentModel.content,
                      DocumentModel.user_id,
                      UserModel.username,
                      DocumentModel.update_time,
                      DocumentModel.comment_count). \
        filter(DocumentModel.user_id == UserModel.id)
