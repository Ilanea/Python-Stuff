import igraph
from igraph import Graph, EdgeSeq
import plotly.graph_objects as go
import scipy.special

# Input of variables:
# EventCount - Number of Events per Draw
# EventProbability - Probability per Event
# DrawCount - Number of Draws
def get_variables():
    global EventCount
    global EventProbability
    global DrawCount

    EventCount_valid = False
    while not EventCount_valid:
        EventCount = input("Enter Number of Events per Draw: ")
        if EventCount.isdigit():
            EventCount_valid = True
            EventCount = int(EventCount)
        else:
            print("Integer number expected.")

    #EventProbability_valid = False
    #while not EventProbability_valid:
    #    EventProbability = input("Enter probability per Event: ")
    #    if validate(EventProbability):
    #        EventProbability_valid = True
    #    else:
    #        print("Fraction expected. (1/6)")

    DrawCount_valid = False
    while not DrawCount_valid:
        DrawCount = input("Enter the Number of Draws: ")
        if DrawCount.isdigit():
            DrawCount_valid = True
            DrawCount = int(DrawCount)
        else:
            print("Integer number expected.")

    EventProbability = 1/EventCount

# Check if input is a fraction and return true or false
def validate(s):
    values = s.split('/')
    return len(values) == 2 and all(i.isdigit() for i in values)


def print_tree(EventCount, EventProbability, DrawCount):

    def make_annotations(pos, text, font_size=10, font_color='rgb(250,250,250)'):
        L = len(pos)
        if len(text) != L:
            raise ValueError('The lists pos and text must have the same len')
        annotations = []
        count = 0
        for k in range(L):

            annotations.append(
                dict(
                    text=labels[count],
                    x=pos[k][0], y=2 * M - position[k][1],
                    xref='x1', yref='y1',
                    font=dict(color=font_color, size=font_size),
                    showarrow=False)
            )

            if count < 3:
                count += 1
            else:
                count = 1

        return annotations

    nr_vertices = 0

    for x in range(DrawCount+1):
        nr_vertices = nr_vertices + EventCount ** x

    v_label = list(map(str, range(nr_vertices)))
    G = Graph.Tree(nr_vertices, EventCount)
    lay = G.layout('tree')

    position = {k: lay[k] for k in range(nr_vertices)}
    Y = [lay[k][1] for k in range(nr_vertices)]
    M = max(Y)

    es = EdgeSeq(G)  # sequence of edges
    E = [e.tuple for e in G.es]  # list of edges

    L = len(position)
    Xn = [position[k][0] for k in range(L)]
    Yn = [2 * M - position[k][1] for k in range(L)]
    Xe = []
    Ye = []
    for edge in E:
        Xe += [position[edge[0]][0], position[edge[1]][0], None]
        Ye += [2 * M - position[edge[0]][1], 2 * M - position[edge[1]][1], None]

    labels = v_label

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=Xe,
                             y=Ye,
                             mode='lines',
                             line=dict(color='rgb(210,210,210)', width=1),
                             text=EventProbability,
                             hoverinfo='text'
                             ))
    fig.add_trace(go.Scatter(x=Xn,
                             y=Yn,
                             mode='markers',
                             name='bla',
                             marker=dict(symbol='circle-dot',
                                         size=25,
                                         color='#6175c1',  # '#DB4551',
                                         line=dict(color='rgb(50,50,50)', width=1)
                                         ),
                             text=labels,
                             hoverinfo='none',
                             opacity=0.8
                             ))

    axis = dict(showline=False,  # hide axis line, grid, ticklabels and  title
                zeroline=False,
                showgrid=False,
                showticklabels=False,
                )

    fig.update_layout(title='Tree Diagram',
                      annotations=make_annotations(position, v_label),
                      font_size=12,
                      showlegend=False,
                      xaxis=axis,
                      yaxis=axis,
                      #margin=dict(l=40, r=40, b=85, t=100),
                      hovermode='closest',
                      plot_bgcolor='rgb(248,248,248)'
                      )
    fig.show()





if __name__ == '__main__':
   get_variables()
   print_tree(EventCount, EventProbability, DrawCount)


