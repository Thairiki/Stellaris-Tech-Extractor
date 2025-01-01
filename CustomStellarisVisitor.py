from antlr_output.stellarisVisitor import stellarisVisitor

def remove_quotes(text):
    if text.startswith('"') and text.endswith('"'):
        return text[1:-1]
    return text

class CustomStellarisVisitor(stellarisVisitor):
    def visitContent(self, ctx):
        result = {}
        for expr in ctx.expr():
            result.update(self.visit(expr))
        return result

    def visitExpr(self, ctx):
        # print(f"Visiting expr: {ctx.getText()}")
        result = {}
        for keyval_ctx in ctx.keyval():
            key, value = self.visit(keyval_ctx)

            if key in result:
                if isinstance(result[key], list):
                    result[key].append(value)
                else:
                    result[key] = [result[key], value]
            else:
                result[key] = value

        return result


    def visitKeyval(self, ctx):
        key = self.visit(ctx.key())
        value = self.visit(ctx.val())
        return key, value

    def visitKey(self, ctx):
        if ctx.id_():
            return self.visit(ctx.id_())
        elif ctx.attrib():
            return self.visit(ctx.attrib())
        return None

    def visitVal(self, ctx):
        if ctx.id_():
            return self.visit(ctx.id_())
        elif ctx.attrib():
            return self.visit(ctx.attrib())
        elif ctx.array():
            return self.visit(ctx.array())
        elif ctx.group():
            return self.visit(ctx.group())
        return None

    def visitAttrib(self, ctx):
        return remove_quotes(ctx.getText())

    def visitArray(self, ctx):
        # print(f"Visiting array: {ctx.getText()}")
        elements = []
        if ctx.array_elements():
            for id_node in ctx.array_elements().id_():
                elements.append(self.visit(id_node))

        return elements

    def visitGroup(self, ctx):
        result = {}
        for expr in ctx.expr():
            result.update(self.visit(expr))
        return result

    def visitId_(self, ctx):
        return remove_quotes(ctx.getText())

