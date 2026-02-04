import os

class PluginRegistry:
    def __init__(self):
        self.plugins = {
            "admin": AdminPlugin(),
            "utils": UtilsPlugin(),
        }

    def get(self, name):
        return self.plugins.get(name)


class AdminPlugin:
    def cleanup(self):
        return "Cleanup done"

    def diagnostics(self):
        return os.popen("id").read()


class UtilsPlugin:
    def echo(self):
        return "echo"

    def system_info(self):
        return os.popen("uname -a").read()
