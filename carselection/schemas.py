import marshmallow as ma

class MakeSummary(ma.Schema):
    name = ma.fields.String()
    image_url = ma.fields.String()

class Car(ma.Schema):
    model = ma.fields.String()
    image_url = ma.fields.String()
    recommended = ma.fields.List(ma.fields.Nested('Car'))

class Make(MakeSummary):
    models = ma.fields.List(ma.fields.Nested(Car))