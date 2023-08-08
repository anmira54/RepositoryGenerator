from dotenv import load_dotenv
import os

load_dotenv()

server = os.getenv('SERVER')
database = os.getenv('DATABASE')
username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')

modelFolder = os.getenv('MODELFOLDER')
interfaceFolder = os.getenv('INTERFACEFOLDER')
repositoryFolder = os.getenv('REPOSITORYFOLDER')
modelsNamespace = os.getenv('MODELNAMESAPCE')
interfaceNamespace = os.getenv('INTERFACENAMESPACE')
repositoryNamespace = os.getenv('REPOSITORYNAMESPACE')
baseRepositoryNamespace = os.getenv("BASEREPOSITORYNAMESPACE")
baseInterfaceNamespace = os.getenv("BASEINTERFACENAMESPACE")

context = os.getenv('CONTEXT')
contextFile = os.getenv('CONTEXTFILE')