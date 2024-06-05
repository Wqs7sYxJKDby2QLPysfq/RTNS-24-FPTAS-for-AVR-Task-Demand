"""
PDS BPCKP Experiment
"""

from sxs_fxns import exp_runner
from sxs_fxns import exp_task
from sxs_fxns import avr_alg_params
from sxs_fxns import delta_set
from task_sets import lit_avr_task_sets
from apx_fxns import apx_obj

#Create algorithm parameters
PRECISION = 5
MEMOIZE = True
GIVE_SLN_SEQ = False
TRACE_MEMORY = False
APX_PARAMS = apx_obj.ApxObj(0.025,0.025,0.025)

#Create task set
lit_task_set = lit_avr_task_sets.LitAvrTaskSets()
task_set_can = lit_task_set.avr_task_instance_2018_existing
task_set_gen = lit_task_set.avr_task_instance_2018_general

#Create delta set
START_DELTA_US = 10000
INCREMENT_DELTA_US = 10000
END_DELTA_US = 1000000
alg_delta_set = delta_set.DeltaSet([0],"rtss18")
alg_delta_set.update_delta_set_with_range(START_DELTA_US,INCREMENT_DELTA_US,END_DELTA_US)

#Set verbosity
VERBOSE = 0

PRECISION12 = 12

PRECISION5 = 5
PRECISION6 = 6
PRECISION7 = 7
PRECISION8 = 8

alg_params_p5 = avr_alg_params.AvrAlgParams(PRECISION5,MEMOIZE,GIVE_SLN_SEQ,TRACE_MEMORY,APX_PARAMS)
alg_params_p6 = avr_alg_params.AvrAlgParams(PRECISION6,MEMOIZE,GIVE_SLN_SEQ,TRACE_MEMORY,APX_PARAMS)
alg_params_p7 = avr_alg_params.AvrAlgParams(PRECISION7,MEMOIZE,GIVE_SLN_SEQ,TRACE_MEMORY,APX_PARAMS)
alg_params_p8 = avr_alg_params.AvrAlgParams(PRECISION8,MEMOIZE,GIVE_SLN_SEQ,TRACE_MEMORY,APX_PARAMS)
alg_params_p12 = avr_alg_params.AvrAlgParams(PRECISION12,MEMOIZE,GIVE_SLN_SEQ,TRACE_MEMORY,APX_PARAMS)

var_precision_alg_exp_row17_p5_can = exp_task.ExperimentTask("row17",alg_params_p5,task_set_can,alg_delta_set,VERBOSE)
var_precision_alg_exp_row17_p6_can = exp_task.ExperimentTask("row17",alg_params_p6,task_set_can,alg_delta_set,VERBOSE)
var_precision_alg_exp_row17_p7_can = exp_task.ExperimentTask("row17",alg_params_p7,task_set_can,alg_delta_set,VERBOSE)
var_precision_alg_exp_row17_p8_can = exp_task.ExperimentTask("row17",alg_params_p8,task_set_can,alg_delta_set,VERBOSE)
var_precision_alg_exp_kavr18_p5_can = exp_task.ExperimentTask("kavr18",alg_params_p5,task_set_can,alg_delta_set,VERBOSE)
var_precision_alg_exp_kavr18_p6_can = exp_task.ExperimentTask("kavr18",alg_params_p6,task_set_can,alg_delta_set,VERBOSE)
var_precision_alg_exp_kavr18_p7_can = exp_task.ExperimentTask("kavr18",alg_params_p7,task_set_can,alg_delta_set,VERBOSE)
var_precision_alg_exp_kavr18_p8_can = exp_task.ExperimentTask("kavr18",alg_params_p8,task_set_can,alg_delta_set,VERBOSE)
var_precision_alg_exp_kavr24_p5_can = exp_task.ExperimentTask("kavr24",alg_params_p5,task_set_can,alg_delta_set,VERBOSE)
var_precision_alg_exp_kavr24_p6_can = exp_task.ExperimentTask("kavr24",alg_params_p6,task_set_can,alg_delta_set,VERBOSE)
var_precision_alg_exp_kavr24_p7_can = exp_task.ExperimentTask("kavr24",alg_params_p7,task_set_can,alg_delta_set,VERBOSE)
var_precision_alg_exp_kavr24_p8_can = exp_task.ExperimentTask("kavr24",alg_params_p8,task_set_can,alg_delta_set,VERBOSE)
var_precision_alg_exp_exact_can = exp_task.ExperimentTask("exact",alg_params_p12,task_set_can,alg_delta_set,VERBOSE)
var_precision_alg_exp_apx_can = exp_task.ExperimentTask("apx",alg_params_p12,task_set_can,alg_delta_set,VERBOSE)
var_precision_alg_exp_row17_p5_gen = exp_task.ExperimentTask("row17",alg_params_p5,task_set_gen,alg_delta_set,VERBOSE)
var_precision_alg_exp_row17_p6_gen = exp_task.ExperimentTask("row17",alg_params_p6,task_set_gen,alg_delta_set,VERBOSE)
var_precision_alg_exp_row17_p7_gen = exp_task.ExperimentTask("row17",alg_params_p7,task_set_gen,alg_delta_set,VERBOSE)
var_precision_alg_exp_row17_p8_gen = exp_task.ExperimentTask("row17",alg_params_p8,task_set_gen,alg_delta_set,VERBOSE)
var_precision_alg_exp_kavr18_p5_gen = exp_task.ExperimentTask("kavr18",alg_params_p5,task_set_gen,alg_delta_set,VERBOSE)
var_precision_alg_exp_kavr18_p6_gen = exp_task.ExperimentTask("kavr18",alg_params_p6,task_set_gen,alg_delta_set,VERBOSE)
var_precision_alg_exp_kavr18_p7_gen = exp_task.ExperimentTask("kavr18",alg_params_p7,task_set_gen,alg_delta_set,VERBOSE)
var_precision_alg_exp_kavr18_p8_gen = exp_task.ExperimentTask("kavr18",alg_params_p8,task_set_gen,alg_delta_set,VERBOSE)
var_precision_alg_exp_kavr24_p5_gen = exp_task.ExperimentTask("kavr24",alg_params_p5,task_set_gen,alg_delta_set,VERBOSE)
var_precision_alg_exp_kavr24_p6_gen = exp_task.ExperimentTask("kavr24",alg_params_p6,task_set_gen,alg_delta_set,VERBOSE)
var_precision_alg_exp_kavr24_p7_gen = exp_task.ExperimentTask("kavr24",alg_params_p7,task_set_gen,alg_delta_set,VERBOSE)
var_precision_alg_exp_kavr24_p8_gen = exp_task.ExperimentTask("kavr24",alg_params_p8,task_set_gen,alg_delta_set,VERBOSE)
var_precision_alg_exp_exact_gen = exp_task.ExperimentTask("exact",alg_params_p12,task_set_gen,alg_delta_set,VERBOSE)
var_precision_alg_exp_apx_gen = exp_task.ExperimentTask("apx",alg_params_p12,task_set_gen,alg_delta_set,VERBOSE)

exp_runner_instance = exp_runner.ExperimentRunner()

MAKE_DBF_LOG_FILE = False
MAKE_EXP_LOG_FILE = False
MAKE_AGG_LOG_FILE = True

exp_runner_instance.run_experiments([var_precision_alg_exp_row17_p5_can],MAKE_DBF_LOG_FILE,MAKE_EXP_LOG_FILE,MAKE_AGG_LOG_FILE,"var_precision",VERBOSE)
exp_runner_instance.run_experiments([var_precision_alg_exp_row17_p6_can],MAKE_DBF_LOG_FILE,MAKE_EXP_LOG_FILE,MAKE_AGG_LOG_FILE,"var_precision",VERBOSE)
# exp_runner_instance.run_experiments([var_precision_alg_exp_row17_p7_can],MAKE_DBF_LOG_FILE,MAKE_EXP_LOG_FILE,MAKE_AGG_LOG_FILE,"var_precision",VERBOSE)
# exp_runner_instance.run_experiments([var_precision_alg_exp_row17_p8_can],MAKE_DBF_LOG_FILE,MAKE_EXP_LOG_FILE,MAKE_AGG_LOG_FILE,"var_precision",VERBOSE)
# exp_runner_instance.run_experiments([var_precision_alg_exp_kavr18_p5_can],MAKE_DBF_LOG_FILE,MAKE_EXP_LOG_FILE,MAKE_AGG_LOG_FILE,"var_precision",VERBOSE)
# exp_runner_instance.run_experiments([var_precision_alg_exp_kavr18_p6_can],MAKE_DBF_LOG_FILE,MAKE_EXP_LOG_FILE,MAKE_AGG_LOG_FILE,"var_precision",VERBOSE)
# exp_runner_instance.run_experiments([var_precision_alg_exp_kavr18_p7_can],MAKE_DBF_LOG_FILE,MAKE_EXP_LOG_FILE,MAKE_AGG_LOG_FILE,"var_precision",VERBOSE)
# exp_runner_instance.run_experiments([var_precision_alg_exp_kavr18_p8_can],MAKE_DBF_LOG_FILE,MAKE_EXP_LOG_FILE,MAKE_AGG_LOG_FILE,"var_precision",VERBOSE)
# exp_runner_instance.run_experiments([var_precision_alg_exp_exact_can],MAKE_DBF_LOG_FILE,MAKE_EXP_LOG_FILE,MAKE_AGG_LOG_FILE,"var_precision",VERBOSE)
# exp_runner_instance.run_experiments([var_precision_alg_exp_apx_can],MAKE_DBF_LOG_FILE,MAKE_EXP_LOG_FILE,MAKE_AGG_LOG_FILE,"var_precision",VERBOSE)
exp_runner_instance.run_experiments([var_precision_alg_exp_row17_p5_gen],MAKE_DBF_LOG_FILE,MAKE_EXP_LOG_FILE,MAKE_AGG_LOG_FILE,"var_precision",VERBOSE)
exp_runner_instance.run_experiments([var_precision_alg_exp_row17_p6_gen],MAKE_DBF_LOG_FILE,MAKE_EXP_LOG_FILE,MAKE_AGG_LOG_FILE,"var_precision",VERBOSE)
# exp_runner_instance.run_experiments([var_precision_alg_exp_row17_p7_gen],MAKE_DBF_LOG_FILE,MAKE_EXP_LOG_FILE,MAKE_AGG_LOG_FILE,"var_precision",VERBOSE)
# exp_runner_instance.run_experiments([var_precision_alg_exp_row17_p8_gen],MAKE_DBF_LOG_FILE,MAKE_EXP_LOG_FILE,MAKE_AGG_LOG_FILE,"var_precision",VERBOSE)
# exp_runner_instance.run_experiments([var_precision_alg_exp_kavr18_p5_gen],MAKE_DBF_LOG_FILE,MAKE_EXP_LOG_FILE,MAKE_AGG_LOG_FILE,"var_precision",VERBOSE)
# exp_runner_instance.run_experiments([var_precision_alg_exp_kavr18_p6_gen],MAKE_DBF_LOG_FILE,MAKE_EXP_LOG_FILE,MAKE_AGG_LOG_FILE,"var_precision",VERBOSE)
# exp_runner_instance.run_experiments([var_precision_alg_exp_kavr18_p7_gen],MAKE_DBF_LOG_FILE,MAKE_EXP_LOG_FILE,MAKE_AGG_LOG_FILE,"var_precision",VERBOSE)
# exp_runner_instance.run_experiments([var_precision_alg_exp_kavr18_p8_gen],MAKE_DBF_LOG_FILE,MAKE_EXP_LOG_FILE,MAKE_AGG_LOG_FILE,"var_precision",VERBOSE)
# exp_runner_instance.run_experiments([var_precision_alg_exp_exact_gen],MAKE_DBF_LOG_FILE,MAKE_EXP_LOG_FILE,MAKE_AGG_LOG_FILE,"var_precision",VERBOSE)
# exp_runner_instance.run_experiments([var_precision_alg_exp_apx_gen],MAKE_DBF_LOG_FILE,MAKE_EXP_LOG_FILE,MAKE_AGG_LOG_FILE,"var_precision",VERBOSE)