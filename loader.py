from plugins import PluginRegistry

def load_plugin(name, action):
    registry = PluginRegistry()

    plugin = registry.get(name)
    if not plugin:
        return "Invalid plugin"

    handler = getattr(plugin, action, None)
    if not handler:
        return "Invalid action"

    return handler()
