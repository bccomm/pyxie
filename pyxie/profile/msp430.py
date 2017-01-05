from pyxie.model.pynodes.values import ProfilePyNode

import pyxie.model.functions

def initialise_external_function_definitions():

    # Update the actual profile functions/types

    for function in function_calls:
        pyxie.model.functions.profile_funcs[function] = function_calls[function]

    for t in types:
        pyxie.model.functions.profile_types[t] = types[t]


def populate_profile_context(context):
    return None

def initialise_profile(context):
    context.tag = "PROFILE:msp430"
    populate_profile_context(context)
    initialise_external_function_definitions()

