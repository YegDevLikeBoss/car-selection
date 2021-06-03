import marshmallow as ma

class MakeSummary(ma.Schema):
    name = ma.fields.String()
    image_url = ma.fields.String()