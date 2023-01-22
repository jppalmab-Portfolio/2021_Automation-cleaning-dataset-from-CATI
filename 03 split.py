nombres = df.new_nombre.str.split(expand=True,)

result = pd.concat([df, nombres], axis=1).reindex(df.index)

result = result.fillna(value=np.nan)
result = result.fillna("")

for col in result.columns:
    print(col)

x=col

#result.head()

result["apellidos"]= result[0] + " " + result[1]


if x == 2:
    result["nombres"]= result[2]

elif x == 3:
    result["nombres"]= result[2] + " " + result[3]

elif x == 4:
    result["nombres"]= result[2] + " " + result[3] + " " + result[4]

elif x == 5:
    result["nombres"]= result[2] + " " + result[3] + " " + result[4] + " " + result[5]
    
elif x == 6:
    result["nombres"]= result[2] + " " + result[3] + " " + result[4] + " " + result[5] + " " + result[6]
    
elif x == 7:
    result["nombres"]= result[2] + " " + result[3] + " " + result[4] + " " + result[5] + " " + result[6] + " " + result[7]
    
elif x == 8:
    result["nombres"]= result[2] + " " + result[3] + " " + result[4] + " " + result[5] + " " + result[6] + " " + result[7] + " " + result[8]

elif x == 9:
    result["nombres"]= result[2] + " " + result[3] + " " + result[4] + " " + result[5] + " " + result[6] + " " + result[7] + " " + result[8] + " " + result[9]
    
elif x == 10:
    result["nombres"]= result[2] + " " + result[3] + " " + result[4] + " " + result[5] + " " + result[6] + " " + result[7] + " " + result[8] + " " + result[9]+ " " + result[10]
    
elif x == 11:
    result["nombres"]= result[2] + " " + result[3] + " " + result[4] + " " + result[5] + " " + result[6] + " " + result[7] + " " + result[8] + " " + result[9]+ " " + result[10]+ " " + result[11]
    
elif x == 12:
    result["nombres"]= result[2] + " " + result[3] + " " + result[4] + " " + result[5] + " " + result[6] + " " + result[7] + " " + result[8] + " " + result[9]+ " " + result[10]+ " " + result[11]+ " " + result[12]


#result.head()

#result["nombres"]= result[2] + " " + result[3] + " " + result[4] + " " + result[5] + " " + result[6] + " " + result[7] + " " + result[8] + " " + result[9]

