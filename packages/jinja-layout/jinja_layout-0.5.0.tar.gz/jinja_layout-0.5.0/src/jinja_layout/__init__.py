from jinja2 import nodes, lexer
from jinja2.ext import Extension


class LayoutExtension(Extension):
    tags = set(["use_layout"])

    def __init__(self, environment):
        super(LayoutExtension, self).__init__(environment)
        environment.extend(default_layout="layout.html", default_layout_block="content")

    def parse(self, parser):
        lineno = next(parser.stream).lineno
        template = None
        block_name = self.environment.default_layout_block
        if not parser.stream.current.test("block_end"):
            template = parser.parse_expression()
            if parser.stream.skip_if("comma"):
                block_name = parser.parse_expression().name

        if not template:
            template = nodes.Const(self.environment.default_layout)

        parser.stream.skip_if("comma")
        parser.stream.expect("block_end")
        # parse remaining tokens until EOF
        body = parser.subparse()
        # the parser expects a TOKEN_END_BLOCK after an
        # extension. fake this token and set the token
        # stream iterator with a single EOF token
        parser.stream.current = lexer.Token(1, lexer.TOKEN_BLOCK_END, "%}")
        parser.stream._iter = iter([lexer.Token(1, lexer.TOKEN_EOF, "")])

        macros = []
        blocks = []
        wrap_block = True
        wrap_nodes = []
        # extracts blocks node out of the body
        for node in body:
            if isinstance(node, nodes.Block):
                if node.name == block_name:
                    wrap_block = False
                blocks.append(node)
            elif isinstance(node, nodes.Macro):
                # we don't keep macros in blocks
                macros.append(node)
            else:
                wrap_nodes.append(node)
        if wrap_block and wrap_nodes:
            # wrap nodes which were not wrapped in a block node
            blocks.append(nodes.Block(block_name, wrap_nodes, False, True, lineno=lineno))

        return [nodes.Extends(template, lineno=lineno)] + macros + blocks


class BaseJinjaBlockAsStmtExtension(Extension):
    def parse(self, parser):
        lineno = parser.stream.__next__().lineno
        body = parser.parse_statements(["name:" + self.end_tag], drop_needle=True)
        return nodes.Block(self.block_name, body, False, lineno=lineno)


def create_jinja_block_as_stmt_extension(name, tagname=None, classname=None):
    """Creates a fragment extension which will just act as a replacement of the
    block statement.
    """
    if tagname is None:
        tagname = name
    if classname is None:
        classname = f"{name.capitalize()}BlockFragmentExtension"
    return type(
        classname,
        (BaseJinjaBlockAsStmtExtension,),
        {"tags": set([tagname]), "end_tag": "end" + tagname, "block_name": name},
    )
