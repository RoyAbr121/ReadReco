from marshmallow import Schema, fields

class RecommendationRequestSchema(Schema):
    query = fields.Str(required=True)


class RecommendationResponseSchema(Schema):
    answer = fields.Str(required=True)

