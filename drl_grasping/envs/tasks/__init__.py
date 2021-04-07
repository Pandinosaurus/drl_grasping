from gym.envs.registration import register

from .reach import Reach, ReachColorImage, ReachDepthImage, ReachOctree
from .grasp import Grasp, GraspOctree

# Reach
REACH_MAX_EPISODE_STEPS: int = 100
REACH_AGENT_RATE: float = 2.5
REACH_PHYSICS_RATE: float = 100.0
REACH_RTF: float = 15.0
register(
    id='Reach-Gazebo-v0',
    entry_point='gym_ignition.runtimes.gazebo_runtime:GazeboRuntime',
    max_episode_steps=REACH_MAX_EPISODE_STEPS,
    kwargs={'task_cls': Reach,
            'agent_rate': REACH_AGENT_RATE,
            'physics_rate': REACH_PHYSICS_RATE,
            'real_time_factor': REACH_RTF,
            'restrict_position_goal_to_workspace': True,
            'sparse_reward': False,
            'act_quick_reward': -0.01,
            'required_accuracy': 0.05,
            'verbose': False,
            })
register(
    id='Reach-ColorImage-Gazebo-v0',
    entry_point='gym_ignition.runtimes.gazebo_runtime:GazeboRuntime',
    max_episode_steps=REACH_MAX_EPISODE_STEPS,
    kwargs={'task_cls': ReachColorImage,
            'agent_rate': REACH_AGENT_RATE,
            'physics_rate': REACH_PHYSICS_RATE,
            'real_time_factor': REACH_RTF,
            'restrict_position_goal_to_workspace': True,
            'sparse_reward': False,
            'act_quick_reward': -0.01,
            'required_accuracy': 0.05,
            'verbose': False,
            })
register(
    id='Reach-DepthImage-Gazebo-v0',
    entry_point='gym_ignition.runtimes.gazebo_runtime:GazeboRuntime',
    max_episode_steps=REACH_MAX_EPISODE_STEPS,
    kwargs={'task_cls': ReachDepthImage,
            'agent_rate': REACH_AGENT_RATE,
            'physics_rate': REACH_PHYSICS_RATE,
            'real_time_factor': REACH_RTF,
            'restrict_position_goal_to_workspace': True,
            'sparse_reward': False,
            'act_quick_reward': -0.01,
            'required_accuracy': 0.05,
            'verbose': False,
            })
register(
    id='Reach-Octree-Gazebo-v0',
    entry_point='gym_ignition.runtimes.gazebo_runtime:GazeboRuntime',
    max_episode_steps=REACH_MAX_EPISODE_STEPS,
    kwargs={'task_cls': ReachOctree,
            'agent_rate': REACH_AGENT_RATE,
            'physics_rate': REACH_PHYSICS_RATE,
            'real_time_factor': REACH_RTF,
            'restrict_position_goal_to_workspace': True,
            'sparse_reward': False,
            'act_quick_reward': -0.01,
            'required_accuracy': 0.05,
            'octree_depth': 5,
            'octree_full_depth': 2,
            'octree_include_color': False,
            'octree_n_stacked': 2,
            'octree_max_size': 20000,
            'verbose': False,
            })
register(
    id='Reach-OctreeWithColor-Gazebo-v0',
    entry_point='gym_ignition.runtimes.gazebo_runtime:GazeboRuntime',
    max_episode_steps=REACH_MAX_EPISODE_STEPS,
    kwargs={'task_cls': ReachOctree,
            'agent_rate': REACH_AGENT_RATE,
            'physics_rate': REACH_PHYSICS_RATE,
            'real_time_factor': REACH_RTF,
            'restrict_position_goal_to_workspace': True,
            'sparse_reward': False,
            'act_quick_reward': -0.01,
            'required_accuracy': 0.05,
            'octree_depth': 4,
            'octree_full_depth': 2,
            'octree_include_color': True,
            'octree_n_stacked': 2,
            'octree_max_size': 35000,
            'verbose': False,
            })

# Grasp
GRASP_MAX_EPISODE_STEPS: int = 100
GRASP_AGENT_RATE: float = 2.5
GRASP_PHYSICS_RATE: float = 250.0
GRASP_RTF: float = 10.0
register(
    id='Grasp-Octree-Gazebo-v0',
    entry_point='gym_ignition.runtimes.gazebo_runtime:GazeboRuntime',
    max_episode_steps=GRASP_MAX_EPISODE_STEPS,
    kwargs={'task_cls': GraspOctree,
            'agent_rate': GRASP_AGENT_RATE,
            'physics_rate': GRASP_PHYSICS_RATE,
            'real_time_factor': GRASP_RTF,
            'restrict_position_goal_to_workspace': True,
            'gripper_dead_zone': 0.25,
            'full_3d_orientation': False,
            'sparse_reward': False,
            'normalize_reward': True,
            'required_reach_distance': 0.1,
            'required_lift_height': 0.25,
            'reach_dense_reward_multiplier': 2.0,
            'lift_dense_reward_multiplier': 4.0,
            'act_quick_reward': 0.0,
            'outside_workspace_reward': 0.0,
            'ground_collision_reward': 0.0,
            'n_ground_collisions_till_termination': 1,
            'curriculum_enable_workspace_scale': True,
            'curriculum_min_workspace_scale': 0.4,
            'curriculum_enable_stages': False,
            'curriculum_stage_reward_multiplier': 2.0,
            'curriculum_stage_increase_rewards': True,
            'curriculum_success_rate_threshold': 0.6,
            'curriculum_success_rate_rolling_average_n': 50,
            'curriculum_restart_every_n_steps': 0,
            'curriculum_skip_reach_stage': False,
            'curriculum_skip_grasp_stage': True,
            'curriculum_restart_exploration_at_start': False,
            'max_episode_length': GRASP_MAX_EPISODE_STEPS,
            'octree_depth': 5,
            'octree_full_depth': 2,
            'octree_include_color': False,
            'octree_n_stacked': 2,
            'octree_max_size': 75000,
            'proprieceptive_observations': True,
            'verbose': False})
# register(
#     id='Grasp-OctreeWithColor-Gazebo-v0',
#     entry_point='gym_ignition.runtimes.gazebo_runtime:GazeboRuntime',
#     max_episode_steps=GRASP_MAX_EPISODE_STEPS,
#     kwargs={'task_cls': GraspOctree,
#             'agent_rate': GRASP_AGENT_RATE,
#             'physics_rate': GRASP_PHYSICS_RATE,
#             'real_time_factor': GRASP_RTF,
#             'restrict_position_goal_to_workspace': True,
#             'gripper_dead_zone': 0.25,
#             'full_3d_orientation': False,
#             'sparse_reward': True,
#             'normalize_reward': False,
#             'required_reach_distance': 0.1,
#             'required_lift_height': 0.15,
#             'reach_dense_reward_multiplier': 5.0,
#             'lift_dense_reward_multiplier': 10.0,
#             'act_quick_reward': 0.005,
#             'outside_workspace_reward': 0.0,
#             'ground_collision_reward': 1.0,
#             'n_ground_collisions_till_termination': 1,
#             # Workspace scaling should be disabled for evaluation, collecting demonstrations, etc.
#             'curriculum_enable_workspace_scale': True,
#             'curriculum_min_workspace_scale': 0.1,
#             'curriculum_enable_object_count_increase': True,
#             'curriculum_max_object_count': 4,
#             # Curriculum stages should be disabled for evaluation, collecting demonstrations, etc.
#             'curriculum_enable_stages': True,
#             'curriculum_stage_reward_multiplier': 4.0,
#             'curriculum_stage_increase_rewards': True,
#             'curriculum_success_rate_threshold': 0.75,
#             'curriculum_success_rate_rolling_average_n': 100,
#             'curriculum_restart_every_n_steps': 0,
#             'curriculum_skip_reach_stage': False,
#             'curriculum_skip_grasp_stage': True,
#             # Exploration should be restarted if we continue training a pre-trained agent
#             'curriculum_restart_exploration_at_start': False,
#             'max_episode_length': GRASP_MAX_EPISODE_STEPS,
#             'octree_depth': 4,
#             'octree_full_depth': 2,
#             'octree_include_color': True,
#             'octree_n_stacked': 3,
#             'octree_max_size': 75000,
#             'proprieceptive_observations': True,
#             # Important: 'preload_replay_buffer' can only be enabled if using demonstrations to fill replay buffer. Make sure this is disabled otherwise
#             # 'preload_replay_buffer': False,
#             'verbose': False})


# # For optimization
# register(
#     id='Grasp-OctreeWithColor-Gazebo-v0',
#     entry_point='gym_ignition.runtimes.gazebo_runtime:GazeboRuntime',
#     max_episode_steps=GRASP_MAX_EPISODE_STEPS,
#     kwargs={'task_cls': GraspOctree,
#             'agent_rate': GRASP_AGENT_RATE,
#             'physics_rate': GRASP_PHYSICS_RATE,
#             'real_time_factor': GRASP_RTF,
#             'restrict_position_goal_to_workspace': True,
#             'gripper_dead_zone': 0.25,
#             'full_3d_orientation': False,
#             'sparse_reward': True,
#             'normalize_reward': True,
#             'required_reach_distance': 0.1,
#             'required_lift_height': 0.125,
#             'reach_dense_reward_multiplier': 5.0,
#             'lift_dense_reward_multiplier': 10.0,
#             'act_quick_reward': 0.0,
#             'outside_workspace_reward': 0.0,
#             'ground_collision_reward': 0.0,
#             'n_ground_collisions_till_termination': 2,
#             # Workspace scaling should be disabled for evaluation, collecting demonstrations, etc.
#             'curriculum_enable_workspace_scale': True,
#             'curriculum_min_workspace_scale': 0.1,
#             'curriculum_enable_object_count_increase': True,
#             'curriculum_max_object_count': 4,
#             # Curriculum stages should be disabled for evaluation, collecting demonstrations, etc.
#             'curriculum_enable_stages': False,
#             'curriculum_stage_reward_multiplier': 5.0,
#             'curriculum_stage_increase_rewards': True,
#             'curriculum_success_rate_threshold': 0.75,
#             'curriculum_success_rate_rolling_average_n': 100,
#             'curriculum_restart_every_n_steps': 0,
#             'curriculum_skip_reach_stage': False,
#             'curriculum_skip_grasp_stage': True,
#             'curriculum_restart_exploration_at_start': False,
#             'max_episode_length': GRASP_MAX_EPISODE_STEPS,
#             'octree_depth': 4,
#             'octree_full_depth': 2,
#             'octree_include_color': True,
#             'octree_n_stacked': 3,
#             'octree_max_size': 75000,
#             'proprieceptive_observations': True,
#             # Important: 'preload_replay_buffer' can only be enabled if using demonstrations to fill replay buffer. Make sure this is disabled otherwise
#             # 'preload_replay_buffer': False,
#             'verbose': False})

# # For optimization
# register(
#     id='Grasp-OctreeWithColor-Gazebo-v0',
#     entry_point='gym_ignition.runtimes.gazebo_runtime:GazeboRuntime',
#     max_episode_steps=GRASP_MAX_EPISODE_STEPS,
#     kwargs={'task_cls': GraspOctree,
#             'agent_rate': GRASP_AGENT_RATE,
#             'physics_rate': GRASP_PHYSICS_RATE,
#             'real_time_factor': GRASP_RTF,
#             'restrict_position_goal_to_workspace': True,
#             'gripper_dead_zone': 0.25,
#             'full_3d_orientation': False,
#             'sparse_reward': True,
#             'normalize_reward': False,
#             'required_reach_distance': 0.1,
#             'required_lift_height': 0.125,
#             'reach_dense_reward_multiplier': 5.0,
#             'lift_dense_reward_multiplier': 10.0,
#             'act_quick_reward': 0.0,
#             'outside_workspace_reward': 0.0,
#             'ground_collision_reward': 0.0,
#             'n_ground_collisions_till_termination': 1,
#             # Workspace scaling should be disabled for evaluation, collecting demonstrations, etc.
#             'curriculum_enable_workspace_scale': True,
#             'curriculum_min_workspace_scale': 0.1,
#             'curriculum_enable_object_count_increase': False,
#             'curriculum_max_object_count': 4,
#             # Curriculum stages should be disabled for evaluation, collecting demonstrations, etc.
#             'curriculum_enable_stages': False,
#             'curriculum_stage_reward_multiplier': 2.0,
#             'curriculum_stage_increase_rewards': True,
#             'curriculum_success_rate_threshold': 0.75,
#             'curriculum_success_rate_rolling_average_n': 100,
#             'curriculum_restart_every_n_steps': 0,
#             'curriculum_skip_reach_stage': False,
#             'curriculum_skip_grasp_stage': True,
#             'curriculum_restart_exploration_at_start': False,
#             'max_episode_length': GRASP_MAX_EPISODE_STEPS,
#             'octree_depth': 4,
#             'octree_full_depth': 2,
#             'octree_include_color': True,
#             # robotlab - 2
#             'octree_n_stacked': 1,
#             'octree_max_size': 75000,
#             'proprieceptive_observations': False,
#             # Important: 'preload_replay_buffer' can only be enabled if using demonstrations to fill replay buffer. Make sure this is disabled otherwise
#             # 'preload_replay_buffer': False,
#             'verbose': False})

register(
    id='Grasp-OctreeWithColor-Gazebo-v0',
    entry_point='gym_ignition.runtimes.gazebo_runtime:GazeboRuntime',
    # entry_point='drl_grasping.envs.runtimes:RealEvaluationRuntimeManual',
    max_episode_steps=GRASP_MAX_EPISODE_STEPS,
    kwargs={'task_cls': GraspOctree,
            'agent_rate': GRASP_AGENT_RATE,
            'physics_rate': GRASP_PHYSICS_RATE,
            'real_time_factor': GRASP_RTF,
            'restrict_position_goal_to_workspace': True,
            'gripper_dead_zone': 0.25,
            'full_3d_orientation': False,
            'sparse_reward': True,
            'normalize_reward': False,
            'required_reach_distance': 0.1,
            'required_lift_height': 0.125,
            'reach_dense_reward_multiplier': 5.0,
            'lift_dense_reward_multiplier': 10.0,
            'act_quick_reward': 0.005,
            'outside_workspace_reward': 0.0,
            'ground_collision_reward': 1.0,
            # TODO: Try changing to GRASP_MAX_EPISODE_STEPS
            'n_ground_collisions_till_termination': GRASP_MAX_EPISODE_STEPS,
            # Workspace scaling should be disabled for evaluation, collecting demonstrations, etc.
            'curriculum_enable_workspace_scale': True,
            'curriculum_min_workspace_scale': 0.1,
            'curriculum_enable_object_count_increase': True,
            'curriculum_max_object_count': 4,
            # Curriculum stages should be disabled for evaluation, collecting demonstrations, etc.
            'curriculum_enable_stages': False,
            'curriculum_stage_reward_multiplier': 4.0,
            'curriculum_stage_increase_rewards': True,
            'curriculum_success_rate_threshold': 0.75,
            'curriculum_success_rate_rolling_average_n': 100,
            'curriculum_restart_every_n_steps': 0,
            'curriculum_skip_reach_stage': False,
            'curriculum_skip_grasp_stage': True,
            'curriculum_restart_exploration_at_start': False,
            'max_episode_length': GRASP_MAX_EPISODE_STEPS,
            'octree_depth': 4,
            'octree_full_depth': 2,
            'octree_include_color': True,
            'octree_n_stacked': 3,
            'octree_max_size': 75000,
            'proprieceptive_observations': True,
            # Important: 'preload_replay_buffer' can only be enabled if using demonstrations to fill replay buffer. Make sure this is disabled otherwise
            # 'preload_replay_buffer': False,
            'verbose': False})
