# Apurva Gandhi
# Mini-project2
# KBAI 7637
import copy

class BlockWorldAgent:
    def __init__(self):
        pass

    def solve(self, initial_arrangement, goal_arrangement):
        class State:
            # Initializes the object and sets the values of initial_stacks, goal_stack, total_blocks and moves attributes.
            # If moves is not provided, it is set to an empty list.
            def __init__(self, initial_stacks, goal_stack, total_blocks, moves=None):
                self.initial_stacks = initial_stacks
                self.goal_stack = goal_stack
                self.total_blocks = total_blocks
                self.moves = moves or []

                # Overrides the equality operator to compare two State objects based on
                # their values of initial_stacks, goal_stack, total_blocks, and moves.
            def __eq__(self, other):
                return (self.initial_stacks == other.initial_stacks and self.goal_stack == other.goal_stack
                        and self.total_blocks == other.total_blocks and self.moves == other.moves)
                # Returns the list of moves required to reach the goal state. It does this by repeatedly
                # calling find_move until the difference between the initial and goal state is zero.

            def get_goal_state(self):
                while self.find_difference() != 0:
                    self = self.find_move()
                return self.moves

                # Selects the best move that reduces the difference between the initial and goal state.
                # The function tries to move the top block from one stack to another.
                # If the difference is reduced, it returns the new state.
            def find_move(self):
                # Iterates over the list twice, with two nested loops, and compares each pair
                # of stacks to see if a move can be made. If a move can be made, the function calls the
                # validate_move method with the current self.initial_stacks list, the indices of the two
                # stacks being compared, and the index of the destination stack (-1 means a table)
                for i, stack in enumerate(self.initial_stacks):
                    for j, stack2 in enumerate(self.initial_stacks):
                        if i != j:
                            current_stack, move = self.validate_move(
                                self.initial_stacks, i, j)
                            # Following is done to see if the new move that is being made, reduces the difference
                            new_state = State(
                                current_stack, self.goal_stack, self.total_blocks, copy.copy(self.moves))
                            new_state.moves.append(move)
                            if new_state.find_difference() < self.find_difference():
                                return new_state
                # checks for moves that involve a stack with at least two blocks.
                # In this loop, each block is moved to table to see if it reduces any difference.
                # Here -1 is j index which indicates move to table
                for i, stack in enumerate(self.initial_stacks):
                    if len(stack) > 1:
                        current_stack, move = self.validate_move(
                            self.initial_stacks, i, -1)
                        new_state = State(
                            current_stack, self.goal_stack, self.total_blocks, copy.copy(self.moves))
                        new_state.moves.append(move)
                        if new_state.find_difference() <= self.find_difference():
                            return new_state

                        # Given a table, starting index, and ending index, this function moves the top block from the starting
                        # stack to the ending stack or the table. It returns the updated table and the move.
            def validate_move(self, initial_stacks, i, j):
                # The starting stack is extracted from the copied table using the index i,
                # and the top block of the starting stack is popped and stored in the top_block variable.
                copied_initial_stacks = copy.deepcopy(initial_stacks)
                from_stack = copied_initial_stacks[i]
                top_block = from_stack.pop()
                # empty list to represent the ending stack.
                to_stack = []

                # If j is less than 0, it means that a new stack is being added to the table,
                # so an empty list is created to represent the ending stack, and the
                # ending stack is appended to the copied stack.
                # with the top_block and the string "Table".
                # J will be -1 so move to table
                if j < 0:
                    copied_initial_stacks.append(to_stack)
                    move = (top_block, 'Table')
                # If j is greater than or equal to 0, it means that the move is being made to an existing stack.
                # The ending stack is extracted from the copied table using the index j, and move is
                # set to be a tuple with the top_block and the top block of the ending stack.
                else:
                    to_stack = copied_initial_stacks[j]
                    move = (top_block, to_stack[len(to_stack)-1])

                to_stack.append(top_block)

                if len(from_stack) == 0:
                    copied_initial_stacks.remove(from_stack)
                return copied_initial_stacks, move

                # Computes the difference between the initial and goal state by comparing each stack
                # in the initial state with each stack in the goal state. The difference is the total number
                # of blocks minus the number of blocks in the same order in both stacks.
            def find_difference(self):
                correct_position = 0
                for initial_tower in self.initial_stacks:
                    for goal_tower in self.goal_stack:
                        i = 0
                        while i < len(initial_tower) and i < len(goal_tower):
                            # check if the current block in initial_tower is equal to the current block
                            # in goal_tower. If the blocks are equal, correct_position is incremented by 1, and i is incremented by 1.
                            if initial_tower[i] == goal_tower[i]:
                                correct_position += 1
                                i += 1
                            else:
                                break
                                # calculation represents the difference between the total number of blocks
                                # and the number of blocks that are in their correct positions in the goal state.
                return self.total_blocks - correct_position

        total_blocks = 0
        for stack in initial_arrangement:
            for block in stack:
                total_blocks += 1
        state = State(initial_arrangement, goal_arrangement, total_blocks)
        total_moves = state.get_goal_state()

        return total_moves
