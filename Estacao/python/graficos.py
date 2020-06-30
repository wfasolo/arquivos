import matplotlib.pyplot as plt
import plotly.offline as py
import plotly.graph_objs as go

def graf(corrigido):
    
    plt.plot(corrigido['hora'], corrigido['Temp'])
    plt.xticks(rotation=90)
    plt.show()
    plt.plot(corrigido['hora'], corrigido['Pres'])
    plt.xticks(rotation=90)
    plt.show()
    plt.plot(corrigido['hora'], corrigido['Umid'])
    plt.xticks(rotation=90)
    plt.show()

    trace = go.Scatter(x=corrigido['hora'],
                    y=corrigido['Temp'],
                    text=corrigido['Temp'],
                    textposition='top center',
                    mode='lines+markers+text',
                    showlegend=False)

    trace2 = go.Bar(x=corrigido['hora'],
                    y=corrigido['Temp'],
                    marker_color='LightBlue',
                    opacity=0.5,
                    showlegend=False
                    )

    data_temp = [trace, trace2]
    py.plot(data_temp)




# station_df.to_csv('estacao.csv')
# station_df.to_json('estacao.json',orient='records') # ou 'table'
# corrigido.to_json('corrigido.json',orient='records')
