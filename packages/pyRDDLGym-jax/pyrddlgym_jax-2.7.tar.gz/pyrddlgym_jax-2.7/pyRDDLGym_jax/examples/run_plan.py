'''In this example, the user has the choice to run the Jax planner with three
different options:
    
    1. slp runs the straight-line planner offline, which trains an open-loop plan
    2. drp runs the deep reactive policy, which trains a policy network
    3. replan runs the straight-line planner online, at every decision epoch
    
The syntax for running this example is:

    python run_plan.py <domain> <instance> <method> [<episodes>]
    
where:
    <domain> is the name of a domain located in the /Examples directory
    <instance> is the instance number
    <method> is slp, drp, replan, or a path to a valid .cfg file
    <episodes> is the optional number of evaluation rollouts
'''
import os
import sys

import pyRDDLGym
from pyRDDLGym.core.debug.exception import raise_warning

from pyRDDLGym_jax.core.planner import (
    load_config, JaxBackpropPlanner, JaxOfflineController, JaxOnlineController
)


def run_cnn1d():
    import haiku as hk
    import jax
    import jax.numpy as jnp

    class CNN(hk.Module):
        def __init__(self, name=None):
            super().__init__(name=name)
            self.conv1d_layer = hk.Conv1D(
                output_channels=4,
                kernel_shape=6,  # Kernel size for 1D convolution
                padding="SAME",
                name="conv"
            )

        def __call__(self, x):
            return self.conv1d_layer(x)

    # Example usage:
    key = jax.random.PRNGKey(42)
    input_data = jnp.ones([1, 4])  # Batch size 1, sequence length 10, 1 input channel

    # Transform the Haiku module into a pure function
    f = hk.transform(lambda x: CNN()(x))
    params = f.init(key, input_data)
    print(params['cnn/~/conv']['w'].shape)
    print(params['cnn/~/conv']['b'].shape)
    print(f.apply(params, key, input_data).shape)

    
def main(domain: str, instance: str, method: str, episodes: int=1) -> None:
    
    # set up the environment
    env = pyRDDLGym.make(domain, instance, vectorized=True)
    
    # load the config file with planner settings
    if method in ['drp', 'slp', 'replan']:
        abs_path = os.path.dirname(os.path.abspath(__file__))
        config_path = os.path.join(abs_path, 'configs', f'{domain}_{method}.cfg') 
        if not os.path.isfile(config_path):
            raise_warning(f'[WARN] Config file {config_path} was not found, '
                          f'using default_{method}.cfg.', 'yellow')
            config_path = os.path.join(abs_path, 'configs', f'default_{method}.cfg') 
    elif os.path.isfile(method):
        config_path = method
    else:
        print('method must be slp, drp, replan, or a path to a valid .cfg file.')
        exit(1)
    
    planner_args, _, train_args = load_config(config_path)
    if 'dashboard' in train_args: 
        train_args['dashboard'].launch()
    
    # create the planning algorithm
    planner = JaxBackpropPlanner(
        rddl=env.model, dashboard_viz=env._visualizer, **planner_args)
    
    # evaluate the controller   
    if method == 'replan':
        controller = JaxOnlineController(planner, **train_args)
    else:
        controller = JaxOfflineController(planner, **train_args)    
    controller.evaluate(env, episodes=episodes, verbose=True, render=True)
    env.close()
        

def run_from_args(args):
    run_cnn1d()
    if len(args) < 3:
        print('python run_plan.py <domain> <instance> <method> [<episodes>]')
        exit(1)
    kwargs = {'domain': args[0], 'instance': args[1], 'method': args[2]}
    if len(args) >= 4: kwargs['episodes'] = int(args[3])
    main(**kwargs)


if __name__ == "__main__":
    run_from_args(sys.argv[1:])
    
