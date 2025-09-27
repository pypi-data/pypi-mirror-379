# SPDX-FileCopyrightText: Copyright (c) 2025 The Newton Developers
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest

import warp as wp

import newton
from newton.solvers import SolverMuJoCo, SolverNotifyFlags


class TestJointDrive(unittest.TestCase):
    def compute_expected_velocity_outcome(
        self,
        env_id,
        g,
        dt,
        joint_type,
        free_axis,
        drive_mode,
        targets,
        target_kes,
        target_kds,
        joint_qs,
        joint_qds,
        masses,
        inertias,
    ) -> float:
        target = targets[env_id]
        ke = target_kes[env_id]
        kd = target_kds[env_id]
        q = joint_qs[env_id]
        qd = joint_qds[env_id]
        mass = masses[env_id]
        inertia = inertias[env_id]

        M = 0.0
        if joint_type == newton.JointType.PRISMATIC:
            M = mass
        elif joint_type == newton.JointType.REVOLUTE:
            M = inertia[free_axis][free_axis]
        else:
            print("unsupported joint type")

        F = 0
        if drive_mode == newton.JointMode.TARGET_POSITION:
            F = ke * (target - q) - (kd * qd)
        elif drive_mode == newton.JointMode.TARGET_VELOCITY:
            F = kd * (target - qd)

        F += M * g

        qdNew = qd + F * dt / M
        return qdNew

    def run_test_joint_drive_no_limits(self, is_prismatic: bool, world_up_axis: int, joint_motion_axis: int):
        g = 0.0
        if is_prismatic and world_up_axis == joint_motion_axis:
            g = 5.0

        dt = 0.01

        joint_type = newton.JointType.PRISMATIC
        if is_prismatic:
            joint_type = newton.JointType.PRISMATIC
        else:
            joint_type = newton.JointType.REVOLUTE

        nb_envs = 2
        body_masses = [10.0, 20.0]
        body_coms = [wp.vec3(0.0, 0.0, 0.0), wp.vec3(0.0, 0.0, 0.0)]
        body_inertias = [
            wp.mat33(4.0, 0.0, 0.0, 0.0, 4.0, 0.0, 0.0, 0.0, 4.0),
            wp.mat33(8.0, 0.0, 0.0, 0.0, 8.0, 0.0, 0.0, 0.0, 8.0),
        ]
        joint_start_positions = [100.0, 205.0]
        joint_start_velocities = [10.0, 25.0]
        joint_drive_targets = [200.0, 300.0]
        joint_drive_stiffnesses = [100.0, 200.0]
        joint_drive_dampings = [10.0, 20.0]

        world_builder = newton.ModelBuilder(gravity=g, up_axis=world_up_axis)
        for i in range(0, nb_envs):
            body_mass = body_masses[i]
            body_com = body_coms[i]
            body_inertia = body_inertias[i]
            drive_stiffness = joint_drive_stiffnesses[i]
            joint_drive_target_position = joint_drive_targets[i]
            joint_drive_damping = joint_drive_dampings[i]
            joint_start_position = joint_start_positions[i]
            joint_start_velocity = joint_start_velocities[i]

            # Create a single body jointed to the world with a prismatic joint
            # Make sure that we use the mass properties specified here by setting shape density to 0.0
            environment_builder = newton.ModelBuilder(gravity=g, up_axis=world_up_axis)
            bodyIndex = environment_builder.add_body(mass=body_mass, I_m=body_inertia, armature=0.0, com=body_com)
            environment_builder.add_shape_sphere(
                radius=1.0, body=bodyIndex, cfg=newton.ModelBuilder.ShapeConfig(density=0.0, has_shape_collision=False)
            )
            if is_prismatic:
                environment_builder.add_joint_prismatic(
                    mode=newton.JointMode.TARGET_POSITION,
                    axis=joint_motion_axis,
                    parent=-1,
                    child=bodyIndex,
                    target=joint_drive_target_position,
                    target_ke=drive_stiffness,
                    target_kd=joint_drive_damping,
                    armature=0.0,
                    effort_limit=1000000000000.0,
                    velocity_limit=100000000000000000.0,
                    friction=0.0,
                )
            else:
                environment_builder.add_joint_revolute(
                    mode=newton.JointMode.TARGET_POSITION,
                    axis=joint_motion_axis,
                    parent=-1,
                    child=bodyIndex,
                    target=joint_drive_target_position,
                    target_ke=drive_stiffness,
                    target_kd=joint_drive_damping,
                    armature=0.0,
                    effort_limit=1000000000000.0,
                    velocity_limit=100000000000000000.0,
                    friction=0.0,
                )

            world_builder.add_builder(environment_builder)

            # Set the start pos and vel of the dof.
            world_builder.joint_q[i] = joint_start_position
            world_builder.joint_qd[i] = joint_start_velocity

        # Create the MujocoSolver instance
        model = world_builder.finalize()
        state_in = model.state()
        state_out = model.state()
        control = model.control()
        contacts = model.collide(state_in)
        newton.eval_fk(model, model.joint_q, model.joint_qd, state_in)
        solver = SolverMuJoCo(model, iterations=1, ls_iterations=1, disable_contacts=True, use_mujoco_cpu=False)

        # Compute the expected velocity outcome after a single sim step.
        vNew = [0.0] * nb_envs
        for i in range(0, nb_envs):
            vNew[i] = self.compute_expected_velocity_outcome(
                env_id=i,
                g=g,
                dt=dt,
                joint_type=joint_type,
                free_axis=joint_motion_axis,
                drive_mode=newton.JointMode.TARGET_POSITION,
                targets=joint_drive_targets,
                target_kes=joint_drive_stiffnesses,
                target_kds=joint_drive_dampings,
                joint_qs=joint_start_positions,
                joint_qds=joint_start_velocities,
                masses=body_masses,
                inertias=body_inertias,
            )

        # Perform 1 sim step.
        solver.step(state_in=state_in, state_out=state_out, contacts=contacts, control=control, dt=dt)
        for i in range(0, nb_envs):
            self.assertAlmostEqual(vNew[i], state_out.joint_qd.numpy()[i], delta=0.0001)
        state_in, state_out = state_out, state_in

        #########################

        # Update the stiffness and damping values and reset to start state stored in model.joint_q and model.joint_qd
        joint_drive_stiffnesses[0] *= 2.0
        joint_drive_stiffnesses[1] *= 2.5
        joint_drive_dampings[0] *= 2.75
        joint_drive_dampings[1] *= 3.5
        model.joint_target_ke.assign(joint_drive_stiffnesses)
        model.joint_target_kd.assign(joint_drive_dampings)
        state_in.joint_q.assign(joint_start_positions)
        state_in.joint_qd.assign(joint_start_velocities)
        newton.eval_fk(model, state_in.joint_q, state_in.joint_qd, state_in)

        # Recompute the expected velocity outcomes
        for i in range(0, nb_envs):
            vNew[i] = self.compute_expected_velocity_outcome(
                env_id=i,
                g=g,
                dt=dt,
                joint_type=joint_type,
                free_axis=joint_motion_axis,
                drive_mode=newton.JointMode.TARGET_POSITION,
                targets=joint_drive_targets,
                target_kes=joint_drive_stiffnesses,
                target_kds=joint_drive_dampings,
                joint_qs=joint_start_positions,
                joint_qds=joint_start_velocities,
                masses=body_masses,
                inertias=body_inertias,
            )

        # Run a sim step with the new values of ke and kd
        solver.notify_model_changed(SolverNotifyFlags.JOINT_DOF_PROPERTIES)
        solver.step(state_in=state_in, state_out=state_out, contacts=contacts, control=control, dt=dt)
        for i in range(0, nb_envs):
            self.assertAlmostEqual(vNew[i], state_out.joint_qd.numpy()[i], delta=0.0001)
        state_in, state_out = state_out, state_in

        ################################

        # Change the mode of the joint drives to velocity drive, update the drive targets, and reset to start state
        # Note the drive modes need to be identical.
        joint_drive_targets = [20.0, 300.0]
        joint_drive_stiffnesses = [100.0, 200.0]
        joint_drive_dampings = [10.0, 20.0]
        joint_start_positions = [0.0, 0.0]
        joint_start_velocities = [0.0, 0.0]
        joint_dof_modes = [newton.JointMode.TARGET_VELOCITY, newton.JointMode.TARGET_VELOCITY]
        model.joint_dof_mode.assign(joint_dof_modes)
        model.joint_target_ke.assign(joint_drive_stiffnesses)
        model.joint_target_kd.assign(joint_drive_dampings)
        control.joint_target.assign(joint_drive_targets)
        state_in.joint_q.assign(joint_start_positions)
        state_in.joint_qd.assign(joint_start_velocities)
        newton.eval_fk(model, state_in.joint_q, state_in.joint_qd, state_in)

        # Recompute the expected velocity outcomes
        for i in range(0, nb_envs):
            vNew[i] = self.compute_expected_velocity_outcome(
                env_id=i,
                g=g,
                dt=dt,
                joint_type=joint_type,
                free_axis=joint_motion_axis,
                drive_mode=joint_dof_modes[i],
                targets=joint_drive_targets,
                target_kes=joint_drive_stiffnesses,
                target_kds=joint_drive_dampings,
                joint_qs=joint_start_positions,
                joint_qds=joint_start_velocities,
                masses=body_masses,
                inertias=body_inertias,
            )

        # Run a sim step with the new drive type
        solver.notify_model_changed(SolverNotifyFlags.JOINT_DOF_PROPERTIES)
        solver.step(state_in=state_in, state_out=state_out, contacts=contacts, control=control, dt=dt)
        for i in range(0, nb_envs):
            self.assertAlmostEqual(vNew[i], state_out.joint_qd.numpy()[i], delta=0.0001)
        state_in, state_out = state_out, state_in

        ################################

        # Now run again with JointMode.NONE and reset back to the start state.

        joint_dof_modes = [newton.JointMode.NONE, newton.JointMode.NONE]
        model.joint_dof_mode.assign(joint_dof_modes)
        state_in.joint_q.assign(joint_start_positions)
        state_in.joint_qd.assign(joint_start_velocities)
        newton.eval_fk(model, state_in.joint_q, state_in.joint_qd, state_in)

        # Recompute the expected velocity outcomes
        for i in range(0, nb_envs):
            vNew[i] = self.compute_expected_velocity_outcome(
                env_id=i,
                g=g,
                dt=dt,
                joint_type=joint_type,
                free_axis=joint_motion_axis,
                drive_mode=joint_dof_modes[i],
                targets=joint_drive_targets,
                target_kes=joint_drive_stiffnesses,
                target_kds=joint_drive_dampings,
                joint_qs=joint_start_positions,
                joint_qds=joint_start_velocities,
                masses=body_masses,
                inertias=body_inertias,
            )

        # Run a sim step with the new drive type
        solver.notify_model_changed(SolverNotifyFlags.JOINT_DOF_PROPERTIES)
        solver.step(state_in=state_in, state_out=state_out, contacts=contacts, control=control, dt=dt)
        for i in range(0, nb_envs):
            self.assertAlmostEqual(vNew[i], state_out.joint_qd.numpy()[i], delta=0.0001)

    def test_joint_drive_prismatic_upX_motionX(self):
        self.run_test_joint_drive_no_limits(True, 0, 0)

    def test_joint_drive_prismatic_upX_motionY(self):
        self.run_test_joint_drive_no_limits(True, 0, 1)

    def test_joint_drive_prismatic_upX_motionZ(self):
        self.run_test_joint_drive_no_limits(True, 0, 2)

    def test_joint_drive_prismatic_upY_motionX(self):
        self.run_test_joint_drive_no_limits(True, 1, 0)

    def test_joint_drive_prismatic_upY_motionY(self):
        self.run_test_joint_drive_no_limits(True, 1, 1)

    def test_joint_drive_prismatic_upY_motionZ(self):
        self.run_test_joint_drive_no_limits(True, 1, 2)

    def test_joint_drive_prismatic_upZ_motionX(self):
        self.run_test_joint_drive_no_limits(True, 2, 0)

    def test_joint_drive_prismatic_upZ_motionY(self):
        self.run_test_joint_drive_no_limits(True, 2, 1)

    def test_joint_drive_prismatic_upZ_motionZ(self):
        self.run_test_joint_drive_no_limits(True, 2, 2)

    def test_joint_drive_revolute_upX_motionX(self):
        self.run_test_joint_drive_no_limits(False, 0, 0)

    def test_joint_drive_revolute_upX_motionY(self):
        self.run_test_joint_drive_no_limits(False, 0, 1)

    def test_joint_drive_revolute_upX_motionZ(self):
        self.run_test_joint_drive_no_limits(False, 0, 2)

    def test_joint_drive_revolute_upY_motionX(self):
        self.run_test_joint_drive_no_limits(False, 1, 0)

    def test_joint_drive_revolute_upY_motionY(self):
        self.run_test_joint_drive_no_limits(False, 1, 1)

    def test_joint_drive_revolute_upY_motionZ(self):
        self.run_test_joint_drive_no_limits(False, 1, 2)

    def test_joint_drive_revolute_upZ_motionX(self):
        self.run_test_joint_drive_no_limits(False, 2, 0)

    def test_joint_drive_revolute_upZ_motionY(self):
        self.run_test_joint_drive_no_limits(False, 2, 1)

    def test_joint_drive_revolute_upZ_motionZ(self):
        self.run_test_joint_drive_no_limits(False, 2, 2)


if __name__ == "__main__":
    wp.clear_kernel_cache()
    unittest.main(verbosity=2)
