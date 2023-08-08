import Constants.Environment as environment

def create_interface_file(table):
    with open(f"{environment.interfaceFolder}/I{table}Repository.cs" ,'w') as file:
        file.write(f"using {environment.baseInterfaceNamespace};\n")
        file.write(f"using {environment.modelsNamespace};\n\n")
        file.write(f"namespace {environment.interfaceNamespace} \n{{\n")
        file.write(f"\tpublic interface I{table}Repository : IBaseRepository<{table}> \n\t{{\n")
        file.write("\t}\n")
        file.write("}")
