# flake8: noqa

if __import__("typing").TYPE_CHECKING:
    # import apis into api package
    from numind.openapi_client_async.api.authentication_api import AuthenticationApi
    from numind.openapi_client_async.api.documents_api import DocumentsApi
    from numind.openapi_client_async.api.examples_api import ExamplesApi
    from numind.openapi_client_async.api.extraction_api import ExtractionApi
    from numind.openapi_client_async.api.files_api import FilesApi
    from numind.openapi_client_async.api.inference_api import InferenceApi
    from numind.openapi_client_async.api.jobs_api import JobsApi
    from numind.openapi_client_async.api.organizations_api import OrganizationsApi
    from numind.openapi_client_async.api.playground_api import PlaygroundApi
    from numind.openapi_client_async.api.project_management_api import (
        ProjectManagementApi,
    )
    from numind.openapi_client_async.api.default_api import DefaultApi

else:
    from lazy_imports import LazyModule, as_package, load

    load(
        LazyModule(
            *as_package(__file__),
            """# import apis into api package
from numind.openapi_client_async.api.authentication_api import AuthenticationApi
from numind.openapi_client_async.api.documents_api import DocumentsApi
from numind.openapi_client_async.api.examples_api import ExamplesApi
from numind.openapi_client_async.api.extraction_api import ExtractionApi
from numind.openapi_client_async.api.files_api import FilesApi
from numind.openapi_client_async.api.inference_api import InferenceApi
from numind.openapi_client_async.api.jobs_api import JobsApi
from numind.openapi_client_async.api.organizations_api import OrganizationsApi
from numind.openapi_client_async.api.playground_api import PlaygroundApi
from numind.openapi_client_async.api.project_management_api import ProjectManagementApi
from numind.openapi_client_async.api.default_api import DefaultApi

""",
            name=__name__,
            doc=__doc__,
        )
    )
