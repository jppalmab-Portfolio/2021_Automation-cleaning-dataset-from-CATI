for file_name in os.listdir('00 data'):
    df = pd.read_csv('00 data/' + file_name, sep=",")

file_name = file_name.replace(".csv", "")

name_variable = input("Enter the variable name: ")

strings = df[name_variable]