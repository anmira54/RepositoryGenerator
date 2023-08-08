import Constants.Environment as environment

def modified_context_file(table, content):
    with open(f"{environment.contextFile}", "r") as archivo:
        lineas = archivo.readlines()

    with open(f"{environment.contextFile}", "w") as archivo:
        isDbSetInserted = False
        isModelBuilderInserted = False
        for linea in lineas:
            if linea.startswith("        public virtual DbSet") and isDbSetInserted == False:
                archivo.write(f"\t\tpublic virtual DbSet<{table}> {table} {{get; set;}}\n")
                isDbSetInserted = True
            if linea.startswith("            modelBuilder.Entity") and isModelBuilderInserted == False:
                keys = []
                for i in content:
                    if(i["is_primary_key"]):
                        keys.append(i["column_name"])
                
                archivo.write(f"\t\t\tmodelBuilder.Entity<{table}>(entity => \n")
                archivo.write(f"\t\t\t{{\n")
                archivo.write("\t\t\t\tentity.HasKey(e => new {")
                archivo.write(" ".join([f"e.{key}," for key in keys]))
                archivo.write("});\n")
                archivo.write("\t\t\t});\n\n")
                isModelBuilderInserted = True
            archivo.write(linea)

