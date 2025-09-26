from pyPhases import PluginAdapter
from pyPhasesRecordloader import RecordLoader


class Plugin(PluginAdapter):
    def initPlugin(self):
        # self.project.loadConfig(self.project.loadConfig(pathlib.Path(__file__).parent.absolute().joinpath("config.yaml")))
        module = "pyPhasesRecordloaderSHHS"
        rlPath = f"{module}.recordLoaders"
        RecordLoader.registerRecordLoader("RecordLoaderSHHS", rlPath)
        RecordLoader.registerRecordLoader("SHHSAnnotationLoader", rlPath)
        shhsPath = self.getConfig("shhs-path")
        self.project.setConfig("loader.shhs.filePath", shhsPath)
        self.project.setConfig("loader.shhs.dataset.downloader.basePath", shhsPath)
        self.project.setConfig("loader.shhs2.dataset.downloader.basePath", shhsPath)
