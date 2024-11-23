import panel as pn
import param

CopyValueType = str
CopyValueTypes = (str,)


class CopyButton(pn.custom.PyComponent):
    value: CopyValueType = param.ClassSelector(class_=CopyValueTypes)
    _data = param.Parameter()
    _clicks = param.Integer()

    @param.depends("_clicks", watch=True)
    def _handle_clicks(self):
        value = self.value
        if isinstance(self.value, str):
            value = self.value
        else:
            msg = f"Value of type '{type(value)} is not supported."
            raise ValueError(msg)

        self._data = value
