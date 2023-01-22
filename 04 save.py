if not os.path.exists('01 output'):
    os.makedirs('01 output')

result.to_csv("01 output/"+file_name+"_compuestos.csv")