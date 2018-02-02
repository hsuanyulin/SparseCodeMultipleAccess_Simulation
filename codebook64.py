import numpy as np
import cmath

#plot
from plotly import tools
import plotly.plotly as py
import plotly.graph_objs as go
tools.set_credentials_file(username='hsuanyulin', api_key='1PqaCssxL1WLP06PnL6p')

#plot
import matplotlib.pyplot as plt

#factorGraph
import config


def constant(f):
    def fset(self, value):
        raise TypeError
    def fget(self):
        return f()
    return property(fget, fset)

class _Codebok(object):
    @constant
    def USER1():
        return np.array([[0.7851, -0.2243, 0.2243, -0.7851], [0, 0, 0, 0], [-0.1815-0.1318j, -0.6351-0.4615j, 0.6351+0.4615j, 0.1815+0.1318j], [0, 0, 0, 0]]);
    @constant
    def USER2():
        return np.array([[0, 0, 0, 0], [-0.1815-0.1318j, -0.6351-0.4615j, 0.6351+0.4615j, 0.1815+0.1318j], [0, 0, 0, 0], [0.7851, -0.2243, 0.2243, -0.7851]]);
    @constant
    def USER3():
        return np.array([[-0.6351+0.4615j, 0.1815-0.1318j, -0.1815+0.1318j, 0.6351-0.4615j], [0.1392-0.1759j, 0.4873-0.6156j, -0.4873-0.6156j, -0.1392+0.1759j], [0, 0, 0, 0], [0, 0, 0, 0]]);
    @constant
    def USER4():
        return np.array([[0, 0, 0, 0], [0, 0, 0, 0], [0.7851, -0.2243, 0.2243, -0.7851], [-0.0055-0.2242j, -0.0193-0.7848j, 0.0193+0.7848j, 0.0055+0.2242j]]);
    @constant
    def USER5():
        return np.array([[-0.0055-0.2242j, -0.0193-0.7848j, 0.0193+0.7848j, 0.0055+0.2242j], [0, 0, 0, 0], [0, 0, 0, 0], [-0.6351+0.4615j, 0.1815-0.1318j, -0.1815+0.1318j, 0.6351-0.4615j]]);
    @constant
    def USER6():
        return np.array([[0, 0, 0, 0], [0.7851, -0.2243, 0.2243, -0.7851], [0.1392-0.1759j, 0.4873-0.6156j, -0.4873+0.6156j, -0.1392+0.1759j], [0, 0, 0, 0]]);

    USERS = {1 : USER1.__get__(object),
               2 : USER2.__get__(object),
               3 : USER3.__get__(object),
               4 : USER4.__get__(object),
               5 : USER5.__get__(object),
               6 : USER6.__get__(object),
           }
    def printConstellation(self):
        trace1 = go.Scatter(x=[1, 2, 3], y=[4, 5, 6])
        trace2 = go.Scatter(x=[20, 30, 40], y=[50, 60, 70])
        trace3 = go.Scatter(x=[300, 400, 500], y=[600, 700, 800])
        trace4 = go.Scatter(x=[4000, 5000, 6000], y=[7000, 8000, 9000])

        fig = tools.make_subplots(rows=2, cols=2, subplot_titles=('Plot 1', 'Plot 2', 'Plot 3', 'Plot 4'))
        fig.append_trace(trace1, 1, 1)
        fig.append_trace(trace2, 1, 2)
        fig.append_trace(trace3, 2, 1)
        fig.append_trace(trace4, 2, 2)

        fig['layout']['xaxis1'].update(title='xaxis 1 title')
        fig['layout']['xaxis2'].update(title='xaxis 2 title', range=[10, 50])
        fig['layout']['xaxis3'].update(title='xaxis 3 title', showgrid=False)
        fig['layout']['xaxis4'].update(title='xaxis 4 title', type='log')

        fig['layout']['yaxis1'].update(title='yaxis 1 title')
        fig['layout']['yaxis2'].update(title='yaxis 2 title', range=[40, 80])
        fig['layout']['yaxis3'].update(title='yaxis 3 title', showgrid=False)
        fig['layout']['yaxis4'].update(title='yaxis 4 title')

        fig['layout'].update(title='Customizing Subplot Axes')

        py.iplot(fig, filename='customizing-subplot-axes')
    def print2(self):
        RGB = np.array([[0.1451, 0.0314, 0.3490],[0.0000, 0.2353, 1.0000],[0.0000, 0.6588, 0.8000],[0.2196, 1.0000, 0.7765],[0.4353, 0.9529, 0.7529],[0.6549, 0.9059, 0.7294]]);
        fig = plt.figure()

        for iResource in range(config.factorGraph.shape[0]):
            print(iResource);
            ax = fig.add_subplot(2,2,(iResource+1));
            eta = config.factorGraph[iResource];
            for i,vNode in enumerate(eta):
                if vNode == 1:
                    ax.scatter(CODEBOOK.USERS[i+1].real[iResource], CODEBOOK.USERS[i+1].imag[iResource], s=10, c=RGB[i], marker="s", label=('User '+str(i+1)))
            plt.legend(loc='upper left');
            plt.ylabel('Resource '+str(iResource+1));

        #resource 1
        #eta_0 = config.factorGraph[0]
        #for i,vNode in enumerate(eta_0):
        #    if vNode == 1:
        #        ax1.scatter(CODEBOOK.USERS[i+1].real[0], CODEBOOK.USERS[i+1].imag[0], s=10, c=RGB[i], marker="s", label=('User '+str(i+1)))
        #plt.legend(loc='upper left');

        #ax2 = fig.add_subplot(2,1,2)
        #resource 2
        #eta_1 = config.factorGraph[1]
        #for i,vNode in enumerate(eta_1):
        #    if vNode == 1:
        #        ax2.scatter(CODEBOOK.USERS[i+1].real[1], CODEBOOK.USERS[i+1].imag[1], s=10, c=RGB[i], marker="s", label=('User '+str(i+1)))
        #plt.legend(loc='upper left');
        plt.show()

CODEBOOK = _Codebok()
print(CODEBOOK.USERS[2]);
print(CODEBOOK.USERS[2].real[0]);
CODEBOOK.print2();
