import mongoengine as me

class Makes(me.Document):
    name = me.StringField()
    image_url = me.StringField()
    models = me.ListField(me.ReferenceField("Cars"))

class Cars(me.Document):
    model = me.StringField()
    image_url = me.StringField()