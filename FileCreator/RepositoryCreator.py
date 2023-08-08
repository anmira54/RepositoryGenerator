import Constants.Environment as environment

def create_interface_file(table):
    with open(f"{environment.repositoryFolder}/{table}Repository.cs" ,'w') as file:
        file.write(f"using {environment.baseRepositoryNamespace};\n")
        file.write(f"using {environment.interfaceNamespace};\n")
        file.write(f"using {environment.modelsNamespace};\n")
        file.write(f"namespace {environment.repositoryNamespace} \n{{\n")
        file.write(f"\tpublic class {table}Repository : BaseRepository<{table}>, I{table}Repository \n\t{{\n")
        file.write(f"\t\tpublic {table}Repository({environment.context} context) : base(context) {{  }}\n")
        file.write("\t}\n")
        file.write("}")
