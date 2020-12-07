import justpy as jp
import matplotlib.pyplot as plt
import numpy as np

# import data
RCP_data = np.loadtxt('RCP_data.txt', delimiter="\t", skiprows = 1)

def KlimApp():
    wp = jp.WebPage()

    # event handler for RCP radio buttons
    def rcp_changed(self, msg):

        self.result_div.text = ''
        n = 1

        for btn in self.btn_list:
            print(btn)
            if btn.checked:

                f = plt.figure()
                params = {'mathtext.default': 'regular' }
                plt.plot(RCP_data[:,0],RCP_data[:,n])
                plt.rcParams.update(params)
                plt.xlabel('Jahre')
                plt.ylabel('$CO_2\/Konzentration\/(ppm)$')
                plt.legend([btn.value])
                self.chart.set_figure(f)
                plt.close()

            n = n+1

    result_div = jp.Div(text='Click radio buttons to see results here', classes='m-2 p-2 text-xl')
    rcp_scenarios = ['RCP 2.6', 'RCP 4.5', 'RCP 6.0', 'RCP 8.5', 'Alle RCP']
    outer_div = jp.Div(classes='border m-2 p-2 w-64', a=wp)
    jp.P(a=outer_div, text='IPCC Treibhausgas Szenarien:')

    f = plt.figure()
    params = {'mathtext.default': 'regular' }
    plt.plot(RCP_data[:,0],RCP_data[:,1])
    plt.rcParams.update(params)
    plt.xlabel('Jahre')
    plt.ylabel('$CO_2\/Konzentration\/(ppm)$')
    plt.legend('RCP 2.6')
    chart = jp.Matplotlib(a=wp)
    plt.close(f)

    #create radio buttons for RCP scenarios
    scenarios_list = []
    for scenario in rcp_scenarios:
        label = jp.Label(classes='inline-block mb-1 p-1', a=outer_div)
        radio_btn = jp.Input(type='radio', name='RCP', value=scenario, btn_list=scenarios_list, a=label, change=rcp_changed, result_div=result_div)
        radio_btn.chart = chart
        scenarios_list.append(radio_btn)

        jp.Span(classes='ml-1', a=label, text=scenario)

    wp.add(result_div)
    return wp

jp.justpy(KlimApp)
#jp.justpy(hello_world, host="0.0.0.0", port=80)
