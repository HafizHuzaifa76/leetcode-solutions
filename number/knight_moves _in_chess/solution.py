# The solution is perfect for knight moves and solve many testcases however the solution is not for all testcases of problem

class Solution:
    def canReach(self, start: list[int], target: list[int]) -> bool:
        if start == target:
            return True
        start.append(0)
        queue = [start]
        visited = set()
        visited.add((start[0], start[1]))
        
        moves_number = -1
        while queue:
            position = queue[0]
            moves = self.next_moves(position)

            for move in moves:
                pos = (move[0], move[1])
            
                if pos not in visited:
                    visited.add(pos)
                    queue.append(move)
                    
            if any(move[:2] == target for move in moves):
                moves_number = moves[0][2]
                break
            
            queue.pop(0)
            
        return moves_number % 2 == 0

    def next_moves(self, position: list[int]) -> list[list[int]]:
        moves = [
            [1, 2],
            [2, 1],
            [2, -1],
            [1, -2],
            [-1, -2],
            [-2, -1],
            [-2, 1], 
            [-1, 2],
        ]
        available_moves = []
        
        temp_x = position[0]
        temp_y = position[1]
        num = position[2] + 1

        for move in moves:
            x = temp_x + move[0]
            y = temp_y + move[1]

            if x > 0 and x <= 8 and y > 0 and y <= 8:
                available_moves.append([x, y, num])

        return available_moves
