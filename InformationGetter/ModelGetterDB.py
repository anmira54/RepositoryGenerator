import InformationGetter.DBConnection as DBConnection
from Constants.Types import type_mapping

def getInformationTable(table):
    cursor = DBConnection.connection.cursor()

    query = f"""
    SELECT 
    c.COLUMN_NAME AS NombreColumna,
    c.DATA_TYPE AS TipoDato,
    CASE WHEN c.IS_NULLABLE = 'YES' THEN 1 ELSE 0 END AS EsNullable,
    ISNULL(i.is_primary_key, 0) AS EsPrimaryKey
    FROM 
        INFORMATION_SCHEMA.COLUMNS c
    LEFT JOIN 
        sys.index_columns ic ON ic.object_id = OBJECT_ID(c.TABLE_SCHEMA + '.' + c.TABLE_NAME) AND ic.column_id = c.ORDINAL_POSITION
    LEFT JOIN 
        sys.indexes i ON ic.object_id = i.object_id AND ic.index_id = i.index_id
    WHERE 
        c.TABLE_NAME = '{table}' AND 
        c.TABLE_SCHEMA = 'dbo' 
    ORDER BY 
        c.ORDINAL_POSITION
    """
    cursor.execute(query)
    rows = cursor.fetchall()
    results = []

    for row in rows:
        column_name = row[0]
        data_type = row[1]
        is_nullable = row[2]
        column_key = row[3]

        csharp_type = type_mapping.get(data_type, 'UNKNOWN')

        if is_nullable == True and csharp_type != 'string': 
            csharp_type += "?"

        column_info = {
            'column_name': column_name,
            'data_type': data_type,
            'csharp_type': csharp_type,
            'is_primary_key': column_key
        }

        results.append(column_info)
    DBConnection.connection.close()

    return results