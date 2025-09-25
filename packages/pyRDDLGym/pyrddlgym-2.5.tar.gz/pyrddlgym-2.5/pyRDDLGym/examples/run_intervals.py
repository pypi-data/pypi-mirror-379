'''In this example, compute lower and upper value bounds on a simple policy.

The syntax for running this example is:

    python run_intervals.py <domain> <instance> <policy>
    
where:
    <domain> is the name of a domain located in the /Examples directory
    <instance> is the instance number
    <policy> is either "random" or "noop"
'''
import sys
import numpy as np

import pyRDDLGym
from pyRDDLGym.core.intervals import (
    RDDLIntervalAnalysis, RDDLIntervalAnalysisPercentile, RDDLIntervalAnalysisMean
)


def main(domain, instance, policy, method):
    
    # create the environment
    env = pyRDDLGym.make(domain, instance, vectorized=True)
    
    # create the method
    if method == 'support':
        analysis = RDDLIntervalAnalysis(env.model)
    elif method == 'mean':
        analysis = RDDLIntervalAnalysisMean(env.model)
    else:
        p = float(method)
        analysis = RDDLIntervalAnalysisPercentile(env.model, (p, 1 - p))
        
    # set range of action fluents to uniform over action space
    if policy == 'random':
        action_bounds = {}
        for action, prange in env.model.action_ranges.items():
            lower, upper = env._bounds[action]
            if prange == 'bool':
                lower = np.full(np.shape(lower), fill_value=0, dtype=int)
                upper = np.full(np.shape(upper), fill_value=1, dtype=int)
            action_bounds[action] = (lower, upper)
    else:
        action_bounds = None
    
    # evaluate lower and upper bounds on accumulated reward of random policy
    bounds = analysis.bound(action_bounds=action_bounds, per_epoch=True)
    reward_lower, reward_upper = bounds['reward']    
    print(f'value lower bound = {np.sum(reward_lower)}, '
          f'value upper bound = {np.sum(reward_upper)}')
    
    env.close()


if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) < 4:
        print('python run_intervals.py <domain> <instance> <policy> <method>')
        exit(1)
    kwargs = {'domain': args[0], 'instance': args[1], 
              'policy': args[2], 'method': args[3]}
    main(**kwargs)
