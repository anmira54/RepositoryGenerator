import Constants.Environment as environment

def create_model_file(content, table):
    with open(f"{environment.modelFolder}/{table}.cs" ,'w') as file:
        file.write("using System;\n\n")
        file.write(f"namespace {environment.modelsNamespace} \n{{\n")
        file.write(f"\tpublic class {table} \n\t{{\n")
        for item in content:
            column_name = item['column_name']
            csharp_type = item['csharp_type']
            line = f"\t\tpublic {csharp_type} {column_name} {{get; set;}}\n"
            file.write(line)
        file.write("\t}\n")
        file.write("}")
