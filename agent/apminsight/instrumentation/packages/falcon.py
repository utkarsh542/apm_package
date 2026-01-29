   
from apminsight import constants

from apminsight.instrumentation.wrapper import wsgi_wrapper, default_wrapper

    
module_info = {
    "falcon.api": [{
        constants.class_str: "API",
        constants.method_str: "__call__",
        constants.wrapper_str:wsgi_wrapper,
        constants.component_str:constants.falcon_comp,
    },{
        constants.class_str: "API",
        constants.method_str: "_handle_exception",
        constants.wrapper_str: default_wrapper,
        constants.component_str:constants.falcon_comp,
    }],
    "falcon.app": [{
        constants.class_str: "App",
        constants.method_str: "__call__",
        constants.wrapper_str:wsgi_wrapper,
        constants.component_str:constants.falcon_comp,
    },{
        constants.class_str: "App",
        constants.method_str: "_handle_exception",
        constants.wrapper_str:default_wrapper,
        constants.component_str:constants.falcon_comp,
    }],
    "falcon.routing.util": [{
        constants.method_str: "map_http_methods",
        constants.wrapper_str:default_wrapper,
        constants.component_str:constants.falcon_comp,
    },{
        constants.method_str: "create_http_method_map",
        constants.wrapper_str:default_wrapper,
        constants.component_str:constants.falcon_comp,
    }]
}