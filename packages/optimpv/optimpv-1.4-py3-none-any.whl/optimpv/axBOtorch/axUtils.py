"""Utility functions for the Ax/Botorch library"""
# Note: This class is inspired by the https://github.com/i-MEET/boar/ package
######### Package Imports #########################################################################

import numpy as np
import pandas as pd
import ax
from ax import *
from ax.api.configs import RangeParameterConfig, ChoiceParameterConfig
from ax.core.batch_trial import BatchTrial
from ax.service.ax_client import ObjectiveProperties
from ax.core.base_trial import TrialStatus

######### Function Definitions ####################################################################

def ConvertParamsAx(params):
    """Convert the params to the format required by the Ax/Botorch library

        Parameters
        ----------
        params : list of Fitparam() objects
            list of Fitparam() objects

        Returns
        -------
        list of dict
            list of dictionaries with the following keys:

                'name': string: the name of the parameter
                'type': string: 'range' or 'fixed'
                'bounds': list of float: the lower and upper bounds of the parameter
                
        """ 
    if params is None:
        raise ValueError('The params argument is None')
    
    ax_params,fixed_params = [],{}
    for param in params:
        if param.value_type == 'float':
            if param.type == 'fixed':
                fixed_params[param.name] = float(param.value)
            else:
                if param.force_log:
                    ax_params.append(RangeParameterConfig(name=param.name, bounds=[np.log10(param.bounds[0]), np.log10(param.bounds[1])], parameter_type='float', scaling="linear"))
                else:
                    if param.log_scale:
                        ax_params.append(RangeParameterConfig(name=param.name, bounds=[param.bounds[0]/param.fscale, param.bounds[1]/param.fscale], parameter_type='float', scaling="log"))
                    else:
                        ax_params.append(RangeParameterConfig(name=param.name, bounds=[param.bounds[0]/param.fscale, param.bounds[1]/param.fscale], parameter_type='float', scaling="linear"))
        elif param.value_type == 'int':
            if param.type == 'fixed':
                fixed_params[param.name] = int(param.value)
            else:
                ax_params.append(RangeParameterConfig(name=param.name, bounds=[int(param.bounds[0]/param.stepsize), int(param.bounds[1]/param.stepsize)], parameter_type='int', scaling="linear"))
        elif param.value_type == 'cat' or param.value_type == 'sub' or param.value_type == 'str': 
            if param.type == 'fixed':
                fixed_params[param.name] = param.value
            else:
                ax_params.append(ChoiceParameterConfig(name=param.name, values=param.values, parameter_type='str', is_ordered=param.is_ordered))
        elif param.value_type == 'bool':
            if param.type == 'fixed':
                fixed_params[param.name] = param.value
            else:
                ax_params.append(ChoiceParameterConfig(name=param.name, values=[True, False], parameter_type='bool'))
        else:
            raise ValueError('Failed to convert parameter name: {} to Ax format'.format(param.name))

    return ax_params,fixed_params

def CreateObjectiveFromAgent(agent):
    """Create the objective function from the agent

        Parameters
        ----------
        agent : Agent() object
            the agent object

        Returns
        -------
        function
            the objective function
        """ 

    objectives = {}
    for i in range(len(agent.metric)):
        if hasattr(agent,'exp_format'):
            objectives[agent.name+'_'+agent.exp_format[i]+'_'+agent.metric[i]] = ObjectiveProperties(minimize=agent.minimize[i], threshold=agent.threshold[i])
        else:
            objectives[agent.name+'_'+agent.metric[i]] = ObjectiveProperties(minimize=agent.minimize[i], threshold=agent.threshold[i])


    return objectives

# def search_spaceAx(search_space):
#     parameters = []
#     for param in search_space:
#         if param['type'] == 'range':
#             if param['value_type'] == 'int':
#                 parameters.append(RangeParameter(name=param['name'], parameter_type=ParameterType.INT, lower=param['bounds'][0], upper=param['bounds'][1]))
#             else:
#                 parameters.append(RangeParameter(name=param['name'], parameter_type=ParameterType.FLOAT, lower=param['bounds'][0], upper=param['bounds'][1]))
#         elif param['type'] == 'fixed':
#             if param['value_type'] == 'int':
#                 parameters.append(FixedParameter(name=param.name, parameter_type=ParameterType.INT, value=param.value))
#             elif param['value_type'] == 'str':
#                 parameters.append(FixedParameter(name=param.name, parameter_type=ParameterType.STRING, value=param.value))
#             elif param['value_type'] == 'bool':
#                 parameters.append(FixedParameter(name=param.name, parameter_type=ParameterType.BOOL, value=param.value))
#             else:
#                 parameters.append(FixedParameter(name=param.name, parameter_type=ParameterType.FLOAT, value=param.value))
#         elif param['type'] == 'choice':
#             parameters.append(ChoiceParameter(name=param.name, values=param.values, is_ordered=param.is_ordered, is_sorted=param.is_sorted))
#         else:
#             raise ValueError('The parameter type is not recognized')
#     return SearchSpace(parameters=parameters)

def get_df_from_ax(params, optimizer):
    """Get the dataframe from the ax client and rescale the parameters to their true scale.
    The dataframe contains the parameters and the objective values.
    The parameters are rescaled to their true scale.
    The objective values are the mean of the objective values.
    The dataframe is returned as a pandas dataframe.

    Parameters
    ----------
    params : list of FitParam() objects
        List of Fitparam() objects.
    optimizer : object
        Optimizer object from optimpv.axBOtorch.axBOtorch
        The optimizer object contains the ax client and the experiment.

    Returns
    -------
    pd.DataFrame
        Dataframe containing the parameters and the objective values.

    Raises
    ------
    ValueError
        trying to rescale a parameter that is not int or float
    """    
    ax_client = optimizer.ax_client
    objective_names = optimizer.all_metrics
    
    df = get_df_ax_client_metrics(params, ax_client, objective_names)

    return df

def get_df_ax_client_metrics(params, ax_client, all_metrics):
    """Get the dataframe from the ax client and rescale the parameters to their true scale.
    The dataframe contains the parameters and the objective values.
    The parameters are rescaled to their true scale.
    The objective values are the mean of the objective values.
    The dataframe is returned as a pandas dataframe.

    Parameters
    ----------
    params : list of FitParam() objects
        List of Fitparam() objects.
    ax_client : object
        Ax client object.
    all_metrics : list of str
        List of objective names.

    Returns
    -------
    pd.DataFrame
        Dataframe containing the parameters and the objective values.

    Raises
    ------
    ValueError
        trying to rescale a parameter that is not int or float
    """
    data = ax_client.summarize()
    objective_names = all_metrics
    # dumdic = {}
    # # create a dic with the keys of the parameters
    # if isinstance(ax_client.experiment.trials[0], BatchTrial):# check if trial is a BatchTrial
    #     for key in ax_client.experiment.trials[0].arms[0].parameters.keys():
    #         dumdic[key] = []
        
    #     # fill the dic with the values of the parameters
    #     for i in range(len(ax_client.experiment.trials)):

    #         if ax_client.experiment.trials[i].status == TrialStatus.COMPLETED:
    #             for arm in ax_client.experiment.trials[i].arms:
    #                 if arm.name in data['arm_name'].values: # only add the arm if it is in the data i.e. if it was completed
    #                     for key in arm.parameters.keys():
    #                         dumdic[key].append(arm.parameters[key])       
    # else:
    #     for key in ax_client.experiment.trials[0].arm.parameters.keys():
    #         dumdic[key] = []

    #     # fill the dic with the values of the parameters
    #     for i in range(len(ax_client.experiment.trials)):
    #         if ax_client.experiment.trials[i].status == TrialStatus.COMPLETED:
    #             for key in ax_client.experiment.trials[i].arm.parameters.keys():
    #                 dumdic[key].append(ax_client.experiment.trials[i].arm.parameters[key])

    
    # for objective_name in objective_names:
    #     dumdic[objective_name] = list(data[data['metric_name'] == objective_name]['mean'])

    # dumdic['iteration'] = list(data[data['metric_name'] == objective_name]['trial_index'])

    # df = pd.DataFrame(dumdic)
    df = data

    # add iteration column with 
    for par in params:
        if par.name in df.columns:
            if par.type == 'fixed':
                df[par.name] = par.value
            else:
                if par.value_type == 'int':
                    df[par.name] = df[par.name] * par.stepsize
                elif par.value_type == 'float':
                    if par.force_log:
                        df[par.name] = 10 ** df[par.name]
                    else:
                        df[par.name] = df[par.name] * par.fscale
                elif par.value_type == 'cat' or par.value_type == 'sub' or par.value_type == 'str':
                    pass
                elif par.value_type == 'bool':
                    pass
                else: 
                    raise ValueError('Trying to rescale a parameter that is not int or float')
            # if par.rescale or par.force_log:
            #     if par.value_type == 'int':
            #         df[par.name] = df[par.name] * par.stepsize
            #     elif par.value_type == 'float':
            #         if par.force_log:
            #             df[par.name] = 10 ** df[par.name]
            #         else:
            #             df[par.name] = df[par.name] * par.fscale
            #     else: 
            #         raise ValueError('Trying to rescale a parameter that is not int or float')
    return df