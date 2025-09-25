"""
UPAS Behavior Executor

Main behavior execution orchestrator using modular components.
"""

import asyncio
import logging
from typing import Dict, Any, Optional

from .base import BehaviorType, BehaviorConfig, BehaviorState
from .payload import PayloadBuilder, VariableResolver, CounterManager
from .state import ExecutionContext
from .scheduling import BehaviorScheduler
from .types import PeriodicBehavior, ReactiveBehavior, TriggeredBehavior
from .state_behaviors import StateOnlyBehaviorManager


class BehaviorExecutor:
    """
    Main behavior executor using modular components.

    This is the refactored version that maintains backward compatibility
    while using the new modular architecture.
    """

    def __init__(self, transport_layer=None):
        """Initialize behavior executor with modular components.

        :param transport_layer: Optional transport layer for integration tests
        :type transport_layer: TransportLayer or None
        """
        # Core components
        self.execution_context = ExecutionContext()
        self.variable_resolver = VariableResolver()
        self.counter_manager = CounterManager()
        self.payload_builder = PayloadBuilder(
            self.variable_resolver, self.counter_manager
        )
        self.scheduler = BehaviorScheduler(self.execution_context)

        # Store transport layer if provided
        if transport_layer:
            self.execution_context.transport_layer = transport_layer

        # Behavior management
        self.behaviors: Dict[str, BehaviorConfig] = {}
        self.behavior_executors: Dict[str, Any] = (
            {}
        )  # Store behavior executor functions
        self.state_behavior_manager = None  # Will be initialized after setup
        self.running = False
        self.logger = logging.getLogger(__name__)

    async def setup_behaviors(
        self,
        behaviors_config: Dict[str, Any],
        function_registry=None,
        state_machine=None,
        variables: Dict[str, Any] = None,
        transport_layer=None,
    ) -> None:
        """
        Setup behaviors from configuration.

        :param behaviors_config: Behaviors configuration dictionary
        :type behaviors_config: dict
        :param function_registry: Function registry for custom functions
        :type function_registry: object
        :param state_machine: State machine instance
        :type state_machine: object
        :param variables: Initial variables
        :type variables: dict
        :param transport_layer: Transport layer instance
        :type transport_layer: object
        """
        self.logger.info("Setting up behaviors")

        # Setup execution context
        self.execution_context.set_function_registry(function_registry)
        self.execution_context.set_state_machine(state_machine)
        self.execution_context.set_transport_layer(transport_layer)
        self.execution_context.set_behavior_executor(self)  # Add reference to self
        self.execution_context.set_variables(variables or {})

        # Update payload builder with function registry
        self.payload_builder.function_registry = function_registry

        # Setup variable resolver
        self.variable_resolver.variables.update(self.execution_context.variables)

        # Initialize state behavior manager
        self.state_behavior_manager = StateOnlyBehaviorManager(
            state_machine, self.logger
        )

        # Parse behaviors - support both dict and list formats
        if isinstance(behaviors_config, list):
            # Convert list format to dict format for compatibility
            behaviors_dict = {}
            for behavior_config in behaviors_config:
                behavior_id = behavior_config.get(
                    "id", f"behavior_{len(behaviors_dict)}"
                )
                behaviors_dict[behavior_id] = behavior_config
            behaviors_config = behaviors_dict

        for behavior_name, behavior_config in behaviors_config.items():
            try:
                behavior_type = BehaviorType(behavior_config.get("type", "periodic"))
                active_states = behavior_config.get("active_states")

                config = BehaviorConfig(
                    name=behavior_name,
                    type=behavior_type,
                    config=behavior_config,
                    active_states=active_states,
                )

                self.behaviors[behavior_name] = config
                self.logger.info(
                    f"Setup behavior: {behavior_name} ({behavior_type.value})"
                )

            except ValueError as e:
                self.logger.error(f"Invalid behavior type for {behavior_name}: {e}")
            except Exception as e:
                self.logger.error(f"Error setting up behavior {behavior_name}: {e}")

    async def start(self) -> None:
        """Start all behaviors."""
        self.logger.info("Starting behavior executor")
        self.running = True
        self.scheduler.running = True

        # Start all behaviors
        for behavior_name, behavior_config in self.behaviors.items():
            await self._start_behavior(behavior_name, behavior_config)

    async def stop(self) -> None:
        """Stop all behaviors."""
        self.logger.info("Stopping behavior executor")
        self.running = False

        # Stop all behaviors via scheduler
        await self.scheduler.stop_all_behaviors()

    def get_behavior(self, behavior_name: str) -> Optional[BehaviorConfig]:
        """Get a behavior configuration by name for compatibility with tests."""
        return self.behaviors.get(behavior_name)

    def load_behavior(self, behavior_config_dict: Dict[str, Any]):
        """
        Create a behavior instance from configuration dictionary for testing.

        :param behavior_config_dict: Dictionary containing behavior configuration
        :type behavior_config_dict: Dict[str, Any]
        :return: Behavior instance
        """
        # Convert string type to BehaviorType enum
        behavior_type_str = behavior_config_dict.get("type", "periodic")
        if behavior_type_str == "periodic":
            behavior_type = BehaviorType.PERIODIC
        elif behavior_type_str == "reactive":
            behavior_type = BehaviorType.REACTIVE
        elif behavior_type_str == "triggered" or behavior_type_str == "one_shot":
            behavior_type = BehaviorType.ONE_SHOT
        else:
            behavior_type = BehaviorType.PERIODIC  # default

        # Create BehaviorConfig object
        config = BehaviorConfig(
            name=behavior_config_dict.get("id", "test_behavior"),
            type=behavior_type,
            config=behavior_config_dict,
        )

        # Create and return appropriate behavior instance
        if behavior_type == BehaviorType.PERIODIC:
            return PeriodicBehavior(
                config.name,
                config,
                self.payload_builder,
                self.execution_context,
            )
        elif behavior_type == BehaviorType.REACTIVE:
            return ReactiveBehavior(
                config.name,
                config,
                self.payload_builder,
                self.execution_context,
            )
        elif behavior_type == BehaviorType.ONE_SHOT:
            return TriggeredBehavior(
                config.name,
                config,
                self.payload_builder,
                self.execution_context,
            )
        else:
            raise ValueError(f"Unsupported behavior type: {behavior_type}")

    async def _start_behavior(
        self, behavior_name: str, behavior_config: BehaviorConfig
    ) -> None:
        """
        Start a specific behavior using the new modular approach.

        :param behavior_name: Name of the behavior
        :type behavior_name: str
        :param behavior_config: Behavior configuration
        :type behavior_config: BehaviorConfig
        """
        try:
            # Create behavior executor function based on type
            if behavior_config.type == BehaviorType.PERIODIC:
                behavior_instance = PeriodicBehavior(
                    behavior_name,
                    behavior_config,
                    self.payload_builder,
                    self.execution_context,
                )
                executor_func = behavior_instance.execute
            elif behavior_config.type == BehaviorType.REACTIVE:
                behavior_instance = ReactiveBehavior(
                    behavior_name,
                    behavior_config,
                    self.payload_builder,
                    self.execution_context,
                )
                executor_func = behavior_instance.execute
            elif behavior_config.type == BehaviorType.ONE_SHOT:
                behavior_instance = TriggeredBehavior(
                    behavior_name,
                    behavior_config,
                    self.payload_builder,
                    self.execution_context,
                )
                executor_func = behavior_instance.execute
            elif behavior_config.type == BehaviorType.STATE_ONLY:
                # Create state-only behavior
                state_behavior = self.state_behavior_manager.create_state_behavior(
                    behavior_config.config
                )
                executor_func = state_behavior.execute
            else:
                self.logger.error(f"Unknown behavior type: {behavior_config.type}")
                return

            # Start behavior via scheduler
            await self.scheduler.start_behavior(
                behavior_name, behavior_config, executor_func
            )

            # Store executor function for potential restart
            self.behavior_executors[behavior_name] = executor_func

        except Exception as e:
            self.logger.error(f"Error starting behavior {behavior_name}: {e}")

    def on_state_change(self, new_state: str) -> None:
        """
        Handle state machine state changes.

        :param new_state: New state
        :type new_state: str
        """
        self.logger.info(f"BehaviorExecutor: Handling state change to {new_state}")

        # Delegate to scheduler first
        self.scheduler.on_state_change(new_state, self.behaviors)

        # Now handle behaviors that need to be restarted
        self.logger.info(
            f"BehaviorExecutor: Creating restart task for state {new_state}"
        )
        asyncio.create_task(self._restart_behaviors_for_state(new_state))

    async def _restart_behaviors_for_state(self, new_state: str) -> None:
        """
        Restart behaviors that should run in the new state.

        :param new_state: New state
        :type new_state: str
        """
        self.logger.info(
            f"BehaviorExecutor: _restart_behaviors_for_state called for {new_state}"
        )

        for behavior_name, behavior_config in self.behaviors.items():
            self.logger.info(
                f"BehaviorExecutor: Checking behavior {behavior_name} for state {new_state}"
            )

            should_run = self.execution_context.should_behavior_run(
                behavior_config.active_states
            )
            is_running = (
                behavior_name in self.scheduler.behavior_tasks
                and not self.scheduler.behavior_tasks[behavior_name].done()
            )

            self.logger.info(
                f"BehaviorExecutor: Behavior {behavior_name} - should_run: {should_run}, is_running: {is_running}, active_states: {behavior_config.active_states}"
            )

            # Restart behaviors that should run but aren't running (especially one_shot)
            if should_run and not is_running:
                self.logger.info(
                    f"BehaviorExecutor: Restarting behavior {behavior_name} for state {new_state}"
                )
                if behavior_name in self.behavior_executors:
                    await self.scheduler.start_behavior(
                        behavior_name,
                        behavior_config,
                        self.behavior_executors[behavior_name],
                    )
                else:
                    self.logger.error(
                        f"BehaviorExecutor: No executor function found for {behavior_name}"
                    )

    # Backward compatibility properties and methods
    @property
    def behavior_states(self) -> Dict[str, BehaviorState]:
        """Get behavior states for backward compatibility."""
        return self.scheduler.behavior_states

    @property
    def behavior_tasks(self) -> Dict[str, asyncio.Task]:
        """Get behavior tasks for backward compatibility."""
        return self.scheduler.behavior_tasks

    @property
    def variables(self) -> Dict[str, Any]:
        """Get variables for backward compatibility."""
        return self.execution_context.variables

    @variables.setter
    def variables(self, value: Dict[str, Any]) -> None:
        """Set variables for backward compatibility."""
        self.execution_context.set_variables(value)
        self.variable_resolver.variables.update(value)

    @property
    def function_registry(self):
        """Get function registry for backward compatibility."""
        return self.execution_context.function_registry

    @function_registry.setter
    def function_registry(self, value) -> None:
        """Set function registry for backward compatibility."""
        self.execution_context.set_function_registry(value)
        self.payload_builder.function_registry = value

    @property
    def state_machine(self):
        """Get state machine for backward compatibility."""
        return self.execution_context.state_machine

    @state_machine.setter
    def state_machine(self, value) -> None:
        """Set state machine for backward compatibility."""
        self.execution_context.set_state_machine(value)

    @property
    def transport_layer(self):
        """Get transport layer for backward compatibility."""
        return self.execution_context.transport_layer

    @transport_layer.setter
    def transport_layer(self, value) -> None:
        """Set transport layer for backward compatibility."""
        self.execution_context.set_transport_layer(value)
