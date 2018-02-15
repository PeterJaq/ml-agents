# # Unity ML Agents
# ## ML-Agent Learning

import logging

from docopt import docopt

from unitytrainers.trainer_controller import TrainerController

if __name__ == '__main__':
    logger = logging.getLogger("unityagents")
    _USAGE = '''
    Usage:
      learn (<env>) [options] 

    Options:
      --help                     Show this message.
      --curriculum=<file>        Curriculum json file for environment [default: None].
      --keep-checkpoints=<n>     How many model checkpoints to keep [default: 5].
      --lesson=<n>               Start learning from this lesson [default: 0].
      --load                     Whether to load the model or randomly initialize [default: False].
      --run-id=<path>            The sub-directory name for model and summary statistics [default: ppo]. 
      --save-freq=<n>            Frequency at which to save model [default: 50000].
      --seed=<n>                 Random seed used for training [default: -1].
      --slow                     Whether to run the game at training speed [default: False].
      --train                    Whether to train model, or only run inference [default: False].
      --worker-id=<n>            Number to add to communication port (5005). Used for multi-environment [default: 0].
    '''

    options = docopt(_USAGE)
    logger.info(options)

    # General parameters
    run_id = options['--run-id']
    seed = int(options['--seed'])
    load_model = options['--load']
    train_model = options['--train']
    save_freq = int(options['--save-freq'])
    env_name = options['<env>']
    keep_checkpoints = int(options['--keep-checkpoints'])
    worker_id = int(options['--worker-id'])
    curriculum_file = str(options['--curriculum'])
    if curriculum_file == "None":
        curriculum_file = None
    lesson = int(options['--lesson'])
    fast_simulation = not bool(options['--slow'])

    tc = TrainerController(env_name, run_id, save_freq, curriculum_file, fast_simulation, load_model, train_model,
                           worker_id, keep_checkpoints, lesson, seed)
    tc.start_learning()