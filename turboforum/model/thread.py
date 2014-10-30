from ming import schema as s
from ming.odm import FieldProperty, ForeignIdProperty, RelationProperty
from ming.odm.declarative import MappedClass
from session import DBSession
from auth import User
from tg import predicates, request

__all__ = ['Thread']

class Thread(MappedClass):
    """
    Section definition.
    """
    class __mongometa__:
        session = DBSession
        name = 'threads'
        indexes = [('_father',), ('created',)]

    _id = FieldProperty(s.ObjectId)
    display_name = FieldProperty(s.String)
    created = FieldProperty(s.DateTime)
    section = RelationProperty('Section')
    likes = FieldProperty(s.Int)
    content = FieldProperty(s.String)

    _author = ForeignIdProperty(User)
    author = RelationProperty(User)

    _father = FieldProperty(s.ObjectId, required=False)

    @property
    def father(self):
        if self._father:
            return Thread.query.get(_id=self._father)
        return None

    @property
    def can_be_viewed(self):
        return predicates.in_any_group(self.view).check_authorization(request.environ)

    @property
    def can_be_written(self):
        return predicates.in_any_group(self.write).check_authorization(request.environ)

    @property
    def can_be_moderated(self):
        return predicates.in_any_group(self.moderate).check_authorization(request.environ)

    @property
    def can_be_administered(self):
        return predicates.in_any_group(self.admin).check_authorization(request.environ)