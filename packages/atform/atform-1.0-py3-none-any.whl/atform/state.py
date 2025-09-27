"""Global data storage.

This module stores all data, e.g. configuration and test content, accumulated
during execution of the user script(s). It is implemented as a set of
global variables initialized by a function, as opposed to direct assignment
in the module namespace, to support unit testing, which requires the entire
module to be reinitialized for each test case.

All access to storage attributes in this module must be by importing this
entire module like:

import state

state.<attr>

Do not import individual attributes with the from clause:

from state import <attr>

The reason is the from clause creates a reference to the underlying object
in the local namespace, which does not get reinitialized in init(), causing
unit test failure.
"""

import collections


def init():
    """Initializes all default values."""
    # Suppress this message as all global variables are initially created
    # by this function.
    # pylint: disable=global-variable-undefined

    # Names identifying which fields will be applied to the next test.
    global active_fields
    active_fields = set()

    # The user-defined copyright notice string.
    global copyright_
    copyright_ = None

    # Numeric ID assigned to the most recent test; stored as a list instead
    # of a tuple because items in this list are incremented as tests and
    # sections are created.
    global current_id
    current_id = [0]

    # All defined fields, keyed by name, and ordered as added by add_field().
    global fields
    fields = collections.OrderedDict()

    # Globally accessible labels.
    global labels
    labels = {}

    # Hash of the the user-specified logo image file.
    global logo_hash
    logo_hash = None

    # All tests keyed by ID tuple.
    global tests
    tests = {}

    # The current project information set by the most recent call to
    # set_project_info().
    global project_info
    project_info = {}

    # Reference category titles, keyed by label. Stored as an ordered
    # dictionary because the order the categories are created defines
    # the order they are listed in the output documents.
    global ref_titles
    ref_titles = collections.OrderedDict()

    # Section titles, keyed by ID tuple.
    global section_titles
    section_titles = {}

    # Signature titles, in the order they were defined.
    global signatures
    signatures = []

    # Mapping of image hash to ReportLab Image object.
    global images
    images = {}


init()
