import InformationGetter.ModelGetterDB as ModelGetter
import FileCreator.ModelCreator as ModelCreator
import FileCreator.InterfaceCreator as InterfaceCreator
import FileCreator.RepositoryCreator as RepositoryCreator
import FileCreator.ContextModifier as ContextModifier

def main():
    tabla = input("Digite el nombre de la tabla: ")
    results = ModelGetter.getInformationTable(tabla)
    if(results == []):
        raise Exception("Table not found")
    ModelCreator.create_model_file(results, tabla)
    InterfaceCreator.create_interface_file(tabla)
    RepositoryCreator.create_interface_file(tabla)
    ContextModifier.modified_context_file(tabla, results)
if __name__ == '__main__':
    main()
