from typing import Callable
import pymimir as mm
import pytest
import torch

from pathlib import Path
from pymimir_rgnn import (
    RelationalGraphNeuralNetwork,
    HyperparameterConfig,
    ModuleConfig,
    SumAggregation,
    PredicateMLPMessages,
    MLPUpdates,
    Encoder,
    StateEncoder,
    GroundActionsEncoder,
    GoalEncoder,
    Decoder,
    ActionScalarDecoder
)
from pymimir_rl import *


TEST_DIR = Path(__file__).parent
DATA_DIR = TEST_DIR / 'data'


class RGNNWrapper(ActionScalarModel):
    def __init__(self, domain: mm.Domain) -> None:
        super().__init__()  # type: ignore

        hparam_config = HyperparameterConfig(
            domain=domain,
            num_layers=4,
            embedding_size=8
        )

        input_spec = (StateEncoder(), GroundActionsEncoder(), GoalEncoder())
        output_spec = [('q', ActionScalarDecoder(hparam_config))]

        module_config = ModuleConfig(
            aggregation_function=SumAggregation(),
            message_function=PredicateMLPMessages(hparam_config, input_spec),
            update_function=MLPUpdates(hparam_config)
        )

        self.rgnn = RelationalGraphNeuralNetwork(hparam_config, module_config, input_spec, output_spec)  # type: ignore

    def forward(self, state_goals: list[tuple[mm.State, mm.GroundConjunctiveCondition]]) -> list[tuple[torch.Tensor, list[mm.GroundAction]]]:
        input_list: list[tuple[mm.State, list[mm.GroundAction], mm.GroundConjunctiveCondition]] = []
        actions_list: list[list[mm.GroundAction]] = []
        for state, goal in state_goals:
            actions = state.generate_applicable_actions()
            input_list.append((state, actions, goal))
            actions_list.append(actions)
        q_values_list: list[torch.Tensor] = self.rgnn.forward(input_list).readout('q')  # type: ignore
        output = list(zip(q_values_list, actions_list))
        for tensor, _ in output:
            assert not tensor.isnan().any()
            assert not tensor.isinf().any()
        return output


def test_model_wrapper():
    domain_path = DATA_DIR / 'gripper' / 'domain.pddl'
    problem_path = DATA_DIR / 'gripper' / 'problem.pddl'
    domain = mm.Domain(domain_path)
    problem = mm.Problem(domain, problem_path)
    model = RGNNWrapper(domain)
    current_state = problem.get_initial_state()
    goal_condition = problem.get_goal_condition()
    output = model.forward([(current_state, goal_condition)])
    assert output is not None
    assert isinstance(output, list)
    assert len(output) > 0
    assert isinstance(output[0][0], torch.Tensor)
    assert isinstance(output[0][1], list)
    assert len(output[0][1]) > 0


def test_dqn_loss():
    domain_path = DATA_DIR / 'gripper' / 'domain.pddl'
    problem_path = DATA_DIR / 'gripper' / 'problem.pddl'
    domain = mm.Domain(domain_path)
    problem = mm.Problem(domain, problem_path)
    model = RGNNWrapper(domain)
    optimizer = torch.optim.Adam(model.parameters())
    lr_scheduler = torch.optim.lr_scheduler.ConstantLR(optimizer)
    loss = DQNOptimization(model, optimizer, lr_scheduler, model, 0.999, 10.0, True)
    transitions: list[Transition] = []
    current_state = problem.get_initial_state()
    reward_function = ConstantRewardFunction(-1.0)
    for selected_action in current_state.generate_applicable_actions():
        successor_state = selected_action.apply(current_state)
        goal_condition = problem.get_goal_condition()
        reward = reward_function(current_state, selected_action, successor_state, goal_condition)
        transitions.append(Transition(current_state, successor_state, selected_action, -1.0, -1.0, reward, 0.0, reward_function, goal_condition, False))
    losses = loss(transitions, torch.ones(len(transitions)))
    assert losses is not None
    assert len(losses) == len(transitions)


def test_sac_loss():
    domain_path = DATA_DIR / 'gripper' / 'domain.pddl'
    problem_path = DATA_DIR / 'gripper' / 'problem.pddl'
    domain = mm.Domain(domain_path)
    problem = mm.Problem(domain, problem_path)
    policy_model = RGNNWrapper(domain)
    qvalue_model_1 = RGNNWrapper(domain)
    qvalue_model_2 = RGNNWrapper(domain)
    qvalue_target_1 = RGNNWrapper(domain)
    qvalue_target_2 = RGNNWrapper(domain)
    policy_optimizer = torch.optim.Adam(policy_model.parameters())
    qvalue_optimizer_1 = torch.optim.Adam(qvalue_model_1.parameters())
    qvalue_optimizer_2 = torch.optim.Adam(qvalue_model_2.parameters())
    policy_lr_scheduler = torch.optim.lr_scheduler.StepLR(policy_optimizer, step_size=10, gamma=0.9)
    qvalue_lr_scheduler_1 = torch.optim.lr_scheduler.StepLR(qvalue_optimizer_1, step_size=10, gamma=0.9)
    qvalue_lr_scheduler_2 = torch.optim.lr_scheduler.StepLR(qvalue_optimizer_2, step_size=10, gamma=0.9)
    discount_factor = 0.999
    polyak_factor = 0.005
    entropy_temperature = 1.0
    entropy_lr = 0.0003
    loss = DiscreteSoftActorCriticOptimization(policy_model,
                                               policy_optimizer,
                                               policy_lr_scheduler,
                                               qvalue_target_1,
                                               qvalue_model_1,
                                               qvalue_optimizer_1,
                                               qvalue_lr_scheduler_1,
                                               qvalue_target_2,
                                               qvalue_model_2,
                                               qvalue_optimizer_2,
                                               qvalue_lr_scheduler_2,
                                               discount_factor,
                                               polyak_factor,
                                               entropy_temperature,
                                               entropy_lr)
    transitions: list[Transition] = []
    current_state = problem.get_initial_state()
    reward_function = ConstantRewardFunction(-1.0)
    for selected_action in current_state.generate_applicable_actions():
        successor_state = selected_action.apply(current_state)
        goal_condition = problem.get_goal_condition()
        reward = reward_function(current_state, selected_action, successor_state, goal_condition)
        transitions.append(Transition(current_state, successor_state, selected_action, -1.0, -1.0, reward, 0.0, reward_function, goal_condition, False))
    losses = loss(transitions, torch.ones(len(transitions)))
    assert losses is not None
    assert len(losses) == len(transitions)


@pytest.mark.parametrize("domain_name, trajectory_sampler_creator", [
    ('blocks', lambda model, reward_function: PolicyTrajectorySampler(model, reward_function)),
    ('blocks', lambda model, reward_function: BoltzmannTrajectorySampler(model, reward_function, 1.0)),
    ('blocks', lambda model, reward_function: StateBoltzmannTrajectorySampler(model, reward_function, 1.0, 0.1, 10)),
    ('blocks', lambda model, reward_function: GreedyPolicyTrajectorySampler(model, reward_function)),
    ('blocks', lambda model, reward_function: EpsilonGreedyTrajectorySampler(model, reward_function, 0.5)),
    ('gripper', lambda model, reward_function: PolicyTrajectorySampler(model, reward_function)),
    ('gripper', lambda model, reward_function: BoltzmannTrajectorySampler(model, reward_function, 1.0)),
    ('gripper', lambda model, reward_function: GreedyPolicyTrajectorySampler(model, reward_function)),
    ('gripper', lambda model, reward_function: StateBoltzmannTrajectorySampler(model, reward_function, 1.0, 0.1, 10)),
    ('gripper', lambda model, reward_function: EpsilonGreedyTrajectorySampler(model, reward_function, 0.5))
])
def test_trajectory_sampler(domain_name: str, trajectory_sampler_creator: Callable[[ActionScalarModel, RewardFunction], TrajectorySampler]):
    domain_path = DATA_DIR / domain_name / 'domain.pddl'
    problem_path = DATA_DIR / domain_name / 'problem.pddl'
    domain = mm.Domain(domain_path)
    problem = mm.Problem(domain, problem_path)
    model = RGNNWrapper(domain)
    reward_function = GoalTransitionRewardFunction(1)
    trajectory_sampler = trajectory_sampler_creator(model, reward_function)
    trajectories = trajectory_sampler.sample([(problem.get_initial_state(), problem.get_goal_condition())], 10)
    assert isinstance(trajectories, list)
    assert len(trajectories) == 1
    trajectory = trajectories[0]
    assert isinstance(trajectory, Trajectory)
    assert trajectory.is_solution() or len(trajectory) == 10
    trajectory.validate()  # Performs asserts internally.


@pytest.mark.parametrize("domain_name", ['blocks-hard', 'gripper-hard'])
def test_state_hindsight(domain_name: str):
    domain_path = DATA_DIR / domain_name / 'domain.pddl'
    problem_path = DATA_DIR / domain_name / 'problem.pddl'
    domain = mm.Domain(domain_path)
    problem = mm.Problem(domain, problem_path)
    model = RGNNWrapper(domain)
    reward_function = ConstantRewardFunction(-1)
    trajectory_sampler = PolicyTrajectorySampler(model, reward_function)
    trajectory_refiner = StateHindsightTrajectoryRefiner(10)
    original_trajectories = trajectory_sampler.sample([(problem.get_initial_state(), problem.get_goal_condition())], 100)
    refined_trajectories = trajectory_refiner.refine(original_trajectories)
    assert len(refined_trajectories) < 10
    for refined_trajectory in refined_trajectories:
        assert refined_trajectory.is_solution()
        refined_trajectory.validate()


@pytest.mark.parametrize("domain_name", ['blocks-hard', 'gripper-hard'])
def test_propositional_hindsight(domain_name: str):
    domain_path = DATA_DIR / domain_name / 'domain.pddl'
    problem_path = DATA_DIR / domain_name / 'problem.pddl'
    domain = mm.Domain(domain_path)
    problem = mm.Problem(domain, problem_path)
    model = RGNNWrapper(domain)
    reward_function = ConstantRewardFunction(-1)
    trajectory_sampler = PolicyTrajectorySampler(model, reward_function)
    trajectory_refiner = PropositionalHindsightTrajectoryRefiner([problem], 10)
    original_trajectories = trajectory_sampler.sample([(problem.get_initial_state(), problem.get_goal_condition())], 100)
    refined_trajectories = trajectory_refiner.refine(original_trajectories)
    assert len(refined_trajectories) < 10
    for refined_trajectory in refined_trajectories:
        assert refined_trajectory.is_solution()
        refined_trajectory.validate()


@pytest.mark.parametrize("domain_name", ['blocks-hard', 'gripper-hard'])
def test_lifted_hindsight(domain_name: str):
    domain_path = DATA_DIR / domain_name / 'domain.pddl'
    problem_path = DATA_DIR / domain_name / 'problem.pddl'
    domain = mm.Domain(domain_path)
    problem = mm.Problem(domain, problem_path)
    model = RGNNWrapper(domain)
    reward_function = ConstantRewardFunction(-1)
    trajectory_sampler = PolicyTrajectorySampler(model, reward_function)
    trajectory_refiner = LiftedHindsightTrajectoryRefiner([problem], 10)
    original_trajectories = trajectory_sampler.sample([(problem.get_initial_state(), problem.get_goal_condition())], 100)
    refined_trajectories = trajectory_refiner.refine(original_trajectories)
    assert len(refined_trajectories) < 10
    for refined_trajectory in refined_trajectories:
        assert refined_trajectory.is_solution()
        refined_trajectory.validate()


@pytest.mark.parametrize("domain_name", ['blocks', 'gripper'])
def test_off_policy_algorithm(domain_name: str):
    domain_path = DATA_DIR / domain_name / 'domain.pddl'
    problem_path = DATA_DIR / domain_name / 'problem.pddl'
    domain = mm.Domain(domain_path)
    problem = mm.Problem(domain, problem_path)
    problems = [problem]
    model = RGNNWrapper(domain)
    optimizer = torch.optim.Adam(model.parameters())
    lr_scheduler = torch.optim.lr_scheduler.ConstantLR(optimizer)
    discount_factor = 0.999
    loss_function = DQNOptimization(model, optimizer, lr_scheduler, model, discount_factor, 10.0)
    reward_function = ConstantRewardFunction(-1)
    replay_buffer = PrioritizedReplayBuffer(100)
    trajectory_sampler = PolicyTrajectorySampler(model, reward_function)
    horizon = 100
    rollout_count = 2
    batch_size = 4
    train_steps = 8
    problem_sampler = UniformProblemSampler()
    initial_state_sampler = OriginalInitialStateSampler()
    goal_condition_sampler = OriginalGoalConditionSampler()
    trajectory_refiner = PropositionalHindsightTrajectoryRefiner(problems, 10)
    algorithm = OffPolicyAlgorithm(problems,
                                   loss_function,
                                   reward_function,
                                   replay_buffer,
                                   replay_buffer,
                                   trajectory_sampler,
                                   horizon,
                                   rollout_count,
                                   batch_size,
                                   train_steps,
                                   problem_sampler,
                                   initial_state_sampler,
                                   goal_condition_sampler,
                                   trajectory_refiner)
    algorithm.fit()
    algorithm.fit()
    algorithm.fit()

def test_algorithm_hooks():
    domain_path = DATA_DIR / 'gripper' / 'domain.pddl'
    problem_path = DATA_DIR / 'gripper' / 'problem.pddl'
    domain = mm.Domain(domain_path)
    problem = mm.Problem(domain, problem_path)
    problems = [problem]
    model = RGNNWrapper(domain)
    optimizer = torch.optim.Adam(model.parameters())
    lr_scheduler = torch.optim.lr_scheduler.ConstantLR(optimizer)
    discount_factor = 0.999
    loss_function = DQNOptimization(model, optimizer, lr_scheduler, model, discount_factor, 100.0)
    reward_function = ConstantRewardFunction(-1)
    replay_buffer = PrioritizedReplayBuffer(100)
    trajectory_sampler = PolicyTrajectorySampler(model, reward_function)
    horizon = 10
    rollout_count = 2
    batch_size = 4
    train_steps = 8
    problem_sampler = UniformProblemSampler()
    initial_state_sampler = OriginalInitialStateSampler()
    goal_condition_sampler = OriginalGoalConditionSampler()
    trajectory_refiner = PropositionalHindsightTrajectoryRefiner(problems, 10)
    algorithm = OffPolicyAlgorithm(problems,
                                   loss_function,
                                   reward_function,
                                   replay_buffer,
                                   replay_buffer,
                                   trajectory_sampler,
                                   horizon,
                                   rollout_count,
                                   batch_size,
                                   train_steps,
                                   problem_sampler,
                                   initial_state_sampler,
                                   goal_condition_sampler,
                                   trajectory_refiner)
    sample_problems: list[bool] = []
    sample_initial_states: list[bool] = []
    sample_goal_conditions: list[bool] = []
    sample_trajectories: list[bool] = []
    refine_trajectories: list[bool] = []
    pre_collect_experience: list[bool] = []
    post_collect_experience: list[bool] = []
    pre_optimize_model: list[bool] = []
    post_optimize_model: list[bool] = []
    train_step: list[bool] = []
    algorithm.register_on_sample_problems(lambda x: sample_problems.append(True))
    algorithm.register_on_sample_initial_states(lambda x: sample_initial_states.append(True))
    algorithm.register_on_sample_goal_conditions(lambda x: sample_goal_conditions.append(True))
    algorithm.register_on_sample_trajectories(lambda x: sample_trajectories.append(True))
    algorithm.register_on_refine_trajectories(lambda x: refine_trajectories.append(True))
    algorithm.register_on_pre_collect_experience(lambda: pre_collect_experience.append(True))
    algorithm.register_on_post_collect_experience(lambda: post_collect_experience.append(True))
    algorithm.register_on_pre_optimize_model(lambda: pre_optimize_model.append(True))
    algorithm.register_on_post_optimize_model(lambda: post_optimize_model.append(True))
    algorithm.register_on_train_step(lambda x, l: train_step.append(True))
    algorithm.fit()
    assert len(sample_problems) == 1
    assert len(sample_initial_states) == 1
    assert len(sample_goal_conditions) == 1
    assert len(sample_trajectories) == 1
    assert len(refine_trajectories) == 1
    assert len(pre_collect_experience) == 1
    assert len(post_collect_experience) == 1
    assert len(pre_optimize_model) == 1
    assert len(post_optimize_model) == 1
    assert (len(train_step) == train_steps) or (len(train_step) == 0)


def test_value_based_initial_state_sampler():
    domain_path = DATA_DIR / 'gripper' / 'domain.pddl'
    problem_path = DATA_DIR / 'gripper' / 'problem.pddl'
    domain = mm.Domain(domain_path)
    problem = mm.Problem(domain, problem_path)
    problems: list[mm.Problem] = [problem] * 100
    model: ActionScalarModel = RGNNWrapper(domain)
    reward_function: RewardFunction = ConstantRewardFunction(-1)
    initial_state_sampler = TopValueInitialStateSampler(problems, model, reward_function, 0.5, 0.1, 10)
    # First, test without any additional states to the pool of initial states.
    # We expect to get the original initial state.
    sampled_initial_states_1 = initial_state_sampler.sample(problems)
    assert len(sampled_initial_states_1) == len(problems)
    assert all(sampled_initial_states_1[idx] == problem.get_initial_state() for idx, problem in enumerate(problems))
    # Second, test adding a bunch of states.
    trajectory_sampler: TrajectorySampler = BoltzmannTrajectorySampler(model, reward_function, 1.0)
    sampled_trajectory = trajectory_sampler.sample([(problem.get_initial_state(), problem.get_goal_condition()) for problem in problems], 100)
    for trajectory in sampled_trajectory:
        for transition in trajectory:
            initial_state_sampler.add_state(transition.current_state, transition.predicted_value)
    sampled_initial_states_2 = initial_state_sampler.sample(problems)
    assert len(sampled_initial_states_2) == len(problems)


def test_evaluation():
    domain_path = DATA_DIR / 'gripper' / 'domain.pddl'
    problem_path = DATA_DIR / 'gripper' / 'problem.pddl'
    domain = mm.Domain(domain_path)
    problem = mm.Problem(domain, problem_path)
    problems: list[mm.Problem] = [problem]
    model: ActionScalarModel = RGNNWrapper(domain)
    reward_function: RewardFunction = ConstantRewardFunction(-1)
    trajectory_sampler: TrajectorySampler = GreedyPolicyTrajectorySampler(model, reward_function)
    criterias: list[EvaluationCriteria] = [CoverageCriteria(), LengthCriteria(False), TDErrorCriteria(False)]
    horizon: int = 100
    evaluation = PolicyEvaluation(problems, criterias, trajectory_sampler, horizon)
    best1, result1 = evaluation.evaluate()
    best2, result2 = evaluation.evaluate()
    assert best1
    assert not best2
    assert result1 == result2


def test_iw_subtrajectory_sampler():
    domain_path = DATA_DIR / 'gripper' / 'domain.pddl'
    problem_path = DATA_DIR / 'gripper' / 'problem.pddl'
    domain = mm.Domain(domain_path)
    problem = mm.Problem(domain, problem_path)
    reward_function: RewardFunction = ConstantRewardFunction(-1)
    sampler = IWSubtrajectorySampler(reward_function, 2)
    subtrajectory = sampler.sample(problem.get_initial_state(), problem.get_goal_condition())
    assert isinstance(subtrajectory, Trajectory)
    subtrajectory.validate(False)
    assert len(subtrajectory) == 3


def test_trajectory_sampler_with_subtrajectories():
    domain_path = DATA_DIR / 'gripper' / 'domain.pddl'
    problem_path = DATA_DIR / 'gripper' / 'problem.pddl'
    domain = mm.Domain(domain_path)
    problem = mm.Problem(domain, problem_path)
    model: ActionScalarModel = RGNNWrapper(domain)
    reward_function: RewardFunction = ConstantRewardFunction(-1)
    subtrajectory_sampler = IWSubtrajectorySampler(reward_function, 2)
    trajectory_sampler = EpsilonGreedyTrajectorySampler(model, reward_function, 0.5, subtrajectory_sampler, 1.0)
    state_goals = [(problem.get_initial_state(), problem.get_goal_condition())]
    trajectories = trajectory_sampler.sample(state_goals, 100)
    assert isinstance(trajectories, list)
    assert len(trajectories) > 0
    trajectory = trajectories[0]
    trajectory.validate()
    assert trajectory.is_solution()
    assert len(trajectory) >= 3


# def test_lifted_ff():
#     domain_path = DATA_DIR / 'gripper' / 'domain.pddl'
#     problem_path = DATA_DIR / 'gripper' / 'problem.pddl'
#     domain = mm.Domain(domain_path)
#     problem = mm.Problem(domain, problem_path)
#     lifted_ff = LiftedFFHeuristic(problem, True)
#     initial_state = problem.get_initial_state()
#     initial_h_value = lifted_ff.compute_value(initial_state, False)
#     pass
