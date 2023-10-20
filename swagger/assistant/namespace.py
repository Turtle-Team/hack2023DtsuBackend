import swagger

assistant = swagger.api.namespace(name='assistant', path="/api/assistant")
assistant.default = ""
assistant.description = ""