from marshmallow import Schema, fields, validate


class UrlSchema(Schema):
    cdn = fields.Str(required=True)


class PluginSchema(Schema):
    enabled = fields.Bool(required=True)
    key = fields.Str(required=True)
    url = fields.Nested(UrlSchema, required=True)
    layout = fields.Str(required=True)
    type = fields.Str(required=False, validate=validate.OneOf(["utility", "widget"]))
    priority = fields.Int(required=False)
    route = fields.Str(required=False)
    containerClassName = fields.Str(required=False)


class UiPluginsSchema(Schema):
    name = fields.Str(required=True)
    manifestSpec = fields.Str(required=True, validate=validate.OneOf(["v1"]))
    plugins = fields.Dict(
        keys=fields.Str(),
        values=fields.Nested(PluginSchema),
        required=True
    )
    featureFlags = fields.Dict(
        keys=fields.Str(),
        values=fields.Bool(),
        required=False
    )
