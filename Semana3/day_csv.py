import csv

def data_procees(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            reader = csv.DictReader(file)
            studients = []
            
            for row in reader:
                nombre = row['Nombre']
                nota_1 = int(row['Nota_1'])
                nota_2 = int(row['Nota_2'])
                promedio = round(((nota_1 + nota_2) /2), 2)
                status = 'Ingreso' if promedio >= 15 else "No Ingreso"
                
                studients.append({
                    'Nombre' : nombre,
                    'Nota_1' : nota_1,
                    'Nota_2' : nota_2,
                    'Promedio' : promedio,
                    'Status' : status
                })
                
        with open(ouput_file, 'w', newline='') as file:
            fieldnames = ['Nombre', 'Nota_1', 'Nota_2', 'Promedio', 'Status']
            reader = csv.DictWriter(file, fieldnames=fieldnames)
            reader.writeheader()
            reader.writerows(studients)
            print("Se escribiio corefctamente")
    except FileNotFoundError:
        print("nO EXITE el archiuvo")
    except KeyError:
        print('Error de llaves')
    except Exception as e:
        print(f"An error occurred: {e}")
        
        
input_file = 'Semana3/calificaciones.csv'
ouput_file = 'Semana3/calificaciones_ouput.csv'

data_procees(input_file, ouput_file)