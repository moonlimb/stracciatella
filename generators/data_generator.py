
TEST_CLEANED_DATA = lambda field: "{0}=self.cleaned_data['{0}'],".format(field)
CLEANED_DATA = lambda field: "cleaned_data['{}'],".format(field)
VALID_DATA = lambda field: "'{}': '',".format(field)
OPTIONS_DATA = lambda field: "{0}=options.{0},".format(field)

TAB = '    '

def create_valid_data(form_fields, indent_depth):
    """
    Given a form name (of create type), return as a string valid_data dict to be used for test_forms; each field
    maps to empty str

    :param form_fields: fields user inputed via form 
    :param indent_depth: indentation level
    :returns: returns namedtuple filled with values from cleaned_data.

    Ex. options_generator('SequencingRunCreate', fields, {'user_email': 'moon.limb@invitae.com})
            -> returns SequencingRunCreateOptions using given fields
    """
    line_and_indent = '\n' + TAB * (indent_depth + 1)
    valid_fields = [VALID_DATA(field) for field in form_fields]
    data = line_and_indent.join(valid_fields)
    header = '{0}self.valid_data = '.format(TAB * indent_depth) + r'{'+ line_and_indent
    footer = '{}'.format(line_and_indent + r'}')
    return '{0}{1}{2}'.format(header, data, footer)


def create_options_data(form_class, non_field_params, form_fields, indent_depth):
    line_and_indent = '\n' + '\t'*(indent_depth+1)
    all_params = non_field_params + [OPTIONS_DATA(field) for field in form_fields]
    options = line_and_indent.join(all_params)
    return '{0}{1}{2}'.format(TAB, options, ')')


def create_options_tuple(form_class, more_params, form_fields):
    options_params = more_params + form_fields
    return "{0}Options = namedtuple('{0}Options', {1})".format(form_class, options_params)


def create_test_cleaned_data(form_class, non_field_params, fields, indent_depth):
    line_and_indent = '\n' + '\t'*(indent_depth+1)
    all_params = non_field_params + [TEST_CLEANED_DATA(field) for field in fields]
    options = line_and_indent.join(all_params)
    header =  '{0}opts = {1}Options({2}'.format('\t'*indent_depth, form_class, line_and_indent)
    return '{0}{1}{2}'.format(header, options, ')')

def create_cleaned_data(form_class, non_field_params, fields, indent_depth):
    """
    Given a form name (of create type), a list of fields and optional additional parameters, generates CreateOptions
    tuple for the given form

    :param form_class: name of a form class as a string
    :param non_field_params: additional parameters for the CreateOptions tuple
    :param fields: fields user inputed via form_class
    :returns: returns namedtuple filled with values from cleaned_data.

    Ex. options_generator('SequencingRunCreate', fields, {'user_email': 'moon.limb@invitae.com})
            -> returns SequencingRunCreateOptions using given fields
    """

    line_and_indent = '\n' + '\t'*(indent_depth+1)
    all_params = non_field_params + [CLEANED_DATA(field) for field in fields]
    options = line_and_indent.join(all_params)
    header =  '{0}opts = {1}Options({2}'.format('\t'*indent_depth, form_class, line_and_indent)
    return '{0}{1}{2}'.format(header, options, ')')

