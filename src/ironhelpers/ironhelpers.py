import os
import pandas as pd
import sys

from IPython.display import display, Markdown

def pprint(query, language='SQL'):
    '''
    Pretty print a query in an interactive python environment.

    The default language is SQL.
    '''
    if language.upper() == 'SQL':
        display(Markdown(f'''```mysql \n {query}```'''))
    else:
        display(f'{language} not yet supported.')
        
    return

def df_to_edges(df, entity, edge):
    '''
    Transform a dataframe into another dataframe
    suitable to work with graphs.
    '''
    graph_df = pd.merge(df, df, how='inner', on=edge)
    graph_df = graph_df.groupby([f'{entity}_x', f'{entity}_y']).count().reset_index()
    graph_df = graph_df.query(f'{entity}_x != {entity}_y')

    if type(edge) == list:
        graph_df = graph_df.loc[:, [entity + '_x', entity + '_y'] + edge]
    else:
        graph_df = graph_df.loc[:, [entity + '_x', entity + '_y', edge]]    

    return graph_df.rename(columns={f'{entity}_x':f'{entity}_src', 
                                    f'{entity}_y':f'{entity}_dest'})


def survival(data, group_field, time_field, event_field):
    '''
    Uses KaplanMeier to return the survival probabilities
    of a given group along a timeline.
    '''
    from lifelines import KaplanMeierFitter
    
    model = KaplanMeierFitter()
    results = []
    
    for i in data.loc[:, group_field].unique():
        group = data[data[group_field]==i]
        T = group[time_field]
        E = group[event_field]
        model.fit(T, E, label=str(i))
        results.append(model.survival_function_)

    survival = pd.concat(results, axis=1)
    return survival
