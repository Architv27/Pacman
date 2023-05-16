# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    """
    "*** YOUR CODE HERE ***"
    # list for tracking the nodes visited
    visited_nodes = []
    # Stack to store the new node
    moves = util.Stack()
    # fetch the start state of pacman
    start_state = problem.getStartState()
    # initialize the starting node of pacman with starting coords, empty actions
    start_node = (start_state,[], 0)
    # push the start node into Stack
    moves.push(start_node)
    
    # create a loop that runs while the stack is not empty
    while (moves.isEmpty()!= True):
        current_state, actions, cost = moves.pop()
        # check if latest node has already been visited
        if current_state not in visited_nodes:
            # if the node is not visited add to the list of visited nodes
            visited_nodes.append(current_state)
            # if the current state is the goal return list of actions
            if problem.isGoalState(current_state):
                return actions
            else:
                successors = problem.getSuccessors(current_state)
                for successor_state, successor_action, successor_cost in successors:
                    total_cost = successor_cost + cost
                    new_action = actions + [successor_action]
                    new_node = (successor_state, new_action, total_cost)
                    moves.push(new_node)
    return actions
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    # list for tracking the nodes visited
    visited_nodes = []
    # Queue to store the new node
    moves = util.Queue()
    start_state = problem.getStartState()
    # initialize the starting node of pacman with starting coords, empty actions    
    start_node = (start_state,[],0)
    # push the start node into Queue
    moves.push(start_node)
    # create a loop that runs while the queue is not empty
    while(moves.isEmpty()!= True):
        current_state, actions, cost = moves.pop()

        if current_state not in visited_nodes:
            visited_nodes.append(current_state)
            
            if problem.isGoalState(current_state):
                return actions
            else:
                successors = problem.getSuccessors(current_state)
                for successor_state, successor_action, successor_cost in successors:
                    new_action = actions + [successor_action]
                    total_cost = cost + successor_cost
                    new_node = (successor_state, new_action, total_cost)
                    moves.push(new_node) 
    return actions
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    moves = util.PriorityQueue()
    # Make an empty list of explored nodes
    visited = []
    # Make an empty list of actions
    action_list = []
    # Place the starting point in the priority queue
    moves.push((problem.getStartState(), action_list), problem)
    # create a loop that runs while the priority queue is not empty
    while moves.isEmpty()!=True:
        node, actions = moves.pop()
        if not node in visited:
            visited.append(node)
            if problem.isGoalState(node):
                return actions
            else:
                successor = problem.getSuccessors(node)
                for successor_state, successor_action, cost in successor:
                    total_actions = actions + [successor_action]
                    total_cost = problem.getCostOfActions(total_actions)
                    moves.push((successor_state, total_actions), total_cost)
    return actions
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    moves = util.PriorityQueue()
    action_list = []
    # list for tracking the nodes visited
    visited = []
    moves.push((problem.getStartState(), action_list), heuristic(problem.getStartState(),problem))
    # create a loop that runs while the priority queue is not empty
    while moves.isEmpty()!=True:
        node, actions = moves.pop()
        if not node in visited:
            visited.append(node)
            if problem.isGoalState(node):
                return actions
            else:
                successor = problem.getSuccessors(node)
                for successor_state, successor_actions, successor_cost in successor:
                    total_actions = actions + [successor_actions]
                    total_cost = problem.getCostOfActions(total_actions) + heuristic(successor_state, problem)
                    moves.push((successor_state, total_actions),total_cost)
    return actions

    
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
