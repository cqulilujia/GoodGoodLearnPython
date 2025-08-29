import random
import time

class Minesweeper:
    
    def __init__(self, rows, cols, bombs):
        self.rows = rows
        self.cols = cols
        self.bombs = bombs
        self.shown = []
        self.game_board = []
        for i in range(self.rows):
            temp = ["⏹"] * self.cols
            self.game_board.append(temp)
        self.bombs_board = self.place_bombs()
        self.start_time = time.time()
        
    def place_bombs(self):
        bombs_list = []
        for x in range(0, self.rows):
            temp = []
            for y in range(0, self.cols):
                temp.append("⏹")
            bombs_list.append(temp)
        placed_bombs = 0
        while placed_bombs < self.bombs:
            x = random.randint(0, self.rows - 1)
            y = random.randint(0, self.cols - 1)
            if not bombs_list[x][y] == "✦":
                bombs_list[x][y] = "✦"
                placed_bombs +=1
        return bombs_list

    def interact(self):
        move = input("输入坐标(坐标后输入f编辑旗子)(0,0 f): ").lower()
        if "f" in move: #输入 0,0 f
            split = move.split(" ")
            coordinates = split[0]
            row, col = coordinates.split(",")
            row = int(row)
            col = int(col)
            if self.game_board[row][col] == "⏹":
                self.game_board[row][col] = "○"
            elif self.game_board[row][col] == "○":
                self.game_board[row][col] = "⏹"
            else:
                print("位置已被占用")
        else: #输入 0,0
            row, col = move.split(",")
            row = int(row)
            col = int(col)
            if not self.game_board[row][col] == "⏹":
                print("位置已被占用")
                return True
            if self.bombs_board[row][col] == "✦":
                print("爆炸了！ 游戏结束！")
                print(f"以用时间: {self.timer():.2f}秒")
                for i in range(0, len(self.bombs_board)):
                    for j in range(0, len(self.bombs_board[0])):
                        if self.bombs_board[i][j] == "✦":
                            self.game_board[i][j] = "✦"
                self.show_board()
                return False
            else:
                win = True
                rows = len(self.game_board)
                cols = len(self.game_board[0])
                #开始扫雷
                self.count_bombs(row, col)
                self.show_board()
                for i in range(0, rows):
                    for j in range(0, cols):
                        if self.game_board[i][j] == "⏹" and self.bombs_board[i][j] != "✦":
                            win = False
                            break
                if win:
                    print("你赢了!")
                    print(f"以用时间: {self.timer():.2f}秒")
                    return False
        return True
                    
    def show_board(self):
        rows = len(self.game_board)
        cols = len(self.game_board[0])
        print("  ", end="")
        for i in range(0, cols):
            print(f"{i}", end=" ")
        print()
        for i in range(0, rows):
            print(f"{i}", end=" ")
            for j in range(0, cols):
                print(self.game_board[i][j], end=" ")
            print()

    def count_bombs(self, row, col):
        if not [row, col] in self.shown:
            self.shown.append([row, col])
        else:
            return 0
        rows = len(self.game_board)
        cols = len(self.game_board[0])
        bomb_count = 0
        for i in range(row - 1, row + 2):
            for j in range(col - 1, col + 2):
                if i >= 0 and i < rows and j >= 0 and j < cols:
                    if self.bombs_board[i][j] == "✦":
                        bomb_count +=1
        if bomb_count > 0:
            self.game_board[row][col] = bomb_count
        else:
            self.game_board[row][col] = "◻"
        if bomb_count == 0:
            for i in range(row - 1, row + 2):
                for j in range(col - 1, col + 2):
                    if i >= 0 and i < rows and j >= 0 and j < cols and [i, j] not in self.shown:
                        self.count_bombs(i, j)
    def timer(self):
        time_passed = (time.time() - self.start_time)
        return time_passed
                        
    def play(self):
        playing = True
        while playing:
            self.show_board()
            playing = self.interact()
        if input("继续玩?(Y/N): ").lower() == "n":
            return False      
        
def main():
    
    running = True
        
    while running:
        print("选择难度")
        print("1. 低级")
        print("2. 中级")
        print("3. 高级")
        print("4. 设置棋盘")
        print("5. 退出")
        choice = input("输入选择: ")
            
        match choice:
                
            case "1":
                minesweeper_easy = Minesweeper(5, 5, 6)
                minesweeper_easy.play()
                        
            case "2":
                minesweeper_mid = Minesweeper(10, 10, 24)
                minesweeper_mid.play()
                        
            case "3":
                minesweeper_hard = Minesweeper(15, 20, 72)
                minesweeper_hard.play()
                        
            case "4":
                rows = int(input("输入行数: "))
                cols = int(input("输入列数: "))
                bombs = int(input("输入地雷数: "))  
                minesweeper_custom = Minesweeper(rows, cols, bombs)
                minesweeper_custom.play()
            case "5":
                running = False
                    
if __name__ == "__main__":
    main()
