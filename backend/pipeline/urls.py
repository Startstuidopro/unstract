from django.urls import path
from pipeline.constants import PipelineURL
from pipeline.views import PipelineViewSet
from rest_framework.urlpatterns import format_suffix_patterns

pipeline_list = PipelineViewSet.as_view(
    {
        "get": "list",
        "post": "create",
    }
)
pipeline_detail = PipelineViewSet.as_view(
    {
        "get": "retrieve",
        "put": "update",
        "patch": "partial_update",
        "delete": "destroy",
    }
)

pipeline_execute = PipelineViewSet.as_view({"post": "execute"})


urlpatterns = format_suffix_patterns(
    [
        path("pipeline/", pipeline_list, name=PipelineURL.LIST),
        path("pipeline/<uuid:pk>/", pipeline_detail, name=PipelineURL.DETAIL),
        path("pipeline/execute/", pipeline_execute, name=PipelineURL.EXECUTE),
    ]
)
