# class BlockWorldAgent:

# 	def __init__(self):
# 		self.moves = []

# 	def solve(self, initial, goal):
# 		self.moves = []
# 		self.initial = initial
# 		self.goal = goal
# 		self.move_block_to_table("B")
# 		return self.moves

# 	def move_block_to_table(self, block):
# 		for pile in self.initial:
# 			if block in pile:
# 				pile.remove(block)
# 				self.moves.append((block, "Table"))
# 				if self.is_pile_valid(pile):
# 					self.move_top_block_to_table(pile)
# 				break

# 	def is_pile_valid(self, pile):
# 		pile_goal = self.get_pile_goal(pile)
# 		return pile == pile_goal

# 	def get_pile_goal(self, pile):
# 		for pile_goal in self.goal:
# 			if set(pile).issubset(set(pile_goal)):
# 				return pile_goal
# 		return []

# 	def move_top_block_to_table(self, pile):
# 		top_block = pile.pop()
# 		self.moves.append((top_block, "Table"))
# 		if pile and not self.is_pile_valid(pile):
# 			self.move_top_block_to_table(pile)


# class BlockWorldAgent:
#     def solve(self, initial, goal):
#         moves = []
#         state = initial[:]
#         while state != goal:
#             # find the blocks that are in the correct position in the goal
#             correct_stacks = []
#             for i, stack in enumerate(state):
#                 if stack == goal[i][:len(stack)]:
#                     correct_stacks.append(i)

#             # find the block that needs to be moved
#             for i, stack in enumerate(state):
#                 if i not in correct_stacks:
#                     block = stack.pop()
#                     moves.append((block, goal[correct_stacks[0]][-1]))
#                     state[correct_stacks[0]].append(block)
#                     break
#         return moves


# class BlockWorldAgent:
#     def solve(self, initial, goal):
#         moves = []
#         state = initial[:]
#         while state != goal:
#             # find the blocks that are in the correct position in the goal
#             correct_stacks = []
#             for i, stack in enumerate(state):
#                 if stack == goal[i][:len(stack)]:
#                     correct_stacks.append(i)

#             # find the block that needs to be moved
#             for i, stack in enumerate(state):
#                 if i not in correct_stacks:
#                     block = stack.pop()
#                     if correct_stacks:
#                         moves.append((block, goal[correct_stacks[0]][-1]))
#                         state[correct_stacks[0]].append(block)
#                     else:
#                         moves.append((block, "Table"))
#                         state.append([block])
#                     break
#         return moves

# class BlockWorldAgent:
#     def solve(self, initial, goal):
#         moves = []
#         state = initial[:]
#         while state != goal:
#             # find the blocks that are in the correct position in the goal
#             correct_stacks = []
#             for i, stack in enumerate(state):
#                 if i < len(goal) and stack == goal[i][:len(stack)]:
#                     correct_stacks.append(i)

#             # find the block that needs to be moved
#             for i, stack in enumerate(state):
#                 if i not in correct_stacks:
#                     block = stack.pop()
#                     target = goal[correct_stacks[0]][-1] if correct_stacks else 'Table'
#                     moves.append((block, target))
#                     if correct_stacks:
#                         state[correct_stacks[0]].append(block)
#                     else:
#                         state.append([block])
#                     break
#         return moves


# class BlockWorldAgent:
#     def solve(self, initial, goal):
#         moves = []
#         state = initial[:]
#         while state != goal:
#             # find the blocks that are in the correct position in the goal
#             correct_stacks = []
#             for i, stack in enumerate(state):
#                 if stack == goal[i][:len(stack)]:
#                     correct_stacks.append(i)

#             # find the block that needs to be moved
#             for i, stack in enumerate(state):
#                 if i not in correct_stacks:
#                     if stack:
#                         block = stack.pop()
#                         for j, g_stack in enumerate(goal):
#                             if g_stack[-1] == block:
#                                 moves.append((block, i, j))
#                                 state[j].append(block)
#                                 break
#         return moves

# class BlockWorldAgent:
#     def solve(self, initial, goal):
#         moves = []
#         state = initial[:]
#         while state != goal:
#             # find the blocks that are in the correct position in the goal
#             correct_stacks = []
#             for i, stack in enumerate(state):
#                 if stack == goal[i][:len(stack)]:
#                     correct_stacks.append(i)

#             # check if we have reached the goal state
#             if len(correct_stacks) == len(goal):
#                 break

#             # find the block that needs to be moved
#             for i, stack in enumerate(state):
#                 if i not in correct_stacks:
#                     if len(stack) == 0:
#                         continue
#                     block = stack.pop()
#                     for j, correct_stack in enumerate(correct_stacks):
#                         if block == goal[correct_stack][-1]:
#                             moves.append((block, goal[correct_stack][-1]))
#                             state[correct_stack].append(block)
#                             break
#                     break
#         return moves


# class BlockWorldAgent:
#     def solve(self, initial, goal):
#         moves = []
#         state = initial[:]
#         while state != goal:
#             correct_stacks = []
#             for i, stack in enumerate(state):
#                 if i < len(goal) and stack == goal[i][:len(stack)]:
#                     correct_stacks.append(i)
#             if not correct_stacks:
#                 return []  # no solution found
#             for i, stack in enumerate(state):
#                 if i not in correct_stacks:
#                     if not stack:  # stack is empty, continue to the next one
#                         continue
#                     block = stack.pop()
#                     moves.append((block, goal[correct_stacks[0]][-1]))
#                     state[correct_stacks[0]].append(block)
#                     break
#         return moves

# class BlockWorldAgent:
#     def solve(self, initial, goal):
# moves = []
# state = initial[:]
# while state != goal:
#     correct_stacks = []
#     for i, stack in enumerate(state):
#         if i < len(goal) and stack == goal[i][:len(stack)]:
#             correct_stacks.append(i)
#     if not correct_stacks:
#         return []  # no solution found
#     for i, stack in enumerate(state):
#         if i not in correct_stacks:
#             if not stack:  # stack is empty, continue to the next one
#                 continue
#             block = stack.pop()
#             for j, g_stack in enumerate(goal):
#                 if g_stack[-1] == block:
#                     dest = j
#                     break
#             if dest != i:
#                 moves.append((block, goal[dest][-1]))
#                 state[dest].append(block)
#                 break
# return moves

class BlockWorldAgent:
    def solve(self, initial, goal):
     #  dict that contains goal state for the blocks

        def goal_state_for_block(towers):
            state = {}
            for tower in towers:
                for i, block in enumerate(tower):
                    if i < len(tower)-1:
                        below = tower[i-1]
                    else:
                        below = "Table"
                    state[block] = below
            return state

        def goal_stacks(towers):
            state = {}
            for tower in towers:
                for i, block in enumerate(tower):
                    if i > 0:
                        above = tower[i-1]
                    else:
                        above = "Table"
                    state[block] = above
            return state

        def place_block(block, from_tower, to_tower, goal_state):
            if len(to_tower) == 0:
                to_tower.append(block)
                return True
            else:
                top_block = to_tower[-1]
                if goal_state[block] == top_block:
                    to_tower.append(block)
                    return True
            return False

        def is_valid_state(towers, goal_state):
            for tower in towers:
                for i in range(1, len(tower)):
                    if goal_state[tower[i]] != tower[i-1]:
                        return False
            return True
            # takes the top block off of the stack with the base block closest to the top and puts it on the table

        def move_to_table(towers):
            min_height = float('inf')
            min_index = None
            for i, tower in enumerate(towers):
                height = len(tower)
                if height > 0 and height < min_height:
                    min_height = height
                    min_index = i
            if min_index is not None:
                block = towers[min_index].pop()
                return (block, "Table")
            return None

        def is_valid_stack(stacks, goal_stacks):
            print("printing stacks from isValidStack", stacks)
            for stack in stacks:
                if len(stack) == 0:
                    continue
                for i in range(1, len(stack)):
                    print(stack)
                    print("If they are not equal, it is not valid stack")
                    if (len(stack) == 1 and "Table" == goal_stacks[stack[1]]):
                        print("Table")
                        print(goal_stacks[stack[i]])
                        return True
                    if (stack[i-1] == goal_stacks[stack[i]]):
                        print(stack[i-1])
                        print(goal_stacks[stack[i]])
                        return True
                    if i == len(stack):
                        break
            print("there are no valid stacks, false")
            return False

        # call the helper function to get the goal state of each block
        goal_stacks = goal_stacks(goal)
        print("Goal state is :", goal_stacks)
        # initial_state = inital_state_for_block(initial)
        # print("Initial state is ", initial_state)
        stacks = initial.copy()
        moves = []
        while stacks != goal:
            print("pritniting stacks from solve method", stacks)
            if (is_valid_stack(stacks, goal_stacks)):
                pass  # either place a block on a valid stack
            else:
                print(stacks)
                move = move_to_table(stacks)
                print("move is ", move)
                stacks.append(move[0])
                print(stacks)

                # find the stack with a base block closest to the top and take the top block off of that stack and put it on the table.

            # for i, stack in enumerate(stacks):
            # 	print("pritniting stack from solve method", stack)
            # 	if (is_valid_stack(stacks, goal_stacks)):
            # 		pass  # either place a block on a valid stack
            # 	else:
            # 		print(stacks)
            # 		move = move_to_table(stacks)
            # 		print("move is ", move)
            # 		stacks.append(move[0])
            # 		print(stacks)

                # find the stack with a base block closest to the top and take the top block off of that stack and put it on the table.


