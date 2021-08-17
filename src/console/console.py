# Standard Library
import os
import pprint
import re
import shutil
import sys

__all__ = ['console']

TERMINAL_COLUMNS, _ = shutil.get_terminal_size()
SEPERATOR_CHAR = '.'


class Console:
    """Console class holds the main functionality of console app."""

    valid_options = [
        'source',
        'indent',
        'width',
        'enabled',
        'seperator_char',
        'colored',
        'dir_colors',
        'out_color',
        'header_color',
        'footer_color',
        'basic',
        'writer',
    ]
    default_options = dict(
        indent=4,
        width=TERMINAL_COLUMNS,
        seperator_line='{source:{char}<{width}}',
        seperator_char=SEPERATOR_CHAR,
        colored=False,
        dir_colors=dict(keys='yellow', values='default'),
        out_color='yellow',
        header_color='green',
        footer_color='green',
        basic=True,
        writer=sys.stdout,
    )
    colors = dict(
        black=0,
        red=1,
        green=2,
        yellow=3,
        blue=4,
        magenta=5,
        cyan=6,
        white=7,
        default=8,
    )

    def __init__(self, **options):
        self.options = dict()

        for default_option in self.default_options:
            self.options.update(
                [(default_option, self.default_options.get(default_option))]
            )

        enabled = False
        if os.environ.get('ENABLE_CONSOLE', False):
            if os.environ.get('ENABLE_CONSOLE').lower() in ['1', 'yes', 'true']:
                enabled = True

        self.options.update(enabled=enabled)
        self.configure(**options)

    def configure(self, **options):
        for option in options:
            if option not in self.valid_options:
                raise Exception(f'{option} is not a valid option')
            self.options.update([(option, options.get(option))])

        self.options.update(seperator_char=self.options.get('seperator_char')[0])

    def __call__(self, *args, **options):
        self.configure(**options)
        if args and self.options.get('enabled'):
            self.out(args, **options)

    def dir(self, *args, **options):  # noqa: A003
        self.configure(**options)

        if not args or self.options.get('enabled') is False:
            return

        for arg in args:
            payload = dict()

            source_name = arg.__class__.__name__
            if source_name != 'type':
                source_name = f'instance of {source_name}'
            if hasattr(arg, '__name__'):
                source_name = arg.__name__

            source = f'{source_name} | {type(arg)}'

            dir_arg = dir(arg)
            all_dunders = list(filter(lambda i: i.startswith('_'), dir_arg))

            internal_methods = list(filter(lambda i: i.startswith('__'), all_dunders))
            private_methods = list(
                filter(lambda i: not i.startswith('_', 1), all_dunders)
            )
            public_attributes = list(filter(lambda i: not i.startswith('_'), dir_arg))

            if internal_methods:
                internal_methods.sort(key=str.casefold)
                payload.update(internal_methods=internal_methods)
            if private_methods:
                private_methods.sort(key=str.casefold)
                payload.update(private_methods=private_methods)
            if public_attributes:
                public_attributes.sort(key=str.casefold)
                payload.update(public_attributes=public_attributes)

            if hasattr(arg, '__dict__'):
                data_attributes = list(arg.__dict__.keys()).sort(key=str.casefold)
                payload.update(data_attributes=data_attributes)

            if hasattr(arg.__class__, '__dict__'):
                class_dict = arg.__class__.__dict__

                properties_list = list()
                static_methods_list = list()
                class_methods_list = list()
                methods_list = list()
                class_variables_list = list()

                for k in class_dict:
                    class_name = class_dict[k].__class__.__name__

                    if class_name == 'property':
                        properties_list.append(k)
                    if class_name == 'staticmethod':
                        static_methods_list.append(k)
                    if class_name == 'classmethod':
                        class_methods_list.append(k)

                    if not k.startswith('_'):
                        if class_name == 'function':
                            methods_list.append(k)
                        if class_name in ['int', 'str', 'list', 'dict', 'set']:
                            class_variables_list.append(k)

                if properties_list:
                    properties_list.sort(key=str.casefold)
                    payload.update(properties=properties_list)
                if static_methods_list:
                    static_methods_list.sort(key=str.casefold)
                    payload.update(static_methods=static_methods_list)
                if class_methods_list:
                    class_methods_list.sort(key=str.casefold)
                    payload.update(class_methods=class_methods_list)
                if methods_list:
                    methods_list.sort(key=str.casefold)
                    payload.update(methods=methods_list)
                if class_variables_list:
                    class_variables_list.sort(key=str.casefold)
                    payload.update(class_variables=class_variables_list)

            options.update(source=source)
            self.out(payload, **options)

    def out(self, elements, **options):
        source = self.options.get('source', 'n/a')

        if 'source' in options.keys():
            source = f"{source} : {options.pop('source')}"

        writer = self.options.get('writer')

        pretty_print = pprint.PrettyPrinter(
            indent=self.options['indent'],
            width=self.options['width'],
            compact=True,
            stream=writer,
        )

        header = self.options.get('seperator_line').format(
            source=f'[{source}]',
            char=self.options.get('seperator_char'),
            width=self.options.get('width'),
        )
        footer = self.options.get('seperator_char') * self.options.get('width')

        formated = pretty_print.pformat(elements)

        if self.options.get('colored') is True:
            out_color = self.colors.get(
                self.options.get('out_color', 'green'),
            )
            formated = f'\033[3{out_color}m{elements}\033[0m'

            if self.options.get('basic', True) is False:
                header_color = self.colors.get(
                    self.options.get('header_color', 'green'),
                    'green',
                )
                header = f'\033[3{header_color}m{header}\033[0m'

                footer_color = self.colors.get(
                    self.options.get('footer_color', 'green'),
                    'green',
                )
                footer = f'\033[3{footer_color}m{footer}\033[0m'

            key_color = self.colors.get(
                self.options.get('dir_colors').get('keys', 'yellow'),
                'yellow',
            )
            value_color = self.colors.get(
                self.options.get('dir_colors').get('values', 'white'),
                'white',
            )

            formated = re.sub(
                r"'(\w+)':",
                fr"\033[3{key_color}m'\1'\033[0m: \033[3{value_color}m",
                formated,
            )

        if self.options.get('basic', True) is False:
            writer.write(f'{header}\n')

        writer.write(f'{formated}\n')

        if self.options.get('basic', True) is False:
            writer.write(f'{footer}\n')


def console(**options):
    return Console(**options)
